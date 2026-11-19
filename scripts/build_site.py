import html
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOCALES_PATH = os.path.join(ROOT, "locales", "site_locales.json")
SUBPAGES_PATH = os.path.join(ROOT, "locales", "subpages_locales.json")
STORE_URL = "https://apps.microsoft.com/detail/9NJR56D56R9F"
BASE_URL = "https://gettimescope.com"

ANALYTICS_HEAD = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-T7HPX8ZJJ4"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-T7HPX8ZJJ4');
    </script>
    <!-- Microsoft Clarity -->
    <script type="text/javascript">
      (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
      })(window, document, "clarity", "script", "wfyjqjuxl4");
    </script>"""


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def build_hreflangs(locales: dict, page_file: str = "") -> str:
    lines = []
    for loc_key, data in locales.items():
        url = f"{BASE_URL}{data['url_path']}{page_file}"
        lines.append(f'    <link rel="alternate" hreflang="{loc_key}" href="{url}">')
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE_URL}/{page_file}">')
    return "\n".join(lines)


def build_lang_options(locales: dict, current_key: str, prefix: str, page_file: str = "") -> str:
    opts = []
    for k, d in locales.items():
        loc_dir = d["url_path"].strip("/")
        if page_file:
            target = f"{prefix}{loc_dir}/{page_file}" if loc_dir else f"{prefix}{page_file}"
        else:
            target = f"{prefix}{loc_dir}/" if loc_dir else (f"{prefix}index.html" if prefix else "/")
        sel = " selected" if k == current_key else ""
        opts.append(f'<option value="{esc(target)}" data-locale="{esc(k)}"{sel}>{esc(d["label"])}</option>')
    return "\n".join(opts)


def render_homepage(loc_key: str, d: dict, all_locales: dict) -> str:
    is_root = d["url_path"] == "/"
    prefix = "" if is_root else "../"
    canon = f"{BASE_URL}{d['url_path']}"
    shot_dir = f"{prefix}assets/v2/screenshots/{loc_key}"

    benefits_html = "\n".join(
        f"""                <article class="benefit-card">
                    <span class="benefit-badge">{esc(b['badge'])}</span>
                    <h3>{esc(b['title'])}</h3>
                    <p>{esc(b['desc'])}</p>
                </article>"""
        for b in d["benefits"]
    )

    feature_rows = []
    for idx, feat in enumerate(d["features"]):
        rev = " reverse" if idx % 2 == 1 else ""
        bullets = "\n".join(f"                        <li>{esc(x)}</li>" for x in feat["bullets"])
        feature_rows.append(
            f"""            <div class="feature-row{rev}">
                <div class="feature-copy">
                    <h3>{esc(feat['title'])}</h3>
                    <p>{esc(feat['desc'])}</p>
                    <ul class="feature-list">
{bullets}
                    </ul>
                </div>
                <div class="feature-shot">
                    <img src="{shot_dir}/{feat['shot']}.webp" alt="{esc(feat['alt'])}" width="1440" height="810" loading="lazy">
                </div>
            </div>"""
        )
    features_html = "\n".join(feature_rows)

    free_list = "\n".join(f"                        <li>{esc(x)}</li>" for x in d["free_items"])
    pro_list = "\n".join(f"                        <li>{esc(x)}</li>" for x in d["pro_items"])

    thumbs_html = []
    for i in range(1, 8):
        num = f"0{i}"
        active = " active" if i == 1 else ""
        cap = d["captions"][i - 1]
        thumbs_html.append(
            f"""                <button type="button" class="thumb-btn{active}" data-slide="{i}" data-src="{shot_dir}/{num}.webp" data-caption="{esc(cap)}" aria-label="Screenshot {i}">
                    <img src="{shot_dir}/{num}.webp" alt="{esc(cap)}" width="1440" height="810" loading="lazy">
                </button>"""
        )

    json_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": "TimeScope – Visual Calendar",
            "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "Windows 10, Windows 11",
            "url": canon,
            "downloadUrl": STORE_URL,
            "publisher": {"@type": "Organization", "name": "Tomi-lab"},
            "offers": [
                {"@type": "Offer", "price": "0", "priceCurrency": "USD", "description": "TimeScope Free Edition"},
                {"@type": "Offer", "price": "4.99", "priceCurrency": "USD", "description": "TimeScope Pro (One-time in-app purchase)"},
            ],
        },
        ensure_ascii=False,
    )

    lang_opts = build_lang_options(all_locales, loc_key, prefix)
    hreflangs = build_hreflangs(all_locales)

    return f"""<!DOCTYPE html>
