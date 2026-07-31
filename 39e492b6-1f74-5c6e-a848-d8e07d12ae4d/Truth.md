KANG-TRUTH-SENTINEL: 47220698-bd08-4e47-9f4a-8e05e0c1630b

## Phase 1: Corpus Reconnaissance

**Objective**

Establish the available evidence set, reporting periods, company and peer identities, metric coverage, and the June 30, 2026 information cutoff before forming a view. Treat filenames as discovery aids only; verify dates, periods, units, and contents by reading the files.

**Expected source files**

- `company_profiles.json`
- `financials/income_statement/ual_income_statement.json`
- `financials/income_statement/aal_income_statement.json`
- `financials/income_statement/dal_income_statement.json`
- `financials/income_statement/luv_income_statement.json`
- `financials/balance_sheet/ual_balance_sheet.json`
- `financials/cash_flow/ual_cash_flow.json`
- `financials/cash_flow/aal_cash_flow.json`
- `financials/cash_flow/dal_cash_flow.json`
- `financials/cash_flow/luv_cash_flow.json`
- `sec_filings/10-k/ual_2023_10-k.txt`
- `sec_filings/10-k/ual_2024_10-k.txt`
- `sec_filings/10-k/ual_2025_10-k.txt`
- All six quarterly reports in `sec_filings/10-q/`
- All eight files in `press_releases/`, subject to the cutoff

**Observable trajectory signals**

- Enumerate every corpus file and classify it by company, document type, fiscal period, and publication date.
- Read `company_profiles.json` to confirm UAL as the primary company and identify the AAL, DAL, and LUV peer mappings.
- Inspect the JSON schemas and available period labels rather than assuming that the financial files use identical quarterly or annual conventions.
- Open the annual and quarterly filings and locate their financial statements, operating-statistics tables, management discussion, fleet or capacity discussion, loyalty disclosures, and risk factors.
- Build a chronology from 2023 through the first quarter of 2026, flagging any missing quarter or inconsistent comparative period.
- Record that evidence published after June 30, 2026 is excluded; verify release and filing dates from document contents where available.
- Create a source map showing which files appear capable of supporting capacity, unit revenue, product mix, unit cost, margin, and peer comparisons.

## Phase 2: Question Decomposition

**Objective**

Translate the broad durability question into linked tests with explicit definitions and decision criteria. The analysis should determine whether unit revenue and margins remain defensible as capacity expands, not merely describe recent movements.

**Expected source files**

- `sec_filings/10-k/ual_2025_10-k.txt`
- `sec_filings/10-q/ual_2026q1_10-q.txt`
- `financials/income_statement/ual_income_statement.json`
- `financials/income_statement/aal_income_statement.json`
- `financials/income_statement/dal_income_statement.json`
- `financials/income_statement/luv_income_statement.json`
- `company_profiles.json`
- Earlier UAL annual and quarterly filings when needed to standardize definitions or establish a longer baseline

**Observable trajectory signals**

- Construct an issue tree covering:
  - Capacity growth versus PRASM, TRASM, yield, traffic, and load factor.
  - Domestic and international differences rather than relying only on system averages.
  - Premium, ancillary, loyalty, and other operating revenue as potential defenses against pressure in base passenger revenue.
  - CASM, fuel price, labor expense, ex-fuel costs, operating income, and operating margin.
  - UAL’s capacity strategy and industry pricing risk relative to AAL, DAL, and LUV.
- Define each operating metric and identify whether it is directly disclosed or must be reconstructed.
- Separate the time horizons: annual progression through 2025, the latest quarterly inflection, and the implications for future capacity deployment.
- Write competing hypotheses before collecting conclusions:
  - Recent weakness reflects temporary absorption of capacity and should improve when growth moderates.
  - Recent recovery is too short or too dependent on favorable mix to establish durability.
  - Revenue quality can offset capacity pressure.
  - Cost inflation can overwhelm revenue improvement even if unit revenue stabilizes.
- Establish decision tests, including whether revenue per unit improves without an unsustainable load-factor sacrifice, whether non-ticket revenue grows faster than passenger revenue, whether ex-fuel cost control is visible, and whether operating margins compare favorably with peers.
- Create a claim-to-source worksheet in which every prospective factual statement has an identified corpus path or is discarded.

## Phase 3: Evidence Gathering

**Objective**

Extract primary evidence for each analytical test, preserving period, units, definitions, and source location. Prioritize SEC disclosures and financial statements; use press releases as corroboration, management framing, or incremental detail rather than as an unquestioned substitute.

**Expected source files**

- Unit revenue and capacity:
  - `sec_filings/10-k/ual_2025_10-k.txt`
  - `sec_filings/10-q/ual_2026q1_10-q.txt`
  - `financials/income_statement/ual_income_statement.json`
