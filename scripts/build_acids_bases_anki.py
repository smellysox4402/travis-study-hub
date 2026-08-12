#!/usr/bin/env python3
"""Anki cloze deck builder: Chem HL — Acids & Bases (Reactivity 3.1).
Matches the user's 'Cloze+' model (Text + Back Extra) in the 'Chem HL' deck.
Run: python scripts/build_acids_bases_anki.py
"""
import genanki
import os

MODEL_ID = 1607392319
DECK_ID = 2059400112
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "chem", "acids-bases", "Chem_Acids_Bases.apkg")

model = genanki.Model(
    MODEL_ID,
    "Cloze+",
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[
        {
            "name": "Cloze",
            "qfmt": '{{cloze:Text}}<br><br><span style="font-size:12px;color:#888">{{type:Back Extra}}</span>',
            "afmt": '{{cloze:Text}}<hr id="answer">{{Back Extra}}',
        }
    ],
)

deck = genanki.Deck(DECK_ID, "Chem HL")

def add(text, extra=""):
    deck.add_note(genanki.Note(model, [text, extra]))

# ── R3.1.1 · Brønsted–Lowry ──
add("A {{c1::Brønsted–Lowry acid}} is a {{c2::proton donor}} and a Brønsted–Lowry base is a {{c3::proton acceptor}}.",
    "HCl loses H⁺ → acid; NH₃ gains H⁺ → base. Expands Arrhenius (which required water and OH⁻). NH₃(g) + HCl(g) → NH₄Cl(s) works without water.")
add("The Arrhenius definitions: acid = substance producing {{c1::H⁺}} ions in water; base = substance producing {{c1::OH⁻}} ions in water. Limitation: {{c2::NH₃}} contains no oxygen yet is a base — it makes OH⁻ by reacting with water.",
    "NH₃ + H₂O ⇌ NH₄⁺ + OH⁻. The OH⁻ comes from water, not the base. B–L theory removes the water requirement.")
add("H⁺ in water exists as {{c1::H₃O⁺}} (hydronium/hydroxonium): oxygen donates a lone pair to the empty H⁺ orbital. {{c2::Trigonal pyramidal}} shape. IB accepts H⁺ as shorthand.",
    "Both H⁺ and H₃O⁺ are accepted in assessments.")
add("NaOH is treated in B–L theory as a complex of {{c1::OH⁻ (base)}} with {{c2::Na⁺ (metal cation)}}.",
    "Alkali = water-soluble base (group 1/2 hydroxides). All alkalis are bases, not all bases are alkalis (FeO is a base, not an alkali).")

# ── R3.1.2 · Conjugate pairs ──
add("A conjugate acid–base pair is a pair of species differing by {{c1::exactly one proton}}. HCN/CN⁻ and {{c2::H₃O⁺/H₂O}} are pairs.",
    "H₂SO₄ and SO₄²⁻ are NOT a pair (differ by 2 protons). Stepwise: H₂SO₄ ⇌ H⁺ + HSO₄⁻ and HSO₄⁻ ⇌ H⁺ + SO₄²⁻.")
add("The conjugate base of H₃PO₄ is {{c1::H₂PO₄⁻}}; the conjugate acid of CH₃COO⁻ is {{c1::CH₃COOH}}.",
    "A base gaining a proton → conjugate acid; an acid losing a proton → conjugate base.")

# ── R3.1.3 · Amphiprotic ──
add("{{c1::Amphiprotic}} species can both donate and accept a proton (H₂O, HCO₃⁻, HSO₄⁻, H₂PO₄⁻). {{c2::Amphoteric}} species react with both acids and bases.",
    "Every amphiprotic species is amphoteric, but NOT vice versa. ZnO + HCl AND ZnO + NaOH: amphoteric but NOT amphiprotic (no proton to donate).")
add("Amino acids (H₂N–CH(R)–COOH) exist as {{c1::zwitterions}} in neutral solution — carrying both a + and − charge in the same species.",
    "They are the structural units of peptides/proteins. In acid they act as bases (→ cation); in base as acids (→ anion).")

# ── R3.1.4 · pH ──
add("pH = {{c1::−log₁₀[H⁺]}}; [H⁺] = {{c2::10⁻ᵖᴴ}}. At 298 K: pH 7 = {{c3::neutral}}, &lt;7 acidic, &gt;7 basic.",
    "0.100 mol dm⁻³ HCl → [H⁺] = 0.100 → pH = 1.00. pH 3 → [H⁺] = 10⁻³ = 0.001 mol dm⁻³.")
