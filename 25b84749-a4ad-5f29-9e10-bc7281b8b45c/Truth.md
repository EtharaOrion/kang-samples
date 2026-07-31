KANG-TRUTH-SENTINEL: cbae92b7-2b8c-4914-8489-d6280b499a65

## Phase 1: Corpus Reconnaissance

**Objective**

Establish the available evidence set, reporting periods, data schemas, and point-in-time boundary before forming a view. Treat filenames as routing hints only; open the files and verify their dates, entities, units, and contents. Exclude information dated after June 30, 2026 and do not supplement the corpus with external material.

**Expected source files from the manifest**

- Company and peer identification:
  - `company_profiles.json`
- Primary-company financial data:
  - `financials/income_statement/rtx_income_statement.json`
  - `financials/balance_sheet/rtx_balance_sheet.json`
  - `financials/cash_flow/rtx_cash_flow.json`
- Peer financial data:
  - `financials/income_statement/ge_income_statement.json`
  - `financials/income_statement/hon_income_statement.json`
  - `financials/income_statement/lmt_income_statement.json`
  - `financials/cash_flow/ge_cash_flow.json`
  - `financials/cash_flow/hon_cash_flow.json`
  - `financials/cash_flow/lmt_cash_flow.json`
- Annual filings:
  - `sec_filings/10-k/rtx_2023_10-k.txt`
  - `sec_filings/10-k/rtx_2024_10-k.txt`
  - `sec_filings/10-k/rtx_2025_10-k.txt`
- Quarterly filings:
  - `sec_filings/10-q/rtx_2024q2_10-q.txt`
  - `sec_filings/10-q/rtx_2024q3_10-q.txt`
  - `sec_filings/10-q/rtx_2025q1_10-q.txt`
  - `sec_filings/10-q/rtx_2025q2_10-q.txt`
  - `sec_filings/10-q/rtx_2025q3_10-q.txt`
  - `sec_filings/10-q/rtx_2026q1_10-q.txt`
- Company releases:
  - `press_releases/rtx_2025-01-28_8-k.txt`
  - `press_releases/rtx_2025-04-22_8-k.txt`
  - `press_releases/rtx_2025-07-22_8-k.txt`
  - `press_releases/rtx_2025-09-24_8-k.txt`
  - `press_releases/rtx_2025-10-21_8-k.txt`
  - `press_releases/rtx_2025-11-13_8-k.txt`
  - `press_releases/rtx_2026-01-27_8-k.txt`
  - `press_releases/rtx_2026-04-21_8-k.txt`

**Observable trajectory signals**

- A complete inventory confirms that every referenced source path exists and that no unlisted source is used.
- The JSON files are opened to identify fiscal-period keys, units, null-value conventions, quarterly versus year-to-date fields, and whether values are restated.
- Each filing and release is opened far enough to verify its covered period and publication or filing date.
- A source map identifies the 2025 annual filing and Q1 2026 filing as the principal current-period documents, while older filings and releases are retained for chronology and comparison.
- A keyword index is created for terms such as `commercial aftermarket`, `organic sales`, `commercial OEM`, `backlog`, `Powder Metal Matter`, `PW1100`, `accrued liabilities`, `cash impact`, `operating profit`, `operating margin`, `free cash flow`, `appeal`, and `SEC investigation`.
- A cutoff log records June 30, 2026 as the information boundary and confirms that the latest evidence used falls within it.
- No substantive claim is entered into the working notes merely because a filename appears relevant; the surrounding text or structured data is read first.

## Phase 2: Question Decomposition

**Objective**

Convert the broad topic into a decision-oriented issue tree that separates growth composition, accounting recognition, cash realization, segment economics, consolidated financial effects, and competitive context. Define in advance what evidence would support or weaken each possible conclusion.

**Expected source files from the manifest**

- `sec_filings/10-k/rtx_2023_10-k.txt`
- `sec_filings/10-k/rtx_2024_10-k.txt`
- `sec_filings/10-k/rtx_2025_10-k.txt`
- `sec_filings/10-q/rtx_2025q1_10-q.txt`
- `sec_filings/10-q/rtx_2026q1_10-q.txt`
- `press_releases/rtx_2026-01-27_8-k.txt`
- `press_releases/rtx_2026-04-21_8-k.txt`
- `financials/income_statement/rtx_income_statement.json`
- `financials/cash_flow/rtx_cash_flow.json`
- `financials/income_statement/ge_income_statement.json`
- `financials/income_statement/hon_income_statement.json`
- `company_profiles.json`

