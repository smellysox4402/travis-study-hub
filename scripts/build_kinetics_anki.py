#!/usr/bin/env python3
"""Anki cloze deck builder: Chem HL — Kinetics (Reactivity 2.2).
Matches the user's 'Cloze+' model (Text + Back Extra) in the 'Chem HL' deck.
Run: python scripts/build_kinetics_anki.py
"""
import genanki, os

MODEL_ID = 1607392319   # same model as bio topics (Cloze+)
DECK_ID  = 2059400112   # Chem HL deck (distinct from Bio HL 2059400110)
SUBJECT_DECK = "Chem HL"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics",
                   "chem", "kinetics", "Chem_Kinetics.apkg")

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
    # ---- R2.2.1 / R2.2.2 rate definition & measurement ----
    ("Rate of reaction is the change in {{c1::concentration}} of a reactant or product per unit {{c2::time}}.",
     "rate = Δ[c]/Δt · units mol dm⁻³ s⁻¹ (R2.2.1)"),
    ("The {{c1::instantaneous}} rate of reaction is the gradient of the {{c2::tangent}} to the concentration–time curve.",
     "Initial rate = tangent at t = 0 (R2.2.2)"),
    ("The initial rate of reaction is the gradient of the tangent at {{c1::t = 0}}.",
     "The steepest, cleanest point — standard exam ask (R2.2.2)"),
    ("Methods to measure rate: gas {{c1::syringe}} (volume), loss of {{c1::mass}}, {{c2::colorimetry}}, titration, pH, conductivity.",
     "Every method secretly gives [c] vs time (R2.2.2)"),
    # ---- R2.2.3 collision theory ----
    ("For a reaction to occur, particles must collide with the correct {{c1::orientation}} and energy ≥ {{c2::Eₐ (activation energy)}}.",
     "The bouncer's three rules: collide · orient · energy (R2.2.3)"),
    ("Rate depends on the frequency of {{c1::successful}} collisions, not all collisions.",
     "Only collisions passing all three checks count (R2.2.3)"),
    ("The three requirements for a successful collision: {{c1::collision}}, correct {{c1::orientation}}, energy ≥ {{c1::Eₐ}}.",
     "Miss any one → no reaction (R2.2.3)"),
    # ---- R2.2.4 activation energy ----
    ("Activation energy Eₐ is the {{c1::minimum}} energy that colliding particles need for a reaction to occur.",
     "The bouncer's strength check (R2.2.4)"),
    ("At the transition state, bonds are {{c1::half-broken and half-formed}} — the {{c2::highest energy}} point of the reaction.",
     "Also called the activated complex — fleeting, not stable (R2.2.4)"),
    ("Eₐ is the energy hill to climb; ΔH is the overall {{c1::energy difference between reactants and products}}.",
     "You can have exothermic ΔH with huge Eₐ — petrol + O₂ needs a spark (R2.2.4)"),
    # ---- R2.2.5 catalysts ----
    ("A catalyst increases rate by providing an {{c1::alternative pathway}} with {{c2::lower activation energy}}.",
     "VIP pass — smaller hill, same destination (R2.2.5)"),
    ("A catalyst is {{c1::regenerated unchanged}} — it is both a reactant and a product.",
     "Not consumed! (R2.2.5)"),
    ("A catalyst changes Eₐ and k but does NOT change {{c1::ΔH}}.",
     "Start and finish are the same; only the hill gets smaller (R2.2.5)"),
    ("A {{c1::reaction intermediate}} is a species that can exist briefly (pencil on its flat end); a {{c2::transition state}} cannot (pencil on its tip).",
     "Intermediate = valley · transition state = peak (R2.2.5)"),
    # ---- R2.2.6 factors ----
    ("Increasing concentration increases rate because there are {{c1::more collisions per second}}.",
     "More guests per volume (R2.2.6)"),
    ("Increasing pressure increases rate for {{c1::gases}} — same reason as concentration.",
     "Particles squeezed closer together (R2.2.6)"),
    ("Increasing surface area (crushing a solid) increases rate because {{c1::more particles are exposed}} → more collision sites.",
     "One lump vs powder (R2.2.6)"),
    ("Rate roughly {{c1::doubles to quadruples}} for every +10 °C (0–100 °C).",
     "Temperature is the biggest lever (R2.2.6)"),
    ("Temperature increases rate for TWO reasons: more collisions AND {{c1::a bigger share of particles with E ≥ Eₐ}}.",
     "The M–B tail — see Act 3 (R2.2.6)"),
    # ---- R2.2.7 Maxwell-Boltzmann ----
    ("On a Maxwell–Boltzmann curve, the area under the curve represents {{c1::the total number of particles}}.",
     "Same area at any temperature (R2.2.7)"),
    ("At higher temperature the M–B curve becomes {{c1::flatter and broader}}, with the peak {{c2::lower and shifted right}}.",
     "Redistribution, not more particles (R2.2.7)"),
    ("Raising temperature does not change {{c1::Eₐ}}; it increases the {{c2::average kinetic energy}}.",
     "The crowd moves, the bouncer's line stays (R2.2.7)"),
    ("A catalyst does not change the M–B curve shape; it moves the {{c1::Eₐ threshold}} left so more particles can react.",
     "Same crowd photo, easier door (R2.2.7)"),
    # ---- R2.2.8 rate equation ----
    ("The rate equation is rate = {{c1::k [A]ⁿ [B]ᵐ}}.",
     "k = rate constant · n,m = orders · overall = n+m (R2.2.8)"),
    ("The rate constant k is independent of {{c1::concentration}} but changes with {{c2::temperature}} and {{c2::catalyst}}.",
     "The bouncer's mood (R2.2.8)"),
    ("For rate = k[A]², the units of k are {{c1::mol⁻¹ dm³ s⁻¹}}.",
     "Work out: mol dm⁻³ s⁻¹ ÷ (mol dm⁻³)² (R2.2.8)"),
    ("For a first-order reaction (rate = k[A]), the units of k are {{c1::s⁻¹}}.",
     "mol dm⁻³ s⁻¹ ÷ mol dm⁻³ (R2.2.8)"),
    # ---- R2.2.9 orders ----
    ("Reaction orders are determined {{c1::experimentally}} — never from the {{c2::balanced equation}}.",
     "THE biggest kinetics trap (R2.2.9)"),
    ("If doubling [A] leaves the rate unchanged, the order in A is {{c1::zero}}.",
     "[A]⁰ = 1 — doesn't appear in the rate equation (R2.2.9)"),
    ("If doubling [A] doubles the rate, the order in A is {{c1::first}}.",
     "rate ∝ [A] (R2.2.9)"),
    ("If doubling [A] quadruples the rate, the order in A is {{c1::second}}.",
     "rate ∝ [A]² (R2.2.9)"),
    ("The {{c1::initial rates}} method finds orders by changing ONE concentration while holding the others fixed.",
     "Isolate each reactant's power one at a time (R2.2.9)"),
    # ---- R2.2.10 rate-determining step ----
    ("The rate-determining step is the {{c1::slowest step}} of a multi-step mechanism.",
     "The club moves as fast as its slowest bouncer (R2.2.10)"),
    ("The rate equation reflects the reactants in the {{c1::rate-determining step}} (and any fast step feeding it) — not the overall equation.",
     "2NO₂ + F₂ example: rate = k[NO₂][F₂] (R2.2.10)"),
    ("{{c1::Intermediates}} never appear in the rate equation.",
     "Made and used within the mechanism (R2.2.10)"),
    # ---- R2.2.11 Arrhenius ----
    ("The Arrhenius equation is k = {{c1::A·e^(−Eₐ/RT)}}.",
     "A = frequency factor · Eₐ in J mol⁻¹ · T in kelvin (R2.2.11)"),
    ("In the Arrhenius equation, A (the frequency factor) measures how often collisions happen with the {{c1::right orientation}}.",
     "Big A = simple symmetric particles; small A = big awkward molecules (R2.2.11)"),
    ("In the Arrhenius equation, Eₐ must be in {{c1::J mol⁻¹}} and T in {{c2::kelvin}}.",
     "Convert kJ → J (×1000) before plugging in (R2.2.11)"),
    ("The rate constant k rises {{c1::exponentially}} with temperature.",
     "That's the +10 °C doubling in disguise (R2.2.11)"),
    # ---- R2.2.12 Arrhenius plot ----
    ("Plotting {{c1::ln k}} against {{c2::1/T}} gives a straight line with gradient −Eₐ/R.",
     "Do NOT plot ln k vs T — that's a curve (R2.2.12)"),
    ("On an Arrhenius plot, the y-intercept equals {{c1::ln A}}.",
     "A = e^(intercept) (R2.2.12)"),
    ("From an Arrhenius plot, Eₐ = {{c1::−gradient × R}}.",
     "gradient is in K, R = 8.31 J K⁻¹ mol⁻¹ (R2.2.12)"),
    # ---- R2.2.13 Ea from data ----
    ("The two-point Arrhenius form (no graph needed): ln(k₁/k₂) = {{c1::(Eₐ/R)(1/T₂ − 1/T₁)}}.",
     "If concentrations constant, rates can stand in for k (R2.2.13)"),
    ("Worked example: N₂O₅ decomposition gave gradient −12 500 K → Eₐ = {{c1::104 kJ mol⁻¹}} and A = {{c2::2.85 × 10¹³ s⁻¹}}.",
     "12 500 × 8.31 = 103 875 J mol⁻¹ ≈ 104 kJ (R2.2.13)"),
]

deck = genanki.Deck(DECK_ID, SUBJECT_DECK)
for text, back in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, back]))
genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
