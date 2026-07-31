KANG-TRUTH-SENTINEL: 3da4ddcf-7fea-4794-8959-0ea12f456997

## Phase 1: Corpus Reconnaissance

### Objective

Establish the investable question, source hierarchy, reporting chronology, company and peer identities, measurement conventions, and the information set available as of the June 30, 2026 cutoff. Do not infer document contents from filenames; open and validate each candidate source before using it.

### Expected source files from the manifest

- Company and peer identification:
  - `company_profiles.json`
- Primary financial series:
  - `financials/income_statement/cmg_income_statement.json`
  - `financials/balance_sheet/cmg_balance_sheet.json`
  - `financials/cash_flow/cmg_cash_flow.json`
- Peer financial series:
  - `financials/income_statement/sg_income_statement.json`
  - `financials/income_statement/shak_income_statement.json`
  - `financials/income_statement/wing_income_statement.json`
  - `financials/cash_flow/sg_cash_flow.json`
  - `financials/cash_flow/shak_cash_flow.json`
  - `financials/cash_flow/wing_cash_flow.json`
- Current primary disclosures:
  - `sec_filings/10-k/cmg_2025_10-k.txt`
  - `sec_filings/10-q/cmg_2026q1_10-q.txt`
  - `press_releases/cmg_2026-02-03_8-k.txt`
  - `press_releases/cmg_2026-04-29_8-k.txt`
- Historical comparison sources:
  - `sec_filings/10-k/cmg_2023_10-k.txt`
  - `sec_filings/10-k/cmg_2024_10-k.txt`
  - `sec_filings/10-q/cmg_2024q2_10-q.txt`
  - `sec_filings/10-q/cmg_2024q3_10-q.txt`
  - `sec_filings/10-q/cmg_2025q1_10-q.txt`
  - `sec_filings/10-q/cmg_2025q2_10-q.txt`
  - `sec_filings/10-q/cmg_2025q3_10-q.txt`
- Other potentially relevant company communications:
  - `press_releases/cmg_2025-07-23_8-k.txt`
  - `press_releases/cmg_2025-09-15_8-k.txt`
  - `press_releases/cmg_2025-10-29_8-k.txt`
  - `press_releases/cmg_2025-12-08_8-k.txt`
  - `press_releases/cmg_2026-01-12_8-k.txt`
  - `press_releases/cmg_2026-04-27_8-k.txt`
- Long-term historical context, only if a current claim requires it:
  - `sec_filings/s-1/cmg_2005_s-1.txt`
  - `sec_filings/s-1/cmg_2006_s-1.txt`

### Observable trajectory signals

- Enumerate the corpus and confirm that every cited path exists.
- Read `company_profiles.json` to identify the primary company, peers, business descriptions, and any point-in-time limitations.
- Open each JSON file and record its schema, period labels, units, fiscal-period conventions, null handling, and whether values are quarterly, year-to-date, or annual.
- Open current filings and releases to verify filing periods, publication dates, and the nature of each document.
- Create a chronology that maps annual results, interim results, guidance, and later updates without using information after the cutoff.
- Establish a source hierarchy:
  1. Filed financial statements and detailed filing disclosures.
  2. Filed or furnished company communications.
  3. Structured financial files reconciled to the filings.
  4. Older filings for historical consistency.
- Record duplicated disclosures so the same underlying fact is not treated as independent corroboration.
- Maintain a source ledger with fields for file path, period, section or locator, metric definition, units, and intended analytical use.

## Phase 2: Question Decomposition

### Objective

Convert the broad durability question into testable sub-questions with explicit decision criteria. The analysis should determine whether traffic, restaurant economics, and returns on new-unit growth remain defensible as the unit base matures—not merely describe recent results.

### Expected source files from the manifest

- Core operating evidence:
  - `sec_filings/10-k/cmg_2025_10-k.txt`
  - `sec_filings/10-q/cmg_2026q1_10-q.txt`
  - `financials/income_statement/cmg_income_statement.json`
  - `financials/cash_flow/cmg_cash_flow.json`
- Current outlook and management framing:
  - `press_releases/cmg_2026-02-03_8-k.txt`
  - `press_releases/cmg_2026-04-29_8-k.txt`
