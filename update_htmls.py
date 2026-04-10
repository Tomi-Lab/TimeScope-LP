import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        if old not in content and not hasattr(old, "pattern"):
            print(f"Warning: {old} not found in {filename}")
        if hasattr(old, "pattern"):
            content = re.sub(old, new, content)
        else:
            content = content.replace(old, new)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. hero_animation.html
update_file('hero_animation.html', [
    ('background-color: #fcfcfd;', 'background-color: #ffffff;'),
    ('const dragDuration = 800;', 'const dragDuration = 1800;'),
    ('const pauseAtEnd = 1600;', 'const pauseAtEnd = 2400;')
])

# 2. feature_scroll.html
update_file('feature_scroll.html', [
    ('background-color: #fcfcfd;', 'background-color: #ffffff;'),
    # Scale entire wrapper for visibility
    ('flex-direction: column;\n            align-items: center;', 'flex-direction: column;\n            align-items: center;\n            transform: scale(0.7);\n            transform-origin: center center;'),
    # Slow down animation
    ('transition: height 0.8s', 'transition: height 1.2s'),
    ('setTimeout(() => {\n                // Step 2: Expand (0.8s)\n                win.classList.add(\'expanded\');\n                \n                setTimeout(() => {\n                    // Step 3: Light scroll after expand finishes\n                    months.classList.add(\'scrolled\');\n                    \n                    // Step 5: Show caption 0.1s after expand finishes\n                    setTimeout(() => {\n                        cap.classList.add(\'show\');\n                    }, 100);\n\n                    // Step 4: Stop and wait 0.8s. \n                    // Scroll takes ~0.6s, so wait 1400ms from here to have clear static time\n                    // 1400ms guarantees ~0.8s of pure static time\n                    setTimeout(() => {\n                        // Step 6: Loop reset\n                        win.classList.remove(\'expanded\');\n                        cap.classList.remove(\'show\');\n                        months.classList.remove(\'scrolled\');\n                        setTimeout(playLoop, 900); // wait for UI to retract before starting again\n                    }, 1400); \n\n                }, 800); // matches the 0.8s expand transition\n            }, 500); // Step 1: Initial wait (0.5s)', 
     '''setTimeout(() => {
                win.classList.add('expanded');
                setTimeout(() => {
                    months.classList.add('scrolled');
                    setTimeout(() => {
                        cap.classList.add('show');
                    }, 150);
                    setTimeout(() => {
                        win.classList.remove('expanded');
                        cap.classList.remove('show');
                        months.classList.remove('scrolled');
                        setTimeout(playLoop, 1200); 
                    }, 2200); 
                }, 1200); 
            }, 800);''')
])

# 3. feature_font.html
font_caption_old = """        .caption {
            position: absolute;
            bottom: -20px;
            font-size: 1.1rem;
            font-weight: 600;
            color: #18181b;
            background: #ffffff;
            padding: 10px 24px;
            border-radius: 100px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05), 0 0 0 1px rgba(0,0,0,0.03);
            opacity: 0;
            transform: translateY(10px);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }
        .caption.show {
            opacity: 1;
            transform: translateY(0);
        }"""
font_caption_new = """        .caption {
            position: absolute;
            top: 85%;
            left: 50%;
            transform: translate(-50%, 20px);
            width: max-content;
            font-size: 1.1rem;
            font-weight: 700;
            color: #18181b;
            background: #ffffff;
            padding: 14px 28px;
            border-radius: 100px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.15), 0 0 0 1px rgba(0,0,0,0.05);
            opacity: 0;
            transition: opacity 0.4s ease, transform 0.4s ease;
            z-index: 100;
        }
        .caption.show {
            opacity: 1;
            transform: translate(-50%, 0);
        }"""
