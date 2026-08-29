#!/usr/bin/env python3
"""Build D1.3 Mutations & Gene Editing cloze deck for the Bio HL deck. Usage: python build_d13_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","d1.3-mutations-gene-editing","D1.3_Mutations_and_Gene_Editing.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Gene mutations are {{c1::substitutions}}, {{c2::insertions}} or {{c3::deletions}}.","Types. (d1.3.1)"),
("A base substitution creates a {{c1::single-nucleotide polymorphism (SNP)}}; degeneracy may keep the amino acid unchanged.","Substitution. (d1.3.2)"),
("An insertion or deletion causes a {{c1::frameshift}}, usually making the polypeptide non-functional.","Frameshift. (d1.3.3)"),
("Mutations are caused by {{c1::mutagens}} and by errors in {{c2::replication or repair}}.","Causes. (d1.3.4)"),
("Mutations are {{c1::random}} and can occur anywhere, though some bases are hypermutable.","Randomness. (d1.3.5)"),
("Germ-cell mutations are {{c1::inherited}}; somatic-cell mutations can cause {{c2::cancer}}.","Germ vs somatic. (d1.3.6)"),
("Gene mutation is the original source of {{c1::genetic variation}}.","Variation. (d1.3.7)"),
("AHL {{c1::gene knockout}} makes a gene inoperative to reveal its function.","Knockout. (d1.3.8)"),
("AHL CRISPR guide RNA directs the enzyme {{c1::Cas9}} to cut a specific DNA sequence for gene editing.","CRISPR-Cas9. (d1.3.9)"),
("AHL {{c1::conserved sequences}} are similar across species because of essential functions kept stable by selection.","Conserved. (d1.3.10)"),
("UV/ionising radiation and chemical mutagens are {{c1::mutagens}}.","Mutagens. (d1.3.4)"),
("The genetic code being {{c1::degenerate}} means a substitution may not change the amino acid.","Degeneracy. (d1.3.2)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
