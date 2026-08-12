#!/usr/bin/env python3
"""Anki cloze deck builder: Chem HL — Redox (Reactivity 3.2).
Matches the user's 'Cloze+' model (Text + Back Extra) in the 'Chem HL' deck.
Run: python scripts/build_redox_anki.py
"""
import genanki
import os

MODEL_ID = 1607392319
DECK_ID = 2059400112
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "chem", "redox", "Chem_Redox.apkg")

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

# ── R3.2.1 · Definitions ──
add("OIL RIG: Oxidation Is {{c1::Loss}} (of electrons); Reduction Is {{c2::Gain}}.",
    "2Na → 2Na⁺ + 2e⁻ (oxidized); Cl₂ + 2e⁻ → 2Cl⁻ (reduced).")
add("Oxidation state = {{c1::the charge an atom would have if the compound were ionic}} (all polar covalent bonds treated as ionic, electrons formally given to the more electronegative atom).",
    "C(s) + 2S(s) → CS₂: C 0 → +4 (oxidized), S 0 → −2 (reduced). Some redox reactions (like CS₂) have no electron transfer — hence the oxidation-state definition.")
add("An oxidizing agent {{c1::causes oxidation of another species and is itself reduced}}. A reducing agent {{c2::causes reduction and is itself oxidized}}.",
    "Describe compounds, not atoms: in Fe + 2HBr → FeBr₂ + H₂, HBr(aq) is reduced and is the oxidizing agent.")
add("Disproportionation: {{c1::one species is simultaneously oxidized AND reduced}}. Example: {{c2::4KClO₃ → 3KClO₄ + KCl}}.",
    "Cl goes +5 → +7 (KClO₄) and +5 → −1 (KCl).")
add("Oxidation in the oxygen view = {{c1::gains oxygen}} (2Mg + O₂ → 2MgO); reduction = {{c2::loses oxygen}} (CuO + H₂ → Cu + H₂O).",
    "Hydrogen view: oxidation = loses H; reduction = gains H (C₂H₄ + H₂ → C₂H₆).")

# ── R3.2.2 · Half-equations ──
add("Half-equation balancing in ACIDIC solution: balance O with {{c1::H₂O}}, then balance H with {{c2::H⁺}}.",
    "In basic/neutral: balance O with OH⁻, H with H₂O. Final check: total charge = zero.")
add("Balance: Fe²⁺ + Cr₂O₇²⁻ → Fe³⁺ + Cr³⁺ (acidic): {{c1::6Fe²⁺ + Cr₂O₇²⁻ + 14H⁺ → 6Fe³⁺ + 2Cr³⁺ + 7H₂O}}.",
    "Cr +6 → +3 gains 6e⁻; each Fe loses 1e⁻ (×6). Charge: LHS 12−2+14 = 24; RHS 18+6 = 24 ✓.")
add("The 10-step method: split into half-equations, balance atoms, electrons on {{c1::RHS for oxidation}} / {{c2::LHS for reduction}}, then make electrons {{c3::lost = gained}}, add, cancel, balance O and H, check charge.",
    "States of reactants may be omitted while working, but must appear in the final equation.")

# ── R3.2.3 · Relative ease ──
add("Halogen oxidizing power: {{c1::F₂ > Cl₂ > Br₂ > I₂}} — increases {{c2::UP}} the group.",
    "Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂ (works); Cl₂ + 2F⁻ → no reaction (F₂ stronger).")
add("Group 1 metals: ease of oxidation increases {{c1::DOWN}} the group: Li &lt; Na &lt; K &lt; Rb &lt; Cs.",
    "They are reducing agents (lose the valence electron easily).")
add("Metal displacement: Zn + Cu²⁺ → Zn²⁺ + Cu. {{c1::Zn}} is the stronger reducing agent (more easily oxidized); {{c1::Cu²⁺}} is the stronger oxidizing agent.",
    "Blue Cu²⁺ solution goes colourless, red-brown copper precipitates. If a pure metal reacts, it's more easily oxidized than the metal in solution.")
add("The activity series (most easily oxidized first): {{c1::K Na Ca Mg Al Zn Fe Sn Pb (H) Cu Ag Au Pt}}.",
    "Metals above H react with common acids; those below cannot.")

# ── R3.2.4 · Acids + metals ──
add("Reactive metals + dilute acids → {{c1::salt + hydrogen gas}}. Zn + 2HCl → {{c2::ZnCl₂ + H₂}}.",
    "Zn: 0 → +2 (oxidized, reducing agent); H: +1 → 0 (reduced, acid = oxidizing agent). Pop test confirms H₂.")
add("Cu and Ag do not react with dilute common acids because {{c1::they are below hydrogen in the activity series}}.",
    "Gold sits at the bottom — found elemental in nature; 'impossible to pan for lithium' because it's at the top.")

