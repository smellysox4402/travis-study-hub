#!/usr/bin/env python3
"""Anki cloze deck builder: Chem HL — Atomic Structure & Periodicity (S1.2 + S1.3 + S3.1).
Matches the user's 'Cloze+' model (Text + Back Extra) in the 'Chem HL' deck.
Run: python scripts/build_atomic_structure_anki.py
"""
import genanki
import os

MODEL_ID = 1607392319
DECK_ID = 2059400112
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "chem", "atomic-structure-periodicity", "Chem_Atomic_Structure_Periodicity.apkg")

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

# ── S1.2.1 · The nuclear atom ──
add("The atom = a {{c1::positively charged nucleus}} (protons + neutrons, i.e. {{c2::nucleons}}) surrounded by {{c3::electrons}}. The nucleus holds essentially {{c4::all the mass}} but is only about 1/100 000 of the atom's diameter.",
    "Proton: relative mass 1, charge +1. Neutron: mass 1, charge 0. Electron: mass negligible, charge −1.")
add("Rutherford's gold foil experiment: MOST alpha particles {{c1::passed straight through}} (atom mostly empty space), a FEW {{c2::bounced back}} (tiny, dense, {{c3::positive}} nucleus). This falsified the {{c4::plum-pudding}} model.",
    "Some deflected slightly → passing near a positive nucleus. ~1 in 8000 bounced back.")
add("Nuclear symbol ᴬ_Z X: A = {{c1::mass number}} = protons + neutrons; Z = {{c2::atomic number}} = protons; A = Z + {{c3::N}}.",
    "Neutral atom: electrons = protons. ¹⁹⁷₇₉Au has 197 − 79 = 118 neutrons.")
add("Ion electron count: charge = {{c1::protons − electrons}}. ²⁴₁₂Mg²⁺ has 12 p⁺, 12 n, {{c2::10 e⁻}}. ¹⁶₈O²⁻ has 8 p⁺, 8 n, {{c3::10 e⁻}}.",
    "Cations: electrons lost. Anions: electrons gained.")
add("1 pm = {{c1::10⁻¹² m}}; 1 Å (angstrom) = {{c2::10⁻¹⁰ m}}. Fluorine atomic radius = 60 pm = {{c3::0.60 Å}}.",
    "Atom diameter ≈ 1 × 10⁻¹⁰ to 5 × 10⁻¹⁰ m.")

# ── S1.2.2 · Isotopes + relative atomic mass ──
add("Isotopes = same number of {{c1::protons}}, different number of {{c1::neutrons}} → same {{c2::chemical}} properties, different {{c3::physical}} properties.",
    "Same Z, different N → different A. H: protium ¹H, deuterium ²H, tritium ³H (radioactive). ²H₂O bp 101.4 °C vs ¹H₂O 100.0 °C.")
add("A_r (relative atomic mass) = {{c1::weighted average of isotope masses using natural abundance}}: Σ(mass × NA) ÷ {{c2::100}}.",
    "Boron: ¹¹B 80.1%, ¹⁰B 19.9% → A_r = (11×80.1 + 10×19.9)/100 = 10.8.")
add("Iron A_r from ⁵⁴Fe 5.845%, ⁵⁶Fe 91.754%, ⁵⁷Fe 2.119%, ⁵⁸Fe 0.282% = {{c1::55.91}}.",
    "(54×5.845 + 56×91.754 + 57×2.119 + 58×0.282)/100 = 55.91.")
add("Chlorine (A_r = 35.45) is ³⁵Cl/³⁷Cl. Abundance split: {{c1::77.5% ³⁵Cl, 22.5% ³⁷Cl}}.",
    "(35x + 37(100−x))/100 = 35.45 → x = 77.5. Real values 75.8/24.2 — mass numbers are rounded.")

# ── S1.2.3 · Mass spectrometry ──
add("Mass spectrometer stages in order: {{c1::vaporize → ionize → accelerate → deflect → detect}}.",
    "Electron beam knocks electrons off → cations M⁺. Deflection depends on m/z.")
add("In the mass spectrometer, deflection depends on {{c1::mass-to-charge ratio (m/z)}} — the {{c2::lightest/most charged}} ions are deflected most. Uncharged particles {{c3::aren't deflected at all}}.",
    "Neutral fragments never reach the detector.")
add("A_r from a mass spectrum of boron (peaks m/z 10 at 19.9%, m/z 11 at 80.1%) = {{c1::10.8}}.",
    "(11 × 80.1 + 10 × 19.9)/100 = 10.8. Tallest peak = most abundant isotope.")

