#!/usr/bin/env python3
"""Apply the textbook-diff edits to the C2.1 comic (study-hub copy).
Each (old, new) must match EXACTLY once in the file. Atomic: builds the
new content in memory, asserts every edit, writes once at the end."""
import sys

PATH = r"C:\Users\ASUS\Desktop\Hermes_Workspace\study-hub\topics\bio\c2.1\index.html"

edits = []

def E(old, new):
    edits.append((old, new))

# ── Act 1 (C2.1.1): ligand-binding site + enzyme vs receptor ──
E("""<p class="muted">That's why one chemical can do completely different jobs: the message is the same, the doors it fits are different.</p>
  </div>

  <div class="grid2">""",
"""<p class="muted">That's why one chemical can do completely different jobs: the message is the same, the doors it fits are different.</p>
  </div>

  <div class="panel">
    <h3>LIGAND-BINDING SITE = THE KEYHOLE 🔑</h3>
    <p>Receptor–ligand binding is like enzyme–substrate specificity — with ONE crucial difference:</p>
    <ul class="clean">
      <li><b>Same:</b> binding happens at a <b>specific site</b>; the <b>shape and chemical properties</b> of the site match the ligand (rejecting everything else); neither enzyme nor receptor is changed by binding (induced fit is temporary).</li>
      <li><b>Different:</b> an <b>enzyme converts its substrate</b> into a product and releases it — binding is brief and the cycle repeats many times per second. A <b>receptor catalyses nothing</b> — the signalling chemical stays bound for a long time and is <b>released unchanged</b>.</li>
    </ul>
    <p class="muted">Exam phrasing: "the signalling chemical binds selectively to the ligand-binding site of the receptor and is released unchanged."</p>
  </div>

  <div class="grid2">""")

# ── Act 2 (C2.1.3): delivery table rows ──
E("""<td>Signal can <b>persist for hours</b>; often trigger changes in <b>gene expression</b>. Hydrophilic (proteins, amines) OR hydrophobic (steroids — carried bound to <b>transport proteins</b>).</td></tr>""",
"""<td>Signal can <b>persist for hours</b>; often trigger changes in <b>gene expression</b>. Secreted by <b>endocrine glands</b> (into blood capillaries, no duct) not <b>exocrine glands</b> (duct to the outside). Hydrophilic (proteins, amines) OR hydrophobic (steroids — carried bound to <b>transport proteins</b>). Examples: insulin, thyroxin, testosterone.</td></tr>""")

E("""<td><b>Rapid</b>; quickly <b>removed</b> from the gap after firing. Include amino acids, amines, peptides, <b>esters</b> (acetylcholine!) and gases.</td></tr>""",
"""<td><b>Rapid</b>; removed from the gap after firing — <b>broken down in the cleft OR reabsorbed</b> into the pre-synaptic neuron. <b>Excitatory</b> NTs stimulate impulses; <b>inhibitory</b> NTs block them. Include amino acids, amines, peptides, <b>esters</b> (acetylcholine!) and gases.</td></tr>""")

E("""<td>Also regulate the <b>cell cycle</b> (proliferation, embryo development). Examples: <b>interleukins, erythropoietin, interferon</b>.</td></tr>""",
"""<td>Act on the producing cell or <b>nearby cells</b>; can't enter cells → bind membrane receptors → cascades → gene expression. One cytokine can bind <b>several receptor types</b> → multiple effects. Roles: <b>inflammation</b>, immune responses, cell growth, embryo development (a cytokine storm = sepsis). Examples: <b>interleukins, erythropoietin, interferon</b>.</td></tr>""")

E("""<td>Enters via membrane proteins (active transport / facilitated diffusion) or is released from stores like the <b>sarcoplasmic reticulum</b>. Triggers <b>contraction</b> (muscle), <b>exocytosis</b> (nerves), or acts as a <b>second messenger</b>.</td></tr>""",
"""<td>Stored in the <b>sarcoplasmic reticulum</b> (muscle): an impulse opens channels → Ca²⁺ binds the proteins that <b>block contraction</b> → they shift → contraction starts; no impulse → Ca²⁺ pumped back. In neurons: Ca²⁺ enters the pre-synaptic end → <b>exocytosis</b> of neurotransmitter → pumped back out. Also a <b>second messenger</b>.</td></tr>""")

