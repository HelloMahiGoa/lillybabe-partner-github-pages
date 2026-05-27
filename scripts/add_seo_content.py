#!/usr/bin/env python3
"""Insert unique SEO sections and expanded FAQ + FAQPage schema per variant."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "    <!-- SEO content sections (unique layouts) -->"
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

# (summary, answer_html) — answer may contain HTML
FAQ = {
    "github-pages": [
        ("Do I need to pay an advance?", "<p>No. LillyBabe states <strong class=\"kw\">no advance</strong> and pay-after-meet on <a href=\"https://lillybabe.com\">lillybabe.com</a>. Avoid anyone asking for UPI or wallet confirmation before arrival.</p>"),
        ("How are Chennai escort profiles verified?", "<p>Listings go live after in-house photos and a face-to-face check. Inactive profiles are removed from <a href=\"https://lillybabe.com/escorts\">the gallery</a> rather than left online for show.</p>"),
        ("Which parts of Chennai are covered?", "<p>Outcall to hotels and residences across central Chennai, OMR, ECR, Anna Nagar, Adyar, Guindy, Kilpauk, and more. Use area pages such as <a href=\"https://lillybabe.com/omr-escorts\">OMR</a> and <a href=\"https://lillybabe.com/ecr-escorts\">ECR</a> for realistic travel notes.</p>"),
        ("Is my booking kept private?", "<p>WhatsApp is the usual channel. LillyBabe does not publish client details. For formal contact, use the <a href=\"https://lillybabe.com/contact-us\">contact page</a>.</p>"),
        ("Are photos on the site reliable?", "<p>LillyBabe uses in-house photography for listings. If the person who arrives does not match the gallery, stop the booking and use official <a href=\"https://lillybabe.com/contact-us\">contact</a>.</p>"),
        ("Can I book for a hotel on OMR or ECR?", "<p>Yes — hotel outcall is common. Share hotel name, tower, and time window on WhatsApp. Weekend traffic on ECR can affect ETA; the team usually states that honestly.</p>"),
        ("What is the difference between incall and outcall?", "<p><strong class=\"kw\">Outcall</strong> means someone travels to your hotel or home. <strong class=\"kw\">Incall</strong> means you go to a location they provide. Tell them which applies when you message.</p>"),
        ("How fast does LillyBabe reply on WhatsApp?", "<p>Many chats get a reply within minutes at night and on weekends. If every profile is booked, they typically say so instead of delaying.</p>"),
        ("Where do I see rates?", "<p>Rates and availability are confirmed on <a href=\"https://lillybabe.com\">lillybabe.com</a> or WhatsApp — not on this partner information page.</p>"),
        ("What is this partner page?", "<p>An independent information page about <a href=\"https://lillybabe.com\">LillyBabe</a>. Bookings, payments, and confirmations happen only on the official site or WhatsApp.</p>"),
    ],
    "vercel": [
        ("Do I need to pay before someone arrives?", "<p>No. LillyBabe’s stated policy is cash <strong class=\"kw\">after you meet</strong>, not UPI or wallet transfers in advance.</p>"),
        ("What should my first WhatsApp message include?", "<p>Area (OMR, T. Nagar, etc.), time window, hotel or home, and optional category. Browse <a href=\"https://lillybabe.com/escorts\">escorts</a> first if you want to name a profile.</p>"),
        ("How are profiles verified?", "<p>Face-checked before listing, with photos taken by the agency. See who is on shift at <a href=\"https://lillybabe.com/escorts\">lillybabe.com/escorts</a>.</p>"),
        ("Which Chennai areas work best for late bookings?", "<p>Central zones and OMR often get faster replies than cross-city ECR runs late at night — still message honestly; they will say if timing works.</p>"),
        ("Is booking discreet?", "<p>Yes — WhatsApp is private. Use <a href=\"https://lillybabe.com/contact-us\">contact</a> if you prefer not to use chat.</p>"),
        ("Can I book without opening the website?", "<p>Yes, but checking <a href=\"https://lillybabe.com/escorts\">the gallery</a> first helps you reference a photo when you message.</p>"),
        ("What if the photo does not match?", "<p>Do not pay. LillyBabe’s model is verification before listing; report issues through official channels.</p>"),
        ("Are Russian and Tamil categories verified the same way?", "<p>Same screening for all categories on <a href=\"https://lillybabe.com\">lillybabe.com</a> — category is preference, not a separate quality tier.</p>"),
        ("Do they answer on weekends?", "<p>Yes — nights and weekends are normal. Peak times may mean fully booked shifts; they usually reply with yes, no, or later.</p>"),
        ("What is this page?", "<p>A booking-guide partner page pointing to official <a href=\"https://lillybabe.com\">LillyBabe</a>.</p>"),
    ],
    "netlify": [
        ("Do I need to pay an advance?", "<p>No advance on <a href=\"https://lillybabe.com\">LillyBabe</a>. Pay after meet, in cash, once you are satisfied.</p>"),
        ("Which LillyBabe page should I use for OMR hotels?", "<p><a href=\"https://lillybabe.com/omr-escorts\">OMR escorts</a> plus the main <a href=\"https://lillybabe.com/escorts\">gallery</a>. Message with your hotel or service apartment name.</p>"),
        ("How does ECR differ from central Chennai for outcall?", "<p>ECR resort and beach-road bookings often need longer travel windows, especially on weekends. See <a href=\"https://lillybabe.com/ecr-escorts\">ECR escorts</a> and allow extra time in your message.</p>"),
        ("Is T. Nagar covered for hotel guests?", "<p>Yes — central pins and T. Nagar hotels are common. Use <a href=\"https://lillybabe.com/t-nagar-escorts\">T. Nagar escorts</a> when that is your zone.</p>"),
        ("How are listings verified?", "<p>In-person checks and matched photos before profiles go live on <a href=\"https://lillybabe.com/escorts\">escorts</a>.</p>"),
        ("Should I name my pin or only the area?", "<p>Hotel name, tower, or pin helps OMR and ECR timing. Area alone is enough to start; details reduce waiting.</p>"),
        ("Is booking private?", "<p>WhatsApp-based; no public client list. <a href=\"https://lillybabe.com/contact-us\">Contact</a> for other enquiries.</p>"),
        ("What if traffic makes someone late?", "<p>Honest ETA updates are part of why zone-based pages exist on <a href=\"https://lillybabe.com/locations\">locations</a>.</p>"),
        ("Where are rates listed?", "<p>Confirmed on the official site or WhatsApp — not on this partner page.</p>"),
        ("What is this page?", "<p>A location-focused partner guide for <a href=\"https://lillybabe.com\">LillyBabe</a> Chennai coverage.</p>"),
    ],
    "surge": [
        ("Why do people worry about fake photos?", "<p>Random ads often reuse stock images. LillyBabe states in-house photos and face checks before <a href=\"https://lillybabe.com/escorts\">listings</a> go live.</p>"),
        ("Do I pay before meeting?", "<p>No — <strong class=\"kw\">pay after meet</strong> is the stated policy. Be cautious if another number asks for UPI first.</p>"),
        ("How does LillyBabe verify someone?", "<p>Meet in person before listing, match gallery to face, remove ads when off rotation. Read <a href=\"https://lillybabe.com/about\">about</a> for their own wording.</p>"),
        ("What are red flags on random listings?", "<p>Advance payment demands, changing WhatsApp numbers, photos that look like glamour shoots, and vague “on the way” messages with no ETA.</p>"),
        ("Are all categories held to the same standard?", "<p>Yes — Russian, Tamil, and independent profiles on <a href=\"https://lillybabe.com\">lillybabe.com</a> use the same verification funnel.</p>"),
        ("Is discretion possible?", "<p>WhatsApp booking is standard; client names are not published on a public board.</p>"),
        ("What if the person does not match the gallery?", "<p>Stop the booking. Use official <a href=\"https://lillybabe.com/contact-us\">contact</a> if you need to report a mismatch.</p>"),
        ("Why trust an agency over Telegram forwards?", "<p>Accountability, a stable number, active roster maintenance, and a clear no-advance policy on the official site.</p>"),
        ("Which areas are covered?", "<p>Citywide outcall with zone pages — <a href=\"https://lillybabe.com/locations\">locations</a>, Anna Nagar, OMR, ECR, T. Nagar.</p>"),
        ("What is this page?", "<p>A trust-focused partner editorial linking to <a href=\"https://lillybabe.com\">LillyBabe</a>.</p>"),
    ],
    "gitlab": [
        ("What is step one before WhatsApp?", "<p>Browse <a href=\"https://lillybabe.com/escorts\">who is on shift</a> and note a face or name to reference.</p>"),
        ("Do I pay at step four only?", "<p>Yes — cash after meet, once satisfied. No wallet step in the middle on <a href=\"https://lillybabe.com\">LillyBabe</a>.</p>"),
        ("What causes delays in the timeline?", "<p>Missing area or time in step one, peak-hour OMR/ECR traffic, or a fully booked shift.</p>"),
        ("How are profiles verified before step zero?", "<p>Face-to-face screening and in-house photos before any listing appears online.</p>"),
        ("Hotel or home — when should I say?", "<p>At step one on WhatsApp — it affects travel and availability.</p>"),
        ("Is the same policy true for all areas?", "<p>Yes — pay-after-meet and verification apply across <a href=\"https://lillybabe.com/locations\">locations</a>.</p>"),
        ("Can I skip browsing and message cold?", "<p>Yes, but naming a profile speeds the timeline.</p>"),
        ("Is booking private?", "<p>WhatsApp is the main channel; use <a href=\"https://lillybabe.com/contact-us\">contact</a> if needed.</p>"),
        ("Where do rates get confirmed?", "<p>Official site or WhatsApp during the flow — not on this partner page.</p>"),
        ("What is this page?", "<p>A timeline-style partner page for <a href=\"https://lillybabe.com\">LillyBabe</a> bookings.</p>"),
    ],
    "render": [
        ("Advance payment?", "<p>No — pay after meet per <a href=\"https://lillybabe.com\">LillyBabe</a>.</p>"),
        ("Official gallery URL?", "<p><a href=\"https://lillybabe.com/escorts\">lillybabe.com/escorts</a></p>"),
        ("Verified meaning?", "<p>Face check + matched photos + removed when off shift.</p>"),
        ("Areas covered?", "<p>Anna Nagar · T. Nagar · OMR · ECR · <a href=\"https://lillybabe.com/locations\">full list</a></p>"),
        ("Incall vs outcall?", "<p>Outcall = to your hotel/home. Incall = their location. State which in your message.</p>"),
        ("Privacy?", "<p>WhatsApp booking; no public client posts.</p>"),
        ("Photo mismatch?", "<p>Stop booking; use <a href=\"https://lillybabe.com/contact-us\">contact</a>.</p>"),
        ("Since when operating?", "<p>Since 2010 — <a href=\"https://lillybabe.com/about\">about</a>.</p>"),
        ("Rates on this page?", "<p>No — rates only on official site or WhatsApp.</p>"),
        ("What is this page?", "<p>Quick-reference partner sheet for <a href=\"https://lillybabe.com\">LillyBabe</a>.</p>"),
    ],
    "neocities": [
        ("Do I pay upfront?", "<p>No. Cash after meet on <a href=\"https://lillybabe.com\">lillybabe.com</a> — not before.</p>"),
        ("Are the photos real?", "<p>LillyBabe says they shoot their own and meet people before listing. See <a href=\"https://lillybabe.com/escorts\">gallery</a>.</p>"),
        ("What should I watch out for?", "<p>Advance fees, wrong person at the door, numbers that change after you pay, photos that look too perfect to be recent.</p>"),
        ("Which areas?", "<p>Most of Chennai — <a href=\"https://lillybabe.com/locations\">locations</a>.</p>"),
        ("Private booking?", "<p>WhatsApp — not a public forum. <a href=\"https://lillybabe.com/contact-us\">Contact</a> too.</p>"),
        ("Russian vs Tamil listings?", "<p>Preference categories — same verification either way.</p>"),
        ("Hotel outcall OK?", "<p>Yes — say hotel and area clearly on WhatsApp.</p>"),
        ("How fast do they reply?", "<p>Often minutes; busy nights may mean “fully booked.”</p>"),
        ("Rates here?", "<p>No — check official site or WhatsApp.</p>"),
        ("This page?", "<p>Partner info linking to <a href=\"https://lillybabe.com\">LillyBabe</a>.</p>"),
    ],
    "tiiny": [
        ("Advance?", "<p>No — <a href=\"https://lillybabe.com\">LillyBabe</a> states pay after meet only.</p>"),
        ("First WhatsApp line?", "<p>Area, time, hotel/home, optional category. Example: “T. Nagar, 10pm, hotel, Tamil or independent.”</p>"),
        ("Gallery?", "<p><a href=\"https://lillybabe.com/escorts\">lillybabe.com/escorts</a></p>"),
        ("Verified?", "<p>Face-checked listings; in-house photos.</p>"),
        ("Areas?", "<p>Anna Nagar, T. Nagar, OMR, ECR — <a href=\"https://lillybabe.com/locations\">locations</a></p>"),
        ("Privacy?", "<p>WhatsApp; no public client list.</p>"),
        ("Photo match?", "<p>If wrong person, stop — use <a href=\"https://lillybabe.com/contact-us\">contact</a>.</p>"),
        ("Weekend bookings?", "<p>Common; reply may be slower if fully booked.</p>"),
        ("Rates?", "<p>Official site or WhatsApp only.</p>"),
        ("This page?", "<p>Partner link to <a href=\"https://lillybabe.com\">lillybabe.com</a>.</p>"),
    ],
}

EXTRA = {
    "github-pages": """
    <div class="section-divider" aria-hidden="true"></div>

    <section class="section section-alt reveal" aria-labelledby="page-for-heading">
      <div class="container editorial">
        <h2 id="page-for-heading" class="section-title">Who this <span>page</span> is for</h2>
        <p class="section-intro">A quick note on purpose — so you know what you are reading and where to book.</p>
        <p>This page is for adults in Chennai who want plain information about <strong class="kw">Chennai escorts</strong> and <a href="https://lillybabe.com">LillyBabe</a> before opening the official site. It is not a booking form, not a payment page, and not a place to send money.</p>
        <p>If you only need tonight’s roster, go straight to <a href="https://lillybabe.com/escorts">verified profiles</a>. If you want context on verification, areas, and policy first, the sections below walk through that in neutral language.</p>
      </div>
    </section>

    <section class="section reveal" aria-labelledby="privacy-heading">
      <div class="container editorial">
        <h2 id="privacy-heading" class="section-title">Privacy and <span>discretion</span></h2>
        <p class="section-intro">How booking usually works without public posts or forums.</p>
        <p>Most clients use WhatsApp with the number listed on <a href="https://lillybabe.com">lillybabe.com</a>. That keeps the conversation off open classified boards. LillyBabe states that client details are not published as reviews or public comments on their site.</p>
        <p>For a formal channel, the <a href="https://lillybabe.com/contact-us">contact page</a> exists alongside WhatsApp. Use whichever you are comfortable with — the same no-advance policy applies once you book through official channels.</p>
      </div>
    </section>

    <section class="section section-alt reveal" aria-labelledby="glossary-heading">
      <div class="container">
        <h2 id="glossary-heading" class="section-title">Short <span>glossary</span></h2>
        <p class="section-intro">Terms you may see on listings and in chat — in plain English.</p>
        <div class="seo-type-list">
          <div class="seo-type-item glass-panel">
            <h3><strong class="kw">Verified profile</strong></h3>
            <p>Someone met in person by the agency, with photos taken for that listing — not a recycled ad from elsewhere.</p>
          </div>
          <div class="seo-type-item glass-panel">
            <h3><strong class="kw">Outcall</strong></h3>
            <p>The companion travels to your hotel or home. Area and hotel name help set realistic arrival time.</p>
          </div>
          <div class="seo-type-item glass-panel">
            <h3><strong class="kw">Incall</strong></h3>
            <p>You visit a location the agency provides. Confirm address and timing on WhatsApp before you travel.</p>
          </div>
          <div class="seo-type-item glass-panel">
            <h3><strong class="kw">Pay after meet</strong></h3>
            <p>Cash payment after you meet and are satisfied — not UPI or wallet transfers before arrival.</p>
          </div>
        </div>
      </div>
    </section>
