import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update general feature-visual logic back to simple bounds
new_css = """
        .feature-visual {
            flex: 1.2;
            display: flex;
            align-items: center;
            justify-content: center;
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            overflow: hidden;
            border-radius: 16px;
        }
        
        .feature-visual img {
            width: 100%;
            height: auto;
            border-radius: 16px;
            /* Object fit / bounds adjusted per feature below if needed, but mostly native is fine now! */
            display: block;
        }
"""
html = re.sub(r'\.feature-visual \{[\s\S]*?transform: translateZ\(0\);\s*\}', new_css.split('}')[0] + "}", html, flags=re.DOTALL)
html = re.sub(r'\.feature-visual img \{[\s\S]*?border-radius: 16px;\s*\}', new_css.split('}')[1].split('.feature-visual img {')[1] + "}", html, flags=re.DOTALL)

# 2. Revert the inline extreme transform scales and negative margins!
# Hero
html = re.sub(r'(<img src="assets/hero_animation.*?)" style="[^"]*"(>)', r'\1"\2', html)
# Scroll
html = re.sub(r'(<img src="assets/feature_scroll.*?)" style="[^"]*"(.*?>)', r'\1" style="width: 100%; height: auto;"\2', html)
# Font
html = re.sub(r'(<img src="assets/feature_font.*?)" style="[^"]*"(.*?>)', r'\1" style="width: 100%; height: auto;"\2', html)
# Pro
html = re.sub(r'(<img src="assets/feature_pro.*?)" style="[^"]*"(.*?>)', r'\1" style="width: 100%; height: auto;"\2', html)

# 3. Give Feature 1 (Scroll) a tall aspect ratio layout 
# We'll override the container so the image can visually scroll completely
scroll_block_old = '<div class="feature-visual" style="aspect-ratio: 4/5;">'
scroll_block_new = '<div class="feature-visual" style="width: 100%;">'
html = html.replace(scroll_block_old, scroll_block_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
