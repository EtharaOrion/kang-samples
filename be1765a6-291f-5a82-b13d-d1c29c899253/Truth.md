KANG-TRUTH-SENTINEL: 530c0e92-9a40-4b18-9044-be02c3d56075

## Phase 1: Corpus Reconnaissance

### Objective

Establish the available evidence set, reporting chronology, company/peer mapping, and period cutoff before forming any view. Treat every file as a candidate until its contents are opened and verified; do not infer facts solely from its path or filename.

### Expected source files from the manifest

- `company_profiles.json`
- `financials/income_statement/snow_income_statement.json`
- `financials/balance_sheet/snow_balance_sheet.json`
- `financials/cash_flow/snow_cash_flow.json`
- `financials/income_statement/ddog_income_statement.json`
- `financials/income_statement/mdb_income_statement.json`
- `financials/income_statement/net_income_statement.json`
- `financials/cash_flow/ddog_cash_flow.json`
- `financials/cash_flow/mdb_cash_flow.json`
- `financials/cash_flow/net_cash_flow.json`
- `sec_filings/10-k/snow_2024_10-k.txt`
- `sec_filings/10-k/snow_2025_10-k.txt`
- `sec_filings/10-k/snow_2026_10-k.txt`
- All six files under `sec_filings/10-q/`
- `sec_filings/s-1/snow_2020_s-1.txt`
- All eight files under `press_releases/`

### Observable trajectory signals

- Enumerate the manifest and confirm that every opened path exists within `/app/data/`.
- Parse `company_profiles.json` to verify the primary company, peer identities, and point-in-time profile data.
- Open each financial JSON and inspect its schema, units, fiscal-period labels, restatements, nulls, and whether values are quarterly, year-to-date, or annual.
- Read the cover pages and filing-period identifiers of the annual and quarterly filings to build a chronology by fiscal period rather than relying on filenames.
- Inspect the press releases to determine which contain earnings exhibits, product announcements, or other relevant disclosures and which merely duplicate filing data.
- Build a source register containing path, document type, covered period, publication or filing date when disclosed, and likely analytical use.
- Enforce the June 30, 2026 cutoff. Exclude any event or disclosure first made after that date, while retaining earlier historical periods needed for trend analysis.
- Mark duplicate disclosures so the same company-supplied fact is not incorrectly treated as independent corroboration.

## Phase 2: Question Decomposition

### Objective

Convert the broad assignment into testable analytical questions, define the relevant metrics, and specify what evidence would support or weaken each possible conclusion.

### Expected source files from the manifest

- `sec_filings/10-k/snow_2026_10-k.txt`
- `sec_filings/10-q/snow_2026q1_10-q.txt`
- `sec_filings/s-1/snow_2020_s-1.txt`
- `financials/income_statement/snow_income_statement.json`
- `financials/cash_flow/snow_cash_flow.json`
- `financials/balance_sheet/snow_balance_sheet.json`
- `company_profiles.json`

### Observable trajectory signals

- Write an issue tree with four linked questions:
  - Whether recognized product revenue is supported by durable installed-base consumption and customer expansion.
  - Whether bookings, remaining performance obligations, billing terms, and contract structure provide reliable forward information under a consumption model.
  - Whether gross-margin performance can translate into credible GAAP operating leverage after stock compensation, dilution, and equity-related cash costs.
  - Whether AI-related product adoption can generate incremental consumption despite supplier concentration and direct competition from public-cloud platforms.
- Define each metric before extraction: product revenue, total revenue, net revenue retention, remaining performance obligations, capacity arrangements, on-demand revenue, product gross margin, total gross margin, GAAP operating income, free cash flow, stock-based compensation, weighted-average diluted shares, and shares outstanding.
- Separate operating indicators into:
  - Recognized outcomes, such as revenue and GAAP profit or loss.
  - Forward indicators, such as contractual obligations and customer commitments.
  - Adoption indicators, such as customer counts, large-customer cohorts, and disclosed product usage.
  - Economic costs, including both income-statement expense and cash consequences of employee equity.
