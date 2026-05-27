#!/usr/bin/env python3
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from patch_variant_content import VARIANTS, img_url  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def fix_explore(folder: str, images: list) -> None:
    path = ROOT / folder / "index.html"
    html = path.read_text(encoding="utf-8")
    start = html.find('aria-labelledby="explore-heading"')
    end = html.find('aria-labelledby="steps-heading"', start)
    if start == -1 or end == -1:
        raise ValueError(f"Explore section not found in {folder}")
    section = html[start:end]
    urls = [img_url(x) for x in images]
    idx = 0

    def repl(match: re.Match) -> str:
        nonlocal idx
        if idx >= len(urls):
            return match.group(0)
        out = f'{match.group(1)}{urls[idx]}{match.group(2)}'
        idx += 1
        return out

    new_section = re.sub(
        r'(<div class="card-thumb">\s*<img src=")[^"]+(")',
        repl,
        section,
        flags=re.DOTALL,
    )
    if idx != len(urls):
        print(f"Warning: {folder} replaced {idx}/{len(urls)} explore images")
    path.write_text(html[:start] + new_section + html[end:], encoding="utf-8")
    print(f"Explore images: {folder}")


def main():
    for folder, data in VARIANTS.items():
        fix_explore(folder, data["images_explore"])


if __name__ == "__main__":
    main()