add("0.0100 mol dm⁻³ H₂SO₄ has pH {{c1::1.70}} — because [H⁺] = 2 × 0.0100 = 0.0200 (diprotic!).",
    "pH = −log(0.0200) = 1.70. Always count H⁺ per formula unit.")
add("[HNO₃] needed for pH 4.2 is {{c1::6.3 × 10⁻⁵}} mol dm⁻³.",
    "[H⁺] = 10⁻⁴·² = 6.3 × 10⁻⁵.")

# ── R3.1.5 · Kw ──
add("Kw = [H⁺][OH⁻] = {{c1::1.00 × 10⁻¹⁴}} at {{c2::298 K}}. Pure water: [H⁺] = [OH⁻] = {{c3::1.00 × 10⁻⁷}} mol dm⁻³.",
    "Kw is valid only for dilute aqueous solutions (battery acid breaks it) and INCREASES with temperature.")
add("In 0.100 mol dm⁻³ HCl at 25 °C, [OH⁻] = {{c1::1.00 × 10⁻¹³}} mol dm⁻³.",
    "Kw/[H⁺] = 1.00×10⁻¹⁴ / 0.100 = 1.00×10⁻¹³. [H⁺] &gt; [OH⁻] → acidic ✓.")
add("Water's autoionization: H₂O + H₂O ⇌ {{c1::H₃O⁺ + OH⁻}}. Only ~{{c2::1 in 1.8×10⁹}} water molecules are ionized.",
    "[H₂O] ≈ 55.5 mol dm⁻³ (1000 g ÷ 18.02 g mol⁻¹), effectively constant → K·[H₂O] = Kw.")

# ── R3.1.6 · Strong vs weak ──
add("The 7 strong acids: {{c1::HCl, HBr, HI, HNO₃, H₂SO₄, HClO₄, HClO₃}}. Everything else: assume {{c2::weak}}.",
    "Strong = full dissociation (single arrow →). Weak = equilibrium (⇌).")
add("Strong vs weak acids/bases differ in {{c1::extent of ionization}}, NOT concentration. 10 mol dm⁻³ CH₃COOH is {{c2::weak AND concentrated}}.",
    "'Strong solution'/'weak solution' NOT accepted in IB assessments. Strong ≠ concentrated.")
add("Strong bases: group 1 hydroxides + most group 2 hydroxides. {{c1::Mg(OH)₂ and Ca(OH)₂}} are insoluble → heterogeneous equilibria, so they look weak for solubility (not strength) reasons.",
    "Covalent hydroxides (Al, Be, transition metals, e.g. Fe(OH)₂) are weak bases, virtually insoluble.")
add("Oxoacid strength increases with {{c1::oxidation state of the central atom}} (more O atoms): HNO₂ (N +3) weak → HNO₃ (N +5) strong; H₂SO₄ strong vs H₂SO₃ weak.",
    "Binary acid strength increases across a period (PH₃ → H₂S → HCl) and down a group (HF weak, HCl/HBr/HI strong).")
add("NH₃ is a weak base: NH₃ + H₂O ⇌ {{c1::NH₄⁺ + OH⁻}}. 'Aqueous ammonia' is often written {{c2::NH₄OH(aq)}} — unstable, exists only in solution.",
    "Amines are organic derivatives: methylamine CH₃NH₂, dimethylamine (CH₃)₂NH, trimethylamine (CH₃)₃N.")

# ── R3.1.7 · Neutralization ──
add("Metal + acid → {{c1::salt + H₂}}. Net ionic: {{c2::Mg + 2H⁺ → Mg²⁺ + H₂}} (Cu, Ag below H: no reaction).",
    "Mg + 2HCl → MgCl₂ + H₂. Weak acids stay molecular in ionic equations.")
add("Metal oxide + acid → {{c1::salt + water}}. Carbonate + acid → {{c1::salt + CO₂ + H₂O}}.",
    "MgO + 2HCl → MgCl₂ + H₂O. Na₂CO₃ + 2HCl → 2NaCl + CO₂ + H₂O. Net: CO₃²⁻ + 2H⁺ → CO₂ + H₂O. Hydrogencarbonate: HCO₃⁻ + H⁺ → CO₂ + H₂O.")
