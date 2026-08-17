#!/usr/bin/env python3
"""Build D3.1 Reproduction cloze deck (~100 cards) for the Bio HL deck.
Matches the existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_d31_anki.py  ->  writes D3.1_Reproduction.apkg
"""
import genanki, os

MODEL_ID = 1613201144
DECK_ID  = 2059400110  # same Bio HL deck as C2.1/B3.1/B3.3/D2.1/D3.2 -> merges
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "topics", "bio", "reproduction", "D3.1_Reproduction.apkg")

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
# --- D3.1.1 sexual vs asexual ---
("Reproduction is achieved either {{c1::sexually}} or {{c2::asexually}}. Sexual reproduction brings about {{c3::change}}, asexual reproduction brings about {{c4::continuity}}.",
 "The club theme: remix vs loop. 🔄 (d3.1.1)"),
("In {{c1::asexual}} reproduction: {{c2::one}} parent, mitosis used {{c3::throughout}} the life cycle, offspring {{c4::genetically identical}} to each other and the parent, existing gene combinations are {{c5::maintained}}, and {{c6::no genetic variation}} is generated.",
 "The same track on repeat. 🔁 (d3.1.1)"),
("In {{c1::sexual}} reproduction: {{c2::two}} parents (one male, one female), meiosis used {{c3::once per generation}}, offspring genetically {{c4::different}} from each other and parents, new gene combinations are produced, and {{c5::genetic variation}} is generated.",
 "A fresh remix every generation. 🎧 (d3.1.1)"),
("Asexual reproduction suits organisms adapted to an {{c1::unchanging}} environment; sexual reproduction can produce offspring {{c2::better adapted}} than parents if the environment is {{c3::changing}}.",
 "Loop for stable crowds, remix for shifting scenes. 🌍 (d3.1.1)"),
("Sexual life cycles must include two opposite processes: {{c1::meiosis}} (which {{c2::halves}} chromosome number) and {{c3::fusion of gametes}} / fertilization (which {{c4::doubles}} chromosome number).",
 "Without meiosis, chromosome number would double every generation. ⚖ (d3.1.2)"),
("Gametes are {{c1::haploid}} (n) cells, while body cells are {{c2::diploid}} (2n) with two copies of most genes. In animals meiosis happens during {{c3::creation of the gametes}}.",
 "Half-price tickets for the show. 🎫 (d3.1.2)"),
# --- D3.1.3 anisogamy ---
("All plants and animals are {{c1::anisogamous}} — they have two distinct gamete types. Male gametes are {{c2::smaller}} and {{c3::motile}} (they travel to the female), with {{c4::less}} food reserves and {{c5::more}} produced; female gametes are {{c6::larger}} and {{c7::sessile}}, with {{c8::more}} food reserves for embryo development, produced in {{c9::fewer}} numbers.",
 "The VIP courier vs the stocked lounge. ♂♀ (d3.1.3)"),
("The first known organism to produce two different gamete types was {{c1::Bangiomorpha pubescens}}, a red alga from {{c2::1,200-million-year-old}} rocks — the first known sexually reproducing organism.",
 "The first remix ever dropped. 🦠 (d3.1.3)"),
# --- D3.1.4 anatomy male ---
("In the male reproductive system, the {{c1::testis}} produces sperm and testosterone; the {{c2::scrotum}} holds testes at lower than core body temperature; the {{c3::epididymis}} stores sperm until ejaculation; the {{c4::sperm duct}} (vas deferens) transfers sperm during ejaculation.",
 "Backstage layout, male. 🎸 (d3.1.4)"),
("The {{c1::seminal vesicle}} and {{c2::prostate gland}} secrete fluid containing {{c3::alkali, proteins and fructose}} that is added to sperm to make {{c4::semen}}; the {{c5::urethra}} transfers semen during ejaculation and urine during urination; the {{c6::penis}} penetrates the vagina for ejaculation near the cervix.",
 "The merch table crew. 📦 (d3.1.4)"),
