#!/usr/bin/env python3
"""Unique meta title/description/OG + explore card alt text per variant."""
from __future__ import annotations

import html as html_lib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from patch_variant_content import EXPLORE_HREFS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = [
    "github-pages",
    "vercel",
    "netlify",
    "surge",
    "gitlab",
    "render",
    "neocities",
    "tiiny",
]

# title, description, og_title, og_description, webpage_name, webpage_description
META: dict[str, tuple[str, str, str, str, str, str]] = {
    "github-pages": (
        "Chennai Escorts Since 2010 — Real Photos, Pay Only After You Meet",
        "LillyBabe has matched verified Chennai escorts with hotel guests since 2010. Real photos, WhatsApp booking, pay in cash only after you meet — never in advance.",
        "Chennai Escorts You Can Actually Trust — LillyBabe Since 2010",
        "Verified girls, real in-house photos, and a simple rule: you pay only after you meet. That is how LillyBabe has worked in Chennai for over a decade.",
        "Chennai Escorts Since 2010 — LillyBabe",
        "Verified Chennai escorts with real photos and pay-after-meet booking through LillyBabe since 2010.",
    ),
    "vercel": (
        "What to Write on WhatsApp When Booking Chennai Escorts",
        "Your first message sets the tone. Send your area, time, and hotel name — LillyBabe replies with who is actually free tonight. No advance, verified since 2010.",
        "Booking Chennai Escorts on WhatsApp — What to Say First",
        "Area, time, hotel name — that is all you need in your first message. LillyBabe tells you straight who is free, with no advance payment.",
        "WhatsApp Booking Guide — Chennai Escorts | LillyBabe",
        "How to message LillyBabe on WhatsApp to book verified Chennai escorts — what to include and what to expect back.",
    ),
    "netlify": (
        "Chennai Escorts Near Your Hotel — OMR, ECR, Anna Nagar & More",
        "Staying on OMR, near T. Nagar, or down ECR? LillyBabe sends verified escorts across Chennai with honest travel times — not empty promises from random ads.",
        "Find Chennai Escorts Close to Where You Are Staying",
        "Whether your hotel is on the IT corridor, in central Chennai, or along the coast — LillyBabe covers the city with verified outcall and realistic ETAs.",
        "Chennai Escorts by Area — LillyBabe",
        "Verified Chennai escort coverage by neighbourhood — OMR, ECR, Anna Nagar, T. Nagar, and central hotel zones.",
    ),
    "surge": (
        "How to Tell Real Chennai Escorts From Fake Listings",
        "Wrong girl at the door? Advance fee before she arrives? LillyBabe meets every profile face-to-face, uses their own photos, and lets you pay only after you meet.",
        "Tired of Fake Chennai Escort Photos? Read This First",
        "Face-to-face checks, in-house photography, and pay-after-meet — why LillyBabe clients keep the same WhatsApp number saved for years.",
        "Real vs Fake Chennai Escorts — LillyBabe",
        "How LillyBabe verifies Chennai escort profiles and why pay-after-meet matters when you book.",
    ),
    "gitlab": (
        "First Time Booking a Chennai Escort? Here Is the Full Flow",
        "Browse tonight's gallery, WhatsApp your area and time, get a yes or no reply, pay in cash after meet. LillyBabe has worked that way in Chennai since 2010.",
        "Book a Chennai Escort in Four Simple Steps",
        "Gallery, message, confirmation, pay after meet — no wallet transfers, no guessing games. Here is how a typical LillyBabe booking goes.",
        "How to Book Chennai Escorts — Step by Step | LillyBabe",
        "A clear four-step flow for booking verified Chennai escorts with LillyBabe via WhatsApp.",
    ),
    "render": (
        "Chennai Escort Booking Questions — Answered Plainly",
        "Do you pay in advance? How does verification work? Which areas are covered? Straight answers about LillyBabe Chennai escorts and pay-after-meet booking.",
        "Got Questions About Chennai Escorts? Start Here",
        "No advance, verified profiles, WhatsApp booking, OMR to ECR coverage — the basics about LillyBabe answered without the sales pitch.",
        "Chennai Escort FAQ — LillyBabe",
        "Plain answers to common questions about booking verified Chennai escorts with LillyBabe.",
    ),
    "neocities": (
        "Most Chennai Escort Ads Are Lies — This One Is Not",
        "Fake photos, UPI before meet, ghost numbers — you have seen it all. LillyBabe has run since 2010 on a different rule: real girls, one WhatsApp, pay when she walks in.",
        "Chennai Escorts Without the Usual Scam Script",
        "No advance fees. No recycled glamour shots. One number, verified profiles, pay after meet — that is the whole pitch, and LillyBabe has stuck to it since 2010.",
        "Chennai Escorts — Straight Talk | LillyBabe",
        "Direct information about LillyBabe verified Chennai escorts — no hype, no advance, pay after meet.",
    ),
    "tiiny": (
        "Chennai Escorts — Verified, No Advance, One WhatsApp Away",
        "LillyBabe since 2010. Real photos. Pay after meet. Message your area and time on WhatsApp — they tell you who is free tonight. No wallet transfers, ever.",
        "Verified Chennai Escorts in 30 Seconds",
        "Since 2010. No advance. WhatsApp your area and time. Pay cash only after you meet. That is LillyBabe — nothing more complicated than that.",
        "Chennai Escorts — LillyBabe Essentials",
        "The essentials on booking verified Chennai escorts with LillyBabe — no advance, pay after meet, WhatsApp booking.",
    ),
}

