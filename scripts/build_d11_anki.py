#!/usr/bin/env python3
"""Build D1.1 DNA Replication cloze deck for the Bio HL deck. Usage: python build_d11_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","d1.1-dna-replication","D1.1_DNA_Replication.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("DNA replication produces {{c1::exact copies}} with identical base sequences.","Replication. (d1.1.1)"),
("Replication is {{c1::semi-conservative}}: each copy has one old and one new strand.","Semi-conservative. (d1.1.2)"),
("{{c1::Complementary base pairing}} (A-T, G-C) ensures the copies are accurate.","Accuracy. (d1.1.2)"),
("{{c1::Helicase}} unwinds the DNA and breaks hydrogen bonds.","Helicase. (d1.1.3)"),
("{{c1::DNA polymerase}} adds nucleotides to build the new strand.","Polymerase. (d1.1.3)"),
("{{c1::PCR}} (uses primers, temperature changes, Taq polymerase) amplifies DNA.","PCR. (d1.1.4)"),
("{{c1::Gel electrophoresis}} separates DNA fragments by size.","Electrophoresis. (d1.1.4)"),
("{{c1::DNA profiling}} (paternity, forensics) is a key application of PCR/electrophoresis.","Application. (d1.1.5)"),
("AHL DNA polymerase adds nucleotides to the {{c1::3′}} end, growing the strand 5′→3′.","Directionality. (d1.1.6)"),
("AHL the leading strand is made {{c1::continuously}}; the lagging strand is made in {{c2::Okazaki fragments}}.","Leading/lagging. (d1.1.7)"),
("AHL {{c1::primase}} lays down the RNA primer.","Primase. (d1.1.8)"),
("AHL {{c1::DNA polymerase III}} is the main replication enzyme.","Pol III. (d1.1.8)"),
("AHL {{c1::DNA polymerase I}} removes the RNA primers and replaces them with DNA.","Pol I. (d1.1.8)"),
("AHL {{c1::DNA ligase}} joins the Okazaki fragments.","Ligase. (d1.1.8)"),
("AHL DNA polymerase III proofreads by removing a {{c1::mismatched nucleotide}} from the 3′ end and replacing it.","Proofreading. (d1.1.9)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
