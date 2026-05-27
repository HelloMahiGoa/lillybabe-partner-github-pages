import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..");
const templateDir = path.join(root, "vercel");
const templateHtml = fs.readFileSync(path.join(templateDir, "index.html"), "utf8");
const templateCss = fs.readFileSync(path.join(templateDir, "assets", "styles.css"), "utf8");
const templateJs = fs.readFileSync(path.join(templateDir, "assets", "main.js"), "utf8");

const variants = [
  {
    id: "amplify",
    host: "YOUR-PROJECT.amplifyapp.com",
    themeColor: "#1a1208",
    cssComment: "LillyBabe promo — amplify variant (warm amber)",
    css: {
      bg: "#120a04",
      bgElevated: "#1f1408",
      bgCard: "#2a1c0c",
      text: "#faf3e8",
      muted: "#b8a088",
      accent: "#ff9900",
      accentDim: "rgba(255, 153, 0, 0.14)",
      accentBorder: "rgba(255, 153, 0, 0.45)",
      ctaStart: "#ff9900",
      ctaEnd: "#ec7211",
      theme: "#b45309",
      focus: "#ff9900",
      mesh1: "rgba(255, 153, 0, 0.18)",
      mesh2: "rgba(236, 114, 17, 0.12)",
    },
    title: "Chennai Escort Rates — What to Ask on WhatsApp | LillyBabe",
    description:
      "How to ask about rates for verified Chennai escorts without awkward chats. LillyBabe quotes on WhatsApp after you share area, time, and hotel — pay after meet, no advance.",
    ogTitle: "Chennai Escort Rates — LillyBabe WhatsApp Guide",
    ogDescription:
      "Share area and timing first; LillyBabe replies with who is free and confirms pay-after-meet policy on verified Chennai escorts.",
    schemaName: "Chennai Escort Rates Guide — LillyBabe",
    schemaDesc: "How to message LillyBabe about rates and availability for verified Chennai escorts.",
    whyTitle: "Rates and quotes",
    whySpan: "on WhatsApp",
    whyIntro: "How to ask about pricing without ten messages back and forth.",
    whyBody: `<p><a href="https://lillybabe.com">LillyBabe</a> does not publish fixed rate cards on random reference sites. You get a straight answer on WhatsApp after you send <strong class="kw">area</strong>, <strong class="kw">time</strong>, and <strong class="kw">hotel or home</strong> — the variables that actually change tonight’s quote for <strong class="kw">Chennai escorts</strong>.</p>

        <p>Browse <a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a> first if you want to name a profile. The team confirms who is on shift, then discusses session length. Policy stays consistent: <strong class="kw">cash after meet</strong>, no wallet prepay.</p>

        <p>For agency background, see <a href="https://lillybabe.com/about">about</a>. Official contact: <a href="https://lillybabe.com/contact-us">contact</a>.</p>`,
    pageTitle: "Before you",
    pageSpan: "message",
    pageIntro: "Have these three facts ready — it speeds up the rate reply.",
    pageBody: `<p>Area (OMR, T. Nagar, Anna Nagar, ECR), time window, and outcall vs incall. That is enough for <a href="https://lillybabe.com">LillyBabe</a> to quote honestly for <strong class="kw">verified Chennai escorts</strong> without generic copy-paste numbers.</p>`,
    faqPage: "Guide to rates, availability, and official LillyBabe booking links.",
  },
  {
    id: "workers",
    host: "YOUR-PROJECT.workers.dev",
    themeColor: "#1c0a2e",
    cssComment: "LillyBabe promo — workers variant (violet edge)",
    css: {
      bg: "#0f0618",
      bgElevated: "#1a0f28",
      bgCard: "#261538",
      text: "#ede9fe",
      muted: "#a78bfa",
      accent: "#a855f7",
      accentDim: "rgba(168, 85, 247, 0.14)",
      accentBorder: "rgba(168, 85, 247, 0.4)",
      ctaStart: "#c084fc",
      ctaEnd: "#9333ea",
      theme: "#7e22ce",
      focus: "#c084fc",
      mesh1: "rgba(168, 85, 247, 0.2)",
      mesh2: "rgba(147, 51, 234, 0.12)",
    },
    title: "Hotel vs Home — Chennai Escort Outcall Guide | LillyBabe",
    description:
      "Outcall to your hotel or home in Chennai: what to tell LillyBabe on WhatsApp, travel timing for OMR and ECR, and verified escorts with pay after meet.",
    ogTitle: "Chennai Escort Outcall — Hotel vs Home",
    ogDescription:
      "Logistics for hotel and home outcall bookings with verified Chennai escorts through LillyBabe.",
    schemaName: "Chennai Escort Outcall Guide — LillyBabe",
    schemaDesc: "Hotel vs home outcall guidance for booking verified Chennai escorts with LillyBabe.",
    whyTitle: "Hotel vs home",
    whySpan: "outcall",
    whyIntro: "Location type changes travel time — say it in message one.",
    whyBody: `<p>Hotel outcall in Chennai usually means you share the property name, floor if needed, and a realistic check-in time. Home outcall needs a clear area pin and access notes. <a href="https://lillybabe.com">LillyBabe</a> uses that to match <strong class="kw">Chennai escorts</strong> who are actually willing to travel tonight.</p>

        <p>Pick the closest zone page — <a href="https://lillybabe.com/omr-escorts">OMR</a>, <a href="https://lillybabe.com/anna-nagar-escorts">Anna Nagar</a>, <a href="https://lillybabe.com/ecr-escorts">ECR</a> — before you message. Gallery faces live on <a href="https://lillybabe.com/escorts">escorts</a>. Payment: <strong class="kw">cash after meet</strong>, not advance UPI.</p>

        <p>Questions on policy: <a href="https://lillybabe.com/contact-us">contact</a> · <a href="https://lillybabe.com/about">about</a>.</p>`,
    pageTitle: "Incall is the",
    pageSpan: "alternative",
    pageIntro: "When you travel to their location instead of outcall.",
    pageBody: `<p>State “incall” clearly on WhatsApp if you prefer to travel. Same verification standard on <a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a> — matched photos, <strong class="kw">pay after meet</strong>.</p>`,
    faqPage: "Outcall and incall logistics guide for LillyBabe Chennai escorts.",
  },
  {
    id: "heliohost",
    host: "YOUR-SUBDOMAIN.heliohost.org",
    themeColor: "#052e16",
    cssComment: "LillyBabe promo — heliohost variant (green)",
    css: {
      bg: "#041a0c",
      bgElevated: "#0a2e18",
      bgCard: "#0f3d22",
      text: "#ecfdf5",
      muted: "#86efac",
      accent: "#4ade80",
      accentDim: "rgba(74, 222, 128, 0.14)",
      accentBorder: "rgba(74, 222, 128, 0.4)",
      ctaStart: "#22c55e",
      ctaEnd: "#16a34a",
      theme: "#15803d",
      focus: "#4ade80",
      mesh1: "rgba(34, 197, 94, 0.15)",
      mesh2: "rgba(22, 163, 74, 0.1)",
    },
    title: "Weekend Chennai Escorts — Availability Guide | LillyBabe",
    description:
      "Friday and Saturday nights in Chennai: what to expect when messaging LillyBabe for verified escorts, busy shifts, and pay-after-meet booking.",
    ogTitle: "Weekend Chennai Escorts — LillyBabe",
    ogDescription:
      "Weekend demand, reply times, and how to book verified Chennai escorts on WhatsApp with LillyBabe.",
    schemaName: "Weekend Chennai Escorts Guide — LillyBabe",
    schemaDesc: "Weekend availability guide for verified Chennai escorts via LillyBabe.",
    whyTitle: "Weekends and",
    whySpan: "late nights",
    whyIntro: "Peak demand changes reply speed — plan a short, complete WhatsApp brief.",
    whyBody: `<p>Friday and Saturday after 9pm are the busiest windows for <strong class="kw">Chennai escorts</strong>. <a href="https://lillybabe.com">LillyBabe</a> may answer with a short list, a “fully booked” for your slot, or a later time — that honesty beats fake “always available” ads.</p>

        <p>Send area, time, and hotel or home in one message. Check <a href="https://lillybabe.com/escorts">tonight’s gallery</a> first. Same rules every night: verified photos, <strong class="kw">no advance</strong>, cash after meet.</p>

        <p>Agency info: <a href="https://lillybabe.com/about">about</a> · <a href="https://lillybabe.com/locations">locations</a>.</p>`,
    pageTitle: "Weekday",
    pageSpan: "bookings",
    pageIntro: "Often faster replies Tuesday–Thursday for central zones.",
    pageBody: `<p>Less congestion on WhatsApp mid-week — still send area and time. Browse <a href="https://lillybabe.com/escorts">verified profiles</a> on the official site before you message.</p>`,
    faqPage: "Weekend and weekday booking guide for LillyBabe Chennai escorts.",
  },
  {
    id: "awardspace",
    host: "YOUR-SUBDOMAIN.awardspace.com",
    themeColor: "#0c1844",
    cssComment: "LillyBabe promo — awardspace variant (royal blue)",
    css: {
      bg: "#080f24",
      bgElevated: "#0f1a3d",
      bgCard: "#152452",
      text: "#e8eeff",
      muted: "#94a3d8",
      accent: "#60a5fa",
      accentDim: "rgba(96, 165, 250, 0.14)",
      accentBorder: "rgba(96, 165, 250, 0.4)",
      ctaStart: "#3b82f6",
      ctaEnd: "#2563eb",
      theme: "#1d4ed8",
      focus: "#60a5fa",
      mesh1: "rgba(59, 130, 246, 0.18)",
      mesh2: "rgba(37, 99, 235, 0.1)",
    },
    title: "Russian, Tamil & Independent Chennai Escorts | LillyBabe",
    description:
      "Category guide for Russian, Tamil, and independent verified Chennai escorts on LillyBabe — same vetting, pay after meet, WhatsApp booking.",
    ogTitle: "Chennai Escort Categories — LillyBabe",
    ogDescription:
      "How Russian, Tamil, and independent listings work on LillyBabe’s verified Chennai escort gallery.",
    schemaName: "Chennai Escort Categories — LillyBabe",
    schemaDesc: "Category guide for Russian, Tamil, and independent Chennai escorts on LillyBabe.",
    whyTitle: "Categories",
    whySpan: "explained",
    whyIntro: "Russian, Tamil, and independent are preferences — not different trust tiers.",
    whyBody: `<p>On <a href="https://lillybabe.com">LillyBabe</a>, <a href="https://lillybabe.com/russian-escorts-in-chennai">Russian escorts</a>, <a href="https://lillybabe.com/tamil-escorts-in-chennai">Tamil escorts</a>, and <a href="https://lillybabe.com/independent-escorts-in-chennai">independents</a> share the same verification: in-person check, in-house photos, removed when off shift.</p>

        <p>Name a category in WhatsApp only if it narrows your shortlist. Otherwise send area and time first. Full roster: <a href="https://lillybabe.com/escorts">escorts</a>. <strong class="kw">Pay after meet</strong> — no UPI before arrival.</p>

        <p>Contact: <a href="https://lillybabe.com/contact-us">contact</a>.</p>`,
    pageTitle: "VIP and",
    pageSpan: "short stays",
    pageIntro: "International visitors often start with the Russian category page.",
    pageBody: `<p>Read the category blurb on the official site, then message with hotel zone and dates. All bookings confirm through <a href="https://lillybabe.com">LillyBabe</a> WhatsApp — not this reference page.</p>`,
    faqPage: "Category guide for verified Chennai escorts on LillyBabe.",
  },
  {
    id: "codeberg",
    host: "YOUR-USER.codeberg.page",
    themeColor: "#0d3d38",
    cssComment: "LillyBabe promo — codeberg variant (teal EU)",
    css: {
      bg: "#051816",
      bgElevated: "#0a2624",
      bgCard: "#0f3532",
      text: "#e6fffa",
      muted: "#5eead4",
      accent: "#2dd4bf",
      accentDim: "rgba(45, 212, 191, 0.14)",
      accentBorder: "rgba(45, 212, 191, 0.4)",
      ctaStart: "#14b8a6",
      ctaEnd: "#0d9488",
      theme: "#0f766e",
      focus: "#2dd4bf",
      mesh1: "rgba(20, 184, 166, 0.16)",
      mesh2: "rgba(13, 148, 136, 0.1)",
    },
    title: "Discreet Chennai Escort Booking — Privacy Guide | LillyBabe",
    description:
      "Private WhatsApp booking for verified Chennai escorts: what LillyBabe does and does not share, gallery use, and pay-after-meet policy since 2010.",
    ogTitle: "Discreet Chennai Escorts — LillyBabe",
    ogDescription:
      "Privacy-focused guide to booking verified Chennai escorts through LillyBabe on WhatsApp.",
    schemaName: "Discreet Chennai Escorts Guide — LillyBabe",
    schemaDesc: "Privacy guide for booking verified Chennai escorts with LillyBabe.",
    whyTitle: "Privacy on",
    whySpan: "WhatsApp",
    whyIntro: "What stays between you and the agency — and what you should still verify.",
    whyBody: `<p><a href="https://lillybabe.com">LillyBabe</a> books through private WhatsApp threads — no public client reviews or social posts. You still verify the face on <a href="https://lillybabe.com/escorts">escorts</a> before travel starts; discretion is not a reason to skip photo match.</p>

        <p>Do not pay strangers who DM you claiming to be LillyBabe. Use the number from <a href="https://lillybabe.com/contact-us">contact</a> only. Policy: <strong class="kw">cash after meet</strong>, no advance wallet transfers.</p>

        <p>Operating since 2010 — background on <a href="https://lillybabe.com/about">about</a>.</p>`,
    pageTitle: "Gallery",
    pageSpan: "first",
    pageIntro: "Browsing profiles on the official site is the discreet way to pick a face.",
    pageBody: `<p>Open <a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a> on your own device, then reference a profile in WhatsApp. Faster than describing someone from memory.</p>`,
    faqPage: "Privacy and booking guide for LillyBabe Chennai escorts.",
  },
  {
    id: "bitbucket",
    host: "YOUR-USER.bitbucket.io",
    themeColor: "#001f3d",
    cssComment: "LillyBabe promo — bitbucket variant (deep blue)",
    css: {
      bg: "#001529",
      bgElevated: "#002140",
      bgCard: "#003060",
      text: "#e6f4ff",
      muted: "#69b1ff",
      accent: "#1677ff",
      accentDim: "rgba(22, 119, 255, 0.14)",
      accentBorder: "rgba(22, 119, 255, 0.4)",
      ctaStart: "#4096ff",
      ctaEnd: "#1677ff",
      theme: "#0958d9",
      focus: "#4096ff",
      mesh1: "rgba(22, 119, 255, 0.2)",
      mesh2: "rgba(9, 88, 217, 0.12)",
    },
    title: "Verified Chennai Escorts vs Random Ads | LillyBabe",
    description:
      "Compare LillyBabe verified Chennai escorts to random listings: photos, pay-after-meet, area pages, and WhatsApp booking since 2010.",
    ogTitle: "Verified vs Random Chennai Escort Ads",
    ogDescription:
      "Side-by-side booking standards: LillyBabe verified Chennai escorts vs typical classified risk.",
    schemaName: "Verified vs Random Ads — Chennai Escorts | LillyBabe",
    schemaDesc: "Comparison guide between LillyBabe verified escorts and random Chennai ads.",
    whyTitle: "Gallery vs",
    whySpan: "random ads",
    whyIntro: "Why an official roster beats scrolling unverified classifieds.",
    whyBody: `<p>Random <strong class="kw">Chennai escort</strong> ads recycle stock photos and push UPI before anyone arrives. <a href="https://lillybabe.com">LillyBabe</a> lists only after an in-person meet, shoots photos in-house, and removes profiles when someone is off shift — see <a href="https://lillybabe.com/escorts">escorts</a>.</p>

        <p>Area pages (<a href="https://lillybabe.com/locations">locations</a>) set honest travel windows for OMR, ECR, and central Chennai. Payment model: <strong class="kw">pay after meet</strong>, cash.</p>

        <p>Report mismatches through official <a href="https://lillybabe.com/contact-us">contact</a> — do not argue with intermediaries on random numbers.</p>`,
    pageTitle: "Quick",
    pageSpan: "rule",
    pageIntro: "Official gallery + clear area + no advance.",
    pageBody: `<p>If a chat cannot point you to <a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a> and insists on wallet prepay, it is not described as LillyBabe policy.</p>`,
    faqPage: "Comparison guide for verified Chennai escorts on LillyBabe.",
  },
  {
    id: "statichost",
    host: "YOUR-SUBDOMAIN.statichost.eu",
    themeColor: "#0a2e1a",
    cssComment: "LillyBabe promo — statichost variant (forest green)",
    css: {
      bg: "#061208",
      bgElevated: "#0c1f10",
      bgCard: "#122a18",
      text: "#f0fdf4",
      muted: "#86efac",
      accent: "#34d399",
      accentDim: "rgba(52, 211, 153, 0.14)",
      accentBorder: "rgba(52, 211, 153, 0.4)",
      ctaStart: "#10b981",
      ctaEnd: "#059669",
      theme: "#047857",
      focus: "#34d399",
      mesh1: "rgba(16, 185, 129, 0.15)",
      mesh2: "rgba(5, 150, 105, 0.1)",
    },
    title: "ECR & Resort Chennai Escorts — Coastal Booking | LillyBabe",
    description:
      "ECR and resort bookings for verified Chennai escorts: travel timing, weekend demand, LillyBabe gallery, and pay-after-meet on WhatsApp.",
    ogTitle: "ECR Chennai Escorts — Resort & Coastal",
    ogDescription:
      "Coastal and ECR booking guide for verified Chennai escorts through LillyBabe.",
    schemaName: "ECR Chennai Escorts Guide — LillyBabe",
    schemaDesc: "ECR and coastal resort booking guide for verified Chennai escorts.",
    whyTitle: "ECR and",
    whySpan: "resort stays",
    whyIntro: "Coastal bookings need longer lead time — plan WhatsApp messages early.",
    whyBody: `<p>East Coast Road resorts and weekend villas add distance. <a href="https://lillybabe.com">LillyBabe</a> sets ETAs from the <a href="https://lillybabe.com/ecr-escorts">ECR escorts</a> page context — not unrealistic “20 minutes from anywhere” claims.</p>

        <p>Share property name, check-in time, and session length on WhatsApp. Match faces on <a href="https://lillybabe.com/escorts">escorts</a> before you commit. <strong class="kw">Cash after meet</strong> — no advance.</p>

        <p>Central fallback zones: <a href="https://lillybabe.com/omr-escorts">OMR</a> · <a href="https://lillybabe.com/t-nagar-escorts">T. Nagar</a>.</p>`,
    pageTitle: "OMR vs",
    pageSpan: "ECR",
    pageIntro: "IT corridor vs coastal — pick the area page that matches your pin.",
    pageBody: `<p>Wrong zone in message one causes delays. Open the matching official location page, then message <a href="https://lillybabe.com">LillyBabe</a> with the same area name.</p>`,
    faqPage: "ECR and coastal booking guide for LillyBabe Chennai escorts.",
  },
  {
    id: "fly",
    host: "YOUR-APP.fly.dev",
    themeColor: "#2e1065",
    cssComment: "LillyBabe promo — fly variant (violet)",
    css: {
      bg: "#0f0720",
      bgElevated: "#1a1035",
      bgCard: "#251448",
      text: "#f5f3ff",
      muted: "#c4b5fd",
      accent: "#8b5cf6",
      accentDim: "rgba(139, 92, 246, 0.14)",
      accentBorder: "rgba(139, 92, 246, 0.4)",
      ctaStart: "#a78bfa",
      ctaEnd: "#7c3aed",
      theme: "#6d28d9",
      focus: "#a78bfa",
      mesh1: "rgba(139, 92, 246, 0.2)",
      mesh2: "rgba(124, 58, 237, 0.12)",
    },
    title: "First-Time Chennai Escort Booking Checklist | LillyBabe",
    description:
      "First booking with verified Chennai escorts: checklist for WhatsApp, gallery, pay-after-meet, and LillyBabe area pages — operating since 2010.",
    ogTitle: "First-Time Chennai Escort Booking — LillyBabe",
    ogDescription:
      "Step-by-step checklist for a first LillyBabe booking with verified Chennai escorts.",
    schemaName: "First-Time Chennai Escort Checklist — LillyBabe",
    schemaDesc: "First-time client checklist for booking verified Chennai escorts with LillyBabe.",
    whyTitle: "First-time",
    whySpan: "checklist",
    whyIntro: "Seven items before you send the first WhatsApp message.",
    whyBody: `<p><strong>1.</strong> Open <a href="https://lillybabe.com/escorts">escorts</a> and pick a face on shift. <strong>2.</strong> Note your area (hotel zone or neighbourhood). <strong>3.</strong> Choose a time window. <strong>4.</strong> Decide outcall or incall. <strong>5.</strong> Message <a href="https://lillybabe.com">LillyBabe</a> with all four — not “who is free?” alone.</p>

        <p><strong>6.</strong> Confirm the same photo on arrival. <strong>7.</strong> Pay cash after meet only — LillyBabe’s stated policy since 2010. Read <a href="https://lillybabe.com/about">about</a> for agency background.</p>`,
    pageTitle: "What not",
    pageSpan: "to do",
    pageIntro: "Common first-timer mistakes that slow everyone down.",
    pageBody: `<p>No wallet prepay to “hold” someone. No booking through random Instagram DMs. Use official <a href="https://lillybabe.com/contact-us">contact</a> if a number looks wrong.</p>`,
    faqPage: "First-time booking checklist for LillyBabe Chennai escorts.",
  },
  {
    id: "zeabur",
    host: "YOUR-APP.zeabur.app",
    themeColor: "#2d1b4e",
    cssComment: "LillyBabe promo — zeabur variant (magenta)",
    css: {
      bg: "#14061f",
      bgElevated: "#1f0a30",
      bgCard: "#2a1040",
      text: "#fdf4ff",
      muted: "#e9d5ff",
      accent: "#e879f9",
      accentDim: "rgba(232, 121, 249, 0.14)",
      accentBorder: "rgba(232, 121, 249, 0.4)",
      ctaStart: "#d946ef",
      ctaEnd: "#c026d3",
      theme: "#a21caf",
      focus: "#e879f9",
      mesh1: "rgba(217, 70, 239, 0.18)",
      mesh2: "rgba(192, 38, 211, 0.12)",
    },
    title: "Incall vs Outcall Chennai Escorts — Choose Right | LillyBabe",
    description:
      "Incall vs outcall for Chennai escorts: what to message LillyBabe, hotel bookings, travel time, verified gallery, and pay after meet.",
    ogTitle: "Incall vs Outcall — Chennai Escorts",
    ogDescription:
      "How to choose incall or outcall when booking verified Chennai escorts with LillyBabe.",
    schemaName: "Incall vs Outcall Guide — LillyBabe Chennai",
    schemaDesc: "Incall vs outcall decision guide for verified Chennai escorts.",
    whyTitle: "Incall vs",
    whySpan: "outcall",
    whyIntro: "Pick the mode that matches your night — then message once.",
    whyBody: `<p><strong>Outcall</strong> — she travels to your hotel or home. You provide area, property name, and access timing. <strong>Incall</strong> — you travel to her location. Both modes use the same verified roster on <a href="https://lillybabe.com/escorts">lillybabe.com/escorts</a>.</p>

        <p><a href="https://lillybabe.com">LillyBabe</a> needs the mode in line one of WhatsApp so they do not quote the wrong travel window for <strong class="kw">Chennai escorts</strong>. Payment stays <strong class="kw">cash after meet</strong>.</p>

        <p>Area help: <a href="https://lillybabe.com/locations">locations</a> · <a href="https://lillybabe.com/contact-us">contact</a>.</p>`,
    pageTitle: "Hotel",
    pageSpan: "outcall",
    pageIntro: "Most business travellers choose outcall with a named hotel.",
    pageBody: `<p>Include check-in status and floor policy if the property requires it. Browse <a href="https://lillybabe.com/escorts">verified profiles</a> before you message.</p>`,
    faqPage: "Incall vs outcall guide for LillyBabe Chennai escorts.",
  },
  {
    id: "oracle",
    host: "YOUR-DOMAIN.example.com",
    themeColor: "#3d1008",
    cssComment: "LillyBabe promo — oracle variant (burnt orange)",
    css: {
      bg: "#1a0a06",
      bgElevated: "#2a120c",
      bgCard: "#3a1810",
      text: "#fff7ed",
      muted: "#fdba74",
      accent: "#f97316",
      accentDim: "rgba(249, 115, 22, 0.14)",
      accentBorder: "rgba(249, 115, 22, 0.4)",
      ctaStart: "#fb923c",
      ctaEnd: "#ea580c",
      theme: "#c2410c",
      focus: "#fb923c",
      mesh1: "rgba(249, 115, 22, 0.18)",
      mesh2: "rgba(234, 88, 12, 0.12)",
    },
    title: "Repeat Chennai Escort Clients — LillyBabe Since 2010",
    description:
      "Returning clients: how LillyBabe handles repeat bookings, same WhatsApp line, verified Chennai escorts, and pay-after-meet policy year after year.",
    ogTitle: "Repeat Clients — LillyBabe Chennai Escorts",
    ogDescription:
      "Guide for repeat bookings with verified Chennai escorts through LillyBabe since 2010.",
    schemaName: "Repeat Client Guide — LillyBabe Chennai Escorts",
    schemaDesc: "Repeat booking guide for verified Chennai escorts with LillyBabe.",
    whyTitle: "Repeat",
    whySpan: "bookings",
    whyIntro: "Why the same agency number and gallery still matter on visit three.",
    whyBody: `<p>Repeat clients still check <a href="https://lillybabe.com/escorts">escorts</a> for tonight’s shift — faces change week to week. <a href="https://lillybabe.com">LillyBabe</a> has used the same core rules since 2010: verify in person, in-house photos, <strong class="kw">no advance</strong>.</p>

        <p>Message area and time even if they remember you; roster availability is night-specific. Cash after meet remains the standard — not “trusted client” wallet prepay exceptions.</p>

        <p>History and policies: <a href="https://lillybabe.com/about">about</a> · <a href="https://lillybabe.com/contact-us">contact</a>.</p>`,
    pageTitle: "Long-stay",
    pageSpan: "visitors",
    pageIntro: "Hotel changes and multiple nights — update area each message.",
    pageBody: `<p>Moving from OMR to central Chennai? Send the new zone before assuming prior ETAs still apply. Official area pages on <a href="https://lillybabe.com/locations">locations</a>.</p>`,
    faqPage: "Repeat client guide for LillyBabe Chennai escorts.",
  },
];

