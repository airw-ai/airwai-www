# Deploy — airwai.com

First-time setup notes for the `airwai-www` repo. Same pattern as `airwai-documentation` and `laira-partners`. Estimated time: ~20 minutes (Cloudflare DNS is already authoritative, which removes the GoDaddy nameserver step).

---

## Prerequisites

- GitHub org access (`airw-ai/`)
- Cloudflare One access (`airwai.com` already on Cloudflare since 2026-05-19)

---

## Step 1 — Create the GitHub repo

```bash
# from this airwai-www/ folder
git init
git add .
git commit -m "Initial airwai.com scaffold"
git branch -M main
gh repo create airw-ai/airwai-www --public --source . --remote origin --push
```

Public is intentional — airwai.com is public-facing. If you prefer a private repo with public Pages, use `--private` and toggle Pages visibility settings later.

---

## Step 2 — Enable GitHub Pages

Settings → Pages:
- **Source:** GitHub Actions (not branch — we deploy via workflow)
- **Custom domain:** leave blank initially; will be set when the apex cutover happens (Step 4)

The first push to `main` triggers `.github/workflows/docs.yml`, which builds with `mkdocs build --strict` and deploys to the `github-pages` environment.

---

## Step 3 — Test before cutover

The site will be live at `airw-ai.github.io/airwai-www/` once Pages deploy completes. Smoke-test the build there. Don't touch the airwai.com DNS yet.

---

## Step 4 — The apex cutover (the load-bearing step)

`airwai.com` currently has two A records pointing to Elementor's Cloudflare instance. Cutover replaces them with a CNAME-flattened pointer to GitHub Pages.

1. **In Cloudflare** → `airwai.com` → **DNS → Records**
2. **Delete** the two apex A records:
   - `airwai.com  A  162.159.137.9`
   - `airwai.com  A  162.159.138.9`
3. **Add** a single CNAME at apex (Cloudflare CNAME-flattens automatically):
   - **Type:** CNAME
   - **Name:** `@` (apex)
   - **Target:** `airw-ai.github.io`
   - **Proxy status:** Proxied (orange cloud) — gets WAF + Web Analytics
   - **TTL:** Auto
4. **Update the `www` CNAME** if you want to keep `www.airwai.com`:
   - Currently CNAMEs to `tgcsqplr.elementor.cloud` (gray cloud)
   - Change target to `airw-ai.github.io`
   - Toggle proxy to orange
5. **Add `airwai.com` as the custom domain** in GitHub repo Settings → Pages
6. Wait ~2 min for GitHub to provision the cert and verify the CNAME

---

## Step 5 — Decommission Elementor Cloud

Once airwai.com is serving from GitHub Pages and verified working for at least a week:

1. Cancel the Elementor Cloud subscription (~$249/yr savings)
2. Export any final media from the WordPress media library if not already done
3. Confirm the cancellation date in calendar

---

## Companion config

| File | Purpose |
|:---|:---|
| `mkdocs.yml` | Site config, nav, theme |
| `.github/workflows/docs.yml` | Build + deploy pipeline |
| `docs/CNAME` | Tells GitHub Pages which custom domain to serve (`airwai.com`) |
| `docs/stylesheets/` | Shared `adx-*` design system |
| `overrides/` | MkDocs Material theme overrides |

---

## Rollback plan

If anything goes wrong at the apex cutover:

1. Re-add the two A records (162.159.137.9, 162.159.138.9) to Cloudflare DNS, both gray-cloud
2. Remove the CNAME at apex
3. Site reverts to Elementor instantly (TTL is 1=auto on Cloudflare; propagation under a minute)

Keep the old WordPress admin credentials accessible until Elementor Cloud is cancelled. Don't cancel the subscription on Day 1 of the cutover; wait at least a week of stable operation.
