#!/usr/bin/env python3
"""Build the A3.1 Diversity of Organisms topic page for Travis's Study Hub.
Reuses the exact neon CSS + JS from the C2.1 page (single source of style),
with new content grounded in Allott & Mindorff Oxford 2023 pp. 97-115.
"""
from pathlib import Path

HUB = Path(r"C:\Users\ASUS\Desktop\Hermes_Workspace\study-hub")
TPL = HUB / "topics" / "bio" / "c2.1" / "index.html"
OUT_DIR = HUB / "topics" / "bio" / "a3.1-diversity-of-organisms"
OUT = OUT_DIR / "index.html"

src = TPL.read_text(encoding="utf-8")
head = src[: src.index("</head>") + len("</head>")]
head = head.replace("<title>C2.1 Chemical Signalling — The Nightclub</title>", "<title>A3.1 Diversity of Organisms — The Guest List</title>")
script = src[src.index("<script>"):]
script = script.replace("</script>\n</body>\n</html>", "</script>\n</html>")

script = script.replace("var KEY='c21-checklist-v2';", "var KEY='a31-checklist-v2';")

BODY = []
BODY.append(r"""<body>

<a class="home-btn" href="../../../index.html">HOME</a>

<nav>
  <a href="#act1">ACT 1 · THE GUEST LIST</a>
  <a href="#act2">ACT 2 · NAME TAGS</a>
  <a href="#act3">ACT 3 · THE BLUR</a>
  <a href="#act4">ACT 4 · GENOME COUNTER</a>
  <a href="#act5">ACT 5 · THE SCANNER</a>
  <a href="#map">MIND MAP</a>
  <a href="#cheat">CHEAT</a>
  <a href="#test">TEST</a>
  <a href="#check">CHECKLIST</a>
  <span class="pill" id="progPill">0/15</span>
</nav>

<div class="wrap">

<header class="hero">
  <div class="kicker">IB Biology · Higher Level · Theme A</div>
  <h1>A3.1 DIVERSITY OF ORGANISMS</h1>
  <div class="sub">Every species is a VIP list of one. It gets a name tag, the bouncer checks its chromosomes at the door, and if it can't interbreed and produce fertile kids, it doesn't get in. That's how 8.7 million species stay a club instead of one giant blur.</div>
  <div class="badges">
    <span class="badge hl">A3.1 · SL + HL</span>
    <span class="badge ahl">FIRST TOPIC OF THEME A</span>
    <span class="badge">15 SYLLABUS POINTS</span>
  </div>
</header>
""")
print("part1 ok", len(BODY[0]))

BODY.append(r"""<!-- ACT 1 -->
<section class="act" id="act1">
  <div class="acttag">Act 1 · A3.1.1 – A3.1.2</div>
  <h2>THE GUEST LIST</h2>
  <p class="aim">First rule of the club: no two guests are identical. That's not a flaw — it's the whole reason the club exists.</p>

  <div class="panel">
    <h3>NO TWO GUESTS ARE THE SAME</h3>
    <p class="big">Variation between organisms is a <span class="accent">defining feature of life</span>. Not between species — <b>between individuals</b>.</p>
    <ul class="clean">
      <li>The variety across life is immense: humans, trees over 100 m tall, fungi that are a network of threads, bacteria living in volcanic pools above <b>80°C at pH below 2</b>.</li>
      <li>Even <span class="accent">monozygotic (identical) twins</span> differ — they acquire differences through <b>mutations</b> and because the environment they develop in is never identical.</li>
      <li>Why it matters: evolution by <b>natural selection cannot happen without variation</b> — no variation, nothing to select.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>THE VIP LIST</h3>
    <p>A <span class="accent">species</span> = a group of organisms with <b>shared traits</b>. Before DNA, this was judged on <b>morphology</b> — outer form and inner structure (the <span class="cyan">morphological species concept</span>, from Linnaeus's era).</p>
    <ul class="clean">
      <li>The Maori of New Zealand recognised <b>seven types of tree fern</b> by shared traits: wheki, kuripaka, tuokura, mamuka, punui, ponga and katote.</li>
      <li>Biologists later described three more: <i>Alsophila colensoi</i>, <i>A. milnei</i> and <i>A. kermadecensis</i>.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>ONE SPECIES, TWO LOOKS</h3>
    <p>The jaguar <i>Panthera onca</i> comes in a light morph and a dark <b>melanistic</b> morph. They look like different animals — but they are <span class="accent">one species</span>, because they interbreed in the wild.</p>
    <p class="muted">Morphology can lie. Breeding behaviour doesn't. That's the whole plot of Act 2.</p>
  </div>
</section>
""")
print("act1 ok", len(BODY[-1]))

