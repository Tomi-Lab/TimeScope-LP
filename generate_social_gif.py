import time
import os
import io
from PIL import Image
from playwright.sync_api import sync_playwright

def record_gif(page, file_path, viewport, record_ms, gif_path):
    print(f"Recording {gif_path}...")
    page.set_viewport_size(viewport)
    
    page.goto(f"file:///{os.path.abspath(file_path)}")
    
    frames = []
    start_time = time.time()
    
    # 4 seconds recording
    while time.time() - start_time < record_ms / 1000.0:
        loop_start = time.time()
        screenshot_bytes = page.screenshot()
        img = Image.open(io.BytesIO(screenshot_bytes)).convert("RGB")
        frames.append(img)
        
        elapsed = time.time() - loop_start
        if elapsed < 0.05:
            time.sleep(0.05 - elapsed)
            
    print(f"Captured {len(frames)} frames.")
    
    if frames:
        frames[0].save(
            gif_path,
            save_all=True,
            append_images=frames[1:],
            duration=50,
            loop=0,
            optimize=True
        )
        print(f"Saved {gif_path}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Timeline:
        # 0-400ms: Enter
        # 400-1400ms: Drag
        # 1400-1700ms: Pre-pop wait
        # 1700-2300ms: Pop animation
        # 2300-2800ms: Post-pop wait
        # 2800-3400ms: Shrink + Tray Enter
        # 3400-4400ms: Pulse hold
        # Total ~4400ms
        record_gif(page, "social_animation.html", {"width": 720, "height": 600}, 4400, "assets/social_promo.gif")
        
        browser.close()

if __name__ == "__main__":
    main()
