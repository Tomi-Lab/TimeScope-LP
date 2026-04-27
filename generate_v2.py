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
        
        # 400ms start + 1000ms drag + 400ms pre-pop + 600ms pop anim + 1200ms hold = 3600ms
        record_gif(page, "hero_animation_v2.html", {"width": 560, "height": 560}, 3600, "assets/hero_animation_v2.gif")
        
        browser.close()

if __name__ == "__main__":
    main()
