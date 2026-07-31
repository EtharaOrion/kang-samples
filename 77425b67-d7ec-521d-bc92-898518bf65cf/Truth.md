KANG-TRUTH-SENTINEL: 88646bbd-b28b-4bf0-9369-e542a0bc0d2e

## Phase 1: Corpus Reconnaissance

### Objective

Establish the available evidence set, period coverage, entity mapping, and source hierarchy before forming a view. Apply a hard information cutoff of June 30, 2026. Do not infer document contents from filenames; open each relevant file and verify its reporting period, units, definitions, and whether it contains reported results, management commentary, risk disclosures, or structured financial data.

Prioritize primary-company SEC filings and financial statements for factual claims. Use press releases to identify management-defined metrics and reconciliations, historical filings to establish trends, and peer files only for comparable context.

### Expected source files from the manifest

- Identity and peer mapping:
  - `company_profiles.json`
- Primary-company structured financials:
  - `financials/income_statement/net_income_statement.json`
  - `financials/balance_sheet/net_balance_sheet.json`
  - `financials/cash_flow/net_cash_flow.json`
- Peer structured financials:
  - `financials/income_statement/akam_income_statement.json`
  - `financials/income_statement/ddog_income_statement.json`
  - `financials/income_statement/fsly_income_statement.json`
  - `financials/cash_flow/akam_cash_flow.json`
  - `financials/cash_flow/ddog_cash_flow.json`
  - `financials/cash_flow/fsly_cash_flow.json`
- Annual filings:
  - `sec_filings/10-k/net_2023_10-k.txt`
  - `sec_filings/10-k/net_2024_10-k.txt`
  - `sec_filings/10-k/net_2025_10-k.txt`
- Quarterly filings:
  - `sec_filings/10-q/net_2024q2_10-q.txt`
  - `sec_filings/10-q/net_2024q3_10-q.txt`
  - `sec_filings/10-q/net_2025q1_10-q.txt`
  - `sec_filings/10-q/net_2025q2_10-q.txt`
  - `sec_filings/10-q/net_2025q3_10-q.txt`
  - `sec_filings/10-q/net_2026q1_10-q.txt`
- Press releases:
  - `press_releases/net_2025-02-06_8-k.txt`
  - `press_releases/net_2025-03-27_8-k.txt`
  - `press_releases/net_2025-05-08_8-k.txt`
  - `press_releases/net_2025-06-17_8-k.txt`
  - `press_releases/net_2025-07-31_8-k.txt`
  - `press_releases/net_2025-10-30_8-k.txt`
  - `press_releases/net_2026-02-10_8-k.txt`
  - `press_releases/net_2026-05-07_8-k.txt`
- Long-term business-model context:
  - `sec_filings/s-1/net_2019_s-1.txt`

### Observable trajectory signals

- A complete inventory confirms that every path above exists and is readable.
- The analyst opens the JSON files to inspect field names, units, fiscal-period conventions, null values, and whether quarterly values are discrete or year-to-date.
- The filings and releases are indexed by covered period rather than filename alone.
- Searches are run for revenue, customer counts, dollar-based retention, remaining performance obligations, operating loss, gross margin, operating cash flow, capital expenditures, free cash flow, stock-based compensation, network costs, GPUs, Workers, AI, competition, consumption, and usage.
- A source hierarchy is written down, with duplicate disclosures linked across the annual filing, quarterly filing, structured statements, and corresponding releases.
- Any documents dated after the cutoff are excluded; documents before the cutoff that discuss expectations beyond it are clearly labeled as forecasts rather than realized results.
- Potential inconsistencies in units, metric definitions, or period labels are logged for resolution rather than silently normalized.

## Phase 2: Question Decomposition

### Objective

Convert the broad question into four connected tests and define in advance what evidence would support or weaken each one:

- Whether revenue growth is durable at scale, separating installed-base expansion from new-customer acquisition.
- Whether operating leverage is genuinely improving when GAAP results, non-GAAP results, operating cash flow, free cash flow, stock-based compensation, and gross margin are considered together.
- Whether enterprise penetration and contracted obligations improve forward visibility without overstating the quality of usage-sensitive demand.
- Whether the AI and developer platform has disclosed monetization and defensibility sufficient to justify near-term network and compute investment.

