#!/usr/bin/env python3
"""Anki cloze deck builder: Chem HL — Organic Chemistry (S3.2 + R3.3 + R3.4).
Matches the user's 'Cloze+' model (Text + Back Extra) in the 'Chem HL' deck.
Run: python scripts/build_organic_anki.py
"""
import genanki
import os

MODEL_ID = 1607392319
DECK_ID = 2059400112
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "chem", "organic-chemistry", "Chem_Organic.apkg")

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

# ── S3.2.1 · Formulas ──
add("The {{c1::empirical}} formula is the simplest whole-number ratio of atoms; the {{c2::molecular}} formula gives the actual numbers. Glucose: C₆H₁₂O₆ → empirical {{c3::CH₂O}}.",
    "Neither shows structure — that's what structural formulas are for.")
add("The three types of structural formula: {{c1::full (displayed)}} — every atom and bond; {{c2::condensed}} — atoms in order, bonds implied (CH₃CH₂CH₃); {{c3::skeletal}} — vertices and line-ends are carbons, H hidden, functional atoms shown.",
    "Skeletal example: propan-2-ol shows the chain as a zig-zag plus an explicit OH.")
add("Carbon forms {{c1::4}} bonds and its ability to chain up is called {{c2::catenation}} → straight, branched or cyclic structures.",
    "That's why carbon chemistry dwarfs all other elements combined.")

# ── S3.2.2 · Functional groups ──
add("A functional group is {{c1::the atom or group of atoms that determines a compound's physical and chemical characteristics}}.",
    "Same group → same class → similar chemical properties. R = any carbon-containing group.")
add("The -OH group makes a compound an {{c1::alcohol}} (suffix -ol); the carbonyl in the middle of a chain makes a {{c2::ketone}} (-one); a terminal carbonyl makes an {{c3::aldehyde}} (-al).",
    "Ethanol, propanone, ethanal.")
add("The carboxyl group {{c1::–COOH}} gives carboxylic acids (suffix -oic acid); R–O–R' is an {{c2::ether}}; R–NH₂ is an {{c3::amine}} (-amine); R–COO–R' is an {{c4::ester}} (-oate); R–C(=O)NH₂ is an {{c5::amide}}.",
    "Examples: ethanoic acid, methoxymethane, ethanamine, methyl ethanoate, ethanamide.")
add("Saturated = {{c1::all C–C bonds single}} (alkanes). Unsaturated = {{c2::at least one C=C or C≡C}} (alkenes, alkynes).",
    "Aliphatic = no aromatic ring.")

# ── S3.2.3 · Homologous series ──
add("A homologous series is a family with {{c1::the same functional group and a shared general formula}}, each member differing by {{c2::one CH₂}}.",
    "Successive members: methane, ethane, propane…")
add("General formulas: alkanes {{c1::CₙH₂ₙ₊₂}}, alkenes {{c2::CₙH₂ₙ}}, alkynes {{c3::CₙH₂ₙ₋₂}}.",
    "Alkanes: methane CH₄ … hexane C₆H₁₄. Alkenes: ethene, propene, but-2-ene.")
add("General formulas: alcohols {{c1::CₙH₂ₙ₊₁OH}}, aldehydes AND ketones {{c2::CₙH₂ₙO}}, carboxylic acids {{c3::CₙH₂ₙO₂}}, amines {{c4::CₙH₂ₙ₊₃N}}.",
    "Aldehydes and ketones share CₙH₂ₙO — the position of C=O is the only difference.")

# ── S3.2.4 · Physical trends ──
add("Along a homologous series, boiling point {{c1::increases}} with chain length because {{c2::London (dispersion) forces strengthen}}.",
    "Methane −161 °C → ethane −89 → propane −42 → butane −0.5 → pentane 36 → hexane 69 °C.")
add("Which physical trend is smooth/predictable and which is noisy? {{c1::Boiling point}} is smooth (use it to predict); {{c2::melting point}} is noisy (unreliable).",
    "Density and viscosity also rise with chain length.")

# ── S3.2.5 · Naming ──
add("IUPAC roots: 1 {{c1::meth-}}, 2 {{c2::eth-}}, 3 {{c3::prop-}}, 4 {{c4::but-}}, 5 {{c5::pent-}}, 6 {{c6::hex-}}.",
    "Alkanes end -ane, alkenes -ene, alkynes -yne.")
