import time
import os
import io
from PIL import Image
from playwright.sync_api import sync_playwright

def record_gif(page, file_path, viewport, duration_sec, gif_path, last_frame_pause=3000):
    print(f"Recording {gif_path}...")
    page.set_viewport_size(viewport)
    
    page.goto(f"file:///{os.path.abspath(file_path)}")
    
    frames = []
    start_time = time.time()
    
    while time.time() - start_time < duration_sec:
        loop_start = time.time()
        screenshot_bytes = page.screenshot()
        img = Image.open(io.BytesIO(screenshot_bytes)).convert("RGB")
        frames.append(img)
        
        elapsed = time.time() - loop_start
        if elapsed < 0.05:
            time.sleep(0.05 - elapsed)
            
    print(f"Captured {len(frames)} frames.")
    
    if frames:
        last_frame = frames[-1]
        extra_frames = int(last_frame_pause / 50)
        for _ in range(extra_frames):
            frames.append(last_frame.copy())
            
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
        
        # Capture for 4 seconds (400ms start + 2400ms drag + 100ms pop delay + 600ms pop animation = 3500ms)
        # We capture for 4 seconds to be safe.
        record_gif(page, "hero_animation_tmp.html", {"width": 560, "height": 560}, 4, "assets/hero_animation.gif", 3000)
        
        browser.close()

if __name__ == "__main__":
    main()
