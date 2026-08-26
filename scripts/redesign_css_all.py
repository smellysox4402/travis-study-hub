#!/usr/bin/env python3
"""Apply the dark-airy CSS transformation to every remaining study-hub page
(bio, business, chinese, math, recall-dojo). Tolerant: reports MISSING/AMBIG
per page so variant CSS (c2.2, gas-exchange) can be handled separately.
"""
import os, re, sys

ROOT = r"C:\Users\ASUS\Desktop\Hermes_Workspace\study-hub\topics"

CSS = [
    ("body{background:var(--bg); color:var(--ink); font-family:'Segoe UI',system-ui,-apple-system,sans-serif; line-height:1.55;}",
     "body{background:var(--bg); color:var(--ink); font-family:'Segoe UI',system-ui,-apple-system,sans-serif; line-height:1.7;}"),
    ("nav a{color:var(--dim); text-decoration:none; font-size:12px; font-weight:600; letter-spacing:.04em;",
     "nav a{color:var(--dim); text-decoration:none; font-size:13px; font-weight:600; letter-spacing:.04em;"),
    ("h1{font-size:clamp(34px,6vw,58px); font-weight:900; line-height:1.05; margin:14px 0 6px;\n     background:linear-gradient(90deg,var(--pink),var(--violet),var(--cyan));\n     -webkit-background-clip:text; background-clip:text; color:transparent;\n     text-shadow:0 0 42px rgba(255,46,196,.35);}",
     "h1{font-size:clamp(30px,5vw,44px); font-weight:800; line-height:1.1; margin:14px 0 8px; color:#fff; letter-spacing:-.02em;}"),
    (".sub{color:var(--dim); font-size:16px; max-width:680px; margin:10px auto 0;}",
     ".sub{color:var(--dim); font-size:17px; max-width:680px; margin:10px auto 0;}"),
    (".act h2{font-size:clamp(24px,4vw,34px); font-weight:900; margin:6px 0 4px;\n          background:linear-gradient(90deg,var(--pink),var(--violet));\n          -webkit-background-clip:text; background-clip:text; color:transparent;}",
     ".act h2{font-size:clamp(24px,4vw,30px); font-weight:750; margin:6px 0 12px; color:#fff; letter-spacing:-.01em;}"),
    (".act .aim{color:var(--dim); font-size:14px; margin-bottom:18px; max-width:720px;}",
     ".act .aim{color:var(--dim); font-size:15.5px; margin-bottom:22px; max-width:720px;}"),
    (".panel{background:var(--panel); border:1px solid var(--line); border-radius:18px; padding:20px 22px; margin:16px 0;\n         box-shadow:0 0 30px rgba(168,85,247,.08);}",
     ".panel{background:var(--panel); border:1px solid var(--line); border-radius:16px; padding:24px 26px; margin:20px 0;}"),
    (".panel h3{font-size:17px; font-weight:800; margin-bottom:10px; color:#fff;}",
     ".panel h3{font-size:18px; font-weight:750; margin-bottom:10px; color:#fff;}"),
    (".panel p{margin:8px 0; color:var(--ink); font-size:15px;}",
     ".panel p{margin:10px 0; color:var(--ink); font-size:16px;}"),
    (".panel .big{font-size:16.5px;}",
     ".panel .big{font-size:17.5px;}"),
    (".muted{color:var(--dim); font-size:13.5px;}",
     ".muted{color:var(--dim); font-size:14px;}"),
    ("ul.clean li{padding:7px 0 7px 26px; position:relative; font-size:15px;}",
     "ul.clean li{padding:9px 0 9px 26px; position:relative; font-size:16px;}"),
    ("ol.steps li{counter-increment:s; padding:7px 0 7px 40px; position:relative; font-size:15px;}",
     "ol.steps li{counter-increment:s; padding:9px 0 9px 40px; position:relative; font-size:16px;}"),
    ("table{width:100%; border-collapse:collapse; margin:12px 0; font-size:14px;}",
     "table{width:100%; border-collapse:collapse; margin:16px 0; font-size:15px; line-height:1.6;}"),
    ("th{background:linear-gradient(90deg,rgba(255,46,196,.18),rgba(168,85,247,.18)); color:#fff; text-align:left;\n     padding:10px 12px; font-size:12.5px; letter-spacing:.06em; text-transform:uppercase;}",
     "th{background:rgba(168,85,247,.16); color:#fff; text-align:left;\n     padding:13px 16px; font-size:12.5px; letter-spacing:.04em; text-transform:uppercase; border-bottom:2px solid var(--line2);}"),
    ("td{padding:10px 12px; border-top:1px solid rgba(168,85,247,.2); vertical-align:top;}",
     "td{padding:14px 16px; border-bottom:1px solid var(--line); vertical-align:top;}"),
    ("td:first-child{font-weight:700; color:var(--pink); white-space:nowrap;}",
     "td:first-child{font-weight:600; color:#fff; white-space:nowrap;}"),
    ("tr:hover td{background:rgba(168,85,247,.06);}",
     "tr:hover td{background:rgba(168,85,247,.06);}\n  tr:nth-child(even) td{background:rgba(255,255,255,.03);}"),
    (".card p{font-size:14px; color:var(--ink); margin:5px 0;}",
     ".card p{font-size:15px; color:var(--ink); margin:6px 0;}"),
    (".bouncer{display:flex; gap:18px; background:var(--panel); border:1px solid var(--line); border-radius:18px;\n           padding:20px; margin:16px 0; box-shadow:0 0 30px rgba(168,85,247,.08);}",
     ".bouncer{display:flex; gap:18px; background:var(--panel); border:1px solid var(--line); border-radius:16px;\n           padding:20px; margin:16px 0;}"),
    (".bouncer p, .bouncer li{font-size:14.5px;}",
     ".bouncer p, .bouncer li{font-size:15.5px;}"),
    ("border-radius:12px; margin:8px 0; cursor:pointer; transition:.15s; font-size:14px;}",
     "border-radius:12px; margin:8px 0; cursor:pointer; transition:.15s; font-size:15px;}"),
    (".q label{display:block; padding:7px 12px; margin:4px 0; border-radius:10px; cursor:pointer; font-size:14px;",
     ".q label{display:block; padding:8px 12px; margin:4px 0; border-radius:10px; cursor:pointer; font-size:15px;"),
    (".node{background:var(--panel2); border:1px solid var(--line2); border-radius:12px; padding:10px 14px; font-size:13.5px; font-weight:600;}",
     ".node{background:var(--panel2); border:1px solid var(--line2); border-radius:12px; padding:10px 14px; font-size:14px; font-weight:600;}"),
    (".fig .cap{font-size:12px; color:var(--dim); margin-top:10px; line-height:1.5;}",
     ".fig .cap{font-size:13.5px; color:var(--dim); margin-top:12px; line-height:1.6;}"),
]

def transform(page_dir):
    path = os.path.join(ROOT, page_dir, "index.html")
    if not os.path.exists(path):
        return None
    s = open(path, encoding="utf-8").read()
    miss = 0
    for o, n in CSS:
        c = s.count(o)
        if c == 1:
            s = s.replace(o, n, 1)
        elif c == 0:
            miss += 1
    open(path, "w", encoding="utf-8").write(s)
    return miss

if __name__ == "__main__":
    pages = []
    for subj in ["bio", "business", "chinese", "math", "recall-dojo"]:
        d = os.path.join(ROOT, subj)
        if os.path.isdir(d):
            for name in sorted(os.listdir(d)):
                if os.path.isfile(os.path.join(d, name, "index.html")):
                    pages.append(f"{subj}/{name}")
    for p in pages:
        m = transform(p)
        if m is None:
            print(f"{p}: NO FILE")
        elif m:
            print(f"{p}: {m} CSS misses")
        else:
            print(f"{p}: OK")