# Eight alts in EXPLORE_HREFS order
ALTS: dict[str, list[str]] = {
    "github-pages": [
        "Verified Chennai escort gallery on LillyBabe — active profiles with in-house photos",
        "Anna Nagar escorts Chennai — north Chennai hotel and home outcall",
        "OMR escorts Chennai — IT corridor hotels and service apartments",
        "T. Nagar escorts Chennai — central shopping district and hotel outcall",
        "ECR escorts Chennai — coastal resort and beach-road bookings",
        "Russian escorts in Chennai on LillyBabe — internationally verified category",
        "Tamil escorts in Chennai — local companions who know city hotels",
        "Independent escorts Chennai — LillyBabe-screened independents, not classifieds",
    ],
    "vercel": [
        "Open LillyBabe escort gallery before your first WhatsApp message",
        "Anna Nagar zone — mention this area when you message for a faster reply",
        "OMR zone card — share hotel or apartment name in your WhatsApp brief",
        "T. Nagar central stays — link to neighbourhood profiles on LillyBabe",
        "ECR weekend runs — allow extra travel time in your booking message",
        "Russian category on LillyBabe — same verification as other profiles",
        "Tamil category profiles — browse before naming someone on WhatsApp",
        "Independent listings screened by LillyBabe — not open-board ads",
    ],
    "netlify": [
        "Citywide verified escort roster — start here then pick your neighbourhood",
        "Anna Nagar location page — north Chennai pins and hotel names",
        "OMR location page — Old Mahabalipuram Road hotels and apartments",
        "T. Nagar location page — dense central hotel stock",
        "ECR location page — coast and resort corridor with longer ETAs",
        "Russian escorts category — international profiles on the official site",
        "Tamil escorts category — local Chennai companions by area",
        "Independent escorts category — verified independents on LillyBabe",
    ],
    "surge": [
        "Gallery with face-checked Chennai escorts — photos matched before listing",
        "Anna Nagar outcall — verified listings for north Chennai hotels",
        "OMR outcall — verified listings along the IT corridor",
        "T. Nagar outcall — verified central Chennai hotel bookings",
        "ECR outcall — coastal bookings with realistic weekend timing",
        "Russian escorts — same photo verification standard as other categories",
        "Tamil escorts — in-house photos, not recycled classified shots",
        "Independent escorts — screened listings, not anonymous forum posts",
    ],
    "gitlab": [
        "Step 1 — browse tonight's verified escort profiles on LillyBabe",
        "Step 2 — Anna Nagar: add area and hotel when you message",
        "Step 2 — OMR: add tower or hotel name for travel timing",
        "Step 2 — T. Nagar: central pin for faster confirmation",
        "Step 2 — ECR: mention resort or beach road and time window",
        "Optional category — Russian profiles on the official site",
        "Optional category — Tamil profiles on the official site",
        "Optional category — independent profiles on the official site",
    ],
    "render": [
        "Official escort gallery URL — lillybabe.com/escorts",
        "Anna Nagar area link — north Chennai coverage",
        "OMR area link — IT corridor coverage",
        "T. Nagar area link — central Chennai coverage",
        "ECR area link — coastal corridor coverage",
        "Russian escorts category link",
        "Tamil escorts category link",
        "Independent escorts category link",
    ],
    "neocities": [
        "All verified profiles — open the real gallery, not a screenshot ad",
        "Anna Nagar — if your hotel is north, start here",
        "OMR — if you are on the IT strip, start here",
        "T. Nagar — if you are downtown, start here",
        "ECR — if you are on the coast, start here and allow travel time",
        "Russian category — preference filter, same verification",
        "Tamil category — preference filter, same verification",
        "Independents — still verified, still pay after meet",
    ],
    "tiiny": [
        "Gallery — verified Chennai escorts on shift tonight",
        "Anna Nagar — north Chennai",
        "OMR — IT hotels",
        "T. Nagar — central",
        "ECR — coast",
        "Russian category",
        "Tamil category",
        "Independents",
    ],
}


