KANG-TRUTH-SENTINEL: ca5c6141-be15-45cf-bab1-86d980936c01

## Phase 1: Corpus Reconnaissance

### Objective

Map the available evidence, establish CrowdStrike’s fiscal chronology, and identify which documents can support a post–July 19, 2024 analysis through the June 30, 2026 cutoff. Treat filenames as discovery aids only; verify reporting periods, publication dates, units, and document type from the contents before using them.

### Expected source files from the manifest

- `company_profiles.json`
- `financials/income_statement/crwd_income_statement.json`
- `financials/balance_sheet/crwd_balance_sheet.json`
- `financials/cash_flow/crwd_cash_flow.json`
- All CrowdStrike releases under `press_releases/`, especially:
  - `press_releases/crwd_2025-06-03_8-k.txt`
  - `press_releases/crwd_2025-08-27_8-k.txt`
  - `press_releases/crwd_2025-12-02_8-k.txt`
  - `press_releases/crwd_2026-03-03_8-k.txt`
  - `press_releases/crwd_2026-06-03_8-k.txt`
- `sec_filings/10-k/crwd_2024_10-k.txt`
- `sec_filings/10-k/crwd_2025_10-k.txt`
- `sec_filings/10-k/crwd_2026_10-k.txt`
- All CrowdStrike quarterly filings under `sec_filings/10-q/`
- Peer income-statement and cash-flow files for FTNT, PANW, and ZS, used only if comparability can be established

### Observable trajectory signals

- A corpus inventory grouped by SEC filings, releases, financial statements, balance sheet, and peer data.
- Reads of document headers and fiscal-period descriptions rather than reliance on filenames.
- A timeline linking the July 2024 outage, subsequent quarterly disclosures, the fiscal 2026 annual filing, and Q1 FY27 results.
- Identification of the latest usable evidence as of the cutoff, with later information excluded.
- A fiscal-calendar note that prevents calendar-year and fiscal-year periods from being mixed.
- A source hierarchy that prioritizes SEC disclosures and financial statements for risks and GAAP figures, while using releases for current operating metrics, outlook, and non-GAAP reconciliations.

## Phase 2: Question Decomposition

### Objective

Turn the broad durability question into testable subquestions and define in advance what evidence would confirm or weaken each proposition. Separate growth, customer behavior, profitability quality, and unresolved downside risks while preserving the need for one final conclusion.

### Expected source files from the manifest

- `press_releases/crwd_2026-06-03_8-k.txt`
- `sec_filings/10-k/crwd_2026_10-k.txt`
- `sec_filings/10-k/crwd_2025_10-k.txt`
- Relevant files under `sec_filings/10-q/`
- `financials/income_statement/crwd_income_statement.json`
- `financials/cash_flow/crwd_cash_flow.json`
- `financials/balance_sheet/crwd_balance_sheet.json`

### Observable trajectory signals

- A written question tree covering:
  - Whether revenue, subscription revenue, ARR, and net new ARR have recovered or accelerated after the outage.
  - Whether management’s current outlook confirms or contradicts the recent trajectory.
  - Whether net retention and module expansion reflect genuine customer loyalty or retention purchased through concessions.
  - Whether operating cash generation offsets continuing GAAP losses, and what exclusions create the GAAP/non-GAAP gap.
  - Whether competitive attacks, litigation, regulatory inquiries, or customer remedies could impair future growth or margins.
- An evidence matrix with columns for claim, supporting source, contrary source, reporting date, metric definition, and remaining ambiguity.
- Explicit treatment of ARR, net new ARR, revenue, backlog, and dollar-based net retention as different measures rather than interchangeable indicators.
- A plan to compare pre-outage, immediate post-outage, and latest reported periods where the corpus permits.
- Predefined decision standards for a final position such as resilient, not yet proven, or impaired, rather than an open-ended survey.

## Phase 3: Evidence Gathering

### Objective

Extract the primary evidence needed to establish the operating trajectory, retention quality, profitability profile, and legal or competitive exposure. Record exact file paths beside every factual observation intended for later use.

### Expected source files from the manifest

- Growth and outlook:
  - `press_releases/crwd_2026-06-03_8-k.txt`
  - Earlier CrowdStrike releases under `press_releases/`
  - `financials/income_statement/crwd_income_statement.json`
  - `sec_filings/10-k/crwd_2026_10-k.txt`
