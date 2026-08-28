#!/usr/bin/env python
# Redesign bio study-hub pages: strip the nightclub/kitchen/stage narrative.
# Data-driven per-page rewrite. All edits are computed against the ORIGINAL
# index space and applied in DESCENDING order so indices never go stale.
import re, os

BASE = r"C:/Users/ASUS/Desktop/Hermes_Workspace/study-hub/topics/bio"

PLAN = {
"transport": {
  "title": "B3.2 Transport — Blood & Plant Conduction",
  "h1": "B3.2 TRANSPORT",
  "sub": "How the circulatory system moves blood, the role of blood in transport, and how plants move water (xylem) and sugar (phloem).",
  "headings": [
    "BLOOD — A TRANSPORT MEDIUM","ARTERIES, VEINS &amp; CAPILLARIES","WALL STRUCTURES &amp; BLOOD PRESSURE",
    "THE CARDIAC CYCLE &amp; PULSE","VALVES ENSURE ONE-WAY FLOW","BLOOD VESSEL DISEASE",
    "FLUID &amp; WATER TRANSPORT IN PLANTS","WATER &amp; MINERAL UPTAKE BY ROOTS","ACTIVE TRANSPORT &amp; TISSUE FLUID",
    "TISSUE FLUID, LYMPH &amp; DRAINAGE","THE HEART &amp; CARDIAC MUSCLE","PHLOEM TRANSPORT &amp; LOADING",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {"THE VIP CORRIDORS":"BLOOD VESSELS","THE CORRIDOR CODES":"ARTERIES · VEINS · CAPILLARIES",
    "THE PRESSURE PIPE":"BLOOD PRESSURE","THE BEAT COUNTER":"CARDIAC CYCLE","THE ONE-WAY DOOR":"VALVES",
    "THE BLOCKED BACKSTAGE":"BLOOD VESSEL DISEASE","THE WATER PIPE NETWORK":"XYLEM","THE PIPE FITTERS":"ROOT UPTAKE",
    "THE FLOOR PLANS":"TISSUE FLUID","THE TISSUE-FLUID TAP":"LYMPH &amp; DRAINAGE","THE DJ'S DECK":"THE HEART",
    "THE VIP ESCALATOR":"PHLOEM"},
},
"respiration": {
  "title": "C1.2 Cell Respiration",
  "h1": "C1.2 CELL RESPIRATION",
  "sub": "How cells release energy from organic molecules, and the four stages of aerobic respiration plus the anaerobic pathways.",
  "headings": [
    "THE ENERGY CURRENCY — ATP","ATP AT WORK IN CELLS","ATP TURNOVER &amp; RECYCLING",
    "RESPIRATION: INTRODUCING THE STAGES","AEROBIC VS ANAEROBIC","MEASURING RESPIRATION RATE",
    "GLYCOLYSIS","STRUCTURE OF THE MITOCHONDRION","THE LINK REACTION &amp; KREBS CYCLE","THE KREBS CYCLE — FULL DETAIL",
    "THE ELECTRON TRANSPORT CHAIN","OXIDATIVE PHOSPHORYLATION","ANAEROBIC PATHWAYS IN MUSCLE","LACTATE FERMENTATION",
    "THE RESPIRATORY SUBSTRATES","THE DELIVERY DOCK — ACETYL COA","RESPIRATION &amp; ENERGY YIELD",
    "LIPIDS VS CARBOHYDRATES AS FUEL",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {},
},
"photosynthesis": {
  "title": "C1.3 Photosynthesis",
  "h1": "C1.3 PHOTOSYNTHESIS",
  "sub": "How light energy is converted into chemical energy: chlorophyll and the light-dependent reactions in the thylakoids, and the Calvin cycle in the stroma.",
  "headings": [
    "PHOTOSYNTHESIS &amp; THE CHLOROPLAST","THE OXYGEN VENT — O₂ RELEASED","CHLOROPHYLL &amp; OTHER PIGMENTS",
    "THE COLOUR OF LIGHT &amp; PHOTOSYNTHESIS","ABSORPTION VS ACTION SPECTRA","RATE/LIMITING FACTORS","THE CO₂ &amp; O₂ BALANCE",
    "THE LIGHT-DEPENDENT REACTIONS","PHOTOSYSTEMS &amp; ELECTRON TRANSPORT","PROTON GRADIENTS &amp; ATP SYNTHASE",
    "THE CALVIN CYCLE","THE CALVIN CYCLE — CARBON FIXATION","FACTORS CARBON &amp; ENERGY USE",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {},
},
"reproduction": {
  "title": "D3.1 Reproduction",
  "h1": "D3.1 REPRODUCTION",
  "sub": "Asexual vs sexual reproduction, the male and female reproductive systems, gamete production, fertilisation, pregnancy and birth control.",
  "headings": [
    "ASEXUAL VS SEXUAL REPRODUCTION","SEXUAL REPRODUCTION &amp; VARIATION","THE MALE REPRODUCTIVE SYSTEM","MALE HORMONE CONTROL",
    "THE FEMALE REPRODUCTIVE SYSTEM","THE MENSTRUAL CYCLE","GAMETES &amp; FERTILISATION","IVF — IN VITRO FERTILISATION",
    "FERTILISATION — SITE &amp; PROCESS","SPERM TRANSPORT &amp; CAPACITATION","HORMONES OF PREGNANCY",
    "SPERMATOGENESIS VS OOGENESIS","AIDS/HIV &amp; SEXUAL HEALTH","PREGNANCY &amp; IMPLANTATION","THE PLACENTA","LABOUR &amp; BIRTH",
    "HORMONAL CONTRACEPTION","CHILD &amp; MATERNAL HEALTH",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {},
},
"muscle-motility": {
  "title": "B3.3 Muscle &amp; Motility",
  "h1": "B3.3 MUSCLE &amp; MOTILITY",
  "sub": "The sliding-filament mechanism of muscle contraction, motor units, bones and joints, and locomotion across animals.",
  "headings": [
    "MUSCLE CONTRACTION &amp; THE SARCOMERE","THE SLIDING-FILAMENT MECHANISM","MOTOR UNITS &amp; NEUROMUSCULAR JUNCTIONS",
    "BONES, JOINTS &amp; THE SKELETON","INTERCOSTAL MUSCLES &amp; VENTILATION","LOCOMOTION &amp; WHY WE MOVE",
    "SWIMMING IN DOLPHINS &amp; AQUATIC LIFE",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {},
},
"cell-division": {
  "title": "D2.1 Cell &amp; Nuclear Division",
  "h1": "D2.1 CELL &amp; NUCLEAR DIVISION",
  "sub": "How cells replicate and divide by mitosis and meiosis, chromosome structure, cytokinesis, the cell cycle and how errors cause cancer.",
  "headings": [
    "WHY NEW CELLS ARE MADE","CYTOKINESIS","MITOSIS &amp; MEIOSIS — TWO ROLES","CHROMOSOME STRUCTURE","MITOSIS — THE PMAT STAGES",
    "MEIOSIS — GENERATING VARIATION","NON-DISJUNCTION","THE CELL CYCLE","CELL CYCLE CONTROL &amp; CANCER",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {"NEW CELLS":"NEW CELLS","CYTOKINESIS":"CYTOKINESIS","MITOSIS &amp; MEIOSIS":"MITOSIS &amp; MEIOSIS",
    "CHROMOSOMES":"CHROMOSOMES","MITOSIS":"MITOSIS","MEIOSIS":"MEIOSIS","NON-DISJUNCTION":"NON-DISJUNCTION",
    "CELL CYCLE":"CELL CYCLE","CONTROL":"CONTROL","CANCER":"CANCER"},
},
"enzymes": {
  "title": "C1.1 Enzymes &amp; Metabolism",
  "h1": "C1.1 ENZYMES &amp; METABOLISM",
  "sub": "Enzymes as biological catalysts: specificity, active sites, induced fit, activation energy, factors affecting rate, and inhibition.",
  "headings": [
    "ENZYMES AS CATALYSTS","ROLE OF ENZYMES IN METABOLISM","ANABOLIC &amp; CATABOLIC REACTIONS",
    "ENZYMES: GLOBULAR PROTEINS WITH AN ACTIVE SITE","SUBSTRATE-ACTIVE SITE BINDING (INDUCED FIT)",
    "MOLECULAR MOTION &amp; COLLISIONS","SPECIFICITY, STRUCTURE &amp; DENATURATION","FACTORS AFFECTING ENZYME ACTIVITY",
    "MEASURING ENZYME-CATALYSED REACTIONS","LOWERING ACTIVATION ENERGY",
    "INTRACELLULAR VS EXTRACELLULAR ENZYME REACTIONS","HEAT GENERATION BY METABOLISM",
    "CYCLICAL &amp; LINEAR METABOLIC PATHWAYS","ALLOSTERIC SITES &amp; NON-COMPETITIVE INHIBITION",
    "COMPETITIVE INHIBITION","FEEDBACK INHIBITION &amp; END PRODUCTS","MECHANISM-BASED INHIBITION",
    "ENZYMES — FULL REVISION",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {},
},
"gas-exchange": {
  "title": "B3.1 Gas Exchange",
  "h1": "B3.1 GAS EXCHANGE",
  "sub": "How oxygen reaches cells and carbon dioxide leaves them: the properties of exchange surfaces, mammalian lungs, ventilation, and gas exchange in leaves.",
  "headings": [
    "GAS EXCHANGE AS A VITAL FUNCTION","PROPERTIES OF EXCHANGE SURFACES","MAINTAINING CONCENTRATION GRADIENTS",
    "ADAPTATIONS OF MAMMALIAN LUNGS","VENTILATION OF THE LUNGS","MEASURING LUNG VOLUMES",
    "GAS EXCHANGE IN LEAVES &amp; TISSUES","TRANSPIRATION &amp; GAS EXCHANGE","STOMATAL DENSITY",
    "OXYGEN TRANSPORT &amp; DELIVERY",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {},
},
"homeostasis": {
  "title": "D3.3 Homeostasis",
  "h1": "D3.3 HOMEOSTASIS",
  "sub": "How the body maintains a stable internal environment through negative-feedback mechanisms controlling glucose, temperature, water and blood pressure.",
  "headings": [
    "SET POINTS &amp; STABLE INTERNAL ENVIRONMENT","NEGATIVE FEEDBACK LOOPS","GLUCOSE REGULATION","DIABETES &amp; BLOOD GLUCOSE",
    "THERMOREGULATION — THE HYPOTHALAMUS","HEAT GAIN &amp; LOSS","THE KIDNEY &amp; OSMOREGULATION","THE NEPHRON FILTER",
    "SALT &amp; WATER REABSORPTION","ADH &amp; WATER BALANCE","BLOOD PRESSURE &amp; ITS CONTROL",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {"SET POINTS":"SET POINTS","NEGATIVE FEEDBACK":"NEGATIVE FEEDBACK","GLUCOSE":"GLUCOSE","DIABETES":"DIABETES",
    "TEMPERATURE":"TEMPERATURE","HEAT CONTROL":"HEAT CONTROL","KIDNEY":"KIDNEY","FILTER":"FILTER",
    "SALT LADDER":"SALT &amp; WATER","WATER BOSS":"ADH &amp; WATER","BLOOD ROUTER":"BLOOD PRESSURE",
    "POSITIVE FEEDBACK":"POSITIVE FEEDBACK"},
},
"inheritance": {
  "title": "D3.2 Inheritance",
  "h1": "D3.2 INHERITANCE",
  "sub": "How genes and alleles are passed on, Mendelian genetics and Punnett grids, monohybrid and dihybrid crosses, sex linkage, pedigrees and the chi-squared test.",
  "headings": [
    "GAMETES &amp; ZYGOTES — THE TRANSMISSION OF GENES","MENDEL'S EXPERIMENTS &amp; LAWS","ALLELES, GENOTYPES &amp; PHENOTYPES",
    "DOMINANT &amp; RECESSIVE ALLELES","PUNNETT GRIDS &amp; MONOHYBRID CROSSES","MULTIPLE ALLELES — THE ABO BLOOD GROUP",
    "SEX CHROMOSOMES &amp; THE X-FACTOR","SEX LINKAGE","THE DIHYBRID PUNNETT GRID","VARIATION &amp; PLASTICITY",
    "LINKAGE &amp; THE CHI-SQUARED TEST",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {"GAMETES":"GAMETES","ZYGOTE":"ZYGOTE","ALLELES":"ALLELES","GENOTYPE":"GENOTYPE","PHENOTYPE":"PHENOTYPE",
    "DOMINANT / RECESSIVE":"DOMINANT / RECESSIVE","PLASTICITY":"PLASTICITY","MULTIPLE ALLELES":"MULTIPLE ALLELES",
    "CODOMINANCE":"CODOMINANCE","SEX LINKAGE":"SEX LINKAGE","PEDIGREES":"PEDIGREES","DIHYBRID":"DIHYBRID",
    "VARIATION":"VARIATION","LINKAGE + χ²":"LINKAGE + χ²"},
},
"integration": {
  "title": "C3.1 Integration of Body Systems",
  "h1": "C3.1 INTEGRATION OF BODY SYSTEMS",
  "sub": "How the brain, nervous system, endocrine system and blood co-ordinate the body's responses and homeostasis across body systems.",
  "headings": [
    "THE INTEGRATION HIERARCHY","THE THREE CHANNELS — NERVE &amp; HORMONE","THE BRAIN &amp; NERVOUS SYSTEM","THE ENDOCRINE GLANDS",
    "SENSORY INPUT &amp; MOTOR OUTPUT","THE SPINAL CORD &amp; REFLEXES","THE PAIN PATHWAY","THE CEREBELLUM &amp; MOVEMENT",
    "CIRCADIAN RHYTHMS","EPINEPHRINE &amp; THE FIGHT-OR-FLIGHT","THE HYPOTHALAMUS &amp; PITUITARY","AUTONOMIC OUTPUT &amp; HOMEOSTASIS",
    "PLANT RESPONSES &amp; PHYTOHORMONES",
  ],
  "sectitles": {"mind":"🗺 MIND MAP","cheat":"⚡ CHEAT","test":"✍ SELF-TEST","check":"✅ CHECKLIST"},
  "nodes": {"HIERARCHY":"HIERARCHY","THREE CHANNELS":"THREE CHANNELS","THE DJ BOOTH":"THE BRAIN",
    "BRAIN = DJ BOOTH":"THE BRAIN","SPINAL CORD":"SPINAL CORD","SENSORY IN / MOTOR OUT":"SENSORY IN / MOTOR OUT",
    "NERVES = CABLE BUNDLES":"NERVE BUNDLES","PAIN EXPRESS":"THE PAIN PATHWAY","CEREBELLUM":"CEREBELLUM",
    "CIRCADIAN RHYTHM":"CIRCADIAN RHYTHM","EPINEPHRINE":"EPINEPHRINE","THE CONDUCTOR'S DESK":"THE CONDUCTOR",
    "HYPOTHALAMUS + PITUITARY":"HYPOTHALAMUS + PITUITARY","AUTO-PILOTS":"AUTONOMIC OUTPUT"},
},
}

CLUB = re.compile(r"(bouncer|crowd|VIP|dance ?floor|dancers?|DJ|kitchen|nightclub|turnstile|scoreboard|compass|ledger|"
                  r"guest ?list|tracklist|sound ?system|\bclub\b|encore|concert|\bstage\b|backstage|conductor|booth|"
                  r"power ?plant|valet|brewery|remix|velvet rope|vibe|party|setlist|playlist|head chef|assembly line|venue)", re.I)

def short_name(h):
    # nav label: take the part before ' — ' (or ':' ) and cap at ~18 chars
    t = h.split(' — ')[0]
    t = re.sub(r'&amp;','&', t)
    # strip trailing subtitle after ':' too
    t = t.split(' : ')[0]
    if len(t) > 20: t = t[:20].rstrip(' &') 
    return t

def do(page):
    f = os.path.join(BASE, page, "index.html")
    s = open(f, encoding="utf-8", errors="replace").read()
    p = PLAN[page]
    n = len(p["headings"])
    edits = []

    # --- title/h1 ---
    m = re.search(r"<title>(.*?)</title>", s, re.S); assert m, f"{page}: title"
    edits.append((m.start()+7, m.end()-8, p["title"]))
    m = re.search(r"<h1>(.*?)</h1>", s, re.S); assert m, f"{page}: h1"
    edits.append((m.start()+4, m.end()-5, p["h1"]))

    # --- h2s: classify by CLEAN tab patterns, content sections in order ---
    h2s = list(re.finditer(r"<h2([^>]*)>(.*?)</h2>", s, re.S))
    ci = 0
    for m in h2s:
        vis = re.sub(r"\s+"," ", re.sub(r"<[^>]+>","", m.group(2))).strip().upper()
        if "MIND MAP" in vis: new = p["sectitles"]["mind"]
        elif "CHEAT" in vis: new = p["sectitles"]["cheat"]
        elif "TEST" in vis or "QUIZ" in vis: new = p["sectitles"]["test"]
        elif "CHECKLIST" in vis: new = p["sectitles"]["check"]
        else:
            # content section
            assert ci < len(p["headings"]), f"{page}: too many content h2s"
            new = p["headings"][ci]; ci += 1
        oi = m.start()+len("<h2"+m.group(1)+">"); ci_end = m.end()-5
        edits.append((oi, ci_end, new))
    assert ci == len(p["headings"]), f"{page}: content h2s={ci} vs headings={len(p['headings'])}"

    # --- nav labels (use group offsets so the closing </a> is preserved) ---
    nm = re.search(r"<nav.*?</nav>", s, re.S)
    if nm:
        nav = nm.group(0)
        for am in re.finditer(r'<a href="(#[^"]+)"([^>]*)>([^<]+)</a>', nav):
            href = am.group(1); label = am.group(3)
            mm = re.match(r"#act(\d+)$", href)
            if mm:
                idx = int(mm.group(1))-1
                if 0 <= idx < n:
                    newl = f"{idx+1} · {short_name(p['headings'][idx])}"
                else:
                    newl = label
            elif href == "#map": newl = p["sectitles"]["mind"]
            elif href == "#cheat": newl = p["sectitles"]["cheat"]
            elif href == "#test": newl = p["sectitles"]["test"]
            elif href == "#check": newl = p["sectitles"]["check"]
            else: continue
            gs = nm.start() + am.start(3)
            ge = nm.start() + am.end(3)
            edits.append((gs, ge, newl))

    # --- acttags: drop "Act N ·"; neutralize tab-section acttags ---
    CODE = re.compile(r"[A-D]\d\.\d")
    for m in re.finditer(r'<div class="acttag">(.*?)</div>', s, re.S):
        body = m.group(1)
        newb = re.sub(r"^\s*(ACT|Act)?\s*\d+\s*[·\-–—]\s*", "", body)
        vis_tag = re.sub(r"<[^>]+>","", newb).strip()
        if not CODE.search(vis_tag):
            t = vis_tag.lower()
            if "map" in t or "overview" in t or "one-page" in t or "whole" in t:
                newb = "One-page overview"
            elif "recap" in t or "60" in t:
                newb = "Quick recap"
            elif "check" in t or "quiz" in t or "practice" in t or "test" in t:
                newb = "Test yourself"
            elif "syllabus" in t:
                newb = "Syllabus objectives"
            elif t in ("revision", "practice"):
                newb = re.sub(r"\s+"," ",vis_tag)
        if newb != body:
            edits.append((m.start(1), m.end(1), newb))

    # --- hero sub: keep syllabus-line sub, replace narrative sub(s) ---
    hsubs = list(re.finditer(r'<(p|div) class="sub"[^>]*>(.*?)</\1>', s, re.S))
    kept = []
    for m in hsubs:
        inner = re.sub(r"<[^>]+>","", m.group(2))
        is_syl = bool(re.search(r"IB Biology HL|· [A-D]\d", inner)) and len(inner.strip())<130 and not CLUB.search(inner)
        kept.append((m, is_syl))
    narr = [m for m, sy in kept if not sy]
    if narr:
        first = narr[0]
        edits.append((first.start(2), first.end(2), p["sub"]))
        for extra in narr[1:]:
            edits.append((extra.start(0), extra.end(0), ""))
    elif not any(sy for _, sy in kept):
        # no syllabus-line, single narrative-natured sub -> replace
        first = hsubs[0]
        edits.append((first.start(2), first.end(2), p["sub"]))

    # --- mind-map nodes ---
    for m in re.finditer(r'<span class="node[^"]*"[^>]*>([^<]+)<small>', s, re.S):
        word = m.group(1)
        if word in p["nodes"] and p["nodes"][word] != word:
            open_tag = re.search(r'<span class="node[^"]*"[^>]*>', m.group(0)).group(0)
            wstart = m.start()+len(open_tag)
            edits.append((wstart, wstart+len(word), p["nodes"][word]))

    # apply
    edits.sort(key=lambda e: e[0], reverse=True)
    for st, en, tx in edits:
        s = s[:st]+tx+s[en:]
    open(f, "w", encoding="utf-8", errors="replace").write(s)
    return len(edits)

for page in PLAN:
    try:
        k = do(page)
        print(f"OK  {page:24s} edits={k}")
    except Exception as e:
        print(f"FAIL {page:24s} -> {e!r}")