def patch_meta(content: str, folder: str) -> str:
    title, desc, og_t, og_d, wp_name, wp_desc = META[folder]
    esc = html_lib.escape

    content = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", content, count=1)
    content = re.sub(
        r'(<meta name="description" content=")[^"]*(")',
        rf"\1{esc(desc)}\2",
        content,
        count=1,
    )
    content = re.sub(
        r'(<meta property="og:title" content=")[^"]*(")',
        rf"\1{esc(og_t)}\2",
        content,
        count=1,
    )
    content = re.sub(
        r'(<meta property="og:description" content=")[^"]*(")',
        rf"\1{esc(og_d)}\2",
        content,
        count=1,
    )
    content = re.sub(
        r'("@type": "WebPage",\s*"name": ")[^"]+(")',
        rf"\1{esc(wp_name)}\2",
        content,
        count=1,
    )
    content = re.sub(
        r'("@type": "WebPage",.*?"name": "[^"]+",\s*"description": ")[^"]+(")',
        rf"\1{esc(wp_desc)}\2",
        content,
        count=1,
        flags=re.DOTALL,
    )
    return content


def patch_explore_alts(content: str, folder: str) -> str:
    start = content.find('aria-labelledby="explore-heading"')
    end = content.find('aria-labelledby="steps-heading"', start)
    if start == -1 or end == -1:
        raise ValueError(f"Explore section not found in {folder}")
    section = content[start:end]
    alts = ALTS[folder]

    for href, alt in zip(EXPLORE_HREFS, alts):
        esc_alt = html_lib.escape(alt, quote=True)
        section, n = re.subn(
            rf'(<a href="{re.escape(href)}"[^>]*>.*?<img[^>]+alt=")[^"]*(")',
            rf"\1{esc_alt}\2",
            section,
            count=1,
            flags=re.DOTALL,
        )
        if n != 1:
            raise ValueError(f"{folder}: alt not patched for {href} (n={n})")

    return content[:start] + section + content[end:]


def patch_file(folder: str) -> None:
    path = ROOT / folder / "index.html"
    html = path.read_text(encoding="utf-8")
    html = patch_meta(html, folder)
    html = patch_explore_alts(html, folder)
    path.write_text(html, encoding="utf-8")
    print(f"Patched meta + explore alts: {folder}")


def main() -> None:
    for folder in FOLDERS:
        patch_file(folder)
    print("Done.")


if __name__ == "__main__":
    main()
