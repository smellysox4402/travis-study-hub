#!/usr/bin/env python3
"""Build B2.3 Cell Specialization cloze deck for the Bio HL deck. Usage: python build_b23_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","b2.3-cell-specialization","B2.3_Cell_Specialization.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("After fertilisation, unspecialised cells become specialised by {{c1::differentiation}}, driven by {{c2::gene expression}} gradients.","Differentiation. (b2.3.1)"),
("Stem cells can {{c1::divide endlessly}} and {{c2::differentiate along different pathways}}.","Stem cells. (b2.3.2)"),
("An adult stem-cell niche example is {{c1::bone marrow}} (and {{c2::hair follicles}}).","Niches. (b2.3.3)"),
("{{c1::Totipotent}} cells can form any cell type including extra-embryonic tissue; {{c2::pluripotent}} cells form all body cell types; {{c3::multipotent}} form a few related types.","Potency. (b2.3.4)"),
("A large cell has a {{c1::small surface area-to-volume ratio}}, which limits cell size.","SA:vol. (b2.3.6)"),
("AHL cells can increase SA:vol by {{c1::flattening}}, {{c2::microvilli}} or {{c3::invagination}} (e.g. erythrocytes, proximal convoluted tubule cells).","Raise SA:vol. (b2.3.7)"),
("AHL {{c1::type I pneumocytes}} are extremely thin to reduce diffusion distance; {{c2::type II pneumocytes}} secrete {{c3::surfactant}}.","Pneumocytes. (b2.3.8)"),
("AHL cardiac muscle cells are {{c1::branched}}/short/one nucleus; striated muscle fibres are {{c2::unbranched}}/long/{{c3::multinucleate}} — both have myofibrils.","Muscle. (b2.3.9)"),
("AHL a sperm has a {{c1::flagellum}}, {{c2::acrosome}} (enzymes) and many {{c3::mitochondria}}.","Sperm. (b2.3.10)"),
("AHL an egg (ovum) has a large {{c1::cytoplasm/yolk}}, a {{c2::zona pellucida}} and forms {{c3::polar bodies}}.","Egg. (b2.3.10)"),
("Early embryo cells are {{c1::totipotent}} but soon become {{c2::pluripotent}}; adult bone-marrow stem cells are {{c3::multipotent}}.","Potency examples. (b2.3.4)"),
("Exchange across a cell surface depends on {{c1::surface area}}; the need for exchange depends on {{c2::volume}}.","SA vs vol. (b2.3.6)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