# --- D3.1.4 anatomy female ---
("In the female reproductive system, the {{c1::ovary}} produces eggs, oestradiol and progesterone; the {{c2::oviduct}} collects eggs at ovulation, provides a site for fertilization, then moves the embryo to the uterus; the {{c3::uterus}} provides for the embryo and foetus during pregnancy.",
 "Backstage layout, female. 🎤 (d3.1.4)"),
("The {{c1::cervix}} protects the foetus during pregnancy and then dilates to provide a birth canal; the {{c2::vagina}} stimulates the penis to cause ejaculation and provides a birth canal; the {{c3::vulva}} protects the internal parts of the female reproductive system.",
 "Doors and corridors. 🚪 (d3.1.4)"),
# --- D3.1.5 menstrual cycle ---
("The menstrual cycle consists of the {{c1::uterine}} cycle and the {{c2::ovarian}} cycle together. Day 1 is the start of {{c3::menstruation}}, when the ovaries have returned to the {{c4::follicular}} phase.",
 "The monthly booking calendar. 🗓 (d3.1.5)"),
("In the ovarian cycle: the first half is the {{c1::follicular}} phase (a group of follicles develops, each with an egg); the most developed follicle breaks open releasing its egg — {{c2::ovulation}} — usually on about {{c3::Day 14}}; the second half is the {{c4::luteal}} phase, when the follicle wall develops into the {{c5::corpus luteum}}.",
 "One egg leaves the building each month. 🥚 (d3.1.5)"),
("In the uterine cycle, the {{c1::endometrium}} thickens and becomes more richly supplied with blood during the {{c2::luteal}} phase in preparation for implantation; if there is no embryo it breaks down and is shed during {{c3::menstruation}}.",
 "The room gets redecorated, then cleared if no guest arrives. 🛏 (d3.1.5)"),
("{{c1::FSH}} (follicle-stimulating hormone) and {{c2::LH}} (luteinizing hormone) are {{c3::protein}} hormones from the {{c4::pituitary}} gland; {{c5::oestradiol}} and {{c6::progesterone}} are {{c7::ovarian steroid}} hormones that influence gene expression.",
 "The four managers of the booking calendar. 🎛 (d3.1.5)"),
("FSH stimulates the {{c1::development of follicles}}, each containing an oocyte, and stimulates secretion of {{c2::oestradiol}} by the follicle wall.",
 "Booking agent no.1. 📈 (d3.1.5)"),
("Oestradiol stimulates {{c1::repair and thickening of the endometrium}} after menstruation and an increase in {{c2::FSH receptors}} (positive feedback boosting oestradiol); at high levels it {{c3::inhibits FSH secretion}} (negative feedback) and {{c4::stimulates LH secretion}}.",
 "The headliner: builds the room, then flips to LH. 🌟 (d3.1.5)"),
("LH rises to a sharp peak at the end of the follicular phase and stimulates {{c1::completion of meiosis}} in the oocyte and {{c2::ovulation}}; afterwards it stimulates the follicle wall to develop into the {{c3::corpus luteum}}.",
 "The trigger that fires the egg. 🎯 (d3.1.5)"),
("Progesterone, secreted by the {{c1::corpus luteum}}, maintains the {{c2::endometrium}} in the luteal phase; if fertilization does not occur the corpus luteum {{c3::breaks down}} and progesterone falls, allowing menstruation.",
 "The bouncer holding the room together. 🛡 (d3.1.5)"),
# --- D3.1.6 fertilization ---
("Fertilization is the {{c1::fusion of a sperm with an egg}} to form a {{c2::zygote}}. Sperm plasma membranes have receptors that detect {{c3::chemicals released by the egg}}, enabling directional swimming.",
 "The courier smells the venue. 🧭 (d3.1.6)"),
