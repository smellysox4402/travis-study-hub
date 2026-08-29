#!/usr/bin/env python3
"""Build D2.3 Water Potential cloze deck for the Bio HL deck. Usage: python build_d23_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","d2.3-water-potential","D2.3_Water_Potential.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Water dissolves solutes by {{c1::hydrogen bonds}} and ion-dipole attractions (solvation).","Solvation. (d2.3.1)"),
("By osmosis, water moves toward the {{c1::higher solute concentration}}.","Osmosis direction. (d2.3.2)"),
("In a {{c1::hypotonic}} environment, water moves into the cell; in a {{c2::hypertonic}} one, out.","Tonicity. (d2.3.3)"),
("An animal cell in a hypotonic solution {{c1::swells and may burst}}; in a hypertonic one it {{c2::crenates}}.","No wall. (d2.3.5)"),
("A plant cell in a hypotonic solution develops {{c1::turgor pressure}}; in a hypertonic one it {{c2::plasmolyses}}.","Wall. (d2.3.6)"),
("{{c1::Isotonic}} solutions are used as IV fluids and for bathing organs for transplantation.","Medical. (d2.3.7)"),
("AHL water potential is the {{c1::potential energy of water per unit volume}}; only differences are measurable.","Water potential. (d2.3.8)"),
("AHL water moves from {{c1::higher}} to {{c2::lower}} water potential.","Direction. (d2.3.9)"),
("AHL ψw = {{c1::ψs + ψp}}.","Equation. (d2.3.10)"),
("AHL solute potential ({{c1::ψs}}) is negative and pressure potential ({{c2::ψp}}) is usually positive (turgor).","Potentials. (d2.3.10)"),
("AHL a turgid cell has positive {{c1::pressure potential}} and negative {{c2::solute potential}}.","Turgid. (d2.3.11)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
