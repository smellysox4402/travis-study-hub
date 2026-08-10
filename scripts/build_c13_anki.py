#!/usr/bin/env python3
"""Build C1.3 Photosynthesis cloze deck for the Bio HL deck.
Matches the existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_c13_anki.py  ->  writes C1.3_Photosynthesis.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as all other bio decks -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "photosynthesis", "C1.3_Photosynthesis.apkg")

model = genanki.Model(
    MODEL_ID,
    "Cloze+",
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>',
    }],
    model_type=1,  # cloze
)

CARDS = [
# --- C1.3.1-2 energy transformation ---
("Photosynthesis transforms {{c1::light energy}} into {{c2::chemical energy}} stored in carbon compounds; this energy transformation supplies {{c3::most of the chemical energy for life processes in ecosystems}}.",
 "The solar kitchen powers the whole club. ☀ (c1.3.1)"),
("In photosynthesis, {{c1::carbon dioxide}} is converted to {{c2::glucose}} using hydrogen obtained by {{c3::splitting water}}.",
 "CO2 + water → sugar, H comes from water. 💧 (c1.3.2)"),
# --- C1.3.3 oxygen by-product ---
("Simple word equation: {{c1::carbon dioxide + water → glucose + oxygen}} (in the presence of light and chlorophyll).",
 "CO2 + H2O → C6H12O6 + O2. ⚖ (c1.3.3)"),
("The oxygen produced by photosynthesis comes from {{c1::the splitting of water}}, NOT from carbon dioxide — the classic exam trap.",
 "The O2 leaves from the water tap, not the CO2 tank. 💨 (c1.3.3)"),
("Oxygen is a {{c1::by-product}} of photosynthesis in {{c2::plants, algae and cyanobacteria}}.",
 "Waste for them, our air supply. 🌍 (c1.3.3)"),
# --- C1.3.4 chromatography ---
("Photosynthetic pigments are separated and identified by {{c1::chromatography}} (paper or thin-layer); Rf values are calculated as {{c2::distance moved by pigment ÷ distance moved by solvent front}} and used with colour to identify pigments.",
 "The pigment race: Rf = how far each colour ran. 🏁 (c1.3.4)"),
# --- C1.3.5 absorption spectra ---
("Pigments absorb {{c1::specific wavelengths}} of light — absorption {{c2::excites electrons}} within the pigment molecule, transforming {{c3::light energy to chemical energy}}; only some wavelengths are absorbed (which is why leaves are green).",
 "The pigment only eats certain colours of light. 🍽 (c1.3.5)"),
("Absorption spectra plot {{c1::percentage absorbance (or absorption)}} against {{c2::wavelength AND colour of light}} — chlorophyll absorbs most strongly in {{c3::blue-violet and red}}, least in green.",
 "Two peaks (blue + red), a green valley. 📈 (c1.3.5)"),
# --- C1.3.6 absorption vs action spectra ---
("An {{c1::action spectrum}} plots {{c2::rate of photosynthesis}} (from O2 production or CO2 consumption) against wavelength — comparing it with the absorption spectrum shows {{c3::which pigments actually drive photosynthesis}}.",
 "Absorption = what it eats; action = what it does with the meal. 🔁 (c1.3.6)"),
("Absorption and action spectra are {{c1::similar}} (peaks in blue and red) but not identical — differences reveal {{c2::accessory pigments}} passing energy to chlorophyll a.",
 "The side-kick pigments feed the main star. 🌈 (c1.3.6)"),
# --- C1.3.7 limiting factors ---
("The rate of photosynthesis can be limited by {{c1::carbon dioxide concentration}}, {{c2::light intensity}} or {{c3::temperature}} — each can be varied experimentally while controlling the others.",
 "Three dials on the kitchen: CO2, light, heat. 🎛 (c1.3.7)"),
("In a limiting-factor experiment you identify the {{c1::independent variable}} (the one you change), the {{c2::dependent variable}} (the one you measure) and {{c3::controlled variables}} (kept constant).",
 "Change one, measure one, hold the rest. 🧪 (c1.3.7)"),
("Hypotheses are {{c1::provisional explanations that require repeated testing}} — they can be derived from theory and tested, or based on evidence from earlier experiments.",
 "Guess → test → keep or discard. 🔬 (c1.3.7)"),
# --- C1.3.8 CO2 enrichment + FACE ---
("Carbon dioxide enrichment experiments predict future rates of photosynthesis and plant growth — done in {{c1::enclosed greenhouses}} or as {{c2::free-air CO2 enrichment (FACE)}} experiments in natural ecosystems.",
 "Feed the plants extra CO2 and watch. 🌾 (c1.3.8)"),
("Field experiments like FACE are needed because {{c1::some experiments can only be done in the field}}; careful control of variables is part of experimental design.",
 "Lab control vs real-world realism. 🏞 (c1.3.8)"),
# --- C1.3.9-10 photosystems ---
("A photosystem is an {{c1::array of pigment molecules}} (chlorophyll + accessory pigments) with a special {{c2::chlorophyll at the reaction centre}} that {{c3::emits excited electrons}}; photosystems are always located in {{c4::membranes}} (thylakoids, cyanobacteria).",
 "A solar panel: many collectors, one hot centre. 🔆 (c1.3.9)"),
("A single pigment molecule {{c1::cannot perform any part of photosynthesis}} — the structured array is essential (advantage: the array captures more light and funnels it to the reaction centre).",
 "One collector does nothing; the whole roof works. ☀ (c1.3.10)"),
# --- C1.3.11 photolysis ---
("Photolysis of water occurs in {{c1::photosystem II}}: water is split into {{c2::protons, electrons and oxygen}} — the protons and electrons are used in photosynthesis, and {{c3::oxygen is a waste product}}.",
 "The kitchen's water-splitting knife. 🔪 (c1.3.11)"),
("The advent of oxygen generation by photolysis had {{c1::immense consequences for living organisms and geological processes}} on Earth (the rise of O2).",
 "The great oxygenation event — one kitchen changed the planet. 🌍 (c1.3.11)"),
# --- C1.3.12 chemiosmosis ---
("ATP is produced by {{c1::chemiosmosis}} in thylakoids: a {{c2::chain of electron carriers}} pumps protons across the membrane, building a {{c3::proton gradient}}; protons flow back through {{c4::ATP synthase}}, making ATP.",
 "Protons dam up, then spin the generator on the way back. 🌊 (c1.3.12)"),
("Electrons for ATP production come from {{c1::photosystem I}} ({{c2::cyclic photophosphorylation}}) or {{c3::photosystem II}} ({{c4::non-cyclic photophosphorylation}}).",
 "The short loop or the long loop. 🔄 (c1.3.12)"),
# --- C1.3.13 NADP reduction ---
("NADP is reduced by {{c1::photosystem I}} — it accepts {{c2::two electrons}} from PSI plus a {{c3::hydrogen ion from the stroma}} to become {{c4::NADPH (reduced NADP)}}.",
 "NADP+ + 2e− + H+ → NADPH. ➕ (c1.3.13)"),
# --- C1.3.14 thylakoids as systems ---
("The thylakoid is the system for the {{c1::light-dependent reactions}} — {{c2::photolysis of water}} happens in the lumen/membrane, {{c3::ATP synthesis by chemiosmosis}} across the membrane, and {{c4::reduction of NADP}} at the stroma side.",
 "One membrane, three jobs. 🏭 (c1.3.14)"),
# --- C1.3.15 Rubisco ---
("{{c1::Rubisco}} fixes carbon: it catalyses the reaction of {{c2::RuBP + CO2 → glycerate 3-phosphate (GP)}} — the first step of the Calvin cycle.",
 "The head chef: RuBP grabs CO2, out comes GP. 👨‍🍳 (c1.3.15)"),
("Rubisco is the {{c1::most abundant enzyme on Earth}}; chloroplasts need high concentrations in the stroma because it works {{c2::relatively slowly}} and is {{c3::not effective at low CO2 concentrations}}.",
 "The chef is slow, so the kitchen hires many of him. 🥣 (c1.3.15)"),
# --- C1.3.16 GP → TP ---
("Glycerate 3-phosphate (GP) is converted into {{c1::triose phosphate (TP)}} using {{c2::NADPH and ATP}} from the light-dependent reactions.",
 "GP gets an energy top-up (NADPH + ATP) and becomes TP. 💸 (c1.3.16)"),
# --- C1.3.17 RuBP regeneration ---
("In the Calvin cycle, {{c1::five molecules of triose phosphate}} are converted to {{c2::three molecules of RuBP}} using ATP, allowing the cycle to continue.",
 "5 TP → 3 RuBP, the cycle's recycling step. ♻ (c1.3.17)"),
("If glucose is the product, {{c1::five-sixths of all triose phosphate}} must be converted back to RuBP — only one-sixth leaves the cycle as product.",
 "Six TP made, five recycled, one leaves as sugar. 🍬 (c1.3.17)"),
# --- C1.3.18 end products ---
("All the carbon in compounds in photosynthesizing organisms is {{c1::fixed in the Calvin cycle}}; carbohydrates, amino acids and other carbon compounds are made by pathways that {{c2::trace back to an intermediate in the cycle}} (using mineral nutrients too).",
 "The cycle is the single entrance; everything else branches off. 🌳 (c1.3.18)"),
# --- C1.3.19 interdependence ---
("The light-dependent and light-independent reactions are interdependent: a lack of {{c1::light}} stops the {{c2::light-dependent reactions}} (so no ATP/NADPH → Calvin cycle halts); a lack of {{c3::CO2}} prevents {{c4::photosystem II from functioning}} (the cycle stalls and back-pressure stops the light reactions).",
 "No light, no kitchen power; no CO2, no kitchen work — either way, dinner stops. 🔗 (c1.3.19)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
print(f"Wrote {OUT} — {len(CARDS)} notes")
