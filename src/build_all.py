#!/usr/bin/env python3
"""Build the Urdu CAR-T page into build/. Does not modify the published tree.

The published repo is the static site. This generator reuses the Urdu Q&A chrome
(nav, form, certificates, footer) and the CAR-T physician/hospital JSON-LD, and
writes the Urdu page from src/qa_cart.py. Run src/deploy.py afterwards.
"""

from __future__ import annotations

import json
import re
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from common import CART_SLUG, EMAIL, LANGS, SITE, WHATSAPP_DISPLAY, WHATSAPP_WA_ME  # noqa: E402
from qa_cart import DESCRIPTION, FAQ, H1, INTRO, TITLE  # noqa: E402

BUILD = ROOT / "build"
OUT = BUILD / "ur" / CART_SLUG / "index.html"
CANCER = ROOT / "ur" / "cancer-treatment-turkey" / "index.html"
EN_CART = ROOT / "en" / CART_SLUG / "index.html"

FORBIDDEN = (
    "kymriah",
    "yescarta",
    "tecartus",
    "abecma",
    "carvykti",
    "breyanzi",
    "aucatzyl",
    "%",
    "$",
    "€",
    "₺",
    "سب سے بہتر",
    "بہترین",
    "نمبر ایک",
    "world-class",
    "number one",
)


def _svg(html: str, cls: str) -> str:
    match = re.search(rf'<svg class="{re.escape(cls)}".*?</svg>', html)
    if not match:
        raise SystemExit(f"missing svg {cls}")
    return match.group(0)


def _ldjson(html: str, needle: str) -> str:
    for block in re.findall(r'<script type="application/ld\+json">.*?</script>', html):
        if needle in block:
            return block
    raise SystemExit(f"missing JSON-LD containing {needle}")


def _faq_json() -> str:
    url = f"{SITE}/ur/{CART_SLUG}/"
    payload = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "@id": url + "#faq",
        "url": url,
        "name": H1,
        "inLanguage": "ur",
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            }
            for question, answer in FAQ
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "</script>"


def _webpage_json() -> str:
    url = f"{SITE}/ur/{CART_SLUG}/"
    payload = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": H1,
        "description": DESCRIPTION,
        "inLanguage": "ur",
        "about": {
            "@type": "MedicalTherapy",
            "name": "CAR-T cell therapy",
            "alternateName": "Chimeric antigen receptor T-cell therapy",
        },
        "mainEntity": {"@id": url + "#faq"},
        "breadcrumb": {"@id": url + "#breadcrumb"},
        "publisher": {"@id": f"{SITE}/#hospital"},
    }
    return '<script type="application/ld+json">' + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "</script>"


def _crumb_json() -> str:
    url = f"{SITE}/ur/{CART_SLUG}/"
    payload = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "@id": url + "#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ہوم", "item": f"{SITE}/ur/"},
            {
                "@type": "ListItem",
                "position": 2,
                "name": "سیلولر تھراپی اور CAR-T",
                "item": f"{SITE}/ur/medical-centers/cellular-therapy/",
            },
            {"@type": "ListItem", "position": 3, "name": "ترکی میں CAR-T سیل تھراپی", "item": url},
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "</script>"


def _answer_html(index: int, answer: str) -> str:
    if index != 10:
        return f"<p>{escape(answer)}</p>"
    phone = f'<bdi dir="ltr" class="wa-num">{escape(WHATSAPP_DISPLAY)}</bdi>'
    text = escape(answer)
    text = text.replace(escape(WHATSAPP_DISPLAY), phone)
    text = text.replace(escape(EMAIL), f'<a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a>')
    return f"<p>{text}</p>"


