KANG-TRUTH-SENTINEL: e66c9033-1ba4-474c-9eae-d4165583689b

## Phase 1: Corpus Reconnaissance

**Objective**

Establish the available evidence set, its chronology, and its limitations before forming a view. Treat filenames as routing information only: verify reporting periods, publication dates, definitions, and actual contents inside each document. Use no information published after June 30, 2026 and no information outside the manifest.

**Expected source files from the manifest**

- `company_profiles.json`
- `press_releases/ddog_2024-12-12_8-k.txt`
- `press_releases/ddog_2025-02-13_8-k.txt`
- `press_releases/ddog_2025-05-06_8-k.txt`
- `press_releases/ddog_2025-08-07_8-k.txt`
- `press_releases/ddog_2025-11-06_8-k.txt`
- `press_releases/ddog_2026-02-10_8-k.txt`
- `press_releases/ddog_2026-04-22_8-k.txt`
- `press_releases/ddog_2026-05-07_8-k.txt`
- `sec_filings/10-k/ddog_2023_10-k.txt`
- `sec_filings/10-k/ddog_2024_10-k.txt`
- `sec_filings/10-k/ddog_2025_10-k.txt`
- `sec_filings/10-q/ddog_2024q2_10-q.txt`
- `sec_filings/10-q/ddog_2024q3_10-q.txt`
- `sec_filings/10-q/ddog_2025q1_10-q.txt`
- `sec_filings/10-q/ddog_2025q2_10-q.txt`
- `sec_filings/10-q/ddog_2025q3_10-q.txt`
- `sec_filings/10-q/ddog_2026q1_10-q.txt`
- `sec_filings/s-1/ddog_2019_s-1.txt`
- All DDOG and peer files under `financials/`

**Observable trajectory signals**

- Produce an inventory recording each file’s document type, covered period, publication or filing date, company, and intended analytical use.
- Confirm the primary company and peer identities from `company_profiles.json` rather than inferring them solely from ticker-like filenames.
- Read document headers and financial JSON metadata to distinguish quarter-end dates, year-end dates, filing dates, and release dates.
- Establish a source hierarchy: SEC disclosures for business mechanics and risks; current filings and releases for recent operating metrics and outlook; financial JSON for standardized historical calculations.
- Mark the 2019 prospectus and older annual reports as historical context, not current evidence, unless the relevant disclosure is still corroborated by a newer filing.
- Identify duplicate reporting of the same quarter across releases, filings, and financial JSON so later comparisons do not count one observation multiple times.
- Record any document whose internal date or contents would place it beyond the cutoff and exclude it.

## Phase 2: Question Decomposition

**Objective**

Translate the assignment into linked, testable questions and define what evidence would support or weaken a durability conclusion. Set the decision standard before selecting favorable facts.

**Expected source files from the manifest**

- `sec_filings/10-k/ddog_2025_10-k.txt`
- `sec_filings/10-q/ddog_2025q2_10-q.txt`
- `sec_filings/10-q/ddog_2026q1_10-q.txt`
- `press_releases/ddog_2026-02-10_8-k.txt`
- `press_releases/ddog_2026-05-07_8-k.txt`
- `financials/income_statement/ddog_income_statement.json`
- `financials/cash_flow/ddog_cash_flow.json`
- `company_profiles.json`

**Observable trajectory signals**

- Build a question-to-source matrix covering:
  - Whether recent revenue growth and customer expansion are consistent with durable usage growth.
  - How host-based, data-volume, committed, and incremental consumption billing affect expansion and volatility.
  - Whether retention trends demonstrate persistent expansion or conceal customer optimization.
  - Whether growth is broad-based or materially dependent on a small AI-native cohort.
  - How large-customer usage changes, renewal behavior, or pricing concessions could affect future growth.
  - Whether platform breadth and integrations create consolidation advantages relative to point products, internal tools, open-source alternatives, and bundled offerings.
  - Whether GAAP profitability, non-GAAP profitability, operating cash flow, and free cash flow tell materially different stories.
  - Whether current guidance provides a credible near-term test of the durability thesis.
- Define positive indicators, contrary indicators, and possible falsifiers for each question.
- Specify that “durable” requires more than rapid current growth: the final judgment must address concentration, optimization sensitivity, competition, and economic conversion.
- Create a period map preventing figures with different measurement dates from being presented as if contemporaneous.
- Prepare a claim ledger with fields for fact, source path, covered period, reported or derived status, definition, opposing evidence, and confidence.

## Phase 3: Evidence Gathering

**Objective**

Collect primary evidence for operating momentum, usage mechanics, customer concentration, platform breadth, competition, margins, cash generation, and forward expectations. Preserve definitions and dates so every eventual factual statement can receive an exact inline file citation.

**Expected source files from the manifest**