- Record known comparability hazards: consumption revenue is not equivalent to ratable subscription revenue; remaining obligations do not fix consumption timing; product gross margin is not total-company gross margin; company-defined free cash flow may differ from a mechanically calculated measure; weighted-average shares are not the same as period-end shares.
- Create a claim plan requiring every eventual factual statement to carry an inline citation to an exact relative path.
- Identify ambiguity tests in advance, including whether a one-quarter change is signal or noise, whether backlog changes reflect seasonality or demand, and whether AI adoption evidence demonstrates incremental consumption rather than product availability alone.

## Phase 3: Evidence Gathering

### Objective

Extract the primary-company disclosures and structured financial data needed to evaluate growth durability, contract quality, profitability, dilution, and competitive positioning without forming the final conclusion prematurely.

### Expected source files from the manifest

- `sec_filings/10-k/snow_2026_10-k.txt`
- `sec_filings/10-q/snow_2026q1_10-q.txt`
- `sec_filings/10-k/snow_2024_10-k.txt`
- `sec_filings/10-k/snow_2025_10-k.txt`
- `sec_filings/10-q/snow_2024q2_10-q.txt`
- `sec_filings/10-q/snow_2024q3_10-q.txt`
- `sec_filings/10-q/snow_2025q1_10-q.txt`
- `sec_filings/10-q/snow_2025q2_10-q.txt`
- `sec_filings/10-q/snow_2025q3_10-q.txt`
- `financials/income_statement/snow_income_statement.json`
- `financials/cash_flow/snow_cash_flow.json`
- `financials/balance_sheet/snow_balance_sheet.json`
- `press_releases/snow_2026-02-25_8-k.txt`
- `press_releases/snow_2026-03-31_8-k.txt`
- `press_releases/snow_2026-05-27_8-k.txt`
- Earlier press-release files where a content search confirms relevant disclosures

### Observable trajectory signals

- Search the latest annual and quarterly filings for disclosures concerning consumption-based recognition, customer control over usage timing, optimization behavior, macro sensitivity, holidays, contract rollover, and consumption beyond an original contract term.
- Extract net revenue retention observations with their exact measurement dates and definitions. Compare like-for-like annual and quarterly disclosures and note any definition change.
- Extract total-customer counts, large-customer cohort counts, product-revenue concentration associated with those cohorts, and the share of revenue tied to capacity arrangements.
- Extract remaining performance obligations at each available quarter or year-end, together with management’s discussion of bookings seasonality, conversion timing, contract duration, and limitations of that indicator.
- Read billing and contract disclosures to identify annual, quarterly, or monthly invoicing practices, changes in billing cadence, and the relative significance of capacity and on-demand arrangements.
- Pull product revenue, total revenue, product cost of revenue, total cost of revenue, operating expenses, operating loss, net loss, and diluted weighted-average shares from the income-statement JSON. Reconcile annual totals or quarter labels against the filing before use.
- Pull operating cash flow, capital expenditures or purchases of property and equipment, stock-based compensation add-backs, and any disclosed employee-equity payroll-tax cash payments from the cash-flow JSON and filing.
- Pull accumulated deficit, period-end equity balances, and shares outstanding where available from the balance-sheet JSON and filing.
- Search research-and-development and sales-and-marketing notes for stock-compensation allocations rather than relying only on the consolidated total.
- Search the latest filings and relevant releases for AI and Cortex product availability, adoption, usage, monetization, and consumption claims. Distinguish a product launch from evidence of material revenue contribution.
- Search risk factors and business descriptions for named competitors, dependence on public-cloud infrastructure providers, cloud-pricing exposure, GPU or inference costs, and warnings that newer features could compress margins.
- Store each extracted item in an evidence table with metric or statement, period, value, unit, definition, exact path, document location, and whether it is a company assertion or audited/accounting data.
- Cite the original filing where possible; use an earnings release as a supplemental source or for information not present in the filing, not as artificial independent confirmation.

