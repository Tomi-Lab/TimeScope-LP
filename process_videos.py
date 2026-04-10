from PIL import Image
import os

def process_video(input_path, output_path, crop_box, add_fade=False):
    img = Image.open(input_path)
    frames = []
    duration = img.info.get('duration', 30)
    
    for i in range(getattr(img, 'n_frames', 1)):
        img.seek(i)
        frame = img.crop(crop_box).copy()
        frames.append(frame)
        
    print(f"{input_path}: extracted {len(frames)} frames. Target Box: {crop_box}")

    if add_fade and len(frames) > 0:
        last_frame = frames[-1].convert("RGBA").copy()
        fade_color = (252, 252, 253)
        for i in range(1, 13):
            opacity = int((i / 12) * 255)
            overlay = Image.new("RGBA", last_frame.size, (*fade_color, opacity))
            fade_frame = Image.alpha_composite(last_frame, overlay)
            frames.append(fade_frame)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        method=6,
        quality=90
    )
    print(f"Saved {output_path}")

# Original Sizes
# hero       (750, 734)
# scroll     (750, 734)
# font       (750, 734)
# pro        (972, 888)

# Center of 750x734 is 375. Width 500 is (125, 625), cropping out pink extensions heavily.
# Top UI is ~80px. Height 600 is (80, 680)

# We want 560x560 for hero, scroll, font
box_standard = (95, 80, 655, 640) 

# Pro was recorded at 972x888. Center 486.
box_pro = (136, 80, 836, 780) # 700x700 

process_video('assets/hero_animation.webp', 'assets/hero_animation_clean.webp', box_standard)
process_video('assets/feature_scroll.webp', 'assets/feature_scroll_clean.webp', box_standard)
process_video('assets/feature_font.webp', 'assets/feature_font_clean.webp', box_standard)
process_video('assets/feature_pro.webp', 'assets/feature_pro_clean.webp', box_pro, add_fade=True)

# Replace originals
os.replace('assets/hero_animation_clean.webp', 'assets/hero_animation.webp')
os.replace('assets/feature_scroll_clean.webp', 'assets/feature_scroll.webp')
os.replace('assets/feature_font_clean.webp', 'assets/feature_font.webp')
os.replace('assets/feature_pro_clean.webp', 'assets/feature_pro.webp')
print("Replacement complete.")