- `press_releases/ddog_2026-05-07_8-k.txt`
- `press_releases/ddog_2026-02-10_8-k.txt`
- `press_releases/ddog_2025-05-06_8-k.txt`
- `press_releases/ddog_2025-08-07_8-k.txt`
- `press_releases/ddog_2025-11-06_8-k.txt`
- `sec_filings/10-k/ddog_2025_10-k.txt`
- `sec_filings/10-k/ddog_2024_10-k.txt`
- `sec_filings/10-q/ddog_2025q2_10-q.txt`
- `sec_filings/10-q/ddog_2025q3_10-q.txt`
- `sec_filings/10-q/ddog_2026q1_10-q.txt`
- `financials/income_statement/ddog_income_statement.json`
- `financials/cash_flow/ddog_cash_flow.json`
- `financials/balance_sheet/ddog_balance_sheet.json`
- `company_profiles.json`
- Peer income-statement and cash-flow JSON files, if used for carefully standardized context

**Observable trajectory signals**

- Read `press_releases/ddog_2026-05-07_8-k.txt` for the latest quarter’s revenue, growth, large-customer data, GAAP and non-GAAP results, cash flow, guidance, and reconciliation definitions.
- Read `sec_filings/10-q/ddog_2026q1_10-q.txt` to corroborate the latest reported period and capture details or caveats omitted from the shorter release.
- Search `sec_filings/10-q/ddog_2025q2_10-q.txt` and adjacent quarterly filings for dollar-based net retention disclosures, exact measurement dates, comparison periods, and management explanations.
- Search `sec_filings/10-k/ddog_2025_10-k.txt` for:
  - Usage-pricing mechanics, commitments, overages, and consumption patterns.
  - Optimization behavior among cloud-native and AI-native customers.
  - Customer concentration, major-customer exposure, cohort growth contribution, and renewal risks.
  - Product architecture, agent deployment, integrations, and product categories.
  - Named competitors, internal and open-source alternatives, bundled or lower-cost products, and differences in competitor resources.
  - Management’s market-opportunity estimate and the categories and forecast year underlying it.
  - Risk disclosures that connect customer behavior or competition to revenue volatility and retention.
- Compare the latest annual filing with `sec_filings/10-k/ddog_2024_10-k.txt` to identify newly added, strengthened, or removed concentration and optimization language.
- Read historical releases and income-statement data to determine whether current growth is an acceleration, normalization, or isolated quarter.
- Read `financials/cash_flow/ddog_cash_flow.json` and the release’s reconciliation before accepting the issuer’s free-cash-flow presentation.
- Use `financials/balance_sheet/ddog_balance_sheet.json` only where liquidity or balance-sheet capacity materially affects the durability judgment.
- Use peer files only after confirming identities and comparable accounting periods. Do not treat the listed peers as proof of direct product competition unless a DDOG filing identifies that relationship.
- Maintain an extraction table with exact path, period, units, metric definition, reported value, surrounding caveat, and intended analytical use.
- Separate issuer assertions, audited or filed facts, management estimates, risk disclosures, and analyst interpretations.

## Phase 4: Counter-Evidence Engagement

**Objective**

Develop the strongest evidence against the emerging position and determine whether it changes the conclusion. Do not place positive and negative facts side by side without explaining their relative importance.

**Expected source files from the manifest**

- `sec_filings/10-k/ddog_2025_10-k.txt`
- `sec_filings/10-k/ddog_2024_10-k.txt`
- `sec_filings/10-q/ddog_2025q2_10-q.txt`
- `sec_filings/10-q/ddog_2026q1_10-q.txt`
- `press_releases/ddog_2026-02-10_8-k.txt`
- `press_releases/ddog_2026-05-07_8-k.txt`
- `financials/income_statement/ddog_income_statement.json`
- `financials/cash_flow/ddog_cash_flow.json`

**Observable trajectory signals**

- Construct a two-sided evidence table rather than collecting only support for the initial view.
- Against a skeptical position, test the force of:
  - Recent revenue growth and any retention improvement.
  - Expansion in the large-customer population.
  - Breadth of products and integrations.
  - Operating cash flow, free cash flow, and forward revenue expectations.
- Against a favorable position, test the force of:
  - Customer optimization inherent in a consumption model.
  - Volatility caused by rapid usage changes or non-renewal.
  - Dependence on a concentrated AI-native cohort or a very large customer.
  - Renewal on less favorable terms.
  - Point products, internal tooling, open-source products, and lower-cost or bundled alternatives.
  - The difference between GAAP and non-GAAP operating performance.
- Compare annual risk language across years to distinguish recurring boilerplate from a newly prominent or more specific operating risk.
- Reconcile metrics with different dates. For example, do not attach an ARR-share disclosure from one quarter to a customer count from another quarter without explicit date labels.
- Treat market-size figures as management estimates, preserving their forecast horizon and category definitions rather than presenting them as realized demand.
- Investigate apparent conflicts by checking definitions, period coverage, and subsequent disclosures before choosing which source controls.
- Maintain an ambiguity log for missing current retention data, cohort-definition changes, unavailable renewal detail, non-comparable margin definitions, or disclosures that cannot be cleanly reconciled.
- Write a short preliminary synthesis stating why the strongest contrary evidence does or does not overturn the developing position.

