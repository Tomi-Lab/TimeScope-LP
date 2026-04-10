from PIL import Image

def analyze(path):
    try:
        img = Image.open(path)
        frames = getattr(img, 'n_frames', 1)
        print(f"{path} -> Size: {img.size}, Frames: {frames}")
    except Exception as e:
        print(f"Error on {path}: {e}")

analyze("assets/feature_pro.webp")
analyze("assets/hero_animation.webp")
analyze("assets/feature_scroll.webp")
analyze("assets/feature_font.webp")
