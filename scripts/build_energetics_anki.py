#!/usr/bin/env python3
"""Anki cloze deck builder: Chem HL — Energetics & Thermochemistry (Reactivity 1).
Matches the user's 'Cloze+' model (Text + Back Extra) in the 'Chem HL' deck.
Run: python scripts/build_energetics_anki.py
"""
import genanki, os

MODEL_ID = 1607392319   # same model as bio topics (Cloze+)
DECK_ID  = 2059400112   # Chem HL deck (distinct from Bio HL 2059400110)
SUBJECT_DECK = "Chem HL"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics",
                   "chem", "energetics", "Chem_Energetics.apkg")

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
    # ---- R1.1.1 / R1.1.2 system & energy transfer ----
    ("The universe = the {{c1::system}} + the {{c2::surroundings}}; in any chemical reaction total energy is {{c3::conserved}}.",
     "R1.1.1 — system = reacting chemicals, surroundings = everything else"),
    ("In an {{c1::open}} system both matter and energy cross the boundary; in an {{c2::isolated}} system neither does.",
     "Closed = energy only (R1.1.1)"),
    ("An {{c1::exothermic}} reaction releases heat to the surroundings (ΔH {{c2::&lt; 0}}, mixture warms).",
     "EXit = EXothermic (R1.1.2)"),
    ("An {{c1::endothermic}} reaction absorbs heat from the surroundings (ΔH {{c2::&gt; 0}}, mixture cools).",
     "EnTER = ENdothermic (R1.1.2) — e.g. NH₄NO₃ dissolving feels cold"),
    # ---- R1.1.3 relative stability ----
    ("In an exothermic reaction the products are {{c1::more stable}} than the reactants (lower enthalpy).",
     "Lower energy = more stable = ball rolls downhill (R1.1.3)"),
    ("Activation energy Eₐ is {{c1::NOT}} the same as ΔH — Eₐ is the hill to climb, ΔH is the net drop/rise.",
     "Petrol + O₂ is hugely exothermic but needs a spark — big Eₐ (R1.1.3)"),
    # ---- R1.1.4 q = mcΔT ----
    ("The heat absorbed or released by a substance: q = {{c1::mcΔT}}, where c = {{c2::specific heat capacity}}.",
     "c(water) = 4.18 kJ kg⁻¹ K⁻¹ (R1.1.4)"),
    ("ΔH = {{c1::−q/n}} — the minus because heat gained by the water = heat lost by the reaction.",
     "Worked ex: LiCl → ΔH = −14.6 kJ mol⁻¹ (R1.1.4)"),
    ("STP = {{c1::273.15 K}} and 100 kPa; SATP = {{c2::298.15 K}} and 100 kPa.",
     "Standard conditions for ΔH° (R1.1.4)"),
    ("A coffee-cup calorimeter measures ΔH for {{c1::solution}} reactions (neutralisation, displacement); a bomb calorimeter measures {{c2::combustion}}.",
     "Bomb = sealed steel chamber + O₂ (R1.1.4)"),
    ("Heat loss to the surroundings makes the measured |ΔH| come out {{c1::too small}} (systematic error); fix by {{c2::insulating}} + extrapolating the cooling line back to mixing time.",
     "Spirit-burner methanol: −359 vs true −726 kJ mol⁻¹ (R1.1.4)"),
    ("In calorimetry ALWAYS check the {{c1::limiting reactant}} before dividing q by n.",
     "Zn + CuSO₄: n(Zn) = 0.0210 &lt; n(CuSO₄) = 0.0250 → Zn limits (R1.1.4)"),
    # ---- R1.2.1 bond enthalpies ----
    ("Bond-{{c1::breaking}} absorbs energy (endothermic); bond-{{c2::forming}} releases energy (exothermic).",
     "R1.2.1"),
    ("ΔH from bond enthalpies = Σ(bonds {{c1::broken}}) − Σ(bonds {{c2::formed}}).",
     "Average bond enthalpies = data booklet section 12 (R1.2.1)"),
    # ---- R1.2.2 Hess ----
    ("Hess's law: the enthalpy change for a reaction is {{c1::independent of the pathway}} between initial and final states.",
     "Enthalpy is a state function (R1.2.2)"),
    ("Hess's law works because of the law of {{c1::conservation of energy}}.",
     "Two routes with different ΔH would create/destroy energy (R1.2.2)"),
    # ---- R1.2.3 formation & combustion ----
    ("Standard enthalpy of combustion ΔHc° = 1 mole burned {{c1::completely in oxygen}}, standard states (data booklet section 14).",
     "C₄H₁₀: −2878 kJ mol⁻¹ (R1.2.3)"),
    ("Standard enthalpy of formation ΔHf° = 1 mole formed {{c1::from its elements in standard states}} (section 13).",
     "ΔHf(butane) = −126 kJ mol⁻¹ (R1.2.3)"),
    ("Elements in their standard states have ΔHf = {{c1::0}}; carbon's standard allotrope is {{c2::graphite}}.",
     "Diamond and buckminsterfullerene have nonzero ΔHf (R1.2.3)"),
    ("{{c1::Fractional}} stoichiometric coefficients ARE allowed in combustion/formation equations (e.g. ½O₂).",
     "One of the few places fractions are correct (R1.2.3)"),
    # ---- R1.2.4 Hess applications ----
    ("ΔH° = ΣΔHf°({{c1::products}}) − ΣΔHf°({{c2::reactants}}).",
     "Formation formula (R1.2.4)"),
    ("ΔH° = ΣΔHc°({{c1::reactants}}) − ΣΔHc°({{c2::products}}).",
     "Combustion formula — swapped, because combustion drops to CO₂ + H₂O (R1.2.4)"),
    ("Worked example: ΔHf of pentane from combustion data = 5(−394) + 6(−286) + 3509 = {{c1::−177 kJ mol⁻¹}} (book −173 — bond-enthalpy averaging explains the difference).",
     "Reverse pentane's combustion → flip sign to +3509 (R1.2.4)"),
    ("Worked example: ΔHc of pentane from formation data = +173 + 5(−394) + 6(−286) = {{c1::−3513 kJ mol⁻¹}}.",
     "Reverse pentane's formation → +173 (R1.2.4)"),
    # ---- R1.2.5 Born-Haber (AHL) ----
    ("Enthalpy of atomization ΔHat: M(s) → M(g), endothermic; for a diatomic gas it equals {{c1::½ of the bond enthalpy}}.",
     "R1.2.5 AHL"),
    ("Ionization energy IE is {{c1::endothermic}} (M(g) → M⁺(g) + e⁻); electron affinity EA is usually {{c2::exothermic}} (X(g) + e⁻ → X⁻(g)).",
     "Exceptions to EA negative: He, N; 2nd EA of O is positive (R1.2.5)"),
    ("In DP chemistry, lattice enthalpy is defined as {{c1::MX(s) → M⁺(g) + X⁻(g)}} — lattice breaking — so it is always {{c2::positive}}.",
     "Formation of gaseous ions FROM the solid lattice (R1.2.5)"),
    ("Worked example: ΔHlattice(KBr) = −(−392) + 89 + 419 + 112 + (−325) = {{c1::+687 kJ mol⁻¹}}.",
     "Reverse formation (−392 → +392), then atomize, ionize, atomize, add e⁻ (R1.2.5)"),
    ("A Born–Haber cycle is just {{c1::Hess's law}} applied to the formation of an {{c2::ionic compound}}.",
     "Sum around the loop = 0 — solve for the unknown step (R1.2.5)"),
    ("Lattice enthalpy increases with {{c1::higher ionic charges}} and {{c2::smaller ionic radii}}.",
     "Charge × charge / distance — MgO &gt; NaCl (R1.2.5)"),
    # ---- R1.3.1 combustion ----
    ("Combustion of a reactive metal: 4Li + O₂ → 2Li₂O — the metal is {{c1::oxidized}} (loses e⁻), oxygen is {{c2::reduced}}.",
     "Redox! (R1.3.1)"),
    ("Combustion of sulfur: S + O₂ → SO₂, then 2SO₂ + O₂ → 2SO₃, then SO₃ + H₂O → {{c1::H₂SO₄}}.",
     "The acid-rain cascade — and industrial sulfuric acid (R1.3.1)"),
    ("General complete combustion of an alkane CₙH₂ₙ₊₂: → nCO₂ + {{c1::(n+1)H₂O}}.",
     "C₈H₁₈: −5470 kJ mol⁻¹ (R1.3.1)"),
    ("A fuel must be {{c1::volatile}} (vaporize easily) to burn; short-chain alkanes are more volatile → better fuels.",
     "LPG = mostly propane (R1.3.1)"),
    # ---- R1.3.2 incomplete combustion ----
    ("Incomplete combustion (limited O₂) produces {{c1::CO (carbon monoxide)}} and/or {{c2::C (soot)}}.",
     "CO binds haemoglobin irreversibly — odourless killer (R1.3.2)"),
    ("Incomplete combustion releases {{c1::less}} energy than complete combustion.",
     "Sooty flame = wasted fuel (R1.3.2)"),
    # ---- R1.3.3 fossil fuels ----
    ("The three fossil fuels: {{c1::coal}}, {{c1::crude oil}} and {{c1::natural gas}} — all non-renewable.",
     "Natural gas has the highest specific energy (R1.3.3)"),
    ("CO₂ is a greenhouse gas because it absorbs {{c1::infrared}} radiation and re-emits some back to Earth; N₂ and O₂ (99%+ of air) do {{c2::not}}.",
     "Greenhouse effect → global warming (R1.3.3)"),
    # ---- R1.3.4 biofuels ----
    ("Biofuels are produced from {{c1::biological carbon fixation}} — photosynthesis over a short timescale, not ancient carbon.",
     "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ (R1.3.4)"),
    ("Fermentation: C₆H₁₂O₆ → {{c1::2C₂H₅OH + 2CO₂}}.",
     "Glucose → ethanol biofuel (R1.3.4)"),
    ("Two disadvantages of biofuels: {{c1::agricultural land/food competition}} and {{c2::high production cost}}.",
     "Also monocultures, deforestation, biodiversity loss (R1.3.4)"),
    # ---- R1.3.5 fuel cells ----
    ("A fuel cell converts {{c1::chemical energy directly to electrical energy}}, with fuel supplied {{c2::continuously}} from an external source.",
     "Unlike a voltaic cell with finite reactants (R1.3.5)"),
    ("Hydrogen fuel cell anode: H₂ → {{c1::2H⁺ + 2e⁻}}; cathode: O₂ + 4H⁺ + 4e⁻ → {{c2::2H₂O}}; overall 2H₂ + O₂ → 2H₂O.",
     "PEM lets only H⁺ cross; electrons take the external circuit (R1.3.5)"),
    ("The PEM (proton exchange membrane) allows {{c1::H⁺ ions}} to pass but blocks {{c2::electrons}}.",
     "That's why electrons detour through the external circuit (R1.3.5)"),
    ("H₂ for fuel cells can come from electrolysis of water (clean) or {{c1::steam reforming}} of hydrocarbons (produces CO + CO₂).",
     "The fossil-fuel catch (R1.3.5)"),
    ("A direct-methanol fuel cell (DMFC) has higher {{c1::energy density}} than hydrogen gas or Li-ion batteries, but methanol is {{c2::toxic}} and needs precious-metal catalysts.",
     "CH₃OH + ³⁄₂O₂ → CO₂ + 2H₂O — emits CO₂ (R1.3.5)"),
    # ---- R1.4.1 entropy (AHL) ----
    ("Entropy S is a measure of the {{c1::dispersal/distribution of matter and/or energy}} in a system.",
     "\"Disorder\" is shorthand — say dispersal/distribution (R1.4.1)"),
    ("Under the same conditions: S({{c1::gas}}) &gt; S({{c2::liquid}}) &gt; S({{c3::solid}}).",
     "More freedom of movement → more ways to distribute energy (R1.4.1)"),
    ("Second law: a reaction is spontaneous if ΔS{{c1::total}} &gt; 0, where ΔS_total = ΔS_system + ΔS_surroundings.",
     "= 0 equilibrium · &lt; 0 → reverse is spontaneous (R1.4.1)"),
    ("To predict ΔS: {{c1::moles of gas}} dominate — more gas on the product side → ΔS &gt; 0.",
     "NH₄Cl(s) → NH₃ + HCl: ΔS &gt; 0 ✓ (R1.4.1)"),
    ("ΔS° = ΣS°(products) − ΣS°(reactants); standard entropy units are {{c1::J K⁻¹ mol⁻¹}}.",
     "H₂ + Cl₂ → 2HCl: (2×187) − (131+223) = +20 J K⁻¹ mol⁻¹ (R1.4.1)"),
    # ---- R1.4.2 / 1.4.3 Gibbs (AHL) ----
    ("The Gibbs equation: ΔG = {{c1::ΔH − TΔS}}.",
     "Watch units — ΔS in kJ (÷1000) before ×T (R1.4.2)"),
    ("At constant pressure, a change is spontaneous if ΔG is {{c1::negative}}.",
     "R1.4.3"),
    ("ΔH &lt; 0 and ΔS &gt; 0 → spontaneous {{c1::at any temperature}}; ΔH &gt; 0 and ΔS &lt; 0 → {{c2::never}} spontaneous.",
     "The two easy rows of the sign table (R1.4.3)"),
    ("For ΔH &gt; 0, ΔS &gt; 0 the reaction becomes spontaneous when {{c1::TΔS &gt; ΔH}} — flip temperature T = {{c2::ΔH/ΔS}}.",
     "CH₄ + H₂O → 3H₂ + CO: T = 205/0.216 = 949 K (R1.4.3)"),
    ("Spontaneous (ΔG &lt; 0) does NOT mean fast — the reaction may be kinetically blocked by a {{c1::high activation energy}}.",
     "Diamond → graphite has ΔG &lt; 0 but Eₐ is enormous (R1.4.3)"),
    # ---- R1.4.4 equilibrium (AHL) ----
    ("As a reaction approaches equilibrium, ΔG becomes {{c1::less negative}} and finally reaches {{c2::zero}}.",
     "R1.4.4"),
    ("ΔG = ΔG° + RT ln Q; at equilibrium ΔG = 0 and Q = K, so ΔG° = {{c1::−RT ln K}}.",
     "R = 8.31 J K⁻¹ mol⁻¹ — convert ΔG° to joules (R1.4.4)"),
    ("If K &gt; 1, products are favoured and ΔG° is {{c1::negative}}.",
     "K = 1 → ΔG° = 0 · K &lt; 1 → ΔG° &gt; 0 (R1.4.4)"),
    ("Worked example (Haber): N₂ + 3H₂ ⇌ 2NH₃ with ΔH = −92 kJ mol⁻¹, ΔS = −202 J K⁻¹ mol⁻¹ → ΔG at 298 K = {{c1::−31.8 kJ mol⁻¹}} (spontaneous), K = {{c2::3.77 × 10⁵}}.",
     "ln K = 31800/(8.31 × 298) → K huge → products strongly favoured (R1.4.4)"),
]

deck = genanki.Deck(DECK_ID, SUBJECT_DECK)
for text, back in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, back]))
genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