**Observable trajectory signals**

- A written issue tree separates four questions:
  - Whether commercial aftermarket activity is the principal recent growth source at both Collins Aerospace and Pratt & Whitney, and whether the evidence extends beyond one quarter.
  - Whether the powder-metal matter should be understood as a historical income-statement event, an ongoing cash obligation, or both.
  - Whether Pratt’s margin improvement reflects recurring aftermarket economics or primarily the nonrecurrence of the earlier charge.
  - Whether the resulting consolidated cash, profitability, backlog, and peer position indicate strengthening or only stabilization.
- A period map aligns annual 2023–2025 figures with Q1 2025 and Q1 2026 comparisons, avoiding accidental comparisons between quarterly, year-to-date, and full-year data.
- A definitions sheet distinguishes:
  - Reported sales from organic sales.
  - Commercial aftermarket from commercial OEM activity.
  - Segment operating profit from consolidated operating income.
  - GAAP operating cash flow from company-defined free cash flow.
  - An expense or charge from the later settlement of an accrued liability.
  - Backlog from recognized revenue or cash generation.
- A claim-evidence ledger assigns at least one anticipated source to every factual proposition and leaves unsupported propositions out of scope.
- The planned conclusion is framed as a directional decision with a specified time horizon, not as a list of positives and negatives.

## Phase 3: Evidence Gathering

**Objective**

Build a source-linked factual record for the growth engine, powder-metal obligation, Pratt economics, consolidated cash generation, and peer context. Capture enough surrounding text to preserve management’s stated causality and any qualifications.

**Expected source files from the manifest**

- Aftermarket growth and demand:
  - `sec_filings/10-k/rtx_2025_10-k.txt`
  - `sec_filings/10-q/rtx_2026q1_10-q.txt`
  - `press_releases/rtx_2026-01-27_8-k.txt`
  - `press_releases/rtx_2026-04-21_8-k.txt`
- Powder-metal recognition, accrual, cash payments, and contingencies:
  - `sec_filings/10-k/rtx_2023_10-k.txt`
  - `sec_filings/10-k/rtx_2024_10-k.txt`
  - `sec_filings/10-k/rtx_2025_10-k.txt`
  - `sec_filings/10-q/rtx_2026q1_10-q.txt`
- Segment economics:
  - `sec_filings/10-k/rtx_2025_10-k.txt`
  - `sec_filings/10-q/rtx_2025q1_10-q.txt`
  - `sec_filings/10-q/rtx_2026q1_10-q.txt`
  - `press_releases/rtx_2026-04-21_8-k.txt`
  - `financials/income_statement/rtx_income_statement.json`
- Consolidated cash and peer context:
  - `press_releases/rtx_2026-04-21_8-k.txt`
  - `financials/cash_flow/rtx_cash_flow.json`
  - `financials/income_statement/rtx_income_statement.json`
  - `financials/income_statement/ge_income_statement.json`
  - `financials/income_statement/hon_income_statement.json`
  - `company_profiles.json`

**Observable trajectory signals**

- A segment growth table records, with exact periods and units:
  - Collins’ total organic sales increase and the portion attributed to commercial aftermarket activity.
  - Pratt’s total organic sales increase and the portion attributed to commercial aftermarket activity.
  - Q1 2026 aftermarket growth at both segments.
  - Pratt’s Q1 2026 organic sales bridge, including the direction of commercial OEM activity.
- A demand table records total and commercial backlog at year-end 2024, year-end 2025, and Q1 2026, with explicit warnings that backlog is a demand indicator rather than immediate revenue or cash.
- The powder-metal chronology records:
  - The quarter in which the original charge was recognized.
  - The pre-tax amount, program-share mechanics, after-tax or partner-share presentation, and disclosed EPS effect.
  - The associated accrued-liability increase and subsequent annual reductions from cash payments and customer credits.
  - The remaining accrual and management’s expected 2026 cash effect.
  - The disclosed status of related litigation, appeal activity, and regulatory investigation as of the cutoff.
