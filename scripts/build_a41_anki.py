#!/usr/bin/env python3
"""Build A4.1 Evolution & Speciation cloze deck for the Bio HL deck. Usage: python build_a41_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","a4.1-evolution-speciation","A4.1_Evolution_and_Speciation.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Evolution is a change in the {{c1::heritable characteristics}} of a population.", "Definition. (a4.1.1)"),
("Evolution is a change in the heritable characteristics of a {{c1::population}}, not an individual.", "Population-level. (a4.1.1)"),
("Strong evidence for evolution comes from {{c1::base sequences}} in DNA/RNA and {{c2::amino acid sequences}} in proteins.", "Sequence evidence. (a4.1.2)"),
("{{c1::Selective breeding}} of domesticated animals and crop plants is evidence of change in heritable traits.", "Selective breeding. (a4.1.3)"),
("{{c1::Homologous structures}} share the same evolutionary origin; the {{c2::pentadactyl limb}} is an example.", "Homologous. (a4.1.4)"),
("The pentadactyl limb (in humans, cats, whales, bats) is a {{c1::homologous}} structure.", "Pentadactyl. (a4.1.4)"),
("{{c1::Convergent evolution}} produces {{c2::analogous}} structures — same function, different origin (e.g. bird vs insect wings).", "Convergent/analogous. (a4.1.5)"),
("{{c1::Speciation}} is the splitting of a pre-existing species into two or more new species.", "Speciation. (a4.1.6)"),
("Speciation is the only way {{c1::new species}} appear, and it {{c2::increases biodiversity}}.","Biodiversity. (a4.1.6)"),
("Speciation is driven by {{c1::reproductive isolation}} and {{c2::differential selection}}.","Drivers. (a4.1.7)"),
("{{c1::Geographical isolation}} is a way of achieving reproductive isolation (e.g. bonobos and common chimpanzees split by a river).","Geographic isolation. (a4.1.7)"),
("In {{c1::allopatric}} speciation, populations are separated by a physical barrier; in {{c2::sympatric}} speciation, isolation occurs without one.","Allopatric vs sympatric. (a4.1.8)"),
("{{c1::Adaptive radiation}} lets closely related species coexist without competing, increasing biodiversity (e.g. Darwin's finches).","Adaptive radiation. (a4.1.9)"),
("{{c1::Courtship behaviour}} can prevent hybridization in animals, keeping species separate.","Courtship barrier. (a4.1.10)"),
("Interspecific hybrids are often {{c1::sterile}} (e.g. a mule), preventing allele mixing between species.","Sterile hybrids. (a4.1.10)"),
("{{c1::Polyploidy}} after hybridization can cause abrupt speciation, reproductively isolating the new plant species (e.g. {{c2::Persicaria}}).","Polyploidy. (a4.1.11)"),
("A polyploid hybrid is {{c1::reproductively isolated}} from both parent species, so it forms a new species in one step.","Abrupt speciation. (a4.1.11)"),
("Homologous structures have the same {{c1::evolutionary origin}}; analogous structures have the same {{c2::function}} but different origins.","Homologous vs analogous. (a4.1.4-5)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
