import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Hero Subtitle & Mockup
html = html.replace(
    '<p data-i18n="hero.subtitle">Know the duration. Instantly.</p>',
    '<p data-i18n="hero.subtitle">Understand and decide time instantly.</p>'
)
html = html.replace(
    '<div class="hero-mockup">\n                    <span data-i18n="hero.mockup">[ UI GIF / Video Placeholder ]</span>\n                </div>',
    '<div class="hero-mockup">\n                    <img src="assets/hero_animation.webp" alt="TimeScope Hero UI" style="width: 100%; height: 100%; object-fit: cover;">\n                </div>'
)

# 2. Add New CSS Styles
new_css = """
        .pro-badge {
            display: inline-flex;
            align-items: center;
            background: rgba(37, 99, 235, 0.1);
            color: #2563eb;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 12px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 16px;
        }
        
        .pro-feature-row {
            background: linear-gradient(180deg, transparent 0%, rgba(37,99,235,0.04) 100%);
            border: 1px solid rgba(37, 99, 235, 0.1);
            border-radius: 32px;
            padding: 60px 40px;
        }

        .feature-visual {
            flex: 1.2;
            display: flex;
            align-items: center;
            justify-content: center;
            /* Override old static box */
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }
        
        .feature-visual img {
            width: 100%;
            height: auto;
            border-radius: 16px;
            mix-blend-mode: multiply; /* Helps blend the fcfcfd background gracefully */
        }
        
        .cta-group {
            display: flex;
            gap: 16px;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            margin-bottom: 8px;
        }
"""
html = html.replace('/* 4.5 Intermediate CTA Banner */', new_css + '\n        /* 4.5 Intermediate CTA Banner */')

# 3. Replace Features Section
new_features = """
    <!-- 4. FEATURES (with GIF framing) -->
    <section class="features container">
        
        <!-- Feature 1: Scroll -->
        <div class="feature-row fade-in">
            <div class="feature-text">
                <h3 data-i18n="feature.1.title">See time clearly.</h3>
                <p data-i18n="feature.1.desc">Scroll seamlessly and navigate infinite months without jarring pagination. TimeScope makes project phases and sprint lengths instantly obvious.</p>
            </div>
            <div class="feature-visual">
                <img src="assets/feature_scroll.webp" alt="Scroll Multi-Months">
            </div>
        </div>
        
        <!-- Feature 2: Font Adjust -->
        <div class="feature-row fade-in">
            <div class="feature-text">
                <h3 data-i18n="feature.2.title">Adjust for your comfort.</h3>
                <p data-i18n="feature.2.desc">Scale the calendar to fit your visual preference. A beautifully responsive UI natively built for Windows, designed so you never have to strain to read dates again.</p>
            </div>
            <div class="feature-visual">
                <img src="assets/feature_font.webp" alt="Adjust Font Size">
            </div>
        </div>

        <!-- CLI-MAX FEATURE 3: Pro Decision Making -->
        <div class="feature-row pro-feature-row fade-in">
            <div class="feature-text">
                <div class="pro-badge" data-i18n="feature.probadge">Pro Feature</div>
                <h3 data-i18n="feature.3.title">Make better decisions instantly.</h3>
                <p data-i18n="feature.3.desc">Compare durations for different project scenarios directly on the calendar. Visualize the difference between Option A and Option B instantly without doing the math.</p>
            </div>
            <div class="feature-visual">
                <img src="assets/feature_pro.webp" alt="Compare Durations">
            </div>
        </div>
    </section>
"""
# Use regex to replace the entire <section class="features container">...</section>
html = re.sub(r'<section class="features container">.*?</section>', new_features, html, flags=re.DOTALL)


