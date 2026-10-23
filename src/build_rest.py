#!/usr/bin/env python3
"""Translate the Arabic/English-only directory pages into ru, es, fr, ur and fa.

The English HTML is the structure and the fact source. Visible text, meta
copy, alt text, form labels and JSON-LD prose are replaced from src/rest_i18n.py.
Doctor names, insurer names, schema.org types and data-* filter values stay
as on the English page.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from build_guides import (  # noqa: E402
    _head_links,
    _patch_head_links,
    _patch_switch,
    _retarget,
    _upsert_sitemap,
)
from common import SITE  # noqa: E402
from rest_i18n import TRANSLATIONS  # noqa: E402

BUILD = ROOT / "build"
TODAY = date.today().isoformat()
LANGS = ("ru", "es", "fr", "ur", "fa")
ALL_LANGS = ("ar", "en", "ru", "es", "fr", "ur", "fa")
SLUGS = (
    "about",
    "doctors",
    "international-insurance",
    "medical-centers",
    "medical-centers/bone-marrow-transplant",
    "medical-centers/breast-health",
    "medical-centers/cardiology",
    "medical-centers/gynecologic-oncology",
    "medical-centers/hematology",
    "medical-centers/ivf",
    "medical-centers/neurosurgery",
    "medical-centers/nuclear-medicine",
    "medical-centers/organ-transplant",
    "medical-centers/orthopedics",
    "medical-centers/pediatric-hematology-oncology",
    "medical-centers/radiation-oncology",
    "medical-centers/surgical-oncology",
)
RTL = {"ur", "fa"}
_LOCALE = {"ru": "ru_RU", "es": "es_ES", "fr": "fr_FR", "ur": "ur_PK", "fa": "fa_IR"}
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
    "سب سے بہتر",
    "بہترین",
    "نمبر ایک",
    "%",
    "$",
    "€",
    "₺",
)
# Proper nouns, abbreviations and certificate names that stay in Latin.
ALLOW = {
    "biruni", "bridge", "university", "hospital", "faculty", "medicine",
    "istanbul", "whatsapp", "temos", "kvkk", "car", "pet", "mri", "ivf",
    "google", "maps", "jacie", "elekta", "versa", "imrt", "vmat", "tavi",
    "teer", "mitraclip", "evar", "tevar", "ffr", "ivus", "cabg", "hla",
    "spect", "dicom", "aml", "all", "cml", "cll", "mds", "gmp", "cd",
    "allianz", "axa", "bupa", "cigna", "aetna", "generali", "mapfre",
    "metlife", "henner", "gmmi", "europ", "assistance", "sos", "healix",
    "img", "msh", "medilink", "falck", "euro", "coris", "hansemerkur",
    "tiha", "diplomatic", "council", "birunihospital", "com", "prof",
    "doc", "assoc", "podolog", "psikolog", "dyt", "dkt", "ct", "icu",
    "germany", "june", "may", "preferred", "partner", "quality", "care",
    "international", "healthcare", "accreditation", "certificate",
    "global", "center", "no", "tr", "de", "or", "petct", "spectct",
}
LATIN = re.compile(r"[A-Za-z]{4,}")
PHRASES = sorted(
    (key for key in TRANSLATIONS["ru"] if key.count(" ") >= 1 and len(key) >= 15),
    key=len,
    reverse=True,
)


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _apply(text: str, table: dict[str, str]) -> str:
    key = _norm(text)
    if key in table:
        return table[key]
    out = text
    replaced = False
    for phrase in PHRASES:
        if phrase in out:
            out = out.replace(phrase, table[phrase])
            replaced = True
    return out if replaced else text


def _translate_json(value, table: dict[str, str], lang: str, key: str | None = None):
    if isinstance(value, dict):
        return {k: _translate_json(v, table, lang, k) for k, v in value.items()}
    if isinstance(value, list):
        return [_translate_json(v, table, lang, key) for v in value]
    if isinstance(value, str) and key != "@type":
        swapped = value.replace("/en/", f"/{lang}/")
        mapped = _apply(swapped, table)
        return mapped
    return value


def _normalize_head(head: str, lang: str, slug: str) -> str:
    def link_repl(match: re.Match) -> str:
        tag = match.group(0)
        attrs = dict(re.findall(r'([\w:-]+)="([^"]*)"', tag))
        href = attrs.get("href", "")
        rel = attrs.get("rel", "")
        if rel == "canonical":
            href = href.replace(f"/en/{slug}/", f"/{lang}/{slug}/")
            return f'<link rel="canonical" href="{href}">'
        if rel == "alternate" and "hreflang" in attrs:
            return f'<link rel="alternate" hreflang="{attrs["hreflang"]}" href="{href}">'
        if rel == "stylesheet" and href:
            return f'<link rel="stylesheet" href="{href}">'
        if rel == "icon" or attrs.get("type") == "image/svg+xml":
            extra = f' type="{attrs["type"]}"' if attrs.get("type") else ""
            return f'<link rel="{rel}" href="{href}"{extra}>'
        return tag

    head = re.sub(r"<link\b[^>]*>", link_repl, head)
    head = head.replace(
        f'content="https://birunibridge.com/en/{slug}/" property="og:url"',
        f'content="https://birunibridge.com/{lang}/{slug}/" property="og:url"',
    )
    head = head.replace('content="en_US" property="og:locale"', f'content="{_LOCALE[lang]}" property="og:locale"')
    return head


def _render(lang: str, slug: str) -> str:
    table = TRANSLATIONS[lang]
    html = (ROOT / "en" / slug / "index.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    root = soup.find("html")
    if root is None:
        raise SystemExit(f"no html tag in en/{slug}")
    root["lang"] = lang
    root["dir"] = "rtl" if lang in RTL else "ltr"
    for node in list(soup.find_all(string=True)):
        parent = node.parent
        if parent is None or parent.name in ("script", "style", "[document]"):
            continue
        raw = str(node)
        key = _norm(raw)
        if not key:
            continue
        new = _apply(raw, table)
        if new != raw:
            prefix = raw[: len(raw) - len(raw.lstrip())]
            suffix = raw[len(raw.rstrip()) :]
            node.replace_with(prefix + _norm(new) + suffix)
    for tag in soup.find_all(True):
        if tag.name in ("script", "style"):
            continue
        for attr in ("alt", "placeholder", "aria-label", "title"):
            if tag.has_attr(attr):
                tag[attr] = _apply(tag[attr], table)
        if tag.name == "meta" and (
            tag.get("name") == "description" or tag.get("property") in ("og:title", "og:description")
        ):
            tag["content"] = _apply(tag.get("content", ""), table)
    lang_input = soup.find("input", attrs={"name": "lang"})
    if lang_input is not None:
        lang_input["value"] = lang
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        if not script.string:
            continue
        data = json.loads(script.string)
        script.string = json.dumps(_translate_json(data, table, lang), ensure_ascii=False, separators=(",", ":"))
    text = str(soup)
    parts = re.split(r'(<div class="langs">.*?</div>)', text, maxsplit=1, flags=re.S)
    if len(parts) != 3:
        raise SystemExit(f"language switcher missing in {lang}/{slug}")
    switch = (
        '<div class="langs">'
        + "".join(
            f'<a class="{"on" if code == lang else ""}" href="/{code}/{slug}/" hreflang="{code}" lang="{code}">{code.upper()}</a>'
            for code in ALL_LANGS
        )
        + "</div>"
    )
    head = _normalize_head(parts[0], lang, slug)
    tail = parts[2]
    tail = re.sub(r'(<a\b[^>]*?\shref=")/en/', rf"\1/{lang}/", tail)
    tail = tail.replace('action="/en/', f'action="/{lang}/')
    text = head + switch + tail
    text = _patch_head_links(text, lang, slug)
    visible = []
    for node in soup.find_all(string=True):
        if node.parent is None or node.parent.name in ("script", "style", "[document]"):
            continue
        visible.append(str(node))
    low = " ".join(visible).lower()
    for token in FORBIDDEN:
        if token in low:
            raise SystemExit(f"{lang}/{slug} contains forbidden token {token}")
    if not re.search(rf'<html[^>]*lang="{lang}"', text):
        raise SystemExit(f"lang attribute missing for {lang}/{slug}")
    if 'name="lang"' not in text or f'value="{lang}"' not in text:
        raise SystemExit(f"form lang missing for {lang}/{slug}")
    if text.count("<main>") != 1 or text.count("</main>") != 1:
        raise SystemExit(f"unbalanced main for {lang}/{slug}")
    return text


KEEP_EXACT = {
    "Biruni Bridge",
    "Biruni University Hospital",
    "Biruni University Faculty of Medicine Hospital",
    "Biruni Üniversitesi Tıp Fakültesi Hastanesi",
    "WhatsApp",
    "WhatsApp +90 536 842 55 97",
    "TEMOS",
    "KVKK",
    "IVF",
    "PET/CT",
    "MRI",
    "CT",
    "HLA",
    "JACIE",
    "Elekta Versa HD",
    "IMRT / VMAT",
    "TAVI",
    "TEER",
    "EVAR",
    "TEVAR",
    "FFR",
    "IVUS",
    "CABG",
    "AML",
    "ALL",
    "CML",
    "CLL",
    "MDS",
    "DICOM",
    "SPECT-CT",
    "3T MRI",
    "Google Maps",
    "birunihospital.com",
    "info@birunibridge.com",
    "TR0187JUN2024",
    "Gültepe Mah. Halkalı Cd. No: 99, 34295 Küçükçekmece / İstanbul, Türkiye",
    "Gültepe Mah. Halkalı Cd. No: 99",
    "Küçükçekmece",
    "İstanbul",
    "Allianz Care",
    "AXA Global",
    "Bupa Global",
    "Cigna Global",
    "Aetna",
    "Generali",
    "MAPFRE",
    "MetLife",
    "Henner",
    "GMMI",
    "Europ Assistance",
    "International SOS",
    "Healix International",
    "IMG",
    "MSH International",
    "Medilink International",
    "Falck Global Assistance",
    "Euro Center",
    "Coris Assistance",
    "Hansemerkur",
    "Temos International Healthcare Accreditation",
    "Diplomatic Council",
}


def _visible(html: str) -> set[str]:
    soup = BeautifulSoup(html, "html.parser")
    found = set()
    for node in soup.find_all(string=True):
        if node.parent is None or node.parent.name in ("script", "style", "[document]"):
            continue
        key = _norm(str(node))
        if key:
            found.add(key)
    for tag in soup.find_all(True):
        if tag.name in ("script", "style"):
            continue
        for attr in ("alt", "placeholder", "aria-label"):
            if tag.has_attr(attr):
                key = _norm(tag[attr])
                if key:
                    found.add(key)
        if tag.name == "meta" and (
            tag.get("name") == "description" or tag.get("property") in ("og:title", "og:description")
        ):
            key = _norm(tag.get("content", ""))
            if key:
                found.add(key)
    return found


def _leftovers(lang: str, slug: str, html: str) -> list[str]:
    english = _visible((ROOT / "en" / slug / "index.html").read_text(encoding="utf-8"))
    current = _visible(html)
    table = TRANSLATIONS[lang]
    bad = []
    for item in sorted(english & current):
        if not re.search(r"[A-Za-z]", item):
            continue
        if table.get(item) == item or item in KEEP_EXACT or item in ALLOW:
            continue
        if re.search(r"(?:Prof\.|Doç\.|Dr\.|Assoc\.|Uzm\.|Op\.|Dt\.|Dyt\.|DKT\.|Podolog|Psikolog)", item):
            continue
        if re.fullmatch(r"[A-ZÇĞİÖŞÜÂÎÛ ]{2,}", item):
            continue
        if re.search(r"[^\x00-\x7f]", item) and not re.search(
            r"\b(the|and|for|with|your|from|this|that|hospital|center|health|send|about|contact|doctor|medical|treatment|patient|surgery|cancer|transplant|care|quality)\b",
            item,
            re.I,
        ):
            continue
        bad.append(item)
    return bad


def build_rest() -> int:
    count = 0
    problems = []
    for lang in LANGS:
        for slug in SLUGS:
            html = _render(lang, slug)
            problems.extend(f"{lang}/{slug}: {item}" for item in _leftovers(lang, slug, html))
            path = BUILD / lang / slug / "index.html"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(html, encoding="utf-8")
            count += 1
    if problems:
        unique = []
        seen = set()
        for item in problems:
            text = item.split(": ", 1)[-1]
            if text not in seen:
                seen.add(text)
                unique.append(text)
        Path("/tmp/missing-rest.txt").write_text("\n".join(unique), encoding="utf-8")
        preview = "\n".join(unique[:50])
        raise SystemExit(f"{len(problems)} untranslated fragments, {len(unique)} unique\n{preview}")
    print(f"built {count} directory pages")
    return count


def install_rest() -> None:
    missing = [f"{lang}/{slug}" for lang in LANGS for slug in SLUGS if not (BUILD / lang / slug / "index.html").is_file()]
    if missing:
        raise SystemExit("directory build missing; run python3 src/build_all.py first: " + ", ".join(missing[:8]))
    for lang in LANGS:
        for slug in SLUGS:
            src = BUILD / lang / slug / "index.html"
            dest = ROOT / lang / slug / "index.html"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    for lang in LANGS:
        for path in (ROOT / lang).rglob("*.html"):
            text = path.read_text(encoding="utf-8")
            original = text
            for slug in SLUGS:
                text = _retarget(text, lang, slug)
            text = text.replace('"href=', '" href=')
            text = re.sub(r"<a {2,}", "<a ", text)
            if text != original:
                path.write_text(text, encoding="utf-8")
    for lang in ALL_LANGS:
        for slug in SLUGS:
            path = ROOT / lang / slug / "index.html"
            if not path.is_file():
                raise SystemExit(f"missing installed page {path}")
            text = _patch_head_links(path.read_text(encoding="utf-8"), lang, slug)
            for code in ALL_LANGS:
                if code != lang:
                    text = _patch_switch(text, code, slug)
            # English/Arabic switchers use class="na" only when the page was missing.
            # Also point a current-language "on" link at itself if it still targets another slug.
            text = re.sub(
                rf'<a class="on" href="/{lang}/[^"]*" hreflang="{lang}" lang="{lang}">{lang.upper()}</a>',
                f'<a class="on" href="/{lang}/{slug}/" hreflang="{lang}" lang="{lang}">{lang.upper()}</a>',
                text,
                count=1,
            )
            path.write_text(text, encoding="utf-8")
    sitemap_path = ROOT / "sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8")
    for slug in SLUGS:
        sitemap = _upsert_sitemap(sitemap, slug, ALL_LANGS)
    sitemap_path.write_text(sitemap, encoding="utf-8")
    for slug in SLUGS:
        locs = sum(1 for lang in ALL_LANGS if f"<loc>{SITE}/{lang}/{slug}/</loc>" in sitemap)
        if locs != 7:
            raise SystemExit(f"sitemap {slug} locs={locs}")
    print(f"installed directory pages; sitemap urls={sitemap.count('<loc>')}")


if __name__ == "__main__":
    build_rest()