- Premium, ancillary, and loyalty mix:
  - `sec_filings/10-k/ual_2025_10-k.txt`
  - `sec_filings/10-q/ual_2026q1_10-q.txt`
  - `press_releases/ual_2026-01-20_8-k.txt`
  - `press_releases/ual_2026-04-21_8-k.txt`
- Costs and margins:
  - `sec_filings/10-k/ual_2025_10-k.txt`
  - `sec_filings/10-q/ual_2026q1_10-q.txt`
  - `financials/income_statement/ual_income_statement.json`
- Strategy, fleet, and competitive risk:
  - `sec_filings/10-k/ual_2025_10-k.txt`
  - `press_releases/ual_2026-02-02_8-k.txt`
  - `press_releases/ual_2026-02-06_8-k.txt`
  - `press_releases/ual_2026-04-27_8-k.txt`
- Peer benchmarking:
  - `financials/income_statement/aal_income_statement.json`
  - `financials/income_statement/dal_income_statement.json`
  - `financials/income_statement/luv_income_statement.json`
  - `company_profiles.json`
- Historical cross-checks:
  - `sec_filings/10-k/ual_2023_10-k.txt`
  - `sec_filings/10-k/ual_2024_10-k.txt`
  - Relevant files in `sec_filings/10-q/` and `press_releases/`

**Observable trajectory signals**

- Search annual and quarterly filings for `ASM`, `RPM`, `PRASM`, `TRASM`, `yield`, `load factor`, `CASM`, `fuel`, `salary`, `MileagePlus`, `co-brand`, `ancillary`, `premium`, `capacity`, `discount`, and `United Next`.
- Extract annual operating statistics for 2023–2025 and first-quarter statistics for 2025 and 2026 into a period-aligned table.
- Capture systemwide and geographic operating data where available, including domestic, Atlantic, Pacific, and Latin performance.
- Record passenger revenue, other operating revenue, total operating revenue, operating expenses, operating income, and the expense categories needed to interpret margin movement.
- Extract loyalty economics, award-travel participation, ancillary revenue, premium segmentation, and co-brand disclosures without combining differently defined categories.
- Identify management’s stated drivers of capacity, revenue, and cost changes, then distinguish those explanations from the underlying reported data.
- Read the capacity and pricing risk discussion alongside strategic fleet and product disclosures so that expansion plans are not evaluated only through promotional language.
- Pull comparable revenue, operating income, and expense observations for UAL, AAL, DAL, and LUV, while recording differences in fiscal periods and accounting presentation.
- Maintain citations at the row or note level in the evidence table, using the exact relative file path for every extracted item.
- Mark any apparently conflicting disclosures for later resolution instead of silently selecting the more favorable value.

## Phase 4: Counter-Evidence Engagement

**Objective**

Develop the strongest evidence against the emerging interpretation and determine whether it changes, limits, or invalidates the initial hypothesis. Do not present opposing facts as disconnected observations; identify why they conflict and what evidence should receive greater weight.

**Expected source files**

- `sec_filings/10-k/ual_2025_10-k.txt`
- `sec_filings/10-q/ual_2026q1_10-q.txt`
- `financials/income_statement/ual_income_statement.json`
- `financials/income_statement/aal_income_statement.json`
- `financials/income_statement/dal_income_statement.json`
- `financials/income_statement/luv_income_statement.json`
- `company_profiles.json`
- Relevant files in `press_releases/` for management guidance and strategic claims
- Earlier UAL filings where a longer history is needed to test whether the latest period is exceptional

**Observable trajectory signals**

- Build a two-sided evidence matrix around the central tension between full-year unit-revenue pressure during faster capacity deployment and the latest quarterly improvement during more restrained growth.
- Test whether the recent improvement is broad-based across geography, yield, and traffic or is concentrated in a limited region, product, or comparison base.
- Examine whether a lower load factor is consistent with improved pricing quality, indicates unused capacity, or reflects seasonality and period mismatch.
- Challenge the premium-and-loyalty defense by checking its scale relative to total revenue and ASMs, its growth relative to passenger revenue, and whether it supports PRASM, TRASM, or only total dollars.
- Challenge the cost argument by separating fuel effects from labor and other operating expenses and by checking whether absolute cost growth is being obscured by unit-cost presentation.
- Compare UAL’s margin trajectory with peers to test whether apparent strength is company-specific, industrywide, or weaker than the best alternative.
- Confront management’s capacity strategy with the filing’s discussion of industry oversupply and price discounting.
- Record unresolved ambiguities, including noncomparable metric definitions, annual-versus-quarterly seasonality, and missing peer operating statistics.
- Write a short counter-case that could plausibly overturn the preliminary view, followed by a source-based assessment of which parts survive scrutiny.

## Phase 5: Quantitative Anchoring

**Objective**