def _article(chrome: str) -> str:
    wa = _svg(chrome, "ico wa-g")
    upload = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" /> <polyline points="17 8 12 3 7 8" /> <line x1="12" x2="12" y1="3" y2="15" /></svg>'
    question = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" /> <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" /> <path d="M12 17h.01" /></svg>'
    chev = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m15 18-6-6 6-6" /></svg>'
    arrow = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 19-7-7 7-7" /> <path d="M19 12H5" /></svg>'
    home_ico = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v4" /> <path d="M14 14h-4" /> <path d="M14 18h-4" /> <path d="M14 8h-4" /> <path d="M18 12h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2" /> <path d="M18 22V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v18" /></svg>'
    en_badge = '<span class="xl" lang="en" title="English">EN</span>'
    blocks = []
    for number, (question_text, answer) in enumerate(FAQ, start=1):
        blocks.append(f'<h2 id="q{number}">{escape(question_text)}</h2>{_answer_html(number - 1, answer)}')
    doctors = []
    for name, image in (
        ("Prof. Dr. Ali Hakan KAYA", "/assets/doctors/ali-hakan-kaya.webp"),
        ("Prof. Dr. Rafet EREN", "/assets/doctors/rafet-eren.webp"),
    ):
        doctors.append(
            '<div class="doc" data-s="أمراض الدم" data-t="أستاذ دكتور (بروفيسور)" data-c="مركز زراعة نخاع العظم للبالغين">'
            f'<div class="av ph"><img src="{image}" alt="{escape(name)}" loading="lazy" width="120" height="120"></div>'
            f"<h4>{escape(name)}</h4><div class=\"ti\">پروفیسر</div><span class=\"sp\">امراضِ خون (ہیماٹولوجی)</span>"
            f'<div class="cn">{home_ico}بالغوں کا بون میرو ٹرانسپلانٹ سینٹر</div></div>'
        )
    related = (
        '<a href="/ur/medical-centers/cellular-therapy/">سیلولر تھراپی اور CAR-T</a>'
        '<a href="/ur/medical-centers/oncology/">آنکولوجی سینٹر</a>'
        '<a href="/ur/cancer-treatment-turkey/">ترکی میں کینسر کا علاج</a>'
        f'<a href="/en/medical-centers/bone-marrow-transplant/" hreflang="en">بون میرو ٹرانسپلانٹ {en_badge}</a>'
        '<a href="/ur/bone-marrow-transplant-turkey/">ترکی میں بون میرو ٹرانسپلانٹ</a>'
        f'<a href="/en/doctors/" hreflang="en">ڈاکٹرز کی فہرست {en_badge}</a>'
        f'<a href="/en/patient-journey/" hreflang="en">مریض کا سفر {en_badge}</a>'
        f'<a href="/en/faq/" hreflang="en">عام سوالات {en_badge}</a>'
        '<a href="#form">فارم کے ذریعے اپنی میڈیکل رپورٹ بھیجیں</a>'
    )
    return (
        '<main><div class="wrap"><nav class="crumbs" aria-label="breadcrumb">'
        f'<a href="/ur/">ہوم</a>{chev}'
        f'<a href="/ur/medical-centers/cellular-therapy/">سیلولر تھراپی اور CAR-T</a>{chev}'
        "<b>ترکی میں CAR-T سیل تھراپی</b></nav>"
        '<div class="lp"><div><div class="lp-hero"><img src="/assets/img/cell.jpg" alt=""><div class="tx">'
        f'<span class="pill">{question}سوال و جواب</span><h1>{escape(H1)}</h1><p>{escape(INTRO)}</p>'
        '<div class="ctas">'
        f'<a class="btn white" href="#form">{upload}اپنی طبی رپورٹ بھیجیں</a>'
        f'<a class="btn outline-w" href="https://wa.me/{WHATSAPP_WA_ME}" data-wa>{wa}واٹس ایپ</a>'
        "</div></div></div>"
        f'<a class="more qa-top" href="/ur/medical-centers/cellular-therapy/">{home_ico}سیلولر تھراپی اور CAR-T{arrow}</a>'
        f'<div class="qa">{"".join(blocks)}</div>'
        '<div class="ctas" style="margin-top:22px">'
        f'<a class="btn lg" href="#form">{upload}اپنی طبی رپورٹ بھیجیں</a>'
        f'<a class="btn ghost lg" href="https://wa.me/{WHATSAPP_WA_ME}" data-wa>{wa}واٹس ایپ</a>'
        "</div><h2>CAR-T پروگرام کے ڈاکٹر</h2>"
        f'<div class="docrow">{"".join(doctors)}</div>'
        f'<a class="more" style="margin-top:14px" href="/en/doctors/" hreflang="en">ڈاکٹرز کی مکمل فہرست {en_badge}{arrow}</a>'
        '<p class="note">نام، القابات اور تخصصات ہسپتال کے ڈاکٹروں کے سرکاری صفحات سے لیے گئے ہیں اور صرف معلومات کے لیے دکھائے گئے ہیں: آپ کی فائل متعلقہ شعبے کو بھیجی جاتی ہے اور معالج ڈاکٹر ہسپتال مقرر کرتا ہے۔</p>'
        f'<h2>متعلقہ مراکز اور رہنما صفحات</h2><div class="qa-rel">{related}</div>'
        '<div class="disc">صرف عمومی معلومات؛ یہ تشخیص یا علاج کی سفارش نہیں ہے۔ نتائج مریض سے مریض مختلف ہوتے ہیں اور صرف آپ کا معالج ڈاکٹر طے کر سکتا ہے کہ آپ کے لیے کیا مناسب ہے۔</div>'
        "</div>"
    )


