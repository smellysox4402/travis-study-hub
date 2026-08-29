#!/usr/bin/env python3
"""Build C4.2 Transfer of Energy & Matter cloze deck for the Bio HL deck. Usage: python build_c42_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","c4.2-transfer-energy-matter","C4.2_Transfer_of_Energy_and_Matter.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Ecosystems are {{c1::open systems}} — both energy and matter can enter and exit.","Open system. (c4.2.1)"),
("{{c1::Sunlight}} is the principal energy source sustaining most ecosystems.","Sunlight. (c4.2.2)"),
("Ecosystems in caves and below light-penetration in oceans use {{c1::chemoautotrophs}} instead.","Exceptions. (c4.2.2)"),
("Chemical energy flows from one {{c1::trophic level}} to the next as organisms feed.","Energy flow. (c4.2.3)"),
("In a food web, {{c1::arrows}} show the direction of energy flow.","Food web. (c4.2.4)"),
("Decomposers get energy from {{c1::dead organic matter}}, dead parts and faeces.","Decomposers. (c4.2.5)"),
("Autotrophs use an external {{c1::energy source}} to synthesise carbon compounds from {{c2::inorganic substances}}.","Autotroph. (c4.2.6)"),
("{{c1::Photoautotrophs}} use light; {{c2::chemoautotrophs}} use oxidation reactions.","Photo vs chemo. (c4.2.7)"),
("Heterotrophs obtain carbon compounds from {{c1::other organisms}}.","Heterotroph. (c4.2.8)"),
("Both autotrophs and heterotrophs release energy by {{c1::oxidation}} in cell respiration.","Respiration. (c4.2.9)"),
("Trophic levels: {{c1::producer}} → {{c2::primary}} → {{c3::secondary}} → {{c4::tertiary}} consumer.","Trophic levels. (c4.2.10)"),
("An {{c1::energy pyramid}} shows decreasing energy at each trophic level.","Energy pyramid. (c4.2.11)"),
("Energy is {{c1::lost}} at each trophic level (as heat), limiting the number of levels.","Energy loss. (c4.2.12-14)"),
("Primary production is biomass accumulation by {{c1::autotrophs}}.","Primary production. (c4.2.15)"),
("Secondary production is biomass accumulation by {{c1::heterotrophs}}.","Secondary production. (c4.2.16)"),
("Carbon is recycled by {{c1::photosynthesis}}, {{c2::feeding}} and {{c3::respiration}}.","Carbon cycle. (c4.2.17)"),
("An ecosystem is a carbon {{c1::sink}} if photosynthesis exceeds respiration, a {{c2::source}} if respiration exceeds photosynthesis.","Sinks/sources. (c4.2.18)"),
("{{c1::Combustion}} of biomass, peat, coal, oil and gas releases CO₂.","Combustion. (c4.2.19)"),
("The {{c1::Keeling Curve}} shows a seasonal sawtooth over a long-term CO₂ rise.","Keeling. (c4.2.20)"),
("Aerobic respiration uses {{c1::O₂}} from photosynthesis; photosynthesis uses {{c2::CO₂}} from respiration.","Gas interdependence. (c4.2.21)"),
("All chemical elements are {{c1::recycled}} in ecosystems.","Recycling. (c4.2.22)"),
("Decomposers and detritus feeders are not usually counted in {{c1::energy pyramids}}.","Not counted. (c4.2.12)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