<html lang="{esc(d['html_lang'])}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(d['seo_title'])}</title>
    <meta name="description" content="{esc(d['seo_desc'])}">
    <link rel="canonical" href="{canon}">
{hreflangs}

    <!-- Open Graph / Twitter -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canon}">
    <meta property="og:title" content="{esc(d['seo_title'])}">
    <meta property="og:description" content="{esc(d['seo_desc'])}">
    <meta property="og:image" content="{BASE_URL}/assets/v2/timescope-ogp-v6.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(d['seo_title'])}">
    <meta name="twitter:description" content="{esc(d['seo_desc'])}">
    <meta name="twitter:image" content="{BASE_URL}/assets/v2/timescope-ogp-v6.jpg">

    <link rel="icon" href="{prefix}favicon.ico" type="image/x-icon">
    <link rel="apple-touch-icon" href="{prefix}assets/v2/timescope_icon_rounded_256.png">
    <link rel="stylesheet" href="{prefix}assets/v2/styles.css">
    <script type="application/ld+json">{json_ld}</script>
{ANALYTICS_HEAD}
</head>
<body>
    <header class="site-header">
        <div class="container header-inner">
            <a href="index.html" class="brand-link">
                <img src="{prefix}assets/v2/timescope_icon_rounded_64.png" alt="TimeScope Logo" width="32" height="32">
                <span>TimeScope</span>
            </a>
            <nav class="nav-links" aria-label="Main navigation">
                <a href="#features">{esc(d['nav_features'])}</a>
                <a href="#pricing">{esc(d['nav_pricing'])}</a>
                <a href="support.html">{esc(d['nav_support'])}</a>
            </nav>
            <div class="header-actions">
                <select class="lang-select" aria-label="Language" onchange="switchLocale(this)">
{lang_opts}
                </select>
                <a href="{STORE_URL}" target="_blank" rel="noopener" class="btn btn-primary btn-sm" data-cta="header">{esc(d['nav_cta'])}</a>
            </div>
        </div>
    </header>

    <main>
        <section class="hero-section">
            <div class="container">
                <div class="hero-content">
                    <span class="hero-pill">{esc(d['hero_pill'])}</span>
                    <h1>{esc(d['hero_h1'])}</h1>
                    <p>{esc(d['hero_sub'])}</p>
                    <div class="hero-ctas">
                        <a href="{STORE_URL}" target="_blank" rel="noopener" class="btn btn-primary" data-cta="hero">{esc(d['hero_cta_primary'])}</a>
                        <a href="#pricing" class="btn btn-secondary">{esc(d['hero_cta_secondary'])}</a>
                    </div>
                    <p class="hero-meta">{esc(d['hero_meta'])}</p>
                </div>
                <div class="hero-visual">
                    <img src="{shot_dir}/01.webp" alt="{esc(d['hero_alt'])}" width="1440" height="810">
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="section-header">
                    <h2>{esc(d['benefits_title'])}</h2>
                    <p>{esc(d['benefits_sub'])}</p>
                </div>
                <div class="benefits-grid">
{benefits_html}
                </div>
            </div>
        </section>

        <section id="features" class="section section-tinted">
            <div class="container">
                <div class="section-header">
                    <h2>{esc(d['features_title'])}</h2>
                    <p>{esc(d['features_sub'])}</p>
                </div>
                <div class="feature-stack">
{features_html}
                </div>
            </div>
        </section>

        <section id="pricing" class="section">
            <div class="container">
                <div class="section-header">
                    <h2>{esc(d['pricing_title'])}</h2>
                    <p>{esc(d['pricing_sub'])}</p>
                </div>
                <div class="pricing-grid">
                    <div class="tier-card">
                        <div class="tier-top">
                            <span class="tier-name">{esc(d['free_name'])}</span>
                            <span class="tier-tag">{esc(d['free_tag'])}</span>
                        </div>
                        <div class="tier-price">{esc(d['free_price'])} <span>· {esc(d['free_price_unit'])}</span></div>
                        <p class="tier-sub">{esc(d['free_sub'])}</p>
                        <ul class="tier-list">
{free_list}
                        </ul>
                        <a href="{STORE_URL}" target="_blank" rel="noopener" class="btn btn-secondary" data-cta="pricing_free">{esc(d['free_cta'])}</a>
                    </div>
                    <div class="tier-card pro">
                        <div class="tier-top">
                            <span class="tier-name">{esc(d['pro_name'])}</span>
                            <span class="tier-tag">{esc(d['pro_tag'])}</span>
                        </div>
                        <div class="tier-price">{esc(d['pro_price'])} <span>· {esc(d['pro_price_unit'])}</span></div>
                        <p class="tier-sub">{esc(d['pro_sub'])}</p>
                        <ul class="tier-list">
{pro_list}
                        </ul>
                        <a href="{STORE_URL}" target="_blank" rel="noopener" class="btn btn-pro" data-cta="pricing_pro">{esc(d['pro_cta'])}</a>
                    </div>
                </div>
                <p class="pricing-note">{esc(d['pricing_note'])}</p>
            </div>
        </section>

        <section id="screenshots" class="section section-tinted">
            <div class="container">
                <div class="section-header">
                    <h2>{esc(d['gallery_title'])}</h2>
                    <p>{esc(d['gallery_sub'])}</p>
                </div>
                <div class="gallery-stage">
                    <img id="gallery-main-img" src="{shot_dir}/01.webp" alt="{esc(d['captions'][0])}" width="1440" height="810">
                </div>
                <p id="gallery-caption" class="gallery-caption">{esc(d['captions'][0])}</p>
                <div class="gallery-thumbs">
{chr(10).join(thumbs_html)}
                </div>
            </div>
        </section>

        <section class="bottom-cta">
            <div class="container">
                <h2>{esc(d['bottom_h2'])}</h2>
                <p>{esc(d['bottom_p'])}</p>
                <a href="{STORE_URL}" target="_blank" rel="noopener" class="btn btn-primary" data-cta="bottom">{esc(d['bottom_cta'])}</a>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container footer-inner">
            <div>{esc(d['footer_rights'])}</div>
            <div class="footer-links">
                <a href="{STORE_URL}" target="_blank" rel="noopener" data-cta="footer">{esc(d['footer_store'])}</a>
                <a href="release-notes.html">{esc(d['footer_release_notes'])}</a>
                <a href="support.html">{esc(d['footer_support'])}</a>
                <a href="contact.html">{esc(d['footer_contact'])}</a>
                <a href="privacy.html">{esc(d['footer_privacy'])}</a>
                <a href="terms.html">{esc(d['footer_terms'])}</a>
                <a href="https://x.com/TimeScope_App" target="_blank" rel="noopener">X (Twitter)</a>
                <select class="lang-select" aria-label="Footer language" onchange="switchLocale(this)">
{lang_opts}
                </select>
            </div>
        </div>
    </footer>

    <script>
      const CURRENT_LOCALE = "{esc(loc_key)}";
      function track(name, params) {{
        if (typeof gtag === "function") gtag("event", name, params || {{}});
      }}
      function switchLocale(sel) {{
        const opt = sel.options[sel.selectedIndex];
        track("language_switch", {{ from_locale: CURRENT_LOCALE, to_locale: opt.getAttribute("data-locale") }});
        window.location.href = sel.value;
      }}
      document.querySelectorAll("[data-cta]").forEach(function(el) {{
        el.addEventListener("click", function() {{
          track("store_cta_click", {{ cta_location: el.getAttribute("data-cta"), locale: CURRENT_LOCALE }});
        }});
      }});
      const mainImg = document.getElementById("gallery-main-img");
      const capEl = document.getElementById("gallery-caption");
      document.querySelectorAll(".thumb-btn").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
          document.querySelectorAll(".thumb-btn").forEach(function(b) {{ b.classList.remove("active"); }});
          btn.classList.add("active");
          mainImg.src = btn.getAttribute("data-src");
          mainImg.alt = btn.getAttribute("data-caption");
          capEl.textContent = btn.getAttribute("data-caption");
          track("gallery_slide_view", {{ slide_index: btn.getAttribute("data-slide"), locale: CURRENT_LOCALE }});
        }});
      }});
      const pricingEl = document.getElementById("pricing");
      if (pricingEl && "IntersectionObserver" in window) {{
        let seen = false;
        new IntersectionObserver(function(entries) {{
          if (!seen && entries[0].isIntersecting) {{
            seen = true;
            track("pricing_section_view", {{ locale: CURRENT_LOCALE }});
          }}
        }}, {{ threshold: 0.3 }}).observe(pricingEl);
      }}
    </script>
