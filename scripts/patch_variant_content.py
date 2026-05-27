#!/usr/bin/env python3
"""Apply unique copy and image rotations to each variant index.html."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Shared block markers (same across variants before patch)
EDITORIAL_START = '    <section class="section reveal" aria-labelledby="why-heading">'
EDITORIAL_END = '    <!-- SEO content sections (unique layouts) -->'

VARIANTS = {
    "github-pages": {
        "hero_lead": '<strong>LillyBabe</strong> is the long-running <a href="https://lillybabe.com">Chennai escort agency</a> behind this partner page — verified photos, pay-after-meet, and the same WhatsApp line clients have used for years.',
        "why_title": 'Why this <span>partner page</span> points to LillyBabe',
        "why_intro": "A neutral overview for searchers who land here first — and why the official site is still where bookings happen.",
        "why_paras": [
            '<p>This page exists to explain <a href="https://lillybabe.com">LillyBabe</a> in plain language before you open the main gallery. The agency has operated in Chennai since 2010 with a simple promise: the woman in the photo is the woman who arrives, and you never pay until you have met her in person.</p>',
            '<p>That is a different standard from classifieds that recycle old pictures or demand UPI before anyone shows up. LillyBabe checks profiles face-to-face, removes listings when someone is off rotation, and answers WhatsApp with a direct yes or no about who is free tonight.</p>',
            '<p>When you are ready to browse, use the live roster at <a href="https://lillybabe.com/escorts">verified escort profiles</a>. Categories — Russian, Tamil, independent, VIP — all pass the same verification funnel. Area pages for Anna Nagar, OMR, T. Nagar, and ECR help set realistic travel times across the city.</p>',
            '<p>For agency background and policies, read <a href="https://lillybabe.com/about">about LillyBabe</a>. To reach the team, use <a href="https://lillybabe.com/contact-us">contact</a> or WhatsApp on the number listed below — the same channel returning clients have saved for years.</p>',
        ],
        "seo_verified_title": 'Verified <span>Chennai escorts</span> with clear expectations',
        "seo_verified_intro": "What “verified” means on LillyBabe before you send your first message.",
        "seo_verified_p1": 'Searching for <strong class="kw">Chennai escorts</strong> is easier when you filter for <strong class="kw">active</strong> listings, <strong class="kw">matched photos</strong>, and a team that states <strong class="kw">pay after meet</strong> upfront — not after a payment link.',
        "seo_verified_p2": 'The official gallery at <a href="https://lillybabe.com/escorts"><strong class="kw">lillybabe.com/escorts</strong></a> is updated when profiles go on or off shift.',
        "seo_areas_intro": "Chennai is large; LillyBabe splits coverage into zones so outcall timing stays honest.",
        "seo_whatsapp_intro": 'Send these five details on WhatsApp for a faster <strong class="kw">Chennai escort booking</strong> reply.',
        "reviews_intro": "Recurring feedback themes from Chennai clients — paraphrased for privacy.",
        "testimonials": [
            ('"Profile matched who walked in — rare compared to other listings I tried."', "— Weekend guest, Anna Nagar"),
            ('"Paid cash only after she arrived. No advance, exactly as advertised."', "— Business traveller, OMR"),
            ('"Same WhatsApp for years; they still reply after midnight."', "— Repeat client, T. Nagar"),
        ],
        "steps_intro": "Four steps most new clients follow — usually a reply within fifteen minutes.",
        "faq": [
            ("Do I need to pay an advance?", '<p>No. LillyBabe does not take wallet transfers or “confirmation” fees before you meet someone. Cash after the session, as stated on <a href="https://lillybabe.com">lillybabe.com</a>.</p>'),
            ("How are profiles verified?", '<p>Face-to-face checks and in-house photos before a listing goes live. Inactive ads are removed. See <a href="https://lillybabe.com/escorts">the gallery</a> for who is on shift now.</p>'),
            ("Which areas of Chennai do they cover?", '<p>Hotels and homes across T. Nagar, Anna Nagar, Adyar, Guindy, OMR, ECR, Kilpauk, and more — with dedicated pages like <a href="https://lillybabe.com/anna-nagar-escorts">Anna Nagar</a> and <a href="https://lillybabe.com/omr-escorts">OMR</a>.</p>'),
            ("Is booking private?", '<p>WhatsApp is the main channel; client details are not published. Formal enquiries: <a href="https://lillybabe.com/contact-us">contact page</a>.</p>'),
            ("What is this page?", '<p>An informational partner page linking to official <a href="https://lillybabe.com">LillyBabe</a>. Bookings and rates are confirmed only on lillybabe.com or WhatsApp.</p>'),
        ],
        "explore_intro": "Deep links into the official site — gallery, neighbourhoods, and categories.",
        "images_explore": ["6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.png", "vip-girl1.png", "assets/look.jpg", "kiss.png"],
        "seo_split_img": "header.jpg",
        "seo_types_img": "banners/5.jpg",
    },
    "vercel": {
        "hero_lead": 'Use this <strong>booking guide</strong> before you message <a href="https://lillybabe.com">LillyBabe</a> — what to write on WhatsApp, what to expect, and why <strong class="kw">no advance</strong> is non-negotiable.',
        "why_title": 'How to book <span>Chennai escorts</span> without wasted chats',
        "why_intro": "A practical walkthrough for first-time and returning clients messaging LillyBabe on WhatsApp.",
        "why_paras": [
            '<p>Most slow bookings fail in the first message: no area, no time window, no idea if you need hotel outcall or incall. <a href="https://lillybabe.com">LillyBabe</a> replies faster when you treat WhatsApp like a short brief, not a novel.</p>',
            '<p>Start with neighbourhood (OMR, T. Nagar, Anna Nagar), tonight’s time slot, and whether you are at a hotel or home. Add preference — Tamil, Russian, independent — only if it matters. The team answers with who is actually on shift, not a copy-paste list from last week.</p>',
            '<p>Photos on <a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a> are taken in-house. Pick a face you like; they hold the slot while you confirm. Policy stays the same every time: <strong class="kw">pay after you meet</strong>, cash, no UPI “confirmation”.</p>',
            '<p>If you want the agency’s own wording on standards, see <a href="https://lillybabe.com/about">about</a>. For direct contact outside WhatsApp, use <a href="https://lillybabe.com/contact-us">contact</a>.</p>',
        ],
        "seo_verified_title": 'Your first message: <span>what to include</span>',
        "seo_verified_intro": "Cut reply time by sending a complete brief — LillyBabe can say yes or no in one thread.",
        "seo_verified_p1": 'For <strong class="kw">Chennai escorts</strong>, include <strong class="kw">area</strong>, <strong class="kw">time</strong>, <strong class="kw">hotel or home</strong>, and optional category. That beats asking “who is free?” with no context.',
        "seo_verified_p2": 'Live roster: <a href="https://lillybabe.com/escorts"><strong class="kw">lillybabe.com/escorts</strong></a>. Browse first, then message with a name or photo reference.',
        "seo_areas_intro": "Travel time matters — pick the zone closest to you before you ask for outcall.",
        "seo_whatsapp_intro": 'Copy this checklist into your first <strong class="kw">WhatsApp booking</strong> message.',
        "reviews_intro": "Clients often mention speed and clarity — not hype.",
        "testimonials": [
            ('"Sent area and hotel name — got two real options in ten minutes."', "— OMR service apartment"),
            ('"They told me honestly when ECR was too far for the slot I wanted."', "— Resort guest, ECR"),
            ('"No payment link before meet. Cash at the door, done."', "— First-time booker, T. Nagar"),
        ],
        "steps_intro": "Follow these four steps in order — most chats finish in under fifteen minutes.",
        "faq": [
            ("What should my first WhatsApp say?", '<p>Area, time window, hotel or home, and any category preference. Example: “OMR, 11pm, Marriott, Tamil or independent.” Then check <a href="https://lillybabe.com/escorts">escorts</a> if you want to name someone specific.</p>'),
            ("Can I book without browsing the site?", '<p>Yes — WhatsApp works. Browsing <a href="https://lillybabe.com">lillybabe.com</a> first helps you reference a profile photo when you message.</p>'),
            ("Do they charge before arrival?", '<p>No advance. LillyBabe’s stated rule is pay after meet, in cash, once you are satisfied.</p>'),
            ("How fast do they reply?", '<p>Usually within minutes at night and weekends; slower only if every girl on shift is already booked.</p>'),
            ("What is this page?", '<p>A booking-focused partner guide pointing to <a href="https://lillybabe.com">LillyBabe</a>. Official bookings happen on the main site or WhatsApp.</p>'),
        ],
        "explore_intro": "Open these pages while you draft your WhatsApp message.",
        "images_explore": ["5.jpg", "8.jpg", "9.jpg", "10.png", "3.avif", "4.avif", "background.jpg", "escort-bg.webp"],
        "seo_split_img": "banners/5.jpg",
        "seo_types_img": "vip-girl1.png",
    },
    "netlify": {
        "hero_lead": 'Planning by neighbourhood? <a href="https://lillybabe.com">LillyBabe</a> covers <strong class="kw">Chennai escorts</strong> from Anna Nagar and T. Nagar to the OMR IT strip and ECR resorts — with area pages that match real travel times.',
        "why_title": 'Chennai <span>areas</span> and how LillyBabe covers them',
        "why_intro": "A location-first look at outcall, hotels, and which official pages to open before you book.",
        "why_paras": [
            '<p>Chennai traffic can turn a “citywide” promise into a two-hour wait. <a href="https://lillybabe.com">LillyBabe</a> publishes <a href="https://lillybabe.com/locations">location hubs</a> and neighbourhood escort pages so you start in the right zone — Anna Nagar and Kilpauk in the north, T. Nagar and Nungambakkam centrally, OMR and Sholinganallur along the IT corridor, ECR toward the coast.</p>',
            '<p>Hotel outcall is common on OMR service apartments and ECR weekend stays. Central guests often use T. Nagar or Anna Nagar depending on check-in. Tell them the pin or hotel name honestly; they will say who is nearby and whether the timing works tonight.</p>',
            '<p>Every area still uses the same verification: in-house photos, active-only listings on <a href="https://lillybabe.com/escorts">escorts</a>, and <strong class="kw">no advance payment</strong>. Russian, Tamil, and independent categories are not separate quality tiers — same checks, different profiles.</p>',
            '<p>Map your stay first, then message WhatsApp with area and time. Background on the agency: <a href="https://lillybabe.com/about">about</a> · <a href="https://lillybabe.com/contact-us">contact</a>.</p>',
        ],
        "seo_verified_title": 'Start with your <span>neighbourhood</span>',
        "seo_verified_intro": "Pick an area page before you ask for outcall — it sets realistic arrival expectations.",
        "seo_verified_p1": '<strong class="kw">Chennai escorts</strong> bookings go smoother when your message names a <strong class="kw">zone</strong> (OMR, ECR, T. Nagar) tied to <a href="https://lillybabe.com/locations">official location pages</a>.',
        "seo_verified_p2": 'Then browse <a href="https://lillybabe.com/escorts"><strong class="kw">who is active</strong></a> in that part of town tonight.',
        "seo_areas_intro": "Three corridors clients book most often — each with its own LillyBabe page.",
        "seo_whatsapp_intro": 'Include <strong class="kw">area + hotel name</strong> so travel time is calculated correctly.',
        "reviews_intro": "Location accuracy comes up often in client feedback.",
        "testimonials": [
            ('"They sent someone actually near OMR — not a girl stuck across town."', "— IT park guest"),
            ('"ECR resort booking: honest ETA, no two-hour ghosting."', "— Beach road stay"),
            ('"T. Nagar hotel — arrived when they said, profile matched."', "— Central Chennai"),
        ],
        "steps_intro": "Area → gallery → WhatsApp → meet. Four steps with a geographic head start.",
        "faq": [
            ("Which LillyBabe page should I open for OMR?", '<p><a href="https://lillybabe.com/omr-escorts">OMR escorts</a> plus the main <a href="https://lillybabe.com/escorts">gallery</a>. Message with hotel or tower name.</p>'),
            ("Do they cover ECR resorts?", '<p>Yes — see <a href="https://lillybabe.com/ecr-escorts">ECR escorts</a>. Weekend traffic can affect ETA; they usually say that upfront.</p>'),
            ("Anna Nagar vs T. Nagar — does it matter?", '<p>Yes for travel time. Use <a href="https://lillybabe.com/anna-nagar-escorts">Anna Nagar</a> or <a href="https://lillybabe.com/t-nagar-escorts">T. Nagar</a> pages when you know your hotel zone.</p>'),
            ("Is pay-after-meet the same in every area?", '<p>Same policy citywide — no advance on <a href="https://lillybabe.com">lillybabe.com</a>.</p>'),
            ("What is this page?", '<p>A location-focused partner page for <a href="https://lillybabe.com">LillyBabe</a> Chennai coverage.</p>'),
        ],
        "explore_intro": "Neighbourhood and category entry points on the official site.",
        "images_explore": ["1.avif", "2.avif", "3.avif", "4.avif", "7.jpg", "8.jpg", "locations.avif", "header.jpg"],
        "seo_split_img": "locations.avif",
        "seo_types_img": "escort-bg.webp",
    },
    "surge": {
        "hero_lead": 'Skeptical of Chennai listings? <a href="https://lillybabe.com">LillyBabe</a> built its name on <strong class="kw">verified escorts</strong>, in-house photos, and a pay-only-after-you-meet rule — no advance, no bait-and-switch.',
        "why_title": 'Trust, verification, and <span>why it matters</span>',
        "why_intro": "An editorial look at how LillyBabe reduces bait-and-switch risk compared to random ads.",
        "why_paras": [
            '<p>The usual failure mode in <strong class="kw">Chennai escort</strong> classifieds is predictable: stolen photos, a different person at the door, then pressure for UPI before anyone arrives. <a href="https://lillybabe.com">LillyBabe</a> was structured around the opposite — meet the woman before she is listed, match gallery to face, pull the ad when she is off rotation.</p>',
            '<p>“Verified” here is not a badge graphic. It means someone from the team has sat across from her, confirmed she is booking in Tamil Nadu now, and shot the images you see on <a href="https://lillybabe.com/escorts">escorts</a>. That is why repeat clients cite photo accuracy more than marketing copy.</p>',
            '<p>Payment policy is part of trust too: <strong class="kw">cash after meet</strong>, no wallet “confirmation.” If a chat pushes advance payment, it is not LillyBabe policy — walk away and use the official <a href="https://lillybabe.com/contact-us">contact</a> line instead.</p>',
            '<p>Read their story in their words on <a href="https://lillybabe.com/about">about</a>. When you are comfortable, message WhatsApp with area and time — same accountability as the main brand since 2010.</p>',
        ],
        "seo_verified_title": 'What <span>verified</span> means here',
        "seo_verified_intro": "Verification is process, not a label — this is how LillyBabe applies it.",
        "seo_verified_p1": 'For <strong class="kw">Chennai escorts</strong>, verification means <strong class="kw">in-person screening</strong>, <strong class="kw">matched photos</strong>, and listings removed when someone is unavailable.',
        "seo_verified_p2": 'See the current vetted roster at <a href="https://lillybabe.com/escorts"><strong class="kw">lillybabe.com/escorts</strong></a> — not archived faces.',
        "seo_areas_intro": "Trust does not remove geography — these zones still need honest travel windows.",
        "seo_whatsapp_intro": 'Red flags vs normal <strong class="kw">LillyBabe WhatsApp</strong> flow.',
        "reviews_intro": "Trust and photo match dominate paraphrased reviews.",
        "testimonials": [
            ('"Finally a listing where the face matched — I stopped using random ads."', "— Anna Nagar hotel"),
            ('"Refused advance when another number asked UPI. LillyBabe stuck to cash after."', "— OMR client"),
            ('"Profile was gone next week when she was off — felt maintained, not abandoned."', "— Gallery browser"),
        ],
        "steps_intro": "Verify on site → message → meet → pay. No wallet step in the middle.",
        "faq": [
            ("How is LillyBabe different from Telegram listings?", '<p>In-house verification, active roster maintenance, and stated <strong class="kw">no advance</strong> on <a href="https://lillybabe.com">lillybabe.com</a>.</p>'),
            ("What if photos do not match?", '<p>Stop the booking. Policy is face-checked profiles; report via <a href="https://lillybabe.com/contact-us">contact</a>.</p>'),
            ("Why no advance payment?", '<p>Reduces scam risk for both sides; pay cash after meet once you are satisfied.</p>'),
            ("Are Russian profiles verified the same way?", '<p>Same funnel — see <a href="https://lillybabe.com/russian-escorts-in-chennai">Russian escorts</a>.</p>'),
            ("What is this page?", '<p>A trust-focused partner editorial linking to <a href="https://lillybabe.com">LillyBabe</a>.</p>'),
        ],
        "explore_intro": "Official pages that back up verification and policy claims.",
        "images_explore": ["10.png", "6.jpg", "5.jpg", "7.jpg", "9.jpg", "8.jpg", "hero-bg.webp", "background.jpg"],
        "seo_split_img": "background.jpg",
        "seo_types_img": "banners/4.avif",
    },
    "gitlab": {
        "hero_lead": 'From first WhatsApp to cash payment — here is the <strong>LillyBabe</strong> <a href="https://lillybabe.com">Chennai escort</a> timeline: browse, confirm, meet, pay after.',
        "why_title": 'The booking <span>timeline</span> step by step',
        "why_intro": "Chronological view of a typical LillyBabe night — what happens when, and where delays usually come from.",
        "why_paras": [
            '<p><strong>Step 0 — Browse.</strong> Open <a href="https://lillybabe.com/escorts">escorts</a> and note who is on shift. Photos are current; inactive profiles disappear instead of cluttering the grid.</p>',
            '<p><strong>Step 1 — Brief on WhatsApp.</strong> Message <a href="https://lillybabe.com">LillyBabe</a> with area, time, hotel or home, and optional category. They reply with availability — yes, no, or “later slot.”</p>',
            '<p><strong>Step 2 — Hold and travel.</strong> They confirm ETA for OMR, ECR, or central Chennai honestly. You lock hotel details or incall address.</p>',
            '<p><strong>Step 3 — Meet and pay.</strong> She arrives; you pay cash only after you are satisfied. No advance at any point — same rule since 2010.</p>',
            '<p>Delays usually mean missing area or time in step 1. Agency background: <a href="https://lillybabe.com/about">about</a> · <a href="https://lillybabe.com/contact-us">contact</a>.</p>',
        ],
        "seo_verified_title": 'Timeline: <span>before</span> you message',
        "seo_verified_intro": "Do this on the site first so step 1 on WhatsApp is one message, not ten.",
        "seo_verified_p1": 'Pick from <strong class="kw">verified Chennai escorts</strong> on <a href="https://lillybabe.com/escorts"><strong class="kw">lillybabe.com/escorts</strong></a> — reference a name or photo in WhatsApp.',
        "seo_verified_p2": 'Confirm <strong class="kw">pay after meet</strong> policy on <a href="https://lillybabe.com">the homepage</a> so expectations match before travel starts.',
        "seo_areas_intro": "Timeline branches by zone — choose the page closest to your hotel.",
        "seo_whatsapp_intro": 'Message template aligned to the <strong class="kw">booking timeline</strong>.',
        "reviews_intro": "Clients describe the flow more than individual compliments.",
        "testimonials": [
            ('"Browsed gallery, named her on WhatsApp, she showed up — clean process."', "— OMR timeline"),
            ('"They said 45 min to ECR and arrived at 50 — honest window."', "— ECR booking"),
            ('"Paid last, not first. That order mattered to me."', "— T. Nagar"),
        ],
        "steps_intro": "Expanded timeline — same four beats, more detail per step.",
        "faq": [
            ("What is step 1 on WhatsApp?", '<p>Area, time, hotel/home, preferences. See <a href="https://lillybabe.com/escorts">escorts</a> first if you want to name someone.</p>'),
            ("When do I pay?", '<p>After meet, in cash — never before arrival on <a href="https://lillybabe.com">LillyBabe</a>.</p>'),
            ("Can I skip browsing and message cold?", '<p>Yes, but naming a profile speeds step 1.</p>'),
            ("What causes delays?", '<p>Vague location, peak-hour OMR/ECR traffic, or fully booked shifts.</p>'),
            ("What is this page?", '<p>A timeline-style partner page for <a href="https://lillybabe.com">LillyBabe</a> bookings.</p>'),
        ],
        "explore_intro": "Pages to open at each stage of the timeline.",
        "images_explore": ["8.jpg", "9.jpg", "6.jpg", "10.png", "2.avif", "1.avif", "kiss.png", "assets/look.jpg"],
        "seo_split_img": "banners/3.avif",
        "seo_types_img": "banners/2.avif",
    },
    "render": {
        "hero_lead": '<strong>Quick facts:</strong> <a href="https://lillybabe.com">LillyBabe</a> · Chennai since 2010 · verified <strong class="kw">escorts</strong> · 24/7 WhatsApp · ₹0 advance · pay after meet · <a href="https://lillybabe.com/escorts">live gallery</a>.',
        "why_title": 'LillyBabe <span>at a glance</span>',
        "why_intro": "Reference sheet — policies, links, and coverage without the long read.",
        "why_paras": [
            '<p><strong>Brand:</strong> <a href="https://lillybabe.com">LillyBabe</a> — Chennai escort agency, operating since 2010.</p>',
            '<p><strong>Policy:</strong> Verified profiles · in-house photos · <strong class="kw">no advance</strong> · <strong class="kw">cash pay after meet</strong> · WhatsApp booking.</p>',
            '<p><strong>Gallery:</strong> <a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a> — active listings only; Russian, Tamil, independent, VIP categories.</p>',
            '<p><strong>Areas:</strong> Anna Nagar · T. Nagar · OMR · ECR · <a href="https://lillybabe.com/locations">full locations</a> · hotel outcall and incall.</p>',
            '<p><strong>Contact:</strong> <a href="https://lillybabe.com/contact-us">contact</a> · WhatsApp +91 81214 26651 · <a href="https://lillybabe.com/about">about</a>.</p>',
        ],
        "seo_verified_title": 'Fact sheet: <span>verification</span>',
        "seo_verified_intro": "Bullet facts — what verified means on LillyBabe.",
        "seo_verified_p1": '<strong class="kw">Chennai escorts</strong> = face check + matched photos + removed when off shift.',
        "seo_verified_p2": 'Roster: <a href="https://lillybabe.com/escorts"><strong class="kw">lillybabe.com/escorts</strong></a>.',
        "seo_areas_intro": "Coverage facts by corridor — tap the matching official page.",
        "seo_whatsapp_intro": 'Minimum message fields for a <strong class="kw">fast reply</strong>.',
        "reviews_intro": "Short factual feedback — paraphrased.",
        "testimonials": [
            ('"No advance — fact checked on arrival."', "— Hotel guest"),
            ('"Gallery matched tonight’s shift."', "— OMR"),
            ('"24/7 number still active."', "— Repeat client"),
        ],
        "steps_intro": "Four facts, four steps — browse, message, meet, pay.",
        "faq": [
            ("Advance payment?", '<p>No — pay after meet per <a href="https://lillybabe.com">LillyBabe</a>.</p>'),
            ("Official gallery URL?", '<p><a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a></p>'),
            ("Areas covered?", '<p>Citywide; see <a href="https://lillybabe.com/locations">locations</a> and neighbourhood pages.</p>'),
            ("Since when?", '<p>Operating since 2010 — <a href="https://lillybabe.com/about">about</a>.</p>'),
            ("What is this page?", '<p>Quick-reference partner sheet for <a href="https://lillybabe.com">LillyBabe</a>.</p>'),
        ],
        "explore_intro": "Direct links — copy into bookmarks or WhatsApp.",
        "images_explore": ["4.avif", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "look.jpg", "vip-girl1.png"],
        "seo_split_img": "banners/1.avif",
        "seo_types_img": "banners/10.png",
    },
    "neocities": {
        "hero_lead": 'Straight talk: <a href="https://lillybabe.com">LillyBabe</a> does <strong class="kw">Chennai escorts</strong> with real photos and pay-after-meet. No advance. Message WhatsApp when you are ready.',
        "why_title": 'Why people still use <span>LillyBabe</span>',
        "why_intro": "Short version — no fluff.",
        "why_paras": [
            '<p>Random ads lie. <a href="https://lillybabe.com">LillyBabe</a> does not — photos are theirs, girls are met in person, listings come down when someone is off.</p>',
            '<p>You pay cash after you meet her. Not before. Not by UPI “confirmation.”</p>',
            '<p>See who is working tonight: <a href="https://lillybabe.com/escorts">escorts</a>. North, central, OMR, ECR — they cover it. Tell them where you are.</p>',
            '<p>More words on <a href="https://lillybabe.com/about">about</a>. Talk to humans: <a href="https://lillybabe.com/contact-us">contact</a> or WhatsApp below.</p>',
        ],
        "seo_verified_title": 'Verified = <span>actually met</span>',
        "seo_verified_intro": "Plain English.",
        "seo_verified_p1": '<strong class="kw">Chennai escorts</strong> on LillyBabe are face-checked. Photos are not random downloads.',
        "seo_verified_p2": 'List: <a href="https://lillybabe.com/escorts"><strong class="kw">lillybabe.com/escorts</strong></a>.',
        "seo_areas_intro": "Pick your part of town.",
        "seo_whatsapp_intro": "WhatsApp them area + time. That is most of it.",
        "reviews_intro": "What people actually say.",
        "testimonials": [
            ('"Looked like the pic. Good enough for me."', "— Anna Nagar"),
            ('"No UPI scam. Cash later."', "— OMR"),
            ('"Answered at 1am."', "— T. Nagar"),
        ],
        "steps_intro": "Four steps. Done.",
        "faq": [
            ("Advance?", '<p>Nope. After meet on <a href="https://lillybabe.com">lillybabe.com</a>.</p>'),
            ("Real photos?", '<p>Their own shoots — <a href="https://lillybabe.com/escorts">gallery</a>.</p>'),
            ("Areas?", '<p>Most of Chennai — <a href="https://lillybabe.com/locations">locations</a>.</p>'),
            ("Private?", '<p>WhatsApp, not public posts — <a href="https://lillybabe.com/contact-us">contact</a>.</p>'),
            ("This page?", '<p>Partner link page to <a href="https://lillybabe.com">LillyBabe</a>.</p>'),
        ],
        "explore_intro": "Links to the real site.",
        "images_explore": ["3.avif", "6.jpg", "7.jpg", "10.png", "5.jpg", "8.jpg", "escort-bg.webp", "locations.avif"],
        "seo_split_img": "kiss.png",
        "seo_types_img": "assets/look.jpg",
    },
    "tiiny": {
        "hero_lead": '<a href="https://lillybabe.com">LillyBabe</a> — verified <strong class="kw">Chennai escorts</strong>. Pay after meet. <a href="https://lillybabe.com/escorts">Gallery</a> · WhatsApp below.',
        "why_title": 'Essentials <span>only</span>',
        "why_intro": "Minimum you need before you book.",
        "why_paras": [
            '<p><a href="https://lillybabe.com">LillyBabe</a>: verified photos, no advance, cash after meet. Since 2010.</p>',
            '<p>Browse <a href="https://lillybabe.com/escorts">escorts</a> → WhatsApp area + time → meet → pay.</p>',
            '<p>Areas: Anna Nagar, T. Nagar, OMR, ECR. <a href="https://lillybabe.com/locations">Locations</a> · <a href="https://lillybabe.com/about">About</a> · <a href="https://lillybabe.com/contact-us">Contact</a>.</p>',
        ],
        "seo_verified_title": 'Verified <span>escorts</span>',
        "seo_verified_intro": "Active listings, matched photos.",
        "seo_verified_p1": '<strong class="kw">Chennai escorts</strong> — <strong class="kw">pay after meet</strong>, no advance.',
        "seo_verified_p2": '<a href="https://lillybabe.com/escorts"><strong class="kw">lillybabe.com/escorts</strong></a>',
        "seo_areas_intro": "Main zones.",
        "seo_whatsapp_intro": "Message: area, time, hotel/home.",
        "reviews_intro": "Brief notes.",
        "testimonials": [
            ('"Matched photo."', "— Chennai"),
            ('"No advance."', "— OMR"),
            ('"Fast reply."', "— T. Nagar"),
        ],
        "steps_intro": "Browse · Message · Meet · Pay.",
        "faq": [
            ("Advance?", '<p>No — <a href="https://lillybabe.com">LillyBabe</a>.</p>'),
            ("Gallery?", '<p><a href="https://lillybabe.com/escorts">/escorts</a></p>'),
            ("Areas?", '<p><a href="https://lillybabe.com/locations">Locations</a></p>'),
            ("Contact?", '<p><a href="https://lillybabe.com/contact-us">Contact</a> / WhatsApp</p>'),
            ("This page?", '<p>Partner link to <a href="https://lillybabe.com">lillybabe.com</a>.</p>'),
        ],
        "explore_intro": "Official links.",
        "images_explore": ["2.avif", "7.jpg", "8.jpg", "9.jpg", "1.avif", "6.jpg", "background.jpg", "header.jpg"],
        "seo_split_img": "banners/4.avif",
        "seo_types_img": "banners/3.avif",
    },
}

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


def img_url(path: str) -> str:
    base = "https://lillybabe.com/images"
    if path.startswith("http"):
        return path
    if path.startswith(("assets/", "banners/")):
        return f"{base}/{path}"
    flat = {
        "header.jpg", "background.jpg", "locations.avif", "escort-bg.webp",
        "hero-bg.webp", "kiss.png", "vip-girl1.png", "look.jpg",
    }
    if path in flat:
        if path == "look.jpg":
            return f"{base}/assets/look.jpg"
        return f"{base}/{path}"
    if path.endswith(".avif"):
        return f"{base}/banners/{path}"
    return f"{base}/banners/{path}"


def replace_between(text: str, start: str, end: str, new: str) -> str:
    i = text.find(start)
    j = text.find(end, i)
    if i == -1 or j == -1:
        raise ValueError(f"Markers not found: {start!r} .. {end!r}")
    return text[:i] + new + text[j:]


def patch_file(folder: str, data: dict) -> None:
    path = ROOT / folder / "index.html"
    html = path.read_text(encoding="utf-8")

    # Hero lead
    import re
    html = re.sub(
        r'(<p class="hero-lead">).*?(</p>)',
        rf"\1\n          {data['hero_lead']}\n        \2",
        html,
        count=1,
        flags=re.DOTALL,
    )

    # Editorial block
    paras = "\n\n        ".join(data["why_paras"])
    editorial = f"""    <section class="section reveal" aria-labelledby="why-heading">
      <div class="container editorial">
        <h2 id="why-heading" class="section-title">{data['why_title']}</h2>
        <p class="section-intro">{data['why_intro']}</p>

        {paras}
      </div>
    </section>