BODY.append(r"""<!-- ACT 2 -->
<section class="act" id="act2">
  <div class="acttag">Act 2 · A3.1.3 – A3.1.4</div>
  <h2>NAME TAGS &amp; DOOR POLICY</h2>
  <p class="aim">Every guest gets a name tag, and the door policy is brutal: can you make fertile babies with the others on the list?</p>

  <div class="panel">
    <h3>THE NAME TAG SYSTEM</h3>
    <p class="big">The international naming system is the <span class="accent">binomial system</span> — two words, and the rules are non-negotiable:</p>
    <ul class="clean">
      <li><b>First word = genus</b> (a group of similar species) — starts with a <span class="accent">capital letter</span>.</li>
      <li><b>Second word = species</b> name — starts with a <span class="cyan">lowercase letter</span>.</li>
      <li>In print, <b>both words are italicised</b>.</li>
      <li>After first use, abbreviate the genus to its initial: <i>L. borealis</i>.</li>
      <li>Binomials often honour a biologist: <i>Linnaea borealis</i> is a small woodland plant named after Carl Linnaeus himself.</li>
    </ul>
  </div>

  <div class="fig">
    <svg viewBox="0 0 640 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="labelled name tag showing the binomial system: genus Panthera capitalised, species onca lower case, both italicised">
      <rect width="640" height="270" rx="14" fill="#150a26"/>
      <rect x="40" y="45" width="380" height="190" rx="16" fill="rgba(255,46,196,.06)" stroke="#ff2ec4" stroke-width="3"/>
      <circle cx="230" cy="45" r="9" fill="none" stroke="#ff2ec4" stroke-width="3"/>
      <path d="M 180 18 L 280 18" stroke="#ff2ec4" stroke-width="3"/>
      <text x="70" y="88" fill="#fbbf24" font-size="13" font-weight="800" letter-spacing="2">HELLO, MY NAME IS</text>
      <text x="70" y="150" fill="#ff2ec4" font-size="52" font-weight="900">PANTHERA</text>
      <text x="70" y="205" fill="#22d3ee" font-size="52" font-weight="900" font-style="italic">onca</text>
      <text x="70" y="225" fill="#f3e8ff" font-size="11" font-weight="700">genus — CAPITAL · species — lowercase · BOTH italic</text>
      <rect x="455" y="45" width="150" height="190" rx="16" fill="rgba(34,211,238,.06)" stroke="#22d3ee" stroke-width="2.5"/>
      <text x="472" y="80" fill="#22d3ee" font-size="12" font-weight="800">AFTER FIRST USE:</text>
      <text x="472" y="130" fill="#ff2ec4" font-size="40" font-weight="900" font-style="italic">P. onca</text>
      <text x="472" y="158" fill="#f3e8ff" font-size="10.5" font-weight="700">abbreviate the genus</text>
      <text x="472" y="174" fill="#f3e8ff" font-size="10.5" font-weight="700">to its initial</text>
      <text x="472" y="210" fill="#b9a3d6" font-size="10" font-weight="600">two words · one species</text>
    </svg>
    <div class="cap"><b>THE NAME TAG:</b> capital genus + lowercase species, both italic. After the first mention, <i>Panthera onca</i> becomes <i>P. onca</i> — same species, shorter tag.</div>
  </div>

  <div class="panel">
    <h3>THE DOOR POLICY: FERTILE BABIES ONLY</h3>
    <p class="big">The <span class="accent">biological species concept</span>: a species = a group of organisms that can <b>successfully interbreed and produce fertile offspring</b>. Members interbreed, so they share genes in a <span class="cyan">gene pool</span>.</p>
    <ul class="clean">
      <li><b>Works well:</b> the genus <i>Allium</i> (onion, garlic) — few interspecific hybrids in the wild, and they're usually sterile. The garden variety "Globemaster" (a deliberate cross of <i>A. christophii</i> x <i>A. macleanii</i>) is sterile.</li>
      <li><b>Also works:</b> conifers — 600+ species, interbreeding very unusual, hybrids usually sterile.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>WHEN THE DOOR POLICY BACKFIRES</h3>
    <p>Captive lions and tigers sometimes hybridise — <b>ligers</b> and <b>tigons</b>. Male hybrids are infertile, but <b>female hybrids are sometimes fertile</b>. A rigorous reading of the BSC would call lions and tigers the same species — which nobody accepts.</p>
    <p>Polar bears and grizzly bears are usually separated geographically, but as grizzlies push north they can meet — and produce <span class="gold">fertile offspring</span>.</p>
    <p class="muted">Over <b>30 different species definitions</b> have been suggested. Darwin in 1859: "No one definition has satisfied all naturalists; yet every naturalist knows vaguely what he means when he speaks of a species."</p>
  </div>
</section>
""")
print("act2 ok", len(BODY[-1]))

BODY.append(r"""<!-- ACT 3 -->
<section class="act" id="act3">
  <div class="acttag">Act 3 · A3.1.5 · A3.1.12</div>
  <h2>THE BLUR</h2>
  <p class="aim">Two populations stop talking. Over generations they drift apart. At exactly which party does the door policy change? Nobody can point to the second.</p>

  <div class="panel">
    <h3>THE LONG GOODBYE</h3>
    <p>A <span class="accent">population</span> = a group of the same species, same area, same time. Two populations in different areas don't interbreed — but that doesn't make them different species. If they're physically and genetically similar, they're still one species.</p>
    <ul class="clean">
      <li>If they <b>stay apart</b>, they diverge: recognisable differences accumulate until they may become separate species. This is <span class="cyan">speciation</span> (Topic A4.1), and it's <b>gradual</b> — so biologists genuinely disagree about where the line is.</li>
      <li>Real case: Cabot's tern was classed as a <b>subspecies</b> of the sandwich tern (<i>Thalasseus sandvicensis</i>), but recent phylogenetic research says it's a separate species, <i>T. acuflavidus</i>. Not all biologists agree.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>NO SEX, NO DOOR POLICY</h3>
    <p class="big">Asexually reproducing species break the concept. Dandelions (<i>Taraxacum officinale</i>) and blackberries (<i>Rubus fruticosus</i>) make flowers and look like they're reproducing sexually — but the offspring are produced by <span class="accent">mitosis</span> and are <b>genetically identical clones</b>.</p>
    <ul class="clean">
      <li>If a clone doesn't interbreed with other clones, it's a separate species by the BSC — so hundreds of blackberry clones have been named as separate <span class="cyan">"microspecies"</span> that only a few experts can tell apart.</li>
      <li>Cleaner conclusion: species that have abandoned sexual reproduction are <b>no longer species</b> under the biological species concept.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>BACTERIA SHARE THE BOUNCER'S NOTES</h3>
    <p>Bacteria do <span class="accent">horizontal gene transfer</span> — genes move between lineages that never interbreed. There's no single gene pool, so the whole "interbreeding population" idea collapses. The BSC simply doesn't apply.</p>
    <p class="muted">Takeaway for exams: the BSC works for sexually reproducing animals and plants; it fails for asexual species (clones) and for bacteria (horizontal gene transfer).</p>
  </div>
</section>
""")
print("act3 ok", len(BODY[-1]))

