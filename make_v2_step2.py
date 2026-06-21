import re

with open(r'c:\dev\projects\TimeScope-LP\index.html', 'r', encoding='utf-8') as f:
    original = f.read()

# Extract head and styles
head_match = re.search(r'(<head>.*?</head>)', original, re.DOTALL)
head_content = head_match.group(1) if head_match else '<head></head>'

# Update Meta Description for SEO
new_desc = "A lightweight Windows calendar app to calculate durations, compare dates, and see relative days instantly. The perfect timeline and countdown calculator."
head_content = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{new_desc}">', head_content)
head_content = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{new_desc}">', head_content)
head_content = re.sub(r'<meta property="twitter:description" content="[^"]*">', f'<meta property="twitter:description" content="{new_desc}">', head_content)

html_content = f'''<!DOCTYPE html>
<html lang="en">
{head_content}
<body>
    <style>
        .pricing-table {{ width: 100%; border-collapse: collapse; margin-top: 40px; background: var(--light-elevated); border-radius: 16px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }}
        .pricing-table th, .pricing-table td {{ padding: 16px 24px; text-align: left; border-bottom: 1px solid var(--light-border); }}
        .pricing-table th {{ background: #f4f4f5; font-weight: 700; color: var(--light-text-main); }}
        .pricing-table td:nth-child(2), .pricing-table th:nth-child(2) {{ text-align: center; border-left: 1px solid var(--light-border); border-right: 1px solid var(--light-border); }}
        .pricing-table td:nth-child(3), .pricing-table th:nth-child(3) {{ text-align: center; background: rgba(0, 208, 255, 0.05); }}
        .pricing-table tr:last-child td {{ border-bottom: none; }}
        .check-yes {{ color: #10b981; font-weight: bold; font-size: 1.2rem; }}
        .check-no {{ color: var(--light-text-muted); }}
    </style>

    <!-- NAV -->
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

    <!-- 1. HERO -->
    <div class="theme-dark">
        <header class="hero container fade-in" style="padding-top: 140px;">
            <h1 data-i18n="hero.title">See time. Instantly.</h1>
            <p data-i18n="hero.subtitle" style="max-width: 700px; margin: 0 auto 32px; line-height: 1.5; font-size: 1.25rem;">Calculate durations, compare periods, and instantly know how far away important dates are.</p>
            
            <div class="hero-actions" style="flex-direction: row; flex-wrap: wrap; justify-content: center; align-items: center; gap: 16px;">
                <a href="ms-windows-store://pdp/?productid=dummy" class="btn btn-primary" style="background: #fff; color: #000; font-size: 1.1rem; padding: 14px 28px; border-radius: 30px;" data-i18n="hero.cta_free">Download Free</a>
                <a href="#pricing" class="btn btn-outline" style="border: 2px solid #fff; color: #fff; font-size: 1.1rem; padding: 12px 28px; border-radius: 30px; text-decoration: none;" data-i18n="hero.cta_pro">Upgrade to Pro</a>
            </div>
            
            <div class="hero-mockup-wrapper fade-in" style="max-width: 900px; margin-top: 60px;">
                <div class="hero-mockup" style="background-color: #000000; border: 1px solid #333;">
                    <img src="social/DAY1_hero.gif" alt="TimeScope Hero" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
            </div>
        </header>
    </div>

    <!-- 2. FEATURES -->
    <section class="features container" style="padding-top: 100px;">
        
        <!-- Feature 1: Duration -->
        <div class="feature-row fade-in">
            <div class="feature-text">
                <h3 data-i18n="feature.1.title" style="font-size: 2.2rem; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.03em;">Calculate durations instantly</h3>
                <p data-i18n="feature.1.desc" style="font-size: 1.1rem; color: var(--light-text-muted); line-height: 1.6;">Instantly select periods and calculate durations with a simple click and drag.<br><br>Perfect for vacations, project planning, countdowns, and life events.</p>
            </div>
            <div class="feature-visual" style="box-shadow: 0 10px 40px rgba(0,0,0,0.08); background: #fff;">
                <img src="social/TimeScope_ss2.png" alt="Calculate Durations" style="width: 100%; border-radius: 16px;">
            </div>
        </div>
        
        <!-- Feature 2: Relative Days -->
        <div class="feature-row fade-in">
            <div class="feature-text">
                <h3 data-i18n="feature.2.title" style="font-size: 2.2rem; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.03em;">See exactly how far away any date is</h3>
                <p data-i18n="feature.2.desc" style="font-size: 1.1rem; color: var(--light-text-muted); line-height: 1.6;">See how many days remain until any date—or how long ago it was.</p>
            </div>
            <div class="feature-visual" style="box-shadow: 0 10px 40px rgba(0,0,0,0.08); background: #fff;">
                <img src="social/TimeScope_ss1.png" alt="Relative Days" style="width: 100%; border-radius: 16px;">
            </div>
        </div>

        <!-- Feature 3: Compare -->
        <div class="feature-row fade-in">
            <div class="feature-text">
                <div class="pro-badge" data-i18n="feature.probadge" style="display: inline-block; padding: 4px 10px; background: #e0e7ff; color: #4338ca; border-radius: 4px; font-size: 0.8rem; font-weight: 700; margin-bottom: 12px;">Pro Feature</div>
                <h3 data-i18n="feature.3.title" style="font-size: 2.2rem; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.03em;">Compare multiple date ranges</h3>
                <p data-i18n="feature.3.desc" style="font-size: 1.1rem; color: var(--light-text-muted); line-height: 1.6;">Evaluate different travel plans, project schedules, or important events side-by-side.</p>
            </div>
            <div class="feature-visual" style="box-shadow: 0 10px 40px rgba(0,0,0,0.08); background: #fff;">
                <img src="social/TimeScope_ss3.png" alt="Compare Timelines" style="width: 100%; border-radius: 16px;">
            </div>
        </div>
        
        <!-- Feature 4 & 5: System Tray (Grid Layout) -->
        <div class="fade-in" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; margin-top: 60px;">
            <div style="background: var(--light-elevated); border: 1px solid var(--light-border); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                <div style="font-size: 2rem; margin-bottom: 16px;">⚡</div>
                <h3 data-i18n="feature.4.title" style="font-size: 1.5rem; font-weight: 700; margin-bottom: 12px;">Always within reach</h3>
                <p data-i18n="feature.4.desc" style="color: var(--light-text-muted); line-height: 1.6;">Access TimeScope instantly from your system tray. No need to relaunch the application every time.</p>
            </div>
            <div style="background: var(--light-elevated); border: 1px solid var(--light-border); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                <div style="font-size: 2rem; margin-bottom: 16px;">📅</div>
                <h3 data-i18n="feature.5.title" style="font-size: 1.5rem; font-weight: 700; margin-bottom: 12px;">Stay aware of today's date</h3>
                <p data-i18n="feature.5.desc" style="color: var(--light-text-muted); line-height: 1.6;">See today's date directly from the system tray and stay connected to time. Apps don't need to be open to be useful.</p>
            </div>
        </div>
    </section>

    <!-- 3. WHY TIMESCOPE -->
    <section class="problem container fade-in" style="padding: 120px 0 80px; text-align: center;">
        <h2 data-i18n="why.title1" style="font-size: 2.8rem; font-weight: 800; line-height: 1.2; letter-spacing: -0.04em;">Not a planner.<br>A time navigator.</h2>
        <p data-i18n="why.title2" style="font-size: 1.5rem; color: var(--light-text-muted); font-weight: 500; margin-top: 24px;">Stop counting.<br>Start seeing time.</p>
    </section>

    <!-- 4. PRICING & COMPARISON -->
    <section id="pricing" class="pricing container fade-in" style="padding: 40px 0 100px;">
        <div class="section-header" style="text-align: center; margin-bottom: 40px;">
            <h2 data-i18n="pricing.title">Choose your TimeScope</h2>
            <p data-i18n="pricing.subtitle">Start free, upgrade for professional workflows.</p>
        </div>
        
        <table class="pricing-table">
            <thead>
                <tr>
                    <th style="width: 50%; font-size: 1.1rem;" data-i18n="pricing.table.features">Features</th>
                    <th style="width: 25%;">
                        <div style="font-size: 1.5rem; font-weight: 800; color: var(--light-text-main);">Free</div>
                        <div style="font-size: 0.9rem; font-weight: 500; color: var(--light-text-muted); margin-top: 4px;">$0</div>
                    </th>
                    <th style="width: 25%;">
                        <div style="font-size: 1.5rem; font-weight: 800; color: #4338ca;">Pro</div>
                        <div style="font-size: 0.9rem; font-weight: 500; color: #4338ca; margin-top: 4px;">$9.99 <span style="font-size: 0.8em;">(one-time)</span></div>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td data-i18n="pricing.feat.1">Calculate durations (Click & Drag)</td>
                    <td class="check-yes">✓</td>
                    <td class="check-yes">✓</td>
                </tr>
                <tr>
                    <td data-i18n="pricing.feat.2">Relative days indicator (± days)</td>
                    <td class="check-yes">✓</td>
                    <td class="check-yes">✓</td>
                </tr>
                <tr>
                    <td data-i18n="pricing.feat.3">System Tray quick access</td>
                    <td class="check-yes">✓</td>
                    <td class="check-yes">✓</td>
                </tr>
                <tr>
                    <td data-i18n="pricing.feat.4">Compare multiple date ranges</td>
                    <td class="check-no">—</td>
                    <td class="check-yes">✓</td>
                </tr>
                <tr>
                    <td data-i18n="pricing.feat.5">Advanced time navigation</td>
                    <td class="check-no">—</td>
                    <td class="check-yes">✓</td>
                </tr>
                <tr>
                    <td data-i18n="pricing.feat.6">Commercial use</td>
                    <td class="check-no">—</td>
                    <td class="check-yes">✓</td>
                </tr>
                <tr>
                    <td></td>
                    <td style="padding: 24px;">
                        <a href="ms-windows-store://pdp/?productid=dummy" class="btn btn-light-outline" style="width: 100%;" data-i18n="hero.cta_free">Download Free</a>
                        <div style="font-size: 0.8rem; color: var(--light-text-muted); margin-top: 8px;" data-i18n="pricing.free.micro">via Microsoft Store</div>
                    </td>
                    <td style="padding: 24px;">
                        <a href="https://buy.stripe.com/6oUaEWeH89ta9xaa6S1wY00" class="btn btn-upgrade" style="width: 100%;" target="_blank" data-i18n="hero.cta_pro">Upgrade to Pro</a>
                        <div style="font-size: 0.8rem; color: var(--light-text-muted); margin-top: 8px;" data-i18n="pricing.pro.micro">Secure checkout via Stripe</div>
                    </td>
                </tr>
            </tbody>
        </table>
    </section>

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
                "hero.subtitle": "Calculate durations, compare periods, and instantly know how far away important dates are.",
                "hero.cta_free": "Download Free",
                "hero.cta_pro": "Upgrade to Pro",
                
                "feature.1.title": "Calculate durations instantly",
                "feature.1.desc": "Instantly select periods and calculate durations with a simple click and drag.<br><br>Perfect for vacations, project planning, countdowns, and life events.",
                
                "feature.2.title": "See exactly how far away any date is",
                "feature.2.desc": "See how many days remain until any date—or how long ago it was.",
                
                "feature.probadge": "Pro Feature",
                "feature.3.title": "Compare multiple date ranges",
                "feature.3.desc": "Evaluate different travel plans, project schedules, or important events side-by-side.",
                
                "feature.4.title": "Always within reach",
                "feature.4.desc": "Access TimeScope instantly from your system tray.<br>No need to relaunch the application every time.",
                
                "feature.5.title": "Stay aware of today's date",
                "feature.5.desc": "See today's date directly from the system tray and stay connected to time.",
                
                "why.title1": "Not a planner.<br>A time navigator.",
                "why.title2": "Stop counting.<br>Start seeing time.",
                
                "pricing.title": "Choose your TimeScope",
                "pricing.subtitle": "Start free, upgrade for professional workflows.",
                "pricing.table.features": "Features",
                "pricing.feat.1": "Calculate durations (Click & Drag)",
                "pricing.feat.2": "Relative days indicator (± days)",
                "pricing.feat.3": "System Tray quick access",
                "pricing.feat.4": "Compare multiple date ranges",
                "pricing.feat.5": "Advanced time navigation",
                "pricing.feat.6": "Commercial use",
                "pricing.free.micro": "via Microsoft Store",
                "pricing.pro.micro": "Secure checkout via Stripe",
                
                "footer.rights": "All rights reserved.",
                "footer.terms": "Terms",
                "footer.privacy": "Privacy",
                "footer.contact": "Contact"
            }},
            "ja": {{
                "hero.title": "時間を、一瞬で見渡す。",
                "hero.subtitle": "期間を測り、比較し、大切な日まであと何日かを瞬時に把握。",
                "hero.cta_free": "無料版をダウンロード",
                "hero.cta_pro": "Pro版を見る",
                
                "feature.1.title": "期間を一瞬で計算",
                "feature.1.desc": "クリック＆ドラッグするだけで、期間の日数を瞬時に計算できます。<br><br>旅行計画、プロジェクト管理、記念日までのカウントダウンなどに最適です。",
                
                "feature.2.title": "あと何日か、一目でわかる",
                "feature.2.desc": "未来の日付まであと何日か、過去の日付から何日経ったかを瞬時に確認できます。",
                
                "feature.probadge": "Pro機能",
                "feature.3.title": "複数の期間を比較",
                "feature.3.desc": "異なる予定や候補日程を比較し、それぞれの期間を直感的に把握できます。",
                
                "feature.4.title": "いつでもすぐ使える",
                "feature.4.desc": "タスクトレイからいつでもアクセスできます。<br>アプリを起動し直す必要はありません。",
                
                "feature.5.title": "今日の日付をいつでも確認",
                "feature.5.desc": "タスクトレイ上で今日の日付や時間を確認できます。<br>アプリを開かなくても時間を意識できます。",
                
                "why.title1": "予定管理ではなく、<br>時間を見渡すためのツール。",
                "why.title2": "数えるのではなく、<br>見渡す。",
                
                "pricing.title": "料金プラン",
                "pricing.subtitle": "まずは無料で。必要になったらProへ。",
                "pricing.table.features": "機能",
                "pricing.feat.1": "ドラッグで期間を計算",
                "pricing.feat.2": "相対日数の表示 (± 日数)",
                "pricing.feat.3": "タスクトレイ常駐",
                "pricing.feat.4": "複数期間の同時比較",
                "pricing.feat.5": "高度な時間ナビゲーション",
                "pricing.feat.6": "商用利用",
                "pricing.free.micro": "Microsoft Store経由",
                "pricing.pro.micro": "Stripeによる安全な決済",
                
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

            document.title = lang === 'en' ? 'TimeScope | See time. Instantly.' : 'TimeScope | 時間を、一瞬で見渡す。';
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