function buildCss(v) {
  const c = v.css;
  let css = templateCss
    .replace(/LillyBabe promo — Vercel variant \(cyan minimal\)/, v.cssComment)
    .replace(/variant-vercel/g, `variant-${v.id}`)
    .replace(
      /--bg: #0f172a;\s*--bg-elevated: #1e293b;\s*--bg-card: #1e293b;\s*--text: #f1f5f9;\s*--text-muted: #94a3b8;\s*--amber: #38bdf8;\s*--amber-dim: rgba\(56, 189, 248, 0\.14\);\s*--amber-border: rgba\(56, 189, 248, 0\.4\);\s*--cta-start: #38bdf8;\s*--cta-end: #818cf8;\s*--whatsapp: #059669;\s*--whatsapp-hover: #047857;\s*--theme: #1e1b4b;\s*--radius: 12px;\s*--radius-pill: 9999px;\s*--container: min\(100% - 2rem, 680px\);\s*--header-h: 4rem;\s*--focus: #38bdf8;/s,
      `--bg: ${c.bg};
  --bg-elevated: ${c.bgElevated};
  --bg-card: ${c.bgCard};
  --text: ${c.text};
  --text-muted: ${c.muted};
  --amber: ${c.accent};
  --amber-dim: ${c.accentDim};
  --amber-border: ${c.accentBorder};
  --cta-start: ${c.ctaStart};
  --cta-end: ${c.ctaEnd};
  --whatsapp: #059669;
  --whatsapp-hover: #047857;
  --theme: ${c.theme};
  --radius: 12px;
  --radius-pill: 9999px;
  --container: min(100% - 2rem, 680px);
  --header-h: 4rem;
  --focus: ${c.focus};`
    )
    .replace(
      /radial-gradient\(ellipse 80% 50% at 20% -10%, rgba\(56, 189, 248, 0\.2\), transparent 50%\),\s*radial-gradient\(ellipse 60% 40% at 90% 20%, rgba\(129, 140, 248, 0\.15\), transparent 45%\),\s*radial-gradient\(ellipse 50% 30% at 10% 80%, rgba\(15, 23, 42, 0\.8\), transparent 40%\),/,
      `radial-gradient(ellipse 80% 50% at 20% -10%, ${c.mesh1}, transparent 50%),
    radial-gradient(ellipse 60% 40% at 90% 20%, ${c.mesh2}, transparent 45%),
    radial-gradient(ellipse 50% 30% at 10% 80%, rgba(0, 0, 0, 0.5), transparent 40%),`
    );
  return css;
}

