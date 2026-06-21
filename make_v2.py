import re

with open(r'c:\dev\projects\TimeScope-LP\index.html', 'r', encoding='utf-8') as f:
    original = f.read()

# Extract head and styles
head_match = re.search(r'(<head>.*?</head>)', original, re.DOTALL)
head_content = head_match.group(1) if head_match else '<head></head>'

html_content = f'''<!DOCTYPE html>
<html lang="en">
{head_content}
<body>
    <!-- NAV (Dark Overlay) -->
    <nav>
        <div class="logo" style="display: flex; align-items: center; gap: 8px;">
            <img src="social/StoreLogo_Floating_Dot.png" alt="TimeScope Icon" style="height: 24px; width: auto; border-radius: 4px;">
            TimeScope
        </div>
        <div class="lang-switch">
            <button onclick="setLanguage('en')" id="btn-en" class="active">EN</button>
            <button onclick="setLanguage('ja')" id="btn-ja">JP</button>
        </div>
    </nav>

    <!-- 1. HERO (Dark Theme) -->
    <div class="theme-dark">
        <header class="hero container fade-in" style="padding-top: 140px;">
            <h1 data-i18n="hero.title">See time. Instantly.</h1>
            <p data-i18n="hero.subtitle" style="max-width: 700px; margin: 0 auto 32px; line-height: 1.5; font-size: 1.25rem;">Drag to calculate durations, compare multiple periods, and see exactly how far away any date is.</p>
            
            <div class="hero-actions" style="flex-direction: column; align-items: center; gap: 16px;">
                <div class="cta-wrapper">
                    <a href="ms-windows-store://pdp/?productid=dummy" class="btn btn-primary download-link" data-i18n="hero.cta" style="font-size: 1.1rem; padding: 16px 32px; border-radius: 30px;">Get it from Microsoft Store</a>
                    <div class="microcopy" data-i18n="hero.micro">Available for Windows 10 & 11</div>
                </div>
            </div>
            
            <div class="hero-mockup-wrapper fade-in" style="max-width: 900px;">
                <div class="hero-mockup" style="background-color: #000000; border: 1px solid #333;">
                    <img src="social/DAY1_hero.gif" alt="TimeScope Hero" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
            </div>
        </header>
    </div>

    <!-- 2. FEATURES -->
    <section class="features container" style="padding-top: 140px;">
        
        <!-- Feature 1: Duration -->
        <div class="feature-row fade-in">
            <div class="feature-text">
                <h3 data-i18n="feature.1.title" style="font-size: 2.2rem; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.03em;">Drag to Calculate Durations</h3>
                <p data-i18n="feature.1.desc" style="font-size: 1.1rem; color: var(--light-text-muted); line-height: 1.6;">Just click and drag across the calendar to instantly see the exact number of days between any two dates. Perfect for project planning, trip scheduling, or counting down to major life events without doing the math.</p>
            </div>
            <div class="feature-visual" style="box-shadow: 0 10px 40px rgba(0,0,0,0.08); background: #fff;">
                <img src="social/TimeScope_ss2.png" alt="Calculate Durations" style="width: 100%; border-radius: 16px;">
            </div>
        </div>
        
        <!-- Feature 2: Relative Days -->
        <div class="feature-row fade-in">
            <div class="feature-text">
                <h3 data-i18n="feature.2.title" style="font-size: 2.2rem; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.03em;">Know "How Many Days" at a Glance</h3>
                <p data-i18n="feature.2.desc" style="font-size: 1.1rem; color: var(--light-text-muted); line-height: 1.6;">Stop counting weeks manually. Smart relative indicators automatically display exactly how many days remain until a future date, or how many days have passed since a past event.</p>
            </div>
            <div class="feature-visual" style="box-shadow: 0 10px 40px rgba(0,0,0,0.08); background: #fff;">
                <img src="social/TimeScope_ss1.png" alt="Relative Days" style="width: 100%; border-radius: 16px;">
            </div>
        </div>

        <!-- Feature 3: Compare -->
        <div class="feature-row fade-in">
            <div class="feature-text">
                <h3 data-i18n="feature.3.title" style="font-size: 2.2rem; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.03em;">Compare Multiple Timelines</h3>
                <p data-i18n="feature.3.desc" style="font-size: 1.1rem; color: var(--light-text-muted); line-height: 1.6;">Visually compare different periods side-by-side. Highlight multiple date ranges to effortlessly evaluate overlapping schedules, alternative trip dates, and complex project phases.</p>
            </div>
            <div class="feature-visual" style="box-shadow: 0 10px 40px rgba(0,0,0,0.08); background: #fff;">
                <img src="social/TimeScope_ss3.png" alt="Compare Timelines" style="width: 100%; border-radius: 16px;">
            </div>
        </div>
    </section>

    <!-- 3. WHY TIMESCOPE -->
    <section class="problem container fade-in" style="padding: 100px 0; border-top: 1px solid var(--light-border);">
        <h2 data-i18n="why.title" style="font-size: 2.5rem; font-weight: 800; margin-bottom: 24px; letter-spacing: -0.03em;">Not a planner. A time navigator.</h2>
        <div style="max-width: 700px; margin: 0 auto; text-align: center; border-left: 4px solid #00D0FF; padding-left: 24px; text-align: left;">
            <p data-i18n="why.desc1" style="font-size: 1.15rem; color: var(--light-text-muted); margin-bottom: 16px; line-height: 1.6;">Traditional calendar apps are built to track meetings and to-do lists. TimeScope is built to help you understand time itself.</p>
            <p data-i18n="why.desc2" style="font-size: 1.15rem; color: var(--light-text-main); font-weight: 600; line-height: 1.6;">Know how long things take. See how far away important dates are. Stop counting days on your fingers, and start seeing time instantly.</p>
        </div>
    </section>

    <!-- 4. MID CTA -->
    <div class="container fade-in" style="margin-bottom: 80px;">
        <div class="mid-cta" style="background: var(--dark-bg); color: #fff; border-radius: 24px; padding: 80px 40px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">
            <h2 data-i18n="midcta.title" style="font-size: 2.5rem; letter-spacing: -0.03em; margin-bottom: 32px;">Ready to see time instantly?</h2>
            <div class="cta-wrapper">
                <a href="ms-windows-store://pdp/?productid=dummy" class="btn btn-primary download-link" style="background: #fff; color: #000; font-size: 1.1rem; padding: 16px 32px; border-radius: 30px;" data-i18n="hero.cta">Get it from Microsoft Store</a>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer style="margin-top: 60px;">
        <div class="container footer-content">
            <div class="copyright">&copy; 2026 TimeScope. <span data-i18n="footer.rights">All rights reserved.</span></div>
            <div class="footer-links">
                <a href="terms.html" data-i18n="footer.terms">Terms</a>
                <a href="privacy.html" data-i18n="footer.privacy">Privacy</a>
                <a href="contact.html" data-i18n="footer.contact">Contact</a>
                <a href="https://x.com/TimeScope_App" target="_blank">X (Twitter)</a>
            </div>
        </div>
    </footer>

    <!-- I18N AND LOGIC -->
    <script>
        const i18nData = {{
            "en": {{
                "hero.title": "See time. Instantly.",
                "hero.subtitle": "Drag to calculate durations, compare multiple periods, and see exactly how far away any date is.<br>The ultra-lightweight time navigator for Windows.",
                "hero.cta": "Get it from Microsoft Store",
                "hero.micro": "Available for Windows 10 & 11",
                
                "feature.1.title": "Drag to Calculate Durations",
                "feature.1.desc": "Just click and drag across the calendar to instantly see the exact number of days between any two dates. Perfect for project planning, trip scheduling, or counting down to major life events without doing the math.",
                
                "feature.2.title": "Know \\"How Many Days\\" at a Glance",
                "feature.2.desc": "Stop counting weeks manually. Smart relative indicators automatically display exactly how many days remain until a future date, or how many days have passed since a past event.",
                
                "feature.3.title": "Compare Multiple Timelines",
                "feature.3.desc": "Visually compare different periods side-by-side. Highlight multiple date ranges to effortlessly evaluate overlapping schedules, alternative trip dates, and complex project phases.",
                
                "why.title": "Not a planner. A time navigator.",
                "why.desc1": "Traditional calendar apps are built to track meetings and to-do lists. TimeScope is built to help you understand time itself.",
                "why.desc2": "Know how long things take. See how far away important dates are. Stop counting days on your fingers, and start seeing time instantly.",
                
                "midcta.title": "Ready to see time instantly?",
                
                "footer.rights": "All rights reserved.",
                "footer.terms": "Terms",
                "footer.privacy": "Privacy",
                "footer.contact": "Contact"
            }},
            "ja": {{
                "hero.title": "See time. Instantly.",
                "hero.subtitle": "なぞるだけで期間を測り、予定を比較し、あの日まで「あと何日か」を直感的に把握する。<br>Windowsのための、超軽量な時間ナビゲーションツール。",
                "hero.cta": "Microsoft Store で手に入れる",
                "hero.micro": "Windows 10 & 11 に対応",
                
                "feature.1.title": "なぞるだけで、期間を計算",
                "feature.1.desc": "カレンダーをクリックしてドラッグするだけで、2つの日付の間が「何日間」あるのかを瞬時に計算します。旅行の計画、プロジェクトのスケジュール確認、記念日までのカウントダウンが、かつてないほどスムーズに。",
                
                "feature.2.title": "「あと何日？」が、一目でわかる",
                "feature.2.desc": "すべての日付の下に、今日からの「相対日数」を自動表示。未来の予定まであと何日残っているか、過去の出来事から何日経ったかが、もうカレンダーを指で数えることなく一瞬で把握できます。",
                
                "feature.3.title": "複数のスケジュールを直感的に比較",
                "feature.3.desc": "複数の期間を同時にハイライトし、視覚的に見比べることができます。旅行のA案・B案の比較や、重なり合うプロジェクトの期間調整など、「複雑な時間の思考」をシンプルにサポートします。",
                
                "why.title": "予定帳ではなく、時間を測る「ものさし」",
                "why.desc1": "一般的なカレンダーアプリは、ミーティングやタスクを「管理」するために作られています。しかしTimeScopeは、純粋に時間の長さを測り、比較し、理解するために生まれました。",
                "why.desc2": "これからは、日数を頭で計算する必要はありません。ただ、視るだけです。",
                
                "midcta.title": "Ready to see time instantly?",
                
                "footer.rights": "無断複写・転載を禁じます。",
                "footer.terms": "利用規約",
                "footer.privacy": "プライバシーポリシー",
                "footer.contact": "お問い合わせ"
            }}
        }};

        function setLanguage(lang) {{
            document.documentElement.lang = lang;
            
            document.getElementById('btn-en').classList.toggle('active', lang === 'en');
            document.getElementById('btn-ja').classList.toggle('active', lang === 'ja');
            
            const elements = document.querySelectorAll('[data-i18n]');
            elements.forEach(el => {{
                const key = el.getAttribute('data-i18n');
                if (i18nData[lang] && i18nData[lang][key]) {{
                    el.innerHTML = i18nData[lang][key]; 
                }}
            }});

            document.title = 'TimeScope | See time. Instantly.';
            document.body.style.opacity = '1';
            document.body.style.transition = 'opacity 0.2s ease-in';

            try {{ localStorage.setItem('timescope-lang', lang); }} catch(e) {{}}
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            const initialLang = document.documentElement.lang || 'en';
            setLanguage(initialLang);

            const observer = new IntersectionObserver((entries) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('visible');
                    }}
                }});
            }}, {{
                threshold: 0.15,
                rootMargin: "0px 0px -40px 0px"
            }});

            document.querySelectorAll('.fade-in').forEach(el => {{
                observer.observe(el);
            }});
        }});
    </script>
</body>
</html>
'''

with open(r'c:\dev\projects\TimeScope-LP\index_v2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