Define the final decision as a choice between competing interpretations, not as a collection of disconnected positives and negatives.

### Expected source files from the manifest

- Core operating record:
  - `sec_filings/10-k/net_2023_10-k.txt`
  - `sec_filings/10-k/net_2024_10-k.txt`
  - `sec_filings/10-k/net_2025_10-k.txt`
  - `sec_filings/10-q/net_2025q1_10-q.txt`
  - `sec_filings/10-q/net_2025q2_10-q.txt`
  - `sec_filings/10-q/net_2025q3_10-q.txt`
  - `sec_filings/10-q/net_2026q1_10-q.txt`
- Financial statements:
  - `financials/income_statement/net_income_statement.json`
  - `financials/balance_sheet/net_balance_sheet.json`
  - `financials/cash_flow/net_cash_flow.json`
- Management-defined metrics and outlook:
  - All eight files under `press_releases/` listed in Phase 1
- Competitive context:
  - `company_profiles.json`
  - The three peer income-statement files and three peer cash-flow files listed in Phase 1
- Business-model history:
  - `sec_filings/s-1/net_2019_s-1.txt`

### Observable trajectory signals

- A question tree links each workstream to specific metrics, disclosures, risks, and possible contrary interpretations.
- A period matrix is created for annual results from 2023 through 2025 and quarterly results through the latest period available before the cutoff.
- The analyst records the reported definition and measurement date for each non-GAAP or operating KPI before comparing it over time.
- Revenue growth is split conceptually into new customers, customer expansion, pricing, usage, and other disclosed drivers rather than treated as one undifferentiated figure.
- The profitability test explicitly separates gross-margin economics, operating-expense leverage, non-cash compensation, working-capital effects, and capital intensity.
- The enterprise test distinguishes customer counts, revenue concentration or mix, deferred revenue, and remaining performance obligations instead of treating them as interchangeable.
- The AI test distinguishes product availability, customer adoption, revenue disclosure, unit economics, capital requirements, and competitive differentiation.
- Decision criteria are established before synthesis so the final position is not chosen solely from the most recent headline result.

## Phase 3: Evidence Gathering

### Objective

Build a claim-level evidence ledger from verified passages and structured statement fields. Capture both the reported value and the surrounding definition, period, comparison base, and management explanation. Prefer primary filings when a release and filing repeat the same fact, while retaining the release for non-GAAP reconciliations or management-defined KPIs not available elsewhere.

### Expected source files from the manifest

#### Revenue durability and customer expansion

- `sec_filings/10-k/net_2023_10-k.txt`
- `sec_filings/10-k/net_2024_10-k.txt`
- `sec_filings/10-k/net_2025_10-k.txt`
- `sec_filings/10-q/net_2024q2_10-q.txt`
- `sec_filings/10-q/net_2024q3_10-q.txt`
- `sec_filings/10-q/net_2025q1_10-q.txt`
- `sec_filings/10-q/net_2025q2_10-q.txt`
- `sec_filings/10-q/net_2025q3_10-q.txt`
- `sec_filings/10-q/net_2026q1_10-q.txt`
- `financials/income_statement/net_income_statement.json`
- All eight listed `press_releases/net_*_8-k.txt` files

Search these files for revenue, year-over-year and sequential growth, paying customers, large-customer definitions, dollar-based net retention, calculation methodology, contract duration, usage, pricing, customer expansion, churn, and management outlook.

#### Profitability and operating leverage

- `financials/income_statement/net_income_statement.json`
- `financials/cash_flow/net_cash_flow.json`
- `sec_filings/10-k/net_2024_10-k.txt`
- `sec_filings/10-k/net_2025_10-k.txt`
- `sec_filings/10-q/net_2025q1_10-q.txt`
- `sec_filings/10-q/net_2026q1_10-q.txt`
- All eight listed `press_releases/net_*_8-k.txt` files

