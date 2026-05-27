# Deploy one repo -> one platform

Each GitHub repo deploys **only** to its matching host.

| Repo | Platform | Deploy command / setup |
|------|----------|------------------------|
| [lillybabe-partner-github-pages](https://github.com/HelloMahiGoa/lillybabe-partner-github-pages) | **GitHub Pages** | Enabled on `main` / root. URL: `https://hellomahigoa.github.io/lillybabe-partner-github-pages/` |
| [lillybabe-partner-vercel](https://github.com/HelloMahiGoa/lillybabe-partner-vercel) | **Vercel** | `cd vercel && npx vercel deploy --prod` |
| [lillybabe-partner-netlify](https://github.com/HelloMahiGoa/lillybabe-partner-netlify) | **Netlify** | `cd netlify && netlify deploy --prod --dir .` |
| [lillybabe-partner-surge](https://github.com/HelloMahiGoa/lillybabe-partner-surge) | **Surge** | `cd surge && npx surge . lillybabe-partner-surge.surge.sh` |
| [lillybabe-partner-gitlab](https://github.com/HelloMahiGoa/lillybabe-partner-gitlab) | **GitLab Pages** | https://lillybabe-partner-gitlab-58412d.gitlab.io/ |
| [lillybabe-partner-render](https://github.com/HelloMahiGoa/lillybabe-partner-render) | **Render** | https://lillybabe-partner-render.onrender.com/ |
| [lillybabe-partner-tiiny](https://github.com/HelloMahiGoa/lillybabe-partner-tiiny) | **Tiiny Host** | https://lillybabe.tiiny.site/ |
| [lillybabe-partner-cloudflare](https://github.com/HelloMahiGoa/lillybabe-partner-cloudflare) | **Cloudflare Pages** | https://lillybabe-partner-cloudflare.pages.dev/ |
| [lillybabe-partner-firebase](https://github.com/HelloMahiGoa/lillybabe-partner-firebase) | **Firebase Hosting** | https://studio-9048837108-f3ed0.web.app/ |
| [lillybabe-partner-azure](https://github.com/HelloMahiGoa/lillybabe-partner-azure) | **Azure Static Web Apps** | https://ambitious-beach-0394c6410.7.azurestaticapps.net/ |
| [lillybabe-partner-deno](https://github.com/HelloMahiGoa/lillybabe-partner-deno) | **Deno Deploy** | https://lillybabe-dk7226c4ec8k.lillybabe.deno.net/ |
| [lillybabe-partner-infinityfree](https://github.com/HelloMahiGoa/lillybabe-partner-infinityfree) | **InfinityFree** | https://lillybabe.xo.je/ |

Do **not** enable GitHub Pages on non-github-pages repos or deploy variants to other hosts.

Free hosting options and limits: [FREE-DEPLOY.md](FREE-DEPLOY.md).
