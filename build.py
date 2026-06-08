#!/usr/bin/env python3
"""
airwai-www build script.

Reads sources from src/, partials from _partials/, and writes the
generated site to docs/. Each source file is a body-only HTML
fragment with metadata in a header comment block:

    <!-- @meta
    title: Page Title · Airwai
    description: Meta description for SEO and social.
    body-class: legal-page    # optional; e.g., for narrow reading container
    @meta-end -->

    <style>
      /* optional page-specific CSS */
    </style>

    <section class="...">
      ... body content ...
    </section>

The build script:
  1. Reads every src/<page>.html (recursive).
  2. Parses the @meta block.
  3. Optionally extracts a single top-level <style>...</style> block as page CSS.
  4. The remainder is the body content.
  5. Injects everything into _partials/base.html with the nav and footer.
  6. Writes docs/<page>/index.html (or docs/index.html for src/index.html).

Output path mapping:
  src/index.html               → docs/index.html
  src/laira.html               → docs/laira/index.html
  src/customers/sbd.html       → docs/customers/sbd/index.html
  src/legal/privacy.html       → docs/privacy/index.html      # legal/ folder stripped

Asset prefix is computed from output depth:
  docs/index.html              → ASSET_PREFIX=""
  docs/laira/index.html        → ASSET_PREFIX="../"
  docs/customers/sbd/index.html → ASSET_PREFIX="../../"
"""

from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).parent
SRC = ROOT / "src"
PARTIALS = ROOT / "_partials"
DOCS = ROOT / "docs"


def read(path):
    return Path(path).read_text()


def parse_meta(text):
    """Parse the <!-- @meta ... @meta-end --> block. Returns (meta dict, remaining text)."""
    m = re.search(r"<!--\s*@meta\s*(.*?)\s*@meta-end\s*-->", text, re.DOTALL)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, text[:m.start()] + text[m.end():]


def extract_style(text):
    """Pull a single top-level <style>...</style> block out of the source.
    Returns (style_block_or_empty, remaining_text)."""
    m = re.search(r"<style>.*?</style>", text, re.DOTALL)
    if not m:
        return "", text
    return m.group(0), text[:m.start()] + text[m.end():]


def strip_hidden(text):
    """Remove <!-- @hidden ... --> ... <!-- @hidden-end --> blocks entirely.

    Keeps unapproved/embargoed content (e.g., a customer reference pending
    publish permission) in the source tree while ensuring it is absent from
    the published output — not even present as an HTML comment that
    view-source would expose. To restore the content, delete the marker pair
    and rebuild.
    """
    return re.sub(
        r"<!--\s*@hidden\b.*?@hidden-end\s*-->\s*", "", text, flags=re.DOTALL
    )


def output_path(src_path):
    """Map src/<rel>.html → docs/<rel>/index.html (with legal/ folder stripped)."""
    rel = src_path.relative_to(SRC)
    parts = list(rel.parts)
    # Strip "legal/" folder (legal pages live at top-level URLs)
    if parts[0] == "legal":
        parts = parts[1:]
    # rename "index.html" → "index.html" (no change)
    # rename "<name>.html" → "<name>/index.html"
    if parts[-1] == "index.html":
        return DOCS.joinpath(*parts)
    name = parts[-1][:-5]  # strip .html
    return DOCS.joinpath(*parts[:-1], name, "index.html")


def asset_prefix_for(out_path):
    """Number of '../' needed to reach docs/ from the output file's directory."""
    rel = out_path.relative_to(DOCS).parent
    depth = len(rel.parts)
    return "../" * depth


def build_page(src_path, base_tpl, nav_tpl, footer_tpl):
    text = read(src_path)
    meta, text = parse_meta(text)
    style, text = extract_style(text)
    text = strip_hidden(text)

    out_path = output_path(src_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    prefix = asset_prefix_for(out_path)

    # Resolve partials' asset prefixes
    nav = nav_tpl.replace("{{ASSET_PREFIX}}", prefix)
    footer = footer_tpl.replace("{{ASSET_PREFIX}}", prefix)

    # body class
    body_cls = meta.get("body-class", "").strip()
    body_class_attr = f' class="{body_cls}"' if body_cls else ""

    page = (
        base_tpl
        .replace("{{TITLE}}", meta.get("title", "Airwai"))
        .replace("{{DESCRIPTION}}", meta.get("description", ""))
        .replace("{{ASSET_PREFIX}}", prefix)
        .replace("{{PAGE_CSS}}", style)
        .replace("{{BODY_CLASS}}", body_class_attr)
        .replace("{{NAV}}", nav.strip())
        .replace("{{CONTENT}}", text.strip())
        .replace("{{FOOTER}}", footer.strip())
    )

    out_path.write_text(page)
    return out_path, len(page)


def main():
    if not SRC.exists():
        print(f"FATAL: {SRC} does not exist.", file=sys.stderr)
        sys.exit(1)

    base = read(PARTIALS / "base.html")
    nav = read(PARTIALS / "nav.html")
    footer = read(PARTIALS / "footer.html")

    # Wipe and recreate docs/ except for CNAME, .nojekyll, and assets/ which we want to preserve
    preserved = {DOCS / "CNAME", DOCS / ".nojekyll", DOCS / "assets"}
    for child in DOCS.iterdir():
        if child in preserved:
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    sources = sorted(SRC.rglob("*.html"))
    if not sources:
        print(f"WARN: no source files found in {SRC}/", file=sys.stderr)
        sys.exit(1)

    print(f"Building {len(sources)} page(s) from {SRC}/ → {DOCS}/\n")
    for src_path in sources:
        out_path, size = build_page(src_path, base, nav, footer)
        rel_src = src_path.relative_to(ROOT)
        rel_out = out_path.relative_to(ROOT)
        print(f"  {rel_src}  →  {rel_out}  ({size:,} bytes)")
    print(f"\nDone. {len(sources)} pages built.")


if __name__ == "__main__":
    main()
