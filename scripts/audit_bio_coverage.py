#!/usr/bin/env python3
import re, os

SYL = r"C:/Users/ASUS/Desktop/Hermes_Workspace/IB_Study/bio_hl/syllabus_extracted.txt"
syl = open(SYL, encoding="utf-8", errors="replace").read()

# ---- current IB syllabus codes. Normalise "A.1.2.1" / "A2.1.2" / "AHL A2.3.1" -> "A1.2.1"
def norm(c): return re.sub(r"^([A-D])\.", r"\1", c)

# Collect all statement codes per topic.
# Statement = letter + number + "." + number + "." + number(s) (e.g. A1.2.10)
stated = {}
for m in re.finditer(r"\[[AHL ]*([A-D]\.?\d\.\d\.\d+)", syl):
    c = norm(m.group(1))
    parts = c.split(".")
    topic = ".".join(parts[:2])          # A1.2
    stated.setdefault(topic, set()).add(c)

BASE = r"C:/Users/ASUS/Desktop/Hermes_Workspace/study-hub/topics/bio"
BUILT = {
 "a1.1-water":"A1.1","a1.2-nucleic-acids":"A1.2","a2.1-origins-of-cells":"A2.1",
 "a2.2-cell-structure":"A2.2","a2.3-viruses":"A2.3","a3.2-classification-cladistics":"A3.2",
 "a4.1-evolution-speciation":"A4.1","a4.2-conservation-biodiversity":"A4.2",
 "b1.1-carbohydrates-lipids":"B1.1","b1.2-proteins":"B1.2","b2.1-membranes":"B2.1",
}

def expand(text):
    """From an acttag like 'A1.2.11-15' or 'AHL · B2.1.14' or 'B3.1.7 · B3.1.17' return set of codes."""
    out = set()
    for m in re.finditer(r"([A-D]\.?\d\.\d\.\d+)(?:\s*[-–]\s*([A-D]\.?\d\.\d\.\d+))?", text):
        a = norm(m.group(1)); b = norm(m.group(2)) if m.group(2) else None
        if b:
            # expand range on last component
            ap = a.split("."); bp = b.split(".")
            for k in range(int(ap[-1]), int(bp[-1])+1):
                out.add(".".join(ap[:-1]) + "." + str(k))
        else:
            out.add(a)
    return out

all_ok = True
for d, topic in BUILT.items():
    f = os.path.join(BASE, d, "index.html")
    s = open(f, encoding="utf-8", errors="replace").read()
    tags = re.findall(r'<div class="acttag">(.*?)</div>', s, re.S)
    page_codes = set()
    for t in tags:
        page_codes |= expand(t)
    want = stated.get(topic, set())
    missing = sorted(w for w in want if w not in page_codes)
    print(f"== {topic} ==  syllabus_stmts={len(want):2d}  page_covers={len(page_codes):2d}")
    if missing:
        all_ok=False
        print(f"   MISSING on page: {missing}")
    else:
        print("   FULL COVERAGE ✓")
print("\nALL TOPICS FULLY COVERED:", all_ok)
