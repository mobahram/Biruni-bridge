"""Visible-text translations for the directory pages. Keys are exact English strings."""

from __future__ import annotations

from rest_centers import CENTER_ROWS
from rest_labels import LABEL_ROWS
from rest_more import MORE_ROWS
from rest_prose import PROSE_ROWS

LANGS = ("ru", "es", "fr", "ur", "fa")


def _pack(rows: list[tuple[str, str, str, str, str, str]]) -> dict[str, dict[str, str]]:
    out = {lang: {} for lang in LANGS}
    for en, ru, es, fr, ur, fa in rows:
        if not en:
            raise SystemExit("empty English key")
        values = {"ru": ru, "es": es, "fr": fr, "ur": ur, "fa": fa}
        for lang, value in values.items():
            if en in out[lang] and out[lang][en] != value:
                raise SystemExit(f"duplicate key for {lang}: {en[:80]}")
            if not value:
                raise SystemExit(f"empty {lang} translation for {en[:80]}")
            out[lang][en] = value
    return out


TRANSLATIONS = _pack(LABEL_ROWS + PROSE_ROWS + MORE_ROWS + CENTER_ROWS)
_keys = [set(TRANSLATIONS[lang]) for lang in LANGS]
if any(keys != _keys[0] for keys in _keys):
    raise SystemExit("translation key sets differ between languages")
