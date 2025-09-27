from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time
import json
import sys
import re

# ---------- helpers ----------

def _normalize(s: str) -> str:
    """
    Normalize output text for comparison:
    - convert Unicode ellipsis to three dots
    - collapse >=2 trailing dots to '...'
    - strip whitespace
    - lowercase
    """
    if s is None:
        return ""
    s = s.replace("…", "...")
    s = re.sub(r"\.{2,}$", "...", s)  # .., .... -> ...
    s = s.strip().lower()
    return s

def _is_running_text(s: str) -> bool:
    """
    True if the UI is still in the transient 'running' state.
    Accepts 'running', 'running...', 'running …', etc.
    """
    n = _normalize(s)
    return n == "running" or n == "running..."

def _get_preview_frame(page, timeout_ms=30000):
    """
    Wait for the Ordinals preview iframe and return its Frame object.
    """
    try:
        iframe_el = page.wait_for_selector("iframe[src*='/preview/']", timeout=timeout_ms)
        frame = iframe_el.content_frame()
        if frame:
            return frame
    except PlaywrightTimeoutError:
        return None

    # Fallback: scan existing frames
    for f in page.frames:
        if "/preview/" in f.url:
            return f
    return None


def run_il_in_frame(frame, block_num, poll_timeout_s=20, poll_interval_s=0.25):
    """
    Trigger runIL(block_num) inside the /preview/ frame (no visible UI required)
    and poll #ilOutput until JSON or a terminal string appears (or timeout).

    Returns (block_str, minted_inscription_or_status)
    """
    il_output = frame.locator("#ilOutput")

    # Ensure the output node exists (it's present even when hidden)
    try:
        il_output.wait_for(state="attached", timeout=5000)
    except PlaywrightTimeoutError:
        # Try revealing the fallback once, then re-check
        try:
            frame.evaluate("() => { if (typeof window.showFallback==='function') window.showFallback(); }")
            il_output.wait_for(state="attached", timeout=3000)
        except Exception:
            return (str(block_num), "NO_OUTPUT_NODE")

    # Kick off computation inside the frame
    try:
        frame.evaluate(
            """async (B) => {
                // Clear/set a transient status like the UI would
                const out = document.getElementById('ilOutput');
                if (out) out.textContent = 'running…';

                // Preferred path: direct function
                if (typeof window.runIL === 'function') {
                    await window.runIL(B);
                    return 'CALL_RUNIL';
                }

                // Fallback 1: simulate the button path programmatically
                const inp = document.getElementById('blockIL');
                const btn = document.getElementById('ilButton');
                if (inp) inp.value = String(B);
                if (btn && typeof btn.click === 'function') {
                    btn.click();
                    return 'CLICK_BTN';
                }

                // Fallback 2: reveal classic panel, then try again
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

    # Poll until JSON or terminal text (or timeout)
    start = time.time()
    final_text = ""

    while True:
        try:
            final_text = (il_output.inner_text() or "").strip()
        except Exception:
            final_text = ""

        if final_text.startswith("{"):  # JSON -> done
            break

        if _is_running_text(final_text):
            if time.time() - start > poll_timeout_s:
                final_text = "TIMEOUT_RUNNING"
                break
            time.sleep(poll_interval_s)
            continue

        if final_text:  # non-empty terminal text -> done
            break

        if time.time() - start > poll_timeout_s:
            final_text = "TIMEOUT_NO_OUTPUT"
            break
        time.sleep(poll_interval_s)

    # Some environments return quoted strings; strip them
    if final_text.startswith('"') and final_text.endswith('"'):
        final_text = final_text[1:-1]

    # Parse JSON if present
    try:
        data = json.loads(final_text)
        minted_str = data.get("mintedInscription", "error")
        block_str  = str(data.get("block", block_num))
        return (block_str, minted_str)
    except Exception:
        # Not JSON; return raw text
        return (str(block_num), final_text)


# ---------- main ----------

def main():
    # Any inscription URL that contains the same delegate logic
    url = "https://ordinals.com/inscription/40820a6e4ed67a1123e7d3272db9fc8ba6f8ea06f55412993d6f86408bceae90i0"

    print("Block,MintedInscription")
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

        # Iterate your desired range
        start_b, end_b = 830500, 830505  # inclusive
        for b in range(start_b, end_b + 1):
            try:
                blk, minted = run_il_in_frame(preview, b, poll_timeout_s=20, poll_interval_s=0.25)
            except PlaywrightTimeoutError:
                blk, minted = (str(b), "IFRAME_TIMEOUT")
            except Exception as e:
                blk, minted = (str(b), f"EXC_{type(e).__name__}")

            print(f"{blk},{minted}")
            sys.stdout.flush()

        browser.close()

if __name__ == "__main__":
    main()
