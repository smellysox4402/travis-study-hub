#!/usr/bin/env python3
"""Build A2.3 Viruses cloze deck for the Bio HL deck. Usage: python build_a23_anki.py"""
import genanki, os
MODEL_ID=1607392319; DECK_ID=2059400110
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","topics","bio","a2.3-viruses","A2.3_Viruses.apkg")
model=genanki.Model(MODEL_ID,"Cloze+",fields=[{"name":"Text"},{"name":"Back Extra"}],templates=[{"name":"Cloze","qfmt":"{{cloze:Text}}","afmt":'{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],model_type=1)
CARDS=[
("Viruses have a {{c1::protein capsid}} and {{c2::nucleic acid}} (DNA or RNA), no cytoplasm and few enzymes.","Virus structure. (a2.3.1)"),
("A virus has {{c1::no cytoplasm}} and {{c2::few or no enzymes}}.","No cytoplasm. (a2.3.1)"),
("Viral genetic material can be {{c1::DNA or RNA}}, and either single- or {{c2::double-stranded}}.","Nucleic acid diversity. (a2.3.2)"),
("Some viruses have an outer {{c1::envelope}} around the capsid.","Envelope. (a2.3.2)"),
("In the {{c1::lytic}} cycle the host cell is destroyed to release new viruses.","Lytic. (a2.3.3)"),
("The lytic cycle phases: attach, {{c1::inject}} nucleic acid, replicate, assemble, {{c2::lyse}} the host.","Lytic phases. (a2.3.3)"),
("Viruses rely on the host cell for {{c1::energy}}, {{c2::nutrition}} and {{c3::protein synthesis}}.","Host dependence. (a2.3.3)"),
("In the {{c1::lysogenic}} cycle the viral genome integrates into the host {{c2::chromosome}} as a prophage.","Lysogenic. (a2.3.4)"),
("In the lysogenic cycle the prophage is {{c1::copied}} along with the host DNA each time the host divides.","Prophage copying. (a2.3.4)"),
("Viruses are {{c1::obligate}} parasites and their diversity suggests they arose {{c2::several}} times from other organisms' genes.","Origins. (a2.3.5)"),
("Some viruses evolve rapidly because of {{c1::short generation times}} and {{c2::high mutation rates}}.","Why fast. (a2.3.6)"),
("{{c1::Influenza}} evolves rapidly by antigenic drift/shift of its surface proteins, requiring updated vaccines.","Influenza. (a2.3.6)"),
("HIV evolves rapidly partly because {{c1::reverse transcriptase}} makes many copying errors.","HIV. (a2.3.6)"),
("Because viruses mutate fast, treatment uses {{c1::combination therapy}} and {{c2::updated vaccines}}.","Treatment. (a2.3.6)"),
]
deck=genanki.Deck(DECK_ID,"Bio HL")
for t,b in CARDS: deck.add_note(genanki.Note(model=model,fields=[t,b]))
genanki.Package(deck).write_to_file(OUT); print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