- Historical baselines:
  - `sec_filings/10-k/cmg_2023_10-k.txt`
  - `sec_filings/10-k/cmg_2024_10-k.txt`
  - `sec_filings/10-q/cmg_2025q1_10-q.txt`
  - `sec_filings/10-q/cmg_2025q2_10-q.txt`
  - `sec_filings/10-q/cmg_2025q3_10-q.txt`
- Competitive comparison:
  - `company_profiles.json`
  - All four income-statement JSON files
  - All four cash-flow JSON files

### Observable trajectory signals

- Build a question matrix covering:
  - Whether comparable-sales changes are transaction-led, price-led, or mix-led.
  - Whether digital growth represents incremental demand, channel migration, check enhancement, or an unresolved combination.
  - Whether restaurant-level margins can withstand wage, food, freight, tariff, and volume pressures.
  - Whether overhead leverage can materially offset restaurant-level deleverage.
  - Whether new-unit growth is adding attractive capacity or diluting average unit volumes and fixed-cost leverage during ramp.
  - Whether capital requirements are rising faster than the economic contribution of new units.
  - Whether recent softness appears company-specific, industry-wide, or mixed.
  - Which competitive, consumer, brand, and food-safety risks could invalidate an apparent recovery.
- Define the evidence needed for both a durable and a non-durable conclusion before gathering facts.
- Specify the time horizons separately:
  - Near-term operating inflection.
  - Medium-term margin recovery.
  - Long-term unit economics and market runway.
- Define the final decision standard in advance: select a directional position and explain why the evidence on one side is more persistent, broad-based, or economically important than the evidence on the other.
- Create an ambiguity log for disclosures that do not cleanly separate menu price, mix, transactions, new-unit effects, or timing effects.

## Phase 3: Evidence Gathering

### Objective

Extract directly supportable operating, financial, strategic, and risk evidence. Capture definitions and periods alongside every fact so that annual, quarterly, comparable-store, and consolidated measures are not mixed improperly.

### Expected source files from the manifest

#### Comparable sales, transactions, check, price, mix, and digital

- `sec_filings/10-k/cmg_2025_10-k.txt`
- `sec_filings/10-q/cmg_2026q1_10-q.txt`
- `financials/income_statement/cmg_income_statement.json`
- `press_releases/cmg_2026-02-03_8-k.txt`
- `press_releases/cmg_2026-04-29_8-k.txt`
- Historical checks:
  - `sec_filings/10-k/cmg_2023_10-k.txt`
  - `sec_filings/10-k/cmg_2024_10-k.txt`
  - `sec_filings/10-q/cmg_2025q1_10-q.txt`
  - `sec_filings/10-q/cmg_2025q2_10-q.txt`
  - `sec_filings/10-q/cmg_2025q3_10-q.txt`

Search the opened documents for comparable restaurant sales, comparable restaurants, transactions, average check, menu pricing, product or channel mix, digital sales, rewards, delivery, and full-year outlook. Verify whether each metric is annual, quarterly, year-to-date, or point-in-time.

#### Restaurant-level margin and inflation exposure

- `sec_filings/10-k/cmg_2025_10-k.txt`
- `sec_filings/10-q/cmg_2026q1_10-q.txt`
- `financials/income_statement/cmg_income_statement.json`
- `press_releases/cmg_2026-02-03_8-k.txt`
- `press_releases/cmg_2026-04-29_8-k.txt`

Extract revenue and restaurant operating-cost components, including food and packaging, labor, occupancy, other restaurant operating costs, and any disclosed restaurant-level margin. Search for explanations involving wage inflation, commodity costs, beef, freight, tariffs, sales-volume leverage, efficiency initiatives, and menu-price offsets.

#### Unit growth, maturity, average unit volumes, and capital intensity

- `sec_filings/10-k/cmg_2025_10-k.txt`
- `sec_filings/10-q/cmg_2026q1_10-q.txt`
- `financials/cash_flow/cmg_cash_flow.json`
- `financials/balance_sheet/cmg_balance_sheet.json`
- `press_releases/cmg_2026-02-03_8-k.txt`
- `press_releases/cmg_2026-04-29_8-k.txt`

Extract beginning and ending restaurant counts, openings, closures, development guidance, format mix, long-term unit aspirations, new-unit ramp commentary, average restaurant sales, capital expenditures, and available funding. Distinguish actual openings from planned openings and company-owned units from any partner-operated units.

#### Competitive and demand risks