add("2H₃PO₄ + 3CaCO₃ → {{c1::Ca₃(PO₄)₂ + 3CO₂ + 3H₂O}} (O check: 17 = 17).",
    "Balance nonmetals (except H/O) → metals → H → verify O.")

# ── R3.1.8 · pH curves SL ──
add("Strong acid + strong base pH curve: low start, {{c1::sharp pH jump}} at equivalence to {{c2::7.0}}, flatten at pH ~12–14.",
    "Equivalence = only NaCl(aq). Typical concentrations 0.01–1 M → initial pH 2 to 0.")

# ── R3.1.9 · pOH (AHL) ──
add("pOH = {{c1::−log₁₀[OH⁻]}}; [OH⁻] = {{c2::10⁻ᵖᴼᴴ}}. At 298 K: pH + pOH = {{c3::14}}.",
    "0.025 mol dm⁻³ KOH → [OH⁻] = 0.025 → pOH = 1.60 → pH = 12.40.")
add("pOH of 0.025 mol dm⁻³ H₂SO₄ = {{c1::12.70}} (alt: pH 1.30, pOH = 14 − 1.30).",
    "[H⁺] = 2 × 0.025 = 0.050; [OH⁻] = 10⁻¹⁴/0.050 = 2.00×10⁻¹³; pOH = −log(2.00×10⁻¹³) = 12.70.")

# ── R3.1.10 · Ka/Kb (AHL) ──
add("Ka = {{c1::[H⁺][A⁻]/[HA]}}; pKa = {{c2::−log Ka}}. Larger Ka = stronger acid; {{c3::larger pKa = weaker}}.",
    "Kb = [BH⁺][OH⁻]/[B]. Methanoic pKa 3.75 &lt; ethanoic 4.76 → methanoic stronger. Methylamine pKb 3.34 &lt; NH₃ 4.75 → methylamine stronger base.")
add("Ka of CH₃COOH = {{c1::1.74 × 10⁻⁵}} (pKa 4.76). Ka of HCN = {{c2::6.17 × 10⁻¹⁰}} (pKa 9.21).",
    "Table 8: HF 6.76×10⁻⁴/3.17; HCOOH 1.78×10⁻⁴/3.75; (CH₃)₂NH Kb 5.37×10⁻⁴/3.27; CH₃NH₂ Kb 4.57×10⁻⁴/3.34; NH₃ Kb 1.78×10⁻⁵/4.75; C₆H₅NH₂ Kb 7.41×10⁻¹⁰/9.13.")
add("0.0100 mol dm⁻³ propanoic acid, pH 3.44: Ka = {{c1::1.32 × 10⁻⁵}}, pKa = {{c1::4.88}}.",
    "[H⁺] = 10⁻³·⁴⁴ = 3.63×10⁻⁴ ≈ [A⁻]; Ka = (3.63×10⁻⁴)²/0.0100. Approximations: [HA] ≈ initial, [A⁻] ≈ [H⁺]. Quadratics NOT required in exams.")
add("pH of 0.100 mol dm⁻³ propanoic acid (Ka 1.32×10⁻⁵): [H⁺] = √(Ka·c) = {{c1::1.15 × 10⁻³}} → pH = {{c1::2.94}}.",
    "For weak acids: [H⁺] ≈ √(Ka × c).")
add("0.0100 mol dm⁻³ trimethylamine, pH 10.90: Kb = {{c1::6.31 × 10⁻⁵}}, pKb = {{c1::4.20}}.",
    "pOH = 14 − 10.90 = 3.10; [OH⁻] = 10⁻³·¹⁰ = 7.94×10⁻⁴; Kb = (7.94×10⁻⁴)²/0.0100.")
add("pH of 0.100 mol dm⁻³ trimethylamine (Kb 6.31×10⁻⁵): [OH⁻] = {{c1::2.51 × 10⁻³}}, pOH ≈ 2.60, pH = {{c1::11.40}}.",
    "[OH⁻] = √(Kb·c) = √(6.31×10⁻⁵ × 0.100).")

