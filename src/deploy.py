#!/usr/bin/env python3
"""Copy the built Urdu CAR-T page into the site and update hreflang, sitemap, and Urdu links."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from common import CART_SLUG, SITE  # noqa: E402

BUILD_PAGE = ROOT / "build" / "ur" / CART_SLUG / "index.html"
LIVE_PAGE = ROOT / "ur" / CART_SLUG / "index.html"
LANGS_WITH_PAGE = ("ar", "en", "ru", "es", "fr", "fa")
UR_HREFLANG = f'<link rel="alternate" hreflang="ur" href="{SITE}/ur/{CART_SLUG}/">'
UR_SITEMAP = f'<xhtml:link rel="alternate" hreflang="ur" href="{SITE}/ur/{CART_SLUG}/"/>'
FA_LINK = f'<link rel="alternate" hreflang="fa" href="{SITE}/fa/{CART_SLUG}/">'
FA_SITEMAP = f'<xhtml:link rel="alternate" hreflang="fa" href="{SITE}/fa/{CART_SLUG}/"/>'
SWITCH_OLD = '<a class="na" href="/ur/" hreflang="ur" lang="ur">UR</a>'
SWITCH_NEW = f'<a class="" href="/ur/{CART_SLUG}/" hreflang="ur" lang="ur">UR</a>'
FOOTER_OLD = '<li><a href="/ur/medical-centers/cellular-therapy/">سیلولر تھراپی اور CAR-T</a></li>'
FOOTER_NEW = FOOTER_OLD + f'<li><a href="/ur/{CART_SLUG}/">ترکی میں CAR-T سیل تھراپی</a></li>'
CARD_OLD = (
    'href="/ur/medical-centers/cellular-therapy/"><div class="im"><img src="/assets/img/cell.jpg" alt="">'
    '</div><div class="bd"><span class="cat">سیلولر تھراپی</span><h3>CAR-T سیل تھراپی کیا ہے؟ آسان وضاحت</h3>'
)
CARD_NEW = CARD_OLD.replace(
    'href="/ur/medical-centers/cellular-therapy/"',
    f'href="/ur/{CART_SLUG}/"',
    1,
)
QA_TOP_OLD = f'qa-top" href="/en/{CART_SLUG}/" hreflang="en">'
QA_TOP_NEW = f'qa-top" href="/ur/{CART_SLUG}/">'
QA_BADGE = 'CAR-T: آپ کے سوالات کے جوابات <span class="xl" lang="en" title="English">EN</span>'
QA_BADGE_NEW = "CAR-T: آپ کے سوالات کے جوابات "


def _replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)


def _patch_language_pages() -> int:
    changed = 0
    for lang in LANGS_WITH_PAGE:
        path = ROOT / lang / CART_SLUG / "index.html"
        text = path.read_text(encoding="utf-8")
        original = text
        if UR_HREFLANG not in text:
            text = _replace_once(text, FA_LINK, UR_HREFLANG + FA_LINK, f"{lang} hreflang")
        if SWITCH_OLD in text:
            text = _replace_once(text, SWITCH_OLD, SWITCH_NEW, f"{lang} switcher")
        elif SWITCH_NEW not in text:
            raise SystemExit(f"{lang} CAR-T page has no UR language link")
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
    return changed


def _sitemap_block() -> str:
    lastmod = date.today().isoformat()
    alternates = []
    for lang in ("ar", "en", "ru", "es", "fr", "ur", "fa"):
        alternates.append(
            f'<xhtml:link rel="alternate" hreflang="{lang}" href="{SITE}/{lang}/{CART_SLUG}/"/>'
        )
    alternates.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/en/{CART_SLUG}/"/>')
    loc = f"{SITE}/ur/{CART_SLUG}/"
    return f"<url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>{''.join(alternates)}</url>"


def _patch_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    text = text.replace(UR_SITEMAP + FA_SITEMAP, FA_SITEMAP)
    if text.count(FA_SITEMAP) not in (6, 7):
        raise SystemExit(f"unexpected CAR-T sitemap entries: {text.count(FA_SITEMAP)}")
    text = text.replace(FA_SITEMAP, UR_SITEMAP + FA_SITEMAP)
    loc = f"<loc>{SITE}/ur/{CART_SLUG}/</loc>"
    if loc not in text:
        anchor = f"<loc>{SITE}/ru/{CART_SLUG}/</loc>"
        at = text.find(anchor)
        if at < 0:
            raise SystemExit("Russian CAR-T sitemap entry missing")
        end = text.find("</url>", at)
        text = text[: end + len("</url>")] + "\n" + _sitemap_block() + text[end + len("</url>") :]
    path.write_text(text, encoding="utf-8")


def _patch_urdu_links() -> int:
    changed = 0
    for path in (ROOT / "ur").rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        original = text
        if FOOTER_OLD in text and f'href="/ur/{CART_SLUG}/">ترکی میں CAR-T سیل تھراپی' not in text:
            text = text.replace(FOOTER_OLD, FOOTER_NEW)
        if path == ROOT / "ur" / "index.html" and CARD_OLD in text:
            text = text.replace(CARD_OLD, CARD_NEW, 1)
        if path == ROOT / "ur" / "medical-centers" / "cellular-therapy" / "index.html":
            if QA_TOP_OLD in text:
                text = text.replace(QA_TOP_OLD, QA_TOP_NEW, 1)
            if QA_BADGE in text:
                text = text.replace(QA_BADGE, QA_BADGE_NEW, 1)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    if not BUILD_PAGE.is_file():
        raise SystemExit("build output missing; run python3 src/build_all.py first")
    LIVE_PAGE.parent.mkdir(parents=True, exist_ok=True)
    LIVE_PAGE.write_text(BUILD_PAGE.read_text(encoding="utf-8"), encoding="utf-8")
    pages = _patch_language_pages()
    _patch_sitemap()
    urdu = _patch_urdu_links()
    from build_guides import install_guides

    install_guides()
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    ur_locs = sitemap.count(f"<loc>{SITE}/ur/{CART_SLUG}/</loc>")
    ur_alts = sitemap.count(UR_SITEMAP)
    if ur_locs != 1 or ur_alts != 7:
        raise SystemExit(f"sitemap ur links loc={ur_locs} alts={ur_alts}, expected 1 and 7")
    print(f"deployed {LIVE_PAGE.relative_to(ROOT)}; language pages touched {pages}; urdu files touched {urdu}")


if __name__ == "__main__":
    main()
