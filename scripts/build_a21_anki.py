#!/usr/bin/env python3
"""Build A2.1 Origins of Cells cloze deck for the Bio HL deck. Usage: python build_a21_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","a2.1-origins-of-cells","A2.1_Origins_of_Cells.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
# A2.1.1
("The early atmosphere had {{c1::no free oxygen}}, so there was no {{c2::ozone}} layer.", "No O₂/ozone. (a2.1.1)"),
("Early Earth had high levels of {{c1::carbon dioxide}} and {{c2::methane}}, giving higher temperatures.", "Greenhouse gases. (a2.1.1)"),
("Because there was no ozone shield, {{c1::ultraviolet light}} reached the surface strongly.", "UV penetration. (a2.1.1)"),
("These conditions may have caused a variety of {{c1::carbon compounds}} to form spontaneously.", "Spontaneous organics. (a2.1.1)"),
# A2.1.2
("The smallest unit of self-sustaining life is the {{c1::cell}}.", "Cell = unit of life. (a2.1.2)"),
("Viruses are considered non-living because they cannot {{c1::reproduce on their own}} and have no {{c2::metabolism}}.", "Why viruses aren't living. (a2.1.2)"),
# A2.1.3
("Today cells can only be produced by {{c1::division of pre-existing cells}} — explaining a spontaneous origin is hard.", "Cells from cells. (a2.1.3)"),
("The four requirements for the first cells were {{c1::catalysis}}, {{c2::self-replication}}, {{c3::self-assembly}} and {{c4::compartmentalization}}.", "Four requirements. (a2.1.3)"),
("The origin-of-cells hypothesis is hard to test because the early conditions cannot be {{c1::replicated}} and protocells did not {{c2::fossilise}}.", "NOS: hard to test. (a2.1.3)"),
# A2.1.4
("The Miller–Urey experiment used water, methane, ammonia and hydrogen, passed {{c1::electric sparks}} through them.", "Simulated lightning. (a2.1.4)"),
("Miller–Urey produced {{c1::amino acids}} (and other organic compounds) — evidence organics can form spontaneously.", "Result. (a2.1.4)"),
("A limitation of Miller–Urey is that its {{c1::gas mixture}} was a guess that may not match the real early atmosphere.", "Evaluation. (a2.1.4)"),
# A2.1.5
("Fatty acids spontaneously form spherical {{c1::bilayer vesicles}} in water.", "Vesicle formation. (a2.1.5)"),
("A membrane-bound compartment allows the {{c1::internal}} chemistry to become different from the {{c2::outside}}.", "Compartmentalization. (a2.1.5)"),
# A2.1.6
("{{c1::RNA}} is thought to have been the first genetic material because it can both replicate and {{c2::catalyse}}.", "RNA world. (a2.1.6)"),
("{{c1::Ribozymes}} are RNA molecules with catalytic activity.", "Ribozymes. (a2.1.6)"),
("The ribosome uses RNA to catalyse {{c1::peptide bond formation}} during protein synthesis.", "Ribosome relic. (a2.1.6)"),
# A2.1.7
("Evidence for a last universal common ancestor includes the {{c1::universal genetic code}} and {{c2::shared genes}}.", "LUCA evidence. (a2.1.7)"),
("Other early forms of life were likely {{c1::outcompeted}} by LUCA and its descendants.", "Extinction by competition. (a2.1.7)"),
# A2.1.8
("The first living cells arose roughly {{c1::3.5 billion}} years ago.", "Immense timescale. (a2.1.8)"),
("Scientists estimate dates using the {{c1::fossil record}}, {{c2::radiometric dating}} and {{c3::molecular clocks}}.", "Dating methods. (a2.1.8)"),
# A2.1.9
("Evidence suggests LUCA evolved near {{c1::hydrothermal vents}}.", "Vent origin. (a2.1.9)"),
("Fossilised life has been found in ancient seafloor {{c1::hydrothermal vent precipitates}}.", "Fossil evidence. (a2.1.9)"),
("{{c1::Conserved sequences}} from genomic analysis point to a heat-adapted, oxygen-free ancestor.", "Genomic evidence. (a2.1.9)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