# ── Act 2 (C2.1.4): chemical menu ──
E("""<p class="big">Why so many different chemicals? Because each ligand must be <span class="accent">complementary in shape and charge</span> to its receptor — and <span class="cyan">small and soluble enough</span> to travel. Evolution just repurposed whatever molecules already existed.</p>""",
"""<p class="big">Why so many different chemicals? A signalling chemical must have a <span class="accent">distinctive shape and chemical properties</span> (so the receptor can tell it apart from everything else) and be <span class="cyan">small and soluble enough</span> to be transported. Evolution just repurposed whatever molecules already existed.</p>""")

E("""<tr><td>AMINE</td><td>Modified amino acid. <b>Melatonin</b> (circadian rhythm), <b>adrenaline</b> (heart rate).</td></tr>""",
"""<tr><td>AMINE</td><td>Modified amino acid. <b>Melatonin</b>, <b>thyroxin</b>, <b>adrenaline/epinephrine</b>.</td></tr>""")

E("""<tr><td>AMINE</td><td><b>Dopamine</b>.</td></tr>""",
"""<tr><td>AMINE</td><td><b>Dopamine</b>, <b>norepinephrine</b>.</td></tr>""")

E("""<div class="tip"><b>NITRIC vs NITROUS:</b> the official guide says <b>nitric oxide</b> (NO) is the gas neurotransmitter. Some sites say "nitrous oxide" — that's laughing gas (N₂O), a different molecule. In the exam, write <b>nitric oxide</b>.</div>
  </div>
</section>""",
"""<div class="tip"><b>NITRIC vs NITROUS:</b> the official guide says <b>nitric oxide</b> (NO) is the gas neurotransmitter. Some sites say "nitrous oxide" — that's laughing gas (N₂O), a different molecule. In the exam, write <b>nitric oxide</b>.</div>
    <p class="muted" style="margin-top:12px">🧪 Textbook grouping (Oxford 2023): hormones = <b>amines · peptides · steroids</b> (insulin sits under peptides there); neurotransmitters = <b>amines · gases · amino acids · esters</b>. The sharper exam answer keeps peptide (&lt;50 aa) vs protein (≥50 aa) separate.</p>
    <p class="muted">🐟 Fun fact from the textbook's own data question: <b>nitric oxide even runs newt courtship</b> — nitric oxide synthase activity in male newt brains spikes through each stage of the mating dance. NO: signalling gas, dating coach.</p>
  </div>
</section>""")

# ── Act 3 (C2.1.6): receptor chemistry ──
E("""<p><b>Receptor chemistry:</b> non-polar surface embedded in the lipid bilayer; <b>polar amino acids exposed to the fluids</b> form the binding site.</p>""",
"""<p><b>Receptor chemistry:</b> a <b>band of hydrophobic amino acids</b> on its surface — attracted to the apolar phospholipid tails in the core of the membrane — with <b>hydrophilic amino acids on both sides</b>, in contact with the aqueous fluids inside and outside the cell.</p>""")

E("""<p><b>Receptor chemistry:</b> <b>hydrophilic surface</b> (so it sits happily in aqueous cytoplasm) + <b>non-polar binding site</b> (for the fat-soluble ligand).</p>""",
"""<p><b>Receptor chemistry:</b> <b>hydrophilic amino acids</b> on its surface (so it stays dissolved in the aqueous cytoplasm or nucleus) + a <b>non-polar binding site</b> (for the fat-soluble ligand).</p>""")

E("""<p class="muted">Steroid hormones (oestradiol, progesterone, testosterone) work this way.</p>""",
"""<p class="muted">Steroid hormones (oestradiol, progesterone, testosterone) work this way. Oestradiol receptors even pair up: two hormone–receptor complexes <b>jointly bind DNA</b> as a dimer.</p>""")

# ── Act 3 (C2.1.8): ACh channel ──
E("""<li>The channel <b>opens</b> → <b>Na⁺ diffuses in passively</b> (down its gradient).</li>""",
"""<li>The channel <b>opens</b> → <b>Na⁺ floods in by facilitated diffusion</b> (down its gradient, through the open pore).</li>""")

E("""<li>The voltage across the membrane changes → <b>DEPOLARISATION</b>.</li>""",
"""<li>The voltage across the membrane changes → <b>LOCAL DEPOLARISATION</b> → can trigger an action potential (full story in C2.2).</li>""")

