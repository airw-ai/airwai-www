# Airwai — Marketing Site

Source of truth for **airwai.com** — Airwai's public marketing surface. **Static HTML site** (no build step) sourced from the wireframes in `Marketing/Wireframes/`. Deployed to GitHub Pages.

The marketing site is intentionally NOT MkDocs — that stack is used for [docs.airwai.com](https://docs.airwai.com) and [partners.airwai.com](https://partners.airwai.com) where its markdown ergonomics fit. Marketing benefits from full layout control, so each page is hand-built HTML with inline brand CSS.

---

## What's here

```
airwai-www/
├── docs/                          ← what gets served
│   ├── .nojekyll                  ← tells GitHub Pages to skip Jekyll processing
│   ├── CNAME                      ← airwai.com (used at apex cutover)
│   ├── index.html                 ← Home (/)
│   ├── laira/index.html           ← LAIRA platform (/laira/)
│   ├── pricing/index.html         ← Pricing & procurement (/pricing/)
│   ├── customers/index.html       ← Customer index (/customers/)
│   ├── customers/sbd/index.html   ← SBD case study (/customers/sbd/)
│   ├── company/index.html         ← Company (/company/)
│   └── assets/                    ← Logo, favicon
├── .github/workflows/docs.yml     ← CI: upload docs/ to Pages on push to main
├── .gitignore
├── DEPLOY.md                      ← Operator notes for first-time setup + apex cutover
└── README.md                      ← This file
```

Each page is self-contained: inline CSS, no shared JS. Brand tokens (Chalk, Ink, Federal Navy, Signal Lime) and grid system (1240px container, 12-column) are duplicated per page. Slightly redundant but maximally maintainable — change one page without worrying about regressions on the others.

---

## Local development

Open any `docs/<page>/index.html` directly in a browser, or serve the folder:

```bash
# from this folder
python3 -m http.server -d docs 8000
# → http://127.0.0.1:8000
```

No build step, no MkDocs, no Python dependencies.

---

## Architecture

- **Static HTML** with inline brand CSS (Söhne / Suisse Int'l / Suisse Screen with Inter / JetBrains Mono fallbacks). No build tools.
- **GitHub Pages** serves `docs/` directly via the workflow in `.github/workflows/docs.yml`.
- **Cloudflare DNS** authoritative for airwai.com (since 2026-05-19); the apex CNAMEs to `airw-ai.github.io` once the rebuild ships (see DEPLOY.md Step 4).
- **Cloudflare proxy** orange-cloud on the apex for WAF + Web Analytics + edge TLS.
- **Replaces:** the previous WordPress + Elementor Cloud stack (decommissioned 2026-05).

---

## Decisions baked into this repo

Per the airwai.com inventory and consolidation thesis (see `Strategy/2026-05-19 - Inventory - airwai.com Current State.md`):

- **Dropped:** `/industries/` (stock Elementor demo content), `/contact/` (stock demo content; contact intake folded into the `/pricing/#scope` HubSpot form)
- **Kept:** Home, LAIRA platform, Pricing & Procurement, Customers index + SBD case study, Company
- **Source:** wireframes in `Marketing/Wireframes/` — design system v2 (brand guide-aligned, light-default with one dark cognitive-break section)
- **`/brand-guide/`** lives at docs.airwai.com (not duplicated on the marketing site)
- **Legal pages** (`/privacy/`, `/terms/`, `/cookies/`) referenced from the footer but not yet ported; footer links will 404 until added

---

## How updates flow

1. Edit any `docs/<page>/index.html` in any editor
2. Push to `main` via PR
3. GitHub Actions uploads `docs/` to Pages
4. airwai.com serves the new content within ~2 minutes

---

## Companion repos

| Repo | Surface | Stack |
|:---|:---|:---|
| `airw-ai/airwai-www` (this) | airwai.com — public marketing | Static HTML |
| `airw-ai/airwai-documentation` | docs.airwai.com — public technical docs | MkDocs Material |
| `airw-ai/laira-partners` | partners.airwai.com — gated partner kit (Cloudflare Access) | MkDocs Material |