("The egg is surrounded by a cloud of {{c1::follicle cells}} and a layer of {{c2::glycoproteins}} (the zona pellucida). The sperm pushes between the cells and digests its way through the glycoproteins to reach the egg plasma membrane.",
 "The moat and the wall around the castle. 🏰 (d3.1.6)"),
("The first sperm to penetrate the zona pellucida binds, and the membranes of sperm and egg {{c1::fuse}}; the {{c2::sperm nucleus}} then enters the egg — the moment of fertilization. The sperm {{c3::tail}} either does not penetrate or is broken down inside the zygote; sperm {{c4::mitochondria}} are usually all destroyed.",
 "One guest gets through the door. 🚪 (d3.1.6)"),
("The zygote's two haploid nuclei remain separate until the first mitosis, when both nuclear membranes break down and {{c1::23 chromosomes from each}} participate jointly in mitosis — producing two nuclei each with {{c2::46 chromosomes}}.",
 "The two halves of the ticket become one backstage pass. 🎫 (d3.1.6)"),
# --- D3.1.7 IVF ---
("In IVF, the first stage is usually {{c1::down-regulation}}: a drug stops the pituitary secreting {{c2::FSH or LH}} for about two weeks, suspending the normal menstrual cycle so doctors control timing.",
 "Mute the club's own calendar first. 🔇 (d3.1.7)"),
("IVF then uses daily {{c1::FSH injections}} for 7-12 days to stimulate follicles; the aim is far more follicles than normal — between {{c2::8 and 15}} is ideal. When follicles are {{c3::18 mm}} in diameter they are matured by an injection of {{c4::hCG}}.",
 "Crank the booking agents up to 11. 💉 (d3.1.7)"),
("In IVF, eggs are collected {{c1::34-35 hours}} after the hCG injection using a micropipette on an ultrasound scanner. Each egg is mixed with {{c2::50,000-100,000}} sperm in a dish incubated at {{c3::37°C}}; embryos are placed in the uterus about {{c4::48 hours}} old, with extra {{c5::progesterone}} given to maintain the lining.",
 "The lab remix. 🧪 (d3.1.7)"),
# --- D3.1.8 plant reproduction ---
("Stamens are the male parts of a flower: an {{c1::anther}} supported by a {{c2::filament}}. Diploid cells in the anther divide by {{c3::meiosis}} to produce four haploid cells, each developing into a {{c4::pollen grain}}. The pollen nucleus divides by mitosis to produce {{c5::three haploid nuclei}}, two of which are {{c6::male gametes}}.",
 "The DJ booth of the flower. 🌸 (d3.1.8)"),
("Carpels are the female parts of a flower: an {{c1::ovary}}, a {{c2::stigma}} (where pollen is received) and a {{c3::style}} connecting them. The ovary contains {{c4::ovules}}; one cell in each ovule divides by meiosis then three times by mitosis to produce {{c5::eight haploid nuclei}}, one of which is the {{c6::egg}} (female gamete).",
 "The VIP lounge of the flower. 🌺 (d3.1.8)"),
("{{c1::Pollination}} is the transfer of pollen from an {{c2::anther}} to a {{c3::stigma}}, usually by wind or animals. From each pollen grain a {{c4::pollen tube}} grows down the style to the ovary, carrying the {{c5::male gametes}}; when it reaches the ovule the male gametes are released and fertilization occurs.",
 "The courier service. 📬 (d3.1.8)"),
("The product of fertilization is a {{c1::zygote}} which develops into an embryo with an {{c2::embryo root}}, an {{c3::embryo shoot}} and one or two {{c4::cotyledons}} (embryo leaves). Flower reproduction is sexual because it includes {{c5::meiosis, gamete production and fertilization}}.",
 "The new act gets its band members. 🎻 (d3.1.8)"),
# --- D3.1.9 insect-pollinated flower ---
("Insect-pollinated flowers have {{c1::large, brightly coloured petals}} that advertise the flower and act as a landing stage; {{c2::scent}} is secreted from the petals to advertise it.",
 "Bribe the couriers with visuals and smell. 🌈 (d3.1.9)"),