update_file('feature_font.html', [
    ('background-color: #fcfcfd;', 'background-color: #ffffff;'),
    (font_caption_old, font_caption_new),
    # slower transitions
    ('transition: transform 0.4s', 'transition: transform 0.7s'),
    ('''            setTimeout(() => {
                // 1. Shrink to Small
                win.className = 'calendar-window size-small';
                
                // 2. Trigger Large AFTER: 0.4s transition + 0.3s hold = 700ms
                setTimeout(() => {
                    win.className = 'calendar-window size-large';
                    
                    // 3. Trigger Caption AFTER: 0.4s transition + 0.6s hold = 1000ms
                    setTimeout(() => {
                        cap.classList.add('show');
                        
                        // 4. Hold caption visible for 0.7s before resetting
                        setTimeout(() => {
                            win.style.transition = 'transform 0.3s ease'; 
                            win.className = 'calendar-window size-normal';
                            cap.classList.remove('show');
                            
                            setTimeout(() => {
                                win.style.transition = ''; 
                                playLoop();
                            }, 300); // 0.3s retract time

                        }, 700); 

                    }, 1000); 

                }, 700); 

            }, 400); // Initial hold''',
    '''            setTimeout(() => {
                win.className = 'calendar-window size-small';
                setTimeout(() => {
                    win.className = 'calendar-window size-large';
                    setTimeout(() => {
                        cap.classList.add('show');
                        setTimeout(() => {
                            win.style.transition = 'transform 0.4s ease'; 
                            win.className = 'calendar-window size-normal';
                            cap.classList.remove('show');
                            setTimeout(() => {
                                win.style.transition = ''; 
                                playLoop();
                            }, 500); 
                        }, 1800); 
                    }, 1200); 
                }, 1200); 
            }, 600);''')
])

# 4. feature_pro.html
pro_caption_old = """        .caption {
            position: absolute;
            bottom: -20px;
            font-size: 1.1rem;
            font-weight: 600;
            color: #18181b;
            background: #ffffff;
            padding: 10px 24px;
            border-radius: 100px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05), 0 0 0 1px rgba(0,0,0,0.03);
            opacity: 0;
            transform: translateY(10px);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }
        .caption.show {
            opacity: 1;
            transform: translateY(0);
        }"""
pro_caption_new = """        .caption {
            position: absolute;
            top: 86%;
            left: 50%;
            transform: translate(-50%, 20px);
            width: max-content;
            font-size: 1.15rem;
            font-weight: 700;
            color: #18181b;
            background: #ffffff;
            padding: 14px 28px;
            border-radius: 100px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.15), 0 0 0 1px rgba(0,0,0,0.05);
            opacity: 0;
            transition: opacity 0.4s ease, transform 0.4s ease;
            z-index: 100;
        }
        .caption.show {
            opacity: 1;
            transform: translate(-50%, 0);
        }"""
# Wait, changing 400->800 everywhere in feature_pro loop
pro_loop_old = """            setTimeout(() => {
                // Range 1
                wrapper.classList.add('show-range1');
                
                setTimeout(() => {
                    // Range 2
                    wrapper.classList.add('show-range2');
                    
                    setTimeout(() => {
                        // Options pop
                        wrapper.classList.add('show-badges');
                        
                        setTimeout(() => {
                            // Delta (+1 day) pop centrally
                            wrapper.classList.add('show-delta');
                            
                            // 1.0s Hold (increased from 0.8s as requested)
                            setTimeout(() => {
                                // Show Caption
                                cap.classList.add('show');
                                
                                // Hold for reading
                                setTimeout(() => {
                                    wrapper.classList.add('fade-out');
                                    setTimeout(() => {
                                        wrapper.classList.remove('show-range1', 'show-range2', 'show-badges', 'show-delta', 'fade-out');
                                        cap.classList.remove('show');
                                        setTimeout(playLoop, 300);
                                    }, 400);
                                }, 2200); // 2.2s hold for max readability

                            }, 1000); 

                        }, 400); 

                    }, 400); 

                }, 400); 

            }, 400);"""
pro_loop_new = """            setTimeout(() => {
                wrapper.classList.add('show-range1');
                setTimeout(() => {
                    wrapper.classList.add('show-range2');
                    setTimeout(() => {
                        wrapper.classList.add('show-badges');
                        setTimeout(() => {
                            wrapper.classList.add('show-delta');
                            setTimeout(() => {
                                cap.classList.add('show');
                                setTimeout(() => {
                                    wrapper.classList.add('fade-out');
                                    setTimeout(() => {
                                        wrapper.classList.remove('show-range1', 'show-range2', 'show-badges', 'show-delta', 'fade-out');
                                        cap.classList.remove('show');
                                        setTimeout(playLoop, 400);
                                    }, 500);
                                }, 2800); 
                            }, 1200); 
                        }, 700); 
                    }, 700); 
                }, 700); 
            }, 600);"""
update_file('feature_pro.html', [
    ('background-color: #fcfcfd;', 'background-color: #ffffff;'),
    (pro_caption_old, pro_caption_new),
    (pro_loop_old, pro_loop_new),
    # Make Delta animations a bit slower too just to complement the flow
    ('0.2s cubic-bezier', '0.3s cubic-bezier'),
    ('0.3s cubic-bezier', '0.4s cubic-bezier')
])

print("Files updated successfully!")
