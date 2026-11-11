"""Shared contact details. Change the WhatsApp number here, then rebuild.

Every wa.me link also carries a prefilled message so a lead can be told apart
from the same number on the other site. The greeting and the closing line are
localized; the tag "(Biruni Bridge)" stays in Latin. The page name is the
document title before the site-name separator. Keep the copy in sync with
assets/site.js, which recomputes the same message in the browser.
"""

from __future__ import annotations

import re
from html import unescape
from urllib.parse import quote

WHATSAPP_DISPLAY = "+90 536 842 55 97"
WHATSAPP_WA_ME = "905368425597"
EMAIL = "info@birunibridge.com"
SITE = "https://birunibridge.com"
LANGS = ("ar", "en", "ru", "es", "fr", "ur", "fa")
CART_SLUG = "car-t-cell-therapy-turkey"

# Latin brand, then the Arabic and Persian spellings used in <title>.
_BRANDS = ("Biruni Bridge", "بيروني بريدج", "بیرونی بریج")
# hello, closing line, homepage label (the site's own crumb word).
_COPY = {
    "ar": ("مرحباً", "أريد الاستفسار", "الرئيسية"),
    "en": ("Hello", "I'd like to ask about…", "Home"),
    "es": ("Hola", "Quisiera hacer una consulta", "Inicio"),
    "fr": ("Bonjour", "Je souhaite me renseigner", "Accueil"),
    "fa": ("سلام", "می‌خواهم سؤال کنم", "خانه"),
    "pt": ("Olá", "Gostaria de obter informações", "Início"),
    "ru": ("Здравствуйте", "Хочу уточнить информацию", "Главная"),
    "tr": ("Merhaba", "Bilgi almak istiyorum", "Ana sayfa"),
    "ur": ("سلام", "میں استفسار کرنا چاہتا ہوں", "ہوم"),
}
# Href attributes on this site are double-quoted. Apostrophes stay literal
# (encodeURIComponent does not encode them) and must not end the match.
_WA_URL = re.compile(
    r"https://wa\.me/" + re.escape(WHATSAPP_WA_ME) + r'(?:\?[^"\s>]*)?'
)


def _lang(lang: str) -> str:
    code = (lang or "en").lower().split("-", 1)[0]
    return code if code in _COPY else "en"


def page_label(title: str, lang: str) -> str:
    """Short page name: the title text before the site-name separator."""
    text = re.sub(r"\s+", " ", unescape(title or "")).strip()
    home = _COPY[_lang(lang)][2]
    found = None
    for brand in _BRANDS:
        index = text.find(brand)
        if index >= 0 and (found is None or index < found):
            found = index
    if found is None:
        return text or home
    if found == 0:
        return home
    before = re.sub(r"[\s|–—:：-]+$", "", text[:found]).strip()
    return before or home


def wa_message(title: str, lang: str) -> str:
    hello, line, _home = _COPY[_lang(lang)]
    return f"{hello} (Biruni Bridge) – {page_label(title, lang)}: {line}"


def whatsapp_href(title: str, lang: str) -> str:
    """wa.me link with an encodeURIComponent-compatible text parameter."""
    encoded = quote(wa_message(title, lang), safe="-_.!~*'()")
    return f"https://wa.me/{WHATSAPP_WA_ME}?text={encoded}"


def strip_whatsapp_text(html: str) -> str:
    """Drop prefilled text so a '%' price check does not see URL encoding."""
    return _WA_URL.sub(f"https://wa.me/{WHATSAPP_WA_ME}", html)


def stamp_whatsapp_links(html: str) -> str:
    """Point every WhatsApp link on a page at this site and this page."""
    lang_match = re.search(r'<html[^>]*\blang="([^"]+)"', html, flags=re.I)
    title_match = re.search(r"<title>(.*?)</title>", html, flags=re.I | re.S)
    lang = lang_match.group(1) if lang_match else "en"
    title = title_match.group(1) if title_match else ""
    if f"https://wa.me/{WHATSAPP_WA_ME}" not in html:
        return html
    href = whatsapp_href(title, lang)
    return _WA_URL.sub(href, html)