""",
    "vercel": """
    <div class="section-divider" aria-hidden="true"></div>

    <section class="section section-alt reveal" aria-labelledby="page-for-heading">
      <div class="container editorial">
        <h2 id="page-for-heading" class="section-title">Who should read this <span>guide</span></h2>
        <p class="section-intro">Anyone messaging LillyBabe for the first time — or returning after a long break.</p>
        <p>This guide suits you if you want a faster <strong class="kw">Chennai escort booking</strong> on WhatsApp without ten back-and-forth messages. It does not replace <a href="https://lillybabe.com/escorts">the official gallery</a> — it helps you use it well.</p>
      </div>
    </section>

    <section class="section reveal" aria-labelledby="first-message-heading">
      <div class="container glass-panel" style="padding:1.5rem">
        <h2 id="first-message-heading" class="section-title">A first message <span>template</span></h2>
        <p class="section-intro">Copy the idea, not word for word — adjust to your night.</p>
        <p style="color:#e5e5e5;margin-bottom:1rem">“Hi, I would like to book a verified Chennai escort. My area is <strong class="kw">[OMR / T. Nagar / Anna Nagar / ECR]</strong>, time is <strong class="kw">[time window]</strong>, location is <strong class="kw">[hotel name or home]</strong>. Preference: <strong class="kw">[Tamil / Russian / independent / no preference]</strong>. Please share who is available.”</p>
        <p style="color:#a3a3a3;font-size:0.9rem">Then open <a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a> if you want to name someone from tonight’s shift.</p>
      </div>
    </section>

    <section class="section section-alt reveal" aria-labelledby="timing-heading">
      <div class="container editorial">
        <h2 id="timing-heading" class="section-title">Weeknights, <span>weekends</span>, and reply time</h2>
        <p class="section-intro">What to expect when demand is high.</p>
        <p>Friday and Saturday nights are busy for <a href="https://lillybabe.com">LillyBabe</a>. You may get a fast list of who is free — or a direct “fully booked for this slot.” That is normal for a roster that removes inactive profiles instead of pretending everyone is available.</p>
        <p>Weekday late evenings on OMR and in central hotels are often quicker than cross-city ECR runs at midnight. Mention your real time window; they can say if travel still works.</p>
      </div>
    </section>
