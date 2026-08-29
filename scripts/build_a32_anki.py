#!/usr/bin/env python3
"""Build A3.2 Classification & Cladistics cloze deck for the Bio HL deck. Usage: python build_a32_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","a3.2-classification-cladistics","A3.2_Classification_and_Cladistics.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Classification is needed because of the {{c1::immense diversity}} of species, and it facilitates {{c2::further study}}.","Why classify. (a3.2.1)"),
("The traditional hierarchy is kingdom, phylum, class, order, family, genus and {{c1::species}}.","The hierarchy. (a3.2.2)"),
("The traditional hierarchy does not always correspond to patterns of {{c1::divergence}}.","Hierarchy problem. (a3.2.2)"),
("The ideal classification follows {{c1::evolutionary relationships}}, so all members of a group share a {{c2::common ancestor}}.","Evolutionary classification. (a3.2.3)"),
("A {{c1::clade}} is a group of organisms with common ancestry and shared characteristics.","Clade. (a3.2.4)"),
("The most objective evidence for placing organisms in a clade is {{c1::base sequences}} of genes or {{c2::amino acid sequences}} of proteins.","Objective evidence. (a3.2.4)"),
("The {{c1::molecular clock}} uses the gradual accumulation of sequence differences to estimate when clades diverged.","Molecular clock. (a3.2.5)"),
("Cladograms are constructed from {{c1::base / amino acid sequence}} data.","Building cladograms. (a3.2.6)"),
("In a cladogram, the {{c1::root}} is the most ancient ancestor, a {{c2::node}} is a common ancestor, and a {{c3::terminal branch}} is a present-day group.","Cladogram terms. (a3.2.7)"),
("The three domains — {{c1::Bacteria}}, {{c2::Archaea}} and {{c3::Eukarya}} — were proposed from {{c4::rRNA}} sequence evidence in {{c5::1977}}.","Three domains. (a3.2.9)"),
("A {{c1::monophyletic}} group consists of a common ancestor and all its descendants.","Monophyletic. (a3.2.3)"),
("Cladistics can show a species belongs in a different {{c1::family}} than its appearance suggested.","Classification case study. (a3.2.8)"),
("A {{c1::node}} on a cladogram represents a speciation event (a common ancestor).","Node. (a3.2.7)"),
("Sequence differences accumulate at a roughly steady rate, so they are proportional to {{c1::time since divergence}}.","Molecular clock basis. (a3.2.5)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
