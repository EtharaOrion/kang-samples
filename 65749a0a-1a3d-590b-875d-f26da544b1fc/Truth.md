KANG-TRUTH-SENTINEL: 2037058e-fd00-4327-9ba5-8adcf6a57a38

## Phase 1: Corpus Reconnaissance

### Objective

Establish the available evidence set, verify document periods and entities from file contents, and create a source hierarchy before forming any view. Treat June 30, 2026 as the information cutoff. Do not infer relevance, reporting period, or transaction status solely from a filename.

### Expected source files from the manifest

- `company_profiles.json`
- `press_releases/dash_2026-05-06_8-k.txt`
- `press_releases/dash_2026-06-12_8-k.txt`
- `press_releases/dash_2026-02-18_8-k.txt`
- `press_releases/dash_2025-11-05_8-k.txt`
- `press_releases/dash_2025-08-06_8-k.txt`
- `press_releases/dash_2025-06-02_8-k.txt`
- `press_releases/dash_2025-05-28_8-k.txt`
- `press_releases/dash_2025-10-02_8-k.txt`
- `sec_filings/10-k/dash_2025_10-k.txt`
- `sec_filings/10-k/dash_2024_10-k.txt`
- `sec_filings/10-k/dash_2023_10-k.txt`
- `sec_filings/10-q/dash_2026q1_10-q.txt`
- `sec_filings/10-q/dash_2025q3_10-q.txt`
- `sec_filings/10-q/dash_2025q2_10-q.txt`
- `sec_filings/10-q/dash_2025q1_10-q.txt`
- `sec_filings/10-q/dash_2024q3_10-q.txt`
- `sec_filings/10-q/dash_2024q2_10-q.txt`
- `sec_filings/s-1/dash_2020_s-1.txt`
- `financials/income_statement/dash_income_statement.json`
- `financials/balance_sheet/dash_balance_sheet.json`
- `financials/cash_flow/dash_cash_flow.json`
- `financials/income_statement/uber_income_statement.json`
- `financials/income_statement/cart_income_statement.json`
- `financials/cash_flow/uber_cash_flow.json`
- `financials/cash_flow/cart_cash_flow.json`

### Observable trajectory signals

- Produce a file inventory grouped into press releases, annual filings, quarterly filings, financial statements, company profiles, and optional peer material.
- Open each high-priority document and verify its internal company name, reporting period, filing or publication date, units, and whether figures are quarterly, year-to-date, or annual.
- Rank sources by analytical use:
  1. Contemporaneous quarterly release and quarterly filing for current operating data.
  2. Latest annual filing for historical context, risk disclosures, business model, and accounting definitions.
  3. Structured financial files for trend reconstruction and cross-checks.
  4. Earlier releases and filings for prior-period comparisons.
  5. Peer files only for a clearly defined and like-for-like sanity check.
- Inspect `press_releases/dash_2026-06-12_8-k.txt` rather than presuming it updates operating results. Record either the relevant evidence extracted or a documented reason for excluding it.
- Search the principal files for terms related to orders, Marketplace GOV, revenue, adjusted EBITDA, net income, contribution profit, grocery, retail, advertising, Deliveroo, Wolt, international operations, acquisition costs, integration, stock-based compensation, depreciation, amortization, and country exposure.
- Maintain a source log showing files opened, relevant sections located, reporting periods, and unresolved definition differences.
- Confirm that every item retained is available as of the cutoff and that no conclusion has yet been drafted.

## Phase 2: Question Decomposition

### Objective

Convert the assignment into testable analytical questions and define what evidence would confirm or weaken each proposition. Separate operating growth, accounting profitability, expansion economics, and acquisition integration so that evidence from one area is not used as a substitute for another.

### Expected source files from the manifest

- `press_releases/dash_2026-05-06_8-k.txt`
- `sec_filings/10-q/dash_2026q1_10-q.txt`
- `sec_filings/10-k/dash_2025_10-k.txt`
- `financials/income_statement/dash_income_statement.json`
- `financials/cash_flow/dash_cash_flow.json`
- `financials/balance_sheet/dash_balance_sheet.json`
- `company_profiles.json`

### Observable trajectory signals