# 4. Replace Mid CTA
new_mid_cta = """
    <!-- 4.5. MID CTA -->
    <div class="container fade-in">
        <div class="mid-cta" style="background: var(--light-elevated); border: 1px solid var(--light-border);">
            <h2 data-i18n="midcta.title">Start free. Upgrade when you need more power.</h2>
            <div class="cta-wrapper">
                <div class="cta-group">
                    <a href="#" class="btn btn-light-outline" data-i18n="midcta.cta_free">Download Free</a>
                    <a href="#pricing" class="btn btn-light-primary" data-i18n="midcta.cta_pro">View Pro Features</a>
                </div>
                <div class="microcopy microcopy-light" data-i18n="midcta.micro">✓ Lightweight installer. Free version works forever.</div>
            </div>
        </div>
    </div>
"""
html = re.sub(r'<!-- 4\.5\. MID CTA -->\n    <div class="container fade-in">.*?</div>\n    </div>', new_mid_cta, html, flags=re.DOTALL)


# 5. Pricing Pro Card alignment
html = html.replace(
    '<ul class="feature-list">\n                    <li data-i18n="pricing.pro.feat1">Compare multiple time ranges</li>',
    '<ul class="feature-list">\n                    <li data-i18n="pricing.pro.feat1" style="color: #60a5fa; font-weight: 700;">Compare multiple time ranges (Duration Delta)</li>'
)


# 6. Update i18n
i18n_new_en = """
                "hero.subtitle": "A calendar built to understand and decide time instantly.",
                
                "feature.1.title": "See time clearly.",
                "feature.1.desc": "Scroll seamlessly and navigate infinite months without jarring pagination. TimeScope makes project phases and sprint lengths instantly obvious.",
                
                "feature.2.title": "Adjust for your comfort.",
                "feature.2.desc": "Scale the calendar to fit your visual preference. A beautifully responsive UI natively built for Windows, designed so you never have to strain to read dates again.",
                
                "feature.probadge": "Pro Feature",
                "feature.3.title": "Make better decisions instantly.",
                "feature.3.desc": "Compare durations for different project scenarios directly on the calendar. Visualize the difference between Option A and Option B instantly without doing the math.",
                
                "midcta.title": "Start free. Upgrade when you need more power.",
                "midcta.cta_free": "Download Free",
                "midcta.cta_pro": "View Pro Features",
                "midcta.micro": "✓ Lightweight installer. Free version works forever.",
                
                "pricing.pro.feat1": "Compare multiple time ranges (Duration Delta)",
"""

i18n_new_ja = """
                "hero.subtitle": "「期間」を理解し、一瞬で決断するためのカレンダー。",
                
                "feature.1.title": "時間を、直感的に見渡す。",
                "feature.1.desc": "途切れることのない滑らかなスクロールで、複数月をシームレスに移動。プロジェクトの全体像やスプリント期間が、ひと目で手に取るように分かります。",
                
                "feature.2.title": "あなたの目に最適化。",
                "feature.2.desc": "カレンダー全体の拡縮に完全対応。Windowsネイティブの美しくレスポンシブなUIにより、最も見やすく、思考を妨げないスケールへと一瞬で調整できます。",
                
                "feature.probadge": "Pro機能",
                "feature.3.title": "より良い決断を、一瞬で。",
                "feature.3.desc": "複数のシナリオ（例えばOption AとB）を同時にカレンダー上に展開。どちらがどれだけ長くかかるのか、差分の日数（Delta）と共に自動で可視化し、迷いのない意思決定を強力にサポートします。",
                
                "midcta.title": "無料でスタート。より高度な力が必要になったらProへ。",
                "midcta.cta_free": "無料版をダウンロード",
                "midcta.cta_pro": "Pro機能の詳細を見る",
                "midcta.micro": "✓ 超軽量インストーラー。無料版はずっと無料でお使いいただけます。",
                
                "pricing.pro.feat1": "複数期間の同時比較（差分表示機能）",
"""

# Replace the specific i18n blocks dynamically
def replace_i18n(lang, new_block, html_content):
    if lang == 'en':
        pattern = r'"hero\.subtitle": "A calendar built for understanding duration.",.*?"midcta\.micro": ".*?Runs instantly.",'
    else:
        pattern = r'"hero\.subtitle": "「期間」を理解することに特化した、新しいカレンダー。",.*?"midcta\.micro": ".*?すぐに起動",'
    
    html_content = re.sub(pattern, new_block.strip() + ',', html_content, flags=re.DOTALL)
    return html_content

html = replace_i18n('en', i18n_new_en, html)
html = replace_i18n('ja', i18n_new_ja, html)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
