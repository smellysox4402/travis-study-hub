#!/usr/bin/env python3
"""Build D2.2 Gene Expression cloze deck for the Bio HL deck. Usage: python build_d22_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","d2.2-gene-expression","D2.2_Gene_Expression.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Gene expression is the process by which gene information affects the {{c1::phenotype}} (via transcription → translation).","Gene expression. (d2.2.1)"),
("Transcription is regulated by {{c1::promoters}}, {{c2::enhancers}} and {{c3::transcription factors}}.","Regulation. (d2.2.2)"),
("Translation is regulated by the rate of {{c1::mRNA degradation}} (mRNA lasts minutes → days).","mRNA. (d2.2.3)"),
("{{c1::Epigenesis}} develops differentiation patterns without altering the DNA base sequence.","Epigenesis. (d2.2.4)"),
("The {{c1::genome}} is all the DNA; the {{c2::transcriptome}} is all the mRNA; the {{c3::proteome}} is all the proteins.","OMEs. (d2.2.5)"),
("{{c1::Methylation}} of the promoter represses transcription; histones are also epigenetic tags.","Methylation. (d2.2.6)"),
("{{c1::Epigenetic inheritance}} passes on changes to gene expression without changing DNA.","Inheritance. (d2.2.7)"),
("Air pollution can alter {{c1::methyl tags on DNA}}, changing gene expression.","Environment. (d2.2.8)"),
("Most but not all {{c1::epigenetic tags}} are removed from the ovum and sperm, then re-set.","Gametes. (d2.2.9)"),
("{{c1::Monozygotic twins}} share a genome, so differences show environmental effects on expression.","Twins. (d2.2.10)"),
("In bacteria, {{c1::lactose}} (lac operon) controls gene expression by binding the repressor.","Operon. (d2.2.11)"),
("A hormone can act as an {{c1::external factor}} affecting gene expression.","Hormone. (d2.2.11)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
