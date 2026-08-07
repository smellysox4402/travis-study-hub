#!/usr/bin/env python3
"""Anki cloze deck builder: Chem HL — Equilibrium (Reactivity 2.3).
Matches the user's 'Cloze+' model (Text + Back Extra) in the 'Chem HL' deck.
Run: python scripts/build_equilibrium_anki.py
"""
import genanki, os

MODEL_ID = 1607392319   # same model as all other topics (Cloze+)
DECK_ID  = 2059400112   # Chem HL deck
SUBJECT_DECK = "Chem HL"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics",
                   "chem", "equilibrium", "Chem_Equilibrium.apkg")

model = genanki.Model(
    MODEL_ID,
    "Cloze+",
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>',
    }],
    model_type=1,  # cloze — genanki.CLOZE constant does NOT exist in this venv
)

CARDS = [
    # ---- R2.3.1 dynamic equilibrium (SL) ----
    ("A {{c1::closed}} system is required for equilibrium — in an open one, escaped gas can't be re-formed, so no balance is possible.",
     "R2.3.1 — closed system = energy can cross, matter cannot"),
    ("At dynamic equilibrium the rates of the {{c1::forward}} and {{c2::reverse}} reactions are {{c3::equal}} — not the amounts.",
     "R2.3.1 — the turnstile: same number through each side per second"),
    ("At equilibrium, changes stop at the {{c1::macroscopic}} level (colour, density, concentrations constant) but continue at the {{c2::microscopic}} level.",
     "R2.3.1 — reactions NEVER stop; they just balance"),
    ("The same equilibrium state can be reached {{c1::from either direction}} — start with reactants OR products, same final concentrations.",
     "R2.3.1 — N₂+3H₂→NH₃ or pure NH₃ → same plateau"),
    ("Radioactive ⁸⁰Br₂ added to an equilibrium mixture of Br₂(l) ⇌ Br₂(g) appears in the {{c1::gas phase almost immediately}} — proof evaporation/condensation still run.",
     "R2.3.1 — the isotope trick proves it's dynamic"),
    ("A saturated solution (excess NaCl(s) ⇌ Na⁺(aq) + Cl⁻(aq)) is a {{c1::dynamic equilibrium}} between dissolution and precipitation.",
     "R2.3.1 — heterogeneous equilibrium, solid + solution"),
    ("Equilibrium of Br₂: Br₂(l) ⇌ Br₂(g) is a {{c1::heterogeneous}} equilibrium (two phases present).",
     "R2.3.1 — heterogeneous = more than one phase"),
    # ---- R2.3.2 equilibrium law (SL) ----
    ("For aA + bB + ... ⇌ xX + yY + ..., K = {{c1::[X]ˣ[Y]ʸ… / [A]ᵃ[B]ᵇ…}}.",
     "R2.3.2 — products (forward) on top, reactants on bottom, coefficients as exponents"),
    ("K for the Haber process N₂ + 3H₂ ⇌ 2NH₃ = {{c1::[NH₃]² / ([N₂][H₂]³)}}.",
     "R2.3.2 — memorise this one; it's the classic"),
    ("K values are treated as {{c1::unitless}}, even though concentrations are quoted in mol dm⁻³.",
     "R2.3.2 — units are dropped from K"),
    ("In the K expression, {{c1::solids}}, {{c2::pure liquids}} and the {{c3::solvent}} (water in aqueous reactions) are excluded.",
     "R2.3.2 — constant-concentration species don't appear"),
    ("In a NON-aqueous reaction where water is a real reactant, water {{c1::IS}} included in the K expression.",
     "R2.3.2 — solvent-exclusion rule only applies to aqueous solutions"),
    ("The equilibrium law says the K ratio is constant if {{c1::temperature}} is kept constant.",
     "R2.3.2 — the one condition that defines K"),
    # ---- R2.3.3 magnitude of K (SL) ----
    ("K &gt;&gt; 1 means {{c1::products}} are strongly favoured — the reaction is practically {{c2::irreversible}} (goes to completion).",
     "R2.3.3 — big scoreboard = home team won"),
    ("K &lt;&lt; 1 means {{c1::reactants}} are strongly favoured — the forward reaction barely proceeds.",
     "R2.3.3 — tiny K = reaction barely happens"),
    ("K = 1 means the equilibrium is established at approximately {{c1::equal concentrations}} of reactants and products.",
     "R2.3.3 — exact ratio still depends on stoichiometric coefficients"),
    ("K depends on {{c1::temperature}} only — NOT on pressure or concentration.",
     "R2.3.3 — bump initial N₂ from 1.0 to 2.5 mol dm⁻³: different concentrations, same K = 0.59"),
    ("If all stoichiometric coefficients are halved, the new K = {{c1::√K}}; if doubled, K′ = {{c2::K²}}.",
     "R2.3.3 — K surgery rule 1"),
    ("If the equation is reversed, the new K = {{c1::1/K}}; if two equations are added, K′ = {{c2::K₁ × K₂}}.",
     "R2.3.3 — K surgery rules 2 and 3"),
    ("Worked example: at 475 K, N₂+3H₂ ⇌ 2NH₃ has K = 0.59. Reversed (2NH₃ ⇌ N₂+3H₂): K = {{c1::1.7}}; halved (NH₃ ⇌ ½N₂+1.5H₂): K = {{c2::1.3}}.",
     "R2.3.3 — 1/0.59 = 1.7; √1.7 = 1.3"),
    ("Worked example: [NH₃]=1.00, [N₂]=0.50, [H₂]=1.50 mol dm⁻³ at equilibrium → K = {{c1::0.59}}.",
     "R2.3.3 — 1.00²/(0.50 × 1.50³) = 1/1.6875"),
    # ---- R2.3.4 Le Chatelier (SL) ----
    ("Le Chatelier's principle: a disturbed equilibrium shifts to {{c1::counteract the change}} and return to equilibrium.",
     "R2.3.4 — the bouncer restores order"),
    ("Shift to the {{c1::right}} = forward reaction favoured = more {{c2::products}}; shift to the left = more reactants.",
     "R2.3.4 — direction language matters in answers"),
    ("↑ concentration of a reactant → equilibrium shifts {{c1::right}}; ↑ concentration of a product → shifts {{c2::left}}.",
     "R2.3.4 — push the crowd, it pushes back"),
    ("2CrO₄²⁻ + 2H⁺ ⇌ Cr₂O₇²⁻ + H₂O: adding acid turns the solution {{c1::orange}} (shift right, dichromate); adding alkali turns it {{c2::yellow}} (shift left, chromate).",
     "R2.3.4 — chromate yellow ⇌ dichromate orange"),
    ("Water is excluded from K and barely affects the chromate/dichromate position because it is {{c1::the solvent in huge excess}}.",
     "R2.3.4 — dilution only makes the colour paler, not yellow"),
    ("For pressure effects, count {{c1::gas molecules only}} — ignore solids, liquids and aqueous species.",
     "R2.3.4 — the general rule for heterogeneous equilibria"),
    ("↑ pressure shifts equilibrium toward the side with {{c1::fewer}} gas molecules; ↓ pressure toward {{c2::more}}.",
     "R2.3.4 — N₂+3H₂ (4 gas) ⇌ 2NH₃ (2 gas): ↑P → right"),
    ("Br₂(l) ⇌ Br₂(g): ↑ pressure shifts the equilibrium {{c1::left}} (condensation) — liquids are incompressible, only the gas concentration rises.",
     "R2.3.4 — 0 gas molecules left, 1 right"),
    ("Equal numbers of gas molecules on both sides → pressure changes have {{c1::no effect}} on the position.",
     "R2.3.4 — H₂ + I₂ ⇌ 2HI is the classic"),
    ("Pressure changes have no effect on equilibria in {{c1::condensed phases}} (liquids/solids are almost incompressible).",
     "R2.3.4 — but heterogeneous equilibria with gases respond like gas systems"),
    ("A decrease in volume = {{c1::increase in pressure}} (PV = nRT) — so volume effects are OPPOSITE to pressure effects.",
     "R2.3.4 — ↓V acts like ↑P"),
    ("To predict temperature effects, treat heat as a {{c1::chemical}}: product for exothermic (reactants ⇌ products + Q), reactant for endothermic (reactants + Q ⇌ products).",
     "R2.3.4 — the heat-as-substance trick"),
    ("For an exothermic forward reaction, ↑ temperature shifts equilibrium {{c1::left}} and K {{c2::decreases}}.",
     "R2.3.4 — Haber: ΔHr = −91.8 kJ mol⁻¹; hot reactor → less NH₃"),
    ("For an endothermic forward reaction, ↑ temperature shifts equilibrium {{c1::right}} and K {{c2::increases}}.",
     "R2.3.4 — reverse of the exo case"),
    ("Temperature is the ONLY factor that changes {{c1::both}} the position of equilibrium and the value of K.",
     "R2.3.4 — everything else moves position at most"),
    ("A catalyst increases the rates of both forward and reverse reactions {{c1::equally}}, so the position and K are {{c2::unchanged}} — equilibrium is just reached faster.",
     "R2.3.4 — wider pipe, same final water level"),
    ("Haber process conditions: {{c1::200 atm (20 MPa)}}, {{c2::400–450 °C}}, {{c3::iron catalyst}}, NH₃ condensed out + gases recycled (~98% yield).",
     "R2.3.4 — high P pushes right (4→2 gas), moderate T is a rate/position compromise"),
    ("Haber's forward reaction is {{c1::exothermic}} (ΔHr = −91.8 kJ mol⁻¹), so low temperature would favour yield but slow the rate — hence the compromise.",
     "R2.3.4 — 400–450 °C balances yield vs rate"),
    # ---- R2.3.5 reaction quotient Q (AHL) ----
    ("The reaction quotient Q is calculated like K but with {{c1::actual (non-equilibrium)}} concentrations.",
     "R2.3.5 AHL — the compass reading RIGHT NOW"),
    ("If Q &lt; K, the {{c1::forward}} reaction is favoured (too few products — build them up).",
     "R2.3.5 AHL — Q behind the target → catch up forward"),
    ("If Q &gt; K, the {{c1::reverse}} reaction is favoured (too many products — break them down).",
     "R2.3.5 AHL — Q overshot → come back"),
    ("If Q = K, the system is {{c1::at equilibrium}} — forward and reverse proceed at the same rate.",
     "R2.3.5 AHL — compass needle on target"),
    ("Worked example: N₂+3H₂ ⇌ 2NH₃, K = 0.59, all species at 0.50 mol dm⁻³ → Q = {{c1::4.0}} &gt; K → {{c2::reverse}} favoured.",
     "R2.3.5 AHL — 0.5²/(0.5 × 0.5³) = 0.25/0.0625 = 4.0"),
    # ---- R2.3.6 ICE calculations (AHL) ----
    ("2SO₂ + O₂ ⇌ 2SO₃, K = 3.0: equilibrium [SO₂] = 0.12, [SO₃] = 0.18 → [O₂] = {{c1::0.75}} mol dm⁻³.",
     "R2.3.6 AHL — 3.0 = 0.18²/([O₂] × 0.12²)"),
    ("Same system: initial [SO₂] = {{c1::0.30}}, initial [O₂] = {{c2::0.84}} mol dm⁻³ (each mole of SO₃ uses 1 SO₂ + ½ O₂).",
     "R2.3.6 AHL — 0.12 + 0.18; 0.75 + 0.09"),
    ("An ICE table row is: {{c1::Initial / Change / Equilibrium}} — the change row follows the {{c2::stoichiometric ratios}} exactly.",
     "R2.3.6 AHL — the ledger of concentrations"),
    ("For weak acids/bases, tiny K means [HA]ₑq ≈ [HA]ᵢₙᵢₜᵢₐₗ, so K ≈ {{c1::x²/[HA]₀}} — no quadratic needed (quadratics NOT assessed in DP).",
     "R2.3.6 AHL — the weak-acid shortcut"),
    ("Worked example: CH₃COOH, K = 1.74 × 10⁻⁵, 0.100 mol dm⁻³ → [H⁺] = [CH₃COO⁻] = {{c1::1.32 × 10⁻³}} mol dm⁻³.",
     "R2.3.6 AHL — x = √(1.74×10⁻⁵ × 0.100) = √(1.74×10⁻⁶)"),
    ("Practice: phenylamine (aniline), Kb = 7.41 × 10⁻¹⁰, 0.100 mol dm⁻³ → [OH⁻] = {{c1::8.6 × 10⁻⁶}} mol dm⁻³.",
     "R2.3.6 AHL — √(7.41×10⁻¹⁰ × 0.100)"),
    ("Esterification: 1.00 mol acid + 2.00 mol ethanol in 1 dm³, 0.60 mol reacts → K = (0.60×0.60)/(0.40×1.40) = {{c1::0.64}}.",
     "R2.3.6 AHL — book Q13; then Q = 1 &gt; K → hydrolysis favoured at equal concentrations"),
    ("Esterification data trend: K decreases as the alcohol or acid gets {{c1::longer / more branched}} — steric hindrance makes ester formation harder.",
     "R2.3.6 AHL — methanol+ethanoic 5.03 → 2-methylpropan-1-ol+butanoic 0.92"),
    # ---- R2.3.7 K and Gibbs (AHL) ----
    ("The bridge between K and spontaneity: ΔG° = {{c1::−RT ln K}}.",
     "R2.3.7 AHL — R = 8.31 J K⁻¹ mol⁻¹, T in kelvin, ΔG° in J (convert from kJ!)"),
    ("K &gt; 1 ⇔ ΔG° {{c1::&lt; 0}} ⇔ forward reaction spontaneous under standard conditions.",
     "R2.3.7 AHL — products win ⇔ negative Gibbs"),
    ("K &lt; 1 ⇔ ΔG° {{c1::&gt; 0}} ⇔ reverse reaction spontaneous; K = 1 ⇔ ΔG° = {{c2::0}} (neither favoured).",
     "R2.3.7 AHL — the three-way correspondence"),
    ("Worked example: 2NO ⇌ N₂O₂, K = 1.39 × 10⁻⁵ at 298 K → ΔG° = {{c1::+27.7 kJ mol⁻¹}}.",
     "R2.3.7 AHL — −8.31 × 298 × ln(1.39×10⁻⁵) = +27 700 J — positive, reverse favoured"),
    ("Using ΔGf(NO) = 87.6 kJ mol⁻¹, ΔGf(N₂O₂) = {{c1::+202.9 kJ mol⁻¹}} — hugely positive, so N₂O₂ is unstable.",
     "R2.3.7 AHL — 27.7 = −(2 × 87.6) + ΔGf(N₂O₂)"),
    ("Standard Gibbs energy ΔG° refers to reactants → products in {{c1::standard states}} (100 kPa gases / 1 mol dm⁻³ aqueous) at a given temperature (298 K if unspecified).",
     "R2.3.7 AHL — the 'standard' in ΔG°"),
    ("Activity: ΔG° = −3.9 kJ mol⁻¹ at 298 K → K = {{c1::4.8}} (e^(3900/(8.31 × 298))).",
     "R2.3.7 AHL — negative ΔG° must give K &gt; 1 ✓"),
    ("GDC trick: solving ΔG° = −RT ln K numerically — enter ΔG° in {{c1::joules}} (e.g. −0.82 kJ → −820 J) into nSolve / graph intersection.",
     "R2.3.7 AHL — book p.532: K = 1.39 from −820 J"),
    ("End-of-topic check: H₂ + I₂ ⇌ 2HI at 760 K, [H₂] = 0.012, [I₂] = 0.015, [HI] = 0.091 → K = {{c1::46.0}}; at 715 K, K = 48.0 → forward reaction is {{c2::exothermic}} (K decreases as T rises).",
     "R2.3.7 + R2.3.4 — 0.091²/(0.012 × 0.015) = 46.0"),
]

deck = genanki.Deck(DECK_ID, SUBJECT_DECK)
for text, back in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, back]))
genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