""",
    "netlify": """
    <div class="section-divider" aria-hidden="true"></div>

    <section class="section section-alt reveal" aria-labelledby="page-for-heading">
      <div class="container editorial">
        <h2 id="page-for-heading" class="section-title">Why <span>location</span> matters first</h2>
        <p class="section-intro">Chennai is large — your hotel zone drives travel time more than buzzwords on an ad.</p>
        <p>This page is for guests who already know they are staying in a specific corridor — OMR, T. Nagar, Anna Nagar, or ECR — and want <strong class="kw">Chennai escorts</strong> with honest ETA from <a href="https://lillybabe.com">LillyBabe</a>. Start on <a href="https://lillybabe.com/locations">locations</a>, then the gallery.</p>
      </div>
    </section>

    <section class="section reveal" aria-labelledby="area-guide-heading">
      <div class="container">
        <h2 id="area-guide-heading" class="section-title">Three corridors <span>explained</span></h2>
        <p class="section-intro">Neutral notes — not promises about instant arrival everywhere.</p>
        <div class="seo-card-grid">
          <article class="seo-mini-card glass-panel">
            <h3>OMR (IT corridor)</h3>
            <p>Service apartments and business hotels along Old Mahabalipuram Road. Strong for weekday stays; message tower or hotel name. Details: <a href="https://lillybabe.com/omr-escorts">OMR escorts</a>.</p>
          </article>
          <article class="seo-mini-card glass-panel">
            <h3>T. Nagar (central)</h3>
            <p>Dense hotel stock near shopping and central Chennai. Good when your pin is already central — see <a href="https://lillybabe.com/t-nagar-escorts">T. Nagar escorts</a>.</p>
          </article>
          <article class="seo-mini-card glass-panel">
            <h3>ECR (coast)</h3>
            <p>Resorts and weekend drives along the beach road. Allow extra time in your message, especially Saturday night. Page: <a href="https://lillybabe.com/ecr-escorts">ECR escorts</a>.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section-alt reveal" aria-labelledby="privacy-heading">
      <div class="container editorial">
        <h2 id="privacy-heading" class="section-title">Privacy when you share <span>a hotel name</span></h2>
        <p class="section-intro">You need to share location for outcall — here is how that is usually handled.</p>
        <p>WhatsApp with <a href="https://lillybabe.com">LillyBabe</a> is private to your chat. Sharing hotel name or tower is normal for outcall so someone nearby can respond. If you are uncomfortable, ask on <a href="https://lillybabe.com/contact-us">contact</a> what they need at minimum to confirm timing.</p>
      </div>
    </section>