Create a reproducible numerical bridge from capacity and revenue mix to unit economics and operating margin. Keep disclosed figures separate from analyst calculations, show formulas, and avoid false precision when periods or definitions are not comparable.

**Expected source files**

- `sec_filings/10-k/ual_2025_10-k.txt`
- `sec_filings/10-q/ual_2026q1_10-q.txt`
- `financials/income_statement/ual_income_statement.json`
- `financials/income_statement/aal_income_statement.json`
- `financials/income_statement/dal_income_statement.json`
- `financials/income_statement/luv_income_statement.json`
- `financials/cash_flow/ual_cash_flow.json`
- `financials/balance_sheet/ual_balance_sheet.json`
- `company_profiles.json`

**Observable trajectory signals**

- Create a calculation table with separate columns labeled **reported** and **derived**.
- In the reported section, transcribe disclosed ASMs, RPMs, load factor, yield, PRASM, TRASM, CASM, fuel price, passenger revenue, other operating revenue, total revenue, operating expense, and operating income.
- In the derived section, calculate where inputs and units permit:
  - Capacity growth: current-period ASMs divided by prior-period ASMs, less one.
  - Traffic growth: current-period RPMs divided by prior-period RPMs, less one.
  - Load factor: RPMs divided by ASMs.
  - PRASM: passenger revenue divided by ASMs, with the appropriate cents conversion.
  - TRASM: total operating revenue divided by ASMs, with the appropriate cents conversion.
  - CASM: operating expense divided by ASMs, with the appropriate cents conversion.
  - Operating margin: operating income divided by operating revenue.
  - Revenue and expense growth by line item.
  - Other operating revenue share and its incremental contribution to total revenue growth.
  - Peer operating margins on matched periods.
- Reconcile calculated unit metrics to disclosed metrics and investigate differences caused by rounding, regional operations, special items, or definition changes.
- Build an annual bridge for 2023–2025 and a same-quarter bridge from the first quarter of 2025 to the first quarter of 2026; do not compare a seasonal quarter directly with a full year as if they were equivalent.
- Decompose margin movement into passenger revenue, other revenue, fuel, salaries and related costs, and other operating expenses to test whether revenue gains are outrunning cost inflation.
- Compare reported CASM with an ex-fuel view only if the corpus supplies sufficient inputs or a disclosed measure; label any reconstruction explicitly.
- Use cash flow and balance-sheet files only for relevant context such as investment intensity, liquidity, or financing capacity, and avoid allowing those measures to substitute for operating durability.
- Attach the source path and period to every input cell, retain formula notes for every derived output, and flag calculations that cannot be reproduced from corpus data.

## Phase 6: Synthesis and Position

**Objective**

Resolve the conflicting evidence into one explicit, defensible position on whether UAL’s unit revenue and margin can remain durable as capacity expands. The conclusion may be conditional, but it must identify which mechanism dominates, what evidence supports that judgment, and what would invalidate it.

**Expected source files**

- `sec_filings/10-k/ual_2025_10-k.txt`
- `sec_filings/10-q/ual_2026q1_10-q.txt`
- `financials/income_statement/ual_income_statement.json`
- `financials/income_statement/aal_income_statement.json`
- `financials/income_statement/dal_income_statement.json`
- `financials/income_statement/luv_income_statement.json`
- `company_profiles.json`
- Selected `press_releases/` only where they provide verified strategic or period-specific context
- Earlier UAL filings only where cited for a necessary historical comparison

**Observable trajectory signals**

- Draft a causal chain linking capacity growth to traffic, load factor, yield, PRASM, revenue mix, TRASM, CASM, and operating margin.
- State which interpretation best reconciles the annual deterioration under heavier growth with the latest quarterly recovery under slower growth, rather than merely repeating both observations.
- Decide whether premium, ancillary, and loyalty revenue constitutes a sufficiently large structural defense or only a partial cushion.
- Decide whether cost control is genuinely underlying, primarily fuel-assisted, or threatened by labor and other expense growth.
- Integrate peer evidence into the conclusion by explaining whether UAL’s margin and revenue trajectory is competitively distinctive.
- Characterize the capacity plan as disciplined, conditionally disciplined, or likely to renew unit-revenue pressure, based on observed relationships rather than management intent alone.
- Lead the written synthesis with a clear position, then support it through unit revenue, mix, costs, and competitive capacity in that causal order.
- Address the strongest contrary evidence directly and explain why it changes the confidence level, conditions, or time horizon without leaving the central judgment unresolved.
- Note genuine ambiguity, especially the limited duration of the latest inflection and any metric-definition differences, instead of converting uncertainty into unsupported certainty.
- Inline-cite a specific corpus file for every factual claim, clearly label analyst-derived figures, and remove any assertion that cannot be traced to the permitted evidence set.