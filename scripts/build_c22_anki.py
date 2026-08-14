#!/usr/bin/env python3
"""Build C2.2 Neural Signalling cloze deck for the Bio HL deck.
Matches the existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_c22_anki.py  ->  writes C2.2_Neural_Signalling.apkg
"""
import genanki, os

MODEL_ID = 1607392319
DECK_ID  = 2059400110
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "c2.2", "C2.2_Neural_Signalling.apkg")

model = genanki.Model(
    MODEL_ID,
    "Cloze+",
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>',
    }],
    model_type=1,
)

CARDS = [
# --- C2.2.1 neurons ---
("The nervous system runs on {{c1::neurons}} — about {{c2::85 billion}} of them in a human. A nerve impulse is an {{c3::electrical}} signal carried along nerve fibres.",
 "The cable run. (c2.2.1)"),
("{{c1::Dendrites}} are short branched nerve fibres that collect impulses (e.g. between neurons in the brain); the {{c2::axon}} is the single very elongated fibre that transmits impulses long distances (e.g. toes to spinal cord).",
 "In at the dendrites, out along the axon. (c2.2.1)"),
("The two internal communication systems: the {{c1::endocrine}} system (glands → hormones → blood) and the {{c2::nervous}} system (neurons → electrical impulses).",
 "Slow mail vs fast cable. (c2.2.1)"),
# --- C2.2.2 resting potential ---
("A neuron at rest has a membrane potential of about {{c1::-70 mV}} — cytoplasm {{c2::negative}} relative to the fluid outside.",
 "The standby voltage. (c2.2.2)"),
("The Na⁺/K⁺ pump moves {{c1::3 Na⁺ out}} and {{c2::2 K⁺ in}} per cycle, using {{c3::ATP}} (active transport), creating both a charge imbalance and concentration gradients.",
 "The 3:2 cover charge. (c2.2.2)"),
("The resting membrane is about {{c1::50}}× more permeable to K⁺ than Na⁺, so {{c2::K⁺ leaks out}} faster — increasing the charge imbalance.",
 "The leak. (c2.2.2)"),
("Negatively charged {{c1::proteins (organic anions)}} inside the nerve fibre also contribute to the resting potential's negative inside.",
 "The anions. (c2.2.2)"),
("The membrane potential of a typical living cell is 10–{{c1::100}} mV; a liver cell sits at about {{c2::-40 mV}}.",
 "Scale reference. (c2.2.2)"),
# --- C2.2.3 action potential ---
("An action potential has two main phases: {{c1::depolarization}} (potential from negative to positive) and {{c2::repolarization}} (back from positive to negative). Both are due to movement of {{c3::positively charged ions}} — not electrons.",
 "The drop and the reset. (c2.2.3)"),
("Depolarization is caused by {{c1::Na⁺}} diffusing {{c2::into}} the neuron through open sodium channels — the potential rises from −70 mV to about {{c3::+30 mV}}.",
 "Na⁺ in → +30. (c2.2.3)"),
("Repolarization is caused by closing of {{c1::sodium channels}} and opening of {{c2::potassium channels}}; {{c3::K⁺ diffuses out}}, returning the inside to negative.",
 "K⁺ out → back to −70. (c2.2.3)"),
("Na⁺ concentration outside a resting neuron is about {{c1::10}}× higher than inside.",
 "The gradient that powers the drop. (c2.2.3)"),
("After an action potential, the Na⁺/K⁺ pump takes a few {{c1::milliseconds}} to re-establish the concentration gradients before another AP can fire.",
 "Recharge time. (c2.2.3)"),
("A nerve impulse is an electrical signal, but it does NOT involve movement of {{c1::electrons}} — it is movement of {{c2::ions}} (positively charged particles).",
 "Ions, not electrons. (c2.2.3)"),
# --- C2.2.4 speed ---
("A typical human nerve fibre (~1 µm diameter) conducts at about {{c1::1 m/s}}. The squid giant axon (up to {{c2::500 µm}}) conducts at {{c3::25 m/s}} — it coordinates the jet-propulsion escape response.",
 "Fatter cable, faster signal. (c2.2.4)"),
("Myelination: {{c1::Schwann cells}} wrap the fibre, with bare gaps called {{c2::nodes of Ranvier}}; the impulse jumps node to node ({{c3::saltatory}} conduction) at up to {{c4::100 m/s}}.",
 "The express lane. (c2.2.4)"),
("Earthworms have only {{c1::three}} giant axons, used solely for escape — giant fibres cost space and resources.",
 "Why fat cables are rare. (c2.2.4)"),
("Squid giant axons coordinate a rapid {{c1::jet-propulsion}} escape response.",
 "Why the squid needs speed. (c2.2.4)"),
# --- C2.2.5 synapses ---
("A {{c1::synapse}} is a junction between two cells of the nervous system; the gap is only about {{c2::20 nm}} wide, and signals cross it {{c3::one way}} only.",
 "The DJ booth. (c2.2.5)"),
("The three synapse types: sensory {{c1::receptor cell}}–neuron (sense organs), {{c2::neuron}}–neuron (brain and spinal cord), and neuron–{{c3::effector}} (muscle fibres or gland cells).",
 "Receptor, neuron, effector. (c2.2.5)"),
("The {{c1::presynaptic}} neuron brings the impulse to the synapse; the {{c2::postsynaptic}} neuron carries it away.",
 "Before and after the gap. (c2.2.5)"),
("Synaptic transmission is one-way because neurotransmitter is released only from the {{c1::presynaptic}} membrane and receptors exist only on the {{c2::postsynaptic}} membrane.",
 "One-way booth. (c2.2.5)"),
# --- C2.2.6 release ---
("Order of synaptic transmission: impulse arrives → {{c1::Ca²⁺ diffuses in}} through channels in the presynaptic membrane → {{c2::vesicles fuse}} with the membrane → neurotransmitter released by {{c3::exocytosis}}.",
 "Calcium is the trigger. (c2.2.6)"),
# --- C2.2.7 EPSP ---
("After release, neurotransmitter diffuses across the gap (20–40 nm) and binds {{c1::receptors}} on the postsynaptic membrane, causing {{c2::ion channels}} to open; ions diffuse in and the membrane potential rises — an {{c3::excitatory postsynaptic potential (EPSP)}}.",
 "The record lands. (c2.2.7)"),
("If the EPSP is strong enough to reach {{c1::threshold}}, it triggers an {{c2::action potential}} that propagates away from the synapse.",
 "Strong enough = full drop. (c2.2.7)"),
("Acetylcholine is made from {{c1::choline}} (absorbed from the diet) + an {{c2::acetyl group}} (produced by aerobic respiration) inside the presynaptic neuron.",
 "The record's ingredients. (c2.2.7)"),
("{{c1::Acetylcholinesterase}} in the synaptic gap breaks ACh into {{c2::choline and acetate}}; the {{c3::choline}} is reabsorbed into the presynaptic neuron and rebuilt.",
 "The cleanup crew. (c2.2.7)"),
("When ACh binds its receptor at the neuromuscular junction, a {{c1::Na⁺ channel}} opens in the receptor and sodium diffuses in, causing an {{c2::EPSP}}.",
 "ACh → Na⁺ in. (c2.2.7)"),
("The synaptic gap is 20–40 nm — only {{c1::two to four}} times the thickness of a phospholipid bilayer, which is why diffusion across it is so fast.",
 "Tiny gap = fast diffusion. (c2.2.7)"),
# --- C2.2.8 voltage gating ---
("Na⁺ and K⁺ channels in the axon membrane open and close in response to voltage changes — this is called {{c1::voltage-gating}}.",
 "The door policy. (c2.2.8)"),
("The {{c1::threshold potential}} is about {{c2::-50 mV}}; below it, no action potential fires and the pump restores −70 mV — hence the impulse is {{c3::all-or-nothing}}.",
 "The gate at −50. (c2.2.8)"),
("Depolarization is an example of {{c1::positive feedback}}: Na⁺ entry depolarizes further, opening {{c2::more Na⁺ channels}} — a rapid change from −50 to +30 mV.",
 "The snowball. (c2.2.8)"),
("Sodium channels stay open only {{c1::1–2 ms}}; their closing plus potassium channel opening (also {{c2::1–2 ms}}) causes repolarization.",
 "Short open windows. (c2.2.8)"),
# --- C2.2.9 propagation ---
("Propagation of an action potential is due to {{c1::local currents}} — Na⁺ diffusing along inside the axon from the depolarized patch to the neighbouring polarized patch (and in the opposite direction outside).",
 "The relay. (c2.2.9)"),
("The {{c1::refractory period}} after a depolarization prevents propagation of an action potential {{c2::backwards}} along an axon.",
 "The one-way valve. (c2.2.9)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL")
for text, back in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, back]))

genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
