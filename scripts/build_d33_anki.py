#!/usr/bin/env python3
"""Build D3.3 Homeostasis cloze deck (~60 cards) for the Bio HL deck.
Matches the existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_d33_anki.py  ->  writes D3.3_Homeostasis.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as C2.1/B3.1/B3.3/D2.1/D3.2 -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "homeostasis", "D3.3_Homeostasis.apkg")

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
# --- D3.3.1 homeostasis concept ---
("Homeostasis is the maintenance of the {{c1::internal environment}} within {{c2::preset limits}} (narrow ranges), despite changes in the {{c3::external environment}}.",
 "The club keeps its vibe regardless of the weather outside. 🎚 (d3.3.1)"),
("The four key variables kept in range by homeostasis: {{c1::core temperature}} (~37°C), {{c2::blood pH}} (~7.4), {{c3::blood glucose}} (~5 mmol L⁻¹) and {{c4::blood osmotic concentration}} (~300 mOsm L⁻¹).",
 "The four dials. 🎛 (d3.3.1)"),
("A set point is the {{c1::normal value}} of a variable, and it has a {{c2::tolerance band}} — a narrow range of acceptable drift around it before corrective action kicks in.",
 "Not a razor edge: a safe lane. 🛣 (d3.3.1)"),
("When a homeostatic variable stays outside its preset limits, the result is {{c1::disease or death}} — e.g. body temp above ~41°C or glucose chronically high (diabetes).",
 "Break the dials, pay the price. ⚠ (d3.3.1)"),
# --- D3.3.2 negative feedback ---
("Most homeostatic control uses {{c1::negative feedback}}: the response {{c2::reverses (opposes)}} the change that triggered it, bringing the variable back toward the {{c3::set point}}.",
 "The reverse-gear rule. 🔄 (d3.3.2)"),
("The negative feedback loop chain: {{c1::stimulus}} → {{c2::receptor}} detects → {{c3::control centre}} compares against set point → {{c4::effector}} produces a response that {{c5::reverses the change}}.",
 "The bouncer chain of command. 🪪 (d3.3.2)"),
("Negative feedback works from {{c1::above AND below}} the set point — the response pushes the variable back whichever direction it drifted.",
 "Two-way street. ⬆⬇ (d3.3.2)"),
("Why negative rather than positive feedback? Negative feedback {{c1::decreases the gap}} between the variable and the set point and {{c2::restores balance}}; positive feedback {{c3::increases the gap}} and promotes change — the opposite of what homeostasis needs.",
 "The exam answer: shrink the gap. 📏 (d3.3.2)"),
("Examples of {{c1::positive}} feedback (not homeostatic): {{c2::childbirth}} (contraction → more stretching → stronger contraction), {{c3::ovulation}} and {{c4::lactation}}.",
 "The amplifiers. 🎸 (d3.3.2)"),
# --- D3.3.3 blood glucose regulation ---
("Blood glucose is regulated by two {{c1::antagonistic}} hormones secreted by the {{c2::islets of Langerhans}} in the pancreas: {{c3::insulin}} (from β cells) and {{c4::glucagon}} (from α cells).",
 "The DJ pair in the pancreas. 🍬 (d3.3.3)"),
("When blood glucose is HIGH, {{c1::β cells}} secrete {{c2::insulin}}, which lowers glucose by promoting {{c3::glycogen formation}} (in liver and muscle), {{c4::glucose uptake}} by tissues and {{c5::faster cell respiration}}.",
 "High sugar → insulin clears the floor. 🧹 (d3.3.3)"),
("When blood glucose is LOW, {{c1::α cells}} secrete {{c2::glucagon}}, which raises glucose by stimulating {{c3::glycogen breakdown}} in the liver and release of glucose into the blood.",
 "Low sugar → glucagon opens the doors. 🚪 (d3.3.3)"),
("Hormones reach their target cells via the {{c1::blood}}; target cells carry {{c2::specific receptors}}, so only cells with the right receptor respond.",
 "Blood mail, addressed delivery. ✉ (d3.3.3)"),
("Glucose enters the blood from: {{c1::absorption from the gut}}, {{c2::glycogen breakdown}} and {{c3::production from amino acids / glycerol}}. It leaves by: {{c4::cell respiration}}, {{c5::conversion to glycogen}} and {{c6::conversion to fat}}.",
 "The four taps in, three taps out. 🚰 (d3.3.3)"),
("Insulin and glucagon are antagonistic because they act in {{c1::opposite directions}} on the same variable (glucose) — one lowers, one raises, both part of one negative feedback loop.",
 "Opposite pulls on the same rope. 🥊 (d3.3.3)"),
("The glucose loop runs on negative feedback: high glucose → insulin → glucose falls → {{c1::insulin secretion stops}}; low glucose → glucagon → glucose rises → {{c2::glucagon stops}}.",
 "Self-cancelling. 🔄 (d3.3.3)"),
# --- D3.3.4 diabetes ---
("Diabetes mellitus is a condition of {{c1::hyperglycaemia}} — blood glucose stays {{c2::elevated even during fasting}}, and glucose {{c3::spills into the urine}}.",
 "The club that can't clear the floor. 📉 (d3.3.4)"),
("Symptoms of untreated diabetes include {{c1::frequent urination}}, {{c2::constant thirst}}, {{c3::tiredness}} and glucose in urine (because water reabsorption in the kidney fails).",
 "Pee a lot, drink a lot, feel dead. 🥤 (d3.3.4)"),
("Type 1 diabetes: {{c1::autoimmune destruction of β cells}} → little or no {{c2::insulin}} produced; onset usually {{c3::early (childhood)}}; treated with {{c4::insulin injections}}.",
 "The DJ never shows up. 🚫🎧 (d3.3.4)"),
("Insulin injections must be timed because {{c1::insulin does not last long in the blood}} — it is rapidly broken down, so doses must match meals and activity.",
 "Short-lived DJ set. ⏱ (d3.3.4)"),
("Type 2 diabetes: insulin IS produced but target cells {{c1::cannot respond}} — insulin receptors / glucose transporters are {{c2::down-regulated or deficient}}; onset usually {{c3::later (adult)}}.",
 "Blown speakers: signal sent, nothing heard. 🔊 (d3.3.4)"),
("Risk factors for type 2 diabetes: {{c1::sugary/fatty diet}}, {{c2::obesity}}, {{c3::lack of exercise}} and {{c4::genetics}}.",
 "Lifestyle + genes. 🍟 (d3.3.4)"),
("Type 2 diabetes is managed with {{c1::diet control}} (low glycaemic index foods, high fibre, small frequent meals), {{c2::exercise}} and {{c3::weight loss}} — not routine insulin.",
 "Fix the floor, not the DJ. 🥗 (d3.3.4)"),
("The glucose tolerance test: a standard glucose drink, then {{c1::repeated blood glucose measurements}}. A diabetic curve {{c2::peaks higher}} and takes far longer to return to baseline.",
 "The sugar stress test. 📈 (d3.3.4)"),
# --- D3.3.5 thermoregulation chain ---
("Core temperature is regulated around a set point of about {{c1::37°C}} by the {{c2::hypothalamus}}, which acts as the {{c3::integrating centre}} comparing blood temperature against the set point.",
 "The head bouncer of the thermostat. 🌡 (d3.3.5)"),
("Temperature is detected by {{c1::peripheral thermoreceptors}} in the {{c2::skin}} and {{c3::central thermoreceptors}} deep in the body (including in the hypothalamus).",
 "Sensors at the door and in the booth. 🚪🌡 (d3.3.5)"),
("Cold response chain: hypothalamus secretes {{c1::TRH}} (a {{c2::tripeptide}}) → anterior pituitary secretes {{c3::TSH}} (a {{c4::glycoprotein}}) → thyroid gland secretes {{c5::thyroxin}} (which contains {{c6::iodine}}).",
 "TRH → TSH → thyroxin, the hormone relay. 📣 (d3.3.5)"),
("Thyroxin increases the {{c1::metabolic rate}} of the {{c2::liver, muscle and brain}}, generating more heat — the long-term hormonal heat-up, layered on top of fast nervous shivering.",
 "Turn up the furnace slowly. 🔥 (d3.3.5)"),
("The effectors for temperature regulation are {{c1::muscle}} (shivering, activity) and {{c2::adipose tissue}} (brown fat heat, insulation).",
 "The heaters. 🏋 (d3.3.5)"),
# --- D3.3.6 heat control mechanisms ---
("When too HOT: skin arterioles {{c1::dilate}} ({{c2::vasodilation}}) → more warm blood at the skin surface → heat {{c3::radiates away}}; skin looks {{c4::pink}}.",
 "Open the doors, flush the heat. 🚪 (d3.3.6)"),
("Sweating cools by {{c1::evaporation}}, which removes {{c2::latent heat}} — humans can sweat up to {{c3::2 L per hour}}; sweat contains solutes like {{c4::sodium}} left on the skin.",
 "The sprinkler system. 💦 (d3.3.6)"),
("When too COLD: skin arterioles {{c1::constrict}} ({{c2::vasoconstriction}}) → less blood at the skin surface → {{c3::less heat lost}}; skin looks {{c4::pale}}.",
 "Shut the doors, keep the warmth. 🚪 (d3.3.6)"),
("Shivering = {{c1::rapid involuntary muscle contractions}} that generate {{c2::heat}} from the effort — a fast nervous response to cold.",
 "The body's shiver-dance. 🕺 (d3.3.6)"),
("Piloerection (hair raising) {{c1::traps an insulating air layer}} — effective in furry mammals but {{c2::largely ineffective in humans}} (goosebumps).",
 "The dead-end heater. 🪶 (d3.3.6)"),
("Brown adipose tissue generates heat by {{c1::uncoupled respiration}}: mitochondria burn fuel but make {{c2::no ATP}}, releasing all the energy as {{c3::heat}}.",
 "The furnace with no output but heat. 🔥 (d3.3.6)"),
("Arterioles don't physically move — only their {{c1::diameter changes}}, which alters {{c2::blood flow through skin capillaries}}. Exam trap: never write 'vessels move closer to the skin'.",
 "Diameter, not location. 📐 (d3.3.6)"),
("Vasodilation alone is mild cooling; {{c1::sweating}} is the serious cooler — which is why humid heat is miserable: {{c2::sweat cannot evaporate}}.",
 "Evaporation is the whole game. 💧 (d3.3.6)"),
# --- D3.3.7 kidney roles (AHL) ---
("The kidney has two roles: {{c1::excretion}} (removing metabolic waste from the blood) and {{c2::osmoregulation}} (controlling the osmotic concentration of body fluids).",
 "Bouncer + water valve. 🫘 (d3.3.7)"),
("The main nitrogenous waste excreted by the kidney is {{c1::urea}}, produced in the {{c2::liver}} by {{c3::deamination}} of excess amino acids.",
 "The liver's toxic by-product. ☣ (d3.3.7)"),
("Osmolarity (osmotic concentration) is measured in {{c1::osmoles per litre (osmol L⁻¹)}} — blood is about {{c2::300 mOsm L⁻¹}}.",
 "Units or zero marks. 📏 (d3.3.7)"),
("The working unit of the kidney is the {{c1::nephron}} — about {{c2::one million per kidney}}, consisting of {{c3::Bowman's capsule + glomerulus}}, {{c4::proximal convoluted tubule}}, {{c5::loop of Henle}}, {{c6::distal convoluted tubule}} and {{c7::collecting duct}}.",
 "The kidney's assembly line. 🏭 (d3.3.7)"),
("The kidney filters about {{c1::180 L}} of fluid per day but only ~{{c2::1.5 L}} leaves as urine — nearly everything is reabsorbed.",
 "180 in, 1.5 out. 📊 (d3.3.7)"),
("The kidney has two regions: the outer {{c1::cortex}} (glomeruli, Bowman's capsules, convoluted tubules) and the inner {{c2::medulla}} (loops of Henle, collecting ducts) with its {{c3::solute gradient}}.",
 "Cortex outside, medulla inside. 🍩 (d3.3.7)"),
# --- D3.3.8 ultrafiltration + PCT (AHL) ---
("At the glomerulus, blood is filtered under {{c1::high pressure}} — the {{c2::afferent arteriole is wider than the efferent}}, forcing fluid through into Bowman's capsule: {{c3::ultrafiltration}}.",
 "High pressure + tiny holes. 💨 (d3.3.8)"),
("The filter stack has three layers: {{c1::fenestrated capillary endothelium}} (pores ~{{c2::100 nm}}), the {{c3::basement membrane}} (a {{c4::negatively charged glycoprotein mesh}} — the real filter), and {{c5::podocyte foot processes}} with slit pores.",
 "Three bouncers, one real filter. 🕸 (d3.3.8)"),
("The basement membrane blocks {{c1::plasma proteins}} (and blood cells, platelets) because of {{c2::pore size}} AND its {{c3::negative charge repelling them}}; it is the main filtration barrier.",
 "Charge + size = no proteins through. ⚡ (d3.3.8)"),
("Filtrate entering Bowman's capsule contains {{c1::water, ions, glucose, amino acids and urea}} but NOT {{c2::blood cells, platelets or plasma proteins}}.",
 "The guest list. 📋 (d3.3.8)"),
("In the PCT, {{c1::all glucose and amino acids}} and about {{c2::80% of water and mineral ions}} are reabsorbed back into the blood — {{c3::selective reabsorption}}.",
 "The velvet-rope grab-back. 🧲 (d3.3.8)"),
("The PCT is built for reabsorption: {{c1::microvilli}} (huge surface area), {{c2::tight junctions}} (no leakage between cells) and {{c3::many mitochondria}} (energy for active transport).",
 "The custom-built reabsorber. 🏗 (d3.3.8)"),
("In the PCT, {{c1::Na⁺}} is actively transported out, {{c2::Cl⁻}} follows the charge gradient, glucose and amino acids are transported with Na⁺ ({{c3::cotransport}}), and water follows by {{c4::osmosis}}.",
 "Sodium leads, everything follows. 🧂 (d3.3.8)"),
# --- D3.3.9 loop of Henle (AHL) ---
("The {{c1::descending limb}} of the loop of Henle is permeable to {{c2::water}} but not salts — water leaves, so the filtrate gets {{c3::saltier}} as it descends.",
 "Water out, salts stay. 💧 (d3.3.9)"),
("The {{c1::ascending limb}} is impermeable to {{c2::water}} but actively pumps {{c3::Na⁺}} out into the medulla — so the filtrate gets {{c4::more dilute}} as it ascends.",
 "Salts out, water stays. 🧂 (d3.3.9)"),
("The loop of Henle is a {{c1::countercurrent multiplier}}: the salt pumped out of the ascending limb pulls water out of the descending limb, making the filtrate saltier, which lets the ascending limb pump even more — each cycle {{c2::amplifies the gradient}}.",
 "The salt ladder climbs itself. 🪜 (d3.3.9)"),
("The medulla salt gradient runs from about {{c1::300 mOsm L⁻¹}} (cortex end) to {{c2::~1200 mOsm L⁻¹}} (deep medulla) — the gradient that later drains the collecting duct.",
 "300 → 1200, the ladder. ⬆ (d3.3.9)"),
("The {{c1::vasa recta}} flows alongside the loop of Henle in the same countercurrent pattern, so it does NOT wash away the medulla gradient.",
 "The gradient's bodyguard. 🛡 (d3.3.9)"),
# --- D3.3.10 ADH osmoregulation (AHL) ---
("Osmoreceptors in the {{c1::hypothalamus}} monitor blood osmolarity; when it rises (dehydration), the {{c2::posterior pituitary}} releases {{c3::ADH}} (antidiuretic hormone, aka {{c4::vasopressin}}).",
 "Are De Hydrated → ADH. 🚰 (d3.3.10)"),
("ADH makes the {{c1::collecting duct}} (and DCT) permeable to water by causing {{c2::aquaporin}} channels stored in {{c3::vesicles}} to fuse with the cell membrane.",
 "Aquaporins to the wall. 🔓 (d3.3.10)"),
("More ADH → more aquaporins → more water reabsorbed into the salty medulla → {{c1::concentrated, low-volume urine}}.",
 "Tight water policy. 🧱 (d3.3.10)"),
("When well hydrated: little ADH → aquaporins stay in vesicles → {{c1::dilute, high-volume urine}}.",
 "Open the floodgates. 🌊 (d3.3.10)"),
("The ADH loop is negative feedback on {{c1::blood osmolarity}}: water reabsorbed → osmolarity falls → {{c2::ADH secretion stops}}.",
 "Self-cancelling again. 🔄 (d3.3.10)"),
("ADH is {{c1::made in the hypothalamus}} but {{c2::released by the posterior pituitary}} — the classic exam trap.",
 "Made upstairs, released downstairs. 🏢 (d3.3.10)"),
# --- D3.3.11 blood routing (AHL) ---
("Cardiac output rises with activity: about {{c1::4 L min⁻¹}} asleep, {{c2::5 L min⁻¹}} at rest, up to {{c3::25 L min⁻¹}} in hard exercise — and it is routed by {{c4::arteriole diameter}}.",
 "The router's budget. 🚦 (d3.3.11)"),
("Blood is distributed by {{c1::vasodilation/vasoconstriction of arterioles}}, {{c2::precapillary sphincters}} at capillary beds and {{c3::shunt vessels}} that bypass beds entirely.",
 "Traffic lights + valves + bypasses. 🛣 (d3.3.11)"),
("The brain always receives about {{c1::20% of cardiac output}} in all states — it {{c2::cannot store fuel}}, so its supply never drops.",
 "The VIP that never loses service. 🧠 (d3.3.11)"),
("During exercise: {{c1::skeletal muscle}} blood flow increases greatly; {{c2::gut and kidneys}} constrict (their work can wait).",
 "Muscles first, digestion last. 🏃 (d3.3.11)"),
("During sleep: muscle flow drops, kidneys reduce flow (no midnight toilet trips) and the {{c1::brain gets extra blood during REM sleep}}.",
 "Sleep reroutes the map. 😴 (d3.3.11)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
print(f"Wrote {OUT} — {len(CARDS)} notes")
