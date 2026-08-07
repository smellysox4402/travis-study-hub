#!/usr/bin/env python3
"""Build Unit 3 Finance & Accounts cloze deck (50 cards) for the Business HL deck.
Matches the user's existing 'Cloze+' note model (Text + Back Extra) so cards
merge cleanly into Anki and anki-arena can read them.
Usage: python build_biz_finance_anki.py -> writes Finance_Accounts.apkg
"""
import genanki, os, shutil

MODEL_ID = 1607392321   # Business HL copy of Cloze+ (distinct per subject)
DECK_ID  = 2059400114   # Business HL deck

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "topics", "business", "finance-accounts", "Finance_Accounts.apkg"))
SYNC = os.path.normpath(os.path.join(HERE, "..", "business_hl", "Finance_Accounts.apkg"))

model = genanki.Model(
    MODEL_ID,
    "Cloze+",
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<br><div style="color:#a855f7;font-style:italic">{{Back Extra}}</div>',
    }],
    model_type=1,  # cloze (genanki.CLOZE constant absent in this version)
)

CARDS = [
# --- 3.1 introduction to finance ---
("The {{c1::role of finance}} in a business is to provide the money needed to {{c2::start}} the business, to {{c3::expand}} it, and to {{c4::keep it trading}} day to day.",
 "Money for: start, grow, keep the lights on. 🤑 (3.1.1)"),
("{{c1::Capital expenditure}} is money spent on {{c2::fixed assets}} that last longer than one year (sound system, lighting rig, furniture). It appears on the {{c3::balance sheet}} and is spread over its life as {{c4::depreciation}}.",
 "Buying the assets 🎛 (3.1.2)"),
("{{c1::Revenue expenditure}} is spending on the {{c2::day-to-day operations}} — wages, drinks stock, rent, utilities. It appears in the {{c3::profit and loss account}} and is deducted from revenue in the same period.",
 "Paying to run the night 🌙 (3.1.3)"),
# --- 3.2 sources of finance ---
("Internal sources of finance: {{c1::personal funds}} (sole trader's own savings), {{c2::retained profit}} (profits kept in the business, not paid as dividends), and {{c3::sale of assets}} (selling unused or obsolete assets).",
 "🏠 from inside the club. (3.2.1)"),
("{{c1::Retained profit}} is the cheapest source of finance: no interest and no new shares — but it only exists if the business has actually {{c2::made a profit}}.",
 "📦 profits kept in, not paid out. (3.2.1)"),
("{{c1::Share capital}} = investors buy shares (part-ownership). No repayment, dividends only if profits allow — but {{c2::only limited companies}} can use it, and new shares {{c3::dilute}} the founders' control.",
 "📈 selling a slice of the club. (3.2.2)"),
("{{c1::Loan capital}} = borrowing from a bank, repaid with {{c2::interest}} over a fixed term. Certain and planned — but interest must be paid {{c3::regardless of profit}}, which raises {{c4::gearing}}.",
 "🏦 borrowed money, interest always due. (3.2.2)"),
("An {{c1::overdraft}} lets a business borrow up to a limit, paying interest only on what is used. Flexible for {{c2::short-term}} cash gaps — but high interest and repayable {{c3::on demand}}.",
 "💳 the flexible credit card. (3.2.2)"),
("{{c1::Trade credit}} = suppliers deliver now and the business pays in 30–60 days. It is {{c2::free}} short-term finance — but late payment damages goodwill and may cost discounts.",
 "📄 pay later, keep the cash. (3.2.2)"),
("{{c1::Crowdfunding}} = raising small amounts from {{c2::many people}} online, often with pre-sold perks (early tickets, merch). Great for a launch — but public, and rewards must be delivered.",
 "📣 many small investors. (3.2.2)"),
("{{c1::Leasing}} = renting equipment instead of buying it. Preserves cash and gives flexibility — but costs more overall and the asset is {{c2::never owned}}.",
 "🔑 rent the gear, never own it. (3.2.2)"),
("{{c1::Microfinance providers}} make small, {{c2::short-term}} loans to entrepreneurs who cannot access bank credit — vital for start-ups in developing economies.",
 "🌱 tiny loans, big doors. (3.2.2)"),
("{{c1::Business angels}} are wealthy individuals who invest their own money in early-stage ventures, often mentoring too. They take {{c2::equity}} — sharing control and expecting a big return.",
 "🦅 rich mentor with a stake. (3.2.2)"),
("To judge the appropriateness of a source of finance ask: how {{c1::long}} is the money needed (short vs long-term), what is it {{c2::for}} (asset vs operations), and what can the business {{c3::afford}} (interest vs equity)?",
 "MATCH the source to the use 🎯 (3.2.3)"),
# --- 3.3 costs and revenues ---
("{{c1::Fixed costs}} stay the same however many customers come (rent, salaries of permanent staff, insurance); {{c2::variable costs}} change directly with output (drinks stock, casual bar staff).",
 "Rent never panics; drinks stock does. 🧾 (3.3.1/2)"),
("{{c1::Direct costs}} are traceable to a specific product or service (the cost of the drinks sold, a DJ's fee for one event); {{c2::indirect costs}} (overheads) are shared across the whole business (rent, utilities, admin).",
 "Direct = traceable, indirect = shared. 🧾 (3.3.3/4)"),
("A cost can be both at once: rent is {{c1::fixed AND indirect}}; drinks stock is {{c2::variable AND direct}}.",
 "The pairs are not mutually exclusive. 🧾 (3.3.1–4)"),
("Total revenue = {{c1::price × quantity sold}}. Revenue {{c2::streams}} = the different sources of income a business earns from (tickets, bar sales, VIP booths, merch, sponsorship).",
 "One main product vs many income doors. 🎟 (3.3.5)"),
# --- 3.4 final accounts ---
("Different stakeholders read the accounts differently: {{c1::owners}} want profitability/ROCE/dividends, {{c2::banks}} want liquidity and gearing (can it repay?), {{c3::suppliers}} want to know they'll be paid, {{c4::employees}} want job security, the {{c5::tax authority}} wants accurate profit.",
 "Everyone reads the same film differently. 📊 (3.4.1)"),
("The statement of profit or loss (P&L) order: {{c1::sales revenue}} → minus {{c2::cost of sales}} = {{c3::gross profit}} → minus {{c4::expenses}} = {{c5::profit before interest and tax (PBIT)}} → minus {{c6::finance costs}} = profit before tax → minus {{c7::tax}} = profit after tax → minus {{c8::dividends}} = {{c9::retained profit}}.",
 "The P&L waterfall 🎛 (3.4.2)"),
("{{c1::Gross profit}} = sales revenue − cost of sales. {{c2::Profit before interest and tax (PBIT)}} = gross profit − expenses — the profit from pure trading.",
 "The two numbers the exam builds on. 💰 (3.4.2)"),
("The balance sheet (statement of financial position) equation: {{c1::ASSETS = EQUITY + LIABILITIES}}. It is a {{c2::snapshot at one date}}, unlike the P&L which is a flow over the year.",
 "The seesaw must balance ⚖ (3.4.3)"),
("{{c1::Working capital}} = current assets − current liabilities — found buried inside the balance sheet.",
 "57 − 42 = 15. 💧 (3.4.3)"),
("Intangible assets are {{c1::non-physical}} assets with value: {{c2::goodwill}} (reputation, loyal crowd), {{c3::patents}} (exclusive right to an invention), {{c4::copyright}}, and {{c5::trademarks}} (the brand).",
 "👻 money you can't touch. (3.4.4)"),
("Depreciation spreads the {{c1::cost of a fixed asset}} over its {{c2::useful life}}, matching cost to the years that benefit. It is a {{c3::non-cash expense}} — no money leaves the business.",
 "⏳ assets wear out. (3.4.5)"),
("Straight-line depreciation = {{c1::(cost − residual value) ÷ useful life}}. Example: $120,000 system, $20,000 resale, 4 years → {{c2::$25,000}} every year.",
 "Same charge, every year. 📏 (3.4.5 HL)"),
("Units-of-production depreciation = {{c1::(cost − residual) × units made ÷ total expected units}}. Example: $50,000 lighting, $10,000 resale, 100,000 hours life, 12,000 hours used → {{c2::$4,800}} this year.",
 "Charge matches actual use. ⚙ (3.4.6 HL)"),
("Choose straight-line when the asset wears out {{c1::evenly over time}} (furniture, lighting rigs); choose units of production when wear depends on {{c2::use, not time}} (machinery, vehicles) — the method must reflect how the asset actually wears out.",
 "Match the method to the wear. 🎯 (3.4.7 HL)"),
# --- 3.5 profitability and liquidity ratios ---
("Gross profit margin = {{c1::gross profit ÷ sales × 100}}. Neon Pulse: 600 ÷ 1,000 = {{c2::60%}}.",
 "How much survives the cost of what was sold. 📈 (3.5.1)"),
("Profit margin (net) = {{c1::profit before interest and tax ÷ sales × 100}}. Neon Pulse: 400 ÷ 1,000 = {{c2::40%}}. (New syllabus uses PBIT, not profit after tax.)",
 "What's left after ALL operating costs. 📈 (3.5.2)"),
("ROCE = {{c1::profit before interest and tax ÷ capital employed × 100}}, where capital employed = {{c2::non-current liabilities + equity}}. Neon Pulse: 400 ÷ 495 ≈ {{c3::81%}}.",
 "The big one: return on all the money tied up. 🏆 (3.5.3)"),
("Strategies to improve profitability: {{c1::raise prices}}, {{c2::cut cost of sales}} (cheaper suppliers, bulk buying), {{c3::cut overheads}}, sell higher-margin items (VIP booths), and improve {{c4::productivity}}.",
 "Price up, costs down, sell smarter. 📈 (3.5.4)"),
("Current ratio = {{c1::current assets ÷ current liabilities}}. Neon Pulse: 57 ÷ 42 = {{c2::1.36:1}}. Roughly {{c3::2:1}} is comfortable; below {{c4::1:1}} is danger.",
 "Can the club pay tonight's bills? 💧 (3.5.5)"),
("Acid test = {{c1::(current assets − stock) ÷ current liabilities}}. Neon Pulse: (57 − 35) ÷ 42 = {{c2::0.52:1}} — below 1:1 = danger, because {{c3::stock can't be turned into cash instantly}}.",
 "The harsher test — stock excluded. 🥶 (3.5.6)"),
("Strategies to improve liquidity: {{c1::reduce stock levels}}, {{c2::chase debtors harder}} (cash discounts), {{c3::negotiate longer trade credit}}, {{c4::sell unused assets}}, or use a short-term {{c5::overdraft}}.",
 "Free up cash, fast. 💧 (3.5.7)"),
# --- 3.6 efficiency ratios (HL) ---
("Stock turnover = {{c1::cost of sales ÷ average stock}} (×365 → days held). Neon Pulse: 400 ÷ 35 ≈ {{c2::11.4 times}} a year (~32 days). Perishable goods need {{c3::high}} turnover; luxury goods tolerate low.",
 "How fast stock sells. 🍺 (3.6.1 HL)"),
("Debtor days = {{c1::debtors ÷ sales × 365}}. Neon Pulse: 12 ÷ 1,000 × 365 ≈ {{c2::4.4 days}}. Lower = better — a cash business like a club scores brilliantly.",
 "How long customers take to pay. 💳 (3.6.2 HL)"),
("Creditor days = {{c1::creditors ÷ cost of sales × 365}}. Neon Pulse: 15 ÷ 400 × 365 ≈ {{c2::13.7 days}}. Longer = cash stays in the business longer. Ideally {{c3::debtor days < creditor days}}.",
 "How long until suppliers get paid. 📄 (3.6.3 HL)"),
("Gearing = {{c1::non-current liabilities ÷ capital employed × 100}}. Neon Pulse: 300 ÷ 495 ≈ {{c2::61%}}. Above {{c3::50%}} = highly geared = risky, because {{c4::loans must be repaid regardless of profit}}.",
 "How much is borrowed money. 🎢 (3.6.4 HL)"),
("Strategies to improve efficiency: stock → {{c1::JIT ordering}} / clear obsolete stock; debtors → {{c2::tighter credit control}}; creditors → {{c3::longer payment terms}}; gearing → {{c4::repay loans}} or fund growth with retained profit/equity instead.",
 "Tune the machine. ⚙ (3.6.5 HL)"),
("{{c1::Insolvency}} is a financial state — a business {{c2::cannot pay its debts as they fall due}}, but it can be temporary. {{c3::Bankruptcy}} is a {{c4::legal process}} declaring an individual or sole trader unable to pay; for companies the legal process is {{c5::liquidation}}.",
 "Insolvency = the condition, bankruptcy = the court case. ⚖ (3.6.6 HL)"),
# --- 3.7 cash flow ---
("Profit is booked {{c1::when the sale happens}} (accrual accounting); cash arrives {{c2::when the money lands}} — often weeks later on credit sales. So a business can be {{c3::profitable with negative cash flow}}.",
 "Profit is an opinion, cash is a fact. 👑 (3.7.1)"),
("Net cash flow = {{c1::cash inflows − cash outflows}}. A business can be loss-making with positive cash flow (e.g. customers paying upfront) and {{c2::profitable but bankrupt}} if cash is tied up in stock and unpaid credit.",
 "A profitable business CAN run out of cash. 👑 (3.7.1)"),
("The working capital cycle: {{c1::CASH → STOCK → SALE ON CREDIT → DEBTORS → CASH}}. The time cash is tied up in stock and credit is the {{c2::time lag}} — the shorter the loop, the healthier the business.",
 "Cash → stock → sale → debtors → cash 🔄 (3.7.2)"),
("{{c1::Liquidity}} = how easily the business can turn assets into cash to meet short-term bills. Working capital = {{c2::current assets − current liabilities}}.",
 "💧 (3.7.2/3)"),
("Cash flow forecast mechanics: {{c1::opening balance}} + total inflows − total outflows = {{c2::closing balance}}, which becomes {{c3::next month's opening balance}}. A negative closing balance = danger to fix.",
 "O + in − out = C. 📉 (3.7.4)"),
("Investment creates an {{c1::immediate cash outflow}} but is expected to generate {{c2::profit over several future years}} — so in the short term cash suffers; if the investment works, profit AND cash improve long-term.",
 "Short-term pain, long-term gain. 🚧 (3.7.5)"),
("Strategies for cash flow problems — cut outflows ({{c1::longer trade credit}}, {{c2::lease instead of buy}}, {{c3::less stock}}), boost inflows ({{c4::marketing}}, cash discounts, price tweaks), or bridge with {{c5::overdraft / short-term loan / sale of assets}}.",
 "Cut, boost, or bridge. 🩹 (3.7.6)"),
# --- 3.8 investment appraisal ---
("Payback period = the time to recover the initial cost. Uneven flows: count whole years, then add the fraction. $60k cost, flows 20/18/16/14/12 → after 3 years 54k, 6k left ÷ 14 = 0.43 → {{c1::3.43 years}}. Accept if within the firm's {{c2::target time}}.",
 "⏱ how long to get the money back. (3.8.1)"),
("Payback ignores {{c1::cash after the payback date}} and ignores {{c2::profitability}} entirely — it's a liquidity tool, not a profit tool.",
 "⏱ the shallow-but-fast tool. (3.8.1)"),
("Average rate of return = {{c1::(average annual profit ÷ initial cost) × 100}}. $60k cost, total cash 80k → total profit 20k → avg 4k/yr → ARR = 4 ÷ 60 = {{c2::6.67%}}. Accept if {{c3::above the target rate}}.",
 "📊 profit as a % of cost. (3.8.2)"),
("NPV = {{c1::Σ(present values of future cash flows) − initial cost}}, where each flow is multiplied by a {{c2::discount factor}} (given in the exam). Positive NPV = {{c3::accept}} — the project earns more than the cost of capital.",
 "Future cash, priced in today's money. 💸 (3.8.3 HL)"),
("NPV example at 10%: 20k×0.9091 + 18k×0.8264 + 16k×0.7513 + 14k×0.6830 + 12k×0.6209 = 62,091 − 60,000 = {{c1::+2,091}} → {{c2::ACCEPT}}.",
 "Positive NPV wins. ✅ (3.8.3 HL)"),
# --- 3.9 budgets (HL) ---
("A {{c1::cost centre}} is a department accountable only for its {{c2::own costs}} (marketing, HR, security); a {{c3::profit centre}} is accountable for {{c4::both costs and revenue}} — hence its own profit (each branch, the VIP room).",
 "Cost centres spend, profit centres earn. 📋 (3.9.1 HL)"),
("Roles of cost and profit centres: {{c1::monitoring and control}} of each unit, faster {{c2::decision-making}} by empowered managers, {{c3::motivation}} via responsibility, and {{c4::accountability}}.",
 "Measure, decide, motivate, own it. 📋 (3.9.2 HL)"),
("A variance is favourable when the outcome is {{c1::better than budget}}: revenue {{c2::higher}} than planned or costs {{c3::lower}} than planned. It is adverse when revenue is {{c4::lower}} or costs {{c5::higher}}.",
 "Sales up = F, costs up = A. 📋 (3.9.4 HL)"),
("Budgets matter because they enable {{c1::planning}}, {{c2::cash-flow forecasting}}, {{c3::prioritising}}, {{c4::control}}, target-setting/motivation, accountability, and benchmarking. Limitations: expensive to build, {{c5::inflexible}}, forecasts are guesses, and 'use it or lose it' causes wasteful spending.",
 "🎯 plan, control, benchmark — but they lie too. (3.9.5 HL)"),
]

deck = genanki.Deck(DECK_ID, "Business HL")
for text, back in CARDS:
    deck.add_note(genanki.Note(model=model, fields=[text, back]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
os.makedirs(os.path.dirname(SYNC), exist_ok=True)
genanki.Package(deck).write_to_file(OUT)
shutil.copy2(OUT, SYNC)
print(f"OK: {len(CARDS)} notes -> {os.path.normpath(OUT)}")
print(f"    synced -> {SYNC}")