</body>
</html>
"""


def render_subpage_shell(
    loc_key: str,
    d: dict,
    all_locales: dict,
    page_file: str,
    title: str,
    desc: str,
    h1: str,
    sub: str,
    body_html: str,
    extra_script: str = "",
) -> str:
    is_root = d["url_path"] == "/"
    prefix = "" if is_root else "../"
    canon = f"{BASE_URL}{d['url_path']}{page_file}"
    hreflangs = build_hreflangs(all_locales, page_file)
    lang_opts = build_lang_options(all_locales, loc_key, prefix, page_file)
    sub_p = f"<p>{esc(sub)}</p>" if sub else ""

    return f"""<!DOCTYPE html>
<html lang="{esc(d['html_lang'])}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="canonical" href="{canon}">
{hreflangs}
    <link rel="icon" href="{prefix}favicon.ico" type="image/x-icon">
    <link rel="apple-touch-icon" href="{prefix}assets/v2/timescope_icon_rounded_256.png">
    <link rel="stylesheet" href="{prefix}assets/v2/styles.css">
{ANALYTICS_HEAD}
</head>
<body>
    <header class="site-header">
        <div class="container header-inner">
            <a href="index.html" class="brand-link">
                <img src="{prefix}assets/v2/timescope_icon_rounded_64.png" alt="TimeScope Logo" width="32" height="32">
                <span>TimeScope</span>
            </a>
            <nav class="nav-links" aria-label="Main navigation">
                <a href="index.html#features">{esc(d['nav_features'])}</a>
                <a href="index.html#pricing">{esc(d['nav_pricing'])}</a>
                <a href="support.html">{esc(d['nav_support'])}</a>
            </nav>
            <div class="header-actions">
                <select class="lang-select" aria-label="Language" onchange="switchLocale(this)">
{lang_opts}
                </select>
                <a href="{STORE_URL}" target="_blank" rel="noopener" class="btn btn-primary btn-sm" data-cta="header">{esc(d['nav_cta'])}</a>
            </div>
        </div>
    </header>

    <main>
        <section class="page-hero">
            <div class="container">
                <h1>{esc(h1)}</h1>
                {sub_p}
            </div>
        </section>
        <div class="doc-container">
            <div class="doc-card">
{body_html}
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container footer-inner">
            <div>{esc(d['footer_rights'])}</div>
            <div class="footer-links">
                <a href="{STORE_URL}" target="_blank" rel="noopener" data-cta="footer">{esc(d['footer_store'])}</a>
                <a href="release-notes.html">{esc(d['footer_release_notes'])}</a>
                <a href="support.html">{esc(d['footer_support'])}</a>
                <a href="contact.html">{esc(d['footer_contact'])}</a>
                <a href="privacy.html">{esc(d['footer_privacy'])}</a>
                <a href="terms.html">{esc(d['footer_terms'])}</a>
                <a href="https://x.com/TimeScope_App" target="_blank" rel="noopener">X (Twitter)</a>
                <select class="lang-select" aria-label="Footer language" onchange="switchLocale(this)">
{lang_opts}
                </select>
            </div>
        </div>
    </footer>
    <script>
      const CURRENT_LOCALE = "{esc(loc_key)}";
      function switchLocale(sel) {{
        const opt = sel.options[sel.selectedIndex];
        if (typeof gtag === "function") gtag("event", "language_switch", {{ from_locale: CURRENT_LOCALE, to_locale: opt.getAttribute("data-locale") }});
        window.location.href = sel.value;
      }}
{extra_script}
    </script>
