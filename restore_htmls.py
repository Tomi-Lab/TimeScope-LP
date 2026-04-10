import re

# 1. Strip the HTML scales completely
def strip_scales(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # remove scaling
    content = re.sub(r'transform:\s*scale\([^)]+\);\s*transform-origin:\s*center;\s*', '', content)
    
    # ensure body is not explicitly overflowing hidden with 100vw/vh unless it was default
    # actually reverting to 100vh only is safer for browser_subagent
    content = content.replace("width: 100vw; height: 100vh; overflow: hidden; ", "height: 100vh; ")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

strip_scales("hero_animation.html")
strip_scales("feature_scroll.html")
strip_scales("feature_font.html")
strip_scales("feature_pro.html")

# 2. Fix feature_pro.html specifically for smooth looping and caption position
with open("feature_pro.html", "r", encoding="utf-8") as f:
    pro = f.read()

# Fix caption position to be within the box
pro = pro.replace("bottom: -50px;", "bottom: -20px;")

# Add fade out classes
new_css = """
        .calendar-wrapper {
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: opacity 0.4s ease;
        }
        .calendar-wrapper.fade-out {
            opacity: 0 !important;
        }
"""
pro = re.sub(r'\.calendar-wrapper\s*\{[^\}]+\}', new_css.strip(), pro)

# Update Javascript
old_js = """
                                // Hold for reading
                                setTimeout(() => {
                                    wrapper.classList.remove('show-range1', 'show-range2', 'show-badges', 'show-delta');
                                    cap.classList.remove('show');
                                    setTimeout(playLoop, 400); 
                                }, 1300); 
"""
new_js = """
                                // Hold for reading
                                setTimeout(() => {
                                    wrapper.classList.add('fade-out');
                                    setTimeout(() => {
                                        wrapper.classList.remove('show-range1', 'show-range2', 'show-badges', 'show-delta', 'fade-out');
                                        cap.classList.remove('show');
                                        setTimeout(playLoop, 300);
                                    }, 400);
                                }, 2200); // 2.2s hold for max readability
"""
pro = pro.replace(old_js, new_js)

with open("feature_pro.html", "w", encoding="utf-8") as f:
    f.write(pro)