Extract revenue, gross profit, operating expenses, GAAP operating income or loss, non-GAAP operating results, operating cash flow, capital expenditures, free cash flow, stock-based compensation, depreciation, working-capital changes, and the company’s reconciliation methodology. Record disclosed explanations for changes in network, bandwidth, co-location, equipment, and compute costs.

#### Enterprise mix and contracted visibility

- `sec_filings/10-k/net_2024_10-k.txt`
- `sec_filings/10-k/net_2025_10-k.txt`
- `sec_filings/10-q/net_2025q1_10-q.txt`
- `sec_filings/10-q/net_2025q2_10-q.txt`
- `sec_filings/10-q/net_2025q3_10-q.txt`
- `sec_filings/10-q/net_2026q1_10-q.txt`
- `financials/balance_sheet/net_balance_sheet.json`
- Relevant files among the eight listed press releases, after their contents are verified

Extract the reported large-customer threshold and count, total paying customers, any customer or channel concentration, deferred revenue, remaining performance obligations, expected conversion timing, contract characteristics, and disclosed cancellation or usage sensitivities.

#### AI platform and competitive positioning

- `sec_filings/10-k/net_2023_10-k.txt`
- `sec_filings/10-k/net_2024_10-k.txt`
- `sec_filings/10-k/net_2025_10-k.txt`
- `sec_filings/10-q/net_2026q1_10-q.txt`
- `sec_filings/s-1/net_2019_s-1.txt`
- All eight listed `press_releases/net_*_8-k.txt` files
- `company_profiles.json`
- `financials/income_statement/net_income_statement.json`

Search for Workers, developer services, AI inference, GPUs, serverless products, product pricing, adoption indicators, revenue disclosure, network reach, competitive risks, hyperscalers, bundled products, pricing pressure, and the relationship between investment and gross margin.

### Observable trajectory signals

- Each contemplated factual claim has an exact source path, reporting period, units, and nearby contextual note.
- Repeated disclosures are compared across filings to detect definition changes, restatements, or selective presentation.
- Annual and quarterly revenue figures from filings are reconciled to `financials/income_statement/net_income_statement.json`.
- Cash-flow figures are reconciled between `financials/cash_flow/net_cash_flow.json`, SEC statements, and press-release reconciliations.
- Customer, retention, and performance-obligation metrics are captured only after their definitions and measurement dates are read.
- AI product claims are separated into disclosed capabilities, adoption evidence, monetization evidence, and management aspiration.
- Peer files are used only after confirming comparable periods and accounting line items; absent peer disclosures are not filled with assumptions.
- The evidence ledger flags missing disclosures, particularly where strategic language is available but product revenue or unit economics are not separately reported.

## Phase 4: Counter-Evidence Engagement

### Objective

Actively seek the strongest evidence against the emerging interpretation. Test whether favorable growth signals are temporary, whether cash profitability depends on non-cash compensation or working-capital timing, whether backlog provides less protection than its headline size suggests, and whether AI investment is producing measurable economics or only increasing near-term costs.

### Expected source files from the manifest

- Risk factors, MD&A, accounting notes, and KPI definitions:
  - `sec_filings/10-k/net_2023_10-k.txt`
  - `sec_filings/10-k/net_2024_10-k.txt`
  - `sec_filings/10-k/net_2025_10-k.txt`
  - `sec_filings/10-q/net_2025q1_10-q.txt`
  - `sec_filings/10-q/net_2025q2_10-q.txt`
  - `sec_filings/10-q/net_2025q3_10-q.txt`
  - `sec_filings/10-q/net_2026q1_10-q.txt`
- Conflicting profitability lenses:
  - `financials/income_statement/net_income_statement.json`
  - `financials/cash_flow/net_cash_flow.json`
  - All eight listed press releases
- Backlog and liquidity checks:
  - `financials/balance_sheet/net_balance_sheet.json`
  - `sec_filings/10-k/net_2025_10-k.txt`
  - `sec_filings/10-q/net_2026q1_10-q.txt`
