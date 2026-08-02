# Trading Ideas - Market Meeting Prep
**Monday, August 3, 2026 | Asia Macro Strategy Desk**

This is a cleaned-up presentation draft based on the two ideas in the initial note. It is written for discussion, not as investment advice. All strikes, spot levels, deltas, and option premiums should be recalibrated with live prices on Monday morning.

---

## Executive View

The two original ideas are usable, but they should be framed more tightly.

| Idea | Quality | Main Fix |
|---|---:|---|
| Long copper/aluminium producers, hedge Fed hike risk | Good strategic idea | Keep the structural AI/grid demand story, but do not overstate SOFR as a perfect hedge. The cleaner hedge for a presentation is a direct equity put spread; SOFR is a separate rate-risk overlay. |
| KOSPI put butterfly, then switch into call spreads | Good tactical idea, but more conditional | It works only if we expect a controlled drawdown toward a target, not a disorderly crash. Present it as a "buy-the-dip with defined risk" structure, not as a generic hedge. |

My view: Trade 1 is the better medium-term idea. Trade 2 is more elegant but more path-dependent. The cleanest weekend-news trade is actually a Brent/Dubai crude call spread, because it expresses the Hormuz shock directly.

---

## Weekend News Linkage

| Weekend / Recent News | Market Read-Through | Trade Link |
|---|---|---|
| Hormuz and Middle East shipping risk remains the dominant weekend tail risk. EIA data show Hormuz is a critical route for roughly one-fifth of global petroleum liquids consumption and about one-fifth of global LNG trade. | Higher oil/LNG, higher inflation risk, pressure on Asian energy importers, higher shipping and insurance costs. | Supports energy upside trades; creates downside risk for KOSPI and KRW; supports aluminium if supply/power costs tighten smelting capacity. |
| AI capex remains the positive growth impulse. Local news data flags Big Tech AI infrastructure commitments, while Korea customs data showed July 1-20 exports up sharply on semiconductor strength. | Positive for copper, power grid equipment, data-center supply chains, Samsung/SK Hynix, and Korea export momentum. | Supports long copper/aluminium producers and the eventual KOSPI call-spread switch. |
| Fed hike risk has re-priced higher into September. Rate-monitor data showed the market pricing a meaningful probability of a September hike. | Higher yields and stronger real-rate pressure can compress equity multiples and weigh on cyclical commodity producers. | Explains why the metals equity trade needs downside protection or a rates overlay. |
| Korea is exposed to both sides of the shock: chip exports are strong, but energy import costs are rising and crude sourcing is shifting away from the Middle East. | KOSPI can rally on AI demand, but oil/Hormuz shocks can hit margins, CPI, KRW, and discount rates. | Favors options over outright direction in KOSPI. |

---

## Assessment of the Two Original Ideas

### 1. Long copper/aluminium producers with Fed-risk hedge

This is a good idea because the fundamental story is coherent:

1. AI data centers and grid expansion are physical-capex stories, not just software stories. Copper wiring, transformers, transmission, cooling infrastructure, and power connections are all bottlenecks.
2. Aluminium has a clearer near-term supply angle than copper. Smelting is power-intensive, and energy disruption can tighten supply even if broader risk sentiment is weaker.
3. Producer equities give operational leverage to commodity prices.

The weakness is hedge design. A Fed hike does not hit the basket through rates alone. It can also hit through USD strength, China/Asia growth sentiment, equity risk premia, and commodity price weakness. SOFR futures hedge the policy-rate channel but not the full equity drawdown.

Conclusion: keep the trade, but present the put spread as the primary hedge and SOFR as an optional macro overlay.

### 2. KOSPI put butterfly, then call spread

This is a good idea only if the expected path is:

1. KOSPI drifts or sells down toward a defined target.
2. Implied volatility falls after the event risk passes.
3. The AI/export thesis remains intact.
4. The market does not gap far through the lower wing.

The problem is that weekend geopolitical news is binary. If Hormuz escalates, KOSPI may gap lower and stay volatile. A put butterfly is not ideal for that scenario because it has a narrow profit zone. If the view is "large downside shock," a simple put spread is cleaner. If the view is "temporary selloff then AI-led rebound," the butterfly-to-call-spread sequence makes sense.

Conclusion: present it as a conditional buy-the-dip plan, not a standalone bearish trade.

---

## Polished Trade 1 - Long Copper/Aluminium Producers With Defined Downside

### Thesis

Go long a basket of Asian copper and aluminium producers to capture the AI infrastructure, grid expansion, and electrification cycle. Hedge the equity drawdown risk because the same weekend news that supports metals supply tightness also raises oil, inflation, and Fed-hike risk.

### Why Now

