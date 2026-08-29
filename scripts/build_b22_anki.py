#!/usr/bin/env python3
"""Build B2.2 Organelles cloze deck for the Bio HL deck. Usage: python build_b22_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","b2.2-organelles-compartmentalization","B2.2_Organelles.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Organelles are {{c1::discrete subunits}} adapted to specific functions.", "Organelle. (b2.2.1)"),
("The {{c1::cell wall}}, {{c2::cytoskeleton}} and {{c3::cytoplasm}} are NOT considered organelles.","Not organelles. (b2.2.1)"),
("The nucleus separates transcription (nucleus) from {{c1::translation}} (cytoplasm), allowing {{c2::post-transcriptional modification}} of mRNA.","Nucleus separation. (b2.2.2)"),
("Compartmentalization {{c1::concentrates}} reactants and {{c2::separates incompatible processes}} (e.g. lysosomes).","Compartmentalization. (b2.2.3)"),
("AHL mitochondrion: {{c1::double membrane}}, small intermembrane space, large {{c2::cristae}} surface, Krebs cycle in the {{c3::matrix}}.","Mitochondrion. (b2.2.4)"),
("AHL chloroplast: large {{c1::thylakoid}} surface with photosystems, small internal fluid volume, Calvin cycle in the {{c2::stroma}}.","Chloroplast. (b2.2.5)"),
("AHL nuclear envelope: {{c1::pores}} let mRNA out; it {{c2::breaks into vesicles}} during mitosis/meiosis.","Nuclear membrane. (b2.2.6)"),
("AHL {{c1::free ribosomes}} make proteins retained in the cell; {{c2::rough ER}} ribosomes make proteins for transport/secretion.","Ribosomes vs ER. (b2.2.7)"),
("AHL the {{c1::Golgi apparatus}} processes and secretes proteins.","Golgi. (b2.2.8)"),
("AHL {{c1::clathrin}} is involved in the formation of {{c2::vesicles}}.","Vesicles. (b2.2.9)"),
("{{c1::Lysosomes}} are an example of compartmentalization separating incompatible processes.","Lysosomes. (b2.2.3)"),
("In prokaryotes, mRNA can immediately meet {{c1::ribosomes}} (no nuclear separation).","Prokaryote. (b2.2.2)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