BODY.append(r"""<!-- ACT 4 -->
<section class="act" id="act4">
  <div class="acttag">Act 4 · A3.1.6 – A3.1.10 · A3.1.13</div>
  <h2>THE GENOME COUNTER</h2>
  <p class="aim">The bouncer checks your chromosomes at the door. Same number, same club. Different number — the club has no idea what to do with you.</p>

  <div class="panel">
    <h3>THE CHROMOSOME COUNT</h3>
    <p>Chromosome number is a fundamental characteristic of a species. It can change over evolution (fusions decrease it, splits increase it, doubling happens) — but changes are <b>rare</b>, and usually a species keeps its number for millions of years.</p>
    <ul class="clean">
      <li>Sexual reproduction keeps numbers <b>even</b>: gametes are <span class="accent">haploid</span> (one set — 9 in cabbages), fusion makes a <span class="cyan">diploid</span> zygote (18 in cabbages), and mitosis preserves it.</li>
      <li>The range is huge: <b>2</b> (jack jumper ant) to <b>78</b> (dog). Humans <b>46</b>, chimpanzees <b>48</b>.</li>
      <li><span class="gold">No sexually reproducing species has 13 chromosomes.</span> Odd numbers can't pair up as homologues in meiosis.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>THE KARYOGRAM</h3>
    <p>Chromosomes are visible when cells divide — <b>metaphase</b> gives the clearest view. Cells are stained, burst to spread the chromosomes, photographed, and the chromosomes are arranged in <span class="accent">homologous pairs, longest to shortest</span>.</p>
    <ul class="clean">
      <li><b>Karyotype</b> = the characteristic set of chromosomes of a species. <b>Karyogram</b> = the image of it.</li>
      <li>Chromosomes are classified three ways: <b>banding pattern</b> (stains give each type a distinctive pattern), <b>size</b> (human chromosome 1 is more than 5x longer than chromosome 21), and <b>centromere position</b> (arms equal vs one arm short, one long).</li>
    </ul>
  </div>

  <div class="fig">
    <svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="labelled diagram of human chromosome 2 arising from the fusion of chimpanzee chromosomes 12 and 13, with telomere and centromere remnants as evidence">
      <rect width="640" height="300" rx="14" fill="#150a26"/>
      <text x="30" y="34" fill="#a855f7" font-size="13" font-weight="800">CHIMPANZEE (48)</text>
      <text x="30" y="52" fill="#b9a3d6" font-size="11" font-weight="600">two separate chromosomes</text>
      <line x1="105" y1="75" x2="105" y2="230" stroke="#a855f7" stroke-width="16" stroke-linecap="round"/>
      <circle cx="105" cy="152" r="8" fill="#150a26" stroke="#a855f7" stroke-width="3"/>
      <circle cx="105" cy="75" r="7" fill="#fbbf24"/>
      <circle cx="105" cy="230" r="7" fill="#fbbf24"/>
      <text x="78" y="265" fill="#a855f7" font-size="12" font-weight="800">12</text>
      <line x1="185" y1="95" x2="185" y2="215" stroke="#22d3ee" stroke-width="16" stroke-linecap="round"/>
      <circle cx="185" cy="155" r="8" fill="#150a26" stroke="#22d3ee" stroke-width="3"/>
      <circle cx="185" cy="95" r="7" fill="#fbbf24"/>
      <circle cx="185" cy="215" r="7" fill="#fbbf24"/>
      <text x="158" y="265" fill="#22d3ee" font-size="12" font-weight="800">13</text>
      <line x1="235" y1="152" x2="330" y2="152" stroke="#ff2ec4" stroke-width="3"/>
      <polygon points="330,144 345,152 330,160" fill="#ff2ec4"/>
      <text x="252" y="135" fill="#ff2ec4" font-size="11.5" font-weight="800">end-to-end</text>
      <text x="252" y="150" fill="#ff2ec4" font-size="11.5" font-weight="800">FUSION</text>
      <line x1="420" y1="60" x2="420" y2="245" stroke="#ff2ec4" stroke-width="22" stroke-linecap="round"/>
      <circle cx="420" cy="152" r="9" fill="#150a26" stroke="#ff2ec4" stroke-width="3"/>
      <circle cx="420" cy="60" r="8" fill="#fbbf24"/>
      <circle cx="420" cy="245" r="8" fill="#fbbf24"/>
      <rect x="406" y="112" width="28" height="10" rx="5" fill="#fbbf24"/>
      <text x="470" y="80" fill="#ff2ec4" font-size="13" font-weight="800">HUMAN 2 (46)</text>
      <text x="470" y="98" fill="#b9a3d6" font-size="11" font-weight="600">one fused chromosome</text>
      <line x1="455" y1="117" x2="438" y2="117" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="470" y="130" fill="#fbbf24" font-size="10.5" font-weight="800">telomere remnants</text>
      <text x="470" y="145" fill="#fbbf24" font-size="10.5" font-weight="800">where the ends joined</text>
      <line x1="455" y1="170" x2="432" y2="157" stroke="#22d3ee" stroke-width="1.5"/>
      <text x="470" y="172" fill="#22d3ee" font-size="10.5" font-weight="800">remnant of a second</text>
      <text x="470" y="187" fill="#22d3ee" font-size="10.5" font-weight="800">centromere</text>
      <text x="470" y="222" fill="#4ade80" font-size="10.5" font-weight="800">testable theory:</text>
      <text x="470" y="238" fill="#4ade80" font-size="10.5" font-weight="800">banding matches 12 + 13</text>
    </svg>
    <div class="cap"><b>THE FUSION:</b> human chromosome 2 = chimpanzee chromosomes 12 + 13 joined end-to-end. Evidence inside the chromosome: leftover telomere sequences at the fusion point and a second, inactive centromere.</div>
  </div>
""")
print("act4a ok", len(BODY[-1]))