## Phase 4: Counter-Evidence Engagement

### Objective

Actively seek the strongest evidence against the emerging interpretation and test whether apparent positives or negatives survive alternative explanations.

### Expected source files from the manifest

- `sec_filings/10-k/snow_2024_10-k.txt`
- `sec_filings/10-k/snow_2025_10-k.txt`
- `sec_filings/10-k/snow_2026_10-k.txt`
- All six files under `sec_filings/10-q/`
- All eight files under `press_releases/`
- `financials/income_statement/snow_income_statement.json`
- `financials/cash_flow/snow_cash_flow.json`
- `financials/balance_sheet/snow_balance_sheet.json`
- `company_profiles.json`
- All listed peer income-statement and cash-flow JSON files

### Observable trajectory signals

- Construct a two-column evidence matrix for each analytical question, with the strongest supporting and contradicting facts listed side by side and tied to exact paths.
- Test whether stabilization in retention is broad-based or merely a short observation after a longer deceleration.
- Challenge large-customer growth by checking revenue concentration, dependence on existing capacity customers, and whether cohort expansion is sufficient to offset slower usage elsewhere.
- Challenge remaining-obligation growth or decline by comparing equivalent fiscal quarters across prior years, reading disclosed sales seasonality, and distinguishing contractual demand from timing of consumption.
- Examine whether changes in invoicing cadence affect billings and cash collection without changing underlying customer demand.
- Challenge positive free cash flow by tracing noncash stock compensation, equity-related cash payroll taxes, capital-expenditure definitions, and any working-capital benefit.
- Challenge gross-margin optimism with disclosed AI infrastructure costs, new-product mix, professional-services losses, cloud-provider pricing, and supplier concentration.
- Challenge an AI growth narrative by requiring evidence of incremental usage, customer conversion, or monetization rather than treating general availability or product count as proof.
- Challenge a bearish view by checking whether product gross margin, customer expansion, retention, revenue growth, or cash generation improved despite the cited risks.
- Compare the peer financial files only after verifying business-model and accounting comparability. Use peers as context for margins, growth, cash generation, and dilution, not as substitutes for company-specific evidence.
- Maintain an ambiguity log for unresolved definition changes, missing quarterly details, overlapping disclosures, and management statements that cannot be independently quantified.

## Phase 5: Quantitative Anchoring

### Objective

Turn the extracted evidence into reproducible time-series and bridge calculations while clearly separating figures disclosed by the company from analyst-derived results.

### Expected source files from the manifest

- `financials/income_statement/snow_income_statement.json`
- `financials/cash_flow/snow_cash_flow.json`
- `financials/balance_sheet/snow_balance_sheet.json`
- `sec_filings/10-k/snow_2026_10-k.txt`
- `sec_filings/10-q/snow_2026q1_10-q.txt`
- Earlier Snowflake annual and quarterly filings for comparable periods
- All listed peer income-statement and cash-flow JSON files
- `company_profiles.json`

### Observable trajectory signals

- Create a calculation workbook or structured table with separate columns for:
  - Reported value.
  - Derived value.
  - Formula.
  - Source period.
  - Unit.
  - Exact source path.
  - Comparability or definition caveat.