# ── Act 3 (C2.1.9/10): GPCR ──
E("""<p><b>The G protein</b> = three subunits: an <b>α subunit bound to GDP</b> + a <b>βγ dimer</b>.</p>""",
"""<p><b>The G protein</b> = three subunits: an <b>α subunit bound to GDP</b> + a <b>βγ dimer</b>. When resting, the α, β and γ subunits sit <b>assembled on the receptor</b>.</p>
      <p><b>GPCRs are everywhere:</b> their ligands include <b>light-sensitive compounds, odours, pheromones, hormones and neurotransmitters</b> — your <b>eyes (rhodopsin) and nose (olfactory receptors) run on GPCRs</b>. One of the biggest receptor families humans have.</p>""")

E("""<li>The <b>α subunit and βγ dimer dissociate</b> from the receptor.</li>""",
"""<li>The activated G protein <b>separates into its α, β and γ subunits and dissociates from the receptor</b> — the subunits then carry the message to effectors.</li>""")

E("""<p class="muted">Fight-or-flight effects to know: <b>heart rate ↑, muscle contraction, metabolism ↑ (fuel release), ventilation ↑, pupils dilate</b>.</p>""",
"""<p class="muted">Fight-or-flight effects to know: <b>heart rate ↑, muscle contraction, metabolism ↑ (fuel release), ventilation ↑, pupils dilate</b>.</p>
      <p class="muted">Speed check (textbook): liver cells break down glycogen and release glucose into the blood <b>within seconds</b> of an epinephrine signal.</p>""")

E("""<div class="nos"><b>NOS — NAMING CONVENTIONS:</b> "adrenaline" (Latin: <i>ad</i> = at, <i>ren</i> = kidney) and "epinephrine" (Greek: <i>epi</i> = above, <i>nephros</i> = kidney) both describe the same thing — produced at the kidney/adrenal gland. Two names persisting in different parts of the world is an example of <b>international cooperation in science</b>. Use either in the exam — both are accepted.</div>""",
"""<div class="nos"><b>NOS — NAMING CONVENTIONS:</b> "adrenaline" (Latin: <i>ad</i> = at, <i>ren</i> = kidney) and "epinephrine" (Greek: <i>epi</i> = above, <i>nephros</i> = kidney) both name the same hormone — produced at the adrenal gland, above the kidney. Most of the world says adrenaline; North America says epinephrine; the IUPAC chemical name is (R)-1-(3,4-dihydroxyphenyl)-2-methylaminoethanol. Shared naming conventions are <b>international cooperation in science</b> — though "epinephrine" risks confusion with the stimulant drug <b>ephedrine</b>, which is why some prefer "adrenaline". Use either in the exam — both accepted.</div>""")

# ── Act 3 (C2.1.11): insulin / RTK ──
E("""<p><b>What an RTK is:</b> a transmembrane <b>enzyme</b> that catalyses the <b>phosphorylation of tyrosine residues</b> on proteins, using phosphate groups from <b>ATP</b>. Adding phosphate changes a protein's shape and activity.</p>""",
"""<p><b>What an RTK is:</b> a transmembrane <b>kinase</b> — an enzyme that adds a phosphate group from <b>ATP</b> to a molecule (that's <b>phosphorylation</b>). This one phosphorylates the <b>amino acid tyrosine</b> in proteins. Adding phosphate changes a protein's shape and activity.</p>""")

E("""<li>The receptor has <b>two intracellular tails</b> that <b>connect</b> on binding.</li>""",
"""<li>The receptor has <b>two intracellular tails</b> — each one a tyrosine kinase enzyme — that <b>connect to form a dimer</b> on binding.</li>""")

E("""<li>One response: <b>vesicles containing glucose transporters (GLUT4) move to the plasma membrane</b> → glucose uptake increases.</li>""",
"""<li>One response: <b>vesicles containing glucose transporters (GLUT4) move to the plasma membrane and fuse with it</b> → the transporters are <b>channel proteins</b> → glucose enters by <b>facilitated diffusion</b> → used in cell respiration.</li>""")

# ── Act 3 (C2.1.12): steroids / FADS1 ──
E("""<p class="muted">Speed: slow (minutes to hours) but the effect <b>lasts</b>. Testosterone → male sex characteristics + <b>muscle growth</b>; oestradiol → female characteristics + <b>menstrual cycle</b>; progesterone → pregnancy (implantation, milk production).</p>""",
"""<p class="muted">Speed: slow (minutes to hours) but the effect <b>lasts</b>. Testosterone → male sex characteristics + <b>muscle growth</b> (textbook example: the androgen–receptor complex boosts the <b>FADS1</b> gene → more fats in prostate cells); oestradiol → female characteristics + <b>menstrual cycle</b>; progesterone → pregnancy (implantation, milk production).</p>""")

