#!/usr/bin/env python3
"""Run collision + pagecheck audits on a topic page via Playwright (headless Chrome).
Usage: python run_audits.py <url> [<url> ...]
"""
import sys, json, urllib.request
from playwright.sync_api import sync_playwright

def fetch(url):
    return urllib.request.urlopen(url).read().decode()

AC = fetch("http://127.0.0.1:8080/assets/_audit/audit_collisions.js")
PC = fetch("http://127.0.0.1:8080/assets/_audit/audit_pagecheck.js")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for url in sys.argv[1:]:
        page = browser.new_page(viewport={"width": 1400, "height": 1000})
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(800)
        ac = page.evaluate(AC)
        pc = page.evaluate(PC)
        print(f"URL: {url}")
        print("  COLLISIONS:", ac)
        print("  PAGECHECK:", pc)
        page.close()
    browser.close()
