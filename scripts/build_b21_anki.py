#!/usr/bin/env python3
"""Build B2.1 Membranes cloze deck for the Bio HL deck. Usage: python build_b21_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","b2.1-membranes","B2.1_Membranes.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Amphipathic phospholipids form a {{c1::bilayer}} in water — the basis of cell membranes.","Bilayer. (b2.1.1)"),
("The hydrophobic core of a bilayer is impermeable to {{c1::large}} molecules and {{c2::charged/ionic}} particles.","Barrier. (b2.1.2)"),
("O₂ and CO₂ cross a membrane by {{c1::simple diffusion}} through the phospholipids.","Simple diffusion. (b2.1.3)"),
("{{c1::Integral}} proteins are embedded in the bilayer; {{c2::peripheral}} proteins are on the surface.","Membrane proteins. (b2.1.4)"),
("Osmosis is the movement of water due to {{c1::random particle}} movement; {{c2::aquaporins}} speed it up.","Osmosis. (b2.1.5)"),
("{{c1::Channel proteins}} allow specific ions to diffuse through (facilitated diffusion).","Channels. (b2.1.6)"),
("{{c1::Pumps}} use {{c2::ATP}} for active transport against the gradient.","Active transport. (b2.1.7)"),
("Selective permeability comes from {{c1::channel}} and {{c2::pump}} proteins; simple diffusion is {{c3::not}} selective.","Selectivity. (b2.1.8)"),
("Glycoprotein/glycolipid carbohydrates are on the {{c1::extracellular}} surface, used in cell recognition.","Glyco. (b2.1.9)"),
("The fluid-mosaic model: a fluid {{c1::phospholipid bilayer}} with embedded {{c2::proteins}}.","Fluid mosaic. (b2.1.10)"),
("AHL: {{c1::unsaturated}} fatty acids (lower melting point) make membranes {{c2::more fluid}}.","Fluidity. (b2.1.11)"),
("AHL: {{c1::cholesterol}} modulates membrane fluidity in animal cells.","Cholesterol. (b2.1.12)"),
("AHL: {{c1::exocytosis}} releases contents and {{c2::endocytosis}} takes material in (vesicle fusion/formation).","Vesicles. (b2.1.13)"),
("AHL: nicotinic acetylcholine receptors are a {{c1::neurotransmitter-gated}} ion channel; Na⁺/K⁺ channels are {{c2::voltage-gated}}.","Gated channels. (b2.1.14)"),
("AHL: the Na⁺/K⁺ pump moves {{c1::3 Na⁺ out}} and {{c2::2 K⁺ in}}, generating a {{c3::membrane potential}}.","Na/K pump. (b2.1.15)"),
("AHL: sodium-dependent glucose cotransport is {{c1::indirect active transport}}, used in the {{c2::small intestine}}.","Cotransport. (b2.1.16)"),
("AHL: {{c1::Cell-adhesion molecules (CAMs)}} allow cells to adhere and form tissues.","CAMs. (b2.1.17)"),
("{{c1::Aquaporins}} are membrane proteins that allow water to move quickly.","Aquaporins. (b2.1.5)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
