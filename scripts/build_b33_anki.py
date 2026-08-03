#!/usr/bin/env python3
"""Build B3.3 Muscle & Motility cloze deck (~50 cards) for the Bio HL deck.
Matches the user's existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_b33_anki.py  ->  writes B3.3_Muscle_and_Motility.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as C2.1/B3.1 -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "muscle-motility", "B3.3_Muscle_and_Motility.apkg")

model = genanki.Model(
    MODEL_ID,
    "Cloze+",
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>',
    }],
    model_type=1,  # cloze
)

CARDS = [
# --- B3.3.1 movement as a universal feature ---
("Movement is a function of life. {{c1::Locomotion}} is movement from place to place, whereas {{c2::movement within the body}} (e.g. peristalsis, ventilation) happens in ALL organisms, even ones that can't walk.",
 "Even the doormat moves — peristalsis happens everywhere. 🚪 (b3.3.1)"),
("An organism that moves from place to place is {{c1::motile}}; one that stays fixed in one spot is {{c2::sessile}}. Coral polyps and adult barnacles are {{c3::sessile}}, but barnacle larvae are {{c4::motile}}.",
 "Club rule: some dancers move, some hold the wall. 🪩 (b3.3.1)"),
("The bar-tailed godwit migrates {{c1::10,400 km}} non-stop from eastern Siberia to New Zealand in 7–8 days, fuelled by {{c2::double}} its body weight in fat reserves.",
 "The marathon dancer. 🪁 (b3.3.1)"),
("Motile organisms tend to have {{c1::higher}} metabolic rates and {{c2::greater}} nutritional needs than sessile ones, because locomotion costs energy.",
 "Moving is expensive — the club needs more drinks. 🍸 (b3.3.1)"),
("Movement in ALL living organisms happens within the body (e.g. {{c1::cytoplasmic streaming}} in cells, {{c2::peristalsis}} in the gut, {{c3::ventilation}} of lungs/gills), even in sessile organisms — so movement is a {{c4::universal}} feature of life.",
 "Nobody is truly frozen. 🧊 (b3.3.1)"),
# --- B3.3.2 sliding filament model ---
("A muscle fibre contains many parallel {{c1::myofibrils}}, each made of sarcomeres linked end-to-end at {{c2::Z-discs}}.",
 "The dance floor tiles. 💃 (b3.3.2)"),
("In a relaxed sarcomere, the {{c1::light bands}} (I-bands) sit at the ends and the {{c2::dark band}} (A-band) sits in the middle. On contraction, the light bands get {{c3::narrower}} while the dark band stays the {{c4::same length}}.",
 "KEY EXAM FACT: light bands shrink, dark band does NOT. 📏 (b3.3.2)"),
("The thin filaments in a sarcomere are made of {{c1::actin}} and are attached to the {{c2::Z-discs}}; the thick filaments are made of {{c3::myosin}} and occupy the centre, interlocking with the actin like fingers.",
 "Fingers clasped between the walls. 🖐 (b3.3.2)"),
("Each myosin filament is surrounded by {{c1::six}} actin filaments, and myosin heads form {{c2::cross-bridges}} that bind to binding sites on the actin.",
 "One dancer, six partners. 🪩 (b3.3.2)"),
("Myosin heads bind to actin, then {{c1::swivel}}, pushing the actin filaments toward the centre of the sarcomere — this is the {{c2::power stroke}}, sliding actin about {{c3::8–10 nm}}.",
 "The swivel-and-pull. 💪 (b3.3.2)"),
("After the power stroke, the myosin head detaches, swings back, and reattaches at the next binding site further along the actin — this repeated cycle is the {{c1::ratchet mechanism}}, powered by {{c2::ATP}}.",
 "Never let go of the rail; reach, pull, repeat. 🎡 (b3.3.2)"),
("Because hundreds of myosin heads are always attached at any moment, the sliding filaments produce {{c1::smooth}} and {{c2::powerful}} shortening of the sarcomere — many small pulls add up.",
 "Many small pulls = one big slide. 🏋 (b3.3.2)"),
("As sarcomeres shorten, the {{c1::Z-discs}} are pulled closer together, so the whole myofibril — and the whole muscle fibre — {{c2::shortens}}. The filaments themselves do NOT shorten; they {{c3::slide past each other}}.",
 "Nothing shrinks; everything slides. 📏 (b3.3.2)"),
# --- B3.3.3 titin + antagonistic muscles ---
("{{c1::Titin}} is the largest polypeptide ever discovered — in humans it is {{c2::34,350}} amino acids long (35,213 in mice).",
 "The bungee cord giant. 🧵 (b3.3.3)"),
("Titin is an elastic {{c1::molecular spring}} that connects the end of each {{c2::myosin}} filament to the {{c3::Z-disc}}.",
 "It anchors the dancer to the wall. 🧵 (b3.3.3)"),
("Three functions of titin: it holds the myosin filament {{c1::centred}} among its six actins, prevents the sarcomere from {{c2::overstretching}}, and adds force to contraction by {{c3::recoiling}} like a spring.",
 "Centring, safety, and a free push. 🧵 (b3.3.3)"),
("A muscle can only {{c1::exert force when contracting}} — it cannot actively lengthen itself. Lengthening is done by the {{c2::antagonistic}} muscle: when the biceps contracts, the {{c3::triceps}} is stretched.",
 "Muscles pull; they never push. ↔ (b3.3.3)"),
("When an antagonistic muscle is stretched by its partner's contraction, its titin stores {{c1::potential energy}}, which is released as {{c2::recoil}} to help the muscle return to its resting length.",
 "The spring does the return trip. 🧵 (b3.3.3)"),
# --- B3.3.4 motor units ---
("Skeletal muscle fibres contract only when stimulated by a {{c1::motor neuron}}. The synapse between the neuron branch and the fibre is a {{c2::neuromuscular junction}}, where the neurotransmitter {{c3::acetylcholine}} (ACh) is released.",
 "The DJ sends the signal through the speakers. 📢 (b3.3.4)"),
("A motor unit = one {{c1::motor neuron}} + {{c2::ALL the muscle fibres}} it stimulates, which is usually {{c3::hundreds}} of fibres.",
 "One DJ controls a whole section of the crowd. 📢 (b3.3.4)"),
("The fibres of a single motor unit are {{c1::mingled}} among fibres of other units, NOT clumped together — so a single neuron's contraction is spread across the muscle.",
 "Dancers of one crew are scattered through the whole floor. 🪩 (b3.3.4)"),
("When a motor neuron fires, {{c1::all}} the fibres in its unit contract together (all-or-nothing); the strength of a muscle contraction is graded by recruiting {{c2::more motor units}}.",
 "Turn on more speakers → more of the floor moves. 🔊 (b3.3.4)"),
("Twitch fibres contract fast and powerfully but tire quickly; slow-twitch fibres contract {{c1::slowly}} but can sustain contraction for long periods — muscles have a mix of both.",
 "Sprinter crew vs endurance crew. 🏃 (b3.3.4)"),
# --- B3.3.5 skeletons as anchorage + levers ---
("An {{c1::exoskeleton}} is a hard outer covering (e.g. the chitin of arthropods); an {{c2::endoskeleton}} is an internal framework of bones (vertebrates). Both give {{c3::anchorage}} for muscles and act as {{c4::levers}}.",
 "The club frame: outside scaffolding or inside beams. 🏗 (b3.3.5)"),
("The end of a muscle that is fixed is its {{c1::origin}}; the end that moves when the muscle contracts is its {{c2::insertion}}. In the masseter, the origin is on the {{c3::cheekbone}} and the insertion is on the {{c4::jawbone}} (mandible).",
 "Origin = bolted to the wall, insertion = the moving end. 🦴 (b3.3.5)"),
("A lever has a {{c1::fulcrum}} (pivot = the joint), an {{c2::effort}} (the muscle, via tendons) and a {{c3::load}} (the resultant force). If the effort is further from the fulcrum than the load, the lever {{c4::increases force}} but {{c5::decreases distance}} moved.",
 "Give me a lever long enough... 🎛 (b3.3.5)"),
("Moles have short, wide forelimb bones — a lever that favours {{c1::force}} for digging; cheetahs have long, narrow limb bones — a lever that favours {{c2::distance/range}} for sprinting.",
 "Shovel arms vs race legs. 🦡 (b3.3.5)"),
# --- B3.3.6 movement at a synovial joint ---
("The parts of a synovial joint: {{c1::bones}}, {{c2::cartilage}}, {{c3::synovial fluid}}, {{c4::ligaments}}, {{c5::muscles}} and {{c6::tendons}}.",
 "THE SIX VIP PARTS — know the list. 🦴 (b3.3.6)"),
("Cartilage covers the bone ends at a joint to prevent {{c1::friction}} and absorb {{c2::shock}}; synovial fluid {{c3::lubricates}} the joint, reducing friction further.",
 "The cushion and the oil. 🧈 (b3.3.6)"),
("Ligaments are tough cords of {{c1::collagen}} that connect bone to bone and prevent {{c2::aberrant movements}} (dislocation); the {{c3::joint capsule}} surrounds and seals the joint.",
 "The seatbelt holding the club doors together. 🔗 (b3.3.6)"),
("Tendons attach {{c1::muscle to bone}}; they are made of {{c2::collagen}} with high tensile strength. Muscles provide the {{c3::force}} that moves the joint.",
 "The cables from the dancers to the frame. 🪢 (b3.3.6)"),
("The human hip is a {{c1::ball-and-socket}} joint: the head of the {{c2::femur}} (ball) fits into a socket in the {{c3::pelvis}}.",
 "The pelvis socket and the femur ball. 🦵 (b3.3.6)"),
# --- B3.3.7 range of motion ---
("Hinge joints (elbow, knee) allow movement in {{c1::one}} plane only: {{c2::flexion}} (bending) and {{c3::extension}} (straightening).",
 "Door hinge: back and forth only. 🚪 (b3.3.7)"),
("Ball-and-socket joints (hip) allow {{c1::protraction/retraction}}, {{c2::abduction/adduction}} and {{c3::rotation}} — movement in all three planes.",
 "The DJ booth spins every way. 🪩 (b3.3.7)"),
("The range of motion of a joint can be measured with a {{c1::goniometer}}, or by {{c2::computer analysis of images}} of a person performing movements.",
 "AOS: measure the angles. 📐 (b3.3.7)"),
# --- B3.3.8 intercostal muscles as antagonists ---
("The two layers of intercostal muscle have fibres at {{c1::different orientations}}, so contracting them moves the ribcage in {{c2::opposite directions}}.",
 "Two crews, two angles, two jobs. 🫁 (b3.3.8)"),
("Contraction of the {{c1::external}} intercostals raises the ribs up and out — {{c2::inhalation}}; contraction of the {{c3::internal}} intercostals pulls the ribs down and in — {{c4::exhalation}}.",
 "External = lift the roof; internal = pull it down. 🫁 (b3.3.8)"),
("When the external intercostals contract and lift the ribs, the internal layer is {{c1::stretched}}, storing potential energy in its {{c2::titin}} — which helps recoil during exhalation.",
 "Stretching the other crew stores the return spring. 🧵 (b3.3.8)"),
("The intercostals are an example of an {{c1::antagonistic pair}} of muscles: one contracts, the other is stretched — same principle as biceps/triceps.",
 "Push-pull, all over the body. ↔ (b3.3.8)"),
# --- B3.3.9 reasons for locomotion ---
("Four reasons animals use locomotion: {{c1::foraging for food}}, {{c2::escaping from danger}}, {{c3::searching for a mate}}, and {{c4::migration}}.",
 "THE FOUR REASONS — know all four. 🏃 (b3.3.9)"),
("Bees fly from flower to flower {{c1::foraging}}; predators chase prey; jackdaws leave their roost to {{c2::escape danger}}.",
 "The daily hunt and the alarm bell. 🐝 (b3.3.9)"),
("Male moon moths fly long distances upwind to reach females releasing {{c1::pheromones}} — searching for a mate; young male lions leave the pride to {{c2::challenge}} for dominance.",
 "The perfume trail and the takeover bid. 🦁 (b3.3.9)"),
("Snow geese migrate from the Arctic to the southern US; salmon make a {{c1::once-in-a-lifetime}} migration upstream to spawn — both are {{c2::migration}}.",
 "The season ticket holders. 🪁 (b3.3.9)"),
# --- B3.3.10 marine mammal swimming ---
("Marine mammals are {{c1::streamlined}}: widest near the front, tapering toward the rear, with a {{c2::teardrop}} cross-section and a smooth surface — no hind limbs, no ear flaps, almost no hair.",
 "The body is a droplet. 💧 (b3.3.10)"),
("Marine mammals steer with their {{c1::flippers}} and generate up-and-down thrust with their {{c2::flukes}} (tail lobes) — whales swim by beating the tail {{c3::up and down}}, not side to side like fish.",
 "Flippers steer, flukes drive. 🐬 (b3.3.10)"),
("The {{c1::dorsal fin}} of a marine mammal provides stability, preventing {{c2::rolling}}; {{c3::blubber}} provides buoyancy (and insulation).",
 "The keel and the life vest. ⚓ (b3.3.10)"),
("The {{c1::blowhole}} is a nostril on top of the head that is {{c2::sealed}} while diving and opened for {{c3::periodic breathing}}; there is {{c4::no connection}} between the mouth and the lungs, so water can't flood the airway.",
 "The submarine hatch. 🐋 (b3.3.10)"),
("Because water is about {{c1::1000×}} denser than air, swimming needs {{c2::streamlining}} and powerful propulsion — every shape adaptation in marine mammals reduces drag.",
 "Density is the boss of the ocean dance floor. 🌊 (b3.3.10)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

pkg = genanki.Package(deck)
pkg.write_to_file(OUT)
print(f"Wrote {len(CARDS)} cards -> {os.path.abspath(OUT)}")
