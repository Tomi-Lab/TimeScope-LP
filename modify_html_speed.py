import re
files = ['hero_animation.html', 'feature_scroll.html', 'feature_font.html', 'feature_pro.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add frame forcer (a tiny invisible clock that updates every 40ms to force browser to re-render)
    if 'id="frame-forcer"' not in content:
        forcer = '<div id="frame-forcer" style="position:fixed;top:0;left:0;opacity:0.01;z-index:9999;font-size:1px;">0</div>\n<script>setInterval(()=>document.getElementById("frame-forcer").innerText=Date.now(), 40);</script>\n</body>'
        content = content.replace('</body>', forcer)
    
    # 2. Slow down logic specifically
    if f == 'hero_animation.html':
        content = content.replace('const dragDuration = 1800;', 'const dragDuration = 3000;')
        content = content.replace('const pauseAtEnd = 2400;', 'const pauseAtEnd = 4500;')
        content = content.replace('const delayBeforePop = 100;', 'const delayBeforePop = 200;')
    elif f == 'feature_scroll.html':
        content = content.replace('setTimeout(playLoop, 1200);', 'setTimeout(playLoop, 2000);')
        content = content.replace('}, 3500);', '}, 5000);')
        content = content.replace('}, 1200); // Wait for scroll', '}, 2000); // Wait for scroll')
        content = content.replace('}, 1400); // Wait for expand', '}, 2000); // Wait for expand')
        content = content.replace('}, 800);', '}, 1200);')
        content = content.replace('transition: height 1.2s', 'transition: height 1.8s')
        content = content.replace('transition: transform 1.2s', 'transition: transform 1.8s')
    elif f == 'feature_font.html':
        content = content.replace('transition: transform 0.7s', 'transition: transform 1.2s')
        content = content.replace('}, 500);', '}, 800);')
        content = content.replace('}, 1800);', '}, 3500);')
        content = content.replace('}, 1200);', '}, 2000);')
        content = content.replace('}, 600);', '}, 1000);')
    elif f == 'feature_pro.html':
        content = content.replace('transition: background-color 0.4s', 'transition: background-color 0.8s')
        content = content.replace('transition: max-height 0.8s', 'transition: max-height 1.4s')
        content = content.replace('}, 1800);', '}, 4000);')
        content = content.replace('}, 1200);', '}, 2000);')
        content = content.replace('}, 800);', '}, 1500);')
        content = content.replace('}, 500);', '}, 1000);')
        content = content.replace('}, 400);', '}, 800);')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Done modifying HTMLs')
