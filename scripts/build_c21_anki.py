#!/usr/bin/env python3
"""Build C2.1 Chemical Signalling cloze deck (53 cards) for the Bio HL deck.
Matches the user's existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_c21_anki.py  ->  writes C2.1_Chemical_Signalling.apkg
"""
import genanki, os, sys

MODEL_ID = 1607392319
DECK_ID  = 2059400110
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "c2.1", "C2.1_Chemical_Signalling.apkg")

model = genanki.Model(
    MODEL_ID,
    "Cloze+",
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>',
    }],
    model_type=1,  # cloze (genanki.CLOZE constant absent in this version)
)

CARDS = [
# --- C2.1.1 ligand + receptor ---
("In cell signalling, the signalling chemical released by a communicating cell is called the {{c1::ligand}}. It binds to a {{c2::receptor protein}} with a complementary binding site on or inside the target cell.",
 "The guest + the door. 🎟 Hormone passes every cell — only cells with the matching receptor react. (c2.1.1)"),
("Binding of a ligand causes a {{c1::conformational change}} in the receptor, which triggers a cellular response. Converting a chemical signal into a cellular response is called {{c2::signal transduction}}.",
 "The key changes shape. 🔑 (c2.1.1)"),
("Ligand binding can trigger: changes in {{c1::gene expression}} (differentiation), regulation of {{c2::enzyme activity}} (metabolism), changes in cell size/shape (muscle contraction), and cell {{c3::proliferation}} or {{c3::death}} (apoptosis).",
 "The four possible responses. 🎭 (c2.1.1)"),
# --- C2.1.2 quorum sensing ---
("{{c1::Quorum sensing}} is cell signalling in bacteria that regulates activity based on {{c2::population density}} — when the concentration of released ligand (an {{c3::autoinducer}}) hits a threshold, the whole population changes behaviour.",
 "Lights on when the room's full. 🦑 (c2.1.2)"),
("{{c1::Vibrio fischeri}} bacteria glow via bioluminescence once quorum is reached. They live inside {{c2::bobtail squid}} in a mutualism: the squid gets {{c3::camouflage}} (lit-up underside), the bacteria get {{c4::organic compounds}} from squid metabolism.",
 "Glow = invisible from below. ✨ (c2.1.2)"),
("When quorum is reached, V. fischeri express the enzyme {{c1::luciferase}}, which catalyses the reaction that produces {{c2::bioluminescence}}.",
 "The enzyme that makes the party glow. ✨ (c2.1.2)"),
# --- C2.1.3 functional categories ---
("Hormones are messengers released into the {{c1::bloodstream}} by endocrine cells, acting on distant cells. Their signals can persist for {{c2::hours}} and often trigger changes in {{c3::gene expression}}.",
 "💌 mail across the country. (c2.1.3)"),
("Neurotransmitters are released by {{c1::nerve cells}} and diffuse across the {{c2::synaptic cleft}}. They act {{c3::rapidly}} and are quickly {{c4::removed}} from the gap after secretion.",
 "🤫 the local whisper — fast and clean. (c2.1.3)"),
("Cytokines are signalling {{c1::proteins}} that regulate {{c2::immune activity}} and the {{c3::cell cycle}}. Examples: {{c4::interleukins}}, erythropoietin, interferon.",
 "📡 immune group texts. (c2.1.3)"),
("Calcium ions signal INSIDE cells: they enter via membrane proteins or are released from stores like the {{c1::sarcoplasmic reticulum}}. They trigger {{c2::contraction}} (muscle), {{c3::exocytosis}} (nerves), or act as second messengers.",
 "🔔 the internal doorbell. (c2.1.3)"),
# --- C2.1.4 chemical diversity ---
("The 4 chemical groups of hormones: {{c1::amine}} (modified amino acid — melatonin, adrenaline), {{c2::peptide}} (<50 aa — ADH, oxytocin), {{c3::protein}} (≥50 aa — insulin, glucagon), {{c4::steroid}} (cholesterol-derived lipid — oestrogen, testosterone, cortisol).",
 "Amines, peptides, proteins, steroids. 🧪 (c2.1.4)"),
("The line between peptide and protein hormones is {{c1::50 amino acids}} — below is peptide, at or above is protein.",
 "ADH/oxytocin = peptides; insulin/glucagon = proteins. 📏 (c2.1.4)"),
("Neurotransmitters include: amino acids ({{c1::glutamate}}, glycine), amines ({{c2::dopamine}}), peptides ({{c3::endorphin}}), esters ({{c4::acetylcholine}}), and the gas {{c5::nitric oxide}}.",
 "5 groups: amino acid, amine, peptide, ester, gas. 🤫 (c2.1.4)"),
("Hormones and neurotransmitters are chemically diverse because each must be {{c1::complementary in shape and charge}} to its receptor and {{c2::small and soluble}} enough to travel — evolution repurposed existing molecules.",
 "Lock-and-key chemistry. 🔐 (c2.1.4)"),
# --- C2.1.5 localised vs distant ---
("{{c1::Autocrine}} signalling = a cell's chemical stimulates {{c2::itself}}. Example: an activated T lymphocyte releases cytokines that stimulate that same cell to {{c3::proliferate}}.",
 "📣 message to self. (c2.1.5)"),
("{{c1::Paracrine}} signalling = a chemical stimulates a {{c2::neighbouring}} cell. Example: {{c3::neurotransmitters}} from a pre-synaptic neuron stimulating the post-synaptic neuron.",
 "🤫 message next door. (c2.1.5)"),
("{{c1::Endocrine}} signalling = a chemical travels in the {{c2::bloodstream}} to activate {{c3::distant}} cells. Example: hormones from endocrine glands.",
 "💌 message across the country. (c2.1.5)"),
("Chemicals transmitted between members of the SAME species are {{c1::pheromones}}; between DIFFERENT species they are called {{c2::allelopathy}}.",
 "Same species vs different species. 📡 (c2.1.5)"),
# --- C2.1.6 receptor types ---
("Hydrophilic ligands bind {{c1::transmembrane receptors}}: non-polar surfaces sit in the lipid bilayer while {{c2::polar amino acids}} exposed to the fluids form the binding site. The ligand {{c3::remains outside}} the cell.",
 "Rings the doorbell. 🔔 (c2.1.6)"),
("Hydrophobic ligands bind {{c1::intracellular receptors}} (cytoplasm or nucleus): the receptor has a {{c2::hydrophilic}} surface and a {{c3::non-polar}} binding site. The ligand {{c4::penetrates}} the cell.",
 "Walks straight in. 💎 (c2.1.6)"),
# --- C2.1.7 transduction ---
("The three stages of a cell signalling pathway: {{c1::reception}} (ligand binds receptor), {{c2::transduction}} (signal converted, often a cascade), {{c3::response}} (change in the cell).",
 "RECEPTION → TRANSDUCTION → RESPONSE. 🎬 (c2.1.7)"),
("Examples of second messengers: {{c1::cAMP}}, {{c2::calcium ions}}, {{c3::nitric oxide}}, {{c4::protein kinases}}. They allow {{c5::amplification}} of the initial signal.",
 "One 'fire!' empties the stadium. ⚡ (c2.1.7)"),
# --- C2.1.8 ACh ---
("ACh binds a ligand-gated ion channel → {{c1::conformational change}} → the channel opens → {{c2::Na+ floods in by facilitated diffusion}} (through the open pore, down its gradient) → the membrane {{c3::depolarises}} (local voltage change) → can trigger an action potential → the impulse propagates.",
 "🚪 THE DOOR. Name the ion: sodium. (c2.1.8)"),
("After signalling, ACh is {{c1::broken down}} to prevent continued stimulation and the products are {{c2::recycled}} by the pre-synaptic neuron. ACh drives {{c3::muscle contraction}} plus memory, arousal and learning.",
 "Clean up after the party. 🧹 (c2.1.8)"),
# --- C2.1.9 GPCR ---
("A GPCR is a {{c1::single polypeptide}} spanning the membrane. The extracellular part forms the {{c2::binding site}}; the intracellular part attaches to a {{c3::G protein}}. Humans have {{c4::many (hundreds of)}} different GPCRs.",
 "📻 the walkie-talkie bouncer. (c2.1.9)"),
("A G protein consists of {{c1::three subunits}}: an {{c2::alpha subunit bound to GDP}} and a {{c3::beta-gamma dimer}}.",
 "α-GDP + βγ. 📻 (c2.1.9)"),
("When a ligand binds a GPCR: {{c1::GDP detaches}} from the α subunit, {{c2::GTP replaces it}}, then the {{c3::α subunit and βγ dimer dissociate}} and diffuse laterally along the membrane to interact with other proteins.",
 "GDP OUT → GTP IN → SPLIT → DELIVER. 📻 (c2.1.9)"),
# --- C2.1.10 epinephrine ---
("Adrenaline (epinephrine) is a water-soluble {{c1::amine}} hormone from the {{c2::adrenal glands}} (above the kidneys). It binds {{c3::GPCRs}} found on many cell types → system-wide {{c4::fight-or-flight}} responses.",
 "📻 the walkie-talkie in action. (c2.1.10)"),
("Adrenaline's cascade: the G protein activates {{c1::adenylyl cyclase}} → converts {{c2::ATP to cAMP}} (the {{c3::second messenger}}) → cAMP activates {{c4::protein kinases}} → responses like glycogen → glucose.",
 "ATP → cAMP → kinase → glucose. ⚡ (c2.1.10)"),
("Fight-or-flight effects of adrenaline: {{c1::heart rate ↑}}, muscle {{c2::contraction}}, {{c3::metabolism}} ↑ (fuel release), {{c4::ventilation}} ↑, {{c5::pupils}} dilate.",
 "Heart, muscles, fuel, breath, eyes. 🏃 (c2.1.10)"),
("'Adrenaline' comes from Latin (ad = at, ren = {{c1::kidney}}); 'epinephrine' from Greek (epi = above, nephros = kidney) — both describe production at the adrenal gland. A NOS example of {{c2::international cooperation}} in science.",
 "Same hormone, two languages. 🌍 (c2.1.10 NOS)"),
# --- C2.1.11 insulin / RTK ---
("A receptor tyrosine kinase is a {{c1::transmembrane enzyme}} that phosphorylates {{c2::tyrosine}} residues on proteins using phosphate from {{c3::ATP}} — changing the protein's shape and activity.",
 "🖨 the photocopier bouncer. (c2.1.11)"),
("The insulin receptor has {{c1::two intracellular tails}} that connect when insulin binds; each tail {{c2::phosphorylates tyrosine}} on the other tail (cross-phosphorylation), recruiting {{c3::relay proteins}} that act as second messengers.",
 "Two tails, cross-phosphorylation. 🖨 (c2.1.11)"),
("One insulin response: vesicles containing {{c1::glucose transporters (GLUT4)}} move to the plasma membrane → {{c2::glucose uptake}} increases. No insulin = glucose locked outside = {{c3::diabetes}}.",
 "🔓 insulin unlocks the door for glucose. (c2.1.11)"),
# --- C2.1.12 intracellular receptors ---
("Steroids diffuse through the membrane → bind a receptor in the {{c1::cytoplasm or nucleus}} → the activated complex is a {{c2::transcription factor}} → binds specific DNA sequences → helps {{c3::RNA polymerase}} attach at the {{c4::promoter}} → gene transcription.",
 "💎 VIP straight to the boss. (c2.1.12)"),
("Steroid hormones are hydrophobic — in the bloodstream they are carried bound to {{c1::soluble transport proteins}}.",
 "Hydrophobic rides. 💎 (c2.1.12)"),
("Testosterone → male sex characteristics + {{c1::muscle growth}}. Oestradiol → female characteristics + regulating the {{c2::menstrual cycle}}. Progesterone → pregnancy: prepares the uterine lining for {{c3::implantation}} and coordinates {{c4::milk production}}.",
 "T = muscle, E = cycle, P = pregnancy. 💎 (c2.1.12)"),
# --- C2.1.13 target effects ---
("Oestradiol binds intracellular receptors in {{c1::hypothalamus}} cells → regulates expression of {{c2::GnRH}} → GnRH acts on the {{c3::anterior pituitary}} → releases {{c4::FSH and LH}} → control of the menstrual cycle.",
 "Oestradiol → hypothalamus → GnRH → FSH/LH. 🧠 (c2.1.13)"),
("Oestradiol can {{c1::inhibit OR promote}} GnRH expression — so the same hormone can drive {{c2::negative or positive}} feedback.",
 "One hormone, both knobs. 🎚 (c2.1.13)"),
("Progesterone binds intracellular receptors in {{c1::endometrial}} cells → regulates expression of a {{c2::growth factor}} → promotes {{c3::cell proliferation}} → the uterine lining {{c4::thickens}}.",
 "🏠 building the nursery. (c2.1.13)"),
# --- C2.1.14 feedback ---
("Negative feedback = the response is the {{c1::reverse}} of the change (it reduces it). Examples: {{c2::thermoregulation}} (thyroxin), {{c3::blood sugar}} (insulin ↓ / glucagon ↑), {{c4::osmoregulation}} (ADH when dehydrated, inhibited when hydrated).",
 "🌡 the thermostat. (c2.1.14)"),
("Positive feedback = the response {{c1::reinforces / amplifies}} the change until the signal stops. Examples: {{c2::childbirth}} (oxytocin → contractions), {{c3::blood clotting}} (platelets → more platelets), {{c4::cell division}} (CDKs → more cyclins).",
 "⛄ the snowball. (c2.1.14)"),
# --- extras ---
("Acetylcholine (ACh) is an {{c1::ester}} — a neurotransmitter used throughout the nervous system.",
 "The ester in the five NT groups. 🤫 (c2.1.4)"),
("Peptide hormones include {{c1::insulin}}, glucagon, {{c2::leptin}}, ADH and oxytocin — they are hydrophilic and bind {{c3::transmembrane receptors}}.",
 "IGLAO: insulin, glucagon, leptin, ADH, oxytocin. 🔔 (c2.1.6)"),
("Unlike an enzyme, a receptor does NOT {{c1::catalyse}} anything — the signalling chemical stays bound for a long time and is {{c2::released unchanged}}. (Enzymes convert substrate into product and release it; receptors just hold.)",
 "The key stays in the lock. 🔑 (c2.1.1)"),
("In V. fischeri, autoinducers bind an intracellular receptor called {{c1::LuxR}} in the cytoplasm; the LuxR–autoinducer complex binds {{c2::DNA}} and switches on transcription of the luciferase genes.",
 "The bacteria's own VIP key. 🦑 (c2.1.2)"),
("Luciferase catalyses an {{c1::oxidation}} reaction — over {{c2::80%}} of the released energy emerges as greenish-blue light. Free-living V. fischeri don't glow: no quorum, no function, no {{c3::wasted energy}}.",
 "Glow is a light-efficient burn. ✨ (c2.1.2)"),
("Hormones are secreted by {{c1::endocrine glands}} — internal secretion directly into {{c2::blood capillaries}}, no duct. By contrast, {{c3::exocrine glands}} secrete through a {{c4::duct}} to the outside.",
 "Endocrine = into the blood; exocrine = out the duct. 💌 (c2.1.3)"),
("Neurotransmitters are either {{c1::excitatory}} (stimulate impulses in the postsynaptic neuron) or {{c2::inhibitory}} (block them). After firing they are removed by {{c3::breakdown in the cleft}} OR {{c4::reabsorption}} into the presynaptic neuron — so each signal affects only the ONE postsynaptic neuron.",
 "Excite, inhibit, clean up, repeat. 🤫 (c2.1.3)"),
("GPCR ligands include {{c1::light-sensitive compounds}} (rhodopsin in your eyes), {{c2::odours}} (olfactory receptors in your nose), {{c3::pheromones}}, hormones and neurotransmitters — your eyes and nose literally run on GPCRs.",
 "📻 eyes and nose = GPCR fans. (c2.1.9)"),
("Calcium-induced calcium release (positive feedback): {{c1::IP3}} binds an IP3 receptor on the {{c2::ER}} → a little Ca²⁺ escapes → that Ca²⁺ activates a {{c3::neighbouring}} calcium channel → even more Ca²⁺ floods out.",
 "A calcium snowball. ⛄ (c2.1.14)"),
("Testosterone negative feedback: {{c1::hypothalamus}} → GnRH → {{c2::anterior pituitary}} → LH → {{c3::Leydig cells}} in the testes make testosterone. Rising testosterone → {{c4::less LH}} from the pituitary AND {{c4::less GnRH}} from the hypothalamus — the end-product shuts off its own production.",
 "The end-product is its own bouncer. 🌡 (c2.1.14)"),
("Liver cells break down glycogen and release glucose into the blood {{c1::within seconds}} of an epinephrine signal — that's how fast the GPCR cascade moves.",
 "Fast fuel. ⚡ (c2.1.10)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, back in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, back]))

genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