BODY.append(r"""
  <div class="panel">
    <h3>ONE GENOME, MANY VERSIONS</h3>
    <p class="big">A <span class="accent">genome</span> = all the genetic information of an organism — the entire base sequence of all its DNA molecules. Unity first, then diversity:</p>
    <ul class="clean">
      <li><b>Unity:</b> members of a species have the <span class="cyan">same genes in the same order</span> along their chromosomes — which is what lets chromosomes exchange parts in meiosis without losing genes.</li>
      <li><b>Diversity:</b> alternative forms of a gene — <span class="accent">alleles</span> — differ in base sequence, usually by just one or a few bases.</li>
      <li><span class="gold">SNPs</span> ("snips") = <b>single-nucleotide polymorphisms</b>: positions where more than 1% of individuals have a different base (rarer than that = a mutation). Over <b>100 million</b> different SNPs are known in humans.</li>
      <li>One individual carries only ~<b>4,000–5,000</b> SNPs — about 1 base in 650,000 differs from the common human sequence. That tiny fraction is most of what makes humans different from each other.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>SIZE ISN'T COMPLEXITY</h3>
    <p>Genome size is measured in base pairs (or megabase pairs, Mbp):</p>
    <table>
      <tr><th>Organism</th><th>Genome / Mbp</th><th>Reality check</th></tr>
      <tr><td><i>Paramecium tetraurelia</i></td><td>27</td><td>a single cell</td></tr>
      <tr><td>Honey bee</td><td>217</td><td>an insect</td></tr>
      <tr><td>Human</td><td>3,080</td><td>you</td></tr>
      <tr><td>Chimpanzee</td><td>3,175</td><td>bigger than a human's</td></tr>
      <tr><td><i>Paris japonica</i></td><td>150,000</td><td>a woodland plant. 50x a human.</td></tr>
    </table>
    <ul class="clean">
      <li>Large genomes carry lots of non-functional DNA — about <b>half the human genome is transposons</b> ("junk DNA") with no known function. Bigger genome does not mean more genes or more complexity.</li>
      <li>Genome sizes are quoted as <span class="cyan">C-values</span> — nuclear DNA content of a haploid cell (a gamete), in picograms (1 pg = 10^-12 g) or base pairs.</li>
      <li>Databases: <b>Kew Plant DNA C-values Database</b>, <b>Animal Genome Size Database</b>, Fungal Genome Size Database, NCBI microbial genomes. Great raw material for an IA or EE data question.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>SAME NUMBER = SAME CLUB <span class="muted">(A3.1.13)</span></h3>
    <p>Members of a species share a chromosome number <b>because of sexual reproduction</b>: gametes are haploid (23 in humans), fusion makes a diploid zygote (46), and meiosis relies on <span class="accent">homologous chromosomes pairing up</span>.</p>
    <ul class="clean">
      <li>Parents with different chromosome numbers — some chromosomes have no homologue — meiosis fails — the offspring is <b>almost certainly infertile</b>.</li>
      <li>The Bramley apple is <b>triploid</b> (51 chromosomes instead of 34): meiosis fails, the anthers produce no pollen — but the tree still fruits, because the fruit cells are made by <b>mitosis</b>.</li>
    </ul>
  </div>
</section>
""")
print("act4b ok", len(BODY[-1]))

