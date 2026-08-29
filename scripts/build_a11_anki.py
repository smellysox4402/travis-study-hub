#!/usr/bin/env python3
"""Build A1.1 Water cloze deck for the Bio HL deck.
Matches the existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki.  Usage: python build_a11_anki.py
"""
import genanki, os

MODEL_ID = 1607392319
DECK_ID  = 2059400110
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "a1.1-water", "A1.1_Water.apkg")

model = genanki.Model(
    MODEL_ID, "Cloze+",
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[{"name": "Cloze", "qfmt": "{{cloze:Text}}",
                "afmt": '{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>'}],
    model_type=1,
)

CARDS = [
# --- A1.1.1 medium for life ---
("Water is the {{c1::medium}} in which most of life's processes take place; the first cells are thought to have originated {{c2::in water}}.",
 "Life is water-based. (a1.1.1)"),
("Most of the chemical reactions of metabolism occur in an {{c1::aqueous solution}} inside cells.",
 "Aqueous = water-based. (a1.1.1)"),
("In animals, {{c1::blood plasma}} is the transport medium; in vascular plants, water carries minerals in the {{c2::xylem}} and dissolved sugars in the {{c3::phloem}}.",
 "Water = transport medium. (a1.1.1)"),
# --- A1.1.2 polarity ---
("A water molecule is {{c1::H₂O}} — two hydrogen atoms covalently bonded to one oxygen atom.",
 "Molecular formula. (a1.1.2)"),
("The O–H bonds in water are {{c1::polar covalent}} because the shared electrons are {{c2::unequally shared}} between the atoms.",
 "Unequal sharing. (a1.1.2)"),
("Because oxygen is more {{c1::electronegative}}, it attracts the shared electrons more strongly and carries a slight {{c2::negative}} charge (δ−).",
 "Oxygen pulls electrons. (a1.1.2)"),
("The two hydrogen atoms each carry a slight {{c1::positive}} charge (δ+) when bonded to oxygen.",
 "Hydrogens δ+. (a1.1.2)"),
("The water molecule has a {{c1::bent}} shape, so one end (oxygen) is negative and the other end (hydrogens) is positive, making water {{c2::polar}}.",
 "A polar, bent molecule. (a1.1.2)"),
# --- A1.1.2 hydrogen bonds ---
("A hydrogen bond is a weak attraction between a {{c1::δ+ hydrogen}} of one water molecule and a {{c2::δ− oxygen}} of another.",
 "Intermolecular attraction. (a1.1.2)"),
("Hydrogen bonds in water form specifically between a δ+ hydrogen and the δ− of {{c1::oxygen}} (or nitrogen, fluorine) of another molecule — the most {{c2::electronegative}} elements.",
 "O, N, F are the most electronegative. (a1.1.2)"),
("Hydrogen bonds are {{c1::weaker}} than covalent bonds, but water forms {{c2::many}} of them, giving it strong cohesion.",
 "Weak but numerous. (a1.1.2)"),
("You should be able to draw {{c1::two or more}} water molecules and the {{c2::hydrogen bonds}} between them, showing the δ+ and δ− charges.",
 "Exam drawing skill. (a1.1.2)"),
# --- A1.1.3 cohesion ---
("Cohesion is the attraction of water molecules {{c1::to each other}} due to hydrogen bonding.",
 "Water sticks to water. (a1.1.3)"),
("Cohesion produces {{c1::surface tension}} — the water surface acts like a stretched film because surface molecules are pulled inward.",
 "Surface film. (a1.1.3)"),
("A {{c1::water strider}} can move across the surface of water because of its high surface tension.",
 "Small insect walks on water. (a1.1.3)"),
("In plants, water moves up the xylem under {{c1::tension}} because a cohesive chain of molecules is pulled upward by {{c2::transpiration}}.",
 "The transpiration stream. (a1.1.3)"),
# --- A1.1.4 adhesion ---
("Adhesion is the attraction of water molecules to {{c1::polar or charged}} surfaces.",
 "Water sticks to other surfaces. (a1.1.4)"),
("Capillary action is the rise of water in a narrow tube, driven by {{c1::adhesion}} to the walls and {{c2::cohesion}} between molecules.",
 "Both adhesion and cohesion. (a1.1.4)"),
("Capillary action moves water through {{c1::soil}} and within the {{c2::cell walls}} of plants.",
 "Soil and cell walls. (a1.1.4)"),
("The {{c1::narrower}} the tube, the stronger the capillary action.",
 "Narrow = stronger. (a1.1.4)"),
# --- A1.1.5 solvent ---
("Water is an excellent solvent because it is {{c1::polar}}, so it dissolves {{c2::hydrophilic}} substances.",
 "Polar dissolves polar. (a1.1.5)"),
("Most enzymes catalyse reactions in {{c1::aqueous solution}}, where solutes collide more often with enzymes.",
 "Water = metabolic medium. (a1.1.5)"),
("{{c1::Hydrophilic}} molecules dissolve readily in water; {{c2::hydrophobic}} molecules (e.g. lipids) do not.",
 "Hydrophilic vs hydrophobic. (a1.1.5)"),
("Lipids are transported in the blood packaged with proteins, forming water-soluble {{c1::lipoproteins}}.",
 "Lipids need transport help. (a1.1.5)"),
("Hydrophobic insolubility is essential for molecules such as {{c1::lipids}} that form membranes.",
 "So hydrophobic is also useful. (a1.1.5)"),
# --- A1.1.6 physical properties ---
("The physical properties of water include buoyancy, viscosity, thermal conductivity and {{c1::specific heat capacity}}.",
 "Four physical properties. (a1.1.6)"),
("Water is {{c1::denser}} than air, so it exerts a greater {{c2::buoyant}} force.",
 "Density → buoyancy. (a1.1.6)"),
("Water is more {{c1::viscous}} than air (it resists flow) partly because of hydrogen bonding.",
 "Viscous. (a1.1.6)"),
("Water has a {{c1::higher}} specific heat capacity than air because hydrogen bonds need extra energy to break.",
 "High heat capacity. (a1.1.6)"),
("Water has a {{c1::higher}} thermal conductivity than air because its molecules are packed more tightly.",
 "Conducts heat well. (a1.1.6)"),
("The black-throated loon has {{c1::lighter (less dense)}} bones so it can float, but they are not hollow, allowing it to {{c2::dive}} too.",
 "Loon floats and dives. (a1.1.6)"),
("The loon's legs are at the {{c1::rear}} to better propel it through water, making {{c2::walking on land}} difficult.",
 "Rear legs for swimming. (a1.1.6)"),
("The ringed seal has {{c1::denser}} bones than the loon, helping it stay submerged when diving.",
 "Seal dives and stays down. (a1.1.6)"),
("The ringed seal has a streamlined body (for {{c1::viscosity}}) and insulation of {{c2::fur + blubber}} to prevent heat loss in water.",
 "Adapted to viscous, conducting water. (a1.1.6)"),
("Because water temperature is stable (high {{c1::specific heat capacity}}), the ringed seal has few cooling mechanisms and is vulnerable to {{c2::climate change}}.",
 "Stable water temperature. (a1.1.6)"),
# --- A1.1.7 origins (AHL) ---
("Early Earth was too {{c1::hot}} to condense its water vapour and had too little {{c2::gravity}} to hold it, so most escaped to space.",
 "Why early water was lost. (a1.1.7)"),
("Earth's large bodies of water are hypothesised to have come from {{c1::icy asteroids}} that collided with the planet.",
 "Asteroid origin. (a1.1.7)"),
("The asteroids formed {{c1::further from the Sun}} where it was cold enough for water to freeze as ice.",
 "Cold outer asteroid zone. (a1.1.7)"),
("Water was retained once Earth had enough {{c1::gravity}} and had {{c2::cooled}} enough for the water to condense and stay liquid.",
 "Gravity + cooling = retention. (a1.1.7)"),
# --- A1.1.8 Goldilocks (AHL) ---
("The {{c1::Goldilocks zone}} (habitable zone) is the range of distances from a star where liquid water could exist.",
 "Habitable zone. (a1.1.8)"),
("The position of the Goldilocks zone depends on the star's {{c1::size and temperature}} — it is further away from hotter stars.",
 "Star-dependent. (a1.1.8)"),
("The search for extraterrestrial life focuses on the presence of {{c1::liquid water}} because it is essential for life as we know it.",
 "Water = life target. (a1.1.8)"),
("Very few planets in a Goldilocks zone also have the right {{c1::mass}} and {{c2::atmosphere}} to hold liquid water on the surface.",
 "Rare combination. (a1.1.8)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, back in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, back]))
genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
