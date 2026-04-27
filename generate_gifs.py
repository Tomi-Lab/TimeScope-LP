import time
import os
import io
from PIL import Image
from playwright.sync_api import sync_playwright

def record_animation(page, file_path, viewport, duration_sec, interval_ms, gif_path):
    print(f"Recording {gif_path}...")
    page.set_viewport_size(viewport)
    page.goto(f"file:///{os.path.abspath(file_path)}")
    
    frames = []
    start_time = time.time()
    
    # Take screenshots in a loop
    while time.time() - start_start_time() < duration_sec:
        # We need start_time
        pass

# Redefining properly
def record_gif(page, file_path, viewport, duration_sec, gif_path, last_frame_pause=3000):
    print(f"Recording {gif_path}...")
    page.set_viewport_size(viewport)
    
    # Reload page to start animation
    page.goto(f"file:///{os.path.abspath(file_path)}")
    
    frames = []
    start_time = time.time()
    
    # Record for duration_sec
    while time.time() - start_time < duration_sec:
        loop_start = time.time()
        screenshot_bytes = page.screenshot()
        img = Image.open(io.BytesIO(screenshot_bytes)).convert("RGB")
        frames.append(img)
        
        elapsed = time.time() - loop_start
        # Try to maintain ~60ms per frame
        if elapsed < 0.06:
            time.sleep(0.06 - elapsed)
            
    print(f"Captured {len(frames)} frames.")
    
    if frames:
        # Duplicate last frame for the pause
        last_frame = frames[-1]
        extra_frames = int(last_frame_pause / 60)
        for _ in range(extra_frames):
            frames.append(last_frame.copy())
            
        frames[0].save(
            gif_path,
            save_all=True,
            append_images=frames[1:],
            duration=60,
            loop=0,
            optimize=True
        )
        print(f"Saved {gif_path}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 1. Hero
        record_gif(page, "hero_animation.html", {"width": 560, "height": 560}, 10, "assets/hero_animation.gif", 3000)
        
        # 2. Scroll
        record_gif(page, "feature_scroll.html", {"width": 560, "height": 560}, 12, "assets/feature_scroll.gif", 3000)
        
        # 3. Font
        record_gif(page, "feature_font.html", {"width": 560, "height": 560}, 10, "assets/feature_font.gif", 3000)
        
        # 4. Pro
        record_gif(page, "feature_pro.html", {"width": 700, "height": 700}, 12, "assets/feature_pro.gif", 3000)
        
        browser.close()

if __name__ == "__main__":
    main()