# ── R3.1.11 · Ka·Kb = Kw (AHL) ──
add("For a conjugate acid–base pair: {{c1::Ka × Kb = Kw}} and {{c2::pKa + pKb = 14}} at 298 K.",
    "Adding the two equilibria (HA ⇌ H⁺ + A⁻ and A⁻ + H₂O ⇌ HA + OH⁻) gives H₂O ⇌ H⁺ + OH⁻ → constants multiply. Valid ONLY for conjugate pairs.")
add("pKb of CH₃COO⁻ = {{c1::9.24}} (pKa of CH₃COOH = 4.76).",
    "The stronger the acid, the weaker its conjugate base.")

# ── R3.1.12 · Salt pH (AHL) ──
add("NH₄Cl solution is {{c1::acidic}}: NH₄⁺ + H₂O ⇌ {{c2::NH₃ + H₃O⁺}} (cation of weak base hydrolyses).",
    "'Hydrolysis is for the weak.' Strong acid + weak base → acidic salt.")
add("CH₃COONa solution is {{c1::basic}}: CH₃COO⁻ + H₂O ⇌ {{c2::CH₃COOH + OH⁻}}.",
    "Weak acid + strong base → basic salt. Ions of strong acids/bases don't hydrolyse.")
add("Weak acid + weak base salt (NH₄CN): the pH is set by {{c1::the stronger of the two conjugates}} — CN⁻ (pKb 4.79) beats NH₄⁺ (pKa 9.25) → {{c2::slightly basic}}.",
    "Strong+strong → neutral (KNO₃, NaCl); strong+weak → the weak ion's side wins.")

# ── R3.1.13 · pH curves AHL ──
add("Weak acid + strong base curve: higher start (~pH 3), a {{c1::buffer region}}, smaller pH jump, equivalence at {{c2::pH > 7}}.",
    "CH₃COOH + NaOH: equivalence (CH₃COONa only) at pH &gt; 7 because the anion hydrolyses. Flattens at pH of the strong base ≈ 13.")
add("Strong acid + weak base curve: equivalence at {{c1::pH < 7}} (NH₄Cl hydrolyses).",
    "NH₃ + HCl: pH drop to &lt; 7, flattening at pH of strong acid ≈ 1.")
add("Weak acid + weak base curve: {{c1::NO sharp change anywhere}} → {{c2::indicators are useless}}; use a pH meter.",
    "Buffer region 1 (CH₃COOH + CH₃COONH₄), equivalence ≈ 7, buffer region 2 (NH₃ + CH₃COONH₄).")
add("At the half-equivalence point of a weak acid titration: [HA] = [A⁻], so {{c1::pH = pKa}}.",
    "Ka = [H⁺][A⁻]/[HA] → when [A⁻] = [HA], Ka = [H⁺]. Similarly pOH = pKb for weak bases.")

# ── R3.1.14 · Indicators (AHL) ──
add("Acid–base indicators are {{c1::weak acids}} (HInd ⇌ H⁺ + Ind⁻) whose conjugate forms have {{c2::different colours}}. The end point pH ≈ {{c3::pKa of the indicator}}.",
    "Low pH → mostly HInd (acid colour); high pH → mostly Ind⁻ (base colour).")
add("Indicator ranges: methyl orange {{c1::3.1–4.4}} (red → yellow, pKa 3.7); bromothymol blue {{c1::6.0–7.6}} (yellow → blue, pKa 7.0); phenolphthalein {{c1::8.3–10.0}} (colourless → pink, pKa 9.6).",
    "Data booklet section 18 has more (e.g. methyl red 4.4–6.2).")

# ── R3.1.15 · Choosing indicators (AHL) ──
add("Indicator choice rule: transition range must {{c1::coincide with the equivalence pH}}. Equivalence pH &gt; 7 → {{c2::phenolphthalein}}; &lt; 7 → {{c2::methyl orange}}; = 7 → {{c2::bromothymol blue}} (but any works for strong+strong).",
    "HCOONa equivalence (weak acid + strong base) → phenolphthalein. Weak+weak: no indicator at all.")

# ── R3.1.16 · Buffers (AHL) ──
add("A buffer solution {{c1::resists change in pH}} on addition of small amounts of acid or alkali. It contains {{c2::both conjugates of a weak acid–base pair}}.",
    "Ethanoate buffer: CH₃COOH + CH₃COONa. Human blood: 7.35–7.45, held by hydrogencarbonate/hydrogenphosphate/CO₂/proteins.")
