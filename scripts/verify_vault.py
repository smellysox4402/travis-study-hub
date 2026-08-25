import sys
from playwright.sync_api import sync_playwright

topic = sys.argv[1] if len(sys.argv) > 1 else "kinetics"
url = f"http://127.0.0.1:8080/topics/chem/{topic}/index.html"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    errors = []
    pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(url, wait_until="networkidle")
    pg.wait_for_timeout(500)
    result = pg.evaluate("""() => ({
        title: document.title,
        vault: !!document.getElementById('vault'),
        vaultH2: (document.querySelector('#vault h2')||{}).textContent || null,
        panels: document.querySelectorAll('#vault .panel').length,
        defRows: document.querySelectorAll('#vault .panel')[0].querySelectorAll('table tr').length,
        examQs: document.querySelectorAll('#vault .exam').length,
        navHasVault: !!document.querySelector('nav a[href="#vault"]'),
        pill: (document.getElementById('progPill')||{}).textContent || null,
        checklistItems: document.querySelectorAll('#cl li').length,
        quizQs: document.querySelectorAll('.q').length,
    })""")
    pg.screenshot(path=f"/tmp/vault_{topic}.png", full_page=True)
    b.close()

import json
print(json.dumps(result, indent=2, ensure_ascii=False))
print("CONSOLE ERRORS:", errors if errors else "none")
