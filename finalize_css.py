import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update general feature-visual logic
# Aspect ratio 4/3 for general features, removes explicit height limitation
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
            aspect-ratio: 4/3;
            transform: translateZ(0); /* Force GPU to clip cleanly */
        }
        
        .feature-visual img {
            width: 100%;
            height: auto;
            margin-top: -85px; /* Pulls the image up hiding browser URL UI perfectly without zooming text */
            position: absolute;
            top: 0;
            object-fit: cover;
            border-radius: 16px;
        }
"""
html = re.sub(r'\.feature-visual \{[\s\S]*?border-radius: 16px;\s*\}', new_css.strip(), html, flags=re.DOTALL)

# 2. Revert the inline extreme transform scales from the img tags
# Hero
html = re.sub(r'(<img src="assets/hero_animation.*?)" style="[^"]*"(>)', r'\1"\2', html)
# Scroll
html = re.sub(r'(<img src="assets/feature_scroll.*?)" style="[^"]*"(.*?>)', r'\1" style="height: auto;"\2', html)
# Font
html = re.sub(r'(<img src="assets/feature_font.*?)" style="[^"]*"(.*?>)', r'\1"\2', html)
# Pro
html = re.sub(r'(<img src="assets/feature_pro.*?)" style="[^"]*"(.*?>)', r'\1"\2', html)

# 3. Give Feature 1 (Scroll) a tall aspect ratio
# We will just add an inline style to that specific feature-visual
scroll_block_old = '<div class="feature-visual">\n                <img src="assets/feature_scroll.webp"'
scroll_block_new = '<div class="feature-visual" style="aspect-ratio: 4/5;">\n                <img src="assets/feature_scroll.webp"'
html = html.replace(scroll_block_old, scroll_block_new)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
