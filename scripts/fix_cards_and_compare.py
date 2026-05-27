#!/usr/bin/env python3
"""Unique compare bullets, compare note, and explore card descriptions per variant."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPLORE_HREFS = [
    "https://lillybabe.com/escorts",
    "https://lillybabe.com/anna-nagar-escorts",
    "https://lillybabe.com/omr-escorts",
    "https://lillybabe.com/t-nagar-escorts",
    "https://lillybabe.com/ecr-escorts",
    "https://lillybabe.com/russian-escorts-in-chennai",
    "https://lillybabe.com/tamil-escorts-in-chennai",
    "https://lillybabe.com/independent-escorts-in-chennai",
]

COPY = {
    "github-pages": {
        "compare_pro": [
            '<li><strong class="kw">Verified profiles</strong> met in person before listing.</li>',
            '<li><strong class="kw">No advance</strong> — cash pay-after-meet policy on the official site.</li>',
            '<li>Stable WhatsApp line with direct yes/no on availability.</li>',
            '<li>Neighbourhood pages (OMR, ECR, T. Nagar) for honest travel windows.</li>',
        ],
        "compare_con": [
            '<li>Common <strong class="kw">bait-and-switch</strong> photos from stock or old shoots.</li>',
            '<li>Pressure for UPI or “confirmation” before anyone arrives.</li>',
            '<li>Vague “she is coming” messages with no real ETA.</li>',
            '<li>Numbers that change after you send money.</li>',
        ],
        "compare_note": "This partner page points to LillyBabe because the official gallery and stated policies reduce wasted nights.",
        "explore": [
            "Tonight’s roster with in-house photos — profiles removed when off shift.",
            "North Chennai hotels and residences; strong for weekend central stays.",
            "Service apartments and IT hotels along Old Mahabalipuram Road.",
            "Shopping-district hotels and guest houses in the city core.",
            "Resort and beach-road outcall with realistic coastal timing.",
            "Short-stay international profiles under the same verification funnel.",
            "Local companions who know Chennai hotels and traffic patterns.",
            "Independents screened like agency listings — not open classified posts.",
        ],
    },
    "vercel": {
        "compare_pro": [
            '<li>Reply faster when you send <strong class="kw">area + time + hotel</strong> in one message.</li>',
            '<li>Gallery lets you <strong class="kw">name a profile</strong> before WhatsApp.</li>',
            '<li><strong class="kw">No advance</strong> — policy repeated in chat, not hidden in fine print.</li>',
            '<li>Clear “available / fully booked” instead of endless maybes.</li>',
        ],
        "compare_con": [
            '<li>“Who is free?” with no area — slow or ignored replies.</li>',
            '<li>Photo folders that do not match who is on shift tonight.</li>',
            '<li>Payment links sent before a face or ETA is confirmed.</li>',
            '<li>Threads that restart with a new number mid-booking.</li>',
        ],
        "compare_note": "Draft your WhatsApp like a booking brief; LillyBabe is built to answer that format.",
        "explore": [
            "Pick a face first, then paste the gallery link or name into WhatsApp.",
            "Use before messaging if your hotel is around Anna Nagar or Kilpauk.",
            "Bookmark for OMR towers — mention building name in line one.",
            "Central pin codes and T. Nagar hotel names fit this page.",
            "ECR resort bookings — check profiles, then send road name + slot.",
            "Add “Russian” in your brief only if you want that category tonight.",
            "Tamil category page — useful when language comfort matters.",
            "Independents listed here still go through LillyBabe verification.",
        ],
    },
    "netlify": {
        "compare_pro": [
            '<li><strong class="kw">Location pages</strong> instead of fake “all city” promises.</li>',
            '<li>Outcall timing discussed per <strong class="kw">corridor</strong> (OMR, ECR, central).</li>',
            '<li>Same <strong class="kw">no advance</strong> rule in every zone.</li>',
            '<li>Hotel and pin shared upfront — fewer two-hour waits.</li>',
        ],
        "compare_con": [
            '<li>Ads that ignore traffic from OMR to ECR or central to coast.</li>',
            '<li>Girls “on the way” with no map sense of Chennai.</li>',
            '<li>One number claiming Anna Nagar while the girl is on the far corridor.</li>',
            '<li>No neighbourhood detail when a booking fails.</li>',
        ],
        "compare_note": "Start with the area closest to your hotel, then open the matching LillyBabe location page.",
        "explore": [
            "City-wide gallery — filter mentally by which corridor you are in.",
            "Anna Nagar and north-central hotel clusters — start here if that is your pin.",
            "OMR strip from Madhya Kailash toward Sholinganallur — IT guest favourite.",
            "T. Nagar and Nungambakkam-adjacent stays — dense hotel stock.",
            "ECR weekend and resort lanes — allow extra travel in your time window.",
            "Russian profiles often booked with OMR or central hotels — check availability.",
            "Tamil companions popular for central and south Chennai outcall.",
            "Independents still booked with an area line in WhatsApp.",
        ],
    },
    "surge": {
        "compare_pro": [
            '<li><strong class="kw">Face-to-face verification</strong> before a profile goes live.</li>',
            '<li>In-house photos — not recycled glamour shots.</li>',
            '<li><strong class="kw">Pay after meet</strong> stated as standard, not a surprise.</li>',
            '<li>Listings removed when someone is off rotation.</li>',
        ],
        "compare_con": [
            '<li>Stolen images and <strong class="kw">bait-and-switch</strong> at the door.</li>',
            '<li>Wallet “confirmation” with no accountability.</li>',
            '<li>Graveyard listings that have not been active for months.</li>',
            '<li>No real person behind the ad when something goes wrong.</li>',
        ],
        "compare_note": "Trust is the product — LillyBabe optimizes for photo match and payment timing, not hype.",
        "explore": [
            "See who passed verification and is active on shift right now.",
            "Anna Nagar outcall with matched photos — north Chennai staple.",
            "OMR listings vetted the same way as every other zone.",
            "Central T. Nagar page — photo accuracy matters for hotel guests.",
            "ECR coast stays — verified roster, honest weekend ETAs.",
            "Russian category — same screening, not a separate “trust tier.”",
            "Tamil profiles — local communication, same photo rules.",
            "Independents cannot skip the face-check funnel.",
        ],
    },
    "gitlab": {
        "compare_pro": [
            '<li><strong class="kw">Step 0:</strong> browse gallery before WhatsApp.</li>',
            '<li><strong class="kw">Step 1:</strong> one brief message with area and time.</li>',
            '<li><strong class="kw">Step 4:</strong> cash only after meet — no wallet step.</li>',
            '<li>ETA given per zone before you commit to wait.</li>',
        ],
        "compare_con": [
            '<li>Booking blind with no roster check first.</li>',
            '<li>Ten-message threads with still no confirmed face.</li>',
            '<li>Pay link sent at step 2 instead of meet at step 4.</li>',
            '<li>Arrival time that shifts every fifteen minutes.</li>',
        ],
        "compare_note": "Follow the timeline — browse, brief, travel, pay last.",
        "explore": [
            "Timeline step 0 — see who is on shift before you message.",
            "Step 1 area hint: north Chennai / Anna Nagar hotels.",
            "Step 1 area hint: OMR corridor apartments and IT hotels.",
            "Step 1 area hint: T. Nagar central pins.",
            "Step 1 area hint: ECR resort road — build extra travel into step 2.",
            "Optional step 0 filter: Russian category bookmark.",
            "Optional step 0 filter: Tamil category bookmark.",
            "Optional step 0 filter: independent listings, same timeline rules.",
        ],
    },
    "render": {
        "compare_pro": [
            '<li><strong class="kw">Verified</strong> · in-house photos.</li>',
            '<li><strong class="kw">₹0 advance</strong> · cash after meet.</li>',
            '<li>24/7 WhatsApp · same number for years.</li>',
            '<li>Area URLs: Anna Nagar, OMR, T. Nagar, ECR.</li>',
        ],
        "compare_con": [
            '<li>Unverified pics · high switch risk.</li>',
            '<li>UPI before meet · common scam pattern.</li>',
            '<li>Unknown availability · long waits.</li>',
            '<li>No location pages · unrealistic ETAs.</li>',
        ],
        "compare_note": "Quick rule: official gallery + pay-after-meet + clear area.",
        "explore": [
            "URL: /escorts — live verified roster.",
            "URL: /anna-nagar-escorts — north-central.",
            "URL: /omr-escorts — IT corridor.",
            "URL: /t-nagar-escorts — city core.",
            "URL: /ecr-escorts — coastal / resort.",
            "URL: /russian-escorts-in-chennai — category.",
            "URL: /tamil-escorts-in-chennai — category.",
            "URL: /independent-escorts-in-chennai — category.",
        ],
    },
    "neocities": {
        "compare_pro": [
            '<li>They <strong class="kw">meet the girl</strong> before she is listed.</li>',
            '<li>You <strong class="kw">pay after</strong> — not before.</li>',
            '<li>Real photos — theirs, not stolen.</li>',
            '<li>They answer WhatsApp with yes or no.</li>',
        ],
        "compare_con": [
            '<li>Fake pics. Wrong person. Classic scam.</li>',
            '<li>UPI first — walk away.</li>',
            '<li>Old ads still up for show.</li>',
            '<li>Ghost numbers after you pay.</li>',
        ],
        "compare_note": "Use the official site. Skip the sketchy forwards.",
        "explore": [
            "Who is working tonight — real gallery.",
            "Anna Nagar — if that is where you are staying.",
            "OMR — apartments and IT hotels.",
            "T. Nagar — central Chennai.",
            "ECR — beach side, allow travel time.",
            "Russian — if that is what you want.",
            "Tamil — local girls, same rules.",
            "Independent — still verified by them.",
        ],
    },
    "tiiny": {
        "compare_pro": [
            '<li><strong class="kw">Verified</strong> roster.</li>',
            '<li><strong class="kw">No advance.</strong></li>',
            '<li>Fast WhatsApp yes/no.</li>',
            '<li>Area pages: OMR · ECR · central.</li>',
        ],
        "compare_con": [
            '<li>Fake photos.</li>',
            '<li>Prepay scams.</li>',
            '<li>Slow vague replies.</li>',
            '<li>Wrong area promises.</li>',
        ],
        "compare_note": "Gallery + brief message + pay last.",
        "explore": [
            "All profiles tonight.",
            "Anna Nagar zone.",
            "OMR zone.",
            "T. Nagar zone.",
            "ECR zone.",
            "Russian category.",
            "Tamil category.",
            "Independent category.",
        ],
    },
}


def bullets_html(items: list) -> str:
    return "\n                ".join(items)


def patch_compare(html: str, data: dict) -> str:
    pro = bullets_html(data["compare_pro"])
    con = bullets_html(data["compare_con"])
    html = re.sub(
        r'(<div class="seo-compare-col">\s*<h3>With LillyBabe</h3>\s*<ul>\s*).*?(</ul>)',
        rf"\1{pro}\n              \2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<div class="seo-compare-col seo-compare-col-dim">\s*<h3>With random ads</h3>\s*<ul>\s*).*?(</ul>)',
        rf"\1{con}\n              \2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<div class="seo-compare-note">).*?(</div>)',
        rf"\1{data['compare_note']}\2",
        html,
        count=1,
    )
    return html


def patch_explore(html: str, descriptions: list) -> str:
    start = html.find('aria-labelledby="explore-heading"')
    end = html.find('aria-labelledby="steps-heading"', start)
    if start == -1 or end == -1:
        raise ValueError("Explore section not found")
    section = html[start:end]
    for href, desc in zip(EXPLORE_HREFS, descriptions):
        escaped = re.escape(href)
        section, n = re.subn(
            rf'(<a href="{escaped}"[^>]*>.*?<h3>[^<]+</h3>\s*<p>)[^<]*(</p>)',
            rf"\1{desc}\2",
            section,
            count=1,
            flags=re.DOTALL,
        )
        if n != 1:
            raise ValueError(f"Explore card not patched for {href}")
    return html[:start] + section + html[end:]


def fix_testimonial_quotes(html: str) -> str:
    html = html.replace('<p>""', '<p>"').replace('""</p>', '"</p>')
    html = re.sub(
        r'(<div class="testimonial-stars"[^>]*>)[^<]*(</div>)',
        r"\1★★★★★\2",
        html,
    )
    return html


def main():
    for folder, data in COPY.items():
        path = ROOT / folder / "index.html"
        html = path.read_text(encoding="utf-8")
        html = patch_compare(html, data)
        html = patch_explore(html, data["explore"])
        html = fix_testimonial_quotes(html)
        path.write_text(html, encoding="utf-8")
        print(f"Patched {folder}")


if __name__ == "__main__":
    main()