- Create a question-and-evidence matrix covering four analytical blocks:
  - How much of current top-line growth is attributable to the acquired business, and what does the comparable-company growth rate indicate?
  - Does the profitability improvement survive scrutiny under both adjusted EBITDA and GAAP net income, including the reconciliation between them?
  - Is grocery and retail expansion showing repeatable consumer, selection, monetization, and unit-economic progress, or primarily investment-led volume growth?
  - Does international expansion improve the long-run earnings base faster than acquisition and integration costs dilute near-term margins?
- Define the principal metrics before extracting values: Total Orders, Marketplace GOV, revenue, net revenue margin, contribution profit, adjusted EBITDA, adjusted EBITDA as a percentage of GOV, GAAP operating income, GAAP net income, operating cash flow, and free cash flow if the corpus supports a consistent definition.
- Split each question into confirming evidence and disconfirming evidence. For example, acquisition-adjusted growth and margin ratios must be tested alongside headline growth rather than treated as footnotes.
- Specify time comparisons in advance: latest quarter versus the prior-year quarter, sequential quarter, five-quarter trend where available, and longer annual context where definitions remain comparable.
- Create a definitions register for non-GAAP measures and identify which document supplies each definition or reconciliation.
- Mark unresolved questions explicitly, including missing segment economics, uncertain allocation of acquisition effects, or disclosure that is qualitative rather than quantified.
- Produce a planned citation map linking each intended factual category to one or more exact corpus paths.

## Phase 3: Evidence Gathering

### Objective

Collect primary evidence for each analytical block, cross-check key claims across documents, and preserve enough context to distinguish management characterization from reported financial results.

### Expected source files from the manifest

- `press_releases/dash_2026-05-06_8-k.txt`
- `sec_filings/10-q/dash_2026q1_10-q.txt`
- `sec_filings/10-k/dash_2025_10-k.txt`
- `financials/income_statement/dash_income_statement.json`
- `financials/cash_flow/dash_cash_flow.json`
- `financials/balance_sheet/dash_balance_sheet.json`
- `press_releases/dash_2026-02-18_8-k.txt`
- `press_releases/dash_2025-11-05_8-k.txt`
- `press_releases/dash_2025-08-06_8-k.txt`
- `sec_filings/10-k/dash_2024_10-k.txt`
- `sec_filings/10-q/dash_2025q1_10-q.txt`
- `sec_filings/10-q/dash_2025q2_10-q.txt`
- `sec_filings/10-q/dash_2025q3_10-q.txt`

### Observable trajectory signals

- Read `press_releases/dash_2026-05-06_8-k.txt` for the latest disclosed operating scale, year-over-year growth, acquisition-excluded growth, non-GAAP profitability, new-category commentary, international operating indicators, and acquisition outlook. Capture full metric labels, periods, units, and scope.
- Read the relevant financial statements, MD&A, non-GAAP reconciliations, acquisition notes, and subsequent-event sections in `sec_filings/10-q/dash_2026q1_10-q.txt`. Compare them directly with the release and record any differences in scope or presentation.
- Read `sec_filings/10-k/dash_2025_10-k.txt` for:
  - Historical profitability and loss context.
  - Revenue and cost drivers.
  - Definitions and limitations of non-GAAP measures.
  - Grocery, retail, advertising, and broader marketplace strategy.
  - Competition from merchants, delivery platforms, and large technology companies.
  - International scale, operating leverage, acquisition, and integration risks.
- Use `financials/income_statement/dash_income_statement.json` to reconstruct the quarterly GAAP revenue and earnings trend. Reconcile periods and units to the filed statements before relying on the structured data.
- Use `financials/cash_flow/dash_cash_flow.json` and `financials/balance_sheet/dash_balance_sheet.json` to test earnings quality, cash generation, acquisition-related balance-sheet changes, and capital or working-capital demands where the files provide comparable data.
- Read earlier quarterly releases and filings to determine whether current margin, contribution-profit, and growth observations represent a sustained trajectory, seasonality, or a one-quarter result.
- Build an evidence table with columns for analytical block, claim candidate, metric or disclosure, period, reported scope, exact source path, corroborating source, and caveat.
- Classify qualitative statements by type: observed operating result, management expectation, strategic assertion, accounting disclosure, or risk disclosure.
- Use the peer files only after verifying identities and metric comparability through `company_profiles.json`. Exclude peer comparisons that mix materially different revenue recognition, geographic scope, or business models.
- Record absences as evidence limitations. In particular, do not infer standalone grocery, retail, advertising, Deliveroo, or Wolt margins if the corpus does not disclose them.