# ── Act 4 (C2.1.2): quorum sensing ──
E("""<p class="big"><span class="accent">Quorum sensing</span> = bacteria regulating their behaviour based on <b>population density</b>. A <b>quorum</b> = the minimum number of organisms needed for a coordinated action (like synchronised gene expression).</p>""",
"""<p class="big"><span class="accent">Quorum sensing</span> = bacteria regulating their behaviour based on <b>population density</b>. A <b>quorum</b> = the fixed minimum number of individuals needed for a meeting to go ahead (like the UN Security Council's two-thirds rule). For bacteria: enough cells to switch on a group activity.</p>""")

E("""<li><i>Vibrio fischeri</i> releases autoinducers that bind to <b>intracellular receptors</b> inside neighbouring bacteria (nice callback to Act 3!).</li>
        <li>Enough activated receptors → <b>transcription switched on</b> → the <b>enzyme luciferase</b> is made.</li>
        <li>Luciferase catalyses the reaction that produces <b>bioluminescence</b> — the bacteria glow.</li>""",
"""<li><i>Vibrio fischeri</i> releases autoinducers that bind to an <b>intracellular receptor called LuxR</b> in the cytoplasm (nice callback to Act 3!).</li>
        <li>The <b>LuxR–autoinducer complex binds DNA</b> → transcription switched on → the <b>enzyme luciferase</b> is made.</li>
        <li>Luciferase catalyses an <b>oxidation reaction</b> — <b>over 80%</b> of its energy comes out as greenish-blue light. Free-living bacteria don't glow: no quorum, no function, no wasted energy.</li>""")

E("""<li><b>Bacteria get:</b> organic compounds produced by the squid's metabolism.</li>
      </ul>
    </div>
  </div>
</section>""",
"""<li><b>Bacteria get:</b> organic compounds produced by the squid's metabolism.</li>
      </ul>
    </div>
  </div>
    <p class="muted" style="margin-top:14px">🦷 Textbook extra: quorum sensing builds <b>biofilms</b> too — bacteria on teeth secrete glue-like chemicals, stick to the tooth surface and form <b>dental plaque</b>. Quorum sensing is <b>interaction</b> (signals pass cell-to-cell); the group behaviours it triggers are <b>interdependence</b> (they only work if many cells take part).</p>
  </div>
</section>""")

# ── Act 5 (C2.1.13): oestradiol + progesterone ──
E("""<li>Binds intracellular receptor → complex = transcription factor.</li>
        <li>Regulates expression of <b>GnRH</b> (gonadotropin-releasing hormone).</li>""",
"""<li>Binds its receptor in the <b>cytoplasm</b> of the hypothalamus cell → complex moves to the nucleus = <b>transcription factor</b>.</li>
        <li>Enhances transcription of <b>GnRH</b> mRNA (gonadotropin-releasing hormone) — <b>just before and during ovulation</b>.</li>""")

E("""<p class="accent">🔥 THE CLEVER BIT: oestradiol can <b>INHIBIT or PROMOTE</b> GnRH — so it can drive <b>negative OR positive feedback</b>. One hormone, both knobs.</p>""",
"""<p class="accent">🔥 THE CLEVER BIT: at different stages of the menstrual cycle oestradiol can <b>INHIBIT or PROMOTE</b> GnRH — so one hormone drives <b>negative OR positive feedback</b>. One hormone, both knobs.</p>""")

E("""<li>Complex = transcription factor → regulates expression of a <b>growth factor</b>.</li>""",
"""<li>Complex = transcription factor → activates a specific gene: <b>insulin-like growth factor</b>.</li>""")

# ── Act 5 (C2.1.14): feedback examples ──
E("""<li><b>Thermoregulation:</b> body temp off → <b>thyroxin</b> drives changes that restore it.</li>""",
"""<li><b>Testosterone (textbook example):</b> hypothalamus → GnRH → anterior pituitary → LH → Leydig cells in the testes make testosterone. Rising testosterone → <b>less LH from the pituitary AND less GnRH from the hypothalamus</b> — the end-product shuts off its own production.</li>
        <li><b>Thermoregulation:</b> body temp off → <b>thyroxin</b> drives changes that restore it.</li>""")

