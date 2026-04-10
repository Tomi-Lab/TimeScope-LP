from PIL import Image

def test_crop():
    try:
        # Open source WebP
        img = Image.open('assets/hero_animation.webp')
        w, h = img.size
        print(f"Original size: {w}x{h}")
        
        # Test crop: Remove top 80px (URL bar), remove right 100px (Pink extension icon), remove bottom/left margins slightly
        box = (20, 80, w - 100, h - 20)
        
        frames = []
        for i in range(getattr(img, 'n_frames', 1)):
            img.seek(i)
            # Crop to isolated component
            frames.append(img.crop(box).copy())
            
        print(f"Cropped {len(frames)} frames to {frames[0].size}")
    except Exception as e:
        print("Error:", e)

test_crop()
