# LillyBabe partner promo pages

Multiple **unique** static variants for external hosting. Each folder is deployed to its own domain root.

| Folder | Design | Content focus |
|--------|--------|----------------|
| [github-pages/](github-pages/) | Dark glass promo (amber/pink baseline) | Full agency overview + SEO sections |
| [vercel/](vercel/) | Same full layout, **cyan** slate theme | WhatsApp booking guide meta |
| [netlify/](netlify/) | Same full layout, **mint** + wide bento cards | Chennai areas / neighborhoods |
| [surge/](surge/) | Same full layout, **rose** editorial typography | Trust & verification story |
| [gitlab/](gitlab/) | Same full layout, **orange** timeline steps | Step-by-step booking |
| [render/](render/) | Same full layout, **blue** panel theme | Quick facts + links |
| [neocities/](neocities/) | **Modern editorial** — coral/violet dark, Sora + DM Sans, bento cards | Straight-talk content |
| [tiiny/](tiiny/) | **Mobile command center** — cyan/gold, full-width, list-style explore links | Essentials-only copy |

Each variant includes: hero, trust strip, **unique editorial copy**, extra SEO sections (who this page is for, privacy, variant-specific topics), SEO blocks, testimonials, explore cards (rotated images), booking steps, **10 FAQ items** with matching **FAQPage** JSON-LD, footer, and mobile CTA — with its own `assets/styles.css` + `assets/main.js`.

Each folder also ships:

- `robots.txt` — allows crawlers and points to your sitemap
- `sitemap.xml` — single URL for the partner homepage

**Before go-live:** in both files, replace the placeholder domain (e.g. `YOUR-VERCEL-DOMAIN.com`) with your real partner URL. Also set `og:url` in `index.html` to that same URL.

## Deploy

Upload **only the contents** of one folder (e.g. `vercel/index.html`, `vercel/assets/`, `vercel/robots.txt`, `vercel/sitemap.xml`) to the partner host root.

- Do not set `canonical` to lillybabe.com on partner URLs.
- Set `og:url` to the live partner URL when deployed.
- Submit each domain in Google Search Console (sitemap: `https://your-domain/sitemap.xml`).

## Shared constants

See [shared/links.json](shared/links.json) for phone, WhatsApp, and official URLs.

## Local preview

Open `index.html` at repo root for a variant picker, or open any `*/index.html` directly.

## Regenerate SEO sections / FAQ

```bash
py scripts/add_seo_content.py
```

Inserts variant-specific sections before the main SEO blocks and replaces FAQ + `FAQPage` schema. Safe to re-run only if `page-for-heading` is absent (already applied in current tree).

Other content scripts: `patch_variant_content.py`, `patch_meta_and_alts.py`, `fix_cards_and_compare.py`, `fix_encoding.py`.