- Competitive checks:
  - `company_profiles.json`
  - `financials/income_statement/akam_income_statement.json`
  - `financials/income_statement/ddog_income_statement.json`
  - `financials/income_statement/fsly_income_statement.json`
  - `financials/cash_flow/akam_cash_flow.json`
  - `financials/cash_flow/ddog_cash_flow.json`
  - `financials/cash_flow/fsly_cash_flow.json`
  - `sec_filings/s-1/net_2019_s-1.txt`

### Observable trajectory signals

- An adverse-evidence table is maintained alongside the supporting-evidence table.
- Any apparent revenue acceleration is tested against sequential growth, comparison-base effects, contract timing, pricing, usage, and guidance rather than accepted from a single year-over-year rate.
- Retention is evaluated both against the immediately preceding period and a longer historical range, with attention to definition consistency and whether it excludes new customers.
- Customer-count growth is compared with revenue and retention to determine whether growth relies more on new logos or expansion of the installed base.
- GAAP operating losses and margins are compared directly with non-GAAP operating results and cash-flow measures; none is allowed to substitute for the others.
- Stock-based compensation, depreciation, working-capital changes, and capital expenditures are tested as possible explanations for divergence between accounting losses and cash generation.
- Gross-margin pressure is investigated separately from operating-expense leverage, preventing lower operating-expense ratios from obscuring deteriorating infrastructure economics.
- Remaining performance obligations are tested for expected timing, contract duration, cancellation exposure, and growth relative to revenue. Deferred revenue and remaining performance obligations are not conflated.
- AI claims are challenged by searching for separately disclosed revenue, customer adoption, pricing, utilization, and gross-profit contribution. Lack of disclosure is presented as uncertainty, not proof of either success or failure.
- Peer comparisons acknowledge differences in product mix and accounting presentation and are discarded where comparability cannot be established.
- The analyst writes the strongest credible opposing case before drafting the final position.

## Phase 5: Quantitative Anchoring

### Objective

Create a reproducible set of calculations that distinguishes company-reported figures from analyst-derived figures. Use calculations to test direction, scale, and consistency rather than to manufacture precision beyond the disclosures.

### Expected source files from the manifest

- Reported income-statement inputs:
  - `financials/income_statement/net_income_statement.json`
  - `sec_filings/10-k/net_2023_10-k.txt`
  - `sec_filings/10-k/net_2024_10-k.txt`
  - `sec_filings/10-k/net_2025_10-k.txt`
  - `sec_filings/10-q/net_2025q1_10-q.txt`
  - `sec_filings/10-q/net_2026q1_10-q.txt`
- Reported cash-flow inputs:
  - `financials/cash_flow/net_cash_flow.json`
  - `sec_filings/10-k/net_2024_10-k.txt`
  - `sec_filings/10-k/net_2025_10-k.txt`
  - `sec_filings/10-q/net_2025q1_10-q.txt`
  - `sec_filings/10-q/net_2026q1_10-q.txt`
- Balance-sheet and obligation inputs:
  - `financials/balance_sheet/net_balance_sheet.json`
  - `sec_filings/10-k/net_2025_10-k.txt`
  - `sec_filings/10-q/net_2026q1_10-q.txt`
- Company-defined non-GAAP inputs:
  - All eight listed press releases
- Optional comparable calculations:
  - The six peer financial-statement files listed in Phase 1

### Observable trajectory signals

- Every table labels values as either **reported** or **derived**.
- Reported figures retain the source’s units, period, and accounting basis before any normalization.
- Derived calculations show formulas and cite every input file. At minimum, the analyst calculates:
  - Year-over-year revenue growth: `(current-period revenue / prior comparable-period revenue) - 1`.
  - Sequential quarterly growth where discrete quarterly data are available.
  - Percentage-point changes in gross margin and operating margin.
  - GAAP operating margin: `GAAP operating income or loss / revenue`.
  - Operating cash-flow margin: `cash from operations / revenue`.
  - Free-cash-flow margin using the company’s reported definition, followed by an independent reconstruction from disclosed cash-flow components where possible.
  - Stock-based compensation as a percentage of revenue and its change over time.
  - The absolute and percentage change in GAAP operating loss.
  - Large-customer growth and total-paying-customer growth, using the disclosed threshold consistently.
  - The ratio of large customers to total paying customers, if both figures use compatible dates and definitions.
  - Remaining-performance-obligation growth, its expected near-term conversion share, and its growth relative to revenue.
