#!/usr/bin/env python3
"""Build D4.1 Natural Selection cloze deck for the Bio HL deck. Usage: python build_d41_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","d4.1-natural-selection","D4.1_Natural_Selection.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Natural selection is the mechanism of {{c1::evolutionary change}} via differential survival/reproduction.","Mechanism. (d4.1.1)"),
("Variation comes from {{c1::mutation}} and {{c2::sexual reproduction}}.","Variation. (d4.1.2)"),
("Overproduction of offspring and {{c1::competition}} for resources promote natural selection.","Overproduction. (d4.1.3)"),
("{{c1::Abiotic factors}} (e.g. temperature, density-independent) are selection pressures.","Abiotic. (d4.1.4)"),
("For evolution, a trait must be {{c1::heritable}}.","Heritable. (d4.1.6)"),
("{{c1::Sexual selection}} acts on traits that improve mating success.","Sexual selection. (d4.1.7)"),
("AHL the {{c1::gene pool}} is all the genes and alleles in a population.","Gene pool. (d4.1.9)"),
("AHL natural selection changes {{c1::allele frequencies}} in the gene pool.","Allele frequency. (d4.1.11)"),
("AHL {{c1::directional}} selection favours one extreme; {{c2::disruptive}} favours both extremes; {{c3::stabilizing}} favours the middle.","Selection types. (d4.1.12)"),
("AHL the Hardy–Weinberg equations are {{c1::p + q = 1}} and {{c2::p² + 2pq + q² = 1}}.","Hardy–Weinberg. (d4.1.13)"),
("AHL Hardy–Weinberg requires no mutation, no selection, no migration, {{c1::random mating}} and a {{c2::large population}}.","HW conditions. (d4.1.14)"),
("AHL {{c1::artificial selection}} is human choice of traits (crops, livestock).","Artificial. (d4.1.15)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
