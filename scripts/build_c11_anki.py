#!/usr/bin/env python3
"""Build C1.1 Enzymes cloze deck for the Bio HL deck.
Matches the 'Cloze+' note model (Text + Back Extra) so cards merge
cleanly into Anki and anki-arena can read them.
Usage: python build_c11_anki.py  ->  writes C1.1_Enzymes.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as C2.1/B3.1/B3.3/D2.1/D3.2/D3.1 -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "enzymes", "C1.1_Enzymes.apkg")

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
# --- C1.1.1 enzymes as catalysts ---
("Enzymes are {{c1::globular proteins}} that act as {{c2::biological catalysts}}, speeding up reactions by factors of up to a {{c3::million}} or more without being {{c4::consumed}} in the process.",
 "The club's elite bouncers. 🪪 (c1.1.1)"),
# --- C1.1.2 role in metabolism ---
("Cells with more complicated metabolism make {{c1::thousands}} of different enzymes. Enzyme {{c2::specificity}} allows organisms to control {{c3::metabolism}}: producing more or less of an enzyme controls the {{c4::rate of a reaction}}, and enzymes can be {{c5::temporarily stopped}} when a reaction is not needed.",
 "The guest list is controlled. 🎛 (c1.1.2)"),
# --- C1.1.3 anabolic / catabolic ---
("{{c1::Anabolic}} reactions build smaller molecules into larger ones and {{c2::require energy}}; they are {{c3::condensation}} reactions because water is a by-product. Examples: {{c4::protein synthesis (translation)}}, {{c5::DNA synthesis (replication)}}, and synthesis of {{c6::starch, cellulose and glycogen}}.",
 "Building the club's stage costs energy. 🔨 (c1.1.3)"),
("{{c1::Catabolic}} reactions break larger molecules into smaller ones, {{c2::releasing energy}}, sometimes captured by coupling to {{c3::ATP synthesis}}. Examples: {{c4::digestion of food}}, {{c5::cell respiration}} (glucose or lipids oxidized to CO2 and water), and {{c6::digestion of complex carbon compounds}} by decomposers.",
 "Tearing down old sets releases energy. 💥 (c1.1.3)"),
# --- C1.1.4 globular proteins + active site ---
("Enzymes are {{c1::globular proteins}} with a precise 3D structure. The substrate binds to a special region called the {{c2::active site}}; typically just {{c3::a few amino acids}} there create the conditions that convert substrate to products. These amino acids are often {{c4::not next to each other}} in the polypeptide — they are brought together by {{c5::folding}}. If any part of the enzyme is altered, catalysis is unlikely.",
 "The door itself: a few key amino acids, positioned by folding. 🚪 (c1.1.4)"),
# --- C1.1.5 induced fit ---
("The old '{{c1::key and lock}}' model was rejected because interactions between substrate and active site cause {{c2::both}} to change: bond {{c3::angles and lengths}} are altered, changing the 3D shapes. This is called {{c4::induced-fit}} binding. With a second substrate, it binds to {{c5::another part of the active site}}.",
 "The bouncer shifts stance to let the right molecule in. 🤝 (c1.1.5)"),
# --- C1.1.6 molecular motion + collisions ---
("Substrate can only bind when molecular motion brings it very close to the active site — a {{c1::substrate-active site collision}}. Collision rate increases with higher {{c2::concentration}} of substrate or enzyme, or higher {{c3::temperature}} (faster molecular motion). Successful collisions need the substrate {{c4::aligned}} with the active site. Enzymes embedded in membranes are {{c5::immobilized}} — the substrate must do all the moving.",
 "Random motion, right place, right angle. 🎲 (c1.1.6)"),
# --- C1.1.7 specificity + denaturation ---
("Enzyme-substrate specificity: some enzymes are absolutely specific — {{c1::glucokinase}} binds only glucose — while others are broader, like {{c2::hexokinase}} (any hexose sugar) or proteases (any polypeptide). Enzyme structure depends on {{c3::weak interactions}} (hydrophobic and hydrogen bonds) affected by heat and acidity; small changes can prevent binding or catalysis, and if changes are too great to reverse the enzyme is {{c4::denatured}}.",
 "ID check: some doors accept one face, others any face. 🪪 (c1.1.7)"),
# --- C1.1.8 temperature / pH / substrate concentration ---
("Temperature effect on enzyme activity: rising temperature {{c1::increases}} activity (more kinetic energy, more collisions) until the {{c2::optimum temperature}} (which is not always 40°C), then activity falls as enzymes {{c3::denature}}. The pH scale is {{c4::logarithmic}} — one unit lower = {{c5::10 times}} more acidic; deviating from optimum pH alters {{c6::ionic bonds}} between amino acids. Example: the protease of Bacillus licheniformis has a pH optimum of {{c7::9-10}}, used in biological laundry detergents.",
 "Too hot, wrong pH, and the bouncer collapses. 🌡 (c1.1.8)"),
("Substrate concentration effect: more substrate → more collisions → faster reaction, but as active sites become {{c1::occupied}}, increases get smaller — the curve rises {{c2::less and less steeply}} and never quite reaches a {{c3::maximum}} (all active sites saturated).",
 "The queue grows, but the door only lets so many through. 🚶 (c1.1.8)"),
# --- C1.1.9 measurements ---
("In enzyme experiments: the {{c1::independent variable}} is deliberately varied (commonly temperature, substrate concentration, enzyme concentration or pH); {{c2::control variables}} are kept constant for a fair test; the {{c3::dependent variable}} is the quantity measured to calculate {{c4::reaction rate}} (e.g. mmol s−1). Reaction rate = {{c5::amount of substrate used or product formed divided by time}}.",
 "The lab's scoreboard. 📊 (c1.1.9)"),
("In the catalase experiment, yeast catalase converts {{c1::hydrogen peroxide}} (a toxic by-product of metabolism) into {{c2::water and oxygen}}; oxygen volume collected in a measuring cylinder gives the reaction rate. Starch concentration is usually measured in {{c3::grams per 100 cm3}} (as a percentage).",
 "Bubbles = progress. 🫧 (c1.1.9)"),
# --- C1.1.10 activation energy ---
("Substrates must pass through a {{c1::transition state}} before becoming products; the energy needed is the {{c2::activation energy}}. Enzymes lower the activation energy by {{c3::weakening bonds in the substrate}} as it binds to the active site, so the rate increases — typically by a factor of {{c4::a million or more}}. The {{c5::net energy released}} by the reaction is unchanged.",
 "The velvet rope is lowered, the party starts faster. 🎟 (c1.1.10)"),
# --- C1.1.11 intracellular vs extracellular ---
("{{c1::Intracellular}} enzymes are made by free ribosomes in the cytoplasm and work inside the cell (e.g. {{c2::hexokinase}} in glycolysis, {{c3::fumarase}} in the Krebs cycle). {{c4::Extracellular}} enzymes (exoenzymes) are made by ribosomes attached to the {{c5::endoplasmic reticulum}}, released from the cell, and work outside it — e.g. digestive enzymes, and exoenzymes secreted by unicellular {{c6::archaea, bacteria and fungi}} (whose cell walls block endocytosis) to digest macromolecules into absorbable monomers.",
 "Street-level bouncers vs the in-house crew. 🏢 (c1.1.11)"),
# --- C1.1.12 heat generation ---
("Energy conversion is never 100% efficient — the extra energy from metabolic reactions becomes {{c1::heat}}. Birds and mammals use metabolic heat to stay warmer than their environment; during exercise humans use {{c2::sweating and evaporative cooling}}; in the cold, emperor penguins {{c3::huddle}}, humans {{c4::shiver}} (involuntary muscle contractions), and mammals with {{c5::brown fat}} generate heat via {{c6::uncoupled respiration}} — oxidizing substrates without producing ATP, in mitochondria-rich cells.",
 "The club's body heat keeps the floor warm. 🔥 (c1.1.12)"),
# --- C1.1.13 cyclical and linear pathways ---
("Most metabolic pathways are {{c1::linear chains}} of small steps — glycolysis has {{c2::nine}} reactions catalysed by nine different enzymes. {{c3::Branching}} is very common, making metabolism a network. In a {{c4::cyclical}} pathway (e.g. {{c5::Calvin cycle}}, {{c6::Krebs cycle}}) every intermediate is the product of one reaction and the substrate of another.",
 "A one-way queue vs the same loop of dancers. 🔄 (c1.1.13)"),
# --- C1.1.14 allosteric sites + non-competitive inhibition ---
("Many enzymes have a second binding site called an {{c1::allosteric site}}; binding there causes the enzyme to {{c2::change shape}}, altering the active site. This allows regulation: binding can {{c3::activate}} an enzyme or {{c4::reversibly inhibit}} it. Inhibitors that bind the allosteric site rather than the active site do not compete with substrate — they are {{c5::non-competitive inhibitors}}.",
 "The manager's override switch. 🎚 (c1.1.14)"),
# --- C1.1.15 competitive inhibition ---
("{{c1::Competitive inhibitors}} are structurally similar to the substrate and bind {{c2::reversibly to the active site}}; while bound, substrate cannot bind. Whichever molecule arrives first wins. Increasing {{c3::substrate concentration}} reduces competitive inhibition (substrates usually arrive first), but cannot overcome {{c4::non-competitive}} inhibition. Example: {{c5::statins}} competitively inhibit {{c6::HMG-CoA reductase}} (rate-limiting step of cholesterol synthesis in liver cells); {{c7::sarin}} is a competitive inhibitor of {{c8::acetylcholinesterase}}.",
 "Gatecrashers who look like the VIPs. 🥷 (c1.1.15)"),
# --- C1.1.16 feedback inhibition ---
("In {{c1::feedback inhibition}}, the {{c2::end product}} of a metabolic pathway inhibits the {{c3::first enzyme}} by binding its {{c4::allosteric site}} (a form of non-competitive inhibition and {{c5::negative feedback}}). Too much product → pathway switched off; too little → pathway open. Example: {{c6::threonine}} is converted to {{c7::isoleucine}} in five reactions; isoleucine binds the first enzyme, {{c8::threonine deaminase}}, inhibiting the pathway.",
 "The owner caps the guest list when the club is full. 🚫 (c1.1.16)"),
# --- C1.1.17 mechanism-based inhibition ---
("{{c1::Mechanism-based inhibition}} is irreversible: an inhibitor structurally similar to the substrate binds the active site and forms a {{c2::covalent bond}}, permanently inactivating the enzyme. Every inhibitor molecule permanently kills one enzyme molecule. Examples: heavy metals {{c3::mercury and lead}} bind irreversibly to {{c4::-SH groups of cysteine}}; {{c5::penicillin}} binds covalently to {{c6::transpeptidase}} in bacterial cell walls, weakening the wall so bacteria burst (lysis); {{c7::Novichok}} agents irreversibly inhibit {{c8::acetylcholinesterase}}.",
 "A bouncer handcuffed forever by a sticky molecule. ⛓ (c1.1.17)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL (flat)")
deck.add_model(model)
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.abspath(OUT)}")
