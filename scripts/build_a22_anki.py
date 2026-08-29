#!/usr/bin/env python3
"""Build A2.2 Cell Structure cloze deck for the Bio HL deck. Usage: python build_a22_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","a2.2-cell-structure","A2.2_Cell_Structure.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
# A2.2.1
("The cell is the {{c1::basic structural unit}} of all living organisms.", "Cell theory. (a2.2.1)"),
# A2.2.2
("Actual size is calculated as {{c1::measured size ÷ magnification}}.", "Magnification calc. (a2.2.2)"),
("An {{c1::eyepiece graticule}} is the scale in the eyepiece used to measure cell size.", "Measuring. (a2.2.2)"),
# A2.2.3
("{{c1::Electron microscopy}} gives much higher resolution than light microscopy because it uses electrons.", "EM. (a2.2.3)"),
("{{c1::Freeze fracture}} splits membranes to reveal their internal structure.", "Freeze fracture. (a2.2.3)"),
("{{c1::Cryogenic EM}} freezes specimens to preserve near-native structure at high resolution.", "Cryo-EM. (a2.2.3)"),
("{{c1::Fluorescent stains}} and {{c2::immunofluorescence}} let you localise specific molecules in cells.", "Fluorescence. (a2.2.3)"),
# A2.2.4
("All cells have {{c1::DNA}}, cytoplasm made mainly of {{c2::water}}, and a plasma membrane made of {{c3::lipids}}.", "Common features. (a2.2.4)"),
# A2.2.5
("Prokaryotes have a cell wall, plasma membrane, cytoplasm, {{c1::naked DNA in a loop}} and {{c2::70S ribosomes}}.", "Prokaryote parts. (a2.2.5)"),
("Prokaryotes have {{c1::no nucleus}} and membrane-bound organelles.", "No nucleus. (a2.2.5)"),
# A2.2.6
("Eukaryotes have {{c1::80S}} ribosomes, while prokaryotes have 70S.", "Ribosome size. (a2.2.6)"),
("In eukaryotes the nucleus has {{c1::chromosomes}} (DNA bound to {{c2::histones}}) inside a {{c3::double membrane}} with {{c4::pores}}.", "Nucleus. (a2.2.6)"),
("The eukaryote cytoskeleton is made of {{c1::microtubules}} and {{c2::microfilaments}}.", "Cytoskeleton. (a2.2.6)"),
# A2.2.7
("Unicellular organisms must carry out {{c1::homeostasis}}, metabolism, nutrition, movement, excretion, growth, response to stimuli and reproduction.", "Life processes. (a2.2.7)"),
# A2.2.8
("Plant cell walls are made of {{c1::cellulose}}; fungal cell walls of {{c2::chitin}}.", "Wall types. (a2.2.8)"),
("Plant cells have a large central {{c1::sap vacuole}} and {{c2::chloroplasts}}; plant cells {{c3::lack}} centrioles.", "Plant features. (a2.2.8)"),
# A2.2.9
("Skeletal muscle fibres and aseptate fungal hyphae are {{c1::multinucleate}}.", "Atypical multinucleate. (a2.2.9)"),
("Mammalian red blood cells and phloem sieve tube elements have {{c1::no nucleus}}.", "Atypical no-nucleus. (a2.2.9)"),
# A2.2.10/11
("In electron micrographs you identify the {{c1::nucleoid region}} and prokaryotic cell wall as prokaryotic features.", "Micrograph ID. (a2.2.10)"),
("When drawing organelles you must annotate their {{c1::function}}.", "Annotate function. (a2.2.11)"),
# A2.2.12 AHL
("Mitochondria and chloroplasts arose by {{c1::endosymbiosis}} — engulfed free-living bacteria.", "Endosymbiosis. (a2.2.12)"),
("Evidence for endosymbiosis: mitochondria/chloroplasts have {{c1::70S ribosomes}}, {{c2::naked circular DNA}} and can {{c3::replicate}}.", "Endosymbiosis evidence. (a2.2.12)"),
# A2.2.13 AHL
("Cell differentiation is based on {{c1::different patterns of gene expression}}, often triggered by the environment.", "Differentiation. (a2.2.13)"),
# A2.2.14 AHL
("Multicellularity evolved {{c1::repeatedly}} and gives advantages of {{c2::larger body size}} and {{c3::cell specialization}}.", "Multicellularity. (a2.2.14)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
