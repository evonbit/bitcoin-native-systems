# Configure the inscription URL and block number range as needed.

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time
import json
import sys
import re

def _normalize(s: str) -> str:
    if s is None:
        return ""
    s = s.replace("…", "...")
    s = re.sub(r"\.{2,}$", "...", s)
    s = s.strip().lower()
    return s

def _is_running_text(s: str) -> bool:
    n = _normalize(s)
    return n == "running" or n == "running..."

def _get_preview_frame(page, timeout_ms=30000):
    try:
        iframe_el = page.wait_for_selector("iframe[src*='/preview/']", timeout=timeout_ms)
        frame = iframe_el.content_frame()
        if frame:
            return frame
    except PlaywrightTimeoutError:
        return None
    for f in page.frames:
        if "/preview/" in f.url:
            return f
    return None

def run_al_in_frame(frame, block_num, poll_timeout_s=20, poll_interval_s=0.25):
    al_output = frame.locator("#alOutput")
    try:
        al_output.wait_for(state="attached", timeout=5000)
    except PlaywrightTimeoutError:
        try:
            frame.evaluate("() => { if (typeof window.showFallback==='function') window.showFallback(); }")
            al_output.wait_for(state="attached", timeout=3000)
        except Exception:
            return (str(block_num), "NO_OUTPUT_NODE")

    try:
        frame.evaluate(
            """async (B) => {
                const out = document.getElementById('alOutput');
                if (out) out.textContent = 'running…';
                if (typeof window.runAL === 'function') {
                    await window.runAL(B);
                    return 'CALL_RUNAL';
                }
                const inp = document.getElementById('blockAL');
                const btn = document.getElementById('alButton');
                if (inp) inp.value = String(B);
                if (btn && typeof btn.click === 'function') {
                    btn.click();
                    return 'CLICK_BTN';
                }
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

    start = time.time()
    result_text = ""

    while True:
        try:
            result_text = (al_output.inner_text() or "").strip()
        except Exception:
            result_text = ""

        if result_text.startswith("{"):
            break
        if _is_running_text(result_text):
            if time.time() - start > poll_timeout_s:
                result_text = "TIMEOUT_RUNNING"
                break
            time.sleep(poll_interval_s)
            continue
        if result_text:
            break
        if time.time() - start > poll_timeout_s:
            result_text = "TIMEOUT_NO_OUTPUT"
            break
        time.sleep(poll_interval_s)

    if result_text.startswith('"') and result_text.endswith('"'):
        result_text = result_text[1:-1]

    try:
        data = json.loads(result_text)
        block_str = str(data.get("block", block_num))
        parent_str = data.get("authorizedParent", "invalid")
        return (block_str, parent_str)
    except Exception:
        return (str(block_num), result_text)

def main():
    # Inscription ID
    url = "https://ordinals.com/inscription/40820a6e4ed67a1123e7d3272db9fc8ba6f8ea06f55412993d6f86408bceae90i0"

    print("Block,AuthorizedParent")
    sys.stdout.flush()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
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

        # Block number range
        start_b, end_b = 909216, 909900
        for b in range(start_b, end_b + 1):
            try:
                blk, parent = run_al_in_frame(preview, b, poll_timeout_s=20, poll_interval_s=0.25)
            except PlaywrightTimeoutError:
                blk, parent = (str(b), "IFRAME_TIMEOUT")
            except Exception as e:
                blk, parent = (str(b), f"EXC_{type(e).__name__}")

            print(f"{blk},{parent}")
            sys.stdout.flush()

        browser.close()

if __name__ == "__main__":
    main()