# ── S1.3.1 · Spectra ──
add("Spectrum types: hot gas → {{c1::line emission}} (bright lines on dark); cold gas in front of a white source → {{c2::absorption}} (dark lines on rainbow); hot solid → {{c3::continuous}}.",
    "Emission spectrum = the element's barcode. Na streetlamp: 589.0 + 589.6 nm yellow-orange.")
add("Flame test colours: Li = {{c1::red}}, Na = {{c2::yellow-orange}}, K = {{c3::lilac}}, Ca = {{c4::brick-red}}, Cu = {{c5::blue-green}}, Sr = {{c5::crimson}}.",
    "Same physics as emission spectra: excited electrons fall back and emit visible photons.")

# ── S1.3.2 · Hydrogen spectrum / Bohr ──
add("The line emission spectrum of hydrogen is evidence for {{c1::discrete (quantized) energy levels}} — only certain photon energies exist. The lines {{c2::converge}} at higher energy.",
    "Bohr 1913: fixed orbits; absorb photon of exactly ΔE → jump up; fall back → emit exact ΔE.")
add("c = {{c1::f × λ}} (c = 3.00 × 10⁸ m s⁻¹). E = {{c2::h × f}} (h = 6.63 × 10⁻³⁴ J s). Energy ∝ {{c3::1/λ}}.",
    "EM order: gamma → X-ray → UV → visible → IR → microwave → radio. Short λ = high E.")
add("Hydrogen visible (Balmer) lines — falling to n = 2: {{c1::656 nm red}} (3→2), {{c2::486 nm cyan}} (4→2), {{c3::434 nm blue}} (5→2), {{c4::410 nm violet}} (6→2).",
    "To n = 1 → UV (Lyman). To n = 3 → IR (Paschen).")
add("Hydrogen transitions to n = 1 are in the {{c1::UV}}; to n = 2 in the {{c2::visible}}; to n = 3 in the {{c3::IR}}.",
    "The Balmer series is the visible one — the four colours 656/486/434/410 nm.")

# ── S1.3.3 · 2n² ──
add("Maximum electrons in energy level n = {{c1::2n²}}: n=1 → {{c2::2}}, n=2 → {{c3::8}}, n=3 → {{c4::18}}, n=4 → {{c5::32}}.",
    "Evidence: successive IE big jumps match these shell sizes.")

# ── S1.3.4 · Sublevels & orbitals ──
add("Sublevels in order of increasing energy: {{c1::s < p < d < f}}. Orbitals per sublevel: s = {{c2::1}}, p = {{c3::3}}, d = {{c4::5}}, f = {{c5::7}}.",
    "Each orbital holds max 2 electrons → s 2, p 6, d 10, f 14.")
add("Orbital shapes: s = {{c1::spherical}}; p = {{c2::dumbbell}} (px, py, pz at right angles); d = {{c3::cloverleaf}}.",
    "An orbital = region with high (~99%) probability of finding the electron.")
add("Energy level n=3 contains the sublevels {{c1::3s + 3p + 3d}} = {{c2::9 orbitals}} = {{c3::18 electrons}} max.",
    "Level 1: 1 orbital (2 e⁻). Level 2: 4 orbitals (8 e⁻). Level 4: 16 orbitals (32 e⁻).")

# ── S1.3.5 · Aufbau / Pauli / Hund / configurations ──
add("Pauli exclusion principle: max {{c1::2 electrons per orbital}}, with {{c2::opposite spins}}. Hund's rule: fill degenerate orbitals {{c3::singly first, same spin}}, then pair up.",
    "Degenerate = same energy (the three 2p orbitals). Spreading out first minimises repulsion.")
add("Aufbau filling order: {{c1::1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p}} — note {{c2::4s fills BEFORE 3d}}.",
    "Read the ladder diagonally. IB tests writing configurations up to Z = 36 (krypton).")
add("Full config of Ca = {{c1::1s² 2s² 2p⁶ 3s² 3p⁶ 4s²}}; condensed = {{c2::[Ar]4s²}}.",
    "Noble-gas core + valence electrons.")
add("The two config exceptions: Cr = {{c1::[Ar]4s¹3d⁵}} and Cu = {{c2::[Ar]4s¹3d¹⁰}} — half-filled/full d sublevel is extra stable.",
    "NOT 4s²3d⁴ / 4s²3d⁹.")
add("Ions lose the highest-n electrons first: Mn²⁺ = {{c1::[Ar]3d⁵}}; Fe²⁺ = {{c2::[Ar]3d⁶}}; Fe³⁺ = {{c3::[Ar]3d⁵}}.",
    "4s empties BEFORE 3d even though it filled first. Half-filled d⁵ = stability bonus.")

# ── S1.3.6 · Convergence limit → IE ──
add("The limit of convergence of an emission spectrum = the energy to {{c1::remove the electron completely (ionization energy)}}.",
    "H converges at 9.12 × 10⁻⁸ m → E = hc/λ = 2.18 × 10⁻¹⁸ J per atom.")
