#!/usr/bin/env python3
"""Interactive test of quiz + checklist JS on the atomic-structure-periodicity page."""
import json
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:8080/topics/chem/atomic-structure-periodicity/index.html"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1400, "height": 1000})
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(600)

    # checklist: click items 0,1,2 -> pill should show 3/25, fill width 12%
    page.evaluate("document.querySelectorAll('#cl li')[0].click(); document.querySelectorAll('#cl li')[1].click(); document.querySelectorAll('#cl li')[2].click();")
    after = page.evaluate("JSON.stringify({pill:document.getElementById('progPill').textContent, done:document.querySelectorAll('#cl li.done').length, fill:document.getElementById('fill').style.width})")
    print("CHECKLIST after 3 clicks:", after)

    # persistence: reload, expect still 3 done
    page.reload(wait_until="networkidle")
    persisted = page.evaluate("JSON.stringify({pill:document.getElementById('progPill').textContent, done:document.querySelectorAll('#cl li.done').length})")
    print("CHECKLIST after reload:", persisted)

    # quiz: answer q1 correct, q2 wrong
    r1 = page.evaluate("(() => { const q=document.querySelectorAll('.q')[0]; const c=q.querySelector('input[value=\"'+q.dataset.a+'\"]'); c.checked=true; c.dispatchEvent(new Event('change',{bubbles:true})); return q.className; })()")
    r2 = page.evaluate("(() => { const q=document.querySelectorAll('.q')[1]; const w=q.querySelector('input:not([value=\"'+q.dataset.a+'\"])'); w.checked=true; w.dispatchEvent(new Event('change',{bubbles:true})); return q.className; })()")
    print("QUIZ q1 (correct answer):", r1)
    print("QUIZ q2 (wrong answer):", r2)

    # every quiz question must have exactly one data-a answer that exists among its radios
    missing = page.evaluate("(() => { const bad=[]; document.querySelectorAll('.q').forEach((q,i)=>{ const vals=[...q.querySelectorAll('input')].map(x=>x.value); if(!vals.includes(q.dataset.a)) bad.push(i); }); return JSON.stringify(bad); })()")
    print("QUIZ questions missing their data-a answer:", missing)

    # console errors?
    console_errors = []
    page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else None)
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(500)
    print("CONSOLE errors on load:", console_errors if console_errors else "none")

    browser.close()
