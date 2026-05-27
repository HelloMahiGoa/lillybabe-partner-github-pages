# Free static hosting for partner pages

Platforms with a **free tier** suitable for deploying a folder of static HTML (`index.html` + `assets/`).
One repo → one host. Do not cross-deploy variants.

**Not included:** Koyeb (no meaningful free static tier), Neocities (removed from this project), Fleek (site suspended — removed May 2026).

---

## In this project (active or configured)

| Platform | Free tier | Default URL pattern | Folder / repo |
|----------|-----------|----------------------|---------------|
| [GitHub Pages](https://pages.github.com/) | Yes | `username.github.io/repo-name` | `github-pages/` |
| [GitLab Pages](https://docs.gitlab.com/user/project/pages/) | Yes | `*.gitlab.io` | `gitlab/` |
| [Vercel](https://vercel.com/) | Hobby free | `*.vercel.app` | `vercel/` |
| [Netlify](https://www.netlify.com/) | Starter free | `*.netlify.app` | `netlify/` |
| [Surge](https://surge.sh/) | Yes | `*.surge.sh` | `surge/` |
| [Firebase Hosting](https://firebase.google.com/docs/hosting) | Spark plan free | `*.web.app`, `*.firebaseapp.com` | `firebase/` |
| [Azure Static Web Apps](https://azure.microsoft.com/products/app-service/static) | Free SKU | `*.azurestaticapps.net` | `azure/` |
| [Render](https://render.com/docs/static-sites) | Free static sites | `*.onrender.com` | `render/` |
| [Tiiny Host](https://tiiny.host/) | 1 free site | `*.tiiny.site` | `tiiny/` |
| [Cloudflare Pages](https://pages.cloudflare.com/) | Yes | `*.pages.dev` + custom domain | `cloudflare/` |
| [Deno Deploy](https://deno.com/deploy) | Free tier | `*.deno.dev`, `*.deno.net` | `deno/` |
| [InfinityFree](https://infinityfree.com/) | Free shared hosting | `*.infinityfreeapp.com`, `*.42web.io`, etc. | `infinityfree/` |

Deploy steps for each: see [DEPLOY.md](DEPLOY.md).

---

## Other free options (not yet in repo)

| Platform | Free tier | URL pattern | Notes |
|----------|-----------|-------------|--------|
| [AWS Amplify Hosting](https://aws.amazon.com/amplify/) | Free tier (12 mo / limits) | `*.amplifyapp.com` | Git connect; good AWS ecosystem fit |
| [Cloudflare Workers Sites](https://developers.cloudflare.com/workers/) | Free allowance | Custom domain | More setup than Pages; edge workers |
| [HelioHost](https://www.heliohost.org/) | Yes | Subdomain | Free shared hosting; FTP like InfinityFree |
| [AwardSpace](https://www.awardspace.com/) | Yes | Subdomain | Free PHP + static; FTP upload |
| [Codeberg Pages](https://docs.codeberg.org/pages/) | Yes | `*.codeberg.page` | Git-native; EU-hosted alternative to GitHub Pages |
| [Bitbucket Pages](https://support.atlassian.com/bitbucket-cloud/docs/publishing-a-website-on-bitbucket-cloud/) | Yes | `*.bitbucket.io` | Static sites from Bitbucket repos |
| [Statichost.eu](https://statichost.eu/) | Yes | Custom subdomain | EU GDPR-friendly static hosting |
| [Fly.io](https://fly.io/docs/about/pricing/) | Free allowance | `*.fly.dev` | Static via minimal Dockerfile or nginx |
| [Zeabur](https://zeabur.com/) | Free tier | `*.zeabur.app` | Git deploy; static + serverless |
| [Oracle Cloud Always Free](https://www.oracle.com/cloud/free/) | Always free VPS | Your domain | Self-host nginx/Caddy on ARM VM (not managed static) |

---

## Live URLs (project)

| Variant | Status | URL |
|---------|--------|-----|
| GitHub Pages | Live | https://hellomahigoa.github.io/lillybabe-partner-github-pages/ |
| Vercel | Live | https://lillybabe-partner.vercel.app/ |
| Netlify | Live | https://lillybabe-partner-netlify.netlify.app/ |
| Surge | Live | https://lillybabe-partner-surge.surge.sh/ |
| GitLab | Live | https://lillybabe-partner-gitlab-58412d.gitlab.io/ |
| Firebase | Live | https://studio-9048837108-f3ed0.web.app/ |
| Render | Live | https://lillybabe-partner-render.onrender.com/ |
| Tiiny | Live | https://lillybabe.tiiny.site/ |
| Azure | Live | https://ambitious-beach-0394c6410.7.azurestaticapps.net/ |
| Cloudflare | Live | https://lillybabe-partner-cloudflare.pages.dev/ |
| Deno Deploy | Live | https://lillybabe-dk7226c4ec8k.lillybabe.deno.net/ |
| InfinityFree | Live | https://lillybabe.xo.je/ |
