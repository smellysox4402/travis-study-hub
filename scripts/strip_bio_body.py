#!/usr/bin/env python
# Deep body/SVG/quiz metaphor strip for bio study-hub pages.
# Context-aware, EXACT-STRING replacements (assert count==1 per replacement so
# a mismatch fails loudly instead of silently mis-mapping biology). Only whole
# phrases are changed; no biological facts are altered, only the club/metaphor
# framing is replaced with direct factual language.
import re, os, sys

BASE = r"C:/Users/ASUS/Desktop/Hermes_Workspace/study-hub/topics/bio"

# page -> list of (old_exact_substring, new_exact_substring)
# old must appear EXACTLY once in the file (asserted); if it can appear more
# than once, use a fuller/phrase-form old string.
STRIP = {
"muscle-motility": [
  ("THE SARCOMERE — ONE DANCE FLOOR", "THE SARCOMERE"),
  ("READ THE DANCE FLOOR:", "READ THE SARCOMERE:"),
  ("<b>Think club:</b> the myosin heads are dancers doing a conga — each one grabs the rail (actin), hauls themselves along, lets go, sprints to the next rail.",
   "<b>How it works:</b> the myosin heads are like ratchets — each one binds actin, pulls itself along, lets go, and re-attaches to the next actin site."),
  ("One DJ controls a whole section of the crowd", "One motor neuron controls all the muscle fibres of a motor unit"),
  ("ONE MOTOR UNIT — ONE DJ, MANY DANCERS", "ONE MOTOR UNIT — ONE MOTOR NEURON, MANY FIBRES"),
  ("Fibres of different units intermingle so the club floor fills evenly.",
   "Fibres of different motor units are intermingled so contraction is even across the muscle."),
  ("Synovial joints — the VIP doors", "Synovial joints — the freely movable joints"),
  ("the hip is the club's best example", "the hip is the best example"),
  ("Job at the club", "Role"),
  ("THE HIP — BALL-AND-SOCKET VIP DOOR", "THE HIP — BALL-AND-SOCKET JOINT"),
  ("External vs internal — same club, opposite doors", "External vs internal — opposite surfaces"),
  ("THE DOLPHIN — WATERPROOF VIP", "THE DOLPHIN — ADAPTED FOR SWIMMING"),
  ("Follow the club layout from entrance to VIP lounge.", "Follow the way a muscle is organised, from a whole muscle to its fibres."),
  ("The myosin heads are the dancers — they bind actin", "The myosin heads bind actin"),
  ("You can't have a nightclub where nobody moves — but there are two very different door policies.",
   "There are two very different ways organisms move."),
  ("One neuron, many muscle fibres, all dancing on the same beat.",
   "One neuron, many muscle fibres, all contracting together."),
],
}

def apply(page):
    f = os.path.join(BASE, page, "index.html")
    s = open(f, encoding="utf-8", errors="replace").read()
    n = 0
    for old, new in STRIP[page]:
        c = s.count(old)
        if c == 0:
            continue            # already applied (idempotent)
        assert c == 1, f"{page}: '{old[:40]}...' occurs {c}x (expected 1)"
        s = s.replace(old, new); n += 1
    open(f, "w", encoding="utf-8", errors="replace").write(s)
    return n

for page in STRIP:
    print("OK", page, "replacements:", apply(page))