- Risk disclosures and current updates:
  - `sec_filings/10-k/cmg_2025_10-k.txt`
  - `sec_filings/10-q/cmg_2026q1_10-q.txt`
- Historical consistency:
  - `sec_filings/10-k/cmg_2023_10-k.txt`
  - `sec_filings/10-k/cmg_2024_10-k.txt`
- Peer identification and financial comparison:
  - `company_profiles.json`
  - `financials/income_statement/cmg_income_statement.json`
  - `financials/income_statement/sg_income_statement.json`
  - `financials/income_statement/shak_income_statement.json`
  - `financials/income_statement/wing_income_statement.json`
  - `financials/cash_flow/cmg_cash_flow.json`
  - `financials/cash_flow/sg_cash_flow.json`
  - `financials/cash_flow/shak_cash_flow.json`
  - `financials/cash_flow/wing_cash_flow.json`

Extract risks involving discretionary spending, restaurant and non-restaurant competition, discounting, brand reputation, food safety, labor availability, input costs, and execution. Read peer profiles before deciding whether a comparison is economically valid.

### Observable trajectory signals

- Use targeted searches followed by surrounding-section reads; do not rely on isolated search hits.
- Build a fact table with one row per disclosed metric and columns for:
  - Metric and definition.
  - Period and comparison period.
  - Reported value and units.
  - Source path and section locator.
  - Management’s stated driver.
  - Whether the item is actual, guidance, target, or risk estimate.
- Trace comparable sales into transactions and check, then investigate whether check is further separated into menu pricing and mix.
- Trace restaurant-level margin changes into individual cost lines and stated volume effects.
- Trace unit growth into opening format, maturation period, average unit sales, and capital spending rather than treating restaurant count as sufficient evidence.
- Gather at least one credible supporting and one credible adverse fact for each sub-question.
- Reconcile overlapping disclosures across filings, communications, and structured financial data; flag rather than conceal any difference in period, definition, or rounding.
- Attach an inline source path to every factual note intended for the final analysis.

## Phase 4: Counter-Evidence Engagement

### Objective

Actively test the provisional thesis against the strongest contrary interpretation. Determine whether favorable evidence is a genuine operating inflection or a temporary comparison, price effect, channel shift, cost timing benefit, or management forecast—and whether adverse evidence is cyclical, structural, or already improving.

### Expected source files from the manifest

- Current annual and quarterly disclosures:
  - `sec_filings/10-k/cmg_2025_10-k.txt`
  - `sec_filings/10-q/cmg_2026q1_10-q.txt`
- Earlier comparisons:
  - `sec_filings/10-k/cmg_2023_10-k.txt`
  - `sec_filings/10-k/cmg_2024_10-k.txt`
  - `sec_filings/10-q/cmg_2024q2_10-q.txt`
  - `sec_filings/10-q/cmg_2024q3_10-q.txt`
  - `sec_filings/10-q/cmg_2025q1_10-q.txt`
  - `sec_filings/10-q/cmg_2025q2_10-q.txt`
  - `sec_filings/10-q/cmg_2025q3_10-q.txt`
- Management updates through the cutoff:
  - All eight files in `press_releases/` listed in the manifest
- Primary and peer financial comparisons:
  - All four income-statement JSON files
  - All four cash-flow JSON files
  - `company_profiles.json`

### Observable trajectory signals

- Create a two-column challenge sheet pairing each provisional claim with the strongest corpus-supported objection.
- Test favorable traffic evidence by checking:
  - Transactions versus check.
  - Menu pricing versus mix.
  - One quarter versus the preceding annual and quarterly pattern.
  - Digital penetration versus evidence of total demand growth.
  - Actual results versus guidance.
- Test margin resilience by checking:
  - Restaurant-level costs separately from corporate overhead.
  - Percentage-of-revenue improvements against possible pricing or mix benefits.
  - Cost inflation against volume deleverage.
  - Temporary efficiencies against recurring input and labor exposure.
- Test unit-growth quality by checking:
  - Gross openings against closures and net additions.
  - New-unit ramp time against average-unit-volume movement.
  - Format mix against demonstrated economics.
  - Capital expenditure growth against unit growth and cash generation.
