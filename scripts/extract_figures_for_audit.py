#!/usr/bin/env python3
"""Extract every <svg> from all study-hub topic pages into standalone HTML renders
for the diagram audit (vision comparison + collision checks on a clean single-figure view).

Usage: python scripts/extract_figures_for_audit.py
Output: assets/_audit/<page>__<n>__<slug>.html + manifest.txt
"""
import os, re, html, sys

ROOT = r"C:\Users\ASUS\Desktop\Hermes_Workspace\study-hub"
OUT = os.path.join(ROOT, "assets", "_audit")
PAGES = [
    "topics/bio/c2.1/index.html",
    "topics/bio/gas-exchange/index.html",
    "topics/bio/muscle-motility/index.html",
    "topics/bio/cell-division/index.html",
    "topics/bio/inheritance/index.html",
    "topics/chem/kinetics/index.html",
]

def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s[:40] or "fig"

os.makedirs(OUT, exist_ok=True)
manifest = []
total = 0

for page in PAGES:
    path = os.path.join(ROOT, page)
    src = open(path, encoding="utf-8").read()
    page_tag = page.split("/")[-2]
    # find svg blocks (non-greedy, no nesting inside svg)
    for i, m in enumerate(re.finditer(r"<svg\b[^>]*>.*?</svg>", src, re.S)):
        svg = m.group(0)
        # aria-label = figure title for humans
        am = re.search(r'aria-label="([^"]*)"', svg)
        aria = html.unescape(am.group(1)) if am else "no aria-label"
        # first <text> = title
        tm = re.search(r'<text[^>]*>([^<]{3,60})</text>', svg)
        title = html.unescape(tm.group(1)) if tm else ""
        slug = slugify(title or aria)
        fn = f"{page_tag}__{i}__{slug}.html"
        out_path = os.path.join(OUT, fn)
        # bump width so labels are legible in screenshots; keep aspect via viewBox
        standalone = (
            "<!doctype html><html><head><meta charset='utf-8'>"
            "<style>body{margin:0;background:#150a26;font-family:'Segoe UI',system-ui,-apple-system,sans-serif}svg{display:block;width:880px;height:auto}</style>"
            f"</head><body>{svg}</body></html>"
        )
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(standalone)
        manifest.append(f"{page}\t#{i}\t{title}\t{aria}\t{fn}")
        total += 1

with open(os.path.join(OUT, "manifest.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(manifest))

print(f"extracted {total} svgs to {OUT}")
for line in manifest:
    print(line)