add("Buffer action with added HCl: {{c1::H⁺ + CH₃COO⁻ → CH₃COOH}} (strong acid → weak acid). With added NaOH: {{c1::OH⁻ + CH₃COOH → CH₃COO⁻ + H₂O}} (strong base → weak base).",
    "'A strong acid is replaced with a weak acid, a strong base with a weak base.'")
add("Buffer types: ethanoate (CH₃COOH/CH₃COO⁻, pKa 4.76); ammonia (NH₄⁺/NH₃, pKa 9.25); phosphate (H₂PO₄⁻/HPO₄²⁻, pKa 7.20); carbonate (HCO₃⁻/CO₃²⁻, pKa 10.32).",
    "1 drop 0.1 M HCl in 100 cm³ water: pH 7.0 → 4.3 (Δ2.7). In phosphate buffer: ΔpH &lt; 0.001.")

# ── R3.1.17 · Buffer pH (AHL) ──
add("Henderson–Hasselbalch: pH = {{c1::pKa + log([A⁻]/[HA])}}.",
    "Derived from Ka = [H⁺][A⁻]/[HA]. Diluting changes both concentrations equally → ratio (and pH) unchanged. Capacity is finite.")
add("Buffer pH with 0.100 M CH₃COOH and 0.200 M CH₃COONa (pKa 4.76): {{c1::5.06}}.",
    "pH = 4.76 + log(0.200/0.100) = 4.76 + 0.30 = 5.06.")
add("Buffer of pH 11.00 from CH₃NH₂ + HCl: the conjugate pair is {{c1::CH₃NH₃⁺ (acid) / CH₃NH₂ (base)}}; the excess reactant was {{c2::methylamine}}; ratio [CH₃NH₃⁺]:[CH₃NH₂] = {{c3::1 : 2.19}}.",
    "pKa(CH₃NH₃⁺) = 14 − 3.34 = 10.66; log ratio = 11.00 − 10.66 = 0.34 → ratio = 10⁰·³⁴ = 2.19. If HCl were in excess, all weak base would be consumed — no buffer.")
add("Buffer pH: 0.50 M NaH₂PO₄ + 0.20 M Na₂HPO₄ (pKa 7.20) = {{c1::6.80}}; 0.25 M NH₃ + 0.50 M NH₄Cl (pKa 9.25) = {{c1::8.95}}.",
    "pH = pKa + log(base/acid). 7.20 + log(0.20/0.50) = 6.80; 9.25 + log(0.25/0.50) = 8.95.")

# ── End-of-topic gems ──
add("At 10 °C, Kw = 2.88 × 10⁻¹⁵ → pure water pH = {{c1::7.27}} — but still {{c2::neutral}} because [H⁺] = [OH⁻].",
    "Neutral ≠ pH 7 away from 298 K. Kw(10 °C) = 1.00×10⁻¹⁴/3.47.")
add("0.100 dm³ of 0.020 M KOH diluted with 0.900 dm³ water → pH = {{c1::11.30}}.",
    "[KOH] = 0.0020 M → pOH = 2.70 → pH = 11.30.")
add("Benzoic acid 0.020 M, pH 2.95: Ka = {{c1::6.3 × 10⁻⁵}}, pKa = {{c1::4.20}}; at 0.10 M → pH = {{c1::2.60}}.",
    "Ka = (1.12×10⁻³)²/0.020 = 6.3×10⁻⁵; [H⁺] = √(6.3×10⁻⁵ × 0.10) = 2.5×10⁻³.")
add("0.010 M CH₃NH₂ (Kb 4.57×10⁻⁴) → pH = {{c1::11.33}}.",
    "[OH⁻] = √(4.57×10⁻⁴ × 0.010) = 2.14×10⁻³ → pOH 2.67 → pH 11.33.")
add("Buffer 0.25 M HCOOH + 0.50 M HCOONa (pKa 3.75) → pH = {{c1::4.05}}.",
    "3.75 + log(0.50/0.25) = 3.75 + 0.30 = 4.05.")
add("Buffer 0.50 M CH₃NH₂ + 0.20 M CH₃NH₃Cl (pKa 10.66) → pH = {{c1::11.06}}.",
    "10.66 + log(0.50/0.20) = 10.66 + 0.40 = 11.06.")

genanki.Package(deck).write_to_file(OUT)
print("OK:", len(deck.notes), "notes ->", OUT)
