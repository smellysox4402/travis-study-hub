#!/usr/bin/env python3
"""Build D1.2 Protein Synthesis cloze deck for the Bio HL deck. Usage: python build_d12_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","d1.2-protein-synthesis","D1.2_Protein_Synthesis.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("{{c1::Transcription}} is the synthesis of RNA using a DNA template (by {{c2::RNA polymerase}}).","Transcription. (d1.2.1)"),
("In transcription, adenine (A) on the DNA template pairs with {{c1::uracil (U)}} on RNA.","A-U pairing. (d1.2.2)"),
("A DNA template is {{c1::stable}}, so it can be transcribed many times without changing.","Template stability. (d1.2.3)"),
("Not all genes are {{c1::expressed}} at any given time; transcription is the first step of expression.","Expression. (d1.2.4)"),
("{{c1::Translation}} is the synthesis of a polypeptide from mRNA.","Translation. (d1.2.5)"),
("mRNA binds the {{c1::small}} subunit of the ribosome; two {{c2::tRNAs}} can bind simultaneously.","Roles. (d1.2.6)"),
("A {{c1::codon}} (mRNA) pairs with the complementary {{c2::anticodon}} (tRNA).","Codon/anticodon. (d1.2.7)"),
("The genetic code is {{c1::triplet}}, {{c2::degenerate}} and {{c3::universal}}.","Code features. (d1.2.8)"),
("During elongation the ribosome moves along mRNA and links amino acids by {{c1::peptide bonds}}.","Elongation. (d1.2.10)"),
("A {{c1::point mutation}} is a single base change that can alter protein structure.","Mutation. (d1.2.11)"),
("AHL both transcription and translation proceed {{c1::5′→3′}}.","Directionality. (d1.2.12)"),
("AHL transcription initiates at a {{c1::promoter}}, where {{c2::transcription factors}} bind.","Promoter. (d1.2.13)"),
("AHL non-coding DNA includes regulators, {{c1::introns}}, {{c2::telomeres}} and genes for {{c3::rRNA/tRNA}}.","Non-coding. (d1.2.14)"),
("AHL introns are removed and {{c1::exons}} spliced together; a 5′ cap and {{c2::poly-A tail}} are added.","RNA processing. (d1.2.15)"),
("AHL {{c1::alternative splicing}} produces different protein variants from one gene.","Splicing. (d1.2.16)"),
("AHL translation starts at the {{c1::start codon}} with the initiator tRNA.","Translation start. (d1.2.17)"),
("AHL many polypeptides are {{c1::modified}} to become functional (e.g. insulin, collagen).","Modification. (d1.2.18)"),
("AHL {{c1::proteasomes}} break down proteins and recycle amino acids.","Proteasomes. (d1.2.19)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