- AI capex creates incremental demand for power infrastructure.
- Korea chip/export strength confirms that the AI hardware cycle is still alive in Asia.
- Aluminium is tighter than spot prices imply because Gulf supply normalization is incomplete and smelter restarts are slow.
- Fed and oil risks argue for defined downside instead of outright unhedged beta.

### Basket

Preferred basket if global markets are allowed:

| Weight | Name | Ticker | Role in Basket |
|---:|---|---|---|
| 30% | Zijin Mining | 2899.HK | Core Asia-listed copper miner; gold exposure adds some geopolitical hedge characteristics. |
| 25% | Hindalco | HINDALCO.NS | Aluminium plus copper exposure; India demand angle and less direct China property-cycle beta. |
| 20% | Rio Tinto | RIO.AX / RIO.L | Global quality anchor with copper/aluminium exposure, strong liquidity, and better balance-sheet defensiveness. |
| 15% | China Hongqiao | 1378.HK | Pure aluminium beta; best expression of energy/smelter supply tightness. |
| 10% | CMOC | 3993.HK | Higher-beta copper/cobalt growth exposure; useful electrification/AI infrastructure link, but higher jurisdiction risk. |

This is better than the first draft because it reduces reliance on Jiangxi Copper and adds higher-quality global miners. The basket still prioritizes Asian trading hours through Hong Kong, India, and Australia, but it avoids making the whole idea a China smelting/property-cycle trade. Five names is enough: Zijin and Rio anchor copper quality, Hindalco and Hongqiao carry aluminium/energy sensitivity, and CMOC adds higher-beta electrification exposure.

Pure Asia fallback basket:

| Weight | Name | Ticker |
|---:|---|---|
| 35% | Zijin Mining | 2899.HK |
| 25% | Hindalco | HINDALCO.NS |
| 20% | China Hongqiao | 1378.HK |
| 15% | CMOC | 3993.HK |
| 5% | Jiangxi Copper | 0358.HK |

If single-name option liquidity is poor, hedge using the most liquid listed proxy available to the desk: Rio Tinto options, a global miners ETF, relevant HK index options, or US-listed copper/miner exposure during US hours.

### Preferred Hedge

Use a 1-2 month put spread on the basket or on the most liquid proxy.

Illustrative structure:

| Leg | Strike | Position |
|---|---:|---:|
| Put | 95% of spot | Buy 1 |
| Put | 88% of spot | Sell 1 |

Why this is the cleaner hedge:

- It directly hedges the equity drawdown, regardless of whether the trigger is Fed, oil, China, USD, or broader risk-off.
- Cost is known upfront.
- It is easier to explain than a cross-asset SOFR hedge ratio.
- It keeps upside exposure if metals producers rally.

### Optional Fed Overlay

If the desk wants to hedge only the rate-hike surprise, short 3-month SOFR futures expiring after the relevant FOMC meeting. SOFR futures prices fall when the implied policy path rises, so a short futures position benefits from a hawkish repricing.

Rule of thumb: one SR3 contract is roughly USD 25 per bp. A 25 bp repricing is about USD 625 per contract. Use this only as a macro overlay, not as the main hedge for metals equities.

### Trade Management

- Take profit if the basket outperforms base metals by 8-12% or if aluminium supply risk is fully repriced.
- Cut or reduce if copper breaks lower on China demand weakness and aluminium does not offset.
- Remove the hedge if oil/geopolitical risk de-escalates and Fed-hike odds fall materially.
- Do not run the basket unhedged into a major Fed/inflation event.

### Key Risks

- AI capex disappointment or delayed data-center buildout.
- China demand weakness overwhelms the supply story.
- USD rally and higher real yields compress commodity equities.
- Single-name risk: operational issues, regulation, tariffs, or liquidity.

---

## Polished Trade 2 - KOSPI Put Butterfly, Then Bull Call Spread

### Thesis

Use options to express a two-stage Korea view:

1. Near term: KOSPI is vulnerable to energy-import pressure, Fed-rate volatility, and geopolitical risk.
2. Medium term: if the selloff is controlled, Korea remains a core AI/export beneficiary through semiconductors.

This is not a simple bearish idea. It is a structured entry plan for buying Korea after risk premium is priced in.

### Stage 1: Put Butterfly

Use a 4-6 week put butterfly centered on the desired entry level.

Illustrative strike map using spot = S:

| Leg | Strike Guide | Position |
|---|---:|---:|
| Put | 98% of S | Buy 1 |
| Put | 94% of S | Sell 2 |
| Put | 90% of S | Buy 1 |

The 94% strike is the important level. It should be where valuation and positioning make KOSPI attractive again.

Why this works:

- The structure has defined risk.
- Selling two middle-strike puts helps monetize elevated implied volatility.
- It profits most if KOSPI lands near the target instead of crashing.
- The lower wing protects against a deeper tail event.

### Stage 2: Switch Into Bull Call Spread

Only switch after the selloff looks like risk-premium repricing, not a broken macro regime.

Trigger checklist:

- KOSPI trades near the butterfly body strike.
- Oil stops rising or Hormuz/shipping headlines de-escalate.
- VKOSPI or local equity IV starts to fall.
- Korea semiconductor/export data remains strong.
- KRW is stable enough that FX stress is not driving foreign outflows.

Illustrative call spread after the switch:

| Leg | Strike Guide | Position |
|---|---:|---:|
| Call | At or slightly above spot | Buy 1 |
| Call | 5-7% above spot | Sell 1 |

Fund part of the call-spread debit with gains from the put butterfly if the first stage works.

### When Not To Switch

Do not switch into calls if:

- Brent gaps above USD 110-120 with no shipping de-escalation.
- Hormuz disruption becomes a real physical blockade.
- BOK rhetoric turns clearly hawkish because energy inflation is feeding CPI.
- KOSPI breaks the lower butterfly wing on heavy foreign selling.

### Key Risks

- KOSPI rallies immediately on AI optimism and the butterfly expires worthless.
- KOSPI gaps below the lower wing, making the butterfly the wrong bearish structure.
- IV remains high even at the target level, reducing mark-to-market gains.
- The second-stage call spread is entered too early, before oil/FX stress stabilizes.

---

## Better / Cleaner Weekend-News Ideas

### Alternative 1 - Long Brent or Dubai Crude Call Spread

This is the cleanest expression of the weekend news.

Structure: buy a 1-3 week crude call spread, for example 5% OTM vs 12-15% OTM.

Rationale:

- Direct exposure to Hormuz, tanker, LNG, and Middle East escalation headlines.
- Defined premium at risk.
- Avoids the second-order problem of choosing which Asian equity market absorbs the shock.
- Easy to present: if shipping risk escalates, crude risk premium rises; if diplomacy improves, premium is lost.

Best expression depends on desk access:

- Brent options for global oil risk.
- Dubai/Oman-related exposure if the desk wants a more Asia-specific crude benchmark.
- Energy equities only if options on crude are unavailable.

Main risk: a ceasefire, SPR release, or OPEC+ supply response caps the oil spike.

### Alternative 2 - Buy USD/KRW Call Spread

This is a cleaner Asia macro hedge than shorting KOSPI outright.

Structure: buy a 1-month USD/KRW call spread.

Rationale:

- Korea benefits from AI exports, but KRW is vulnerable if energy import costs rise and foreign investors reduce KOSPI exposure.
- The trade captures the negative side of the Hormuz shock without fully fighting the positive semiconductor story.
- A call spread keeps risk defined and avoids paying unlimited upside vol.

Trigger:

- Enter if oil gaps higher on Monday or if KOSPI opens weak with foreign outflows.
- Reduce if Korea chip names lead a strong rebound and oil fades.

Main risk: official FX smoothing, strong Korea export data, or broad USD weakness.

---

## Recommended Presentation Flow

1. Start with the regime: AI growth impulse vs. energy/Fed shock.
2. Present Trade 1 as the higher-conviction structural idea: long metals producers, protected with a put spread.
3. Present Trade 2 as a tactical Korea options plan: get paid if KOSPI sells to our entry zone, then switch bullish only after stress stabilizes.
4. Add the two cleaner alternatives as backup ideas: crude call spread and USD/KRW call spread.
5. End with risk controls: do not confuse a temporary geopolitical selloff with a full macro regime break.

---

## Sources Checked

- Local weekend news feed: `data/news_data.json`
- Local generated news summary: `data/ai_summary.md`
- EIA, Strait of Hormuz oil and LNG chokepoint data: https://www.eia.gov/todayinenergy/detail.php?id=65504
- KBS World, July 1-20 Korea export data: https://world.kbs.co.kr/service/news_view.htm?Seq_Code=203021&lang=e
- Westpac July 2026 commodities update: https://www.westpaciq.com.au/economics/2026/07/commodities-update-july-2026
- Asia Business Daily, Korea crude import diversification: https://view.asiae.co.kr/en/article/2026052615462158938
- Times of India, IOC spot crude purchases after Middle East disruption: https://timesofindia.indiatimes.com/business/india-business/indian-oil-ramps-up-spot-crude-purchases-as-middle-east-disruptions-hit-supplies/articleshow/132786908.cms
- Investing.com Fed rate monitor, September 16, 2026 meeting pricing: https://www.investing.com/central-banks/fed-rate-monitor