add("Ionization energy of hydrogen from the convergence limit: {{c1::2.18 × 10⁻¹⁸ J atom⁻¹}} = {{c2::1312 kJ mol⁻¹}} (× N_A, ÷ 1000).",
    "Matches the data booklet value for H.")

# ── S1.3.7 · Successive IE ──
add("First ionization energy (definition): {{c1::minimum energy to remove one electron from one mole of gaseous atoms}} — X(g) → X⁺(g) + e⁻.",
    "Always gaseous state, always minimum energy.")
add("Successive ionization energies {{c1::always increase}}, and the {{c2::big jump}} appears when an electron is removed from an inner (core) shell. Group = {{c3::number of electrons before the jump}}.",
    "Na: jump after IE₁ → group 1. Mg: after IE₂ → group 2. Al: after IE₃ → group 13.")

# ── S3.1.1–3.1.3 · The table ──
add("Periodic table: period = {{c1::row}} (1–7), group = {{c2::column}} (1–18), block = {{c3::outer sublevel (s, p, d, f)}}. Modern table ordered by {{c4::atomic number}}; Mendeleev ordered by {{c5::atomic mass}} and predicted {{c6::gallium}}.",
    "Mendeleev 1869 left gaps for undiscovered elements — eka-aluminium = gallium.")
add("Group number = {{c1::number of valence electrons}} (groups 1–2: the number itself; groups 13–18: the {{c2::last digit}}). Period number = {{c3::principal quantum number n}} of the outer shell.",
    "Group 2 = 2 valence e⁻. Group 17 = 7 valence e⁻. Na in period 3 → outer electrons in n = 3.")
add("Group names: group 1 = {{c1::alkali metals}}, group 2 = {{c2::alkaline earth metals}}, group 17 = {{c3::halogens}}, group 18 = {{c4::noble gases}}, groups 3–11 = {{c5::transition elements}}.",
    "Metalloids straddle the zig-zag line: B, Si, Ge, As, Sb, Te. Metals ≈ 80% of elements.")

# ── S3.1.4 · Trends ──
add("Atomic radius {{c1::decreases across a period}} (higher nuclear charge, same shell, no new shielding) and {{c2::increases down a group}} (new shells + more shielding).",
    "Effective nuclear charge Z_eff drives it: what the outer electrons actually feel.")
add("Ionic radius: cations {{c1::smaller}} than the parent atom (fewer e⁻, same protons); anions {{c2::larger}} (extra e⁻). Isoelectronic series sized by protons: {{c3::O²⁻ > F⁻ > Ne > Na⁺ > Mg²⁺}}.",
    "Same electron configuration, more protons = smaller.")
add("First ionization energy {{c1::increases across}} a period, {{c2::decreases down}} a group. Electronegativity {{c3::increases across}}, {{c4::decreases down}} (F = {{c5::4.0}}, the max).",
    "Electron affinity: more negative across, less negative down. Metallic character follows IE: alkali metals more reactive down, halogens less reactive down.")

# ── S3.1.5 · IE discontinuities (AHL) ──
add("IE₁ discontinuity Be → B: boron's 2p electron is {{c1::shielded by the 2s² pair}} (s sublevel penetrates more than p) → {{c2::IE₁(B) < IE₁(Be)}}. Mirrored by {{c3::Mg → Al}}.",
    "New electron enters a higher-energy sublevel, not the same one.")
add("IE₁ discontinuity N → O: nitrogen's 2p³ is {{c1::half-filled (stable)}}; oxygen's extra electron suffers {{c2::pairing repulsion}} → {{c3::IE₁(O) < IE₁(N)}}. Mirrored by {{c3::P → S}}.",
    "Half-filled (p³, d⁵) and filled (p⁶, d¹⁰) sublevels are extra stable — this explains Cr and Cu.")

# ── S3.1.6 · Oxidation states (AHL) ──
add("Oxidation state rules: free element = {{c1::0}}; F always {{c2::−1}}; O usually {{c3::−2}} (peroxides −1, OF₂ +2); H usually {{c4::+1}} (metal hydrides −1); sum = {{c5::0}} in a compound, {{c5::ion charge}} in a polyatomic ion.",
    "Group 1 = +1, group 2 = +2. MnO₄⁻: Mn = +7 → manganate(VII).")
add("Naming oxyanions with oxidation state: MnO₄⁻ = {{c1::manganate(VII)}}; SO₄²⁻ = {{c2::sulfate(VI)}}; NO₃⁻ = {{c3::nitrate(V)}}; Cr₂O₇²⁻ = {{c4::dichromate(VI)}}.",
    "Transition metals show variable oxidation states because successive IEs are close: Fe +2/+3, Cu +1/+2, Mn +2/+4/+7.")