add("Naming rules: number the chain so substituents get the {{c1::lowest locants}}; multiple different substituents go in {{c2::alphabetical order}} (3-ethyl-2-methylhexane); identical ones get a multiplier ({{c3::2,3-dimethylhexane}}).",
    "Hyphen between locant and prefix; commas between locants.")
add("Priority order in naming: the {{c1::C=C double bond}} gets the lowest locant over substituents (4-methylhex-2-ene); {{c2::–OH}} outranks C=C (propan-2-ol); the {{c3::carboxyl carbon}} is always number 1 (no locant needed).",
    "Halogenoalkanes: 2-chloro-1,1,1-trifluoroethane; C=C beats halogen: 3-chlorobut-1-ene.")
add("Name it: CH₃COCH₂CH₃ is {{c1::butanone}}; CH₃CH(OH)CH₃ is {{c2::propan-2-ol}}; CH₃CH₂CH₂CH₂COOH is {{c3::pentanoic acid}}.",
    "4-methylpentanal: aldehyde chain of 5 with methyl at C4.")

# ── S3.2.6 · Structural isomers ──
add("Structural isomers = {{c1::same molecular formula, different connectivity of atoms}}. Three types: {{c2::chain}}, {{c3::positional}}, {{c4::functional group}}.",
    "Not stereoisomers — those keep connectivity and change 3D arrangement.")
add("Chain isomers example: {{c1::butane vs methylpropane}} (both C₄H₁₀). Positional: {{c2::1-, 2-, 3-bromopentane}} (C₅H₁₁Br). Functional group: {{c3::ethanol vs methoxymethane}} (C₂H₆O).",
    "Functional-group pairs: propanal/propanone (C₃H₆O); methyl methanoate/ethanoic acid (C₂H₄O₂).")
add("How many structural isomers does C₄H₉F have? {{c1::4}}: {{c2::1-fluorobutane, 2-fluorobutane, 1-fluoro-2-methylpropane, 2-fluoro-2-methylpropane}}.",
    "3-/4-fluorobutane are equivalent to 2-/1-fluorobutane — numbering from either end.")
add("1°, 2°, 3° = {{c1::number of carbons bonded to the functional-group carbon}}. For amines, count {{c2::carbons bonded directly to nitrogen}}.",
    "2-chloro-2-methylpropane is tertiary; propan-1-amine is primary; N-methylpropan-1-amine is secondary.")

# ── S3.2.7 · Stereoisomers (AHL) ──
add("Stereoisomers have {{c1::the same constitution but different spatial arrangements}}. The two classes: {{c2::conformational}} (rotate about single bonds) and {{c3::configurational}} (need bond-breaking).",
    "Configurational splits into cis-trans and optical. Conformers (staggered/eclipsed ethane) can't be separated.")
add("cis-trans isomerism: {{c1::cis}} = identical substituents on the same side of the C=C; {{c2::trans}} = opposite sides.",
    "But-2-ene shows it; propene does NOT (one alkene carbon has two identical H). Also in disubstituted cycloalkanes (1,2-dimethylcyclobutane).")
add("A chiral carbon is bonded to {{c1::four different atoms or groups}}. A pair of enantiomers is {{c2::non-superimposable mirror images}}.",
    "Penicillamine: C-2 chiral (H, CH₃, NH₂, COOH), C-3 achiral (two identical CH₃).")
add("Enantiomers rotate plane-polarised light by {{c1::the same angle in opposite directions}}; a racemic mixture (50:50) shows {{c2::no rotation}}.",
    "In wedge-dash drawings: wedge = toward viewer, dash = away, line = in the plane.")
add("Why do butan-2-ol enantiomers smell/taste differently in some contexts? {{c1::In chiral environments (e.g. biological molecules) enantiomers interact differently}}.",
    "Identical chemical properties in non-chiral environments.")

# ── S3.2.8 · Mass spec (AHL) ──
add("The molecular ion peak M⁺ is {{c1::the highest m/z peak, equal to the relative molecular mass}}.",
    "Propan-1-ol (Mr 60): M⁺ at m/z 60.")
add("Common MS fragments: m/z 15 = {{c1::CH₃⁺}}; 17 = {{c2::OH⁺}}; 29 = {{c3::CHO⁺ or CH₃CH₂⁺}}; 31 = {{c4::CH₃O⁺ or CH₂OH⁺}}; 45 = {{c5::COOH⁺}}.",
    "Propan-1-ol: 31 = [CH₂OH]⁺ (lost ethyl), 29 = [CH₃CH₂]⁺ (lost CH₂OH).")