- A Pratt economics table captures:
  - Annual segment sales, operating profit or loss, and operating margin for 2023, 2024, and 2025.
  - Management’s explanation of how much of the 2024 profit increase came from the absence of the earlier charge.
  - Q1 2025 and Q1 2026 sales, operating profit, and margin.
  - Management’s attribution of current-quarter profit growth to aftermarket volume.
  - Any disclosure that aftermarket mix or GTF-related maintenance burden offsets part of the benefit.
- A consolidated cash table captures Q1 2025 and Q1 2026 operating cash flow, capital expenditures, free cash flow, and the current full-year 2026 free-cash-flow outlook.
- A peer table extracts comparable quarterly revenue, operating income, and net income for RTX, GE, and Honeywell. `company_profiles.json` is read to identify business-mix differences before treating the companies as directly comparable.
- Every extraction includes the exact file path, covered period, units, whether the figure is GAAP or company-adjusted, and enough section context to prevent a search hit from being misinterpreted.
- Discrepancies between a release, filing, and JSON series are recorded rather than silently harmonized.

## Phase 4: Counter-Evidence Engagement

**Objective**

Stress-test the emerging position using the strongest contrary facts in the corpus. Determine whether apparent improvement survives base-effect, mix, cash-timing, legal, and comparability challenges.

**Expected source files from the manifest**

- `sec_filings/10-k/rtx_2023_10-k.txt`
- `sec_filings/10-k/rtx_2024_10-k.txt`
- `sec_filings/10-k/rtx_2025_10-k.txt`
- `sec_filings/10-q/rtx_2025q1_10-q.txt`
- `sec_filings/10-q/rtx_2026q1_10-q.txt`
- `press_releases/rtx_2026-04-21_8-k.txt`
- `financials/income_statement/rtx_income_statement.json`
- `financials/income_statement/ge_income_statement.json`
- `financials/income_statement/hon_income_statement.json`
- `financials/cash_flow/rtx_cash_flow.json`
- `company_profiles.json`

**Observable trajectory signals**

- The 2024 Pratt profit rebound is decomposed so that the nonrecurrence of the 2023 charge is not mistaken for recurring operating leverage.
- Q1 2026 is evaluated as a cleaner comparison period, while acknowledging that one quarter cannot by itself prove durability.
- Higher aftermarket volume is tested against disclosed unfavorable aftermarket mix, particularly where greater GTF service activity may carry powder-metal-related maintenance costs.
- Pratt’s absolute margin level is compared with its own history and current segment growth; a rising margin is not automatically characterized as economically strong.
- The original charge and subsequent cash payments are kept separate. The analysis checks whether current free cash flow already incorporates the expected powder-metal outflow so that the cost is not subtracted twice.
- The decline in the related accrual is examined as evidence of settlement activity, but not automatically treated as a complete measure of all future operational, legal, or regulatory exposure.
- A litigation dismissal is considered alongside any appeal, and the regulatory investigation is checked for unresolved status. Neither a dismissal nor an open investigation is overstated beyond the filing language.
- Backlog growth is challenged for timing, conversion, cancellation, pricing, and mix limitations disclosed in the filings.
- Organic and adjusted measures are reconciled to reported measures where possible, and any unavailable reconciliation is identified as an ambiguity.
- Peer conclusions are constrained by differences in aerospace exposure, defense mix, portfolio structure, and accounting presentation.
- A counter-evidence matrix pairs every favorable inference with its strongest contrary fact and includes a written resolution rather than leaving the conflict as two parallel observations.

## Phase 5: Quantitative Anchoring

**Objective**

Reconstruct the key comparisons with transparent arithmetic, preserve the distinction between company-reported figures and analyst-derived figures, and test internal consistency across documents.

**Expected source files from the manifest**

- `sec_filings/10-k/rtx_2025_10-k.txt`
- `sec_filings/10-q/rtx_2025q1_10-q.txt`
- `sec_filings/10-q/rtx_2026q1_10-q.txt`
- `press_releases/rtx_2026-04-21_8-k.txt`
- `financials/income_statement/rtx_income_statement.json`
- `financials/cash_flow/rtx_cash_flow.json`
- `financials/income_statement/ge_income_statement.json`
- `financials/income_statement/hon_income_statement.json`

**Observable trajectory signals**

