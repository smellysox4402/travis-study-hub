#!/usr/bin/env python3
"""Vision pass for the atomic-structure-periodicity figures (qwen2.5vl:3b local).
Audits rendered neon SVG diagrams for clipping, overlapping text, dangling
leader lines, and domain correctness vs their titles.
"""
import base64, glob, json, os, sys, urllib.request, time

OLLAMA = "http://127.0.0.1:11434"
MODEL = "qwen2.5vl:3b"
SHOT_DIR = r"C:\Users\ASUS\AppData\Local\hermes\cache\screenshots"

PROMPT = """Audit this neon SVG chemistry diagram (IB topic Atomic Structure & Periodicity). Answer with a single line: PASS or FLAG, then a short reason. Check: (1) any text labels clipped at an edge of the drawing? (2) any text overlapping other text? (3) any dangling leader lines/arrows pointing at nothing? (4) does the diagram match its title/labels (domain correctness)? Be strict about (1)-(3)."""

def main():
    files = sorted(glob.glob(os.path.join(SHOT_DIR, "audit_atomic-structure-periodicity__*.png")))
    print(f"{len(files)} figures to audit")
    results = {}
    for f in files:
        base = os.path.basename(f).replace("audit_", "").replace(".png", "")
        b64 = base64.b64encode(open(f, "rb").read()).decode()
        payload = json.dumps({
            "model": MODEL,
            "prompt": PROMPT,
            "images": [b64],
            "stream": False,
            "options": {"temperature": 0.1},
        }).encode()
        req = urllib.request.Request(OLLAMA + "/api/generate", payload, {"Content-Type": "application/json"})
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=180).read())
            verdict = r.get("response", "").strip().split("\n")[0]
        except Exception as e:
            verdict = f"ERROR {e}"
        results[base] = verdict
        print(f"{base}: {verdict}")
        time.sleep(0.5)
    out = os.path.join(SHOT_DIR, "vision_results_atomic_structure.json")
    json.dump(results, open(out, "w", encoding="utf-8"), indent=1)
    print("saved", out)

if __name__ == "__main__":
    main()
