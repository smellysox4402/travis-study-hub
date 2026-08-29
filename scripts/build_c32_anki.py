#!/usr/bin/env python3
"""Build C3.2 Defence Against Disease cloze deck for the Bio HL deck. Usage: python build_c32_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","c3.2-defence-disease","C3.2_Defence_Against_Disease.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("A {{c1::pathogen}} is a disease-causing organism (bacteria, viruses, fungi, protists).","Pathogen. (c3.2.1)"),
("The skin and mucous membranes act as {{c1::physical}} and {{c2::chemical}} barriers.","Primary defence. (c3.2.2)"),
("Blood clotting: {{c1::platelets}} release clotting factors that trigger a {{c2::cascade}}, forming a {{c3::fibrin}} clot.","Clotting. (c3.2.3)"),
("The {{c1::innate}} immune system responds broadly and doesn't change; the {{c2::adaptive}} system is specific and has memory.","Innate vs adaptive. (c3.2.4)"),
("Phagocytes move by {{c1::amoeboid}} movement, engulf pathogens by {{c2::endocytosis}} and digest with {{c3::lysosomes}}.","Phagocytes. (c3.2.5)"),
("Lymphocytes circulate in the {{c1::blood}} and are contained in {{c2::lymph nodes}} and the spleen.","Lymphocytes. (c3.2.6)"),
("{{c1::Antigens}} (usually glycoproteins/proteins) trigger {{c2::antibody}} production.","Antigens. (c3.2.7)"),
("{{c1::Helper T-cells}} activate antigen-specific {{c2::B-cells}}.","Activation. (c3.2.8)"),
("Activated B-cells multiply into clones of {{c1::plasma cells}} that secrete {{c2::antibodies}}.","Plasma cells. (c3.2.9)"),
("Immunity results from retaining {{c1::memory cells}} after an infection.","Memory. (c3.2.10)"),
("HIV is transmitted in {{c1::body fluids}} (blood, semen, vaginal fluid, breast milk).","HIV transmission. (c3.2.11)"),
("HIV infects and kills {{c1::helper T-lymphocytes}}, and the resulting reduction leads to {{c2::AIDS}}.","HIV→AIDS. (c3.2.12)"),
("Antibiotics block {{c1::bacterial}} processes, so they are ineffective against {{c2::viruses}}.","Antibiotics. (c3.2.13)"),
("Antibiotic {{c1::resistance}} evolves; careful use slows it (e.g. MRSA).","Resistance. (c3.2.14)"),
("A {{c1::zoonosis}} is an infectious disease that transfers from other species to humans.","Zoonosis. (c3.2.15)"),
("A vaccine contains antigens (or nucleic acids coding for them) that stimulate {{c1::memory cell}} production.","Vaccine. (c3.2.16)"),
("{{c1::Herd immunity}} prevents epidemics when a sufficient percentage of a population is immune.","Herd immunity. (c3.2.17)"),
("Percentage change = (new − original) ÷ original × {{c1::100}}.","Data. (c3.2.18)"),
("{{c1::Antibodies}} are proteins made by plasma cells that bind specific antigens.","Antibodies. (c3.2.9)"),
("Fibrinogen is converted to insoluble {{c1::fibrin}} to form a clot.","Fibrin. (c3.2.3)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes")