"""
    html = replace_between(html, EDITORIAL_START, EDITORIAL_END, editorial)

    # SEO verified section intros
    html = re.sub(
        r'(<h2 id="seo-verified-heading" class="section-title">).*?(</h2>)',
        rf"\1{data['seo_verified_title']}\2",
        html,
        count=1,
    )
    html = re.sub(
        r'(<p class="section-intro">)This page is designed to help you understand how LillyBabe works.*?(</p>)',
        rf"\1{data['seo_verified_intro']}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # First seo-split paragraph block
    html = re.sub(
        r'(<div class="seo-split-copy">.*?<p class="section-intro">.*?</p>\s*<p>\s*).*?(</p>\s*<p>\s*For live availability)',
        rf"\1\n            {data['seo_verified_p1']}\n          \2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(For live availability and the full roster, use the official gallery at\s*).*?(\s*</p>)',
        rf"\1\n            {data['seo_verified_p2']}\n          \2",
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = re.sub(
        r'(<h2 id="seo-areas-heading" class="section-title">Areas covered across <span>Chennai</span></h2>\s*<p class="section-intro">).*?(</p>)',
        rf"\1{data['seo_areas_intro']}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<p class="section-intro">)A short message gets a faster yes-or-no.*?(</p>\s*</div>\s*<div class="seo-checklist-grid">)',
        rf"\1{data['seo_whatsapp_intro']}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )

    # SEO split image
    html = re.sub(
        r'(<figure class="seo-split-media">\s*<img src=")[^"]+(")',
        rf"\1{img_url(data['seo_split_img'])}\2",
        html,
        count=1,
    )
    html = re.sub(
        r'(<aside class="seo-two-col-media glass-panel">\s*<img src=")[^"]+(")',
        rf"\1{img_url(data['seo_types_img'])}\2",
        html,
        count=1,
    )

    # Reviews
    html = re.sub(
        r'(<p class="section-intro">)Themes we hear again and again.*?(</p>\s*<ul class="testimonial-grid">)',
        rf"\1{data['reviews_intro']}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    for i, (quote, cite) in enumerate(data["testimonials"]):
        html = re.sub(
            r'(<blockquote>\s*<p>)"[^"]*"(</p>\s*</blockquote>\s*<cite>)— [^<]*(</cite>)',
            rf'\1"{quote}"\2{cite}\3',
            html,
            count=1,
        )

    # Steps intro
    html = re.sub(
        r'(<p class="section-intro">)Four steps — most clients get a yes or no within fifteen minutes\.(</p>)',
        rf"\1{data['steps_intro']}\2",
        html,
        count=1,
    )

    # Explore intro + images
    html = re.sub(
        r'(<p class="section-intro">)Tap through to the pages most clients use.*?(</p>)',
        rf"\1{data['explore_intro']}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )
    for href, img_name in zip(EXPLORE_HREFS, data["images_explore"]):
        url = img_url(img_name)
        html = re.sub(
            rf'(<a href="{re.escape(href)}"[^>]*>.*?<img src=")[^"]+(")',
            rf"\1{url}\2",
            html,
            count=1,
            flags=re.DOTALL,
        )

    # FAQ
    html = re.sub(
        r'(<div class="faq-list">).*?(</div>\s*</div>\s*</section>\s*</main>)',
        lambda m: build_faq(m.group(1), data["faq"]) + m.group(2),
        html,
        count=1,
        flags=re.DOTALL,
    )

    path.write_text(html, encoding="utf-8")
    print(f"Patched {folder}")


def build_faq(prefix: str, items: list) -> str:
    parts = [prefix]
    for q, a in items:
        parts.append(f"""
          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-answer">
              {a}
            </div>
          </details>""")
    return "".join(parts)


def main():
    for folder, data in VARIANTS.items():
        patch_file(folder, data)


if __name__ == "__main__":
    main()