## Phase 5: Quantitative Anchoring

**Objective**

Validate the narrative with reproducible calculations while clearly separating issuer-reported figures from analyst-derived figures. Use consistent periods, units, and accounting definitions.

**Expected source files from the manifest**

- `press_releases/ddog_2026-05-07_8-k.txt`
- `press_releases/ddog_2026-02-10_8-k.txt`
- `sec_filings/10-q/ddog_2025q2_10-q.txt`
- `sec_filings/10-q/ddog_2026q1_10-q.txt`
- `sec_filings/10-k/ddog_2025_10-k.txt`
- `financials/income_statement/ddog_income_statement.json`
- `financials/cash_flow/ddog_cash_flow.json`
- `financials/balance_sheet/ddog_balance_sheet.json`
- Peer income-statement and cash-flow JSON files if comparability is established

**Observable trajectory signals**

- Create a calculation sheet that identifies every input by file, period, unit, and accounting basis.
- Label as **reported**:
  - Revenue and issuer-stated year-over-year growth.
  - Dollar-based net retention and its stated measurement period.
  - Large-customer counts, thresholds, and ARR share.
  - Any disclosed contribution from the AI-native cohort.
  - GAAP and non-GAAP operating income and margins.
  - Operating cash flow and issuer-defined free cash flow.
  - Quarterly and full-year guidance ranges.
- Label as **derived**:
  - Recomputed year-over-year and sequential revenue growth.
  - Large-customer count growth calculated from disclosed period-end counts.
  - GAAP operating margin recomputed as operating income divided by revenue.
  - Free-cash-flow margin calculated using the disclosed free-cash-flow definition.
  - The absolute and percentage-point difference between GAAP and non-GAAP operating results.
  - Guidance midpoints and implied sequential or year-over-year growth, where comparable prior-period inputs exist.
  - The portion of total growth associated with a disclosed cohort contribution, only when quarter, denominator, and definitions match.
- Reconcile free cash flow to the cash-flow statement using the company’s stated formula; identify rather than conceal any difference caused by classification or definition.
- Cross-check press-release revenue, operating income, and cash-flow figures against the financial JSON and latest quarterly filing.
- Retain reported precision and disclose rounding. Do not manufacture precision from approximate customer, retention, or market-size disclosures.
- If peer comparisons are used, normalize period length, currency, GAAP basis, and metric construction. Exclude comparisons that cannot be made consistently.
- Produce a final quantitative table that includes current performance, relevant historical comparisons, forward guidance, source citations, formulas for derived figures, and explicit data limitations.

## Phase 6: Synthesis and Position

**Objective**

Reach an unambiguous position on whether usage-based growth is durable enough to outweigh optimization, concentration, competition, and profitability risks. Resolve the opposing evidence through a causal argument rather than offering a balanced catalogue.

**Expected source files from the manifest**

- `press_releases/ddog_2026-05-07_8-k.txt`
- `sec_filings/10-k/ddog_2025_10-k.txt`
- `sec_filings/10-q/ddog_2025q2_10-q.txt`
- `sec_filings/10-q/ddog_2026q1_10-q.txt`
- `financials/income_statement/ddog_income_statement.json`
- `financials/cash_flow/ddog_cash_flow.json`
- Any historical DDOG release or filing actually used for a trend comparison

**Observable trajectory signals**

- Begin the written synthesis with a one-sentence directional conclusion, not a neutral summary.
- Organize the reasoning as a causal chain:
  - Usage pricing creates expansion potential but also permits rapid consumption changes.
  - Retention and revenue trends indicate how that mechanism is currently behaving.
  - Customer and cohort evidence determines whether growth is broad or concentrated.
  - Platform breadth determines whether consolidation can offset point-solution and bundled competition.
  - GAAP, non-GAAP, and cash-flow results determine how effectively growth converts into economic value.
  - Guidance defines the next observable test of the conclusion.
- Explicitly explain why retention, growth, and cash generation either outweigh or fail to outweigh optimization exposure, AI-native concentration, thin GAAP profitability, and competitive pressure.
- Give more weight to recent, company-specific, filed evidence than to general market claims, while retaining relevant historical comparisons.
- State unresolved ambiguity directly, especially where dates differ, current retention is unavailable, cohort boundaries are unclear, or non-GAAP reconciliation limits interpretation.
- Distinguish the base conclusion from monitoring conditions. Identify the future disclosures that would confirm or weaken the position, such as retention direction, concentration changes, cohort optimization, guidance delivery, and GAAP margin conversion.
- Inline-cite every factual claim with the exact corpus path that supports it; cite multiple files when a sentence combines independently sourced facts.
- Remove any unsupported number, event, entity, causal assertion, or competitor characterization.
- Complete a final citation audit confirming that each source exists in the manifest, each fact was verified inside the file, all evidence predates the cutoff, reported and derived figures are labeled correctly, and the conclusion genuinely reconciles the strongest opposing evidence.