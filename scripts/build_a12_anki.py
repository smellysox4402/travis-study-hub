#!/usr/bin/env python3
"""Build A1.2 Nucleic Acids cloze deck for the Bio HL deck.
Matches the existing 'Cloze+' note model.  Usage: python build_a12_anki.py
"""
import genanki, os
MODEL_ID = 1607392319
DECK_ID  = 2059400110
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "a1.2-nucleic-acids", "A1.2_Nucleic_Acids.apkg")
model = genanki.Model(MODEL_ID, "Cloze+", fields=[{"name":"Text"},{"name":"Back Extra"}],
    templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}], model_type=1)

CARDS = [
# --- A1.2.1 genetic material ---
("The genetic material of all living organisms is {{c1::DNA}}.", "The hereditary molecule. (a1.2.1)"),
("Some viruses use {{c1::RNA}} as their genetic material, but they are not classified as {{c2::living}}.", "Viruses aren't alive. (a1.2.1)"),
# --- A1.2.2 nucleotide ---
("A nucleotide is made of a {{c1::phosphate group}}, a {{c2::pentose sugar}} and a {{c3::nitrogenous base}}.", "Three parts. (a1.2.2)"),
("In a nucleotide diagram, the phosphate is drawn as a {{c1::circle}}, the sugar as a {{c2::pentagon}} and the base as a {{c3::rectangle}}.", "Shape convention. (a1.2.2)"),
# --- A1.2.3 backbone ---
("The phosphate of one nucleotide bonds to the {{c1::sugar}} of the next, forming a strong {{c2::covalent}} sugar-phosphate backbone.", "The backbone. (a1.2.3)"),
# --- A1.2.4 bases ---
("The four bases in DNA are {{c1::adenine (A)}}, {{c2::thymine (T)}}, {{c3::guanine (G)}} and {{c4::cytosine (C)}}.", "DNA bases. (a1.2.4)"),
("In RNA, {{c1::uracil (U)}} replaces thymine, giving the bases A, U, G, C.", "RNA bases. (a1.2.4)"),
("The {{c1::purines}} (two rings) are adenine and guanine; the {{c2::pyrimidines}} (one ring) are cytosine, thymine and uracil.", "Purines vs pyrimidines. (a1.2.4)"),
# --- A1.2.5 RNA polymer ---
("RNA is a polymer formed by {{c1::condensation}} reactions linking nucleotide monomers.", "Condensation. (a1.2.5)"),
("RNA is usually {{c1::single}}-stranded and its sugar is {{c2::ribose}}.", "RNA features. (a1.2.5)"),
# --- A1.2.6 double helix ---
("DNA is a double helix made of two {{c1::antiparallel}} strands of nucleotides.", "Antiparallel. (a1.2.6)"),
("The two DNA strands are linked by {{c1::hydrogen bonds}} between complementary base pairs.", "H-bonds. (a1.2.6)"),
("In DNA, {{c1::A}} pairs with {{c2::T}} and {{c3::G}} pairs with {{c4::C}}.", "Complementary pairs. (a1.2.6)"),
("You only need to draw DNA strands as {{c1::antiparallel}}; you do NOT need to draw the {{c2::helical}} twist.", "Exam drawing rule. (a1.2.6)"),
# --- A1.2.7 DNA vs RNA ---
("DNA is {{c1::double}}-stranded while RNA is {{c2::single}}-stranded.", "Strand count. (a1.2.7)"),
("DNA uses thymine; RNA uses {{c1::uracil}} instead.", "U vs T. (a1.2.7)"),
("DNA's pentose sugar is {{c1::deoxyribose}} (no −OH on carbon 2) while RNA's is {{c2::ribose}} (−OH on carbon 2).", "Deoxyribose vs ribose. (a1.2.7)"),
# --- A1.2.8 base pairing importance ---
("Complementary base pairing lets each DNA strand act as a {{c1::template}}, enabling {{c2::replication}} and {{c3::expression}}.", "Why complementarity matters. (a1.2.8)"),
("Complementarity is based on {{c1::hydrogen bonding}} between bases.", "Based on H-bonds. (a1.2.8)"),
# --- A1.2.9 info capacity ---
("A DNA sequence of length n has {{c1::4^n}} possible arrangements, giving it enormous information-storage capacity.", "4^n. (a1.2.9)"),
("DNA can be any {{c1::length}} with any {{c2::base sequence}}, so it can store an enormous amount of information.", "Limitless capacity. (a1.2.9)"),
# --- A1.2.10 universal code ---
("The genetic code is essentially {{c1::universal}} across all life, which is evidence of {{c2::common ancestry}}.", "Universal code. (a1.2.10)"),
# --- A1.2.11 directionality (AHL) ---
("New nucleotides are always added to the {{c1::3′ end}} of a growing strand.", "Build at 3′. (a1.2.11)"),
("The two DNA strands are {{c1::antiparallel}}: one runs 5′→3′, the other {{c2::3′→5′}}.", "Antiparallel directions. (a1.2.11)"),
("DNA polymerase reads the template {{c1::3′→5′}} and builds the new strand {{c2::5′→3′}}.", "Pol read/build. (a1.2.11)"),
("mRNA is read {{c1::5′→3′}} at the ribosome during translation.", "Translation direction. (a1.2.11)"),
# --- A1.2.12 helix stability (AHL) ---
("A {{c1::purine}} (A or G) always pairs with a {{c2::pyrimidine}} (T or C), keeping every base pair the same {{c3::width}}.", "Even-width pairs. (a1.2.12)"),
("Because A–T and G–C pairs have equal length, the DNA helix has a uniform {{c1::3D structure}} whatever the sequence.", "Uniform helix. (a1.2.12)"),
# --- A1.2.13 nucleosome (AHL) ---
("A nucleosome is DNA coiled around a core of {{c1::eight}} histone proteins.", "8 histones. (a1.2.13)"),
("An {{c1::H1}} histone holds the {{c2::linker DNA}} that connects neighbouring nucleosomes.", "H1 + linker. (a1.2.13)"),
# --- A1.2.14 Hershey-Chase (AHL) ---
("Hershey and Chase used {{c1::radioisotopes}} to label the DNA and protein of a bacteriophage.", "Radioisotope labelling. (a1.2.14)"),
("{{c1::³²P}} labels DNA; {{c2::³⁵S}} labels protein.", "Which isotope labels what. (a1.2.14)"),
("In Hershey-Chase, {{c1::³²P}} (DNA) entered the bacteria while ³⁵S (protein) stayed outside — so DNA is the genetic material.", "Result. (a1.2.14)"),
("The Hershey-Chase experiment became possible only once {{c1::radioisotopes}} were available as tools.", "NOS: technology enables experiments. (a1.2.14)"),
# --- A1.2.15 Chargaff (AHL) ---
("Chargaff found that in DNA {{c1::A ≈ T}} and {{c2::G ≈ C}}.","Base ratios. (a1.2.15)"),
("Chargaff's data {{c1::falsified}} the tetranucleotide hypothesis of a repeating sequence of four bases.", "Falsification. (a1.2.15)"),
("The idea that a hypothesis is accepted until evidence disproves it is an example of {{c1::falsification}} in science.", "Falsification concept. (a1.2.15)"),
]
deck = genanki.Deck(DECK_ID, "Bio HL")
for text, back in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, back]))
genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