# ── S3.1.7 · Oxides (AHL) ──
add("Period 3 oxide trend: Na₂O and MgO {{c1::basic}} → Al₂O₃ {{c2::amphoteric}} → SiO₂, P₄O₁₀, SO₂, SO₃ {{c3::acidic}}.",
    "Metal oxides = Lewis bases (make hydroxides in water). Non-metal oxides = Lewis acids.")
add("Na₂O + H₂O → {{c1::2NaOH}}; SO₃ + H₂O → {{c2::H₂SO₄}}; SO₂ + H₂O → {{c3::H₂SO₃}}; P₄O₁₀ + 6H₂O → {{c4::4H₃PO₄}}; CO₂ + H₂O → {{c5::H₂CO₃}}.",
    "MgO + H₂O → Mg(OH)₂ (weak base). Acid rain: SO₂ + NOₓ from fossil fuels → pH below ~5.6.")
add("Al₂O₃ amphoteric: with acid → {{c1::2AlCl₃ + 3H₂O}}; with base (NaOH) → {{c2::2Na[Al(OH)₄]}}.",
    "Al₂O₃ + 6HCl → 2AlCl₃ + 3H₂O; Al₂O₃ + 2NaOH + 3H₂O → 2Na[Al(OH)₄].")

# ── S3.1.8 · Alkali metals & halogens (AHL) ──
add("Alkali metal + water: 2M + 2H₂O → {{c1::2MOH + H₂}}. Reactivity {{c2::increases down}} the group (IE falls). Na: fizzes, molten ball, OH⁻ → phenolphthalein {{c3::pink}}.",
    "Cs detonates. Na₂O + H₂O → 2NaOH is the oxide version.")
add("Halogen displacement: X₂ + 2X'⁻ → {{c1::2X⁻ + X'₂}}. Cl₂ + 2Br⁻ → {{c2::2Cl⁻ + Br₂}} (orange-brown). More electronegative halogen oxidises the {{c3::halide of the less electronegative}}.",
    "Reactivity decreases down: F₂ > Cl₂ > Br₂ > I₂. F₂ is the strongest oxidising agent of the group.")

# ── S3.1.9 · Transition elements (AHL) ──
add("Transition element = element with {{c1::partially filled d sublevel}} in its atom {{c2::or in any of its common stable ions}} (groups 3–11). Zn²⁺ ([Ar]{{c3::3d¹⁰}}) is NOT one; Sc³⁺ ([Ar]{{c4::3d⁰}}) is not either.",
    "Zinc's d is full → colourless compounds. Sc only +3 → empty d.")
add("Transition element properties: variable {{c1::oxidation states}}, {{c2::coloured}} complexes, {{c3::paramagnetic}} (unpaired d electrons), catalytic activity, high mp/density.",
    "Variable states because successive IEs are close (4s and 3d similar energy). Catalytic converter: 2CO + O₂ → 2CO₂ over Pt/Pd/Rh.")

# ── S3.1.10 · Complexes & colour (AHL) ──
add("A complex ion = central {{c1::transition metal cation}} + {{c2::ligands}} (molecules/ions with lone pairs: H₂O, Cl⁻, NH₃) joined by {{c3::coordinate bonds}}.",
    "Example: [Cr(H₂O)₆]³⁺ is violet.")
add("Why transition complexes are coloured: ligands {{c1::split the five d orbitals}} into two energy sets; the gap ΔE matches a {{c2::visible wavelength}} which gets {{c3::absorbed}}; you see the {{c4::complementary colour}}.",
    "Observed = opposite on the colour wheel from absorbed. [Cr(H₂O)₆]³⁺ absorbs yellow (~585 nm) → looks violet.")
add("Factors controlling the d-splitting gap: {{c1::ligand strength}} (stronger ligand = bigger split = higher-energy light absorbed), {{c2::identity of the central ion}}, and {{c3::its oxidation state}}.",
    "Weaker ligand (Cl⁻) = smaller split = lower-energy (longer λ) absorbed. [Co(H₂O)₆]²⁺ pink → [CoCl₄]²⁻ blue.")
add("[CuCl₄]²⁻ appears the colour of 647 nm (orange-red) light → it ABSORBS the complement {{c1::491 nm}} (blue-green).",
    "f = c/λ = 3.00×10⁸/491×10⁻⁹ = 6.11×10¹⁴ s⁻¹ → E = hf = 4.05×10⁻¹⁹ J — that's the d-orbital gap.")

print(f"Built {len(deck.notes)} cards -> {OUT}")
genanki.Package(deck).write_to_file(OUT)
