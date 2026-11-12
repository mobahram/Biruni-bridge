#!/usr/bin/env python3
"""Install the Biruni Hospital treatment-portfolio package into the static site.

English lives at /en/treatment-portfolio/ (site convention), not /treatment-portfolio/.
Turkish and Portuguese are not invented; those URLs redirect to English.
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import SITE, stamp_whatsapp_links  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PKG = Path("/tmp/biruni-portfolio/biruni-portfolio-package")
SLUG = "treatment-portfolio"
PDF_NAME = "biruni-hospital-treatment-service-portfolio.pdf"
TODAY = "2026-11-12"
PORTFOLIO_LANGS = ("ar", "en", "es", "fa", "fr", "ru", "ur")
ALL_LANGS = ("ar", "en", "ru", "es", "fr", "ur", "fa", "tr", "pt")

LABELS = {
    "en": "Treatment portfolio",
    "ar": "دليل العلاجات",
    "es": "Portafolio de tratamientos",
    "fr": "Portfolio de traitements",
    "ru": "Портфолио лечения",
    "fa": "فهرست درمان‌ها",
    "ur": "علاج کی فہرست",
    # English labels on tr/pt chrome only — no invented translations.
    "tr": "Treatment portfolio",
    "pt": "Treatment portfolio",
}

CALLOUT = {
    "en": 'See the <a href="/en/treatment-portfolio/">full treatment and service portfolio</a> of Biruni University Hospital, also available as a PDF.',
    "ar": 'اطّلع على <a href="/ar/treatment-portfolio/">دليل علاجات وخدمات مستشفى جامعة بيروني الكامل</a>، ومتاح أيضًا كملف PDF.',
    "es": 'Consulte el <a href="/es/treatment-portfolio/">portafolio completo de tratamientos y servicios</a> del Hospital Universitario Biruni, también disponible en PDF.',
    "fr": 'Consultez le <a href="/fr/treatment-portfolio/">portfolio complet des traitements et services</a> de l’hôpital universitaire Biruni, également disponible en PDF.',
    "ru": 'Смотрите <a href="/ru/treatment-portfolio/">полное портфолио лечения и услуг</a> университетской больницы Biruni, также доступно в PDF.',
    "fa": 'فهرست کامل <a href="/fa/treatment-portfolio/">درمان‌ها و خدمات بیمارستان دانشگاهی Biruni</a> را ببینید؛ نسخهٔ PDF هم موجود است.',
    "ur": '<a href="/ur/treatment-portfolio/">بیرونی یونیورسٹی ہسپتال کے علاج اور خدمات کی مکمل فہرست</a> دیکھیں، جو PDF میں بھی دستیاب ہے۔',
}

FOOTER_H5 = {
    "en": ("Centers & treatments",),
    "ar": ("المراكز والعلاجات",),
    "es": ("Centros y tratamientos",),
    "fa": ("مراکز و درمان‌ها", "مراکز و درمان"),
    "fr": ("Centres et traitements",),
    "pt": ("Centros e tratamentos",),
    "ru": ("Центры и лечение",),
    "tr": ("Merkezler ve tedaviler",),
    "ur": ("مراکز اور علاج",),
}

CHEVRON = (
    '<svg aria-hidden="true" class="ico" viewBox="0 0 24 24">'
    '<path d="m9 18 6-6-6-6"></path></svg>'
)

SCOPED_CSS = """
.portfolio-toc{background:rgba(11,165,196,.08);padding:14px 18px;border-radius:12px;font-size:15px;line-height:1.8;margin:20px 0 28px}
.portfolio-toc a{margin:0 .1em}
.portfolio article section{margin:0 0 8px}
.portfolio article section h2{margin-top:32px;padding-bottom:6px;border-bottom:1px solid var(--line)}
.portfolio-list{columns:2;column-gap:32px;margin:12px 0 0;padding:0 0 0 1.1em}
@media(max-width:640px){.portfolio-list{columns:1}}
.portfolio details{border:1px solid var(--line);border-radius:12px;padding:10px 14px;margin:8px 0}
.portfolio summary{cursor:pointer;font-weight:600}
.portfolio .note{font-size:13px;color:var(--navy-70);margin-top:32px}
.portfolio-callout{background:rgba(11,165,196,.08);border-radius:12px;padding:14px 18px;margin:0 0 24px}
""".strip()


def pkg_page(lang: str) -> Path:
    return PKG / f"treatment-portfolio-{lang}.html"


def page_url(lang: str) -> str:
    return f"{SITE}/{lang}/{SLUG}/"


def rewrite_package_urls(text: str) -> str:
    return text.replace(f"{SITE}/treatment-portfolio/", f"{SITE}/en/{SLUG}/")


def extract(tag: str, html: str, flags: int = 0) -> str:
    m = re.search(tag, html, flags)
    if not m:
        raise SystemExit(f"missing pattern: {tag[:80]}")
    return m.group(1) if m.lastindex else m.group(0)


def crumb_home_and_centers(donor: str, lang: str) -> tuple[str, str]:
    m = re.search(
        rf'<nav aria-label="breadcrumb" class="crumbs"><a href="/{lang}/">([^<]+)</a>.*?<a href="/{lang}/medical-centers/">([^<]+)</a>',
        donor,
        re.S,
    )
    if m:
        return m.group(1), m.group(2)
    # medical-centers index current page is <b>
    m = re.search(
        rf'<div class="crumbs"><a href="/{lang}/">([^<]+)</a>.*?<(?:b|span)>([^<]+)</(?:b|span)>',
        donor,
        re.S,
    )
    if not m:
        raise SystemExit(f"crumbs not found for {lang}")
    return m.group(1), m.group(2)


def langs_html(current: str) -> str:
    parts = ['<div class="langs">']
    for code in ALL_LANGS:
        href = f"/{code}/{SLUG}/" if code in PORTFOLIO_LANGS else f"/en/{SLUG}/"
        hreflang = "pt-BR" if code == "pt" else code
        lang_attr = hreflang
        on = ' class="on"' if code == current else ' class=""'
        parts.append(
            f'<a{on} href="{href}" hreflang="{hreflang}" lang="{lang_attr}">{code.upper()}</a>'
        )
    parts.append("</div>")
    return "".join(parts)


def head_alternates() -> str:
    bits = []
    for code in PORTFOLIO_LANGS:
        hl = code
        bits.append(f'<link rel="alternate" hreflang="{hl}" href="{page_url(code)}">')
    bits.append(f'<link rel="alternate" hreflang="x-default" href="{page_url("en")}">')
    return "".join(bits)



def replace_meta(html: str, kind: str, key: str, value: str, optional: bool = False) -> str:
    """Replace a meta tag whether `content` comes before or after name/property."""
    pattern = (
        rf'<meta\s+(?:{kind}="{re.escape(key)}"\s+content="[^"]*"|'
        rf'content="[^"]*"\s+{kind}="{re.escape(key)}")\s*/?>'
    )
    repl = f'<meta {kind}="{key}" content="{value}">'
    new, n = re.subn(pattern, repl, html, count=1)
    if n != 1 and not optional:
        raise SystemExit(f"head replace failed for {kind}={key}")
    return new if n else html

def replace_head(donor: str, package: str, lang: str) -> str:
    title = extract(r"<title>(.*?)</title>", package, re.S)
    desc = extract(r'<meta name="description" content="([^"]*)"', package)
    og_title = extract(r'<meta property="og:title" content="([^"]*)"', package)
    og_desc = extract(r'<meta property="og:description" content="([^"]*)"', package)
    og_locale = extract(r'<meta property="og:locale" content="([^"]*)"', package)
    url = page_url(lang)

    def sub_one(pattern: str, repl: str, text: str, optional: bool = False) -> str:
        new, n = re.subn(pattern, repl, text, count=1, flags=re.S)
        if n != 1 and not optional:
            raise SystemExit(f"head replace failed: {pattern[:80]}")
        return new

    html = donor
    html = sub_one(r"<title>.*?</title>", f"<title>{title}</title>", html)
    html = replace_meta(html, "name", "description", desc)
    html = sub_one(
        r'<link rel="canonical" href="[^"]*"',
        f'<link rel="canonical" href="{url}"',
        html,
    )
    # Replace the whole hreflang block (donor has 9 langs + x-default).
    html = re.sub(
        r'(<link rel="alternate" hreflang="ar" href="[^"]*">(?:<link rel="alternate" hreflang="[^"]+" href="[^"]*">)+)',
        head_alternates(),
        html,
        count=1,
    )
    html = replace_meta(html, "property", "og:title", og_title)
    html = replace_meta(html, "property", "og:description", og_desc)
    html = replace_meta(html, "property", "og:url", url)
    html = replace_meta(html, "property", "og:locale", og_locale, optional=True)
    # Drop donor og:locale:alternate set? leave them — they list all site langs, fine.
    pdf = f"{SITE}/files/{PDF_NAME}"
    extra = (
        f'<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">'
        f'<link rel="alternate" type="application/pdf" href="{pdf}" '
        f'title="Biruni Hospital Advanced Treatment &amp; Service Portfolio (PDF, 4 pages)">'
        f"<style>{SCOPED_CSS}</style>"
    )
    # Package JSON-LD (already URL-rewritten) plus donor MedicalOrganization.
    pkg_ld = extract(
        r'(<script type="application/ld\+json">.*?</script>)', package, re.S
    )
    html = html.replace("</head>", pkg_ld + extra + "</head>", 1)
    return html


def portfolio_article(package: str) -> str:
    article = extract(r"<article>(.*)</article>", package, re.S)
    # Drop the package's stub contact section; the site form replaces it.
    article = re.sub(
        r'<section id="contact">.*?</section>\s*',
        "",
        article,
        count=1,
        flags=re.S,
    )
    # Use site button + scoped list/toc classes; do not ship package global CSS.
    article = article.replace('<p class="toc">', '<p class="portfolio-toc">')
    article = article.replace("<ul>", '<ul class="portfolio-list">')
    article = re.sub(
        r'<a class="btn" href="https://birunibridge\.com/files/[^"]+" download>',
        f'<a class="btn" href="/files/{PDF_NAME}" download>',
        article,
    )
    # Some languages may put download in a different attribute order (bs earlier showed download="" first).
    article = re.sub(
        rf'<a class="btn"([^>]*?)href="https://birunibridge\.com/files/{re.escape(PDF_NAME)}"',
        f'<a class="btn" href="/files/{PDF_NAME}"',
        article,
    )
    return article


def build_main(donor: str, package: str, lang: str) -> str:
    home, centers = crumb_home_and_centers(donor, lang)
    label = LABELS[lang]
    article = portfolio_article(package)
    contact = extract(
        r'(<section class="s alt" id="?contact"?>.*?</section>)', donor, re.S
    )
    crumbs = (
        f'<nav aria-label="breadcrumb" class="crumbs">'
        f'<a href="/{lang}/">{home}</a>{CHEVRON}'
        f'<a href="/{lang}/medical-centers/">{centers}</a>{CHEVRON}'
        f"<b>{label}</b></nav>"
    )
    return (
        "<main>"
        '<section class="s">'
        '<div class="wrap portfolio">'
        f"{crumbs}"
        f"<article>{article}</article>"
        "</div></section>"
        f"{contact}"
        "</main>"
    )


def replace_main(html: str, new_main: str) -> str:
    html, n = re.subn(r"<main\b[^>]*>.*?</main>", new_main, html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("failed to replace <main>")
    return html


def replace_langs(html: str, current: str) -> str:
    html, n = re.subn(
        r'<div class="langs">.*?</div>', langs_html(current), html, count=1, flags=re.S
    )
    if n != 1:
        raise SystemExit("failed to replace language switcher")
    return html


def write_page(lang: str) -> Path:
    donor = (ROOT / lang / "medical-centers" / "index.html").read_text(encoding="utf-8")
    package = rewrite_package_urls(pkg_page(lang).read_text(encoding="utf-8"))
    html = replace_head(donor, package, lang)
    html = replace_main(html, build_main(donor, package, lang))
    html = replace_langs(html, lang)
    html = stamp_whatsapp_links(html)
    dest = ROOT / lang / SLUG / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    return dest


def patch_footers() -> int:
    updated = 0
    for lang in ALL_LANGS:
        href = f"/{lang}/{SLUG}/" if lang in PORTFOLIO_LANGS else f"/en/{SLUG}/"
        label = LABELS[lang]
        item = f'<li><a href="{href}">{label}</a></li>'
        for p in (ROOT / lang).rglob("*.html"):
            text = p.read_text(encoding="utf-8")
            if f"/{SLUG}/" in text and f">{label}</a></li>" in text and "<footer" in text:
                # already patched this file
                if item in text:
                    continue
            new = text
            n_this = 0
            for h5 in FOOTER_H5[lang]:
                pat = f"<h5>{h5}</h5><ul>"
                if pat not in new:
                    continue
                new = new.replace(pat, pat + item, 1)
                n_this += 1
            if n_this:
                p.write_text(new, encoding="utf-8")
                updated += 1
            elif "<footer" in text and any(h in text for h in FOOTER_H5[lang]):
                # footer present but heading didn't match — surface it
                print(f"WARN: footer heading not patched: {p}")
    return updated


def patch_medical_centers() -> None:
    for lang in PORTFOLIO_LANGS:
        path = ROOT / lang / "medical-centers" / "index.html"
        text = path.read_text(encoding="utf-8")
        if 'class="portfolio-callout"' in text:
            continue
        needle = '<div class="tabs">'
        if needle not in text:
            raise SystemExit(f"tabs missing on {path}")
        callout = f'<p class="portfolio-callout">{CALLOUT[lang]}</p>'
        path.write_text(text.replace(needle, callout + needle, 1), encoding="utf-8")


def patch_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    if f"/{SLUG}/" in text:
        return
    alts = []
    for code in PORTFOLIO_LANGS:
        alts.append(
            f'<xhtml:link rel="alternate" hreflang="{code}" href="{page_url(code)}"/>'
        )
    alts.append(
        f'<xhtml:link rel="alternate" hreflang="x-default" href="{page_url("en")}"/>'
    )
    alt = "".join(alts)
    blocks = []
    for code in PORTFOLIO_LANGS:
        blocks.append(
            f"<url><loc>{page_url(code)}</loc><lastmod>{TODAY}</lastmod>{alt}</url>"
        )
    blocks.append(
        f"<url><loc>{SITE}/files/{PDF_NAME}</loc><lastmod>{TODAY}</lastmod></url>"
    )
    insert = "\n".join(blocks) + "\n"
    if "</urlset>" not in text:
        raise SystemExit("sitemap missing urlset close")
    path.write_text(text.replace("</urlset>", insert + "</urlset>", 1), encoding="utf-8")


def write_llms() -> None:
    path = ROOT / "llms.txt"
    snippet = (PKG / "llms-txt-snippet.txt").read_text(encoding="utf-8")
    snippet = snippet.replace(f"{SITE}/treatment-portfolio/", f"{SITE}/en/{SLUG}/")
    # Drop the Arabic instruction comment line if present.
    lines = [ln for ln in snippet.splitlines() if not ln.startswith("#")]
    body = "\n".join(lines).strip() + "\n"
    header = (
        "# Biruni Bridge\n\n"
        "Biruni Bridge (https://birunibridge.com/) coordinates international patient care "
        "with partner hospitals in Istanbul. Biruni University Hospital is a primary partner.\n\n"
        "## Pages\n\n"
    )
    if path.exists() and SLUG in path.read_text(encoding="utf-8"):
        return
    path.write_text(header + body, encoding="utf-8")


def copy_pdf() -> None:
    dest = ROOT / "files" / PDF_NAME
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.chmod(0o644)
    shutil.copy2(PKG / PDF_NAME, dest)
    dest.chmod(0o644)


def patch_netlify() -> None:
    path = ROOT / "netlify.toml"
    text = path.read_text(encoding="utf-8")
    if "/treatment-portfolio" in text:
        return
    block = """
