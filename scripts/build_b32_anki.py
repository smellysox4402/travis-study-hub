#!/usr/bin/env python3
"""Build B3.2 Transport cloze deck for the Bio HL deck.
Matches the existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_b32_anki.py  ->  writes B3.2_Transport.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as all other bio decks -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "transport", "B3.2_Transport.apkg")

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
# --- B3.2.1 capillaries ---
("Capillaries are adapted for exchange by {{c1::large surface area}} (heavy branching + narrow diameters), {{c2::thin walls}} (single layer of endothelium) and {{c3::fenestrations}} (pores) where exchange must be especially rapid.",
 "The exchange booths: skinny, thin-walled, some with windows. 🪟 (b3.2.1)"),
# --- B3.2.2 arteries vs veins ---
("Arteries have {{c1::thick walls relative to the lumen}}; veins have {{c2::thin walls relative to a wide lumen}} — visible in micrographs/TS.",
 "Arteries = thick pipes; veins = floppy wide tubes. 📏 (b3.2.2)"),
# --- B3.2.3 artery adaptations ---
("Arteries carry blood {{c1::away from the heart}} under high pressure; their walls have {{c2::layers of muscle and elastic tissue}} to {{c3::withstand and maintain high blood pressure}} (elastic recoil smooths the flow).",
 "Thick reinforced pipes that flex with each pump. 🚰 (b3.2.3)"),
# --- B3.2.4 pulse ---
("Heart rate (pulse) can be measured by feeling the {{c1::carotid or radial pulse}} with fingertips — traditional method compared with digital monitors.",
 "Fingertips on the wrist or neck. 🫀 (b3.2.4)"),
# --- B3.2.5 vein adaptations ---
("Veins return blood to the heart using {{c1::valves to prevent backflow}} and {{c2::flexible walls}} so they can be {{c3::compressed by surrounding muscle action}} (muscle pump).",
 "One-way doors + the squeeze of nearby muscles. 🦵 (b3.2.5)"),
# --- B3.2.6 coronary occlusion ---
("Occlusion (blockage) of the {{c1::coronary arteries}} reduces blood supply to the {{c2::heart muscle}}, causing {{c3::coronary heart disease}} — heart attacks when supply fails.",
 "The club's own power line gets cut. 🔌 (b3.2.6)"),
("{{c1::Correlation coefficients}} quantify the strength of a relationship — but even a strong correlation (e.g. {{c2::saturated fat intake and CHD}}) does {{c3::NOT prove causation}}.",
 "Correlation is not causation — the exam loves this. 📊 (b3.2.6)"),
# --- B3.2.7 transpiration / cohesion-tension ---
("Transpiration: water loss from {{c1::cell walls in leaf cells}} draws water out of {{c2::xylem vessels}} and through cell walls by {{c3::capillary action}}, generating {{c4::tension (negative pressure potential)}} that pulls water up the xylem.",
 "The leaf-top evaporation pump. 🌿 (b3.2.7)"),
("{{c1::Cohesion}} between water molecules keeps a {{c2::continuous column}} of water in the xylem so tension can pull the whole column upward.",
 "Water molecules hold hands all the way up. 🤝 (b3.2.7)"),
# --- B3.2.8 xylem adaptations ---
("Xylem vessels are adapted for water transport by {{c1::lack of cell contents}}, {{c2::incomplete or absent end walls}} (unimpeded flow), {{c3::lignified walls}} (withstand tension) and {{c4::pits}} (entry/exit of water).",
 "Empty, open-ended, reinforced, with side doors. 🧱 (b3.2.8)"),
# --- B3.2.9 stem TS ---
("In a TS of a dicot stem: {{c1::vascular bundles}} arranged in a ring, each containing {{c2::xylem}} (inner) and {{c3::phloem}} (outer), surrounded by {{c4::cortex}} with the {{c5::epidermis}} outermost.",
 "Ring of bundles — xylem inside, phloem outside. ⭕ (b3.2.9)"),
# --- B3.2.10 root TS ---
("In a TS of a dicot root: a central {{c1::vascular bundle}} with xylem in a {{c2::cross/star shape}} and phloem between the arms, surrounded by {{c3::cortex}} and the {{c4::epidermis}}.",
 "The root's X-shaped core. ✳ (b3.2.10)"),
# --- B3.2.11 tissue fluid ---
("Tissue fluid is formed by {{c1::pressure filtration of plasma}} in capillaries — the {{c2::higher blood pressure at the arteriolar end}} pushes fluid out; the {{c3::lower pressure at the venule end}} lets tissue fluid drain back in.",
 "High pressure squeezes out, low pressure sips back. 💧 (b3.2.11)"),
# --- B3.2.12 plasma vs tissue fluid ---
("Tissue fluid is plasma that has been filtered — it is similar to plasma but contains {{c1::far less protein}} (plasma proteins stay in the blood).",
 "The filtered guest list: no big proteins. 🧾 (b3.2.12)"),
# --- B3.2.13 lymph ---
("Excess tissue fluid drains into {{c1::lymph ducts}}, which have {{c2::thin walls with gaps}} and {{c3::valves}}; lymph is eventually {{c4::returned to the blood circulation}}.",
 "The spill-catcher gutters with one-way flaps. 🛶 (b3.2.13)"),
# --- B3.2.14 single vs double circulation ---
("Bony fish have {{c1::single circulation}} — blood passes through the heart {{c2::once}} per circuit (heart → gills → body → heart); mammals have {{c3::double circulation}} — blood passes through the heart {{c4::twice}} (heart → lungs → heart → body).",
 "Fish: one loop. Mammal: two loops, more pressure for the body. 🐟🫀 (b3.2.14)"),
# --- B3.2.15 heart adaptations ---
("Mammalian heart adaptations for delivering pressurized blood: {{c1::cardiac muscle}}, {{c2::pacemaker}}, {{c3::atria and ventricles}}, {{c4::atrioventricular and semilunar valves}}, {{c5::septum}} and {{c6::coronary vessels}}.",
 "The VIP pump: muscular, timed, valved, divided, self-fed. ❤ (b3.2.15)"),
("In the frontal plane, blood flows {{c1::unidirectionally}} from named veins → atria → ventricles → arteries, kept one-way by the {{c2::valves}}.",
 "One-way traffic through the pump. 🚦 (b3.2.15)"),
# --- B3.2.16 cardiac cycle ---
("The heartbeat is initiated by the {{c1::sinoatrial node (SA node, the 'pacemaker')}} in the right atrium; the cardiac cycle stages follow for the {{c2::left side of the heart}}.",
 "The SA node drops the beat. 🎵 (b3.2.16)"),
("In the cardiac cycle, {{c1::systole}} = contraction (blood pumped out) and {{c2::diastole}} = relaxation (chambers refill); blood pressure readings are e.g. {{c3::120/80}} = systolic/diastolic.",
 "Squeeze (systole) / rest (diastole). 🫀 (b3.2.16)"),
# --- B3.2.17 root pressure ---
("Root pressure is {{c1::positive pressure potential}} generated by {{c2::active transport of mineral ions}} into the xylem, causing water to move up roots and stems when {{c3::transpiration is insufficient}} (high humidity, or spring before deciduous leaves open).",
 "The basement pump that works when the roof pump is off. 🌱 (b3.2.17)"),
# --- B3.2.18 phloem translocation ---
("Sieve tube elements are adapted for sap flow by {{c1::sieve plates}}, {{c2::reduced cytoplasm and organelles}}, and {{c3::no nucleus}}; companion cells have {{c4::many mitochondria}} and connect via {{c5::plasmodesmata}}.",
 "Open pipes with living support staff next door. 🌀 (b3.2.18)"),
("Phloem translocation: carbon compounds are {{c1::loaded into sieve tubes at sources}} and {{c2::unloaded at sinks}} — companion cells power the loading/unloading.",
 "The escalator moves sugar from where it's made to where it's spent. 🛗 (b3.2.18)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
print(f"Wrote {OUT} — {len(CARDS)} notes")
