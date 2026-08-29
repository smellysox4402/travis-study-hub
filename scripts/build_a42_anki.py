#!/usr/bin/env python3
"""Build A4.2 Conservation of Biodiversity cloze deck for the Bio HL deck. Usage: python build_a42_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","a4.2-conservation-biodiversity","A4.2_Conservation_of_Biodiversity.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Biodiversity is the variety of life at {{c1::ecosystem}}, {{c2::species}} and {{c3::genetic}} diversity levels.","Three levels. (a4.2.1)"),
("{{c1::Genetic}} diversity is the variety of genes within a species.","Genetic level. (a4.2.1)"),
("Millions of species have been named, but many more are {{c1::undiscovered}}.","Species count. (a4.2.2)"),
("The current {{c1::sixth}} mass extinction is caused by {{c2::human}} activity.","Sixth extinction. (a4.2.3)"),
("The current extinction event is {{c1::anthropogenic}} (human-caused), unlike earlier mass extinctions.","Anthropogenic. (a4.2.3)"),
("A case study of ecosystem loss is the {{c1::mixed dipterocarp forest}}.","Ecosystem case. (a4.2.4)"),
("Evidence of the biodiversity crisis comes from {{c1::IPBES}} reports and reliable surveys.","Evidence. (a4.2.5)"),
("The overarching cause of the biodiversity crisis is {{c1::human population growth}}.","Overarching cause. (a4.2.6)"),
("Specific causes of the crisis include {{c1::over-exploitation}}, {{c2::urbanization}} and {{c3::deforestation}}.","Causes. (a4.2.6)"),
("{{c1::In situ}} conservation protects species in their natural habitat (e.g. national parks).","In situ. (a4.2.7)"),
("{{c1::Ex situ}} conserves species away from the habitat (e.g. zoos, seed banks, botanical gardens).","Ex situ. (a4.2.7)"),
("No single approach is {{c1::sufficient}} — conservation needs a {{c2::combination}} of in situ and ex situ measures.","Combination. (a4.2.7)"),
("EDGE stands for {{c1::Evolutionarily Distinct and Globally Endangered}}.","EDGE. (a4.2.8)"),
("The EDGE programme prioritises species that are both {{c1::evolutionarily distinct}} and {{c2::globally endangered}}.","EDGE prioritisation. (a4.2.8)"),
("Conservation prioritisation uses EDGE because it preserves the most unique {{c1::evolutionary history}}.","Why EDGE. (a4.2.8)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
