# Deploy one repo -> one platform

Each GitHub repo deploys **only** to its matching host.

## Live

| Repo | Platform | URL |
|------|----------|-----|
| [lillybabe-partner-github-pages](https://github.com/HelloMahiGoa/lillybabe-partner-github-pages) | **GitHub Pages** | https://hellomahigoa.github.io/lillybabe-partner-github-pages/ |
| [lillybabe-partner-vercel](https://github.com/HelloMahiGoa/lillybabe-partner-vercel) | **Vercel** | https://lillybabe-partner.vercel.app/ |
| [lillybabe-partner-netlify](https://github.com/HelloMahiGoa/lillybabe-partner-netlify) | **Netlify** | https://lillybabe-partner-netlify.netlify.app/ |
| [lillybabe-partner-surge](https://github.com/HelloMahiGoa/lillybabe-partner-surge) | **Surge** | https://lillybabe-partner-surge.surge.sh/ |
| [lillybabe-partner-gitlab](https://github.com/HelloMahiGoa/lillybabe-partner-gitlab) | **GitLab Pages** | https://lillybabe-partner-gitlab-58412d.gitlab.io/ |
| [lillybabe-partner-render](https://github.com/HelloMahiGoa/lillybabe-partner-render) | **Render** | https://lillybabe-partner-render.onrender.com/ |
| [lillybabe-partner-tiiny](https://github.com/HelloMahiGoa/lillybabe-partner-tiiny) | **Tiiny Host** | https://lillybabe.tiiny.site/ |
| [lillybabe-partner-cloudflare](https://github.com/HelloMahiGoa/lillybabe-partner-cloudflare) | **Cloudflare Pages** | https://lillybabe-partner-cloudflare.pages.dev/ |
| [lillybabe-partner-firebase](https://github.com/HelloMahiGoa/lillybabe-partner-firebase) | **Firebase Hosting** | https://studio-9048837108-f3ed0.web.app/ |
| [lillybabe-partner-azure](https://github.com/HelloMahiGoa/lillybabe-partner-azure) | **Azure Static Web Apps** | https://ambitious-beach-0394c6410.7.azurestaticapps.net/ |
| [lillybabe-partner-deno](https://github.com/HelloMahiGoa/lillybabe-partner-deno) | **Deno Deploy** | https://lillybabe-dk7226c4ec8k.lillybabe.deno.net/ |
| [lillybabe-partner-infinityfree](https://github.com/HelloMahiGoa/lillybabe-partner-infinityfree) | **InfinityFree** | https://lillybabe.xo.je/ |

## In repo — deploy when ready (no CI wired)

| Repo | Platform | Notes |
|------|----------|--------|
| [lillybabe-partner-amplify](https://github.com/HelloMahiGoa/lillybabe-partner-amplify) | **AWS Amplify** | Connect repo; `amplify.yml` included |
| [lillybabe-partner-workers](https://github.com/HelloMahiGoa/lillybabe-partner-workers) | **Cloudflare Workers** | Static via Workers; separate from Pages |
| [lillybabe-partner-heliohost](https://github.com/HelloMahiGoa/lillybabe-partner-heliohost) | **HelioHost** | FTP upload to `htdocs` |
| [lillybabe-partner-awardspace](https://github.com/HelloMahiGoa/lillybabe-partner-awardspace) | **AwardSpace** | FTP upload |
| [lillybabe-partner-codeberg](https://github.com/HelloMahiGoa/lillybabe-partner-codeberg) | **Codeberg Pages** | Mirror to Codeberg; see `codeberg/PAGES-SETUP.md` |
| [lillybabe-partner-bitbucket](https://github.com/HelloMahiGoa/lillybabe-partner-bitbucket) | **Bitbucket Pages** | Mirror to Bitbucket; enable static site |
| [lillybabe-partner-statichost](https://github.com/HelloMahiGoa/lillybabe-partner-statichost) | **Statichost.eu** | Upload or Git per host docs |
| [lillybabe-partner-fly](https://github.com/HelloMahiGoa/lillybabe-partner-fly) | **Fly.io** | `fly.toml` + `Dockerfile` for nginx static |
| [lillybabe-partner-zeabur](https://github.com/HelloMahiGoa/lillybabe-partner-zeabur) | **Zeabur** | Connect Git in Zeabur dashboard |
| [lillybabe-partner-oracle](https://github.com/HelloMahiGoa/lillybabe-partner-oracle) | **Oracle VPS** | Self-host: copy files to nginx/Caddy on Always Free VM |

Do **not** enable GitHub Pages on non-github-pages repos or deploy variants to other hosts.

Free hosting options: [FREE-DEPLOY.md](FREE-DEPLOY.md).