# ── S3.2.9 · IR (AHL) ──
add("IR identifies {{c1::bond types / functional groups}} because bonds {{c2::vibrate}} and absorb characteristic infrared frequencies.",
    "Two vibration types: stretching/compression and bending.")
add("IR key bands: C=O at {{c1::1700–1750 cm⁻¹}} (strong); carboxylic acid O–H at {{c2::2500–3000 cm⁻¹}} (strong, very broad).",
    "From the butanoic acid spectrum (fig 28).")
add("IR-active requires {{c1::a change in dipole moment during vibration}}. So H₂, O₂ and Cl₂ are {{c2::IR-inactive}}.",
    "Heteronuclear diatomics (HF) are IR-active.")
add("Vibration frequency increases with {{c1::bond enthalpy}} and decreases with {{c2::atomic mass}}. Order: HCl {{c3::2886}} > HBr {{c4::2559}} > HI {{c5::2230}} cm⁻¹.",
    "HCl 431 kJ mol⁻¹ → HI 298: weaker bond + heavier atom = lower frequency.")

# ── S3.2.10+11 · NMR (AHL) ──
add("¹H NMR gives the number of {{c1::different chemical environments of hydrogen atoms}}; the integration (area under a signal) gives {{c2::the relative number of H in that environment}}.",
    "Reference: TMS at 0 ppm. Propanone: 1 signal. Ethanoic acid: 2 signals (COOH 9–13, CH₃ 2.0–2.5, ratio 1:3).")
add("The N + 1 rule: a proton with N neighbours splits into {{c1::N + 1 peaks}}. 0 → {{c2::singlet}}, 1 → {{c3::doublet}}, 2 → {{c4::triplet}} (1:2:1), 3 → {{c5::quartet}} (1:3:3:1).",
    "1,1,2-trichloroethane: Ha (2H) doublet, Hb (1H) triplet — they split each other.")
add("Butanone CH₃COCH₂CH₃: the CH₃ next to C=O is a {{c1::singlet}} at 2.1 ppm; the CH₂ is a {{c2::quartet}} at 2.4; the terminal CH₃ is a {{c3::triplet}} at 1.1.",
    "Neighbour counts: CH₃ next to C=O → 0 neighbours (singlet); CH₂ → 3 (quartet); terminal CH₃ → 2 (triplet).")
add("1,1-dichloroethane CH₃CHCl₂ ¹H NMR: {{c1::2 signals}}, ratio {{c2::3:1}} — CH₃ doublet at 2.0 ppm, CH quartet at 5.8 ppm.",
    "The CH has three CH₃ neighbours (quartet); CH₃ has one CH neighbour (doublet).")

# ── S3.2.12 · Combined analysis (AHL) ──
add("Worked ex (C,H,Cl): 24.27% C, 4.08% H, 71.65% Cl → empirical formula {{c1::C₂H₄Cl₂}} (Mr ≈ 99).",
    "Moles: C 2.021 : H 4.04 : Cl 2.021 → 1 : 2 : 1 with 2 Cl — i.e. C₂H₄Cl₂.")
add("In the mass spectrum of a chlorine compound, why two molecular-ion peaks (98 and 100)? {{c1::Chlorine has two isotopes, ³⁵Cl and ³⁷Cl — different combinations give different Mr}}.",
    "C₂H₄³⁵Cl₂ = 98; C₂H₄³⁵Cl³⁷Cl = 100. Fragment peaks 63/65 similar.")
add("Structure determination combines {{c1::combustion analysis (empirical formula) + MS (Mr) + IR (functional groups) + ¹H NMR (H environments)}} + data booklet.",
    "C₃H₆O + C=O at 1700–1750 + Mr 58 + not terminal C=O → propanone.")

# ── R3.3.1 · Radicals ──
add("A radical is {{c1::a chemical entity with an unpaired electron}}, shown with a dot: {{c2::Cl•, •CH₃, •OH}}.",
    "Unlike ions, radicals exist independently — no counter-ion needed.")
add("Why are radicals usually intermediates, not products? {{c1::Their high reactivity — they react on immediately}}.",
    "The free-radical theory of ageing links radical build-up to oxidative stress (still debated).")

