import re

def process_file(filename, scale_value):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject body styling strictly to 100vw/vh and fcfcfd (unless it's hero background)
    # Actually they are already centered. We just need to ensure body is full bleed.
    if "body { margin: 0; background-color: #fcfcfd" in content:
        content = content.replace(
            "body { margin: 0; background-color: #fcfcfd; height: 100vh;",
            "body { margin: 0; background-color: #fcfcfd; width: 100vw; height: 100vh; overflow: hidden;"
        )
    
    # 2. Add scaling to the wrapper
    # We will just inject it into the calendar-wrapper class style
    content = re.sub(
        r'(\.calendar-wrapper\s*\{[^\}]+justify-content:\s*center;\s*)',
        rf'\1transform: scale({scale_value});\n            transform-origin: center;\n        ',
        content
    )

    # 3. Add 1.5s delay to window load
    content = content.replace("window.addEventListener('load', playLoop);", "window.addEventListener('load', () => setTimeout(playLoop, 1500));")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

process_file("hero_animation.html", "1.2")
process_file("feature_scroll.html", "0.8")
process_file("feature_font.html", "1.1")
process_file("feature_pro.html", "1.4")