- Retention and expansion:
  - `sec_filings/10-k/crwd_2026_10-k.txt`
  - `press_releases/crwd_2026-06-03_8-k.txt`
- Profitability and cash generation:
  - `press_releases/crwd_2026-06-03_8-k.txt`
  - `financials/income_statement/crwd_income_statement.json`
  - `financials/cash_flow/crwd_cash_flow.json`
  - `sec_filings/10-k/crwd_2026_10-k.txt`
- Outage effects, competition, and legal exposure:
  - `sec_filings/10-k/crwd_2025_10-k.txt`
  - `sec_filings/10-k/crwd_2026_10-k.txt`
  - Relevant files under `sec_filings/10-q/`

### Observable trajectory signals

- Extraction of Q1 FY27 total revenue, subscription revenue, ARR, year-over-year growth rates, and the relevant reporting or as-of dates.
- Extraction of Q1 FY27 net new ARR and its year-over-year change, followed by the current full-year net new ARR outlook and any management characterization of acceleration.
- Comparison of the latest growth data with SEC disclosure describing customer purchase deferrals, lost transactions, terminations, or non-renewals associated with the outage.
- Extraction of the most recent disclosed dollar-based net retention rate, preserving its actual measurement date rather than presenting it as a Q1 FY27 metric.
- Reads around customer commitment programs to identify subscription extensions, discounts, promotional modules, or other concessions, including how management says they affect ARR, revenue timing, or retention.
- Extraction of module-adoption tiers and Falcon Flex indicators as evidence of product expansion, with attention to whether the figures describe customer penetration, bookings, or another denominator.
- Extraction of GAAP operating income or margin, non-GAAP operating income or margin, operating cash flow, free cash flow, and revenue for the same quarter.
- Reads of non-GAAP reconciliation tables and filing notes to identify stock-based compensation, outage-related costs, legal reserves, settlements, and other exclusions.
- Extraction of backlog with its measurement date and filing cautions, without treating backlog as equivalent to recognized revenue or ARR.
- Reads of risk factors and legal proceedings for competitor outreach, vendor consolidation pressure, securities cases, derivative actions, consumer claims, and governmental inquiries.
- Inline source-path capture during note-taking so that no final factual assertion depends on memory or an uncited calculation.

## Phase 4: Counter-Evidence Engagement

### Objective

Actively search for the strongest evidence against an initial durability conclusion and determine whether favorable metrics are economically clean, temporarily supported, or contradicted by formal risk disclosures.

### Expected source files from the manifest

- `sec_filings/10-k/crwd_2025_10-k.txt`
- `sec_filings/10-k/crwd_2026_10-k.txt`
- All available files under `sec_filings/10-q/`
- `press_releases/crwd_2026-06-03_8-k.txt`
- Earlier CrowdStrike releases under `press_releases/`
- `financials/income_statement/crwd_income_statement.json`
- `financials/cash_flow/crwd_cash_flow.json`
- `financials/balance_sheet/crwd_balance_sheet.json`

### Observable trajectory signals

- Side-by-side comparison of upbeat operating disclosures with SEC language about purchase disruption, competitive solicitation, customer remedies, litigation, and regulatory scrutiny.
- A chronology showing whether outage-related risk language, legal proceedings, reserves, or customer concessions expanded, narrowed, or remained unresolved across filings.
- Testing whether reported retention could have been supported by contract extensions, discounts, or free functionality, rather than assuming the headline rate is costless.
- Testing whether strong cash generation reflects durable economics or is materially influenced by stock-based compensation, working-capital timing, deferred revenue, or other non-earnings factors.
- Identification of continuing GAAP operating losses even when non-GAAP margins are positive.
- Review of whether backlog offers a meaningful demand cushion while documenting its conversion, cancellation, and timing limitations from the filing.
- Optional peer comparisons only after aligning periods and definitions; peer data should contextualize margins or cash conversion, not substitute for company-specific outage evidence.
- A written counter-case strong enough that the final position must address it directly rather than relegating it to a generic risk paragraph.
- An ambiguity log for items the corpus does not quantify, such as the precise portion of retention attributable to concessions or the eventual cost of unresolved proceedings.

