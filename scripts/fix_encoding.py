#!/usr/bin/env python3
"""Fix common UTF-8 mojibake in HTML and text files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Order matters: longer sequences first
REPLACEMENTS = [
    # Middle dot (UTF-8 C2 B7 misread as two chars)
    ("\u00c2\u00b7", "\u00b7"),
    # Rupee sign (UTF-8 E2 82 B9)
    ("\u00e2\u201a\u00b9", "\u20b9"),
    ("\u00e2\u20ac\u00b9", "\u20b9"),
    # Dashes and quotes
    ("\u00e2\u20ac\u201d", "\u2014"),  # em dash
    ("\u00e2\u20ac\u201c", "\u2013"),  # en dash
    ("\u00e2\u20ac\u0153", "\u201c"),  # left double quote
    ("\u00e2\u20ac\u009d", "\u201d"),  # right double quote
    ("\u00e2\u20ac\u2122", "\u2019"),  # apostrophe
    ("\u00e2\u20ac\u00a6", "\u2026"),  # ellipsis
    # Arrow (UTF-8 E2 86 92)
    ("\u00e2\u2020\u2019", "\u2192"),
    ("\u00e2\u0086\u0092", "\u2192"),
    # Stray Â before valid punctuation (double-encoding edge cases)
    ("\u00c2\u2014", "\u2014"),
    ("\u00c2\u2013", "\u2013"),
    ("\u00c2\u201c", "\u201c"),
    ("\u00c2\u201d", "\u201d"),
    ("\u00c2\u2019", "\u2019"),
]

GLOB_PATTERNS = [
    "*/index.html",
    "index.html",
    "shared/*.template",
    "*/robots.txt",
    "*/sitemap.xml",
]


def fix_text(text: str) -> str:
    for bad, good in REPLACEMENTS:
        text = text.replace(bad, good)
    return text


def main() -> None:
    paths: list[Path] = []
    for pattern in GLOB_PATTERNS:
        paths.extend(ROOT.glob(pattern))

    seen: set[Path] = set()
    for path in sorted(paths):
        if path in seen or not path.is_file():
            continue
        seen.add(path)
        raw = path.read_text(encoding="utf-8")
        fixed = fix_text(raw)
        if fixed != raw:
            path.write_text(fixed, encoding="utf-8", newline="\n")
            print(f"Fixed {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