("Insect-pollinated flowers have {{c1::large, spiky pollen grains}} that stick to insects and are protein-rich food; a {{c2::large, sticky stigma}} to collect pollen from visiting insects; and {{c3::nectaries}} secreting nectar deep inside the flower so insects can only reach them by brushing past the {{c4::anthers and stigma}}.",
 "The courier has to touch the merch on the way in. 🐝 (d3.1.9)"),
("In flower structure: {{c1::petals}} help insects find the flower; {{c2::anthers}} produce pollen with male gametes; {{c3::filaments}} hold anthers where insects brush them; {{c4::stigma}} captures pollen; {{c5::style}} positions the stigma and guides the pollen tube to the ovary; {{c6::ovary}} holds ovules and becomes the fruit; {{c7::ovules}} hold the female gamete and become seeds; {{c8::sepals}} protect the floral organs during development.",
 "The venue map. 🗺 (d3.1.9)"),
# --- D3.1.10 cross-pollination ---
("{{c1::Cross-pollination}} (pollen from a flower on one plant to a stigma of a flower on another plant) promotes {{c2::genetic variation}} and therefore evolution, and promotes {{c3::hybrid vigour}} — offspring of crosses between genetically unrelated plants tend to be healthy and grow strongly.",
 "Fresh genes in, healthy crowd out. 💪 (d3.1.10)"),
("Self-pollination (anther to stigma on the same plant) is extreme {{c1::inbreeding}}; inbreeding increases the chance of a {{c2::rare recessive allele}} being inherited twice, causing genetic disorders — the general trend of premature death, failure to thrive and infertility is called {{c3::inbreeding depression}}.",
 "Same-genome marriages end badly. ⚠ (d3.1.10)"),
("Plant strategies that prevent self-pollination include: separate male and female flowers on the {{c1::same plant}} (e.g. maize), male and female flowers on {{c2::different plants}} (e.g. ginkgo, stinging nettle), and anthers and stigmas maturing at different times — {{c3::protandry}} = anthers first (e.g. foxglove), {{c4::protogyny}} = stigma first (e.g. sacred lotus).",
 "Staggered sets so you can't date yourself. ⏱ (d3.1.10)"),
# --- D3.1.11 self-incompatibility ---
("{{c1::Self-incompatibility}} is when pollen from a plant's own stamens fails to germinate or its pollen tube stops growing before reaching the ovary — preventing inbreeding when a single individual acts as both parents.",
 "The ID check at the door. 🪪 (d3.1.11)"),
("Self-incompatibility has a {{c1::genetic basis}} with alternative alleles of one or more genes (S-genes); plants with the {{c2::same self-incompatibility alleles}} cannot successfully pollinate each other. It is the {{c3::converse of the immune system}}: immunity rejects {{c4::non-self}}, self-incompatibility rejects {{c5::self}}.",
 "Same S-allele = bounced at the door. 🚫 (d3.1.11)"),
# --- D3.1.12 seed dispersal ---
("Seed dispersal reduces {{c1::competition between offspring and parent}} and helps {{c2::spread the species}}. Fruit types: {{c3::dry and explosive}}, {{c4::fleshy and attractive to animals}}, {{c5::feathery or winged}} to catch the wind, or {{c6::covered in hooks}} that catch onto animal coats.",
 "The tour bus leaves the club. 🚌 (d3.1.12)"),
("Pollination transfers {{c1::pollen}} from {{c2::anther to stigma}}, usually by {{c3::wind or animals}}; seed dispersal moves {{c4::seeds}} from the female parent to a {{c5::germination site}}, by {{c6::wind, animals or explosion}}. They are separate processes in the plant sexual life cycle.",
 "Courier drop-off vs tour bus departure. 📦 (d3.1.12)"),