BODY.append(r"""<!-- ACT 5 -->
<section class="act" id="act5">
  <div class="acttag">Act 5 · A3.1.11 · A3.1.14 · A3.1.15</div>
  <h2>THE SCANNER</h2>
  <p class="aim">Modern ID: read the whole genome, run the flowchart, or just swab the water and read the DNA everyone left behind.</p>

  <div class="panel">
    <h3>READ THE WHOLE BOOK</h3>
    <p class="big"><span class="accent">Whole genome sequencing</span> = determining the entire base sequence of an organism's DNA. First done in the 1990s on bacteria and archaea (small genomes), now feasible for almost anything.</p>
    <table>
      <tr><th>Year</th><th>Organism</th><th>Size</th><th>First...</th></tr>
      <tr><td>1995</td><td><i>Haemophilus influenzae</i></td><td>1.8 Mbp</td><td>prokaryote</td></tr>
      <tr><td>1996</td><td>yeast</td><td>12 Mbp</td><td>eukaryote</td></tr>
      <tr><td>1998</td><td><i>C. elegans</i></td><td>100 Mbp</td><td>multicellular organism</td></tr>
      <tr><td>2000</td><td><i>Arabidopsis thaliana</i></td><td>135 Mbp</td><td>plant</td></tr>
      <tr><td>2003</td><td>human</td><td>3,080 Mbp</td><td>us</td></tr>
    </table>
    <ul class="clean">
      <li>Cost of one human genome: <b>$100 million (2001) to under $1,000 (2020)</b>. The <span class="cyan">Earth BioGenome Project</span> aims to sequence every known species.</li>
      <li>Uses: evolutionary origins (compare genomes, trace divergence from common ancestors), conservation of biodiversity, controlling infectious diseases (pathogen genomes), and <b>personalized medicine</b> — know your SNPs, predict and treat health problems.</li>
    </ul>
  </div>

  <div class="panel">
    <h3>THE BOUNCER'S FLOWCHART</h3>
    <p>A <span class="accent">dichotomous key</span> is a numbered series of <b>pairs of descriptions</b>. In each pair, one description clearly matches your specimen and the other is clearly wrong. Each pair leads either to the next pair or to an identification. The features you pick must be <b>reliable and easily visible</b> — and keys are built for a particular area, so every local species can be identified.</p>
    <p class="muted">A3.1.14 is a practical: go build one for a local plant or animal group. It's the easiest skill points in this topic.</p>
  </div>

  <div class="fig">
    <svg viewBox="0 0 640 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="labelled flow diagram of a dichotomous key splitting four leaves by paired descriptions">
      <rect width="640" height="420" rx="14" fill="#150a26"/>
      <rect x="250" y="20" width="140" height="42" rx="10" fill="rgba(251,191,36,.12)" stroke="#fbbf24" stroke-width="2.5"/>
      <text x="320" y="46" fill="#fbbf24" font-size="13" font-weight="800" text-anchor="middle">START: 4 LEAVES</text>
      <line x1="320" y1="62" x2="320" y2="92" stroke="#b9a3d6" stroke-width="2"/>
      <circle cx="320" cy="96" r="4" fill="#b9a3d6"/>
      <line x1="320" y1="96" x2="170" y2="140" stroke="#ff2ec4" stroke-width="2"/>
      <line x1="320" y1="96" x2="470" y2="140" stroke="#22d3ee" stroke-width="2"/>
      <rect x="80" y="140" width="180" height="52" rx="10" fill="rgba(255,46,196,.08)" stroke="#ff2ec4" stroke-width="2"/>
      <text x="170" y="162" fill="#ff2ec4" font-size="11.5" font-weight="800" text-anchor="middle">1a blade needle-like</text>
      <text x="170" y="180" fill="#ff2ec4" font-size="12.5" font-weight="900" text-anchor="middle">PINE</text>
      <rect x="380" y="140" width="180" height="52" rx="10" fill="rgba(34,211,238,.08)" stroke="#22d3ee" stroke-width="2"/>
      <text x="470" y="162" fill="#22d3ee" font-size="11.5" font-weight="800" text-anchor="middle">1b blade broad</text>
      <text x="470" y="180" fill="#22d3ee" font-size="12.5" font-weight="900" text-anchor="middle">GO TO 2</text>
      <line x1="470" y1="192" x2="470" y2="230" stroke="#b9a3d6" stroke-width="2"/>
      <circle cx="470" cy="234" r="4" fill="#b9a3d6"/>
      <line x1="470" y1="234" x2="330" y2="280" stroke="#ff2ec4" stroke-width="2"/>
      <line x1="470" y1="234" x2="560" y2="280" stroke="#22d3ee" stroke-width="2"/>
      <rect x="230" y="280" width="200" height="52" rx="10" fill="rgba(255,46,196,.08)" stroke="#ff2ec4" stroke-width="2"/>
      <text x="330" y="302" fill="#ff2ec4" font-size="11.5" font-weight="800" text-anchor="middle">2a margin toothed</text>
      <text x="330" y="320" fill="#ff2ec4" font-size="12.5" font-weight="900" text-anchor="middle">OAK</text>
      <rect x="500" y="280" width="120" height="52" rx="10" fill="rgba(34,211,238,.08)" stroke="#22d3ee" stroke-width="2"/>
      <text x="560" y="302" fill="#22d3ee" font-size="11.5" font-weight="800" text-anchor="middle">2b smooth</text>
      <text x="560" y="320" fill="#22d3ee" font-size="12.5" font-weight="900" text-anchor="middle">GO TO 3</text>
      <line x1="560" y1="332" x2="560" y2="368" stroke="#b9a3d6" stroke-width="2"/>
      <circle cx="560" cy="372" r="4" fill="#b9a3d6"/>
      <line x1="560" y1="372" x2="420" y2="398" stroke="#ff2ec4" stroke-width="2"/>
      <line x1="560" y1="372" x2="600" y2="398" stroke="#22d3ee" stroke-width="2"/>
      <rect x="300" y="380" width="220" height="30" rx="9" fill="rgba(255,46,196,.08)" stroke="#ff2ec4" stroke-width="2"/>
      <text x="410" y="399" fill="#ff2ec4" font-size="11" font-weight="800" text-anchor="middle">3a waxy shine - MAGNOLIA</text>
      <rect x="560" y="380" width="80" height="30" rx="9" fill="rgba(34,211,238,.08)" stroke="#22d3ee" stroke-width="2"/>
      <text x="600" y="399" fill="#22d3ee" font-size="11" font-weight="800" text-anchor="middle">3b - POPLAR</text>
    </svg>
    <div class="cap"><b>THE BOUNCER'S FLOWCHART:</b> every pair of descriptions splits the group in two. One branch ends in an identification, the other sends you deeper. Build it for YOUR local species — that's A3.1.14.</div>
  </div>
""")
print("act5a ok", len(BODY[-1]))