## Phase 4: Counter-Evidence Engagement

### Objective

Identify and test the strongest evidence against the emerging interpretation. Determine whether favorable operating indicators are offset by accounting deterioration, mix dilution, competitive intensity, integration costs, or an insufficiently long observation window.

### Expected source files from the manifest

- `sec_filings/10-k/dash_2025_10-k.txt`
- `sec_filings/10-q/dash_2026q1_10-q.txt`
- `press_releases/dash_2026-05-06_8-k.txt`
- `financials/income_statement/dash_income_statement.json`
- `financials/cash_flow/dash_cash_flow.json`
- `financials/balance_sheet/dash_balance_sheet.json`
- `sec_filings/10-k/dash_2024_10-k.txt`
- `press_releases/dash_2026-02-18_8-k.txt`

### Observable trajectory signals

- Construct an opposing-evidence ledger pairing every favorable claim with the most credible challenge from another metric, period, or filing section.
- Test headline growth against acquisition-excluded growth and against any change in revenue as a percentage of GOV. Determine whether acquisition mix or geography changes the economic interpretation.
- Test adjusted EBITDA improvement against GAAP net income, operating income, stock-based compensation, depreciation and amortization, acquisition-related costs, and other reconciliation items actually disclosed in the corpus.
- Compare the latest adjusted EBITDA-to-GOV result with the preceding quarters rather than relying only on absolute adjusted EBITDA growth.
- Evaluate grocery and retail momentum against disclosed competitive disadvantages, merchant bargaining power, owned delivery networks, promotional requirements, and the absence of separately disclosed category margins.
- Test the proposed role of advertising by distinguishing evidence of strategic monetization from evidence that it has already offset lower economics elsewhere. Do not quantify an offset without segment-level support.
- Compare international demand and acquisition expectations with integration expense, geographic complexity, foreign-market competition, and disclosures about the difficulty of reaching scale and profitability across many markets.
- Separate realized results from forward-looking expectations. Apply greater evidentiary weight to filed historical figures than to projected acquisition contributions or qualitative synergy claims.
- Check whether cash flow corroborates the non-GAAP earnings direction. If cash flow is distorted by working capital, acquisition timing, or other disclosed items, preserve that ambiguity rather than forcing a clean confirmation.
- Write a short challenge memo explaining which initial interpretation changed after reading the adverse evidence and which uncertainty remains irreducible from the corpus.

## Phase 5: Quantitative Anchoring

### Objective

Create a reproducible set of calculations that distinguishes company-reported figures from analyst-derived figures, preserves period and scope consistency, and quantifies the acquisition overlay and margin trajectory without overstating precision.

### Expected source files from the manifest

- `press_releases/dash_2026-05-06_8-k.txt`
- `sec_filings/10-q/dash_2026q1_10-q.txt`
- `sec_filings/10-k/dash_2025_10-k.txt`
- `financials/income_statement/dash_income_statement.json`
- `financials/cash_flow/dash_cash_flow.json`
- `financials/balance_sheet/dash_balance_sheet.json`
- `press_releases/dash_2026-02-18_8-k.txt`
- `press_releases/dash_2025-11-05_8-k.txt`
- `press_releases/dash_2025-08-06_8-k.txt`

### Observable trajectory signals

- Create separate table fields for:
  - **Reported figures:** copied from a source with the company’s exact metric label, period, unit, scope, and source path.
  - **Derived figures:** calculated from reported inputs, with the formula, input paths, rounding convention, and any comparability limitation shown.