- A calculation log labels every item as either **reported** or **derived**.
- Reported items include disclosed organic sales bridges, segment operating margins, backlog, powder-metal charge amounts, accrued-liability balances, expected cash effects, operating cash flow, company-defined free cash flow, and guidance.
- Derived items use visible formulas and source-linked inputs, including:
  - Aftermarket contribution to segment organic growth  
    `commercial aftermarket sales increase ÷ total organic sales increase`
  - Backlog growth  
    `(ending backlog ÷ beginning backlog) − 1`
  - Segment margin cross-check  
    `segment operating profit ÷ segment sales`
  - Year-over-year operating-profit growth  
    `(current-period operating profit ÷ prior-period operating profit) − 1`
  - Arithmetic free cash flow  
    `operating cash flow − capital expenditures`
  - Peer operating margin  
    `operating income ÷ revenue`
  - Peer net margin  
    `net income ÷ revenue`
  - Powder-metal cash burden relative to guidance  
    `expected powder-metal cash effect ÷ midpoint of free-cash-flow guidance`
- Reported segment margins are retained as the primary figures when available; independently calculated margins serve as rounding and transcription checks.
- The annual Pratt margin series is placed beside the Q1 year-over-year comparison, but quarterly margins are not annualized.
- The 2024 profit change is compared with the disclosed nonrecurring charge effect only after confirming that both figures use compatible scope and presentation.
- The powder-metal accrual is reconstructed as a roll-forward using opening balance, cash paid, credits issued, additions or revisions, and closing balance where the filings disclose those components. Any unexplained residual is explicitly retained.
- Company-defined free cash flow from the release is labeled as such. A separately calculated operating-cash-flow-minus-capital-expenditures figure is labeled derived, and differences are investigated rather than forced to zero.
- Cash-flow JSON fields are checked for sign convention and whether quarterly figures are standalone or cumulative.
- Peer comparisons use the same fiscal period and the same reported-versus-adjusted basis. If exact alignment is unavailable, the comparison is narrowed or qualified.
- A final arithmetic audit confirms that percentages, basis-point changes, guidance midpoints, and units can be reproduced from the cited inputs.

## Phase 6: Synthesis and Position

**Objective**

Convert the verified record into a decisive, source-linked investment view. Resolve the tension between aftermarket recovery and the powder-metal burden at the segment and consolidated levels without concealing uncertainty.

**Expected source files from the manifest**

- `sec_filings/10-k/rtx_2025_10-k.txt`
- `sec_filings/10-q/rtx_2026q1_10-q.txt`
- `press_releases/rtx_2026-04-21_8-k.txt`
- `financials/income_statement/rtx_income_statement.json`
- `financials/cash_flow/rtx_cash_flow.json`
- `financials/income_statement/ge_income_statement.json`
- `financials/income_statement/hon_income_statement.json`
- `company_profiles.json`
- Earlier annual and quarterly filings from the manifest where needed to support chronology or explain changes in disclosure.

**Observable trajectory signals**

- The memo opens with a one-sentence position that states whether the commercial-aftermarket recovery outweighs the powder-metal burden over the selected multi-year horizon.
- The written structure proceeds from growth composition, to charge-versus-cash mechanics, to Pratt economics, and finally to consolidated cash and competitive context.
- The synthesis explicitly resolves, rather than merely lists, the following opposing evidence:
  - Aftermarket-led sales growth versus commercial OEM weakness or adverse service mix.
  - A historical accounting charge versus continuing cash payments and credits.
  - A large post-2023 margin rebound versus the base effect created by the charge’s nonrecurrence.
  - Cleaner Q1 2026 operating leverage versus Pratt’s absolute margin level.
  - Improving consolidated free cash flow and backlog versus the remaining cash tail and unresolved legal or regulatory exposure.
  - RTX’s improving trend versus peer profitability and business-mix differences.
- The conclusion identifies which evidence is most decision-relevant and explains why it receives greater weight; it does not default to a neutral summary.
- Every factual clause carries an inline citation to a specific corpus file, using the exact relative path.
- Reported facts and derived calculations remain visibly differentiated in the prose or accompanying tables.
- Ambiguities—such as disclosure-scope differences, non-GAAP definitions, unexplained accrual movements, or imperfect peer comparability—are stated directly rather than smoothed over.
- The final position includes conditions that would invalidate it, such as a reversal in aftermarket growth, failure of backlog conversion, renewed powder-metal cost escalation, weakening cash guidance, or lack of further Pratt margin progress.
- A final source audit removes uncited facts, external assumptions, duplicate citations that do not support the associated claim, and any information beyond the cutoff.