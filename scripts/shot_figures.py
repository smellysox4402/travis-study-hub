#!/usr/bin/env python3
"""Screenshot every figure render in assets/_audit for the vision pass.
Usage: python shot_figures.py <prefix>  (e.g. reproduction)
Output: cache/screenshots/audit_<prefix>__<n>.png
"""
import sys, os, glob
from playwright.sync_api import sync_playwright

prefix = sys.argv[1] if len(sys.argv) > 1 else "reproduction"
root = r"C:\Users\ASUS\Desktop\Hermes_Workspace\study-hub\assets\_audit"
out_dir = r"C:\Users\ASUS\AppData\Local\hermes\cache\screenshots"
os.makedirs(out_dir, exist_ok=True)

files = sorted(glob.glob(os.path.join(root, f"{prefix}__*.html")))
print(f"{len(files)} renders to shoot")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 900, "height": 700}, device_scale_factor=1.5)
    for f in files:
        base = os.path.basename(f).replace(".html", "")
        url = "file:///" + f.replace("\\", "/")
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(400)
        svg = page.query_selector("svg")
        if not svg:
            print(f"  {base}: NO SVG")
            continue
        box = svg.bounding_box()
        shot = os.path.join(out_dir, f"audit_{base}.png")
        page.screenshot(clip={"x": box["x"], "y": box["y"], "width": box["width"], "height": box["height"]}, path=shot)
        print(f"  {base}: {box['width']:.0f}x{box['height']:.0f} -> {shot}")
    browser.close()
print("done")