# Treatment portfolio: English lives under /en/; no TR/PT originals in the package.
[[redirects]]
  from = "/treatment-portfolio"
  to = "/en/treatment-portfolio/"
  status = 301
[[redirects]]
  from = "/treatment-portfolio/*"
  to = "/en/treatment-portfolio/"
  status = 301
[[redirects]]
  from = "/tr/treatment-portfolio"
  to = "/en/treatment-portfolio/"
  status = 301
[[redirects]]
  from = "/tr/treatment-portfolio/*"
  to = "/en/treatment-portfolio/"
  status = 301
[[redirects]]
  from = "/pt/treatment-portfolio"
  to = "/en/treatment-portfolio/"
  status = 301
[[redirects]]
  from = "/pt/treatment-portfolio/*"
  to = "/en/treatment-portfolio/"
  status = 301
"""
    needle = "# Retired doctor directories"
    if needle not in text:
        raise SystemExit("netlify.toml hook missing")
    path.write_text(text.replace(needle, block.strip() + "\n\n" + needle, 1), encoding="utf-8")


def verify() -> None:
    for lang in PORTFOLIO_LANGS:
        p = ROOT / lang / SLUG / "index.html"
        text = p.read_text(encoding="utf-8")
        assert f'rel="canonical" href="{page_url(lang)}"' in text, lang
        assert "wa.me/905368425597" in text, lang
        assert "/files/" + PDF_NAME in text, lang
        assert 'id="form"' in text, lang
        assert 'src="/assets/site.js"' in text, lang
        assert "G-TD6H8CSGPR" in text, lang
        assert f"/{lang}/{SLUG}/" in text, lang
        # package global CSS must not have leaked (would restyle footer lists)
        assert "ul{columns:2" not in text, lang
        if lang in ("ar", "fa", "ur"):
            assert 'dir="rtl"' in text, lang
        if lang in ("en", "ru"):
            assert "113975813" in text, lang
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for lang in PORTFOLIO_LANGS:
        assert f"<loc>{page_url(lang)}</loc>" in sm, lang
    assert f"{SITE}/files/{PDF_NAME}" in sm
    assert (ROOT / "files" / PDF_NAME).is_file()
    assert (ROOT / "llms.txt").is_file()


def main() -> None:
    if not pkg_page("en").is_file():
        raise SystemExit(f"package missing at {PKG}")
    copy_pdf()
    for lang in PORTFOLIO_LANGS:
        path = write_page(lang)
        print(f"wrote {path.relative_to(ROOT)}")
    n = patch_footers()
    print(f"patched footers in {n} files")
    patch_medical_centers()
    patch_sitemap()
    write_llms()
    patch_netlify()
    verify()
    print("ok")


if __name__ == "__main__":
    main()
