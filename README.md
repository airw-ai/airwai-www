# Airwai — Marketing Site

Source of truth for **airwai.com** — Airwai's public marketing surface. MkDocs site sharing the `adx-*` design system with [docs.airwai.com](https://docs.airwai.com) and [partners.airwai.com](https://partners.airwai.com). Deployed to GitHub Pages.

---

## What's here

```
airwai-www/
├── docs/                ← site content (markdown)
│   ├── index.md         ← marketing home
│   ├── laira.md         ← LAIRA platform deep-dive
│   ├── pricing.md       ← Federal procurement + pricing
│   ├── customers/       ← Case studies
│   │   ├── index.md     ← Index page (also visible at /customers/)
│   │   └── sbd.md       ← San Bernardino International Airport
│   ├── company.md       ← About Airwai
│   ├── brand-guide.md   ← Brand system reference
│   ├── legal/           ← Privacy, Terms, Cookie Preferences
│   ├── assets/          ← Logo + favicon
│   ├── stylesheets/     ← adx-* design system CSS (shared with docs + partners)
│   └── CNAME            ← airwai.com
├── overrides/           ← MkDocs Material theme partials
├── mkdocs.yml           ← Site config + nav
├── requirements.txt     ← Python deps
├── .github/workflows/   ← CI: build + deploy on push to main
├── DEPLOY.md            ← Operator notes for first-time setup
└── README.md            ← This file
```

---

## Local development

```bash
# from this folder
pip install -r requirements.txt
mkdocs serve
# → http://127.0.0.1:8000
```

Hot-reloads on any markdown change.

Build:

```bash
mkdocs build --strict
# output in ./site/
```

`--strict` fails on broken links or missing nav entries. Always use it before pushing.

---

## Architecture

- **Static MkDocs site** hosted on GitHub Pages (free tier, custom domain via CNAME)
- **Cloudflare DNS** authoritative for airwai.com (since 2026-05-19); the `airwai.com` apex CNAMEs to `airw-ai.github.io` once this rebuild ships
- **Cloudflare proxy** orange-cloud on the apex for WAF + Web Analytics + edge TLS
- **No CMS, no PHP, no plugins.** Authoring in Markdown + Git. Replaces the previous WordPress + Elementor Cloud stack (decommissioned 2026-05).
- **Design system:** `adx-*` CSS classes proven on docs.airwai.com and partners.airwai.com; the same `airwai-docs-v3.css` ships in all three repos.

---

## Decisions baked into this scaffold

Per the airwai.com inventory and consolidation thesis (see `Strategy/2026-05-19 - Inventory - airwai.com Current State.md`):

- **Dropped:** `/industries/` (stock Elementor demo content), `/contact/` (stock demo content; contact intake folded into `/pricing/` HubSpot form)
- **Kept:** Home, LAIRA platform, Pricing & Procurement, Company, Brand Guide, SBD case study, Privacy/Terms/Cookie Preferences
- **New:** `/customers/` index page (fixes the 404 the old home page linked to)
- **HubSpot form embed** lives on `/pricing/` — needs portalId + formId from Amir before content ships

---

## How updates flow

1. Edit markdown locally or in the GitHub editor
2. Push to `main` via PR
3. GitHub Actions builds with `mkdocs build --strict` and deploys to GitHub Pages
4. airwai.com serves the new content within ~2 minutes

---

## Companion repos

| Repo | Surface |
|:---|:---|
| `airw-ai/airwai-www` (this) | airwai.com — public marketing |
| `airw-ai/airwai-documentation` | docs.airwai.com — public technical docs |
| `airw-ai/laira-partners` | partners.airwai.com — gated partner kit |