function buildHtml(v) {
  const whyBlock = `        <h2 id="why-heading" class="section-title">${v.whyTitle} <span>${v.whySpan}</span></h2>
        <p class="section-intro">${v.whyIntro}</p>

        ${v.whyBody}`;

  const pageBlock = `        <h2 id="page-for-heading" class="section-title">${v.pageTitle} <span>${v.pageSpan}</span></h2>
        <p class="section-intro">${v.pageIntro}</p>
        ${v.pageBody}`;

  let html = templateHtml
    .replace(/variant-vercel/g, `variant-${v.id}`)
    .replace(
      /<title>[\s\S]*?<\/title>/,
      `<title>${v.title}</title>`
    )
    .replace(
      /<meta name="description" content="[^"]*">/,
      `<meta name="description" content="${v.description}">`
    )
    .replace(
      /<meta name="theme-color" content="[^"]*">/,
      `<meta name="theme-color" content="${v.themeColor}">`
    )
    .replace(
      /<meta property="og:title" content="[^"]*">/,
      `<meta property="og:title" content="${v.ogTitle}">`
    )
    .replace(
      /<meta property="og:description" content="[^"]*">/,
      `<meta property="og:description" content="${v.ogDescription}">`
    )
    .replace(
      /"name": "WhatsApp Booking Guide — Chennai Escorts \| LillyBabe"/,
      `"name": "${v.schemaName.replace(/"/g, '\\"')}"`
    )
    .replace(
      /"description": "How to message LillyBabe on WhatsApp to book verified Chennai escorts — what to include and what to expect back."/,
      `"description": "${v.schemaDesc.replace(/"/g, '\\"')}"`
    )
    .replace(
      /"text": "A booking-guide partner page pointing to official LillyBabe."/,
      `"text": "${v.faqPage.replace(/"/g, '\\"')}"`
    )
    .replace(
      /<h2 id="why-heading" class="section-title">[\s\S]*?<\/section>\s*\n<div class="section-divider"/,
      `${whyBlock}\n      </div>\n    </section>\n\n<div class="section-divider"`
    )
    .replace(
      /<h2 id="page-for-heading" class="section-title">[\s\S]*?<\/section>\s*\n\s*<section class="section reveal" aria-labelledby="first-message-heading">/,
      `${pageBlock}\n      </div>\n    </section>\n\n    <section class="section reveal" aria-labelledby="first-message-heading">`
    )
    .replace(
      /<p>A booking-guide partner page pointing to official <a href="https:\/\/lillybabe.com">LillyBabe<\/a>\.<\/p>/,
      `<p>${v.faqPage.replace(/LillyBabe/g, '<a href="https://lillybabe.com">LillyBabe</a>')}</p>`
    )
    .replace(
      /18\+ only\. This partner page provides information about LillyBabe/,
      "18+ only. Information about verified Chennai escorts and links to LillyBabe"
    )
    .replace(/partner page provides/g, "page provides")
    .replace(/Information about verified Chennai escorts and links to LillyBabe and links to the official website/, "Information about verified Chennai escorts and links to the official LillyBabe website");

  if (html.includes("partner page")) {
    html = html.replace(/partner page/gi, "guide");
  }

  return html;
}