# ── R3.3.2 · Homolytic fission ──
add("Homolytic fission = {{c1::both bonding electrons split evenly, one to each atom → two radicals}}. Drawn with {{c2::single-barbed (fish-hook) arrows}}.",
    "Cl₂ → 2 Cl•. Requires UV light or heat. This is the initiation step.")
add("Curly-arrow rules: start at {{c1::the origin of the moving electrons}}, end at {{c2::their exact destination}}, and go {{c3::electron-rich → electron-poor}}.",
    "Double-barbed arrow = electron PAIR; fish-hook = ONE electron.")

# ── R3.3.3 · Radical substitution ──
add("Radical substitution of methane: initiation {{c1::Cl₂ → 2Cl•}}; propagation {{c2::Cl• + CH₄ → HCl + •CH₃}} then {{c3::•CH₃ + Cl₂ → CH₃Cl + Cl•}}; termination {{c4::radical + radical → molecule}}.",
    "Termination options: Cl•+Cl• → Cl₂; •CH₃+Cl• → CH₃Cl; •CH₃+•CH₃ → C₂H₆ (by-product).")
add("Why does fluorination of alkanes not work well but iodination doesn't happen? {{c1::F₂ is too reactive (breaks C–C bonds); I₂ is too unreactive}}.",
    "Radical halogenation works with Cl₂ and Br₂ under UV/heat. CH₄ + Cl₂ → CH₃Cl + HCl.")
add("A propagation step is {{c1::a radical + a non-radical → a new non-radical + a new radical}} (the chain continues).",
    "MCQ trap: •C₂H₅ + Cl₂ → C₂H₅Cl + Cl• is propagation; •C₂H₅ + Cl• → C₂H₅Cl is termination.")

# ── R3.4.1–3.4.4 · Nucleophiles/electrophiles ──
add("A nucleophile is {{c1::an electron-rich species that donates an electron pair}} to form a bond. It must have {{c2::a lone pair}}.",
    "OH⁻, CN⁻, Cl⁻, H₂O, NH₃, CH₃NH₂. (CH₃)₄N⁺ can't — no lone pair.")
add("An electrophile is {{c1::an electron-deficient species that accepts an electron pair}}. Examples: {{c2::CH₃⁺ (full +), BF₃ and carbonyl carbon (δ+)}}.",
    "Carbonyl/carboxyl compounds are electrophiles at the electron-poor carbon.")
add("Heterolytic fission = {{c1::both bonding electrons stay with one fragment}} → cation + anion. Drawn with a {{c2::double-barbed arrow}} from bond to the atom taking the pair.",
    "CH₃Br → CH₃⁺ (carbocation) + Br⁻. Carbocations are short-lived intermediates.")
add("Nucleophilic substitution in general: {{c1::Nu⁻ + R–X → R–Nu + X⁻}} — the {{c2::leaving group}} takes the electron pair.",
    "CH₃CH₂Cl + OH⁻ → CH₃CH₂OH + Cl⁻. The δ+ carbon is attacked; the C–X pair moves to X.")

# ── R3.4.5 · Electrophilic addition (SL) ──
add("Why are alkenes attacked by electrophiles? {{c1::The C=C double bond is a region of high electron density (accessible π electrons)}}.",
    "Ethene + Br₂(aq) → 1,2-dibromoethane; bromine water decolourises = test for unsaturation.")
add("Electrophilic addition products: alkene + X₂ → {{c1::CₙH₂ₙX₂}} (1,2-dihalogenoalkane); alkene + HX → {{c2::CₙH₂ₙ₊₁X}}; alkene + H₂O (acid) → {{c3::alcohol}}.",
    "But-2-ene + HBr → 2-bromobutane (single product — symmetrical alkene). Hex-3-ene + H₂O → hexan-3-ol.")

# ── R3.4.6–3.4.8 · Lewis + complexes (AHL) ──
add("Lewis acid = {{c1::electron-pair acceptor}}; Lewis base = {{c2::electron-pair donor}}. Broader than Brønsted–Lowry because {{c3::no proton is required}}.",
    "BF₃ + NH₃ → F₃B–NH₃: NH₃ is Lewis base/nucleophile, BF₃ is Lewis acid/electrophile.")
add("Nucleophiles are Lewis {{c1::bases}}; electrophiles are Lewis {{c2::acids}} — all of them, and vice versa.",
    "AlCl₃ dimerises to Al₂Cl₆: Cl lone pairs coordinate to electron-deficient Al — AlCl₃ is both Lewis acid and base.")