""",
    "surge": """
    <div class="section-divider" aria-hidden="true"></div>

    <section class="section section-alt reveal" aria-labelledby="page-for-heading">
      <div class="container editorial">
        <h2 id="page-for-heading" class="section-title">Why trust is the <span>main topic</span></h2>
        <p class="section-intro">This page focuses on verification and payment policy — not hype.</p>
        <p>If you have been burned by fake photos or advance scams on random ads, you are the audience. We explain how <a href="https://lillybabe.com">LillyBabe</a> describes verification and <strong class="kw">pay after meet</strong> so you can compare that standard before you message.</p>
      </div>
    </section>

    <section class="section reveal" aria-labelledby="red-flags-heading">
      <div class="container">
        <h2 id="red-flags-heading" class="section-title">Red flags on <span>random listings</span></h2>
        <p class="section-intro">Neutral checklist — walk away if several line up.</p>
        <div class="seo-banner-grid">
          <div class="seo-banner-point">
            <h3><strong class="kw">Advance payment</strong></h3>
            <p>UPI or wallet “confirmation” before anyone arrives. LillyBabe states the opposite on the official site.</p>
          </div>
          <div class="seo-banner-point">
            <h3><strong class="kw">Photo mismatch</strong></h3>
            <p>Glamour shots that never look like the person at the door. Prefer in-house gallery photos on <a href="https://lillybabe.com/escorts">escorts</a>.</p>
          </div>
          <div class="seo-banner-point">
            <h3><strong class="kw">Changing numbers</strong></h3>
            <p>New WhatsApp mid-chat, especially after money is mentioned. LillyBabe keeps a long-running line.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt reveal" aria-labelledby="pay-policy-heading">
      <div class="container editorial">
        <h2 id="pay-policy-heading" class="section-title">Pay after meet — <span>what it means</span></h2>
        <p class="section-intro">Policy in practical terms, not marketing language.</p>
        <p>You meet the person first. You pay in cash after you are satisfied with how the booking went. There is no legitimate “holding fee” on <a href="https://lillybabe.com">lillybabe.com</a> before arrival. If a chat pushes payment first, it is not described as LillyBabe policy — stop and use the official <a href="https://lillybabe.com/contact-us">contact</a> number only.</p>
      </div>
    </section>