# ── R3.2.5 · Electrochemical cells ──
add("RED CAT: {{c1::REDuction at CAThode}}. Oxidation is always at the {{c2::anode}}.",
    "Applies to voltaic AND electrolytic cells.")
add("The salt bridge (e.g. {{c1::KNO₃, Na₂SO₄}}) lets {{c2::cations flow to the cathode side and anions to the anode side}}, neutralizing charge so the cell keeps running.",
    "Without it: electrons leave Zn (+ charge) and pile at Cu (− charge) → polarization stops the cell.")
add("Cell diagram: anode | anode ion || cathode ion | cathode. The {{c1::||}} is the salt bridge. Daniell cell: {{c2::Zn(s) | Zn²⁺(aq) || Cu²⁺(aq) | Cu(s)}}.",
    "Cathode always written on the right. Electrons flow anode → cathode through the wire.")

# ── R3.2.6 · Primary cells ──
add("A primary (voltaic) cell converts {{c1::energy from spontaneous redox reactions}} into {{c2::electrical energy}}.",
    "Galvani: frog legs twitch (two metals + moist tissue). Volta: first battery (voltaic pile). Daniell cell: Zn anode (−) in ZnSO₄, Cu cathode (+) in CuSO₄.")
add("As the Daniell cell runs: the blue colour of CuSO₄ {{c1::fades}}, the copper bar {{c2::grows}}, and the zinc bar {{c3::thins}}.",
    "Discharge: Zn → Zn²⁺ + 2e⁻ (anode); Cu²⁺ + 2e⁻ → Cu (cathode). Cell stops when significant Zn²⁺ builds up on the cathode side.")

# ── R3.2.7 · Secondary cells ──
add("Secondary (rechargeable) cells involve redox reactions that {{c1::can be reversed using electrical energy}}.",
    "Primary cells: reactants consumed, irreversible. Secondary cells have higher self-discharge (new phone batteries arrive partly discharged).")
add("Lead-acid battery discharge: Pb + PbO₂ + 2H₂SO₄ → {{c1::2PbSO₄ + 2H₂O}}. Charging is the {{c2::reverse}}.",
    "Anode: Pb + HSO₄⁻ → PbSO₄ + H⁺ + 2e⁻; cathode: PbO₂ + 3H⁺ + HSO₄⁻ + 2e⁻ → PbSO₄ + 2H₂O.")
add("Lithium-ion battery: anode = {{c1::Li atoms in a graphite lattice}}, cathode = {{c2::LiCoO₂}}, medium is {{c3::non-aqueous}} (lithium reacts violently with water).",
    "Discharge: Li → Li⁺ + e⁻; Li⁺ + e⁻ + CoO₂ → LiCoO₂. Battery flat when no Li⁺ remain on the anode.")
add("Hydrogen fuel cell overall: {{c1::2H₂ + O₂ → 2H₂O}}. The PEM (proton exchange membrane) lets {{c2::H⁺ diffuse but blocks other ions, electrons and molecules}}.",
    "Anode: H₂ → 2H⁺ + 2e⁻; cathode: O₂ + 4H⁺ + 4e⁻ → 2H₂O. No greenhouse gases. H₂ sources: water electrolysis (clean) or methane reforming CH₄ + H₂O → 3H₂ + CO.")
add("Direct methanol fuel cell (DMFC) overall: {{c1::CH₃OH + 1.5O₂ → CO₂ + 2H₂O}} — advantage: no H₂ extraction; disadvantage: {{c2::produces CO₂}}.",
    "Anode: CH₃OH + H₂O → CO₂ + 6H⁺ + 6e⁻; cathode: 1.5O₂ + 6H⁺ + 6e⁻ → 3H₂O.")

# ── R3.2.8 · Electrolytic cells ──
add("An electrolytic cell converts {{c1::electrical energy into chemical energy}} by bringing about {{c2::non-spontaneous}} reactions.",
    "Electrolysis = process. Electrolyte = molten or aqueous ionic compound with free-moving ions. DC source, cathode + anode dipped in electrolyte.")
add("Electrolysis of molten NaCl: cathode {{c1::Na⁺ + e⁻ → Na(l)}}; anode {{c1::2Cl⁻ → Cl₂(g) + 2e⁻}}; overall {{c1::2NaCl(l) → 2Na(l) + Cl₂(g)}}.",
    "Reactive metals (Li, Mg, Al, Na) obtained by electrolysis of molten salts in an inert atmosphere (they react with oxygen).")
add("Electrolysis of molten PbBr₂: {{c1::Pb²⁺ + 2e⁻ → Pb(l)}} at cathode; {{c1::2Br⁻ → Br₂(g) + 2e⁻}} at anode.",
    "Overall: PbBr₂(l) → Pb(l) + Br₂(g).")