</body>
</html>
"""


def build_support_body(sp: dict) -> str:
    groups_html = []
    for g in sp["groups"]:
        items_html = "\n".join(
            f"""                    <div class="faq-item">
                        <h3>{esc(q)}</h3>
                        <p>{esc(a).replace('support@gettimescope.com', '<a href="mailto:support@gettimescope.com">support@gettimescope.com</a>')}</p>
                    </div>"""
            for q, a in g["items"]
        )
        groups_html.append(
            f"""                <div class="faq-group">
                    <h2>{esc(g['h2'])}</h2>
{items_html}
                </div>"""
        )
    more_p = esc(sp["more_p"]).replace("support@gettimescope.com", '<a href="mailto:support@gettimescope.com">support@gettimescope.com</a>')
    groups_html.append(
        f"""                <div class="faq-group" style="margin-bottom:0;">
                    <h2>{esc(sp['more_h2'])}</h2>
                    <p>{more_p} (<a href="contact.html">contact.html</a>)</p>
                </div>"""
    )
    return "\n".join(groups_html)


def build_contact_body(ct: dict) -> str:
    return f"""                <p>{esc(ct['intro'])}</p>
                <div class="faq-group" style="margin-top:20px;margin-bottom:0;">
                    <div class="faq-item">
                        <h3>{esc(ct['tech_label'])}</h3>
                        <p><a href="mailto:support@gettimescope.com">support@gettimescope.com</a></p>
                    </div>
                    <div class="faq-item" style="margin-bottom:0;">
                        <h3>{esc(ct['biz_label'])}</h3>
                        <p><a href="mailto:info@gettimescope.com">info@gettimescope.com</a></p>
                    </div>
                </div>"""


def build_legal_body(lg: dict) -> str:
    secs = "\n".join(
        f"""                    <h2>{esc(h2)}</h2>
                    <p>{esc(p)}</p>"""
        for h2, p in lg["sections"]
    )
    return f"""                <p>{esc(lg['updated'])}</p>
                <div class="faq-group" style="margin-top:20px;">
{secs}
                </div>"""


def build_release_notes_body(rn: dict) -> str:
    blocks = []
    for rel in rn["releases"]:
        lis = "\n".join(f"                        <li>{esc(item)}</li>" for item in rel["items"])
        blocks.append(
            f"""                <div class="faq-group">
                    <h2>{esc(rel['version'])} <span style="font-size:0.75em;font-weight:normal;color:#64748b;">({esc(rel['date'])})</span></h2>
                    <ul style="margin:12px 0 0 20px;line-height:1.8;">
{lis}
                    </ul>
                </div>"""
        )
    return "\n".join(blocks)


def build_sitemap(all_locales: dict) -> str:
    urls = []
    for data in all_locales.values():
        prio = "1.0" if data["url_path"] == "/" else "0.9"
        urls.append(f"  <url>\n    <loc>{BASE_URL}{data['url_path']}</loc>\n    <priority>{prio}</priority>\n    <changefreq>weekly</changefreq>\n  </url>")
        for pf in ["release-notes.html", "support.html", "contact.html", "privacy.html", "terms.html"]:
            urls.append(f"  <url>\n    <loc>{BASE_URL}{data['url_path']}{pf}</loc>\n    <priority>0.6</priority>\n    <changefreq>monthly</changefreq>\n  </url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"


def main():
    with open(LOCALES_PATH, encoding="utf-8") as fh:
        locales = json.load(fh)
    with open(SUBPAGES_PATH, encoding="utf-8") as fh:
        subpages = json.load(fh)

    built_count = 0
    for loc_key, data in locales.items():
        rel = data["url_path"].strip("/")
        out_dir = os.path.join(ROOT, rel) if rel else ROOT
        os.makedirs(out_dir, exist_ok=True)

        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(render_homepage(loc_key, data, locales))
        built_count += 1

        sp = subpages[loc_key]["support"]
        with open(os.path.join(out_dir, "support.html"), "w", encoding="utf-8") as f:
            f.write(
                render_subpage_shell(
                    loc_key, data, locales, "support.html",
                    sp["title"], sp["desc"], sp["h1"], sp["sub"],
                    build_support_body(sp),
                    extra_script=f'      if (typeof gtag === "function") gtag("event", "support_page_view", {{ locale: CURRENT_LOCALE }});',
                )
            )
        built_count += 1

        ct = subpages[loc_key]["contact"]
        with open(os.path.join(out_dir, "contact.html"), "w", encoding="utf-8") as f:
            f.write(
                render_subpage_shell(
                    loc_key, data, locales, "contact.html",
                    ct["title"], ct["intro"], ct["h1"], "",
                    build_contact_body(ct),
                )
            )
        built_count += 1

        pv = subpages[loc_key]["privacy"]
        with open(os.path.join(out_dir, "privacy.html"), "w", encoding="utf-8") as f:
            f.write(
                render_subpage_shell(
                    loc_key, data, locales, "privacy.html",
                    pv["title"], pv["sections"][0][1], pv["h1"], "",
                    build_legal_body(pv),
                )
            )
        built_count += 1

        tm = subpages[loc_key]["terms"]
        with open(os.path.join(out_dir, "terms.html"), "w", encoding="utf-8") as f:
            f.write(
                render_subpage_shell(
                    loc_key, data, locales, "terms.html",
                    tm["title"], tm["sections"][0][1], tm["h1"], "",
                    build_legal_body(tm),
                )
            )
        built_count += 1

        rn = subpages[loc_key]["release_notes"]
        with open(os.path.join(out_dir, "release-notes.html"), "w", encoding="utf-8") as f:
            f.write(
                render_subpage_shell(
                    loc_key, data, locales, "release-notes.html",
                    rn["title"], rn["desc"], rn["h1"], rn["sub"],
                    build_release_notes_body(rn),
                )
            )
        built_count += 1

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(build_sitemap(locales))
    print(f"BUILT_ALL: {built_count} HTML pages (7 locales × 6 pages) + sitemap.xml")


if __name__ == "__main__":
    main()