""",
    "gitlab": """
    <div class="section-divider" aria-hidden="true"></div>

    <section class="section section-alt reveal" aria-labelledby="page-for-heading">
      <div class="container editorial">
        <h2 id="page-for-heading" class="section-title">Read this as a <span>timeline</span></h2>
        <p class="section-intro">Order matters more than speed — each step builds on the last.</p>
        <p>This page is for people who want a clear sequence before booking <strong class="kw">Chennai escorts</strong> with <a href="https://lillybabe.com">LillyBabe</a>: browse, brief, travel, pay last. Skipping steps is why chats drag on.</p>
      </div>
    </section>

    <section class="section reveal" aria-labelledby="etiquette-heading">
      <div class="container editorial">
        <h2 id="etiquette-heading" class="section-title">Etiquette that <span>speeds replies</span></h2>
        <p class="section-intro">Neutral habits — not rules, just what the team can act on.</p>
        <p>Be direct about area and time. Do not ask “who is free?” without context. Do not negotiate advance payment — the policy is fixed. Confirm hotel name or incall preference once. If you change hotels mid-chat, say so early. Browse <a href="https://lillybabe.com/escorts">escorts</a> so you can name a profile instead of forcing the team to guess your taste.</p>
        <p>If you need to cancel, say it clearly. Rosters are live; holding a slot affects someone else on shift.</p>
      </div>
    </section>

    <section class="section section-alt reveal" aria-labelledby="privacy-heading">
      <div class="container editorial">
        <h2 id="privacy-heading" class="section-title">Privacy through the <span>timeline</span></h2>
        <p class="section-intro">One thread on WhatsApp beats scattered public comments.</p>
        <p>Keep booking details in the official WhatsApp chat or <a href="https://lillybabe.com/contact-us">contact</a>. That matches how LillyBabe presents discreet booking — no public review wall for clients.</p>
      </div>
    </section>