add("Ligands are {{c1::Lewis bases that donate an electron pair to a transition-metal cation}} (a Lewis acid) forming a {{c2::coordination bond}} → complex ion.",
    "Ligands: neutral H₂O/NH₃ or anionic CN⁻/Cl⁻/OH⁻. Cu²⁺ + 6H₂O → [Cu(H₂O)₆]²⁺ (octahedral, blue).")
add("Charge on a complex ion = {{c1::metal charge + Σ(ligand charge)}}. So [CoCl₄] with Co(II): {{c2::2 + 4×(−1) = −2}}; [Fe(OH)(H₂O)₅]²⁺ → Fe is {{c3::3+}}.",
    "Ti in [TiF₆]²⁻: (−2) − 6×(−1) = +4. Co equilibrium: [Co(H₂O)₆]²⁺ pink ⇌ [CoCl₄]²⁻ blue.")

# ── R3.4.9–3.4.10 · SN1 vs SN2 (AHL) ──
add("SN2: {{c1::one concerted step}} with a {{c2::backside attack}} (180° from the leaving group) → {{c3::inversion}} of configuration. Rate = {{c4::k[R–X][Nu⁻]}} (second order).",
    "Primary halogenoalkanes. No intermediate — only a transition state (dotted partial bonds in brackets). The '2' = two molecules in the slow step.")
add("SN1: {{c1::two steps}} — C–X bond breaks first to a {{c2::carbocation}} (slow, rate-determining), then the nucleophile attacks. Rate = {{c3::k[R–X]}} (first order).",
    "Tertiary halogenoalkanes. Carbocation stability: 3° > 2° > 1° (alkyl groups donate electron density — inductive effect).")
add("Carbocation stability order and why: {{c1::3° > 2° > 1°}} because {{c2::alkyl groups donate electron density, spreading the positive charge}}.",
    "Tertiary halogenoalkanes go SN1; primary go SN2; secondary can do either.")
add("Leaving group speed order: {{c1::I > Br > Cl > F}} because {{c2::the weaker the C–X bond, the faster the fission}} (C–I 228 < C–Br 285 < C–Cl 324 < C–F 492 kJ mol⁻¹).",
    "Fluoroalkanes are virtually inert. Fastest: 2-iodopropane > 2-bromopropane > 2-chloropropane.")

# ── R3.4.11–3.4.12 · Addition mechanisms + Markovnikov (AHL) ──
add("Electrophilic addition mechanism: (1) {{c1::electrophile attacks the π bond}} → carbocation; (2) {{c2::the anion/nucleophile attacks the carbocation}}.",
    "Br₂ + ethene: Br⁺ adds first, then Br⁻ attacks the cation → 1,2-dibromoethane.")
add("Markovnikov's rule: the {{c1::electropositive part (H) bonds to the carbon with the fewest alkyl substituents}} → carbocation forms on the {{c2::most substituted carbon}}.",
    "HBr + propene → 2-bromopropane (major, via 2° carbocation) + 1-bromopropane (minor, via 1°).")
add("Why is 2-bromopropane the major product of HBr + propene? {{c1::It forms via the more stable secondary carbocation; 1-bromopropane needs a primary one}}.",
    "Secondary carbocation > primary: inductive donation from two alkyl groups.")

# ── R3.4.13 · Benzene (AHL) ──
add("Benzene undergoes {{c1::electrophilic substitution}} not addition because {{c2::the aromatic ring is too stable to add across (breaking aromaticity costs energy)}}.",
    "Nitration is the standard example: benzene + NO₂⁺ → nitrobenzene.")
add("The nitronium ion is made: {{c1::HNO₃ + H₂SO₄ → H₂NO₃⁺ + HSO₄⁻ → NO₂⁺ + H₂O}}.",
    "Pure HNO₃ has only traces of NO₂⁺; the acid mixture boosts it (higher concentration → faster nitration).")
add("Nitration mechanism: NO₂⁺ attacks the {{c1::delocalised π ring}} → carbocation (aromaticity broken, {{c2::rate-determining}}) → {{c3::H⁺ leaves (water takes it)}} → aromaticity restored.",
    "Drawing rules: incomplete dashed circle + positive charge on the ring; curly arrow for H⁺ leaving starts at the C–H bond; show H⁺/H₃O⁺ product.")

# sanity
print("notes:", len(deck.notes))
genanki.Package(deck).write_to_file(OUT)
print("OK:", OUT)