## Phase 5: Quantitative Anchoring

### Objective

Build a reproducible quantitative bridge from reported source data to analytical conclusions. Clearly distinguish company-reported figures from independently derived values and avoid false precision where definitions or periods differ.

### Expected source files from the manifest

- `press_releases/crwd_2026-06-03_8-k.txt`
- Earlier CrowdStrike releases under `press_releases/`
- `financials/income_statement/crwd_income_statement.json`
- `financials/cash_flow/crwd_cash_flow.json`
- `financials/balance_sheet/crwd_balance_sheet.json`
- `sec_filings/10-k/crwd_2026_10-k.txt`
- Relevant files under `sec_filings/10-q/`
- Peer financial files only for definition-aligned comparisons

### Observable trajectory signals

- A calculation table with fields for period, metric, value, unit, source path, source page or section marker, reported versus derived status, and formula.
- Separate rows for revenue, subscription revenue, ARR, net new ARR, dollar-based net retention, backlog, GAAP operating margin, non-GAAP operating margin, operating cash flow, and free cash flow.
- Recalculation of year-over-year revenue and net new ARR growth from current and prior-period values where both are available, while retaining the company-reported rate separately.
- Verification of any guidance midpoint from disclosed range endpoints; if management directly reports a midpoint, preserve that as reported and use a recalculation only as a check.
- Independent free-cash-flow-margin calculation using free cash flow divided by revenue, labeled derived even if it rounds to a figure described elsewhere.
- Reconciliation of company-defined free cash flow to operating cash flow and capital expenditures where the source provides the necessary components.
- Cross-check of GAAP operating margin from GAAP operating income or loss divided by revenue, while keeping the disclosed margin as the primary reported figure.
- A GAAP-to-non-GAAP bridge that identifies each excluded category and does not treat recurring stock-based compensation or legal costs as economically irrelevant merely because they are excluded.
- Correct handling of stock and flow measures: ARR, retention, backlog, and balance-sheet values retain their as-of dates; revenue and cash flow retain their covered periods.
- No unsupported estimate of concession costs, legal exposure, or future conversion of backlog. If the corpus does not quantify an item, describe the direction of risk and state that the magnitude is unavailable.
- Sensitivity checks showing whether the conclusion changes if cash-flow evidence is given less weight because of non-cash compensation or if retention is discounted for customer incentives.

## Phase 6: Synthesis and Position

### Objective

Resolve the conflicting evidence into a direct, defensible view on whether post-outage security growth and customer retention are durable. The conclusion must explain why the selected evidence deserves greater weight, acknowledge what remains unproven, and avoid a merely balanced recitation.

### Expected source files from the manifest

- `press_releases/crwd_2026-06-03_8-k.txt`
- `sec_filings/10-k/crwd_2026_10-k.txt`
- `sec_filings/10-k/crwd_2025_10-k.txt`
- `financials/income_statement/crwd_income_statement.json`
- `financials/cash_flow/crwd_cash_flow.json`
- Relevant historical releases and quarterly filings used in the trajectory analysis

### Observable trajectory signals

- An opening verdict that selects a clear position and states the confidence level.
- A concise evidence chain linking current revenue and ARR performance, net new ARR momentum, forward guidance, retention, expansion behavior, and cash generation.
- Direct treatment of the opposing evidence: customer concessions, continuing GAAP losses, non-GAAP exclusions, competitive exploitation of the outage, and unresolved legal or regulatory matters.
- At least one explicit reconciliation explaining why one body of evidence outweighs the other, rather than listing favorable and unfavorable facts in parallel.
- Separation of demonstrated resilience from unresolved durability: current customer and growth indicators may support one conclusion while future margin quality or legal costs remain less certain.
- Recognition that retention measured at one date and ARR measured at a later date cannot be presented as perfectly contemporaneous.
- A calibrated discussion of backlog as support for demand visibility, accompanied by its limitations.
- A final paragraph identifying the specific future indicators that could overturn the position, such as weakening net new ARR, lower retention, reduced module expansion, increasing concession costs, deteriorating GAAP margins, or escalating legal exposure.
- Inline citation of a specific corpus file for every factual statement, including the inputs to derived calculations.
- Removal of unsupported outside facts, uncited assertions, and claims that exceed the June 30, 2026 information cutoff.