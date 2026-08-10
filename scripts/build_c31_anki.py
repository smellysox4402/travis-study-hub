#!/usr/bin/env python3
"""Build C3.1 Integration of Body Systems cloze deck for the Bio HL deck.
Matches the existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_c31_anki.py  ->  writes C3.1_Integration.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as all other bio decks -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "integration", "C3.1_Integration.apkg")

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
# --- C3.1.1 system integration ---
("System integration is the {{c1::coordination of component parts}} of a living system so the whole organism works as one — without it, organs act {{c2::independently}} and the system fails.",
 "Every department of the club has to talk to the others. 🎛 (c3.1.1)"),
# --- C3.1.2 hierarchy + emergent properties ---
("The integration hierarchy: {{c1::cells}} → {{c2::tissues}} → {{c3::organs}} → {{c4::body systems}} → the multicellular organism.",
 "The club org chart. 🪜 (c3.1.2)"),
("Integration of subsystems produces {{c1::emergent properties}} — qualities of the whole that {{c2::do not exist in any single part}}. Example: a {{c3::cheetah}} becomes an effective predator only through integration of all its systems.",
 "The whole club makes the vibe, not any one DJ. 🐆 (c3.1.2)"),
# --- C3.1.3 hormonal + nervous + blood transport ---
("Organs are integrated by two signalling systems — the {{c1::nervous system}} and the {{c2::endocrine system}} — plus {{c3::transport of materials and energy in the blood}}.",
 "Wired mics + radio signals + the roadies. 🎤📻 (c3.1.3)"),
("The nervous system sends messages as {{c1::electrical impulses along neurons}} — fast and {{c2::targeted}}; the endocrine system sends messages as {{c3::hormones in the blood}} — slower but {{c4::widespread/long-lasting}}.",
 "Nerves = phone call; hormones = group email. ⚡📧 (c3.1.3)"),
("The blood system's integration role is {{c1::transporting materials between organs}} — e.g. glucose, oxygen, hormones, heat, waste.",
 "The roadies move the gear between departments. 🚚 (c3.1.3)"),
# --- C3.1.4 brain as central integration organ ---
("The brain is a {{c1::central information integration organ}}: it {{c2::processes information combined from several inputs}} and is the seat of {{c3::learning and memory}}.",
 "The head office merges every input before acting. 🧠 (c3.1.4)"),
# --- C3.1.5 spinal cord + conscious vs unconscious ---
("The spinal cord is an integrating centre for {{c1::unconscious}} processes, while the {{c2::cerebral hemispheres}} handle conscious processes.",
 "The basement crew works without you noticing. 🪜 (c3.1.5)"),
("Conscious processes require {{c1::awareness and decision making}} (you think about them); unconscious processes run {{c2::automatically}} without awareness.",
 "Blinking vs deciding what to say. 👁 (c3.1.5)"),
# --- C3.1.6 sensory input ---
("{{c1::Sensory neurons}} convey messages {{c2::from receptor cells}} (e.g. in skin, eyes, ears) {{c3::to the central nervous system}} — input to the spinal cord and cerebral hemispheres.",
 "The bouncers report what they see at the door. 📥 (c3.1.6)"),
# --- C3.1.7 motor output ---
("{{c1::Motor neurons}} carry output {{c2::from the cerebral hemispheres to muscles}}, stimulating them to {{c3::contract}}.",
 "The DJ's orders go out to the dancers. 📤 (c3.1.7)"),
# --- C3.1.8 nerves as bundles ---
("A nerve is a {{c1::bundle of nerve fibres}} containing both {{c2::sensory and motor neurons}}, wrapped in a protective {{c3::sheath}} (connective tissue).",
 "A nerve = a cable of many wires. 🔌 (c3.1.8)"),
("In a transverse section of a nerve you can see {{c1::myelinated nerve fibres}} (with a pale myelin sheath) and {{c2::unmyelinated nerve fibres}} (no sheath), all packed inside the {{c3::protective sheath}}.",
 "Insulated wires and bare wires in one cable. 🧵 (c3.1.8)"),
# --- C3.1.9 pain reflex arc ---
("A pain reflex arc: {{c1::pain receptor}} (free sensory nerve ending in the hand) → {{c2::sensory neuron}} → {{c3::single interneuron in the grey matter of the spinal cord}} → {{c4::motor neuron}} → {{c5::skeletal muscle}} contracts.",
 "Five links, no brain needed. ✋⚡💪 (c3.1.9)"),
("A reflex is {{c1::involuntary}} and {{c2::rapid}} — the spinal cord integrates the response so the {{c3::brain is bypassed}} (though it gets the news afterwards).",
 "The basement crew acts before the manager knows. 🏃 (c3.1.9)"),
# --- C3.1.10 cerebellum ---
("The {{c1::cerebellum}} coordinates {{c2::skeletal muscle contraction and balance}} — it fine-tunes movements so they are smooth and controlled.",
 "The choreographer. 🕺 (c3.1.10)"),
# --- C3.1.11 melatonin + circadian rhythms ---
("Melatonin is secreted by the {{c1::pineal gland}} with a {{c2::diurnal pattern}} — {{c3::high at night, low in the day}} — and it modulates {{c4::sleep patterns}} as part of {{c5::circadian rhythms}}.",
 "The club's night-mode switch. 🌙 (c3.1.11)"),
# --- C3.1.12 epinephrine ---
("{{c1::Epinephrine (adrenaline)}} is secreted by the {{c2::adrenal glands}} to prepare the body for {{c3::vigorous activity}} — it has widespread effects that facilitate intense muscle contraction.",
 "The panic-button broadcast. 🚨 (c3.1.12)"),
("Epinephrine's widespread effects include {{c1::increased heart rate}}, {{c2::increased ventilation rate}}, {{c3::raised blood glucose}}, and diversion of blood to muscles — all prepping for action.",
 "Full-body prep for the drop. ⚡ (c3.1.12)"),
# --- C3.1.13 hypothalamus + pituitary ---
("The endocrine system is controlled by the {{c1::hypothalamus}} and the {{c2::pituitary gland}} — the hypothalamus links nervous and hormonal control.",
 "The head office issues the hormone orders. 🏢 (c3.1.13)"),
# --- C3.1.14 heart rate feedback ---
("Heart rate is controlled by feedback from {{c1::baroreceptors}} (which monitor {{c2::blood pressure}}, located in the aorta and carotid arteries) and {{c3::chemoreceptors}} (which monitor {{c4::blood pH, O2 and CO2}}).",
 "Pressure sensors + chemistry sensors at the door. 🫀 (c3.1.14)"),
("The {{c1::medulla}} coordinates heart-rate responses by sending nerve impulses to the heart to change {{c2::stroke volume and heart rate}}.",
 "The medulla is the heart's sound engineer. 🎛 (c3.1.14)"),
# --- C3.1.15 ventilation feedback ---
("Ventilation rate is controlled by feedback from {{c1::chemoreceptors in the brainstem}} monitoring {{c2::blood pH}}. Rising CO2 → {{c3::more acidic blood (pH falls)}} → signals to {{c4::diaphragm and intercostal muscles}} increase ventilation.",
 "The CO2 leak detector turns up the fans. 🌬 (c3.1.15)"),
# --- C3.1.16 peristalsis CNS vs ENS ---
("{{c1::Swallowing}} of food and {{c2::egestion}} of faeces are under voluntary control by the {{c3::CNS}}; peristalsis between those points is under involuntary control by the {{c4::enteric nervous system (ENS)}}.",
 "You choose to start and finish; the gut runs the middle itself. 🍽 (c3.1.16)"),
# --- C3.1.17-18 phototropism ---
("Tropic responses are {{c1::directional growth responses}} to stimuli — e.g. seedlings curving toward light, which can be recorded with diagrams (qualitative) or by measuring the {{c2::angle of curvature}} (quantitative).",
 "The seedling leans toward the better light. 🌱 (c3.1.17)"),
("{{c1::Positive phototropism}} is a {{c2::directional growth response to lateral light}} in plant shoots — the shoot bends {{c3::toward}} the light.",
 "The shoot chases the spotlight. 💡 (c3.1.18)"),
# --- C3.1.19 phytohormones ---
("Phytohormones are {{c1::signalling chemicals}} controlling {{c2::growth, development and responses to stimuli}} in plants — a variety of chemicals are used.",
 "Plants run their club on chemical memos. 🌿 (c3.1.19)"),
# --- C3.1.20 auxin efflux carriers ---
("Auxin can diffuse {{c1::freely into}} plant cells but {{c2::not out}} of them — it leaves only via {{c3::auxin efflux carriers}} positioned on one side of the cell membrane.",
 "One-way doors: in for free, out via the exit staff. 🚪 (c3.1.20)"),
("If all cells concentrate their {{c1::auxin efflux carriers on the same side}}, auxin is actively transported {{c2::from cell to cell through the tissue}}, becoming {{c3::concentrated in part of the plant}}.",
 "The whole line passes the message one direction. 🎯 (c3.1.20)"),
# --- C3.1.21 auxin cell growth ---
("Auxin promotes cell growth by stimulating {{c1::hydrogen ion secretion into the apoplast}}, {{c2::acidifying the cell wall}}, which {{c3::loosens cross-links between cellulose molecules}} and so allows {{c4::cell elongation}}.",
 "Acid softens the wall so the cell can stretch. 🧱 (c3.1.21)"),
("In phototropism, the {{c1::auxin concentration gradient}} causes {{c2::differences in growth rate}} — the shaded side grows faster, so the shoot bends {{c3::toward the light}}.",
 "Unequal stretch = a lean. 📐 (c3.1.21)"),
# --- C3.1.22 auxin + cytokinin ---
("{{c1::Root tips}} produce {{c2::cytokinin}}, transported to shoots; {{c1::shoot tips}} produce {{c2::auxin}}, transported to roots — their interaction {{c3::integrates root and shoot growth}}.",
 "Two tips texting each other to grow in balance. 💬 (c3.1.22)"),
# --- C3.1.23 ethylene ---
("{{c1::Ethylene (ethene)}} stimulates the changes of fruit ripening, and ripening in turn stimulates {{c2::more ethylene production}} — a {{c3::positive feedback}} loop.",
 "One ripe apple turns the whole bowl. 🍎 (c3.1.23)"),
("The benefit of ethylene positive feedback: fruit ripening is {{c1::rapid and synchronized}} across the fruit (and often the whole crop).",
 "All the fruit hits peak sweetness together. 🍌 (c3.1.23)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
print(f"Wrote {OUT} — {len(CARDS)} notes")