""",
    "render": """
    <div class="section-divider" aria-hidden="true"></div>

    <section class="section section-alt reveal" aria-labelledby="page-for-heading">
      <div class="container editorial">
        <h2 id="page-for-heading" class="section-title">How to use this <span>page</span></h2>
        <p class="section-intro">Quick reference — jump to FAQ for detail.</p>
        <p>Facts and links about <a href="https://lillybabe.com">LillyBabe</a> <strong class="kw">Chennai escorts</strong>. Book on the official site or WhatsApp; do not treat this partner URL as checkout.</p>
      </div>
    </section>

    <section class="section reveal" aria-labelledby="glossary-heading">
      <div class="container">
        <h2 id="glossary-heading" class="section-title">Key <span>terms</span></h2>
        <p class="section-intro">One line each — for scan reading.</p>
        <ul class="seo-checklist-list glass-panel">
          <li><strong class="kw">Verified</strong> — met in person; matched photos on <a href="https://lillybabe.com/escorts">/escorts</a></li>
          <li><strong class="kw">Outcall</strong> — to your hotel or home</li>
          <li><strong class="kw">Incall</strong> — you travel to their location</li>
          <li><strong class="kw">No advance</strong> — pay cash after meet</li>
          <li><strong class="kw">OMR / ECR / T. Nagar</strong> — use matching area pages on <a href="https://lillybabe.com/locations">/locations</a></li>
        </ul>
      </div>
    </section>
