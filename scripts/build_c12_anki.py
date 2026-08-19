#!/usr/bin/env python3
"""Build C1.2 Cell Respiration cloze deck for the Bio HL deck.
Matches the 'Cloze+' note model (Text + Back Extra) so cards merge
cleanly into Anki and anki-arena can read them.
Usage: python build_c12_anki.py  ->  writes C1.2_Respiration.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as C2.1/B3.1/B3.3/D2.1/D3.2/D3.1/C1.1 -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "respiration", "C1.2_Respiration.apkg")

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
# --- C1.2.1 ATP structure ---
("ATP (adenosine triphosphate) is a {{c1::nucleotide}} made of the base {{c2::adenine}}, the five-carbon sugar {{c3::ribose}} and a chain of {{c4::three phosphate groups}}. ATP is soluble in {{c5::water}}, stable at {{c6::neutral pH}}, cannot pass through the {{c7::phospholipid bilayer}} (so it can't diffuse out of cells), and its {{c8::third phosphate}} can easily be removed and reattached by hydrolysis and condensation.",
 "The club's currency tokens. 💰 (c1.2.1)"),
# --- C1.2.2 ATP supplies energy ---
("Cells need ATP for three main activities: {{c1::synthesizing macromolecules}} (DNA replication, RNA transcription, protein translation — one or more ATP per monomer linked), {{c2::active transport}} (pump proteins change conformation using ATP, e.g. from a more stable to a less stable shape), and {{c3::movement}} (chromosome movement in mitosis, vesicle transport, cytokinesis, phagocyte locomotion, muscle contraction via actin and myosin filaments).",
 "What the tokens buy. 🎟 (c1.2.2)"),
# --- C1.2.3 ATP/ADP interconversion ---
("ATP has {{c1::more chemical potential energy}} than ADP, so energy is released when ATP is converted to {{c2::ADP and phosphate}}. Energy to re-form ATP from ADP + phosphate comes from {{c3::cell respiration}}, {{c4::photosynthesis}} or {{c5::chemosynthesis}}. The body uses about {{c6::120 moles of ATP per day}} but has only about {{c7::0.2 moles}} present at any moment — so ATP is continually regenerated. Interconversions are not 100% efficient, so some energy is lost as {{c8::heat}}.",
 "Tokens get spent and re-minted constantly. 🔁 (c1.2.3)"),
# --- C1.2.4 respiration as a system ---
("Cell respiration is performed by {{c1::all living cells}}: carbon compounds are {{c2::oxidized}} to release energy used to produce {{c3::ATP}}. The main respiratory substrates are {{c4::glucose and fatty acids}}. Gas exchange (O2 in, CO2 out by {{c5::simple diffusion}}) and cell respiration are {{c6::interdependent}}: respiration creates the concentration gradients that drive gas diffusion, and gas exchange prevents lack of oxygen and excess CO2.",
 "The power plant needs fuel and ventilation. ⚡ (c1.2.4)"),
# --- C1.2.5 aerobic vs anaerobic in humans ---
("Aerobic respiration: {{c1::glucose + oxygen → carbon dioxide + water}}, yield {{c2::more than 30 ATP per glucose}}; O2 is the electron acceptor; substrates include carbohydrates, lipids and (after deamination) amino acids; initial reactions in cytoplasm, more in mitochondria. Anaerobic respiration: {{c3::glucose → lactate}}, only {{c4::2 ATP per glucose}}; O2 not used; only carbohydrates; all reactions in the {{c5::cytoplasm}}, mitochondria not required.",
 "Main grid vs emergency generator. 🏭 (c1.2.5)"),
("Anaerobic respiration supplies ATP very rapidly for a short time — used by {{c1::weight lifters}}, {{c2::short-distance runners}} (up to 400 m) and {{c3::sprint finishes}}. Lactate tolerance limits how long it can continue. After vigorous exercise the {{c4::oxygen debt}} must be repaid — oxygen is needed to break down the lactate, which takes several minutes.",
 "The emergency generator's fuel bill comes later. 🧾 (c1.2.5)"),
# --- C1.2.6 variables affecting rate ---
("Respiration rate can be measured via {{c1::oxygen uptake}}, {{c2::carbon dioxide production}}, or {{c3::consumption of glucose or other substrates}}. A {{c4::respirometer}} has a sealed container, a base such as {{c5::potassium hydroxide}} to absorb CO2, and a {{c6::capillary tube}} containing fluid — fluid movement measures {{c7::oxygen consumption}}. Temperature and pressure must be controlled (e.g. {{c8::thermostatically controlled water bath}}), and repeats show reliability.",
 "The plant's fuel gauge. 📏 (c1.2.6)"),
# --- C1.2.7 NAD role ---
("Oxidation = {{c1::loss of electrons}}, reduction = {{c2::gain of electrons}}. NAD ({{c3::nicotinamide adenine dinucleotide}}) is the main {{c4::electron carrier}} in respiration. NAD+ accepts {{c5::two electrons and one proton}} (from two hydrogen atoms) becoming {{c6::reduced NAD}} (NADH + H+). Example: in Benedict's test, Cu2+ ions are reduced to copper atoms (red/orange precipitate) while sugar is oxidized.",
 "The delivery van for electrons. 🚚 (c1.2.7)"),
# --- C1.2.8 glycolysis ---
("Glycolysis has four stages: {{c1::phosphorylation}} (2 ATP used, glucose → fructose-1,6-bisphosphate), {{c2::lysis}} (splits into 2 triose phosphate), {{c3::oxidation}} (hydrogen removed and accepted by NAD → reduced NAD; product bisphosphoglycerate), and {{c4::ATP formation}} (4 ATP produced). Per glucose: {{c5::2 pyruvate (3C each)}}, {{c6::2 reduced NAD}}, net yield {{c7::2 ATP}} (4 made − 2 used). Glycolysis does not require oxygen.",
 "The street-level generator: fast, small yield. ⚙ (c1.2.8)"),
# --- C1.2.9 pyruvate → lactate ---
("In anaerobic respiration in human cells, {{c1::pyruvate}} accepts hydrogen from reduced NAD and is converted to {{c2::lactate}}, regenerating {{c3::NAD}} in the cytoplasm — allowing glycolysis to continue as long as glucose is available and lactate doesn't rise too high. This is {{c4::lactic fermentation}}, used to make {{c5::yoghurt, kimchi, sauerkraut and silage}} — lactate lowers pH and prevents decomposition by bacteria or fungi.",
 "The emergency generator's waste gets dumped safely. 🧯 (c1.2.9)"),
# --- C1.2.10 yeast fermentation ---
("In yeast, pyruvate is converted to {{c1::ethanol and carbon dioxide}} in two stages: first a {{c2::decarboxylation}} removes CO2 forming {{c3::ethanal}}, then reduced NAD transfers hydrogen to ethanal forming {{c4::ethanol}} — regenerating NAD. In {{c5::baking}}, CO2 bubbles make dough rise and ethanol evaporates; in {{c6::brewing}}, ethanol is the product (toxic to yeast at about {{c7::15% by volume}}). Yeast is a {{c8::facultative anaerobe}}. Fermentation can also produce {{c9::bioethanol}} as a renewable fuel.",
 "The brewery/backstage kitchen. 🍞 (c1.2.10)"),
# --- C1.2.11 link reaction ---
("If oxygen is available, pyruvate enters the mitochondrial {{c1::matrix}} and is converted by the {{c2::link reaction}} (a complex of three enzymes) into a {{c3::two-carbon acetyl group}}: {{c4::decarboxylation}} removes CO2, {{c5::oxidation}} removes two electrons accepted by {{c6::NAD}} (→ reduced NAD), and the acetyl group binds to {{c7::coenzyme A}}, forming {{c8::acetyl coenzyme A}}. Pyruvate crosses the outer mitochondrial membrane via a {{c9::transporter protein}}.",
 "The delivery dock between street and plant. 🚛 (c1.2.11)"),
# --- C1.2.12 Krebs cycle ---
("The {{c1::Krebs cycle}} happens in the mitochondrial {{c2::matrix}}: acetyl CoA transfers its acetyl group to {{c3::oxaloacetate}} (4C) forming {{c4::citrate}} (6C), which is converted back to oxaloacetate through a series of reactions. Per turn of the cycle: {{c5::2 CO2 released}} (two decarboxylations), {{c6::3 reduced NAD}} and {{c7::1 reduced FAD}} produced (four oxidations), and {{c8::1 ATP}} (1 ADP converted).",
 "The round-the-clock turbine loop. 🔄 (c1.2.12)"),
# --- C1.2.13 reduced NAD to ETC ---
("In the {{c1::inner mitochondrial membrane}}, groups of protein {{c2::electron carriers}} form the {{c3::electron transport chain (ETC)}}. The first carrier accepts a pair of electrons from {{c4::reduced NAD}}, regenerating NAD. Reduced NAD is produced in {{c5::glycolysis, the link reaction and the Krebs cycle}}. Reduced {{c6::FAD}} also transfers electrons but enters the chain {{c7::part way along}} (its electrons carry less energy). Cristae — infoldings of the inner membrane — increase the membrane area and number of ETCs.",
 "The conveyor belt of electrons. 📦 (c1.2.13)"),
# --- C1.2.14 proton gradient ---
("Electrons flowing along the ETC release energy; the {{c1::three main carriers}} act as {{c2::proton pumps}}, pumping protons from the {{c3::matrix}} to the {{c4::intermembrane space}}. Per pair of electrons from reduced NAD: {{c5::4 + 4 + 2 = 10 protons}} pumped; from reduced FAD: only {{c6::6}} (enters after the first carrier). Pumping against the gradient stores energy in the form of the {{c7::proton gradient}} — high H+ concentration in the intermembrane space, low in the matrix.",
 "The water tower filling up. 💦 (c1.2.14)"),
# --- C1.2.15 chemiosmosis / ATP synthase ---
("{{c1::Chemiosmosis}} couples the proton gradient to ATP synthesis. Protons flow down their concentration gradient from the {{c2::intermembrane space}} to the {{c3::matrix}} through {{c4::ATP synthase}}, a large protein in the inner membrane. The rotor (a drum of {{c5::10 c subunits}}, each binding a proton) rotates with the stalk (γ); this causes conformational changes in the {{c6::3 β subunits}} (each with an active site), which phosphorylate {{c7::ADP to ATP}} — one ATP per β subunit per rotation. Yield: {{c8::2.5 ATP per reduced NAD}} and {{c9::1.5 per reduced FAD}}.",
 "The water-wheel driven by the proton waterfall. 🌊 (c1.2.15)"),
# --- C1.2.16 oxygen as terminal electron acceptor ---
("Oxygen is the {{c1::terminal electron acceptor}}: it has the strongest affinity for electrons, accepting them from the final carrier plus {{c2::hydrogen ions from the matrix}}, producing {{c3::water}} (humans produce about {{c4::half a litre of water per day}} this way). If oxygen runs out, electrons aren't removed from the end of the ETC, all carriers stay reduced, reduced NAD accumulates, and the {{c5::link reaction and Krebs cycle stop}} — only {{c6::glycolysis}} continues: 2 ATP per glucose vs {{c7::32}} with aerobic respiration.",
 "The final customer who takes the spent electrons. 🫧 (c1.2.16)"),
# --- C1.2.17 lipids vs carbohydrates ---
("Energy yield: lipids give {{c1::37 kJ per gram}}, carbohydrates only {{c2::17 kJ per gram}} — nearly twice as much — because {{c3::~90% of lipid mass}} is carbon and hydrogen, while over {{c4::50% of carbohydrate mass}} is oxygen (which yields no energy). Anaerobic respiration is {{c5::not possible with lipids}} — their first stage (fatty acids broken to acetyl groups in the {{c6::matrix}}) requires oxygen; carbohydrates can start with glycolysis, which doesn't.",
 "Fat is the premium fuel. 🛢 (c1.2.17)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL (flat)")
deck.add_model(model)
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.abspath(OUT)}")