# --- D3.1.13 puberty ---
("Puberty is controlled by {{c1::gonadotropin-releasing hormone}} ({{c2::GnRH}}), a peptide of {{c3::10 amino acids}}, synthesized by a few hundred neurons in the {{c4::hypothalamus}} and secreted into a blood vessel carrying it directly to the {{c5::pituitary gland}}.",
 "The debut night's promoter. 🎤 (d3.1.13)"),
("GnRH is secreted in {{c1::pulses}} (peaks at least hourly). {{c2::Lower frequency}} pulses stimulate FSH secretion; {{c3::higher frequency}} pulses stimulate LH secretion.",
 "The beat of the pulse decides the hormone. 🥁 (d3.1.13)"),
("In males: {{c1::FSH}} stimulates testis growth, {{c2::LH}} stimulates testosterone secretion by {{c3::Leydig cells}}; testosterone causes secondary sexual characteristics — {{c4::penis enlargement, pubic hair growth, voice deepening}} (larynx growth).",
 "The male debut set list. 🎸 (d3.1.13)"),
("In females: {{c1::FSH}} stimulates follicle development; the follicle wall secretes {{c2::oestradiol}}; {{c3::LH}} stimulates the follicle wall to become the {{c4::corpus luteum}}, which secretes oestradiol and {{c5::progesterone}}; oestradiol causes {{c6::uterus enlargement, breast development, pubic and underarm hair}}; progesterone prepares the {{c7::mammary glands}} for lactation.",
 "The female debut set list. 🎹 (d3.1.13)"),
("GnRH secretion starts in a foetus about {{c1::10 weeks}} after fertilization, continues through pregnancy, stops when a baby is {{c2::4-6 months}} old, and only resumes when the brain decides puberty has arrived (during teenage years).",
 "The promoter is on standby for years. ⏸ (d3.1.13)"),
# --- D3.1.14 gametogenesis ---
("Spermatogenesis happens in the {{c1::testes}}, which are a coiled mass of {{c2::seminiferous tubules}} with interstitial gaps filled with testosterone-secreting {{c3::Leydig cells}}. The outer layer of cells in the tubules is a {{c4::germinal epithelium}} where mitosis occurs continuously.",
 "The factory floor. 🏭 (d3.1.14)"),
("In spermatogenesis: germinal epithelium cells divide by mitosis and are displaced inwards; they grow into {{c1::primary spermatocytes}} (2n), divide by meiosis I into {{c2::secondary spermatocytes}} (n), then meiosis II into {{c3::spermatids}} (n), which differentiate into {{c4::sperm}} by growing a tail and reducing cytoplasm. Large nurse cells called {{c5::Sertoli cells}} help spermatids develop.",
 "4 sperm per meiosis. 🧬 (d3.1.14)"),
("Oogenesis happens in the {{c1::ovaries}}, with the first stages completed before birth. There are about {{c2::400,000 primary follicles}} at birth and no more are ever produced. A primary follicle = an oocyte (arrested in the {{c3::first division of meiosis}}) surrounded by a single layer of follicle cells.",
 "The one-off artwork, stockpiled before birth. 🖼 (d3.1.14)"),
("In oogenesis, each menstrual cycle a small batch of primary follicles is stimulated by {{c1::FSH}}, but usually only {{c2::one}} becomes a mature follicle. The oocyte completes meiosis I at ovulation and meiosis II after fertilization; the result is {{c3::1 egg per meiosis}}, with polar bodies discarded. Eggs contain more {{c4::cytoplasm}} than any other human cell, providing food reserves for the embryo.",
 "1 egg per month vs millions of sperm per day. 🥚 (d3.1.14)"),
("Key differences: spermatogenesis produces {{c1::4}} gametes per meiosis, {{c2::millions per day}}, from puberty onwards, sperm have {{c3::little cytoplasm}} (faster swimming); oogenesis produces {{c4::1}} gamete per meiosis, about {{c5::1 per month}}, production initiated in foetuses and completed during the menstrual cycle until {{c6::menopause}}, eggs have {{c7::large cytoplasm}} for the embryo.",
 "Factory vs one-off, side by side. ⚖ (d3.1.14)"),
