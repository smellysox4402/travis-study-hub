#!/usr/bin/env python3
"""Build C4.1 Populations & Communities cloze deck for the Bio HL deck. Usage: python build_c41_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","c4.1-populations-communities","C4.1_Populations_and_Communities.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("A population is a group of {{c1::the same species}} living in an area, whose members normally {{c2::breed}}.","Population. (c4.1.1)"),
("Population size is estimated (not counted directly) by {{c1::random sampling}}.","Random sampling. (c4.1.2)"),
("{{c1::Random quadrat}} sampling estimates population size of {{c2::sessile}} organisms.","Quadrat. (c4.1.3)"),
("The {{c1::Lincoln index}} (capture-mark-recapture) estimates population size of {{c2::motile}} organisms.","Lincoln index. (c4.1.4)"),
("{{c1::Carrying capacity}} is the maximum population the environment can sustain.","Carrying capacity. (c4.1.5)"),
("{{c1::Density-dependent}} factors provide negative-feedback control of population size.","Density-dependent. (c4.1.6)"),
("A sigmoid growth curve has a {{c1::lag}} phase, {{c2::exponential}} growth, then levelling at carrying capacity.","Sigmoid. (c4.1.7-8)"),
("{{c1::Intraspecific}} relationships are between members of the same species (competition vs cooperation).","Intraspecific. (c4.1.9)"),
("A {{c1::community}} is all the interacting organisms in an ecosystem.","Community. (c4.1.10)"),
("{{c1::Mutualism}} benefits both species (e.g. Fabaceae root nodules, Orchidaceae mycorrhizae).","Mutualism. (c4.1.12)"),
("An {{c1::invasive}} species can outcompete an {{c2::endemic}} species for resources.", "Endemic vs invasive. (c4.1.13)"),
("The {{c1::chi-squared}} test is used for association between two species.","Chi-squared. (c4.1.15)"),
("The {{c1::lynx and snowshoe hare}} show a density-dependent predator-prey cycle.","Predator-prey. (c4.1.16)"),
("{{c1::Top-down}} control is by predators; {{c2::bottom-up}} control is by resources.","Control. (c4.1.17)"),
("{{c1::Allelopathy}} (plants) and antibiotic secretion both release chemicals to deter competitors.","Allelopathy. (c4.1.18)"),
("Herbivory, predation, interspecific competition, mutualism, parasitism and pathogenicity are {{c1::interspecific}} relationships.","Interspecific. (c4.1.11)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