# ── R3.2.9 · Organic oxidation ──
add("Primary alcohol --[O]--> {{c1::aldehyde}} (distillation, alcohol in excess) --[O]--> {{c1::carboxylic acid}} (reflux, oxidizing agent in excess).",
    "R-CH₂OH → R-CHO + H₂O → R-COOH. [O] = oxidizing agent (e.g. acidified K₂Cr₂O₇).")
add("Secondary alcohol --[O]--> {{c1::ketone}}. Tertiary alcohols {{c2::cannot be oxidized}} (no H on the carbon bearing the OH).",
    "R-CH(OH)-R' → R-CO-R' + H₂O. Example: propan-2-ol → propanone; 2-methylpropan-2-ol: no reaction.")

# ── R3.2.10 · Organic reduction ──
add("Ketone --[H]--> {{c1::secondary alcohol}}. Carboxylic acid --[H]--> {{c2::primary alcohol}} (via aldehyde intermediate, usually not isolated).",
    "R-CO-R' → R-CH(OH)-R'; R-COOH → R-CHO → R-CH₂OH. [H] = reducing agent.")
add("Reducing agents: {{c1::LiAlH₄}} reduces everything (including carboxylic acids); {{c1::NaBH₄}} reduces {{c2::aldehydes and ketones only}}.",
    "Van Gogh's 'The Bedroom at Arles' yellow = lead chromate PbCrO₄, fading via redox — chemists + art historians collaborate.")

# ── R3.2.11 · Alkenes/alkynes ──
add("Reduction of unsaturated compounds by H₂ {{c1::lowers the degree of unsaturation}}. Alkyne → alkene needs {{c2::deactivated Pd}}; alkene → alkane needs {{c2::Ni or Pt}}.",
    "R-C≡C-R' + H₂ → alkene; R-CH=CH-R'' + H₂ → R-CH₂-CH₂-R''.")
add("With EXCESS H₂, an alkyne goes straight to the {{c1::alkane}}: R-C≡C-R' + 2H₂ → R-CH₂-CH₂-R'.",
    "Propene + H₂ → propane (C₃H₆ + H₂ → C₃H₈); pent-1-yne + 2H₂ → pentane (C₅H₈ + 2H₂ → C₅H₁₂).")

# ── R3.2.12 · SHE (AHL) ──
add("The standard hydrogen electrode (SHE): {{c1::H⁺(aq) + e⁻ ⇌ ½H₂(g)}}, E° = {{c2::0.00 V}} by convention. Uses an inert {{c3::platinum}} electrode.",
    "Conditions: H₂ at 1 bar, H⁺ at 1.0 mol dm⁻³, 298 K (SATP: 298 K, 100 kPa). Values in data booklet section 19.")
add("More negative E° = {{c1::easier to oxidize}} (stronger reducing agent, higher in activity series). More positive E° = {{c2::easier to reduce}} (stronger oxidizing agent).",
    "Lithium has the greatest ease of oxidation; fluorine the greatest ease of reduction.")
add("E° values: Li⁺/Li {{c1::−3.04 V}}; Zn²⁺/Zn {{c1::−0.76 V}}; Fe²⁺/Fe {{c1::−0.45 V}}; SHE {{c1::0.00 V}}; Cu²⁺/Cu {{c1::+0.34 V}}; Ag⁺/Ag {{c1::+0.80 V}}.",
    "Also: Na⁺/Na −2.71; water −0.83; O₂/H₂O +1.23; Cl₂/Cl⁻ +1.36. Practice: Sn −0.14, Ca −2.87, Al −1.66.")

# ── R3.2.13 · E°cell (AHL) ──
add("E°cell = {{c1::E°(cathode) − E°(anode)}}. A {{c2::positive}} E°cell means the reaction is spontaneous.",
    "Fe/Cu: 0.34 − (−0.45) = +0.79 V. Zn/SHE: 0.00 − (−0.76) = +0.76 V. Cu/Ag: 0.80 − 0.34 = +0.46 V.")
add("When balancing electrons, cell potential is {{c1::NOT multiplied by the balancing coefficient}}.",
    "2Ag⁺ + Cu → 2Ag + Cu²⁺: E°cell = 0.80 − 0.34 = +0.46 V (the Ag value is not doubled).")
add("Cu|Cu²⁺ and Ag|Ag⁺ cell: the cathode is {{c1::Ag (more positive E°)}}; overall {{c2::2Ag⁺ + Cu → 2Ag + Cu²⁺}}; E°cell = {{c3::+0.46 V}}.",
    "Cathode = more positive E°. Anode = more negative E°.")

