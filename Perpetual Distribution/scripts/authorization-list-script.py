from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time
import json
import sys
import re

def _normalize(s: str) -> str:
    """
    Normalize output text for comparison:
    - convert Unicode ellipsis to three dots
    - collapse 2+ trailing dots to '...'
    - strip whitespace
    - lowercase
    """
    if s is None:
        return ""
    s = s.replace("…", "...")
    s = re.sub(r"\.{2,}$", "...", s)  # running.., running..... -> running...
    s = s.strip().lower()
    return s

def _is_running_text(s: str) -> bool:
    """
    Returns True if the UI is still in the transient 'running' state.
    Accepts 'running', 'running...', 'running …', etc.
    """
    n = _normalize(s)
    return n == "running" or n == "running..."

def _get_preview_frame(page, timeout_ms=30000):
    """
    Waits for the Ordinals preview iframe and returns its Frame object.
    """
    try:
        # Wait for the iframe element, then resolve to its frame
        iframe_el = page.wait_for_selector("iframe[src*='/preview/']", timeout=timeout_ms)
        frame = iframe_el.content_frame()
        if frame:
            return frame
    except PlaywrightTimeoutError:
        return None

    # Fallback: try to find by URL substring
    for f in page.frames:
        if "/preview/" in f.url:
            return f
    return None

def run_al_in_frame(frame, block_num, poll_timeout_s=20, poll_interval_s=0.25):
    """
    Kicks off runAL(block_num) inside the /preview/ frame (no reliance on
    visible inputs/buttons) and polls #alOutput for JSON or a terminal string.
    Returns (block_str, authorized_parent_str or status).
    """
    al_output = frame.locator("#alOutput")

    # Ensure the output node exists (even if hidden)
    try:
        al_output.wait_for(state="attached", timeout=5000)
    except PlaywrightTimeoutError:
        # Try to reveal fallback UI once, then check again
        try:
            frame.evaluate("() => { if (typeof window.showFallback==='function') window.showFallback(); }")
            al_output.wait_for(state="attached", timeout=3000)
        except Exception:
            return (str(block_num), "NO_OUTPUT_NODE")

    # Kick off computation inside the frame without relying on visible UI
    try:
        frame.evaluate(
            """async (B) => {
                // set a transient status like the UI would
                const out = document.getElementById('alOutput');
                if (out) out.textContent = 'running…';

                // Preferred: direct function
                if (typeof window.runAL === 'function') {
                    await window.runAL(B);
                    return 'CALL_RUNAL';
                }

                // Fallback: simulate the button path programmatically
                const inp = document.getElementById('blockAL');
                const btn = document.getElementById('alButton');
                if (inp) inp.value = String(B);
                if (btn && typeof btn.click === 'function') {
                    btn.click();
                    return 'CLICK_BTN';
                }

                // Last resort: reveal panel and try again
                if (typeof window.showFallback === 'function') {
                    window.showFallback();
                    if (inp) inp.value = String(B);
                    if (btn && typeof btn.click === 'function') {
                        btn.click();
                        return 'SHOWFALLBACK_AND_CLICK';
                    }
                }
                return 'NO_API';
            }""",
            block_num,
        )
    except Exception as e:
        return (str(block_num), f"EVAL_EXC_{type(e).__name__}")

    # Poll output for JSON or terminal text
    start = time.time()
    result_text = ""

    while True:
        try:
            result_text = (al_output.inner_text() or "").strip()
        except Exception:
            result_text = ""

        # JSON -> done
        if result_text.startswith("{"):
            break

        # Keep waiting while 'running…'
        if _is_running_text(result_text):
            if time.time() - start > poll_timeout_s:
                result_text = "TIMEOUT_RUNNING"
                break
            time.sleep(poll_interval_s)
            continue

        # Any non-empty, non-running terminal text -> done
        if result_text:
            break

        # Empty output -> keep polling until timeout
        if time.time() - start > poll_timeout_s:
            result_text = "TIMEOUT_NO_OUTPUT"
            break
        time.sleep(poll_interval_s)

    # Parse JSON if present
    try:
        data = json.loads(result_text)
        blk_str = str(data.get("block", block_num))
        parent_val = data.get("authorizedParent", "invalid")
        return (blk_str, str(parent_val))
    except Exception:
        return (str(block_num), result_text)

def main():
    url = "https://ordinals.com/inscription/40820a6e4ed67a1123e7d3272db9fc8ba6f8ea06f55412993d6f86408bceae90i0"

    start_block = 909216
    end_block   = 909900

    print("Block,AuthorizedParent")
    sys.stdout.flush()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Avoid 'networkidle' (site does background fetches)
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            preview = _get_preview_frame(page, timeout_ms=30000)
            if not preview:
                print("ALL,NO_PREVIEW_FRAME")
                browser.close()
                return
        except PlaywrightTimeoutError:
            print("ALL,NAV_TIMEOUT")
            browser.close()
            return

        # Loop blocks without reloading the page (stable & fast)
        for b in range(start_block, end_block + 1):
            try:
                blk, par = run_al_in_frame(preview, b, poll_timeout_s=20, poll_interval_s=0.25)
            except PlaywrightTimeoutError:
                blk, par = (str(b), "IFRAME_TIMEOUT")
            except Exception as e:
                blk, par = (str(b), f"EXC_{type(e).__name__}")

            print(f"{blk},{par}")
            sys.stdout.flush()

        browser.close()

if __name__ == "__main__":
    main()