- Label retention rates, customer counts, remaining obligations, disclosed margins, stock compensation, accumulated deficit, and company-defined free cash flow as reported only when directly present in a read source.
- Calculate, and label as derived:
  - Sequential and year-over-year product-revenue growth.
  - Percentage-point changes in net revenue retention.
  - Growth in total customers and large-customer cohorts.
  - Large-customer revenue concentration changes.
  - Sequential and year-over-year changes in remaining obligations.
  - GAAP gross margin as `(revenue − cost of revenue) / revenue` when the needed line items are comparable.
  - GAAP operating margin as `operating income or loss / revenue`.
  - Net margin as `net income or loss / revenue`.
  - Stock-based compensation as a percentage of revenue and operating cash flow.
  - Research-and-development and sales-and-marketing stock compensation as percentages of the corresponding expense categories when allocation data are available.
  - Free cash flow using a transparent cash-flow-statement formula, while preserving the company’s separately reported non-GAAP measure and reconciling definition differences.
  - Changes in diluted weighted-average shares and, separately, period-end shares outstanding.
  - A cash-generation bridge from GAAP net loss to operating cash flow, highlighting noncash stock compensation, working capital, depreciation, and equity-related tax cash outflows where disclosed.
- Reconcile annual figures against quarterly sums only after checking whether quarterly cash-flow figures are standalone or year-to-date.
- Analyze remaining obligations on both sequential and comparable-quarter bases so normal fourth-quarter contracting patterns are not misclassified as structural deterioration or recovery.
- Keep product gross margin separate from total gross margin and identify the contribution of lower-margin or loss-making services where the source permits.
- Avoid presenting peer comparisons as directly equivalent when revenue recognition, product mix, fiscal calendars, or free-cash-flow definitions differ.
- Run sensitivity cases for the final judgment, such as slower retention, delayed obligation conversion, modest gross-margin compression from AI workloads, and different rates of stock-compensation moderation. State assumptions explicitly and do not present sensitivities as reported forecasts.
- Independently reperform every calculation used in the written conclusion and trace it to source line items.

## Phase 6: Synthesis and Position

### Objective

Resolve the conflicting evidence into one explicit view on the durability of consumption-led growth and the credibility of the margin path, including how AI opportunity and cloud-platform competition affect that view.

### Expected source files from the manifest

- `sec_filings/10-k/snow_2026_10-k.txt`
- `sec_filings/10-q/snow_2026q1_10-q.txt`
- `financials/income_statement/snow_income_statement.json`
- `financials/cash_flow/snow_cash_flow.json`
- `financials/balance_sheet/snow_balance_sheet.json`
- `company_profiles.json`
- Relevant, content-verified files under `press_releases/`
- Historical Snowflake filings and peer JSON files used in the preceding comparisons

### Observable trajectory signals

- Begin the written synthesis with a direct, falsifiable position rather than a neutral summary. State separately whether growth durability is strong, conditional, or weak and whether the margin path is credible, delayed, or structurally impaired.
- Build the position in causal order:
  1. Explain how customer consumption and expansion translate into recognized revenue.
  2. Determine how much confidence contractual obligations and billing data add to that outlook.
  3. Assess whether gross profit can translate into GAAP operating leverage after stock compensation and dilution.
  4. Decide whether AI products improve incremental consumption enough to offset infrastructure costs and supplier-competitor pressure.
- Explicitly reconcile opposing evidence. Do not merely list favorable operating indicators next to unfavorable profitability indicators; explain which evidence is more decision-relevant, which is temporary or structural, and why the combined record supports the chosen stance.
- Distinguish near-term revenue visibility from long-term demand quality, and distinguish positive cash generation from economic profitability.
- State unresolved ambiguity where the corpus cannot establish causality, material AI revenue contribution, exact obligation-conversion timing, or a clean path from non-GAAP cash generation to GAAP profitability.
- Include the strongest contrary case in its best form, then explain why it does or does not overturn the position.
- Attach an inline citation to every factual claim using the exact relative source path. For derived figures, cite all input files and identify the result as analyst-calculated.
- End with a concise monitoring framework: retention direction, large-customer expansion, obligation conversion, billing cadence, product and total gross margins, GAAP operating leverage, stock compensation, share-count growth, equity-related cash taxes, and disclosed AI consumption.
- Perform a final citation audit, calculation check, cutoff check, and contradiction check before writing `/app/answer.txt`.