# ── R3.2.14 · ΔG° = −nFE° (AHL) ──
add("ΔG° = {{c1::−nFE°cell}}; n = {{c2::number of electrons transferred}}; F = Faraday constant = {{c3::9.65 × 10⁴ C mol⁻¹}}.",
    "1 V = 1 J C⁻¹ → product in J mol⁻¹, ÷1000 for kJ. Spontaneous ⇔ E°cell &gt; 0 ⇔ ΔG° &lt; 0.")
add("Zn/SHE cell: E°cell = +0.76 V, n = 2 → ΔG° = {{c1::−1.47 × 10⁵ J mol⁻¹ = −147 kJ mol⁻¹}}.",
    "ΔG° = −2 × (9.65×10⁴) × 0.76 = −1.47×10⁵ J mol⁻¹.")
add("Fe + CuSO₄ cell: ΔG° = −152 kJ mol⁻¹ → E°cell = {{c1::+0.79 V}}.",
    "E°cell = −ΔG°/(nF) = 152000/(2 × 96500) = +0.79 V — matches 0.34 − (−0.45).")

# ── R3.2.15 · Aqueous electrolysis (AHL) ──
add("Reduction of water: H₂O + e⁻ → ½H₂ + OH⁻, E° = {{c1::−0.83 V}}. If the salt cation's E° is more negative, {{c2::water is preferentially reduced → H₂(g) at the cathode}}.",
    "Oxidation of water: H₂O → ½O₂ + 2H⁺ + 2e⁻, E° = −1.23 V (reversed from +1.23).")
add("Electrolysis of AQUEOUS NaCl: cathode {{c1::H₂(g)}} (water beats Na⁺: −0.83 vs −2.71); anode {{c2::Cl₂(g) in concentrated solution}}; net {{c3::2NaCl + 2H₂O → H₂ + Cl₂ + 2NaOH}}.",
    "Chloride oxidation −1.36 V vs water −1.23 V: water favoured thermodynamically, but the margin is small so concentrated Cl⁻ gives Cl₂. Dilute: mixture of O₂ + Cl₂; very dilute: O₂ only.")
add("Sulfate (SO₄²⁻) can never be oxidized at the anode because {{c1::sulfur is already in its highest oxidation state (+6)}}.",
    "Removing more electrons gives an impossible electron configuration for sulfur.")

# ── R3.2.16 · Electroplating (AHL) ──
add("Electroplating = coating an object with a {{c1::thin layer of metal by electrolysis}}. The object is the {{c2::cathode}}; the metal is the {{c3::anode}}.",
    "Cu anode + steel cathode + CuSO₄(aq) → steel gets a copper coat. Golden Bear trophy (Berlin) = gold-plated bronze.")
add("Electrolysis of CuSO₄ with COPPER electrodes: the anode {{c1::erodes}} (Cu → Cu²⁺ + 2e⁻), copper plates the cathode, and the blue colour {{c2::does not fade}}.",
    "Cu²⁺ removed at cathode = Cu²⁺ replenished by anode. With INERT electrodes: O₂ at anode, blue fades.")
add("Copper purification: {{c1::impure copper}} is the anode; {{c2::pure copper plates}} on the cathode; impurities stay on the anode or in solution.",
    "Impurities less readily oxidized than Cu stay; ions less readily reduced than Cu²⁺ stay in solution.")

# ── End-of-topic gems ──
add("2MnO₄⁻ + Br⁻ + H₂O → 2MnO₂ + BrO₃⁻ + 2OH⁻: the element reduced is {{c1::Mn}} (+7 → +4).",
    "Br is oxidized (−1 → +5).")
add("Most vigorous reaction pair: {{c1::K and F₂}} (most easily oxidized metal × strongest oxidizing agent).",
    "K: top of activity series. F₂: strongest halogen oxidizing agent.")
add("Ni–Cd battery discharge overall: {{c1::Cd + 2NiO(OH) + 2H₂O → Cd(OH)₂ + 2Ni(OH)₂}}.",
    "Anode: Cd + 2OH⁻ → Cd(OH)₂ + 2e⁻; cathode: NiO(OH) + H₂O + e⁻ → Ni(OH)₂ + OH⁻. Charging = reverse.")
add("Unknown metals: Y displaces Z (blue fades, red-brown solid → Z = {{c1::copper}}); X + Y(NO₃)₂ no reaction; Z + X(NO₃)₂ no reaction → reactivity order {{c2::Z < X < Y}}.",
    "Ni–Cu cell: E°cell = 0.34 − (−0.25) = +0.59 V (data booklet Ni²⁺/Ni = −0.25 V).")
add("Ethene + H₂ (Ni catalyst) → ethane: the degree of unsaturation {{c1::decreases}} and ethene is {{c2::reduced}}.",
    "C₂H₄ + H₂ → C₂H₆ — hydrogenation.")

genanki.Package(deck).write_to_file(OUT)
print("OK:", len(deck.notes), "notes ->", OUT)
