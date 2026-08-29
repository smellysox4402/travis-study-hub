#!/usr/bin/env python3
"""Build B1.2 Proteins cloze deck for the Bio HL deck. Usage: python build_b12_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","b1.2-proteins","B1.2_Proteins.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("An amino acid has a central {{c1::alpha carbon}} bonded to an amine group, carboxyl group, {{c2::R-group}} and hydrogen.","Amino acid. (b1.2.1)"),
("Amino acids join by a {{c1::condensation}} reaction to form a {{c2::peptide bond}}.","Peptide bond. (b1.2.2)"),
("amino acid + amino acid → {{c1::dipeptide + water}}.","Word equation. (b1.2.2)"),
("{{c1::Essential}} amino acids cannot be synthesised and must be obtained from food; {{c2::non-essential}} ones can be made.","Dietary amino acids. (b1.2.3)"),
("There are {{c1::20}} amino acids coded for in the genetic code, in any order and of any length → endless variety.","Infinite variety. (b1.2.4)"),
("High temperature or extreme pH can cause a protein to {{c1::denature}} (lose its specific shape).","Denaturation. (b1.2.5)"),
("R-groups can be {{c1::hydrophobic}} or {{c2::hydrophilic}} (polar/charged, acidic/basic) → protein diversity.","R-groups. (b1.2.6)"),
("The {{c1::primary structure}} (amino acid sequence) determines the protein's 3D conformation.","Primary → conformation. (b1.2.7)"),
("Secondary structure is stabilised by {{c1::hydrogen bonds}} forming {{c2::alpha helices}} and {{c3::beta-pleated sheets}}.","Secondary. (b1.2.8)"),
("Tertiary structure is held by {{c1::hydrogen bonds}}, {{c2::ionic bonds}}, {{c3::disulfide covalent bonds}} and {{c4::hydrophobic interactions}}.","Tertiary. (b1.2.9)"),
("In water-soluble globular proteins, {{c1::hydrophobic}} amino acids cluster in the core.","Hydrophobic core. (b1.2.10)"),
("{{c1::Insulin}} and {{c2::collagen}} are non-conjugated proteins; {{c3::haemoglobin}} is a conjugated protein.","Quaternary. (b1.2.11)"),
("{{c1::Globular}} proteins are spherical and soluble (e.g. insulin, haemoglobin); {{c2::fibrous}} proteins are long and insoluble (e.g. collagen).","Globular vs fibrous. (b1.2.12)"),
("During condensation, two amino acids form a dipeptide and release {{c1::water}}.","Water released. (b1.2.2)"),
("Hydrogen bonds in regular positions stabilise {{c1::secondary}} structure.","Secondary stabiliser. (b1.2.8)"),
("Integral membrane proteins have {{c1::hydrophobic}} regions that let them embed in the membrane.","Membrane proteins. (b1.2.10)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
