#!/usr/bin/env python3
"""Build D2.1 Cell & Nuclear Division cloze deck (~50 cards) for the Bio HL deck.
Matches the user's existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_d21_anki.py  ->  writes D2.1_Cell_Division.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as C2.1/B3.1/B3.3 -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "cell-division", "D2.1_Cell_Division.apkg")

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
# --- D2.1.1 generation of new cells ---
("All organisms need new cells for {{c1::growth}}, {{c2::maintenance}} and {{c3::reproduction}} — they get them by cell division.",
 "The three reasons. 📋 (d2.1.1)"),
("In cell division, the dividing cell is the {{c1::mother cell}} and the products are {{c2::daughter cells}}. The mother cell {{c3::disappears as an entity}} in the process.",
 "No parental supervision — she's gone. 🚪 (d2.1.1)"),
("The cell theory says new cells are only ever produced by {{c1::division of a pre-existing cell}}. Trace it back and every cell connects to the {{c2::zygote}} — then to the earliest cells on Earth: the {{c3::continuity of life}}.",
 "One continuous club history. 🧬 (d2.1.1)"),
("Quaking aspens often reproduce {{c1::asexually}} by sending up new stems from one root system — the whole grove is a {{c2::clone}}, genetically identical.",
 "Pando the giant. 🌳 (d2.1.1)"),
# --- D2.1.2 cytokinesis ---
("Cytokinesis is the division of the {{c1::cytoplasm}} between two daughter cells — it happens alongside nuclear division by {{c2::mitosis}} or {{c3::meiosis}}.",
 "The actual cut. 🍰 (d2.1.2)"),
("In ANIMAL cells, cytokinesis uses a {{c1::cleavage furrow}}: the plasma membrane is pulled inward around the equator by a ring of {{c2::actin and myosin}} — the same proteins that power {{c3::muscle}}.",
 "The pinch crew. 💪 (d2.1.2)"),
("In PLANT cells, {{c1::microtubules}} form a scaffold across the equator, {{c2::vesicles}} fuse into plate-shaped structures forming a cell plate, then {{c3::pectins}} are deposited to make the {{c4::middle lamella}}, and each daughter cell secretes {{c5::cellulose}} to build its own cell wall.",
 "The build crew. 🧱 (d2.1.2)"),
("The plant cell plate grows into {{c1::two complete layers of new plasma membrane}}, which connect to the existing membranes at the sides — completing the split.",
 "Two walls from one plate. 🧱 (d2.1.2)"),
# --- D2.1.3 equal/unequal cytokinesis ---
("Cytokinesis is {{c1::equal}} in a growing root tip, where columns of cells all differentiate the same way.",
 "The orderly queue. 🌱 (d2.1.3)"),
("Two examples of UNEQUAL cytokinesis: {{c1::budding in yeast}} and {{c2::oogenesis in humans}}.",
 "One big winner, one tiny loser. ⚖️ (d2.1.3)"),
("In budding, the yeast nucleus divides by {{c1::mitosis}}, a small outgrowth (bud) receives one nucleus but only a {{c2::small share of cytoplasm}}, and a dividing wall separates the cells — the bud leaves a {{c3::scar}}.",
 "The tiny VIP leaves a mark. 🍺 (d2.1.3)"),
("In oogenesis, the first division makes one {{c1::large cell}} (nearly all the cytoplasm) + a small {{c2::polar body}}; the big cell divides again into one large egg + another tiny polar body. Polar bodies never {{c3::develop}}.",
 "One egg, two scraps. 🥚 (d2.1.3)"),
("A small daughter cell can survive if it gets a nucleus and {{c1::at least one of each organelle}} it can't assemble from scratch — e.g. {{c2::mitochondria}}, which only come from division of a pre-existing mitochondrion.",
 "Never start from zero. 🔋 (d2.1.3)"),
# --- D2.1.4 roles of mitosis and meiosis ---
("If a cell divides without nuclear division first, one daughter is {{c1::anucleate}} — and anucleate cells can't {{c2::synthesise polypeptides}}, so they can't grow or maintain themselves (RBCs live ~{{c3::120 days}}).",
 "The zombie cell. 🧟 (d2.1.4)"),
("MITOSIS produces {{c1::genetically identical}} cells: the diploid number {{c2::2n}} is maintained, every cell keeps the same {{c3::genes}} — preventing tissue rejection and letting a good genome be inherited unchanged in asexual reproduction.",
 "Continuity. 🪩 (d2.1.4)"),
("MEIOSIS halves the chromosome number from {{c1::2n to n}} and generates {{c2::genetic diversity}} — gene pairs are dealt {{c3::randomly}} to daughter cells, fuelling {{c4::evolution by natural selection}}.",
 "Change. 🎲 (d2.1.4)"),
("Mitosis = {{c1::continuity}} (identical cells, 2n kept) · Meiosis = {{c2::change}} (halve to n, shuffled genes).",
 "The one-liner. ⚖️ (d2.1.4)"),
# --- D2.1.5 DNA replication prerequisite ---
("DNA replication is a {{c1::prerequisite}} for both mitosis and meiosis — each daughter must receive a full complement of {{c2::genes}}.",
 "Copy first, split later. 🧬 (d2.1.5)"),
("Before replication a chromosome is one long {{c1::DNA molecule}}. After replication there are two identical molecules — still ONE chromosome — held together by loops of a protein complex called {{c2::cohesin}}.",
 "The twins and the glue. 🧬 (d2.1.5)"),
("Each single DNA molecule is a {{c1::chromatid}}, so a replicated chromosome has two {{c2::sister chromatids}} (genetically identical). Chromatids on different chromosomes are {{c3::non-sister chromatids}} and usually differ.",
 "Identical twins vs cousins. 👯 (d2.1.5)"),
("The cohesin loops are NOT cut until the {{c1::start of anaphase}} — only then do sister chromatids separate and get pulled to opposite poles.",
 "The moment the twins let go. ✂️ (d2.1.5)"),
# --- D2.1.6 condensation and movement ---
("Elongated DNA is too {{c1::narrow}} to see with a light microscope; chromosomes {{c2::condense}} during early mitosis/meiosis, becoming shorter and fatter, and each can then be seen to have {{c3::two strands (chromatids)}}.",
 "Pack it tight to see it. 📦 (d2.1.6)"),
("Chromosomes are moved to opposite poles by {{c1::microtubules}} growing from {{c2::microtubule organising centres (MTOCs)}}, which attach at the centromere region at a protein structure called the {{c3::kinetochore}}.",
 "The tow truck hooks on at the kinetochore. 🚚 (d2.1.6)"),
("Condensation and poleward movement are {{c1::shared features}} of mitosis AND meiosis.",
 "Both clubs use the same rigging. 🏗️ (d2.1.6)"),
# --- D2.1.7 phases of mitosis ---
("The four phases of mitosis: {{c1::Prophase}} (condensation), {{c2::Metaphase}} (chromosomes released from the nucleus, aligned on the equator), {{c3::Anaphase}} (chromosomes moved up to the poles), {{c4::Telophase}} (nuclei reform, chromosomes decondense).",
 "PMAT — pro=before, meta=after, ana=up, telos=finally. 💃 (d2.1.7)"),
("In PROPHASE, chromosomes condense by packing DNA {{c1::tightly}}; toward the end, microtubules grow from the MTOCs to form a {{c2::spindle}}, and the {{c3::nuclear membrane}} breaks down.",
 "Condense + build the dance floor. 🎵 (d2.1.7)"),
("In METAPHASE, spindle microtubules attach to each chromatid's {{c1::centromere/kinetochore}}, sister chromatids attach to {{c2::opposite poles}}, tension tests the attachment, and chromosomes align on the {{c3::equator}}.",
 "Line up and get checked. 📏 (d2.1.7)"),
("In ANAPHASE, the {{c1::cohesin loops are cut}}, sister chromatids become separate chromosomes, and the kinetochore {{c2::shortens the microtubules}}, pulling each chromosome to its pole.",
 "The cut + the haul. 🏃 (d2.1.7)"),
("In TELOPHASE, chromosomes are pulled into a tight group, a {{c1::nuclear membrane}} reforms around each set, and chromosomes {{c2::decondense}} so genes can be transcribed again.",
 "Two clubs from one. 🏠 (d2.1.7)"),
# --- D2.1.8 identification of phases ---
("Root tip squash: fix roots in {{c1::70% ethanol + ethanoic acid}}, treat with {{c2::0.1 mol dm⁻³ HCl at 40 °C}} to loosen cell walls, stain with {{c3::toluidine blue}} (binds DNA), squash under a coverslip, and observe from {{c4::low to medium}} power.",
 "The garlic-root lab dance. 🔬 (d2.1.8)"),
("Mitotic index = {{c1::number of cells in mitosis}} ÷ {{c2::total number of cells}} observed — count ~{{c3::100}} cells and classify each as interphase or a mitosis phase.",
 "The ratio that spots fast growth. 🎯 (d2.1.8)"),
# --- D2.1.9 meiosis as reduction division ---
("Haploid (n) = {{c1::one set of chromosomes}} (all non-homologous). Diploid (2n) = {{c2::two sets}} with homologous pairs. In humans n = {{c3::23}}, so body cells are 2n = {{c4::46}}.",
 "The number system. 🔢 (d2.1.9)"),
("Gametes must be haploid so that fertilization ({{c1::n + n = 2n}}) restores the diploid number — otherwise the chromosome number would {{c2::double every generation}}.",
 "The doubling trap. 🪤 (d2.1.9)"),
("Meiosis is the {{c1::reduction division}}: two rounds of chromosome segregation turn one diploid cell into {{c2::four haploid cells}}.",
 "Half it, twice. 🎲 (d2.1.9)"),
("Meiosis I separates {{c1::homologous chromosomes}} (2n → n); meiosis II separates {{c2::sister chromatids}} (like mitosis, but no replication in between).",
 "First the pairs, then the twins. 🔁 (d2.1.9)"),
# --- D2.1.10 non-disjunction / Down syndrome ---
("Non-disjunction = a pair of chromosomes or chromatids moves to the {{c1::same pole}} instead of opposite ones — at anaphase I or anaphase II — producing cells with one chromosome {{c2::extra or missing}}.",
 "The skipped beat. ⚠️ (d2.1.10)"),
("Down syndrome is caused by {{c1::trisomy 21}} — three copies of chromosome 21 instead of two — from a non-disjunction event. Features can include hearing loss, heart and vision disorders.",
 "The famous trisomy. 🧬 (d2.1.10)"),
("Non-disjunction of sex chromosomes: Klinefelter's syndrome = {{c1::XXY}}; Turner's syndrome = {{c2::one X}} (only one sex chromosome).",
 "XXY and XO. ⚧ (d2.1.10)"),
("The incidence of Down syndrome {{c1::rises}} with {{c2::maternal age}} — older eggs have been halted longer and are more error-prone.",
 "Why the graph climbs. 📈 (d2.1.10)"),
# --- D2.1.11 meiosis as source of variation ---
("Two mechanisms generate variation in meiosis: {{c1::crossing over}} and {{c2::random orientation of bivalents}}.",
 "The double shuffle. 🎲 (d2.1.11)"),
("A pair of homologous chromosomes at synapsis is a {{c1::bivalent}} (4 DNA molecules). Crossing over swaps segments between {{c2::non-sister chromatids}} at points called {{c3::chiasmata}}.",
 "The mid-dance swap. 🔀 (d2.1.11)"),
("Random orientation: each bivalent lines up on the equator facing either way by chance — the number of possible chromosome combinations is {{c1::2ⁿ}} (n = haploid number). In humans: {{c2::2²³ = 8.4 million}}.",
 "The coin-flip multiplier. 🪙 (d2.1.11)"),
("Crossing over occurs at {{c1::random positions}}; at least one crossover happens per bivalent, often {{c2::more than one}}.",
 "Never zero swaps. 🔀 (d2.1.11)"),
# --- D2.1.12 cell proliferation (AHL) ---
("Cell proliferation = a rapid {{c1::increase in cell number}}, when division happens {{c2::faster than}} cell death. Needed for {{c3::growth, cell replacement and tissue repair}}.",
 "Build faster than you lose. 🏗️ (d2.1.12)"),
("Plant proliferation happens in growth regions called {{c1::meristems}} — apical meristems at {{c2::root and shoot tips}}; cells at the margin cease division and {{c3::enlarge and differentiate}}.",
 "The plant building site. 🌱 (d2.1.12)"),
("Skin cell replacement: division happens in the {{c1::basal layer}} of the epidermis; cells make {{c2::keratin}}, dry out, and are rubbed off at the surface. Wound repair uses {{c3::stem cells}} that divide then differentiate.",
 "The conveyor-belt skin. 🧴 (d2.1.12)"),
# --- D2.1.13 phases of the cell cycle (AHL) ---
("The cell cycle has two main phases: {{c1::interphase}} (G1, S, G2) and {{c2::mitosis}} (nuclear division + cytokinesis).",
 "The night in two acts. 🪩 (d2.1.13)"),
("G1 (Gap 1) = after mitosis, before replication — each chromosome is a {{c1::single DNA molecule}}, active {{c2::growth}}. S phase = {{c3::all DNA is replicated}}, forming identical pairs held by {{c4::cohesin}}. G2 (Gap 2) = after replication, each chromosome has {{c5::two chromatids}}, preparing for mitosis.",
 "Grow → copy → check. 🔁 (d2.1.13)"),
("Cells may leave the cycle after mitosis/cytokinesis and enter {{c1::G0}} (Gap zero): they grow and differentiate for a role but {{c2::do not divide again}}.",
 "The VIP lounge. 🛋️ (d2.1.13)"),
# --- D2.1.14 cell growth during interphase (AHL) ---
("In interphase, gene-poor DNA stays condensed as {{c1::heterochromatin}}; the rest decondenses into {{c2::chromatin}} so genes can be {{c3::transcribed}}.",
 "Condensed off, loose on. 🧬 (d2.1.14)"),
("During interphase a cell typically needs to {{c1::double in size}}: DNA replicates, cytoplasm volume increases (new enzymes), membranes expand (extra {{c2::phospholipids, membrane proteins and cholesterol}}), and organelles multiply.",
 "The growth spurt. 📈 (d2.1.14)"),
("Mitochondria and chloroplasts can only be propagated by {{c1::division}} (they contain DNA); Golgi bodies {{c2::bud off}} existing ones; ribosomes are assembled in the {{c3::nucleolus}}.",
 "Every organelle's origin story. 🔬 (d2.1.14)"),
# --- D2.1.15 control by cyclins (AHL) ---
("The cell cycle has {{c1::checkpoints}} that hold cells until it's appropriate to progress — and stop division once a tissue has enough cells.",
 "The bouncers. 🚦 (d2.1.15)"),
("{{c1::Cyclins}} activate {{c2::cyclin-dependent kinases (CDKs)}}, which add {{c3::phosphate}} to other proteins, switching them on at the right phase. Unless cyclins reach a {{c4::threshold concentration}}, the cell doesn't advance.",
 "The DJs run the lights. 🎛️ (d2.1.15)"),
("Cyclin D triggers {{c1::G0 → G1 and G1 → S}}; cyclin E prepares for {{c2::DNA replication}}; cyclin A activates {{c3::DNA replication}} in S; cyclin B promotes {{c4::mitotic spindle assembly}}.",
 "D, E, A, B — the four DJs. 🎵 (d2.1.15)"),
# --- D2.1.16 consequences of mutations (AHL) ---
("Two classes of mutagen: {{c1::carcinogenic chemicals}} (IARC lists 50+ as 'definitely carcinogenic') and {{c2::high-energy radiation}} (X-rays, UV — not visible light).",
 "The troublemakers. ☢️ (d2.1.16)"),
("{{c1::Proto-oncogenes}} normally promote proliferation; a mutated version becomes an {{c2::oncogene}} that actively promotes it and is genetically {{c3::dominant}} — one mutated copy of the pair is enough.",
 "The stuck accelerator. 🚀 (d2.1.16)"),
("{{c1::Tumour-suppressor genes}} prevent proliferation: brakes at checkpoints, {{c2::DNA repair}}, or {{c3::apoptosis}} for damaged cells. Their mutations are {{c4::recessive}} — one working copy still produces enough protein.",
 "The failed brakes. 🛑 (d2.1.16)"),
("A stop-codon mutation in a tumour-suppressor gene makes a {{c1::truncated polypeptide}} with no function — very likely to cause loss of function.",
 "Cut the message, kill the protein. ✂️ (d2.1.16)"),
("Some tumours need as many as {{c1::10 mutations}} together in one cell — rare per cell, but you have vast numbers of cells and a long lifetime; each speed-up creates a bigger pool for the next mutation.",
 "The evolution-in-miniature. 🧫 (d2.1.16)"),
# --- D2.1.17 differences between tumours (AHL) ---
("A {{c1::benign}} tumour's cells adhere to each other as a single mass — unlikely to cause much harm, NOT cancer.",
 "Stuck together, staying put. 🎈 (d2.1.17)"),
("A {{c1::malignant}} tumour has poor cell-to-cell adhesion: cells detach, {{c2::invade neighbouring tissue}}, or travel via {{c3::blood or lymph}} — spread to elsewhere is {{c4::metastasis}}, forming {{c5::secondary tumours}}. This is cancer.",
 "The escape artists. 🦀 (d2.1.17)"),
("Tissues with hormonal stimulation of cell division are more prone to malignancy — e.g. {{c1::breasts, ovaries, testes and thyroid}}.",
 "The hormone hotspot. 🦋 (d2.1.17)"),
("Mitotic index = {{c1::cells in mitosis ÷ total cells}} — a high index means fast cell division, a cancer red flag.",
 "The growth-rate score. 🎯 (d2.1.17)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

pkg = genanki.Package(deck)
pkg.write_to_file(OUT)
print(f"Wrote {len(CARDS)} cards -> {os.path.abspath(OUT)}")
