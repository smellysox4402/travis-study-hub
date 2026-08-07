#!/usr/bin/env python3
"""Build D3.2 Inheritance cloze deck (~60 cards) for the Bio HL deck.
Matches the user's existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_d32_anki.py  ->  writes D3.2_Inheritance.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as C2.1/B3.1/B3.3/D2.1 -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "inheritance", "D3.2_Inheritance.apkg")

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
# --- D3.2.1 gametes are haploid ---
("In a sexual life cycle, parents pass genes to offspring in {{c1::gametes}} — egg and sperm. Gametes are {{c2::haploid (n)}}: they contain {{c3::one chromosome of each type}}.",
 "The tickets: half the set, one of each. 🎟 (d3.2.1)"),
("Because gametes are haploid, both parents make an {{c1::equal genetic contribution}} to the offspring — one full set of chromosomes each.",
 "Mum's set + dad's set, no favourites. ⚖ (d3.2.1)"),
# --- D3.2.2 controlled crosses ---
("Patterns of inheritance are investigated by {{c1::controlled crosses}} — transferring {{c2::pollen}} from the anthers of one plant (male parent) onto the {{c3::stigma}} of another (female parent).",
 "The paintbrush method. 🖌 (d3.2.2)"),
("To keep a cross honest, the flower's own {{c1::anthers}} are removed before they mature and the flower is enclosed in a {{c2::paper bag}} so no stray pollen (insects/wind/self) gets in.",
 "No sneaking in the back door. 🚫🐝 (d3.2.2)"),
("In Mendel's crosses: the known parents are the {{c1::P generation}}, offspring are the {{c2::F₁}} (first filial), and their offspring are the {{c3::F₂}}.",
 "Parent → kids → grandkids. 👨👦👦 (d3.2.2)"),
("Mendel crossed tall × dwarf peas, counted every offspring and calculated {{c1::ratios}} — the evidence for discrete inherited factors (alleles), not blending.",
 "Numbers over vibes, even in 1860. 🔢 (d3.2.2)"),
# --- D3.2.3 meiosis produces haploid gametes ---
("Meiosis is the halving trick: one {{c1::diploid}} nucleus divides twice to produce {{c2::four haploid}} nuclei — {{c3::one copy of each gene}} per gamete.",
 "2n → 4 × n. The copy shop. ✂ (d3.2.3)"),
# --- D3.2.4 fusion restores diploid ---
("When gametes fuse, the nuclei join and the chromosome number doubles: the zygote is {{c1::diploid (2n)}} with two chromosomes of each type. {{c2::n + n = 2n}}.",
 "Two half-sets make a full set. 💍 (d3.2.4)"),
("If gametes weren't halved, the chromosome number would {{c1::double every generation}} — the doubling trap that meiosis prevents.",
 "Why sex needs the halving trick. 🪤 (d3.2.4)"),
# --- D3.2.5 monohybrid inheritance ---
("{{c1::Alleles}} are different versions of a gene, differing by as little as {{c2::one base}}. New alleles are born by {{c3::mutation}}.",
 "Tiny changes, big doors. 🧬 (d3.2.5)"),
("Diploid organisms carry {{c1::two}} alleles of most genes — one inherited from each parent. The combination of alleles is the {{c2::genotype}} (e.g. DD, Dd, dd).",
 "Two tickets per gene. 🎫🎫 (d3.2.5)"),
("If both alleles are the same the individual is {{c1::homozygous}} (all gametes carry that allele); if different, {{c2::heterozygous}} (50% of gametes carry each allele).",
 "Same pair = homozy, mixed pair = hetero. 🤝 (d3.2.5)"),
("The {{c1::phenotype}} is the observable outcome of a trait — structural (curly vs straight hair) or functional (seeing red vs green) — and results from {{c2::genotype × environment}}.",
 "What actually shows. 👀 (d3.2.5)"),
("A {{c1::dominant}} allele shows with just one copy; a {{c2::recessive}} allele only shows when both tickets are recessive ({{c3::tt}}).",
 "The bouncer: dominant gets in, recessive needs a pair. 🥊 (d3.2.5)"),
("Mendel's tall × dwarf cross: all F₁ were {{c1::tall}} (dwarf trait disappeared), then F₂ gave {{c2::3 tall : 1 dwarf}} — the reappearance of dwarfism in F₂ is evidence {{c3::against blending inheritance}}.",
 "The 3:1 that ended blending. 📐 (d3.2.5)"),
# --- D3.2.6 phenotypic plasticity ---
("{{c1::Phenotypic plasticity}}: the same genotype produces different phenotypes because the environment switches {{c2::gene expression}} on or off — the genes are {{c3::not changed into new alleles}}, so it's {{c4::reversible}}.",
 "Same band, different setlist. 🎸 (d3.2.6)"),
("Tanning is plasticity: more sunlight → increased expression of the {{c1::melanin}} gene → darker skin. Same genotype the whole time.",
 "The reversible sun-kiss. ☀ (d3.2.6)"),
("Plant plasticity example: seedlings raised in the dark grow {{c1::tall, pale and etiolated}}; in the light they're {{c2::green and compact}} — same variety, same genotype.",
 "Dark = stretch for light. 🌱 (d3.2.6)"),
("Exam trap: plasticity is {{c1::NOT mutation}} and NOT Lamarckian — nothing about it is inherited by the next generation.",
 "Environment changes the show, not the script. 🚫 (d3.2.6)"),
# --- D3.2.7 PKU ---
("Phenylketonuria (PKU) is caused by a {{c1::recessive allele}} of the gene for the enzyme {{c2::phenylalanine hydroxylase}}, located on chromosome {{c3::12}} (an autosome).",
 "Enzyme: phenylalanine → tyrosine. 🧪 (d3.2.7)"),
("In PKU, the missing enzyme means {{c1::phenylalanine}} accumulates → {{c2::brain damage and intellectual disability}} if untreated.",
 "The poison that builds up. ☠ (d3.2.7)"),
# --- D3.2.8 PKU inheritance ---
("A PKU {{c1::carrier}} (Aa) has one normal + one disease allele: enough functional enzyme to stay symptom-free, but can pass the disease allele on.",
 "The silent ticket holder. 🤫 (d3.2.8)"),
("Two carriers (Aa × Aa) have a {{c1::1 in 4 (25%)}} chance per child of an affected (aa) child. Boys and girls have the {{c2::same}} chance — the gene is {{c3::autosomal}}.",
 "The 1-in-4 trap. 🎲 (d3.2.8)"),
("PKU is preventable: {{c1::screen newborns}} (heel-prick) and give a {{c2::low-phenylalanine diet}}.",
 "Caught at birth = no brain damage. 👶 (d3.2.8)"),
# --- D3.2.9 multiple alleles ---
("A {{c1::gene pool}} is all the genes of all individuals in a sexually reproducing population. Positions where different bases can occur are {{c2::single-nucleotide polymorphisms (SNPs)}} — pronounced 'snips'.",
 "The pool of ticket variants. 🌊 (d3.2.9)"),
("Because a gene can have many SNP positions, a gene pool can hold {{c1::many different alleles}} of the same gene — that's {{c2::multiple alleles}}.",
 "More than two door styles. 🚪 (d3.2.9)"),
("The ABO blood group is the classic {{c1::three-allele}} system: {{c2::Iᴬ, Iᴮ and i}}. Iᴬ codes for the A glycoprotein, Iᴮ for the B glycoprotein, i for {{c3::no glycoprotein}}.",
 "Three tickets, four looks. 🩸 (d3.2.9)"),
# --- D3.2.10 codominance ---
("With the ABO alleles: IᴬIᴬ / Iᴬi → type {{c1::A}}; IᴮIᴮ / Iᴮi → type {{c2::B}}; ii → type {{c3::O}}; IᴬIᴮ → type {{c4::AB}} where both glycoproteins show.",
 "The genotype → phenotype menu. 📋 (d3.2.10)"),
("{{c1::Codominance}}: both alleles are expressed at once, not a blend — e.g. {{c2::AB blood type}} shows both A and B glycoproteins.",
 "Both flags fly. 🏳🏴 (d3.2.10)"),
("{{c1::Incomplete dominance}}: the heterozygote is a blend — e.g. {{c2::Mirabilis jalapa}} CᴿCʷ flowers are {{c3::pink}} (red + white mixed).",
 "Two buckets make a half-bucket. 🪣 (d3.2.10)"),
("Exam trap: codominance = {{c1::both show}} (AB); incomplete dominance = {{c2::blend}} (pink). Don't mix them.",
 "Show vs blend — the classic confusion. ⚠ (d3.2.10)"),
("People make antibodies against ABO glycoproteins they lack, which is why transfusions must be compatible: type {{c1::AB}} is the universal recipient, type {{c2::O}} the universal donor.",
 "AB takes all, O gives all. 💉 (d3.2.10)"),
# --- D3.2.11 sex determination ---
("Humans have 23 pairs of chromosomes; pair 23 is the sex chromosomes. The {{c1::X}} is big with ~900 essential genes; the {{c2::Y}} is small with the {{c3::SRY}} gene.",
 "X = the big essential one, Y = the tiny switch. 🧬 (d3.2.11)"),
("Females are {{c1::XX}}, males {{c2::XY}}. All eggs carry one X; sperm carry {{c3::X or Y}} — so the {{c4::father's sperm}} decides the sex. 50:50.",
 "The sperm makes the call. ⚧ (d3.2.11)"),
("SRY is the {{c1::testis-determining factor (TDF)}}: SRY present → gonads become testes → testosterone → male. No SRY → ovaries → oestradiol → female.",
 "The Y flips the switch. 🔀 (d3.2.11)"),
("Karyotype proof: {{c1::XXY}} (Klinefelter's) develops male — the Y is present; {{c2::XO}} (Turner's) develops female — no Y.",
 "Y present = male, even with two Xs. 🔬 (d3.2.11)"),
# --- D3.2.12 sex linkage ---
("Haemophilia is a {{c1::sex-linked}} (X-linked recessive) disorder: the gene for {{c2::Factor VIII}} (a blood-clotting protein) lives on the {{c3::X chromosome}}.",
 "The clotting protein gene rides the X. 🩹 (d3.2.12)"),
("Males (XY) have only {{c1::one X}} — so {{c2::one}} disease allele is enough to get an X-linked recessive disorder. Females (XX) need {{c3::both}} X chromosomes to carry the disease allele.",
 "One strike and you're out (boys). 🥊 (d3.2.12)"),
("Carrier mother (XᴴXʰ) × normal father (XᴴY): sons {{c1::50% affected}}, daughters {{c2::50% carriers}}. There is {{c3::no male-to-male transmission}} — a son's X always comes from {{c4::mum}}.",
 "Dad's Y can't carry the gene. 👨👦 (d3.2.12)"),
("Treatment for haemophilia: infuse {{c1::Factor VIII}} purified from donated blood.",
 "Top up the clotting protein. 💉 (d3.2.12)"),
# --- D3.2.13 pedigree charts ---
("Pedigree charts: {{c1::squares}} = males, {{c2::circles}} = females, {{c3::filled}} symbols = affected. Generations are Roman numerals down the side, individuals numbered within each generation.",
 "The family album code. 📖 (d3.2.13)"),
("Recessive signature in a pedigree: two {{c1::unaffected parents produce an affected child}} → both parents must be carriers (Aa × Aa).",
 "The hidden-carrier reveal. 🕵 (d3.2.13)"),
("Dominant signature in a pedigree: every affected child has {{c1::at least one affected parent}} — the trait doesn't skip generations.",
 "Dominant doesn't hide. 🔦 (d3.2.13)"),
("X-linked recessive signature in a pedigree: {{c1::mostly affected males}} and {{c2::no father-to-son}} transmission.",
 "Boys-only club. 🧍♂️ (d3.2.13)"),
# --- D3.2.14 continuous vs discrete variation ---
("{{c1::Discrete variation}} (e.g. ABO blood type, pea colour): a few genes, separate categories, no in-between — shown as bar charts/counts.",
 "Club vs club vs club. 🎟 (d3.2.14)"),
("{{c1::Continuous variation}} (height, skin colour, milk yield): many genes ({{c2::polygenic inheritance}}) plus environmental influence → a smooth range — shown as histograms/box plots.",
 "The whole dancefloor, one smooth crowd. 💃 (d3.2.14)"),
# --- D3.2.15 box-and-whisker ---
("A box-and-whisker plot shows: {{c1::minimum}}, {{c2::lower quartile (Q1)}}, {{c3::median}}, {{c4::upper quartile (Q3)}}, {{c5::maximum}}.",
 "The five-number summary. 📊 (d3.2.15)"),
("The box spans the {{c1::interquartile range (IQR = Q3 − Q1)}} — the middle 50% of the data.",
 "The box = the middle half. 📦 (d3.2.15)"),
("Points beyond {{c1::1.5 × IQR}} from the box are plotted separately as {{c2::outliers}}.",
 "The ones dancing way off the floor. 🕺 (d3.2.15)"),
# --- D3.2.16 segregation ---
("{{c1::Segregation}}: the two alleles of each gene separate into different gametes during meiosis — each gamete gets {{c2::one allele}} per gene.",
 "The pair splits for the dance. 💃🕺 (d3.2.16)"),
# --- D3.2.17 independent assortment ---
("{{c1::Independent assortment}}: for genes on different chromosomes, allele pairs sort independently — a heterozygous dihybrid (RrYy) makes four equally common gametes: {{c2::RY, Ry, rY, ry}}.",
 "Four ticket combos, equal odds. 🎰 (d3.2.17)"),
("RrYy × RrYy gives the famous {{c1::9:3:3:1}} phenotype ratio — 9 round-yellow : 3 round-green : 3 wrinkled-yellow : 1 wrinkled-green.",
 "The 16-box grid's answer. 🔢 (d3.2.17)"),
("If a dihybrid ratio is off from 9:3:3:1, the genes aren't assorting independently — a hint of {{c1::linkage}}.",
 "Skewed ratio = genes riding together. 🚩 (d3.2.17)"),
# --- D3.2.18 autosomal linkage (AHL) ---
("Each gene sits at a {{c1::locus}} (plural loci) on a specific chromosome. When two genes sit close together on the same chromosome, their alleles tend to be inherited together — {{c2::autosomal gene linkage}}.",
 "Seatmates on the same chromosome. 💺 (d3.2.18)"),
("Linked genes don't assort independently, so a dihybrid cross gives a {{c1::skewed ratio}}, not 9:3:3:1.",
 "No free mixing when they ride together. 🚫 (d3.2.18)"),
# --- D3.2.19 recombinants ---
("Crossing over in meiosis shuffles segments between {{c1::non-sister chromatids}}, producing {{c2::recombinants}} — new allele combinations.",
 "The mid-dance swap. 🔄 (d3.2.19)"),
("In a test cross of a double heterozygote: unlinked genes → {{c1::1:1:1:1}}; linked genes → {{c2::parental types dominate}}, recombinants are rare (frequency reflects {{c3::how far apart}} the genes are).",
 "Far apart = more swaps. 📏 (d3.2.19)"),
# --- D3.2.20 chi-squared ---
("The {{c1::chi-squared (χ²)}} test decides if an observed ratio fits an expected one: χ² = Σ {{c2::(observed − expected)² / expected}}.",
 "The fit-check formula. ➗ (d3.2.20)"),
("Compare χ² with the critical value at {{c1::p = 0.05}} and degrees of freedom = {{c2::classes − 1}}. If χ² is inside the critical region → {{c3::reject the null hypothesis}} → the ratio doesn't fit.",
 "df = classes − 1, the rule of thumb. 🎯 (d3.2.20)"),
# --- D3.2.21 worked example (AHL) ---
("Corn test cross CcNn × ccnn: if unlinked expect {{c1::1:1:1:1}}. Observed 638 CcNn · 21,379 Ccnn · 21,096 ccNn · 672 ccnn — the {{c2::parental}} combos (Cn, cN) swamp the {{c3::recombinants}} (CN, cn), so C and N are {{c4::linked}}.",
 "Parentals ≫ recombinants = linked. 🌽 (d3.2.21)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
print(f"Wrote {OUT} — {len(CARDS)} notes")
