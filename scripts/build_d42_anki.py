#!/usr/bin/env python3
"""Build D4.2 Stability & Ecosystem Change cloze deck for the Bio HL deck. Usage: python build_d42_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","d4.2-stability-ecosystem-change","D4.2_Stability_and_Ecosystem_Change.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Ecosystem stability requires a supply of {{c1::energy}}, recycling of {{c2::nutrients}}, {{c3::genetic diversity}} and a stable climate.","Requirements. (d4.2.2)"),
("{{c1::Deforestation}} of the Amazon is a possible {{c2::tipping point}} (rainforest → savannah).","Amazon. (d4.2.3)"),
("A {{c1::keystone species}} has a disproportionate impact on its community.","Keystone. (d4.2.5)"),
("Sustainable harvesting: the rate must not exceed {{c1::replenishment}}.","Sustainability. (d4.2.6)"),
("{{c1::Eutrophication}}: nutrients → algal bloom → decomposers use {{c2::oxygen}} → fish die.","Eutrophication. (d4.2.8)"),
("{{c1::Biomagnification}} concentrates persistent toxins up the food chain.","Biomagnification. (d4.2.9)"),
("{{c1::Rewilding}} restores natural processes, e.g. reintroducing apex predators.","Rewilding. (d4.2.11)"),
("AHL {{c1::ecological succession}} is the gradual change of a community over time.","Succession. (d4.2.12)"),
("AHL {{c1::primary}} succession starts on bare substrate (pioneer species).","Primary. (d4.2.13)"),
("AHL a {{c1::climax community}} is the stable final stage; {{c2::arrested succession}} is held short of it.","Climax. (d4.2.15)"),
("AHL some ecosystems show {{c1::cyclical succession}}.","Cyclical. (d4.2.14)"),
("{{c1::Microplastics}} are persistent fragments that enter the food web.","Microplastics. (d4.2.10)"),
("Agriculture sustainability is affected by {{c1::soil erosion}} and {{c2::leaching}} of nutrients.","Agriculture. (d4.2.7)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