""",
    "neocities": """
    <div class="section-divider" aria-hidden="true"></div>

    <section class="section section-alt reveal" aria-labelledby="page-for-heading">
      <div class="container editorial">
        <h2 id="page-for-heading" class="section-title">Straight talk — <span>who this is for</span></h2>
        <p class="section-intro">Adults in Chennai comparing agencies. Not a payment page.</p>
        <p>You want real photos, no advance, and a straight answer on WhatsApp. That is what <a href="https://lillybabe.com">LillyBabe</a> says it delivers. This page explains it; <a href="https://lillybabe.com/escorts">the gallery</a> is where you book.</p>
      </div>
    </section>

    <section class="section reveal" aria-labelledby="red-flags-heading">
      <div class="container editorial">
        <h2 id="red-flags-heading" class="section-title">Walk away <span>if…</span></h2>
        <p class="section-intro">Short list. No drama.</p>
        <p>They want UPI before meet. The photo clearly is not the person at the door. The WhatsApp number changes mid-chat. They will not say a real area or time. LillyBabe on <a href="https://lillybabe.com">lillybabe.com</a> is pitched as the opposite on all four points.</p>
      </div>
    </section>

    <section class="section section-alt reveal" aria-labelledby="privacy-heading">
      <div class="container editorial">
        <h2 id="privacy-heading" class="section-title">Privacy</h2>
        <p class="section-intro">Keep it on WhatsApp.</p>
        <p>No need for public posts. Message the official line or use <a href="https://lillybabe.com/contact-us">contact</a>. Same <strong class="kw">no advance</strong> rule.</p>
      </div>
    </section>