function writeVariant(v) {
  const dir = path.join(root, v.id);
  fs.mkdirSync(path.join(dir, "assets"), { recursive: true });
  fs.writeFileSync(path.join(dir, "index.html"), buildHtml(v));
  fs.writeFileSync(path.join(dir, "assets", "styles.css"), buildCss(v));
  fs.writeFileSync(path.join(dir, "assets", "main.js"), templateJs);
  fs.writeFileSync(
    path.join(dir, "robots.txt"),
    `User-agent: *\nAllow: /\n\nSitemap: https://${v.host}/sitemap.xml\n`
  );
  fs.writeFileSync(
    path.join(dir, "sitemap.xml"),
    `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://${v.host}/</loc>
    <lastmod>2026-05-27</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
`
  );
  fs.writeFileSync(path.join(dir, ".gitignore"), ".DS_Store\nThumbs.db\n");
  console.log("Created", v.id);
}

for (const v of variants) {
  writeVariant(v);
}

// Optional non-deploy configs
fs.writeFileSync(
  path.join(root, "amplify", "amplify.yml"),
  `version: 1
frontend:
  phases:
    build:
      commands: []
  artifacts:
    baseDirectory: /
    files:
      - '**/*'
  cache:
    paths: []
`
);

fs.writeFileSync(
  path.join(root, "fly", "Dockerfile"),
  `FROM nginx:alpine
COPY . /usr/share/nginx/html
EXPOSE 8080
`
);

fs.writeFileSync(
  path.join(root, "fly", "fly.toml"),
  `# Deploy later: fly launch / fly deploy (not run by this repo CI)
app = "lillybabe-partner-fly"
primary_region = "bom"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = "stop"
  auto_start_machines = true
  min_machines_running = 0
`
);

fs.mkdirSync(path.join(root, "codeberg", ".forgejo", "workflows"), { recursive: true });
fs.writeFileSync(
  path.join(root, "codeberg", "PAGES-SETUP.md"),
  `# Codeberg Pages setup

1. Push this repo to Codeberg.
2. Enable Pages in repository settings.
3. See https://docs.codeberg.org/pages/
`
);

fs.writeFileSync(
  path.join(root, "bitbucket", "bitbucket-pipelines.yml"),
  `# Bitbucket Pages — enable in repository settings (static hosting)
# See https://support.atlassian.com/bitbucket-cloud/docs/publishing-a-website-on-bitbucket-cloud/
image: atlassian/default-image:latest
pipelines:
  branches:
    main:
      - step:
          name: Static site (placeholder)
          script:
            - echo "Upload site contents from repo root to hosting when configured."
`
);

console.log("Done:", variants.length, "variants");
