#!/usr/bin/env python3
"""Build B1.1 Carbohydrates & Lipids cloze deck for the Bio HL deck. Usage: python build_b11_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","b1.1-carbohydrates-lipids","B1.1_Carbohydrates_and_Lipids.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Carbon forms up to {{c1::four}} covalent bonds, allowing chains, branches and rings.","Carbon chemistry. (b1.1.1)"),
("A {{c1::condensation}} reaction links monomers into a polymer, removing a water molecule.","Condensation. (b1.1.2)"),
("{{c1::Hydrolysis}} splits a polymer into monomers by adding a water molecule.","Hydrolysis. (b1.1.3)"),
("{{c1::Pentoses}} are 5-carbon sugars and {{c2::hexoses}} are 6-carbon sugars.","Monosaccharides. (b1.1.4)"),
("Glucose is {{c1::soluble}}, {{c2::chemically stable}} and yields {{c3::energy}} on oxidation.","Glucose properties. (b1.1.4)"),
("{{c1::Starch}} (plants) and {{c2::glycogen}} (animals) are compact, largely insoluble energy-storage polysaccharides.","Storage polysaccharides. (b1.1.5)"),
("Starch and glycogen are compact because of {{c1::coiling}} and {{c2::branching}}.","Compactness. (b1.1.5)"),
("Cellulose is made of {{c1::β-glucose}} in alternating orientation, giving {{c2::straight chains}} that form strong bundles.","Cellulose. (b1.1.6)"),
("{{c1::Glycoproteins}} are involved in cell-cell recognition; {{c2::ABO blood group antigens}} are an example.","Glycoproteins. (b1.1.7)"),
("Lipids dissolve in {{c1::non-polar}} solvents but are only sparingly soluble in water.","Lipids. (b1.1.8)"),
("A {{c1::triglyceride}} is one glycerol + three fatty acids; a {{c2::phospholipid}} is one glycerol + two fatty acids + a phosphate group.","Triglyceride vs phospholipid. (b1.1.9)"),
("Phospholipids are {{c1::amphipathic}} — with a hydrophilic head and hydrophobic tails.","Amphipathic. (b1.1.9)"),
("A {{c1::saturated}} fatty acid has no C=C bonds (higher melting point); a {{c2::polyunsaturated}} one has two or more (lower melting point).","Fatty acids. (b1.1.10)"),
("Triglycerides are stored in {{c1::adipose}} tissue for energy storage and thermal insulation.","Adipose. (b1.1.11)"),
("A {{c1::phospholipid bilayer}} forms because heads are hydrophilic and tails are hydrophobic.","Bilayer. (b1.1.12)"),
("Steroids such as {{c1::oestradiol}} and {{c2::testosterone}} are non-polar and can pass straight through the phospholipid bilayer.","Steroids. (b1.1.13)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