- Annual, quarterly, and year-to-date cash-flow figures are not mixed. If only year-to-date data are reported, discrete quarters are derived only when subtraction is valid and clearly labeled.
- Free cash flow is not treated as equivalent to GAAP operating profit. The bridge identifies non-cash charges, working-capital effects, and capital spending without double counting.
- Non-GAAP figures remain company-reported measures; any analyst adjustment is separately named and is not relabeled as company-reported.
- Gross-margin calculations are checked against reported margins, with differences investigated for rounding or numerator-definition issues.
- Peer margins and growth rates are included only after period alignment and confirmation that the line items are comparable.
- Sensitivity analysis tests whether the operating-leverage interpretation changes when stock-based compensation is treated as an economic cost, when working-capital benefits normalize, or when infrastructure investment remains elevated.
- Calculation discrepancies are preserved in an exception log and resolved from the underlying filing where possible.

## Phase 6: Synthesis and Position

### Objective

Resolve the opposing evidence into one explicit investment conclusion about whether the company is entering durable, profitable growth or whether growth is being sustained by spending that delays true operating leverage. The conclusion must cover revenue durability, installed-base expansion, enterprise and contracted visibility, GAAP versus cash profitability, gross-margin economics, and AI monetization as parts of one causal argument.

The final position must state which evidence is decisive, which contrary evidence remains material, and what uncertainty cannot be resolved from the corpus. It must not present positive and negative facts in parallel without explaining why one side carries greater weight.

### Expected source files from the manifest

- Decisive primary evidence:
  - `sec_filings/10-k/net_2024_10-k.txt`
  - `sec_filings/10-k/net_2025_10-k.txt`
  - `sec_filings/10-q/net_2025q1_10-q.txt`
  - `sec_filings/10-q/net_2026q1_10-q.txt`
  - `financials/income_statement/net_income_statement.json`
  - `financials/balance_sheet/net_balance_sheet.json`
  - `financials/cash_flow/net_cash_flow.json`
- KPI, reconciliation, and management-context evidence:
  - All eight listed press releases
- Historical and competitive context where verified:
  - `sec_filings/10-k/net_2023_10-k.txt`
  - `sec_filings/s-1/net_2019_s-1.txt`
  - `company_profiles.json`
  - The six peer financial-statement files listed in Phase 1

### Observable trajectory signals

- The draft opens with a direct position rather than a neutral overview.
- A written synthesis explicitly reconciles growth and customer-expansion evidence with GAAP losses, non-GAAP profitability, cash generation, stock-based compensation, and gross-margin pressure.
- Enterprise customer growth and remaining performance obligations are interpreted as either reinforcing or failing to reinforce the revenue conclusion, with contract and usage risks incorporated.
- AI investment is connected to both sides of the argument: potential product expansion and retention on one side, and present compute costs, margin pressure, monetization uncertainty, and competition on the other.
- The analyst distinguishes evidence of platform capability from evidence of commercial success.
- The strongest opposing case is stated accurately and then answered using the evidence hierarchy and quantitative work, not dismissed.
- Ambiguities—such as missing product-level revenue, uncertain unit economics, or KPI-definition limitations—remain visible in the conclusion.
- Every factual claim carries an inline citation to an exact corpus path. Derived claims cite all source inputs and are labeled as calculations.
- Management forecasts are identified as forecasts; reported results are not blended with outlook.
- Peer context remains secondary to the primary-company record and is omitted if it does not survive comparability checks.
- The conclusion identifies the few future indicators that would confirm or invalidate the position, using only metrics already grounded in the corpus.
- A final citation audit verifies that no number, event, entity, product claim, or causal assertion lacks support from a listed file and that all evidence respects the June 30, 2026 cutoff.