BODY.append(r"""
  <div class="panel">
    <h3>DNA FROM THE WATER</h3>
    <p class="big"><span class="accent">DNA barcodes</span> = short sections of one gene (or a few) that are distinctive enough to identify a species. For animals: part of the gene for <b>cytochrome oxidase subunit 1 (CO1)</b>.</p>
    <ul class="clean">
      <li><span class="cyan">Environmental DNA (eDNA)</span> = DNA collected from water, soil or any part of the abiotic environment — it contains DNA from everything that passed through.</li>
      <li>Real cases: <b>Gouldian finches</b> (a rare bird) detected from waterhole samples in northern Australia; a <b>fisher</b> (<i>Pekania pennanti</i>, a small carnivore) confirmed from DNA left in snow tracks in Idaho.</li>
      <li>Why it's powerful: no need to see, catch or even recognise the organism — the DNA does the ID.</li>
    </ul>
  </div>
</section>

<!-- MIND MAP -->
<section class="act" id="map">
  <div class="acttag">Revision</div>
  <h2>MIND MAP</h2>
  <p class="aim">The whole topic on one screen. Start at the centre, follow any branch.</p>
  <div class="mind">
    <div class="node core">A3.1 DIVERSITY<br>OF ORGANISMS<br><small>SL + AHL · 15 points</small></div>
    <div class="arrow">→</div>
    <div class="node">VARIATION<br><small>defining feature of life · A3.1.1</small></div>
    <div class="arrow">→</div>
    <div class="node">SPECIES<br><small>shared traits · morphology · A3.1.2</small></div>
    <div class="arrow">→</div>
    <div class="node">BINOMIAL<br><small>Genus species · italics · A3.1.3</small></div>
    <div class="arrow">→</div>
    <div class="node">BSC<br><small>interbreed → fertile · A3.1.4</small></div>
    <div class="arrow">→</div>
    <div class="node">THE BLUR<br><small>divergence · asexual · HGT · A3.1.5/12</small></div>
    <div class="arrow">→</div>
    <div class="node">CHROMOSOMES<br><small>46 · 48 · 78 · 2 · A3.1.6/13</small></div>
    <div class="arrow">→</div>
    <div class="node">KARYOGRAM<br><small>pairs, longest → shortest · A3.1.7</small></div>
    <div class="arrow">→</div>
    <div class="node">SNPs<br><small>4–5k per person · A3.1.8</small></div>
    <div class="arrow">→</div>
    <div class="node">GENOME SIZE<br><small>Paris japonica wins · A3.1.9/10</small></div>
    <div class="arrow">→</div>
    <div class="node">WGS + eDNA<br><small>1995→2003 · CO1 · A3.1.11/15</small></div>
  </div>
  <div class="panel">
    <h3>THE FIVE NUMBERS WORTH MEMORISING</h3>
    <table>
      <tr><th>Fact</th><th>Number</th></tr>
      <tr><td>Human chromosomes</td><td>46</td></tr>
      <tr><td>Chimpanzee chromosomes</td><td>48</td></tr>
      <tr><td>Dog chromosomes</td><td>78</td></tr>
      <tr><td>Jack jumper ant chromosomes</td><td>2</td></tr>
      <tr><td><i>Paris japonica</i> genome</td><td>150,000 Mbp (biggest known)</td></tr>
    </table>
  </div>
</section>

<!-- CHEAT -->
<section class="act" id="cheat">
  <div class="acttag">Revision</div>
  <h2>CHEAT SHEET</h2>
  <p class="aim">Everything the examiner wants, compressed into 15 lines.</p>
  <div class="marquee">
    <div class="line">1 · VARIATION = defining feature of life · <span>no variation → no natural selection</span></div>
    <div class="line">2 · SPECIES = group with shared traits · <span>morphological concept = form + structure</span></div>
    <div class="line">3 · BINOMIAL: <span>Genus species</span> · capital + lowercase · ITALICS · abbreviate after first use</div>
    <div class="line">4 · BSC = <span>interbreed + produce FERTILE offspring</span> · shared gene pool</div>
    <div class="line">5 · THE BLUR: separated populations diverge gradually · <span>when do they become species?</span></div>
    <div class="line">6 · NO SEX: dandelions + blackberries = clones · <span>BSC breaks · "microspecies"</span></div>
    <div class="line">7 · BACTERIA: horizontal gene transfer → no single gene pool · <span>BSC breaks</span></div>
    <div class="line">8 · CHROMOSOMES: <span>46 human · 48 chimp · 78 dog · 2 ant</span> · odd numbers don't exist</div>
    <div class="line">9 · KARYOGRAM = chromosomes arranged in pairs · <span>longest → shortest</span></div>
    <div class="line">10 · HUMAN CHROMOSOME 2 = <span>fusion of chimp 12 + 13</span> · telomere + centromere remnants</div>
    <div class="line">11 · UNITY: same genes, same order · <span>DIVERSITY: alleles + SNPs</span> · 4,000–5,000 per person</div>
    <div class="line">12 · GENOME SIZE ≠ COMPLEXITY · <span>Paris japonica (150,000 Mbp) > human (3,080)</span> · transposons</div>
    <div class="line">13 · WGS: bacterium 1995 → yeast 1996 → worm 1998 → plant 2000 → human 2003 · <span>$100M → <$1,000</span></div>
    <div class="line">14 · DICHOTOMOUS KEY = pairs of descriptions · <span>each pair splits the group in two</span></div>
    <div class="line">15 · eDNA BARCODE = short gene section (CO1 for animals) from water/soil · <span>Gouldian finch · fisher</span></div>
  </div>
</section>
""")
print("act5b ok", len(BODY[-1]))