def _check(html: str) -> None:
    lowered = html.casefold()
    for token in FORBIDDEN:
        if token.casefold() in lowered:
            raise SystemExit(f"forbidden content: {token}")
    if html.count("<h1>") != 1 or H1 not in html:
        raise SystemExit("H1 missing")
    if html.count('"@type":"FAQPage"') != 1 and html.count('"@type": "FAQPage"') != 1:
        raise SystemExit("FAQPage JSON-LD missing")
    for number in range(1, 12):
        if f'id="q{number}"' not in html:
            raise SystemExit(f"missing q{number}")
    for needle in (
        "Prof. Dr. Ali Hakan KAYA",
        "Prof. Dr. Rafet EREN",
        "TR0187JUN2024",
        "Diplomatic Council",
        "TEMOS",
        'dir="rtl"',
        'lang="ur"',
        f'name="source_page" value="{CART_SLUG}"',
        'name="lang" value="ur"',
        f"https://wa.me/{WHATSAPP_WA_ME}",
        WHATSAPP_DISPLAY,
        EMAIL,
        f'hreflang="ur" href="{SITE}/ur/{CART_SLUG}/"',
        f'href="/ur/{CART_SLUG}/"',
        'name="contact"',
        'data-netlify="true"',
    ):
        if needle not in html:
            raise SystemExit(f"missing {needle}")
    if "/ur/cancer-treatment-turkey/" not in html:
        raise SystemExit("related cancer link missing")
    if html.count(f"/ur/{CART_SLUG}/") < 8:
        raise SystemExit("expected canonical, hreflang, langs and footer links")


def render() -> str:
    if len(FAQ) != 11:
        raise SystemExit("CAR-T FAQ must have 11 questions, matching the other languages")
    html = CANCER.read_text(encoding="utf-8")
    old_title = "ترکی میں کینسر کا علاج – استنبول میں آنکولوجی | Biruni Bridge"
    old_desc = "بین الاقوامی مریضوں کے لیے ترکی اور استنبول میں کینسر کے علاج کے بارے میں جوابات: خدمات، ٹیومر بورڈ، دوسری رائے، دستاویزات، قیام اور فالو اپ۔"
    if old_title not in html or old_desc not in html:
        raise SystemExit("Urdu cancer chrome changed; update the generator markers")
    html = html.replace(old_title, TITLE).replace(old_desc, DESCRIPTION)

    canonical = f'<link rel="canonical" href="{SITE}/ur/cancer-treatment-turkey/">'
    if canonical not in html:
        raise SystemExit("canonical marker missing")
    start = html.find(canonical)
    end = html.find("<link rel=\"icon\"", start)
    html = html[:start] + html[start:end].replace("cancer-treatment-turkey", CART_SLUG) + html[end:]

    langs_start = html.find('<div class="langs">')
    langs_end = html.find("</div>", langs_start)
    langs = html[langs_start:langs_end].replace("cancer-treatment-turkey", CART_SLUG)
    html = html[:langs_start] + langs + html[langs_end:]

    en = EN_CART.read_text(encoding="utf-8")
    scripts = _faq_json() + _webpage_json() + _crumb_json() + _ldjson(en, "physician-ali-hakan-kaya") + _ldjson(en, '"@type":["Hospital"')
    html, count = re.subn(
        r'(<meta name="theme-color" content="#0BA5C4">).*?(</head>)',
        lambda match: match.group(1) + scripts + match.group(2),
        html,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit("could not replace JSON-LD")

    main_at = html.find("<main>")
    aside_at = html.find('<aside class="side">')
    if main_at < 0 or aside_at < main_at:
        raise SystemExit("could not locate main/aside")
    html = html[:main_at] + _article(html) + html[aside_at:]
    html = html.replace('name="source_page" value="cancer-treatment-turkey"', f'name="source_page" value="{CART_SLUG}"', 1)

    footer_old = '<li><a href="/ur/medical-centers/cellular-therapy/">سیلولر تھراپی اور CAR-T</a></li>'
    footer_new = footer_old + f'<li><a href="/ur/{CART_SLUG}/">ترکی میں CAR-T سیل تھراپی</a></li>'
    if footer_old not in html:
        raise SystemExit("Urdu footer marker missing")
    html = html.replace(footer_old, footer_new, 1)
    _check(html)
    if set(LANGS) != {"ar", "en", "ru", "es", "fr", "ur", "fa"}:
        raise SystemExit("language list drifted")
    return html


def main() -> None:
    html = render()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