# --- D3.1.15 polyspermy ---
("Fusion of more than one sperm with an egg is {{c1::polyspermy}}; it would produce a {{c2::triploid}} zygote that soon dies. Two processes make it very infrequent: the {{c3::acrosome reaction}} and the {{c4::cortical reaction}}.",
 "Only one guest through the velvet rope. 🔒 (d3.1.15)"),
("The {{c1::acrosome reaction}}: sperm bind to specific glycoproteins in the zona pellucida, triggering release of the contents of the {{c2::acrosome}} (a membrane-bound sac of enzymes in the sperm head); the enzymes digest the glycoproteins, weakening the zona so the sperm tail's beating can push it through to the egg plasma membrane.",
 "The courier burns through the wall. 🔥 (d3.1.15)"),
("The {{c1::cortical reaction}}: when the first sperm's nucleus enters, the egg activates and its {{c2::cortical granules}} (enzyme vesicles near the plasma membrane) release contents by {{c3::exocytosis}}; the enzymes {{c4::toughen the zona pellucida}} and change the glycoproteins sperm bind to, so no more sperm can penetrate.",
 "The door slams shut behind guest one. 🚪 (d3.1.15)"),
# --- D3.1.16 blastocyst ---
("After fertilization, DNA replication starts about {{c1::6 hours}} later, and the two haploid nuclei divide jointly by mitosis about {{c2::30 hours}} after fertilization. Early cell cycles happen every ~18 hours without cell growth, so cell size {{c3::decreases}}.",
 "The first rehearsals. 🎭 (d3.1.16)"),
("When the embryo is 6-7 days old it becomes a hollow ball called the {{c1::blastocyst}} (~250 cells, ~200 μm). It has an {{c2::inner cell mass}} (develops into the human body), a surrounding outer layer called the {{c3::trophoblast}} (develops into the placenta) and a fluid-filled cavity ({{c4::blastocoele}}).",
 "The new act moving into the venue. 📦 (d3.1.16)"),
("The blastocyst travels down the {{c1::oviduct}} (moved by cilia wafting), the toughened zona pellucida breaks down, and it attaches to the {{c2::endometrium}} in a process called {{c3::implantation}} — its outer cell layer grows finger-like projections that exchange materials (foods and oxygen) with the mother's blood. By 8 weeks it has started forming bone tissue and is called a {{c4::foetus}}.",
 "Moving in day. 🛋 (d3.1.16)"),
# --- D3.1.17 hCG / pregnancy test ---
("{{c1::hCG}} (human chorionic gonadotropin) is a medium-sized {{c2::protein}} produced by the embryo's {{c3::trophoblast}} cells from the blastocyst stage onwards. In the first ~10 weeks it stimulates the {{c4::corpus luteum}} to secrete progesterone, preventing degeneration of the uterus lining.",
 "The tenant's 'I'm alive, keep the room' signal. 📻 (d3.1.17)"),
("After 8-12 weeks of pregnancy the {{c1::placenta}} starts secreting progesterone in response to hCG; the corpus luteum stops hormone production and breaks down. Trophoblast cells in the placenta continue secreting hCG throughout the rest of the pregnancy.",
 "The venue takes over the booking. 🏢 (d3.1.17)"),
("Pregnancy tests detect {{c1::hCG in urine}} using {{c2::monoclonal antibodies}}: a mobile antibody with blue dye binds hCG; further down, an immobilised antibody traps the hCG-antibody complex forming a {{c3::blue band}} (positive); a control band shows the test worked. Two blue bands = pregnant, one = not.",
 "The rent check slip. 🧪 (d3.1.17)"),
