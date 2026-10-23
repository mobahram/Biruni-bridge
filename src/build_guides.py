#!/usr/bin/env python3
"""Build missing guide and cellular-therapy pages into build/, then install them.

Chrome (nav, form, certificates, footer) is cloned from each language's contact
page. Article text comes from src/guide_copy.py and follows the English pages.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from common import LANGS, SITE  # noqa: E402
from guide_copy import (  # noqa: E402
    CELL,
    CELL_LANGS,
    CHECK,
    CHECK_LABEL,
    FAQ,
    GUIDE_LANGS,
    HONEYPOT,
    JOURNEY,
    ONC,
    ONC_ANCHOR,
    UI,
)

BUILD = ROOT / "build"
TODAY = date.today().isoformat()
ALL_LANGS = ("ar", "en", "ru", "es", "fr", "ur", "fa")
GUIDE_SLUGS = ("faq", "patient-journey", "check-up")
CELL_SLUG = "medical-centers/cellular-therapy"
BADGE = '<span class="xl" lang="en" title="English">EN</span>'
FORBIDDEN = (
    "kymriah",
    "yescarta",
    "tecartus",
    "abecma",
    "carvykti",
    "breyanzi",
    "aucatzyl",
    "world-class",
    "number one",
    "%",
    "$",
    "€",
    "₺",
)


def _donor(lang: str) -> str:
    return (ROOT / lang / "contact" / "index.html").read_text(encoding="utf-8")


def _svg(html: str, cls: str) -> str:
    match = re.search(rf'<svg class="{cls}".*?</svg>', html)
    if not match:
        raise SystemExit(f"missing svg {cls}")
    return match.group(0)


def _check_svg() -> str:
    return '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5" /></svg>'


def _plus_svg() -> str:
    return '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14" /> <path d="M12 5v14" /></svg>'


def _upload_svg() -> str:
    return '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" /> <polyline points="17 8 12 3 7 8" /> <line x1="12" x2="12" y1="3" y2="15" /></svg>'


def _forbid(fragment: str, label: str) -> None:
    visible = re.sub(r'\sstyle="[^"]*"', "", fragment)
    low = visible.lower()
    for word in FORBIDDEN:
        if word in low:
            raise SystemExit(f"{label} contains forbidden token {word}")


def _pairs(page: dict) -> list[tuple[str, str]]:
    if "cats" in page:
        return [(q, a) for _, items in page["cats"] for q, a in items]
    return list(page["faqs"])


def _faq_block(items: list[tuple[str, str]], open_first: bool = False) -> str:
    parts = ['<div class="faq">']
    for index, (question, answer) in enumerate(items):
        opened = " open" if open_first and index == 0 else ""
        parts.append(
            f"<details{opened}><summary>{escape(question)}{_plus_svg()}</summary><p>{answer}</p></details>"
        )
    parts.append("</div>")
    return "".join(parts)


def _buttons(ui: dict, wa: str) -> str:
    return (
        '<div class="ctas">'
        f'<a class="btn white lg" href="#form">{_upload_svg()}{escape(ui["send"])}</a>'
        f'<a class="btn outline-w lg" href="https://wa.me/905368425597" data-wa>{wa}{escape(ui["chat"])}</a>'
        "</div>"
    )


def _disc(ui: dict) -> str:
    return f'<div class="disc"><b>{escape(ui["disc_b"])}</b> {escape(ui["disc"])}</div>'


def _crumbs(lang: str, ui: dict, crumb: str, chevron: str, mid: tuple[str, str] | None = None) -> str:
    mid_html = ""
    if mid:
        mid_html = f'{chevron}<a href="/{lang}/{mid[0]}/">{escape(mid[1])}</a>'
    return (
        f'<div class="crumbs"><a href="/{lang}/">{escape(ui["home"])}</a>{mid_html}'
        f"{chevron}<b>{escape(crumb)}</b></div>"
    )


def _hero(lang: str, ui: dict, page: dict, chevron: str, image: str, alt: str, mid: tuple[str, str] | None = None) -> str:
    checks = "".join(f"<li>{_check_svg()}<span>{escape(item)}</span></li>" for item in page["points"])
    return (
        '<section class="phero"><div class="wrap">'
        + _crumbs(lang, ui, page["crumb"], chevron, mid)
        + '<div class="phg"><div><span class="pill">'
        + escape(page["crumb"])
        + "</span><h1>"
        + escape(page["h1"])
        + '</h1><p class="sub">'
        + escape(page["sub"])
        + '</p><ul class="checks">'
        + checks
        + "</ul>"
        + _buttons(ui, "")  # filled by caller if needed
        + f'</div></div><div class="ph-r"><img src="{image}" alt="{escape(alt)}"></div></div></section>'
    )


def faq_main(lang: str, ui: dict, page: dict, chevron: str, wa: str) -> str:
    nav = ['<nav class="fqnav">']
    cats = []
    for index, (name, items) in enumerate(page["cats"]):
        nav.append(
            f'<a href="#c{index}" class="{"on" if index == 0 else ""}">{escape(name)}</a>'
        )
        cats.append(
            f'<div class="fqcat" id="c{index}"><h2><span class="icb soft">{_plus_svg()}</span>{escape(name)}</h2>'
            + _faq_block(items, open_first=(index == 0))
            + "</div>"
        )
    nav.append("</nav>")
    return (
        '<section class="hlight"><div class="wrap">'
        + _crumbs(lang, ui, page["crumb"], chevron)
        + '<div class="hl"><span class="eyebrow">'
        + escape(page["crumb"])
        + "</span><h1>"
        + escape(page["h1"])
        + '</h1><p class="sub">'
        + escape(page["sub"])
        + '</p><div class="search"><input placeholder="'
        + escape(ui["search_ph"])
        + '"><button type="button" class="btn">'
        + escape(ui["search_btn"])
        + "</button></div></div></div></section>"
        + '<section class="s tight"><div class="wrap"><div class="fqgrid">'
        + "".join(nav)
        + "<div>"
        + "".join(cats)
        + _disc(ui)
        + "</div></div></div></section>"
        + '<section class="s tight"><div class="wrap"><div class="so"><img class="mark" src="/assets/logo/BiruniBridge_A_symbol_reversed.svg" alt=""><div><h2>'
        + escape(page["miss_h"])
        + "</h2><p>"
        + escape(page["miss_p"])
        + "</p></div>"
        + _buttons(ui, wa)
        + "</div></div></section>"
    )


def journey_main(lang: str, ui: dict, page: dict, chevron: str, wa: str) -> str:
    hero = _hero(lang, ui, page, chevron, "/assets/img/airport.jpg", page["img_alt"]).replace(
        _buttons(ui, ""), _buttons(ui, wa), 1
    )
    steps = []
    for index, (title, body, bullets) in enumerate(page["stages"], start=1):
        lis = "".join(f"<li>{escape(item)}</li>" for item in bullets)
        steps.append(
            f'<div class="tli"><span class="num">{index}</span><div class="jc"><h3>{escape(title)}</h3>'
            f"<p>{body}</p><ul>{lis}</ul></div></div>"
        )
    bring = "".join(f"<li>{_check_svg()}<span>{escape(item)}</span></li>" for item in page["bring"])
    return (
        hero
        + '<section class="s"><div class="wrap"><div class="shead c"><span class="eyebrow">'
        + escape(ui["stage"])
        + "</span><h2>"
        + escape(page["stages_h"])
        + '</h2></div><div class="tl">'
        + "".join(steps)
        + "</div></div></section>"
        + '<section class="s alt"><div class="wrap"><div class="shead c"><span class="eyebrow">'
        + escape(ui["video"])
        + "</span><h2>"
        + escape(page["video_h"])
        + '</h2></div><figure class="vid vone"><div class="vf"><video controls preload="none" playsinline width="1280" height="720" data-poster="/media/posters/patient-journey.webp" aria-label="'
        + escape(page["video_label"])
        + '"><source src="/media/patient-journey.mp4" type="video/mp4"></video></div><figcaption><b>'
        + escape(page["video_label"])
        + "</b><span>"
        + escape(page["video_time"])
        + "</span></figcaption></figure></div></section>"
        + '<section class="s"><div class="wrap"><h2>'
        + escape(page["bring_h"])
        + '</h2><ul class="checks">'
        + bring
        + "</ul><h2>"
        + escape(page["unsure_h"])
        + "</h2><p>"
        + escape(page["unsure_p"])
        + "</p>"
        + _buttons(ui, wa)
        + "<h2>"
        + escape(page["q_h"])
        + "</h2>"
        + _faq_block(page["faqs"], open_first=True)
        + "<p>"
        + page["cart_note"]
        + "</p>"
        + _disc(ui)
        + "</div></section>"
    )


def check_main(lang: str, ui: dict, page: dict, chevron: str, wa: str) -> str:
    hero = _hero(
        lang, ui, page, chevron, "/assets/img/tablet.jpg", page["img_alt"], ( "medical-centers", ui["centers"] )
    ).replace(_buttons(ui, ""), _buttons(ui, wa), 1)
    why = "".join(
        f'<div class="svc"><span class="icb soft">{_check_svg()}</span><h4>{escape(title)}</h4><p>{escape(text)}</p></div>'
        for title, text in page["why"]
    )
    cards = []
    rows = []
    for name, who, bullets, duration in page["packages"]:
        lis = "".join(f"<li>{escape(item)}</li>" for item in bullets)
        cards.append(
            '<div class="grp"><h3>'
            + escape(name)
            + "</h3><p><b>"
            + escape(who)
            + "</b></p><ul>"
            + lis
            + "</ul><p><b>"
            + escape(ui["duration"])
            + ":</b> "
            + escape(duration)
            + "</p><p>"
            + escape(ui["price"])
            + '</p><p><a class="more" href="#form">'
            + escape(ui["request"])
            + "</a></p></div>"
        )
        rows.append(
            "<tr><td>"
            + escape(name)
            + "</td><td>"
            + escape(who)
            + "</td><td>"
            + escape(duration)
            + "</td></tr>"
        )
    day = "".join(
        f'<div class="vstep"><span class="n">{index}</span><div><h4>{escape(title)}</h4><p>{escape(text)}</p></div></div>'
        for index, (title, text) in enumerate(page["day"], start=1)
    )
    heads = page["compare_heads"]
    return (
        hero
        + '<section class="s"><div class="wrap"><div class="shead c"><span class="eyebrow">'
        + escape(page["why_eye"])
        + "</span><h2>"
        + escape(page["why_h"])
        + '</h2></div><div class="grid4">'
        + why
        + "</div></div></section>"
        + '<section class="s alt"><div class="wrap"><div class="shead c"><span class="eyebrow">'
        + escape(page["pkg_eye"])
        + "</span><h2>"
        + escape(page["pkg_h"])
        + "</h2></div><p>"
        + escape(page["pkg_intro"])
        + " "
        + escape(ui["price"])
        + '</p><div class="groups">'
        + "".join(cards)
        + "</div><h2>"
        + escape(page["compare_h"])
        + '</h2><table class="ptable"><tr><th>'
        + escape(heads[0])
        + "</th><th>"
        + escape(heads[1])
        + "</th><th>"
        + escape(heads[2])
        + "</th></tr>"
        + "".join(rows)
        + "</table><p>"
        + escape(ui["price"])
        + "</p></div></section>"
        + '<section class="s"><div class="wrap"><div class="shead c"><span class="eyebrow">'
        + escape(page["day_eye"])
        + "</span><h2>"
        + escape(page["day_h"])
        + '</h2></div><div class="vsteps">'
        + day
        + '</div><div class="row2" style="margin-top:28px"><div><h2>'
        + escape(page["stay_h"])
        + "</h2><p>"
        + escape(page["stay_p"])
        + '</p></div><img class="staypic" src="/assets/img/istanbul.jpg" alt="'
        + escape(page["city_alt"])
        + '"></div><h2>'
        + escape(page["q_h"])
        + "</h2>"
        + _faq_block(page["faqs"], open_first=True)
        + _disc(ui)
        + "</div></section>"
    )


def cell_main(lang: str, ui: dict, page: dict, chevron: str, wa: str) -> str:
    hero = _hero(
        lang,
        ui,
        page,
        chevron,
        "/assets/img/cell.jpg",
        page["img_alt"],
        ("medical-centers", ui["centers"]),
    ).replace(_buttons(ui, ""), _buttons(ui, wa), 1)
    pillars = "".join(
        f'<div class="pillar"><div><h4>{escape(title)}</h4><p>{escape(text)}</p></div></div>'
        for title, text in page["pillars"]
    )
    bullets = "".join(f"<li>{_check_svg()}<span>{escape(item)}</span></li>" for item in page["bullets"])
    groups = "".join(f'<span class="chip">{escape(item)}</span>' for item in page["groups"])
    records = "".join(f"<li>{escape(item)}</li>" for item in page["records"])
    process = "".join(
        f'<div class="vstep"><span class="n">{index}</span><div><h4>{escape(title)}</h4><p>{escape(text)}</p></div></div>'
        for index, (title, text) in enumerate(page["process"], start=1)
    )
    journey = "".join(
        f'<div class="vstep"><span class="n">{index}</span><div><h4>{escape(title)}</h4><p>{escape(text)}</p></div></div>'
        for index, (title, text) in enumerate(page["journey"], start=1)
    )
    risks = "".join(f'<span class="chip">{escape(item)}</span>' for item in page["risks"])
    bmt = "".join(
        f'<div class="pillar"><div><h4>{escape(title)}</h4><p>{escape(text)}</p></div></div>'
        for title, text in page["bmt"]
    )
    doctors = "".join(
        f'<div class="doc"><h4>{escape(name)}</h4><p>{escape(role)}</p></div>' for name, role in page["doctors"]
    )
    return (
        hero
        + '<section class="s"><div class="wrap"><h2>'
        + escape(page["intro_h"])
        + "</h2><p>"
        + escape(page["intro_p"])
        + "</p><h2>"
        + escape(page["program_h"])
        + "</h2><p>"
        + escape(page["program_p"])
        + '</p><div class="pillars">'
        + pillars
        + "</div><p>"
        + escape(page["source"])
        + "</p><h3>"
        + escape(page["hosp_h"])
        + '</h3><ul class="checks">'
        + bullets
        + "</ul><h2>"
        + escape(page["who_h"])
        + "</h2><p>"
        + escape(page["who_p"])
        + '</p><div class="chips">'
        + groups
        + "</div><p>"
        + escape(page["who_tail"])
        + "</p><p>"
        + escape(page["who_children"])
        + "</p><h2>"
        + escape(page["rec_h"])
        + "</h2><p>"
        + escape(page["rec_intro"])
        + "</p><ul>"
        + records
        + "</ul><p>"
        + escape(page["rec_note"])
        + '</p><div class="boxcta"><small>'
        + escape(page["box_small"])
        + "</small><h3>"
        + escape(page["box_h"])
        + "</h3><p>"
        + escape(page["box_p"])
        + "</p>"
        + _buttons(ui, wa).replace("btn white lg", "btn").replace("btn outline-w lg", "btn outline")
        + "</div><h2>"
        + escape(page["process_h"])
        + '</h2><div class="vsteps">'
        + process
        + "</div><h2>"
        + escape(page["journey_h"])
        + "</h2><p>"
        + escape(page["journey_p"])
        + '</p><div class="vsteps">'
        + journey
        + "</div><h2>"
        + escape(page["risk_h"])
        + "</h2><p>"
        + escape(page["risk_p"])
        + '</p><div class="chips">'
        + risks
        + "</div><p>"
        + escape(page["risk_when"])
        + "</p><h2>"
        + escape(page["bmt_h"])
        + '</h2><div class="pillars">'
        + bmt
        + '</div><p><a class="more" href="/'
        + lang
        + '/bone-marrow-transplant-turkey/">'
        + escape(page["bmt_link"])
        + "</a></p><h2>"
        + escape(page["phys_h"])
        + '</h2><div class="docrow">'
        + doctors
        + "</div><p>"
        + escape(page["phys_note"])
        + "</p><h2>"
        + escape(page["q_h"])
        + "</h2>"
        + _faq_block(page["faqs"], open_first=True)
        + _disc(ui)
        + "</div></section>"
    )


def _json(lang: str, slug: str, h1: str, description: str, pairs: list[tuple[str, str]], crumbs: list[tuple[str, str]]) -> str:
    url = f"{SITE}/{lang}/{slug}/"
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "@id": url + "#faq",
        "url": url,
        "name": h1,
        "inLanguage": lang,
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", answer)).strip()},
            }
            for question, answer in pairs
        ],
    }
    page = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": h1,
        "description": description,
        "inLanguage": lang,
        "mainEntity": {"@id": url + "#faq"},
        "publisher": {"@id": f"{SITE}/#hospital"},
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "@id": url + "#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": index, "name": name, "item": item}
            for index, (name, item) in enumerate(crumbs, start=1)
        ],
    }
    return "".join(
        '<script type="application/ld+json">' + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "</script>"
        for payload in (faq, page, breadcrumb)
    )


def _form_card(donor: str, source: str) -> str:
    start = donor.find('<div class="fcard" id="form">')
    if start < 0:
        raise SystemExit("contact form card missing")
    depth = 0
    index = start
    end = None
    while index < len(donor):
        next_open = donor.find("<div", index)
        next_close = donor.find("</div>", index)
        if next_close < 0:
            break
        if 0 <= next_open < next_close:
            depth += 1
            index = next_open + 4
            continue
        depth -= 1
        index = next_close + len("</div>")
        if depth == 0:
            end = index
            break
    if end is None or "</form>" not in donor[start:end]:
        raise SystemExit("could not close the contact form card")
    card = donor[start:end]
    card = card.replace('name="source_page" value="contact"', f'name="source_page" value="{source}"', 1)
    if f'value="{source}"' not in card:
        raise SystemExit("could not set source_page")
    return card


def _assemble(lang: str, slug: str, page: dict, article: str, crumbs: list[tuple[str, str]]) -> str:
    donor = _donor(lang)
    ui = UI[lang]
    head, rest = donor.split("</head>", 1)
    head = head.replace("/contact/", f"/{slug}/")
    head = re.sub(r"<title>.*?</title>", f"<title>{escape(page['title'])}</title>", head, count=1)
    head = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{escape(page["description"], quote=True)}"',
        head,
        count=1,
    )
    head = re.sub(
        r'<meta property="og:title" content="[^"]*"',
        f'<meta property="og:title" content="{escape(page["title"], quote=True)}"',
        head,
        count=1,
    )
    head = re.sub(
        r'<meta property="og:description" content="[^"]*"',
        f'<meta property="og:description" content="{escape(page["description"], quote=True)}"',
        head,
        count=1,
    )
    scripts = _json(lang, slug, page["h1"], page["description"], _pairs(page), crumbs)
    head = head.replace('<meta name="theme-color" content="#0BA5C4">', '<meta name="theme-color" content="#0BA5C4">' + scripts, 1)
    body, suffix = rest.split("<main>", 1)
    body = re.sub(
        r'(<div class="langs">.*?</div>)',
        lambda match: match.group(1).replace("/contact/", f"/{slug}/"),
        body,
        count=1,
        flags=re.S,
    )
    _suffix_main, suffix = suffix.split("</main>", 1)
    contact = (
        '<section class="s alt" id="contact"><div class="wrap"><div class="final"><div><span class="eyebrow">'
        + escape(ui["contact"])
        + "</span><h2>"
        + escape(page["ask_h"])
        + '</h2><p class="lead" style="color:var(--navy-70);margin-top:12px">'
        + escape(page["ask_p"])
        + '</p><div class="contacts"><a class="ct" href="https://wa.me/905368425597" data-wa><span class="icb">'
        + _svg(donor, "ico wa-g")
        + "</span><div><b>WhatsApp</b><bdi dir=\"ltr\" class=\"wa-num\">+90 536 842 55 97</bdi></div></a>"
        + '<div class="ct"><div><b>'
        + escape(ui["email"])
        + '</b><a class="ltr" href="mailto:info@birunibridge.com">info@birunibridge.com</a></div></div></div>'
        + _disc(ui)
        + "</div>"
        + _form_card(donor, slug.split("/")[-1])
        + "</div></div></section>"
    )
    html = head + "</head>" + body + "<main>" + article + contact + "</main>" + suffix
    _forbid(article + page["title"] + page["description"], f"{lang}/{slug}")
    if html.count("<main>") != 1 or html.count("</main>") != 1:
        raise SystemExit(f"unbalanced main for {lang}/{slug}")
    return html


def _write(lang: str, slug: str, html: str) -> Path:
    path = BUILD / lang / slug / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    return path


def build_guides() -> int:
    if _pairs(FAQ["ru"]).__len__() != 28:
        raise SystemExit("Russian FAQ no longer has 28 answers")
    for lang in GUIDE_LANGS:
        if len(_pairs(FAQ[lang])) != 28:
            raise SystemExit(f"{lang} FAQ count {len(_pairs(FAQ[lang]))}")
        if len(JOURNEY[lang]["stages"]) != 6 or len(JOURNEY[lang]["faqs"]) != 4:
            raise SystemExit(f"{lang} journey shape")
        if len(CHECK[lang]["packages"]) != 5 or len(CHECK[lang]["faqs"]) != 4:
            raise SystemExit(f"{lang} check-up shape")
    count = 0
    for lang in GUIDE_LANGS:
        ui = UI[lang]
        donor = _donor(lang)
        chevron = re.search(r'<div class="crumbs">.*?(<svg class="ico".*?</svg>)', donor, flags=re.S)
        if not chevron:
            raise SystemExit(f"{lang} crumb chevron missing")
        chev = chevron.group(1)
        wa = _svg(donor, "ico wa-g")
        pages = {
            "faq": (FAQ[lang], faq_main(lang, ui, FAQ[lang], chev, wa), [(ui["home"], f"{SITE}/{lang}/"), (FAQ[lang]["crumb"], f"{SITE}/{lang}/faq/")]),
            "patient-journey": (
                JOURNEY[lang],
                journey_main(lang, ui, JOURNEY[lang], chev, wa),
                [(ui["home"], f"{SITE}/{lang}/"), (JOURNEY[lang]["crumb"], f"{SITE}/{lang}/patient-journey/")],
            ),
            "check-up": (
                CHECK[lang],
                check_main(lang, ui, CHECK[lang], chev, wa),
                [
                    (ui["home"], f"{SITE}/{lang}/"),
                    (ui["centers"], f"{SITE}/{lang}/medical-centers/"),
                    (CHECK[lang]["crumb"], f"{SITE}/{lang}/check-up/"),
                ],
            ),
        }
        for slug, (page, article, crumbs) in pages.items():
            _write(lang, slug, _assemble(lang, slug, page, article, crumbs))
            count += 1
    for lang in CELL_LANGS:
        ui = UI[lang]
        donor = _donor(lang)
        chev = re.search(r'<div class="crumbs">.*?(<svg class="ico".*?</svg>)', donor, flags=re.S).group(1)
        wa = _svg(donor, "ico wa-g")
        page = CELL[lang]
        if len(page["faqs"]) != 8 or len(page["groups"]) != 6 or len(page["journey"]) != 7:
            raise SystemExit(f"{lang} cellular shape")
        article = cell_main(lang, ui, page, chev, wa)
        crumbs = [
            (ui["home"], f"{SITE}/{lang}/"),
            (ui["centers"], f"{SITE}/{lang}/medical-centers/"),
            (page["crumb"], f"{SITE}/{lang}/{CELL_SLUG}/"),
        ]
        _write(lang, CELL_SLUG, _assemble(lang, CELL_SLUG, page, article, crumbs))
        count += 1
    print(f"built {count} guide pages")
    return count


def _head_links(lang: str, slug: str) -> str:
    bits = [f'<link rel="canonical" href="{SITE}/{lang}/{slug}/">']
    for code in ALL_LANGS:
        bits.append(f'<link rel="alternate" hreflang="{code}" href="{SITE}/{code}/{slug}/">')
    bits.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}/en/{slug}/">')
    return "".join(bits)


def _patch_head_links(text: str, lang: str, slug: str) -> str:
    pattern = re.compile(
        rf'<link rel="canonical" href="{re.escape(SITE)}/{lang}/{re.escape(slug)}/">'
        rf'(?:<link rel="alternate" hreflang="[^"]+" href="{re.escape(SITE)}/[^"]*?/{re.escape(slug)}/">)+'
    )
    new, n = pattern.subn(_head_links(lang, slug), text, count=1)
    if n != 1:
        raise SystemExit(f"hreflang block missing for {lang}/{slug}")
    return new


def _patch_switch(text: str, code: str, slug: str) -> str:
    old = f'<a class="na" href="/{code}/" hreflang="{code}" lang="{code}">{code.upper()}</a>'
    new = f'<a class="" href="/{code}/{slug}/" hreflang="{code}" lang="{code}">{code.upper()}</a>'
    if old in text:
        return text.replace(old, new, 1)
    return text


def _retarget(text: str, lang: str, slug: str) -> str:
    pattern = re.compile(rf'<a(\s[^>]*?)href="/en/{re.escape(slug)}/"([^>]*)>([\s\S]*?)</a>')

    def repl(match: re.Match) -> str:
        attrs = f"{match.group(1)} {match.group(2)}"
        attrs = attrs.replace(' hreflang="en"', "")
        attrs = re.sub(r"\s+", " ", attrs).strip()
        inner = match.group(3).replace(BADGE, "")
        inner = re.sub(r"\s+", " ", inner).strip()
        attr_html = f" {attrs}" if attrs else ""
        return f'<a{attr_html} href="/{lang}/{slug}/">{inner}</a>'

    return pattern.sub(repl, text)


def _faq_json_from_html(html: str) -> str | None:
    if '"@type":"FAQPage"' in html or '"@type": "FAQPage"' in html:
        return None
    main = re.search(r"<main[\s\S]*?</main>", html)
    if not main:
        return None
    pairs = []
    for block in re.findall(r"<details[\s\S]*?</details>", main.group(0)):
        question = re.search(r"<summary[^>]*>([\s\S]*?)</summary>", block)
        if not question:
            continue
        q = re.sub(r"<svg[\s\S]*?</svg>", "", question.group(1))
        q = re.sub(r"<[^>]+>", "", q)
        q = re.sub(r"\s+", " ", q).strip()
        answer = re.sub(r"^[\s\S]*</summary>", "", block)
        answer = re.sub(r"<[^>]+>", " ", answer)
        answer = re.sub(r"\s+", " ", answer).strip()
        if q and answer:
            pairs.append((q, answer))
    if len(pairs) < 2:
        return None
    lang = re.search(r'<html lang="([^"]+)"', html).group(1)
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', html).group(1)
    h1 = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", main.group(0))
    name = re.sub(r"<[^>]+>", "", h1.group(1)) if h1 else pairs[0][0]
    name = re.sub(r"\s+", " ", name).strip()
    payload = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "@id": canonical + "#faq",
        "url": canonical,
        "name": name,
        "inLanguage": lang,
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "</script>"


def _onc_block(lang: str) -> tuple[str, str]:
    data = ONC[lang]
    ui = UI[lang]
    items = "".join(f"<li>{_check_svg()}<span>{escape(item)}</span></li>" for item in data["docs"])
    docs = (
        "<!-- guide-onc-docs --><h2>"
        + escape(data["docs_h"])
        + '</h2><ul class="checks">'
        + items
        + '</ul><p style="margin-top:12px">'
        + escape(data["docs_p"])
        + '</p><div class="boxcta"><small>'
        + escape(data["box_small"])
        + "</small><h3>"
        + escape(data["box_h"])
        + "</h3><p>"
        + escape(data["box_p"])
        + '</p><div class="ctas"><a class="btn" href="https://wa.me/905368425597" data-wa>WhatsApp +90 536 842 55 97</a>'
        + '<a class="btn outline" href="#form">'
        + escape(ui["send"])
        + "</a></div></div>"
    )
    links = []
    for href, label in data["links"]:
        links.append(
            f'<a class="svc" href="{href}"><div><h4>{escape(label)}</h4><span class="more">{escape(ui["read"])}</span></div></a>'
        )
    rel = "<!-- guide-onc-rel --><h2>" + escape(data["rel_h"]) + '</h2><div class="grid3">' + "".join(links) + "</div>"
    _forbid(docs + rel, f"onc {lang}")
    return docs, rel


def _sitemap_alternates(slug: str) -> str:
    bits = [
        f'<xhtml:link rel="alternate" hreflang="{code}" href="{SITE}/{code}/{slug}/"/>'
        for code in ALL_LANGS
    ]
    bits.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/en/{slug}/"/>')
    return "".join(bits)


def _upsert_sitemap(text: str, slug: str, langs: tuple[str, ...]) -> str:
    def repl(match: re.Match) -> str:
        block = match.group(0)
        loc_m = re.search(r"<loc>([^<]+)</loc>", block)
        if not loc_m:
            return block
        loc = loc_m.group(1)
        path = loc.replace(SITE, "").strip("/")
        if path.split("/", 1)[-1] != slug:
            return block
        return f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>{_sitemap_alternates(slug)}</url>"

    text = re.sub(r"<url>.*?</url>", repl, text)
    for lang in langs:
        loc = f"{SITE}/{lang}/{slug}/"
        if f"<loc>{loc}</loc>" not in text:
            block = f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>{_sitemap_alternates(slug)}</url>"
            text = text.replace("</urlset>", block + "\n</urlset>")
    return text


def install_guides() -> None:
    expected = []
    for lang in GUIDE_LANGS:
        for slug in GUIDE_SLUGS:
            expected.append(BUILD / lang / slug / "index.html")
    for lang in CELL_LANGS:
        expected.append(BUILD / lang / CELL_SLUG / "index.html")
    missing = [str(path) for path in expected if not path.is_file()]
    if missing:
        raise SystemExit("guide build missing; run python3 src/build_all.py first: " + ", ".join(missing))
    for path in expected:
        target = ROOT / path.relative_to(BUILD)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

    slugs_for_lang = {lang: list(GUIDE_SLUGS) + [CELL_SLUG] for lang in GUIDE_LANGS}
    for lang in GUIDE_LANGS:
        label = CHECK_LABEL.get(lang)
        for path in (ROOT / lang).rglob("*.html"):
            text = path.read_text(encoding="utf-8")
            original = text
            for slug in slugs_for_lang[lang]:
                text = _retarget(text, lang, slug)
            if label:
                text = text.replace(">Check-up</a>", f">{label}</a>")
                text = text.replace(">Check-up </a>", f">{label}</a>")
                text = text.replace("<h3>Check-up</h3>", f"<h3>{label}</h3>")
                text = text.replace("<option>Check-up</option>", f"<option>{label}</option>")
            if lang in HONEYPOT:
                text = text.replace(">Leave empty <", f">{HONEYPOT[lang]} <")
            text = text.replace('"href=', '" href=')
            text = re.sub(r"<a {2,}", "<a ", text)
            if text != original:
                path.write_text(text, encoding="utf-8")

    owned = [(lang, slug) for lang in ALL_LANGS for slug in GUIDE_SLUGS]
    owned += [(lang, CELL_SLUG) for lang in ALL_LANGS]
    for lang, slug in owned:
        path = ROOT / lang / slug / "index.html"
        if not path.is_file():
            raise SystemExit(f"missing installed page {path}")
        text = _patch_head_links(path.read_text(encoding="utf-8"), lang, slug)
        for code in ALL_LANGS:
            if code != lang:
                text = _patch_switch(text, code, slug)
        extra = _faq_json_from_html(text)
        if extra:
            text = text.replace("</head>", extra + "</head>", 1)
        path.write_text(text, encoding="utf-8")

    for lang in GUIDE_LANGS:
        docs, rel = _onc_block(lang)
        who, final = ONC_ANCHOR[lang]
        path = ROOT / lang / "medical-centers" / "oncology" / "index.html"
        text = path.read_text(encoding="utf-8")
        if "guide-onc-docs" not in text:
            if text.count(who) != 1 or text.count(final) != 1:
                raise SystemExit(f"oncology anchors not unique in {lang}")
            text = text.replace(who, docs + who, 1).replace(final, rel + final, 1)
            path.write_text(text, encoding="utf-8")

    sitemap_path = ROOT / "sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8")
    for slug in GUIDE_SLUGS:
        sitemap = _upsert_sitemap(sitemap, slug, ALL_LANGS)
    sitemap = _upsert_sitemap(sitemap, CELL_SLUG, ALL_LANGS)
    sitemap_path.write_text(sitemap, encoding="utf-8")
    for slug in GUIDE_SLUGS + (CELL_SLUG,):
        locs = sum(1 for lang in ALL_LANGS if f"<loc>{SITE}/{lang}/{slug}/</loc>" in sitemap)
        alts = sitemap.count(f'hreflang="ur" href="{SITE}/ur/{slug}/"/>')
        if locs != 7 or alts < 7:
            raise SystemExit(f"sitemap {slug} locs={locs} ur-alts={alts}")
    print("installed guide pages, hreflang, sitemap, oncology sections")


if __name__ == "__main__":
    build_guides()