BODY.append(r"""<!-- TEST -->
<section class="act" id="test">
  <div class="acttag">Practice</div>
  <h2>THE DOOR TEST</h2>
  <p class="aim">Click an answer. Instant feedback. No mercy.</p>

  <div class="q" data-a="bsc">
    <p>1. What is the biological species concept?</p>
    <label><input type="radio" name="q1" value="bsc"> A group of organisms that can interbreed and produce FERTILE offspring</label>
    <label><input type="radio" name="q1" value="w1"> A group of organisms that look alike</label>
    <label><input type="radio" name="q1" value="w2"> A group of organisms that share a habitat</label>
    <div class="fb correct">Correct — interbreed + fertile offspring + shared gene pool. That's the door policy.</div>
    <div class="fb wrong">Not the look-alike club — morphology can lie (jaguar morphs, tree ferns). The BSC is about breeding.</div>
  </div>

  <div class="q" data-a="odd">
    <p>2. Why does no sexually reproducing species have 13 chromosomes?</p>
    <label><input type="radio" name="q2" value="w1"> 13 is an unlucky number for meiosis</label>
    <label><input type="radio" name="q2" value="odd"> An odd number can't pair up as homologous chromosomes in meiosis</label>
    <label><input type="radio" name="q2" value="w2"> Gametes always have an even number of chromosomes</label>
    <div class="fb correct">Correct — one chromosome would have no homologue, meiosis fails, offspring almost certainly infertile.</div>
    <div class="fb wrong">It's meiosis: homologues must PAIR. Odd count = one lonely chromosome = no pairing = no fertile offspring.</div>
  </div>

  <div class="q" data-a="fusion">
    <p>3. What two pieces of evidence show human chromosome 2 is a fusion of two chimp chromosomes?</p>
    <label><input type="radio" name="q3" value="w1"> Two centromeres and twice the genes</label>
    <label><input type="radio" name="q3" value="w2"> A double telomere and double the DNA</label>
    <label><input type="radio" name="q3" value="fusion"> Telomere remnants in the middle + a second, inactive centromere</label>
    <div class="fb correct">Correct — leftover telomere sequences at the fusion point and a dead second centromere. Banding matches chimp 12 + 13.</div>
    <div class="fb wrong">Look INSIDE chromosome 2: telomere sequences mid-chromosome + a second inactive centromere. Banding matches chimp 12 + 13.</div>
  </div>

  <div class="q" data-a="liger">
    <p>4. Why do ligers and tigons break a strict reading of the BSC?</p>
    <label><input type="radio" name="q4" value="w1"> They are infertile, so lions and tigers are different species</label>
    <label><input type="radio" name="q4" value="liger"> Male hybrids are infertile but females are sometimes fertile</label>
    <label><input type="radio" name="q4" value="w2"> They can't be bred in the wild</label>
    <div class="fb correct">Correct — some female hybrids are fertile, so a strict BSC would call lions and tigers ONE species. Nobody accepts that.</div>
    <div class="fb wrong">The catch: male hybrids sterile, FEMALE hybrids sometimes fertile. Strict BSC → lions and tigers same species. Nope.</div>
  </div>

  <div class="q" data-a="snp">
    <p>5. What is a SNP, and roughly how many does one person carry?</p>
    <label><input type="radio" name="q5" value="w1"> A whole-gene difference; about 100</label>
    <label><input type="radio" name="q5" value="w2"> A chromosome rearrangement; about 5,000</label>
    <label><input type="radio" name="q5" value="snp"> A single-nucleotide polymorphism; about 4,000-5,000</label>
    <div class="fb correct">Correct — one base position where >1% of people differ; an individual carries ~4,000-5,000 of them.</div>
    <div class="fb wrong">SNP = single-nucleotide polymorphism (one base, >1% of individuals). One person carries ~4,000-5,000.</div>
  </div>

  <div class="q" data-a="hgt">
    <p>6. Why does the BSC fail for bacteria?</p>
    <label><input type="radio" name="q6" value="w1"> They reproduce too fast to classify</label>
    <label><input type="radio" name="q6" value="hgt"> Horizontal gene transfer moves genes between lineages that never interbreed</label>
    <label><input type="radio" name="q6" value="w2"> They have no chromosomes</label>
    <div class="fb correct">Correct — genes cross lineages freely, so there's no single shared gene pool to define.</div>
    <div class="fb wrong">Horizontal gene transfer: genes jump between lineages that never interbreed. No gene pool = no BSC.</div>
  </div>

  <div class="q" data-a="key">
    <p>7. How does a dichotomous key identify an organism?</p>
    <label><input type="radio" name="q7" value="key"> Numbered PAIRS of descriptions; one in each pair matches, leading to the next pair or a name</label>
    <label><input type="radio" name="q7" value="w1"> A list of every species with a photo</label>
    <label><input type="radio" name="q7" value="w2"> A DNA test at every step</label>
    <div class="fb correct">Correct — pairs of descriptions, each pair splits the group in two until one species is left.</div>
    <div class="fb wrong">It's pairs: in each pair, ONE description clearly matches. Follow the matches to the name.</div>
  </div>

  <div class="q" data-a="edna">
    <p>8. What is environmental DNA and why is it useful?</p>
    <label><input type="radio" name="q8" value="w1"> DNA extracted from fossils only</label>
    <label><input type="radio" name="q8" value="w2"> DNA from a single captured organism</label>
    <label><input type="radio" name="q8" value="edna"> DNA in water/soil from everything that passed through; ID species without seeing them</label>
    <div class="fb correct">Correct — eDNA found the Gouldian finch at waterholes and a fisher from snow tracks. No sighting needed.</div>
    <div class="fb wrong">eDNA = DNA from the abiotic environment — everything that passed through. Detect without seeing (Gouldian finch, fisher).</div>
  </div>
</section>
""")
BODY.append(r"""<!-- CHECKLIST -->
<section class="act" id="check">
  <div class="acttag">A3.1 · full syllabus checklist</div>
  <h2>THE CHECKLIST</h2>
  <p class="aim">15 boxes. Tick what you can explain out loud without notes. Progress saves on this device.</p>
  <div class="progress"><div class="fill" id="fill"></div></div>
  <div class="progtext" id="progText">0 / 15 mastered</div>
  <ul class="cl" id="cl">
    <li data-i="0"><span class="box">✓</span><span class="code">A3.1.1</span><span>Variation between organisms is a defining feature of life (identical twins differ).</span></li>
    <li data-i="1"><span class="box">✓</span><span class="code">A3.1.2</span><span>A species is a group of organisms with shared traits (morphological concept, Maori tree ferns).</span></li>
    <li data-i="2"><span class="box">✓</span><span class="code">A3.1.3</span><span>Binomial system: genus + species, italics, capital/lowercase, abbreviation (<i>Linnaea borealis</i>).</span></li>
    <li data-i="3"><span class="box">✓</span><span class="code">A3.1.4</span><span>Biological species concept: interbreed + fertile offspring (<i>Allium</i>, conifers; ligers/tigons as a challenge).</span></li>
    <li data-i="4"><span class="box">✓</span><span class="code">A3.1.5</span><span>Divergence of populations over time — the boundary between subspecies and species is fuzzy.</span></li>
    <li data-i="5"><span class="box">✓</span><span class="code">A3.1.6</span><span>Chromosome number is a fundamental characteristic (2 → 78; no odd numbers).</span></li>
    <li data-i="6"><span class="box">✓</span><span class="code">A3.1.7</span><span>Karyograms: homologous pairs, longest → shortest, banding/size/centromere position.</span></li>
    <li data-i="7"><span class="box">✓</span><span class="code">A3.1.8</span><span>Unity (same genes, same order) vs diversity (alleles, SNPs; 4,000–5,000 per person).</span></li>
    <li data-i="8"><span class="box">✓</span><span class="code">A3.1.9</span><span>Genome sizes: C-values, Mbp, databases; transposons; size ≠ complexity (<i>Paris japonica</i>).</span></li>
    <li data-i="9"><span class="box">✓</span><span class="code">A3.1.10</span><span>Human chromosome 2 = fusion of chimp 12 + 13, with telomere + centromere remnants.</span></li>
    <li data-i="10"><span class="box">✓</span><span class="code">A3.1.11</span><span>Whole genome sequencing: 1995 bacterium → 2003 human; cost crash; applications.</span></li>
    <li data-i="11"><span class="box">✓</span><span class="code">A3.1.12</span><span>BSC fails: asexual species (dandelion, blackberry microspecies) and bacteria (horizontal gene transfer).</span></li>
    <li data-i="12"><span class="box">✓</span><span class="code">A3.1.13</span><span>Same chromosome number maintained by sexual reproduction; triploid Bramley apple is sterile but fruits.</span></li>
    <li data-i="13"><span class="box">✓</span><span class="code">A3.1.14</span><span>Construct a dichotomous key for a group of local organisms.</span></li>
    <li data-i="14"><span class="box">✓</span><span class="code">A3.1.15</span><span>DNA barcodes (CO1) and environmental DNA: Gouldian finch waterholes, fisher in snow.</span></li>
  </ul>
</section>
""")
BODY.append(r"""</div>

<footer class="foot">A3.1 Diversity of Organisms · built for Travis · grounded in Allott &amp; Mindorff, Oxford IB Biology 2023 (pp. 97–115)</footer>

</body>
""")
print("tail ok", len(BODY[-1]))

OUT_DIR.mkdir(parents=True, exist_ok=True)
page = head + "\n".join(BODY) + "\n" + script
OUT.write_text(page, encoding="utf-8")
print("WROTE", OUT)
print("bytes:", len(page.encode("utf-8")))