# --- D3.1.18 placenta ---
("The placenta is made of {{c1::foetal tissues}} in intimate contact with maternal tissues in the uterus wall. Its basic functional unit is a finger-like piece of foetal tissue called a {{c2::placental villus}}; villi increase in number during pregnancy to cope with the foetus's increasing demands.",
 "The catering corridor. 🍽 (d3.1.18)"),
("In the placenta, {{c1::maternal blood}} flows in spaces around the villi (intervillous spaces) while {{c2::foetal blood}} circulates in capillaries close to each villus surface; the cells separating them (the {{c3::placental barrier}}) are only about {{c4::5 μm}} apart and selectively permeable.",
 "Two crowds separated by a 5 μm wall. 🧱 (d3.1.18)"),
("Across the placenta: {{c1::oxygen, glucose, amino acids, water and antibodies}} pass from maternal to foetal blood (by {{c2::diffusion, facilitated diffusion, osmosis and endocytosis}}); {{c3::carbon dioxide, urea and other wastes}} pass from foetal to maternal blood.",
 "The delivery menu. 📦 (d3.1.18)"),
("The placenta allows humans (placental mammals) to retain the foetus in the uterus much longer than {{c1::monotremes}} (egg-laying) or {{c2::marsupials}} (born underdeveloped, pouch-reared) — needed because the body {{c3::surface-area-to-volume ratio}} becomes smaller as the foetus grows.",
 "Bigger body, smaller ratio, longer residency. 📏 (d3.1.18)"),
# --- D3.1.19 childbirth ---
("During pregnancy, {{c1::progesterone}} inhibits secretion of {{c2::oxytocin}} by the pituitary and inhibits contractions of the {{c3::myometrium}} (uterine muscle). At the end of pregnancy, hormones from the foetus signal the placenta to stop secreting progesterone, so oxytocin starts to be secreted.",
 "The mute switch gets turned off. 🔇 (d3.1.19)"),
("Childbirth is a {{c1::positive feedback}} loop: oxytocin stimulates myometrium contractions → stretch receptors detect them → more oxytocin is secreted → contractions become more frequent and vigorous. Advantage: a gradual increase in contraction intensity, so the baby is born with the minimum intensity needed.",
 "The crowd chanting 'ENCORE!' louder and louder. 👶 (d3.1.19)"),
("Relaxation of muscle fibres in the {{c1::cervix}} causes it to dilate; uterine contractions burst the {{c2::amniotic sac}}; further contractions push the baby out through the cervix and vagina; the {{c3::umbilical cord}} is broken and the baby takes its first breath.",
 "The grand finale. 🎆 (d3.1.19)"),
# --- D3.1.20 HRT ---
("Hormone replacement therapy ({{c1::HRT}}) supplements levels of {{c2::oestrogen and progesterone}} that decrease as a woman approaches the menopause, relieving symptoms such as {{c3::hot flushes, night sweats, mood swings, vaginal dryness and reduced sex drive}}, and helping prevent {{c4::osteoporosis}}.",
 "The remastered mix for the later years. 💊 (d3.1.20)"),
("Early {{c1::observational}} studies suggested HRT reduced the risk of coronary heart disease, but later {{c2::randomised controlled trials}} showed a slightly {{c3::elevated}} risk of CHD, breast cancer and stroke — so HRT use declined dramatically since the early 2000s.",
 "Observational said heart-safe; RCTs said riskier. ⚖ (d3.1.20)"),
("Explanations for the conflicting HRT findings: the observational study used {{c1::observational data}} (women in early menopause, who tend to be more {{c2::affluent}} with better healthcare — a confounder), while the RCTs were {{c3::randomised controlled trials}} with women several years post-menopause. The heart-health link was likely a {{c4::spurious correlation}} — correlation does not equal causation.",
 "The classic confounding trap. 🕵 (d3.1.20)"),
]

deck = genanki.Deck(DECK_ID, "Bio HL (flat)")
deck.add_model(model)
for text, extra in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, extra]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
print(f"OK: {len(CARDS)} notes -> {os.path.abspath(OUT)}")
