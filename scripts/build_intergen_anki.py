#!/usr/bin/env python3
"""
Chinese B SL literature deck: 代际冲突 (intergenerational conflict)
《家》巴金 · 《背影》朱自清 · 《目送》龙应台
Builds Chinese_Intergenerational_Conflict.apkg next to the topic page.
"""
from __future__ import annotations
from pathlib import Path
import genanki

HUB = Path("C:/Users/ASUS/Desktop/Hermes_Workspace/study-hub")
TOPIC = HUB / "topics" / "chinese" / "intergenerational-conflict"

MODEL_ID = 1764119001
DECK_ID = 1764119002

QFMT = ('<div style=\"font-family:Segoe UI,sans-serif;font-size:22px;line-height:1.6\">'
        '<div style=\"color:#a855f7;font-weight:700;font-size:13px;letter-spacing:2px;margin-bottom:8px\">'
        '代际冲突 · 中文文学</div>{{Front}}</div>')
AFMT = ('<div style=\"font-family:Segoe UI,sans-serif;font-size:20px;line-height:1.6\">{{Front}}'
        '<hr id=answer style=\"border:none;border-top:2px solid #ff2ec4;margin:12px 0\">'
        '<div style=\"color:#f3e8ff\">{{Back}}</div></div>')

model = genanki.Model(
    MODEL_ID,
    "Intergen Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card 1", "qfmt": QFMT, "afmt": AFMT}],
    css=".card{background:#150a26;color:#f3e8ff}",
)

cloze_model = genanki.Model(
    MODEL_ID + 1,
    "Intergen Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": ('<div style=\"font-family:Segoe UI,sans-serif;font-size:22px;line-height:1.8\">{{cloze:Text}}</div>'),
        "afmt": ('<div style=\"font-family:Segoe UI,sans-serif;font-size:22px;line-height:1.8\">{{cloze:Text}}'
                 '<br><div style=\"color:#22d3ee;font-size:15px;margin-top:10px\">{{Extra}}</div></div>'),
    }],
    css=".card{background:#150a26;color:#f3e8ff}",
)

deck = genanki.Deck(DECK_ID, "ChineseB::代际冲突 Intergenerational Conflict")

QA = [
    ("《家》的作者和发表时间？", "巴金，《激流三部曲》第一部，1931年。"),
    ("《背影》的作者和体裁？", "朱自清，1925年回忆性散文。"),
    ("《目送》的作者和出版时间？", "龙应台，2008年散文集（约73篇）。"),
    ("《家》中与祖父高老太爷正面冲突、最后离家出走的孙子是谁？", "觉慧（老三）——五四新青年，封建家庭的叛逆者。"),
    ("《家》中「长房长孙」、在旧礼教前处处妥协的是谁？", "觉新（老大）——被迫放弃梅表姐，妻子瑞珏难产而死。"),
    ("《家》中觉慧爱上的丫鬟，被许给冯乐山做姨太太前投湖自尽？", "鸣凤。"),
    ("《家》的结局是什么？", "觉慧离家出走——新青年与封建家庭彻底决裂。"),
    ("《背影》的故事发生在哪里？", "浦口火车站，父亲送儿子北上读书。"),
    ("《背影》中父亲为儿子做了什么？", "穿过铁道、爬上月台去买橘子。"),
    ("《背影》中「我」最初对父亲的照顾是什么态度？", "暗笑他「迂」，觉得不必如此——年轻人的暗中评判。"),
    ("《背影》中「背影」象征什么？", "父亲衰老而沉默的爱；儿子多年后泪光中的理解与和解。"),
    ("《背影》结尾父亲的信里说了什么？", "「大约大去之期不远矣」——父亲预感时日无多。"),
    ("《目送》的两条主线是什么？", "目送儿子安德烈长大远去；目送父亲衰老离世。"),
    ("「他用背影默默告诉你：不必追」是什么意思？", "父母要学会放手，接受孩子渐行渐远是亲情的常态。"),
    ("三部作品各自的代际冲突结局？", "家=反抗（离家出走）；背影=和解（泪光中认出）；目送=放手（不必追）。"),
    ("三部作品的共同主题是什么？", "代际冲突：新旧观念的碰撞与亲情的复杂。"),
    ("「我是青年，我不是畸人，我不是愚人，我要给自己把幸福争过来。」出自哪里？", "《家》中觉慧的话——青年要自己争取幸福，而非服从礼教。"),
    ("「我慢慢地、慢慢地了解到，所谓父女母子一场……不断地在目送他的背影渐行渐远。」出自哪里？", "《目送》龙应台——亲情的本质是不断的目送与放手。"),
]

for f, b in QA:
    deck.add_note(genanki.Note(model=model, fields=[f, b], tags=["chinese", "intergenerational", "代际冲突"]))

CLOZE = [
    ("{{c1::觉慧}}说：「我是青年，我不是畸人，我不是愚人，我要给自己把幸福争过来。」——作品《{{c2::家}}》",
     "《家》巴金——青年对封建礼教的宣言。"),
    ("他用背影默默告诉你：{{c1::不必追}}。——《{{c2::目送}}》",
     "龙应台——父母要学会放手。"),
    ("我慢慢地、慢慢地了解到，所谓父女母子一场，只不过意味着，你和他的缘分就是今生今世不断地在目送他的背影{{c1::渐行渐远}}。——《目送》",
     "龙应台《目送》——亲情的常态是离别。"),
]

for text, extra in CLOZE:
    deck.add_note(genanki.Note(model=cloze_model, fields=[text, extra], tags=["chinese", "quote"]))

out = TOPIC / "Chinese_Intergenerational_Conflict.apkg"
genanki.Package(deck).write_to_file(str(out))
print("deck written:", out, out.stat().st_size, "bytes,", len(QA) + len(CLOZE), "notes")