- Test the competitive interpretation using consistent peer periods and definitions. If peer reporting models differ materially, narrow the comparison to revenue growth, operating margin, and cash investment measures that are genuinely comparable.
- Read the current risk disclosures in context and distinguish generic recurring language from risks tied directly to traffic, pricing, costs, or expansion.
- Maintain a contradiction log showing:
  - The conflicting observations.
  - Whether the conflict reflects period, scope, definition, or genuine economic tension.
  - Which interpretation is better supported and why.
  - What remains unresolved.
- Reject any provisional conclusion that can only survive by omitting the strongest adverse evidence.

## Phase 5: Quantitative Anchoring

### Objective

Turn the extracted evidence into auditable comparisons and bridges. Keep company-reported values separate from analyst-derived values, show formulas for all derivations, and avoid false precision when source disclosures are rounded or definitionally incomplete.

### Expected source files from the manifest

- Primary calculations:
  - `financials/income_statement/cmg_income_statement.json`
  - `financials/cash_flow/cmg_cash_flow.json`
  - `financials/balance_sheet/cmg_balance_sheet.json`
  - `sec_filings/10-k/cmg_2025_10-k.txt`
  - `sec_filings/10-q/cmg_2026q1_10-q.txt`
- Peer calculations:
  - `financials/income_statement/sg_income_statement.json`
  - `financials/income_statement/shak_income_statement.json`
  - `financials/income_statement/wing_income_statement.json`
  - `financials/cash_flow/sg_cash_flow.json`
  - `financials/cash_flow/shak_cash_flow.json`
  - `financials/cash_flow/wing_cash_flow.json`
- Guidance and outlook verification:
  - `press_releases/cmg_2026-02-03_8-k.txt`
  - `press_releases/cmg_2026-04-29_8-k.txt`

### Reported versus derived treatment

- Label as **reported**:
  - Values directly disclosed in a filing, communication, or structured financial file.
  - Management guidance, targets, estimates, or qualitative causal explanations.
  - Disclosed comparable sales, transactions, average check, cost ratios, restaurant counts, average restaurant sales, digital share, and capital expenditures.
- Label as **derived**:
  - Year-over-year growth rates calculated from reported values.
  - Percentage-point or basis-point changes.
  - Cost and margin bridges assembled from individual lines.
  - Ratios such as capital expenditures to sales, capital expenditures per net opening, or cash investment growth.
  - Peer spreads and indexed comparisons.
- Never present a derived figure as company guidance or as a directly disclosed operating metric.

### Required calculations and checks

- **Comparable-sales bridge**
  - Place reported comparable sales, transaction change, and average-check change in one table.
  - Check whether the transaction and check components approximately reconcile to the disclosed comparable-sales result.
  - Treat any residual as interaction, rounding, or definition difference rather than silently forcing equality.
  - If menu-price and mix components are separately disclosed, isolate them; otherwise state that average check cannot be fully decomposed.
- **Digital comparison**
  - Calculate the percentage-point change in digital sales share between consistent disclosed periods.
  - Do not equate a higher share with incremental traffic unless another source supports that causal claim.
- **Restaurant-cost bridge**
  - Compare each restaurant cost line as a percentage of revenue across annual and quarterly periods.
  - Convert percentage-point changes into basis points as a derived presentation.
  - Separate favorable food or packaging movement from labor and other cost pressure.
  - Quantify restaurant-level margin only where the components and definition reconcile.
- **Volume-leverage test**
  - Compare average restaurant sales with labor, occupancy, and other restaurant costs as percentages of revenue.
  - Assess whether lower unit volumes coincide with fixed-cost or labor deleverage, while retaining management’s explanation as reported rather than independently proven.
- **Unit-growth and maturity test**
  - Calculate net unit growth and the mix of new formats from disclosed restaurant counts and openings.
  - Compare average restaurant sales over time.
  - Align opening cohorts and disclosed ramp periods before attributing dilution to immature units.
- **Capital-intensity test**
  - Calculate capital-expenditure growth, capital expenditures as a percentage of revenue, and—if definitions permit—capital expenditures per net opening.
  - Flag that per-opening calculations can include maintenance, technology, remodel, and other spending unless the filing provides a clean development-capital split.
  - Compare planned spending with historical cash generation and balance-sheet resources without assuming planned amounts were incurred.
- **Corporate-offset test**
  - Compare general and administrative expense as a percentage of revenue with restaurant-level margin movement.
  - Determine whether corporate leverage is large enough to offset restaurant-level pressure rather than merely noting that it improved.