""",
    "tiiny": """
    <div class="section-divider" aria-hidden="true"></div>

    <section class="section section-alt reveal" aria-labelledby="page-for-heading">
      <div class="container editorial">
        <h2 id="page-for-heading" class="section-title">Who this <span>page</span> is for</h2>
        <p class="section-intro">Quick read before you tap WhatsApp or the gallery.</p>
        <p>Adults in Chennai who want the essentials on <a href="https://lillybabe.com">LillyBabe</a> — verified <strong class="kw">Chennai escorts</strong>, no advance, pay after meet. Not a checkout page.</p>
      </div>
    </section>

    <section class="section reveal" aria-labelledby="whatsapp-brief-heading">
      <div class="container glass-panel" style="padding:1.25rem">
        <h2 id="whatsapp-brief-heading" class="section-title">Your WhatsApp <span>brief</span></h2>
        <p class="section-intro">Five fields — copy the pattern.</p>
        <p style="color:#cbd5e1">Area · time · hotel or home · optional type (Tamil / Russian / independent) · length of booking. Example: “OMR, 11pm, Marriott, independent, 2 hours.” Then check <a href="https://lillybabe.com/escorts">who is on shift</a>.</p>
      </div>
    </section>

    <section class="section section-alt reveal" aria-labelledby="red-flags-heading">
      <div class="container editorial">
        <h2 id="red-flags-heading" class="section-title">Three red <span>flags</span></h2>
        <p class="section-intro">Stop if you see these.</p>
        <p>Advance payment request. Wrong person vs gallery. New WhatsApp number after you agree. Official policy on <a href="https://lillybabe.com">lillybabe.com</a> is pay after meet with verified listings.</p>
      </div>
    </section>
""",
}

CONTENTS_EXTRA_TIINY = """
          <li><a href="#page-for-heading">Who this page is for</a></li>
          <li><a href="#whatsapp-brief-heading">WhatsApp brief</a></li>
          <li><a href="#red-flags-heading">Red flags</a></li>
"""


def build_faq_html(items: list[tuple[str, str]]) -> str:
    parts = ['        <div class="faq-list">']
    for q, a in items:
        parts.append(f"""
          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-answer">
              {a}
            </div>
          </details>""")
    parts.append("\n        </div>")
    return "".join(parts)


def build_faq_schema(items: list[tuple[str, str]]) -> str:
    entities = []
    for q, a in items:
        text = re.sub(r"<[^>]+>", "", a)
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": text.strip()},
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities,
    }
    return (
        '\n  <script type="application/ld+json">\n  '
        + json.dumps(schema, indent=2).replace("\n", "\n  ")
        + "\n  </script>"
    )


def patch_file(folder: str) -> None:
    path = ROOT / folder / "index.html"
    html = path.read_text(encoding="utf-8")

    if MARKER not in html:
        print(f"  skip {folder}: marker missing")
        return

    if "page-for-heading" not in html:
        html = html.replace(MARKER, EXTRA[folder].strip() + "\n\n" + MARKER, 1)
        print(f"  + extra sections: {folder}")
    else:
        print(f"  = extra sections exist: {folder}")

    faq_items = FAQ[folder]
    faq_html = build_faq_html(faq_items)
    html = re.sub(
        r'<div class="faq-list">.*?</div>\s*</div>\s*</section>\s*</main>',
        faq_html + "\n      </div>\n    </section>\n  </main>",
        html,
        count=1,
        flags=re.DOTALL,
    )

    if '"@type": "FAQPage"' not in html:
        html = html.replace("</head>", build_faq_schema(faq_items) + "\n</head>", 1)
        print(f"  + FAQPage schema: {folder}")

    if folder == "tiiny" and "#whatsapp-brief-heading" not in html:
        html = html.replace(
            '          <li><a href="#why-heading">Essentials before you book</a></li>',
            '          <li><a href="#why-heading">Essentials before you book</a></li>'
            + CONTENTS_EXTRA_TIINY,
            1,
        )

    path.write_text(html, encoding="utf-8")


def main():
    for folder in FOLDERS:
        patch_file(folder)
    print("Done.")


if __name__ == "__main__":
    main()
