# Airwai — Marketing Site

Source of truth for **airwai.com** — Airwai's public marketing surface. Hand-built static HTML with a tiny Python build step that injects shared nav, footer, and CSS into per-page content. Deployed to GitHub Pages via Cloudflare.

The marketing site is intentionally not MkDocs — that stack runs [docs.airwai.com](https://docs.airwai.com) and [partners.airwai.com](https://partners.airwai.com) where markdown ergonomics fit. Marketing benefits from full layout control.

---

## Repo layout

```
airwai-www/
├── src/                          ← source pages (body content + metadata)
│   ├── index.html                ← home
│   ├── laira.html
│   ├── pricing.html
│   ├── customers.html
│   ├── customers/sbd.html        ← nested route
│   ├── company.html
│   ├── contact.html
│   └── legal/{privacy,terms,cookies}.html
├── _partials/                    ← shared chrome (edit once → applies everywhere)
│   ├── base.html                 ← HTML wrapper with markers
│   ├── nav.html                  ← site nav
│   └── footer.html               ← 4-col docs-mirrored footer
├── docs/                         ← built output (uploaded to GitHub Pages)
│   ├── assets/airwai.css         ← shared CSS (linked from every page)
│   ├── assets/airwai-wordmark.svg
│   ├── assets/favicon.svg
│   ├── CNAME                     ← airwai.com
│   ├── .nojekyll
│   └── <generated HTML files>    ← rebuilt every push by build.py
├── build.py                      ← combines src/ + _partials/ → docs/
├── .github/workflows/docs.yml    ← CI runs build.py then deploys
├── DEPLOY.md                     ← Operator notes
└── README.md                     ← This file
```

---

## Authoring a page

A source file in `src/` looks like:

```html
<!-- @meta
title: My Page · Airwai
description: SEO meta description.
body-class: legal-page   # optional — narrow reading container
@meta-end -->

<style>
  /* Optional page-specific CSS goes here */
</style>

<section class="hero dark">
  ...
</section>

<section>
  ...
</section>
```

The build script reads the `@meta` block, extracts any inline `<style>` block as page-specific CSS, takes the rest as body content, and wraps everything with the partials.

---

## Local development

```bash
# build the site
python3 build.py

# serve docs/ locally
python3 -m http.server -d docs 8000
# → http://127.0.0.1:8000
```

`build.py` regenerates everything from `src/` + `_partials/`. No third-party dependencies — uses only the Python 3 standard library.

---

## How updates flow

1. Edit a file in `src/` (or `_partials/` if changing nav/footer/base, or `docs/assets/airwai.css` for site-wide style)
2. Push to `main`
3. GitHub Actions runs `python3 build.py` then deploys `docs/` to Pages
4. airwai.com serves the new content within ~2 minutes

---

## Architecture

- **Build step:** small Python script (no deps) reads `src/` and `_partials/`, writes `docs/`
- **Hosting:** GitHub Pages serves `docs/` via the workflow in `.github/workflows/docs.yml`
- **DNS:** Cloudflare (since 2026-05-19); apex CNAMEs to `airw-ai.github.io`
- **CDN/Edge:** Cloudflare proxy in front (WAF + Web Analytics + TLS termination)
- **Replaces:** the prior WordPress + Elementor Cloud stack (decommissioned 2026-05)

---

## Companion repos

| Repo | Surface | Stack |
|:---|:---|:---|
| `airw-ai/airwai-www` (this) | airwai.com — public marketing | Static HTML + Python build script |
| `airw-ai/airwai-documentation` | docs.airwai.com — public technical docs | MkDocs Material |
| `airw-ai/laira-partners` | partners.airwai.com — gated partner kit (Cloudflare Access) | MkDocs Material |
