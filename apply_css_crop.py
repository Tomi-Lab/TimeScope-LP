import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove mix-blend-mode completely to fix "blue tint" and make it normal blending.
# Update the basic .feature-visual img CSS
new_css = """
        .feature-visual {
            flex: 1.2;
            display: flex;
            align-items: center;
            justify-content: center;
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            /* CRITICAL CROP SETTINGS */
            overflow: hidden;
            border-radius: 16px;
            position: relative;
            transform: translateZ(0); /* Force GPU to clip cleanly */
        }
        
        .feature-visual img {
            width: 100%;
            height: 100%;
            object-fit: cover; /* stretches image to completely fill the box */
            object-position: center 55%; /* shifts image up slightly to miss the URL bar */
            border-radius: 16px;
            /* mix-blend-mode removed to preserve exact white colors #fcfcfd */
        }
"""
html = re.sub(r'\.feature-visual \{[\s\S]*?mix-blend-mode: multiply;.*?\}', new_css.strip(), html, flags=re.DOTALL)


# 2. Add specific scaling overrides per feature to crop the bad UI exactly out
# We will inject specific IDs or styles
old_scroll = '<img src="assets/feature_scroll.webp" alt="Scroll Multi-Months">'
new_scroll = '<img src="assets/feature_scroll.webp" alt="Scroll Multi-Months" style="transform: scale(1.6); object-position: center 60%;">'
html = html.replace(old_scroll, new_scroll)

old_font = '<img src="assets/feature_font.webp" alt="Adjust Font Size">'
new_font = '<img src="assets/feature_font.webp" alt="Adjust Font Size" style="transform: scale(1.5); object-position: center 60%;">'
html = html.replace(old_font, new_font)

old_pro = '<img src="assets/feature_pro.webp" alt="Compare Durations">'
new_pro = '<img src="assets/feature_pro.webp" alt="Compare Durations" style="transform: scale(1.8); object-position: center 60%;">'
html = html.replace(old_pro, new_pro)

# 3. Hero image crop
old_hero = '<img src="assets/hero_animation.webp" alt="TimeScope Hero UI" style="width: 100%; height: 100%; object-fit: cover;">'
new_hero = '<img src="assets/hero_animation.webp" alt="TimeScope Hero UI" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.4); object-position: center 65%; border-radius: 16px;">'
html = html.replace(old_hero, new_hero)

# Apply fixes directly
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
