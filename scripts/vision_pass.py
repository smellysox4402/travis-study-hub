#!/usr/bin/env python3
"""Vision pass: audit all reproduction figure screenshots via local Ollama qwen2.5vl:3b.
Usage: python vision_pass.py [--prefix reproduction] [--limit N]
Output: cache/screenshots/vision_results_<prefix>.json
"""
import base64, glob, json, os, sys, argparse, time

OLLAMA = "http://127.0.0.1:11434"
MODEL = "qwen2.5vl:3b"
SHOT_DIR = r"C:\Users\ASUS\AppData\Local\hermes\cache\screenshots"

PROMPT = """Audit this neon SVG biology diagram (IB topic D3.1 Reproduction). Answer with a single line: PASS or FLAG, then a short reason. Check: (1) any text labels clipped at an edge? (2) any text overlapping other text? (3) any dangling leader lines/arrows pointing at nothing? (4) does the diagram match its title/labels (domain correctness)? Be strict about (1)-(3)."""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", default="reproduction")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    import urllib.request
    files = sorted(glob.glob(os.path.join(SHOT_DIR, f"audit_{args.prefix}__*.png")))
    if args.limit:
        files = files[:args.limit]
    print(f"{len(files)} figures to audit")

    results = {}
    for i, f in enumerate(files, 1):
        base = os.path.basename(f).replace("audit_", "").replace(".png", "")
        b64 = base64.b64encode(open(f, "rb").read()).decode()
        payload = json.dumps({
            "model": MODEL,
            "prompt": PROMPT,
            "images": [b64],
            "stream": False,
            "options": {"temperature": 0},
        }).encode()
        req = urllib.request.Request(OLLAMA + "/api/generate", data=payload,
                                     headers={"Content-Type": "application/json"})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=300) as r:
                    resp = json.loads(r.read())
                verdict = resp.get("response", "").strip().replace("\n", " ")
                results[base] = verdict
                print(f"  [{i}/{len(files)}] {base[:45]} -> {verdict[:110]}")
                break
            except Exception as e:
                print(f"  [{i}] retry {attempt+1}: {e}")
                time.sleep(3)
        else:
            results[base] = "ERROR"
            print(f"  [{i}] {base[:45]} -> ERROR")

    out = os.path.join(SHOT_DIR, f"vision_results_{args.prefix}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    flags = [k for k, v in results.items() if v.startswith("FLAG") or v == "ERROR"]
    print(f"\n{len(files)} audited, {len(flags)} flagged")
    for k in flags:
        print(f"  FLAG {k}: {results[k]}")
    print(f"results -> {out}")

if __name__ == "__main__":
    main()