- **Peer benchmark**
  - Calculate revenue growth and consistently defined operating margins over matched periods.
  - Compare direction and magnitude, not just absolute levels.
  - Note franchising, ownership mix, accounting presentation, and scale differences that limit comparability.

### Observable trajectory signals

- Produce a calculation sheet in which every input cell links to a source path and period.
- Mark every output as reported or derived.
- Show formulas and preserve original units before converting millions, percentages, or basis points.
- Reconcile annual totals to quarterly or year-to-date figures where the available periods permit.
- Run arithmetic and sign checks, especially for expense ratios where an increase is economically adverse.
- Present sensitivity ranges where menu price, mix, ramp timing, or capital allocation cannot be isolated.
- Create a compact scorecard covering traffic quality, pricing dependence, restaurant-cost pressure, unit maturation, capital intensity, corporate offsets, and peer context.

## Phase 6: Synthesis and Position

### Objective

Convert the evidence into one explicit directional position on the durability of traffic and margins as the unit base matures. Resolve opposing evidence through causal reasoning and relative weighting; do not finish with an evenly balanced list.

### Expected source files from the manifest

- Core support for the conclusion:
  - `sec_filings/10-k/cmg_2025_10-k.txt`
  - `sec_filings/10-q/cmg_2026q1_10-q.txt`
  - `financials/income_statement/cmg_income_statement.json`
  - `financials/cash_flow/cmg_cash_flow.json`
- Risk and liquidity context:
  - `financials/balance_sheet/cmg_balance_sheet.json`
  - Current and historical annual filings in `sec_filings/10-k/`
- Current outlook:
  - `press_releases/cmg_2026-02-03_8-k.txt`
  - `press_releases/cmg_2026-04-29_8-k.txt`
- Competitive context:
  - `company_profiles.json`
  - Primary and peer income-statement and cash-flow JSON files

### Synthesis procedure

1. State a one-sentence thesis that chooses a side on durability rather than declaring the evidence merely mixed.
2. Address traffic quality first:
   - Decide whether the latest direction represents transaction-led demand improvement, pricing support, or an unresolved combination.
   - Weigh the latest quarter against the longer annual pattern and management’s outlook.
3. Address restaurant-level margins:
   - Explain whether pricing, efficiency, and overhead discipline can absorb labor, food, freight, tariff, and volume pressures.
   - Keep restaurant economics separate from consolidated-margin support.
4. Address maturing unit growth:
   - Explain how the development runway, format mix, ramp period, average-unit-volume movement, and capital requirements interact.
   - Distinguish revenue growth created by adding units from improvement in mature-unit productivity.
5. Address competitive and demand risk:
   - Decide whether peer evidence suggests an industry backdrop, company-specific execution, or both.
   - Incorporate discretionary-spending, competitive, brand, and food-safety exposures according to their relevance to traffic and pricing.
6. Reconcile the central conflict in a single causal argument:
   - Place the recent favorable traffic evidence and long development runway against the longer-period traffic weakness, restaurant-level deleverage, maturation drag, and demand risks.
   - Explain which side is more durable and why, based on breadth, persistence, economic magnitude, and dependence on management forecasts.
7. State residual ambiguity explicitly, especially where the corpus does not isolate menu price from mix, digital migration from incremental demand, or growth capital from maintenance spending.
8. End with concrete signposts that would confirm or invalidate the position, using disclosed operating measures rather than unsupported forecasts.

### Observable trajectory signals

- The written synthesis contains a clear directional conclusion in its opening and closing.
- Each major factual claim has an inline citation to a specific manifest file.
- At least one paragraph directly resolves favorable and adverse evidence within the same argument rather than listing them separately.
- The conclusion distinguishes:
  - Traffic from price and mix.
  - Restaurant-level margin from consolidated margin.
  - Mature-unit productivity from unit-count-driven revenue growth.
  - Actual results from guidance.
  - Reported figures from derived calculations.
- The strongest contrary evidence is stated fairly and then accepted, bounded, or outweighed with cited reasoning.
- Peer evidence influences the company-specific conclusion but is not treated as perfectly comparable.
- Material ambiguities remain visible and are not replaced with invented precision.
- The final position follows from the quantitative scorecard and contradiction log, with no unsupported fact, post-cutoff information, or uncited external assumption.