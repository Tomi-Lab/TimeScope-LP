from PIL import Image
import os
import glob

def process_video(input_path, output_path, crop_box):
    img = Image.open(input_path)
    frames = []
    duration = img.info.get('duration', 40)
    
    for i in range(getattr(img, 'n_frames', 1)):
        img.seek(i)
        frame = img.crop(crop_box).copy()
        frames.append(frame)
        
    print(f"{input_path}: extracted {len(frames)} frames.")

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        method=4,
        quality=92
    )
    print(f"Saved {output_path}")

target_folder = r'C:\Users\tomio.otowa\.gemini\antigravity\brain\41c615d8-0c28-4386-bd85-bf7cdd5bedf2'

files = {
    'hero_animation.webp': glob.glob(f'{target_folder}\\hero_animation_new_*.webp')[-1],
    'feature_scroll.webp': glob.glob(f'{target_folder}\\feature_scroll_new_*.webp')[-1],
    'feature_font.webp': glob.glob(f'{target_folder}\\feature_font_new_*.webp')[-1],
    'feature_pro.webp': glob.glob(f'{target_folder}\\feature_pro_new_*.webp')[-1]
}

# Image is 1920x890. Center is 960x445.
# Let's crop a generous 720x720 centered area out of it.
box = (960 - 360, 445 - 360, 960 + 360, 445 + 360)

for dest, src in files.items():
    process_video(src, os.path.join('assets', dest), box)

print("WebPs successfully replaced in assets/")
