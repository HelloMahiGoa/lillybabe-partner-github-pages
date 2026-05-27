#!/usr/bin/env python3
"""Unique copy for compare, profile-types, and safety SEO blocks."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXTRA = {
    "github-pages": {
        "compare_h": 'Partner overview: <span>verified agency</span> vs random ads',
        "compare_i": "Why this page recommends LillyBabe over typical Chennai classified noise.",
        "types_h": 'Profile types on the <span>official gallery</span>',
        "types_i": "Categories share one verification standard — pick by preference, not by hype.",
        "safety_h": 'Practical checks before you <span>confirm</span>',
        "safety_i": "Short habits that match LillyBabe’s stated pay-after-meet policy.",
    },
    "vercel": {
        "compare_h": 'Structured booking vs <span>vague ads</span>',
        "compare_i": "How a clear WhatsApp brief compares to open-ended “who is free?” messages.",
        "types_h": 'Categories to name in <span>message line 1</span>',
        "types_i": "Mention Russian, Tamil, or independent only if it narrows your shortlist.",
        "safety_h": 'Before you tap <span>Send</span> on WhatsApp',
        "safety_i": "Confirm gallery face, area, and no-advance rule before travel starts.",
    },
    "netlify": {
        "compare_h": 'Area-first booking vs <span>citywide claims</span>',
        "compare_i": "Why neighbourhood pages beat generic “all Chennai” promises.",
        "types_h": 'Types available in <span>your corridor</span>',
        "types_i": "Not every category is in every zone tonight — area + type in one message helps.",
        "safety_h": 'Location clarity <span>reduces</span> no-shows',
        "safety_i": "Pin, hotel name, and corridor (OMR/ECR/central) set honest ETAs.",
    },
    "surge": {
        "compare_h": 'Verified roster vs <span>bait-and-switch</span> risk',
        "compare_i": "Trust differences that show up before money changes hands.",
        "types_h": 'Same vetting for <span>every category</span>',
        "types_i": "Russian, Tamil, and independent listings are not “premium trust” tiers — same checks.",
        "safety_h": 'Trust signals that <span>still</span> matter',
        "safety_i": "Photo match, no wallet prepay, and a stable WhatsApp line.",
    },
    "gitlab": {
        "compare_h": 'Timeline with agency vs <span>chaotic DMs</span>',
        "compare_i": "Ordered steps versus endless back-and-forth without availability.",
        "types_h": 'Pick type at <span>step 0</span> (browse)',
        "types_i": "Choose category on the site, then reference it in step 1 on WhatsApp.",
        "safety_h": 'Safety at <span>step 3</span> (meet)',
        "safety_i": "Pay only after meet; stop if the person does not match the gallery.",
    },
    "render": {
        "compare_h": 'Fact check: <span>LillyBabe</span> vs random listing',
        "compare_i": "Side-by-side policy and behaviour — quick reference.",
        "types_h": 'Category <span>URLs</span>',
        "types_i": "Direct links for Russian, Tamil, independent — same verification note on each.",
        "safety_h": 'Safety <span>facts</span>',
        "safety_i": "Match photo · no advance · clear area/time.",
    },
    "neocities": {
        "compare_h": 'Real agency vs <span>scammy</span> ads',
        "compare_i": "No poetry — just what changes for you.",
        "types_h": 'Types — <span>same rules</span>',
        "types_i": "Russian, Tamil, independent — all met in person first.",
        "safety_h": 'Don’t get <span>played</span>',
        "safety_i": "Wrong face or UPI upfront = walk away.",
    },
    "tiiny": {
        "compare_h": '<span>LillyBabe</span> vs random',
        "compare_i": "Verified · no advance · clear replies.",
        "types_h": 'Categories',
        "types_i": "Russian · Tamil · independent — same checks.",
        "safety_h": 'Stay <span>safe</span>',
        "safety_i": "Match photo. No prepay. Clear area.",
    },
}


def patch(path: Path, d: dict) -> None:
    html = path.read_text(encoding="utf-8")
    html = re.sub(
        r'(<h2 id="seo-compare-heading" class="section-title">).*?(</h2>)',
        rf"\1{d['compare_h']}\2",
        html,
        count=1,
    )
    html = re.sub(
        r'(<h2 id="seo-compare-heading"[^>]*>.*?</h2>\s*<p class="section-intro">).*?(</p>)',
        rf"\1{d['compare_i']}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<h2 id="seo-types-heading" class="section-title">).*?(</h2>)',
        rf"\1{d['types_h']}\2",
        html,
        count=1,
    )
    html = re.sub(
        r'(<h2 id="seo-types-heading"[^>]*>.*?</h2>\s*<p class="section-intro">).*?(</p>)',
        rf"\1{d['types_i']}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<h2 id="seo-safety-heading" class="section-title">).*?(</h2>)',
        rf"\1{d['safety_h']}\2",
        html,
        count=1,
    )
    html = re.sub(
        r'(<h2 id="seo-safety-heading"[^>]*>.*?</h2>\s*<p class="section-intro">).*?(</p>)',
        rf"\1{d['safety_i']}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(html, encoding="utf-8")


def main():
    for folder, data in EXTRA.items():
        patch(ROOT / folder / "index.html", data)
        print(f"SEO blocks: {folder}")


if __name__ == "__main__":
    main()
