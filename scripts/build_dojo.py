#!/usr/bin/env python3
"""
Build the Recall Dojo — the study-hub's diagram library turned into a
flip-card retrieval drill.

Reads assets/_audit/manifest.txt (the same manifest the audit scripts use),
checks every referenced diagram file exists, and generates
topics/recall-dojo/index.html with the manifest embedded so the page works
from file:// and GitHub Pages alike (no fetch, no CORS surprises).

Why: retrieval practice is the single highest-yield study technique
(Dunlosky et al. 2013). The hub already contains 147 neon diagrams; the
Dojo shows you the title, you reconstruct the picture in your head, then
reveal. Re-calling a diagram from a title is far stickier than re-reading
the page it lives on.

Usage:
  python scripts/build_dojo.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent
AUDIT = HUB / "assets" / "_audit"
OUT = HUB / "topics" / "recall-dojo" / "index.html"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="../../favicon.ico" sizes="32x32">
<title>The Recall Dojo — Travis's Study Hub</title>
<style>
  :root{
    --bg:#0b0214; --panel:#150a26; --panel2:#1d0f33; --ink:#f3e8ff; --dim:#b9a3d6;
    --pink:#ff2ec4; --violet:#a855f7; --cyan:#22d3ee; --gold:#fbbf24; --green:#4ade80;
    --red:#fb7185; --line:rgba(255,46,196,.28); --line2:rgba(168,85,247,.35);
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  body{background:var(--bg); color:var(--ink); font-family:'Segoe UI',system-ui,-apple-system,sans-serif; line-height:1.55;}
  ::selection{background:var(--pink); color:#0b0214;}
  .wrap{max-width:980px; margin:0 auto; padding:0 18px 80px;}

  header.hero{text-align:center; padding:54px 18px 24px;}
  .kicker{font-size:12px; letter-spacing:.35em; color:var(--cyan); text-transform:uppercase; font-weight:700;}
  h1{font-size:clamp(30px,5.5vw,52px); font-weight:900; line-height:1.05; margin:14px 0 6px;
     background:linear-gradient(90deg,var(--pink),var(--violet),var(--cyan));
     -webkit-background-clip:text; background-clip:text; color:transparent;
     text-shadow:0 0 42px rgba(255,46,196,.35);}
  .sub{color:var(--dim); font-size:15px; max-width:700px; margin:10px auto 0;}
  .sub b{color:var(--pink);}

  .stats{margin-top:20px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;}
  .stat{font-size:12.5px; font-weight:700; padding:7px 16px; border-radius:999px; border:1px solid var(--line2); color:var(--violet);}
  .stat b{color:var(--pink);}

  .filters{margin:26px auto 0; display:flex; gap:8px; justify-content:center; flex-wrap:wrap;}
  .pill{font-size:12.5px; font-weight:800; letter-spacing:.06em; padding:8px 18px; border-radius:999px; cursor:pointer;
        color:var(--dim); background:var(--panel); border:1px solid var(--line2); transition:all .18s; user-select:none;}
  .pill:hover{border-color:var(--cyan); color:var(--ink);}
  .pill.on{background:linear-gradient(90deg,rgba(255,46,196,.25),rgba(168,85,247,.25)); border-color:var(--pink); color:#fff; box-shadow:0 0 16px rgba(255,46,196,.25);}

  .stage{margin-top:28px; background:var(--panel); border:1px solid var(--line); border-radius:20px; padding:26px; min-height:300px;
         display:flex; flex-direction:column; align-items:center; justify-content:center; gap:18px; text-align:center; position:relative;}
  .stage .idx{position:absolute; top:14px; right:18px; font-size:11px; letter-spacing:.12em; color:var(--dim); opacity:.6;}
  #cardTitle{font-size:clamp(19px,3.4vw,30px); font-weight:900; line-height:1.25; color:var(--ink);
     text-shadow:0 0 24px rgba(255,46,196,.25); max-width:760px;}
  #cardTitle .tag{display:block; font-size:11px; letter-spacing:.3em; color:var(--cyan); font-weight:800; margin-bottom:10px; text-transform:uppercase;}
  #cardHint{color:var(--dim); font-size:13.5px; max-width:600px;}
  .btns{display:flex; gap:10px; flex-wrap:wrap; justify-content:center;}
  .btn{font-size:13.5px; font-weight:800; letter-spacing:.07em; padding:12px 26px; border-radius:999px; cursor:pointer; border:1px solid var(--line2);
       color:var(--ink); background:var(--panel2); transition:all .18s; user-select:none;}
  .btn:hover{transform:translateY(-1px);}
  .btn.primary{border-color:var(--pink); color:#fff; background:linear-gradient(90deg,rgba(255,46,196,.28),rgba(168,85,247,.28)); box-shadow:0 0 18px rgba(255,46,196,.22);}
  .btn.primary:hover{box-shadow:0 0 30px rgba(255,46,196,.45);}
  .btn.green{border-color:var(--green); color:#fff; background:rgba(74,222,128,.12);}
  .btn.red{border-color:var(--red); color:#fff; background:rgba(251,113,133,.12);}
  .btn:disabled{opacity:.35; cursor:not-allowed; transform:none; box-shadow:none;}

  #diagramFrame{width:100%; height:430px; border:1px solid var(--line2); border-radius:14px; background:var(--panel);
     box-shadow:0 0 26px rgba(34,211,238,.10); display:none;}
  #diagramFrame.show{display:block; animation:fadeIn .25s ease-out;}
  @keyframes fadeIn{from{opacity:0; transform:translateY(6px)} to{opacity:1; transform:none}}

  .how{margin-top:30px; background:var(--panel); border:1px solid var(--line); border-radius:18px; padding:20px 22px;}
  .how h3{font-size:15px; font-weight:800; margin-bottom:8px; color:var(--cyan);}
  .how p{color:var(--dim); font-size:13.5px;}
  .how b{color:var(--pink);}

  footer{margin-top:30px; padding-top:16px; border-top:1px solid var(--line); color:var(--dim); font-size:12.5px; text-align:center;}
  .home-btn{position:fixed; left:16px; bottom:16px; z-index:950; display:inline-flex; align-items:center; gap:8px;
    padding:10px 18px; border-radius:999px; font-size:13px; font-weight:800; letter-spacing:.06em; text-decoration:none;
    color:var(--cyan); background:rgba(21,10,38,.88); border:1px solid rgba(34,211,238,.55);
    box-shadow:0 0 18px rgba(34,211,238,.28), inset 0 0 12px rgba(34,211,238,.08);
    backdrop-filter:blur(4px); transition:all .2s;}
  .home-btn:hover{background:var(--cyan); color:#0b0214; box-shadow:0 0 28px rgba(34,211,238,.65); transform:translateY(-2px);}
</style>
</head>
<body>

<a class="home-btn" href="../../index.html">🏠 HOME</a>

<div class="wrap">

<header class="hero">
  <div class="kicker">Recall mode · retrieval practice</div>
  <h1>THE RECALL DOJO</h1>
  <div class="sub">Every diagram on the hub, filed by title. You see the name, you rebuild the picture in your head, then you reveal. <b>Recalling beats re-reading</b> — this is the diagram library turned into a drill.</div>
  <div class="stats">
    <span class="stat">🗂 <b id="stTotal">0</b> diagrams loaded</span>
    <span class="stat">🎯 <b id="stAcc">—</b> lifetime recall accuracy</span>
    <span class="stat">🔥 <b id="stToday">0</b> recalls today</span>
  </div>
  <div class="filters" id="filters"></div>
</header>

<div class="stage" id="stage">
  <div class="idx" id="stageIdx"></div>
  <div id="cardTitle"></div>
  <div id="cardHint"></div>
  <div class="btns" id="stageBtns"></div>
  <iframe id="diagramFrame" title="diagram" loading="lazy"></iframe>
</div>

<div class="how">
  <h3>HOW TO TRAIN</h3>
  <p><b>1.</b> Read the title out loud. <b>2.</b> Reconstruct the diagram in your head — labels, arrows, colours, the story. <b>3.</b> Hit reveal and compare. <b>4.</b> Nailed it or missed it, then next. One full pass through the library = one dojo run. Come back tomorrow and the shuffle resets.</p>
</div>

<footer>
  <p>The Recall Dojo · part of <a href="../../index.html" style="color:var(--cyan)">Travis's Study Hub</a> · generated by scripts/build_dojo.py</p>
</footer>

</div>

<script>
/* ---- embedded manifest (regenerated by scripts/build_dojo.py) ---- */
var DOJO = __MANIFEST__;

/* ---- state ---- */
var SUBJECTS = {};
DOJO.forEach(function(e){ SUBJECTS[e.subject] = (SUBJECTS[e.subject]||0)+1; });
var SUBJECT_NAMES = {bio:"Biology", chem:"Chemistry", business:"Business", chinese:"Chinese", other:"Other"};
var filter = "all";
var queue = [];
var seenThisPass = {};
var current = null;
var revealed = false;

var STORE_KEY = "dojoStats_v1";
var stats = {correct:0, wrong:0, today:"", todayCount:0, seen:[]};
try{
  var saved = JSON.parse(localStorage.getItem(STORE_KEY)||"{}");
  if(saved && typeof saved==="object") stats = Object.assign(stats, saved);
}catch(e){}
var todayStr = new Date().toISOString().slice(0,10);
if(stats.today !== todayStr){ stats.today = todayStr; stats.todayCount = 0; }

/* ---- ui refs ---- */
var $ = function(id){ return document.getElementById(id); };
var stage = $("stage"), cardTitle = $("cardTitle"), cardHint = $("cardHint"), stageBtns = $("stageBtns"), frame = $("diagramFrame");

/* ---- filters ---- */
var filterBox = $("filters");
function buildFilters(){
  var names = ["all"].concat(Object.keys(SUBJECTS));
  filterBox.innerHTML = "";
  names.forEach(function(s){
    var label = s==="all" ? "ALL SUBJECTS" : (SUBJECT_NAMES[s]||s).toUpperCase();
    var b = document.createElement("div");
    b.className = "pill" + (s===filter ? " on" : "");
    b.textContent = label + " (" + (s==="all" ? DOJO.length : SUBJECTS[s]) + ")";
    b.onclick = function(){ filter = s; document.querySelectorAll(".pill").forEach(function(p){p.classList.remove("on");}); b.classList.add("on"); startPass(); };
    filterBox.appendChild(b);
  });
}

/* ---- drill ---- */
function pool(){
  return DOJO.filter(function(e){ return filter==="all" || e.subject===filter; });
}
function startPass(){
  queue = shuffle(pool().filter(function(e){ return !seenThisPass[e.id]; }));
  if(queue.length===0){ seenThisPass = {}; queue = shuffle(pool()); }
  stats.seen = stats.seen.slice(-400);
  nextCard();
}
function shuffle(a){
  for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; }
  return a;
}
function nextCard(){
  if(queue.length===0){ queue = shuffle(pool().filter(function(e){ return !seenThisPass[e.id]; })); }
  if(queue.length===0){ seenThisPass = {}; queue = shuffle(pool()); }
  current = queue.pop();
  seenThisPass[current.id] = true;
  revealed = false;
  frame.classList.remove("show");
  frame.removeAttribute("src");
  cardTitle.innerHTML = '<span class="tag">' + (SUBJECT_NAMES[current.subject]||current.subject).toUpperCase() + " · DRAW IT IN YOUR HEAD</span>" + esc(current.title);
  cardHint.textContent = "Reconstruct the diagram from memory, then reveal.";
  stageBtns.innerHTML = '<div class="btn primary" id="bReveal">REVEAL DIAGRAM</div>';
  $("bReveal").onclick = reveal;
  $("stageIdx").textContent = (pool().length - queue.length - 1) + " / " + pool().length;
  renderStats();
}
function reveal(){
  revealed = true;
  frame.src = "../../assets/_audit/" + current.file;
  frame.classList.add("show");
  stageBtns.innerHTML =
    '<div class="btn green" id="bNail">NAILED IT</div>' +
    '<div class="btn red" id="bMiss">MISSED IT</div>' +
    '<div class="btn" id="bNext">NEXT →</div>';
  $("bNail").onclick = function(){ grade(true); };
  $("bMiss").onclick = function(){ grade(false); };
  $("bNext").onclick = nextCard;
  cardHint.textContent = "Compare. Then grade yourself honestly.";
}
function grade(gotIt){
  if(gotIt) stats.correct++; else stats.wrong++;
  stats.todayCount++;
  save();
  renderStats();
  nextCard();
}
function esc(s){ return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function save(){ try{ localStorage.setItem(STORE_KEY, JSON.stringify(stats)); }catch(e){} }
function renderStats(){
  $("stTotal").textContent = DOJO.length;
  var total = stats.correct + stats.wrong;
  $("stAcc").textContent = total ? Math.round(100*stats.correct/total) + "% (" + stats.correct + "/" + total + ")" : "—";
  $("stToday").textContent = stats.todayCount;
}

/* ---- go ---- */
buildFilters();
renderStats();
startPass();
</script>
</body>
</html>
"""


def main() -> int:
    lines = (AUDIT / "manifest.txt").read_text(encoding="utf-8").splitlines()
    entries = []
    for line in lines:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 5:
            continue
        src, idx, title, desc, fname = parts[0], parts[1], parts[2], parts[3], parts[4]
        m = re.match(r"topics/([^/]+)/", src)
        subject = m.group(1) if m else "other"
        entries.append({
            "id": f"{subject}__{idx}__{fname}",
            "subject": subject,
            "title": title.strip(),
            "desc": desc.strip(),
            "file": fname,
        })

    missing = [e for e in entries if not (AUDIT / e["file"]).exists()]
    if missing:
        print(f"ERROR: {len(missing)} manifest files missing, aborting", file=sys.stderr)
        for e in missing:
            print("  ", e["file"], file=sys.stderr)
        return 1

    manifest_json = json.dumps(entries, ensure_ascii=False, separators=(",", ":"))
    html = PAGE.replace("__MANIFEST__", manifest_json)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"built {OUT} ({len(entries)} diagrams, {html.count(chr(10))} lines, {len(html.encode('utf-8'))/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
