#!/usr/bin/env python3
"""Build B4.2 Transfer of Energy & Matter cloze deck for the Bio HL deck. Usage: python build_b42_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","b4.2-transfer-energy-matter","B4.2_Transfer_of_Energy_and_Matter.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("An ecological niche is a species' {{c1::role}} including all its {{c2::biotic}} and {{c3::abiotic}} interactions.","Niche. (b4.2.1)"),
("An {{c1::obligate aerobe}} needs oxygen; an {{c2::obligate anaerobe}} lives only without it; a {{c3::facultative anaerobe}} can do either.","O2 tolerance. (b4.2.2)"),
("{{c1::Photosynthesis}} is the mode of nutrition in plants, algae and photosynthetic prokaryotes.","Autotrophy. (b4.2.3)"),
("{{c1::Holozoic}} nutrition (in animals): food is ingested, digested internally and absorbed.","Holozoic. (b4.2.4)"),
("{{c1::Euglena}} is a mixotrophic protist, using both autotrophic and heterotrophic nutrition.","Mixotrophy. (b4.2.5)"),
("{{c1::Saprotrophic}} fungi and bacteria digest dead organic matter and are called {{c2::decomposers}}.","Saprotroph. (b4.2.6)"),
("Archaea are one of the {{c1::three domains}} of life and are metabolically very {{c2::diverse}}.","Archaea. (b4.2.7)"),
("A {{c1::herbivorous}} member of the Hominidae has broad grinding molars; an {{c2::omnivore}} has a mix of teeth.","Dentition. (b4.2.8)"),
("Leaf-eating insects use {{c1::piercing and chewing mouthparts}}; plants defend with {{c2::thorns}}, {{c3::toxins}} and {{c4::tannins}}.","Herbivore/plant. (b4.2.9)"),
("Predators have {{c1::teeth/claws/speed/senses}}; prey use {{c2::chemical}}, physical and behavioural defences.","Predator/prey. (b4.2.10)"),
("Understorey forest plants harvest light with {{c1::large broad leaves}}.","Light harvesting. (b4.2.11)"),
("The {{c1::fundamental niche}} is the potential range; the {{c2::realised niche}} is the actual (smaller) range.","Niche types. (b4.2.12)"),
("{{c1::Competitive exclusion}}: two species cannot occupy the same niche — one is eliminated or both are restricted.","Exclusion. (b4.2.13)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