E("""<li><b>Childbirth:</b> oxytocin → contractions → more oxytocin → baby out. 🍼</li>""",
"""<li><b>Childbirth:</b> oxytocin → contractions → more oxytocin → baby out. 🍼</li>
        <li><b>Calcium-induced calcium release (textbook example):</b> IP₃ binds an IP₃ receptor on the ER → a little Ca²⁺ escapes → that Ca²⁺ activates a <b>neighbouring</b> calcium channel → even more Ca²⁺ floods out. The product amplifies its own production.</li>""")

# ── Cheat sheet ──
E("""<p class="aim">Everything the examiner wants, compressed into 12 lines.</p>""",
"""<p class="aim">Everything the examiner wants, compressed into 14 lines.</p>""")

E("""<div class="line">12 · NEGATIVE = thermostat · <span>POSITIVE = snowball</span></div>
  </div>
</section>""",
"""<div class="line">12 · NEGATIVE = thermostat · <span>POSITIVE = snowball</span></div>
    <div class="line">13 · RECEPTOR HOLDS THE KEY · <span>ENZYME CONVERTS IT</span> · ligand released unchanged</div>
    <div class="line">14 · GPCRs RUN YOUR EYES AND NOSE · <span>LuxR = the bacteria's DNA key</span> · IP₃ → Ca²⁺ → more Ca²⁺</div>
  </div>
</section>""")

# ── Quiz: 2 new questions ──
E("""<div class="fb wrong">❌ Oestradiol can <b>inhibit or promote GnRH</b> — so the same hormone can push the loop either direction.</div>
  </div>
</section>""",
"""<div class="fb wrong">❌ Oestradiol can <b>inhibit or promote GnRH</b> — so the same hormone can push the loop either direction.</div>
  </div>

  <div class="q" data-a="unchanged">
    <p>9. What does a receptor do that an enzyme doesn't?</p>
    <label><input type="radio" name="q9" value="wrong1"> It converts the ligand into a product</label>
    <label><input type="radio" name="q9" value="unchanged"> It binds the ligand for a long time and releases it UNCHANGED</label>
    <label><input type="radio" name="q9" value="wrong2"> It speeds up the ligand's breakdown</label>
    <div class="fb correct">✅ Receptors don't catalyse — the signalling chemical stays bound, then leaves unchanged. Enzymes convert substrates into products and release them.</div>
    <div class="fb wrong">❌ Receptors hold and release the ligand <b>unchanged</b> — no catalysis. Converting substrate to product is what enzymes do.</div>
  </div>

  <div class="q" data-a="pos">
    <p>10. IP₃ opens a calcium channel on the ER; the escaping Ca²⁺ opens a NEIGHBOURING channel; more Ca²⁺ floods out. Which feedback type?</p>
    <label><input type="radio" name="q10" value="pos"> Positive — the product (Ca²⁺) amplifies its own release</label>
    <label><input type="radio" name="q10" value="wrong1"> Negative — it returns the cell to equilibrium</label>
    <div class="fb correct">✅ Positive — calcium-induced calcium release. A snowball: each bit of Ca²⁺ recruits more.</div>
    <div class="fb wrong">❌ Positive. The end-product (Ca²⁺) amplifies the starting point (more Ca²⁺ release) — that's the textbook definition of positive feedback.</div>
  </div>
</section>""")

# ── Footer ──
E("""<p>Built from the <a href="https://ib.bioninja.com.au/c21-chemical-signalling/" target="_blank">BioNinja</a> C2.1 pages · IB Biology guide (first exams 2025) · AHL topic</p>""",
"""<p>Built from the <a href="https://ib.bioninja.com.au/c21-chemical-signalling/" target="_blank">BioNinja</a> C2.1 pages + <b>Biology: Course Companion 2nd ed.</b> (Allott &amp; Mindorff, Oxford 2023) · IB Biology guide (first exams 2025) · AHL topic</p>""")

# ── Apply ──
with open(PATH, "r", encoding="utf-8") as f:
    src = f.read()

fails = []
for i, (old, new) in enumerate(edits, 1):
    n = src.count(old)
    if n != 1:
        fails.append((i, n, old[:70].replace("\n", "\\n")))
        continue
    src = src.replace(old, new)

if fails:
    print("FAILED EDITS:")
    for i, n, snippet in fails:
        print(f"  #{i}: count={n} :: {snippet!r}")
    sys.exit(1)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(src)
print(f"OK — {len(edits)} edits applied atomically to {PATH}")