- Reconcile the latest reported revenue and GAAP earnings to `financials/income_statement/dash_income_statement.json` and the corresponding filed statement. Investigate rather than silently resolve discrepancies.
- Calculate, where compatible inputs exist:
  - Revenue growth = current-period revenue divided by prior-period revenue, less one.
  - GOV growth = current-period GOV divided by prior-period GOV, less one.
  - Net revenue margin = revenue divided by Marketplace GOV.
  - Adjusted EBITDA-to-GOV = adjusted EBITDA divided by Marketplace GOV.
  - GAAP net margin = GAAP net income attributable to the relevant shareholders divided by revenue.
  - Operating cash conversion = operating cash flow divided by the selected earnings measure, with year-to-date and quarterly periods kept separate.
- Preserve company-reported acquisition-excluded growth as reported data. If calculating the percentage-point gap between headline and acquisition-excluded growth, label it a descriptive growth-rate gap rather than a direct estimate of acquired revenue or GOV.
- Build a five-quarter table if the source periods and definitions permit it. Include orders, GOV, revenue, net revenue margin, contribution profit, adjusted EBITDA, adjusted EBITDA-to-GOV, GAAP net income, and relevant reconciliation items.
- Verify whether contribution profit and adjusted EBITDA use the same GOV scope before comparing their margins. If scope differs, present them separately.
- Tie annual profitability context to the annual filings and quarterly inflection claims to quarterly documents; do not mix annual and quarterly figures without labeling the basis.
- Run reasonableness checks for unit scaling, signs, restatements, attributable-income definitions, quarter-versus-year-to-date presentation, and rounding.
- Maintain a calculation sheet in which every derived cell can be traced to reported inputs from exact corpus paths.
- Mark any reconstructed ratio as derived even if it approximates a percentage discussed elsewhere. Mark management projections separately from both historical reported and derived results.

## Phase 6: Synthesis and Position

### Objective

Resolve the conflicting evidence into one explicit, source-grounded position on whether margin improvement is durable while the company expands into new categories and integrates international acquisitions. The conclusion may be conditional, but it cannot remain an evenly balanced survey.

### Expected source files from the manifest

- `press_releases/dash_2026-05-06_8-k.txt`
- `sec_filings/10-q/dash_2026q1_10-q.txt`
- `sec_filings/10-k/dash_2025_10-k.txt`
- `financials/income_statement/dash_income_statement.json`
- `financials/cash_flow/dash_cash_flow.json`
- `financials/balance_sheet/dash_balance_sheet.json`
- Relevant prior-period files used in the completed trend table, including:
  - `press_releases/dash_2026-02-18_8-k.txt`
  - `press_releases/dash_2025-11-05_8-k.txt`
  - `press_releases/dash_2025-08-06_8-k.txt`
  - `sec_filings/10-k/dash_2024_10-k.txt`

### Observable trajectory signals

- Draft one declarative thesis that answers the durability question and identifies the dominant evidence behind it.
- Reconcile, rather than merely juxtapose, the following tensions:
  - Headline growth versus acquisition-excluded growth.
  - Absolute adjusted EBITDA growth versus adjusted EBITDA-to-GOV behavior.
  - Adjusted EBITDA improvement versus GAAP net income and the disclosed reconciliation items.
  - New-category demand and selection gains versus competition and missing standalone unit economics.
  - Advertising monetization potential versus the limits of disclosed evidence about its current economic offset.
  - International demand and acquisition runway versus integration cost, geographic complexity, and profitability risk.
- Explain which metric should carry the most weight and why. For example, if absolute non-GAAP earnings improve while margin ratios or GAAP earnings weaken, determine whether the difference reflects temporary integration effects, structural mix dilution, recurring exclusions, or unresolved disclosure limitations.
- State what is already demonstrated by reported results, what remains a management expectation, and what has been inferred through calculation.
- Include a dedicated ambiguity paragraph for any conclusion that depends on undisclosed category margins, acquisition allocation, advertising economics, or the duration of integration costs.
- Use inline citations to exact corpus paths for every factual statement. Attach citations to the sentence containing the claim rather than relying on a general source list.
- Remove any claim that cannot be traced to a specific file or reproducible calculation from reported inputs.
- End with a clear profitable-scaling verdict, followed by a concise list of corpus-supported indicators that would confirm or invalidate that position in subsequent periods.
- Save the completed, citation-checked synthesis to `/app/answer.txt` only after confirming that all evidence used was available by June 30, 2026.