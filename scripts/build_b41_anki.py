#!/usr/bin/env python3
"""Build B4.1 Adaptation to Environment cloze deck for the Bio HL deck. Usage: python build_b41_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","b4.1-adaptation-environment","B4.1_Adaptation_to_Environment.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("A habitat is the place an organism lives, described by its {{c1::geographical}} location and {{c2::physical conditions}}.","Habitat. (b4.1.1)"),
("A {{c1::mangrove}} tree is adapted to salty, waterlogged swamps (aerial roots, salt glands).","Mangrove. (b4.1.2)"),
("A dune grass is adapted to {{c1::low water}}, moving sand and high {{c2::salt}} exposure.","Dune grass. (b4.1.2)"),
("Abiotic variables such as {{c1::temperature}}, water and {{c2::salinity}} affect where species live.","Abiotic variables. (b4.1.3)"),
("A species survives within a {{c1::range of tolerance}} of a limiting factor.","Tolerance. (b4.1.4)"),
("Coral reefs need {{c1::warm}}, {{c2::shallow}}, clear, stable-salinity water with near-neutral pH.","Coral conditions. (b4.1.5)"),
("Terrestrial biomes are determined by {{c1::temperature}} and {{c2::rainfall}}.","Biome factors. (b4.1.6)"),
("Biomes are groups of ecosystems with similar communities due to {{c1::similar abiotic conditions}} and {{c2::convergent evolution}}.","Biomes. (b4.1.7)"),
("A hot-desert plant (e.g. a {{c1::cactus}}) has a waxy cuticle, spines and water storage.","Desert plant. (b4.1.8)"),
("A hot-desert animal (e.g. a {{c1::camel}}) stores fat and tolerates water loss.","Desert animal. (b4.1.8)"),
("A rainforest tree has {{c1::buttress roots}} and a tall trunk; a {{c2::sloth}} is camouflaged and slow.","Rainforest. (b4.1.8)"),
("A transect is used to correlate species {{c1::distribution}} with an {{c2::abiotic variable}}.","Transect. (b4.1.4)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
