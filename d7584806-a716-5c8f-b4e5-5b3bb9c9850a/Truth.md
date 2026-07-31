KANG-TRUTH-SENTINEL: aa10d949-805e-4360-86d8-d47d1e9eb9c8
## Phase 1: Corpus Reconnaissance

**Objective**

Establish the available evidence, reporting periods, company and peer identities, document hierarchy, and June 30, 2026 cutoff before forming a view. Open each potentially relevant file and verify its contents rather than inferring relevance from its name.

**Expected source files**

- Identity and peer scope:
  - `company_profiles.json`
- Primary-company financial data:
  - `financials/income_statement/schw_income_statement.json`
  - `financials/balance_sheet/schw_balance_sheet.json`
  - `financials/cash_flow/schw_cash_flow.json`
- Peer financial data:
  - `financials/income_statement/ibkr_income_statement.json`
  - `financials/income_statement/lpla_income_statement.json`
  - `financials/income_statement/ms_income_statement.json`
  - `financials/cash_flow/ibkr_cash_flow.json`
  - `financials/cash_flow/lpla_cash_flow.json`
  - `financials/cash_flow/ms_cash_flow.json`
- Annual history:
  - `sec_filings/10-k/schw_2023_10-k.txt`
  - `sec_filings/10-k/schw_2024_10-k.txt`
  - `sec_filings/10-k/schw_2025_10-k.txt`
- Quarterly history:
  - `sec_filings/10-q/schw_2024q2_10-q.txt`
  - `sec_filings/10-q/schw_2024q3_10-q.txt`
  - `sec_filings/10-q/schw_2025q1_10-q.txt`
  - `sec_filings/10-q/schw_2025q2_10-q.txt`
  - `sec_filings/10-q/schw_2025q3_10-q.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
- Releases through the cutoff:
  - `press_releases/schw_2025-11-14_8-k.txt`
  - `press_releases/schw_2026-01-21_8-k.txt`
  - `press_releases/schw_2026-01-29_8-k.txt`
  - `press_releases/schw_2026-03-02_8-k.txt`
  - `press_releases/schw_2026-04-16_8-k.txt`
  - `press_releases/schw_2026-04-22_8-k.txt`
  - `press_releases/schw_2026-05-21_8-k.txt`
  - `press_releases/schw_2026-06-29_8-k.txt`

**Observable trajectory signals**

- An inventory records each file’s document type, covered period, publication date, company, units, and verified relevance.
- The analyst opens the profile and financial JSON files to identify ticker mappings, field names, period conventions, null values, and whether figures are quarterly, year-to-date, or annual.
- The analyst reads the filings’ business, risk, MD&A, liquidity, capital, net-interest, deposit, borrowing, and client-metric sections.
- Releases are opened and classified by actual content; irrelevant releases are documented as reviewed but are not cited as evidence.
- A source hierarchy is established: audited annual filing for full-year history, quarterly filing for the latest detailed period, contemporaneous release for incremental operating data, and standardized financial files for cross-checks and peer comparisons.
- Duplicate disclosures are identified so a press-release figure is not mistakenly treated as independent confirmation of the same filing figure.
- All candidate evidence is checked against the June 30, 2026 cutoff, and no outside data is introduced.

## Phase 2: Question Decomposition

**Objective**

Convert the broad topic into a decision-oriented research tree that separates historical causation, current trajectory, remaining earnings runway, and balance-sheet constraints.

**Expected source files**

- Core historical and current disclosures:
  - `sec_filings/10-k/schw_2023_10-k.txt`
  - `sec_filings/10-k/schw_2024_10-k.txt`
  - `sec_filings/10-k/schw_2025_10-k.txt`
  - `sec_filings/10-q/schw_2025q1_10-q.txt`
  - `sec_filings/10-q/schw_2025q2_10-q.txt`
  - `sec_filings/10-q/schw_2025q3_10-q.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
- Latest operating updates:
  - `press_releases/schw_2026-01-21_8-k.txt`
  - `press_releases/schw_2026-04-16_8-k.txt`
  - Other release files only after their contents are verified as relevant
- Financial cross-checks:
  - `financials/income_statement/schw_income_statement.json`
  - `financials/balance_sheet/schw_balance_sheet.json`
  - `financials/cash_flow/schw_cash_flow.json`
  - `financials/income_statement/ibkr_income_statement.json`
  - `financials/income_statement/lpla_income_statement.json`
  - `financials/income_statement/ms_income_statement.json`

**Observable trajectory signals**

- A written question matrix separates:
  1. The original client-cash reallocation episode from the subsequent deposit recovery.
  2. Organic sweep growth from contractual or administrative transfers onto the balance sheet.
  3. Net interest revenue growth from margin expansion, balance growth, funding-cost relief, lending growth, and asset-yield pressure.
  4. The historical supplemental-funding paydown from the smaller amount of paydown still available.
  5. Client-asset growth from market appreciation, planned client departures, and true net new assets.
  6. Margin-loan expansion from sweep-funded balance-sheet growth.
  7. Capital distributions from changes in reported and AOCI-sensitive leverage measures.
  8. Company-specific recovery from a funding-cycle effect also visible at peers.
- Each question has a provisional hypothesis, a disconfirming test, required periods, required metrics, and likely source paths.
- Definitions are flagged for verification, including transactional sweep cash, bank sweep deposits, brokerage-client payables, bank deposit account balances, supplemental funding, net interest margin, net interest revenue, core net new assets, and leverage ratios.
- The plan explicitly distinguishes stock measures at period-end from flow measures over a quarter or year and average-balance measures used in margin calculations.
- The analyst identifies in advance which conflicts require reconciliation rather than side-by-side reporting.

## Phase 3: Evidence Gathering

**Objective**

Build a citation-ready evidence ledger that traces the deposit arc, net-interest mechanics, funding substitution, lending growth, organic growth, and capital deployment across comparable periods.

**Expected source files**

- For the client-cash history and subsequent deposit turn:
  - `sec_filings/10-k/schw_2023_10-k.txt`
  - `sec_filings/10-k/schw_2024_10-k.txt`
  - `sec_filings/10-k/schw_2025_10-k.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
  - `press_releases/schw_2026-04-16_8-k.txt`
  - Verified relevant portions, if any, of `press_releases/schw_2026-05-21_8-k.txt` and `press_releases/schw_2026-06-29_8-k.txt`
- For net interest revenue and margin:
  - `sec_filings/10-k/schw_2025_10-k.txt`
  - `sec_filings/10-q/schw_2025q1_10-q.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
  - `press_releases/schw_2026-01-21_8-k.txt`
  - `press_releases/schw_2026-04-16_8-k.txt`
  - `financials/income_statement/schw_income_statement.json`
- For supplemental funding and liquidity:
  - `sec_filings/10-k/schw_2023_10-k.txt`
  - `sec_filings/10-k/schw_2024_10-k.txt`
  - `sec_filings/10-k/schw_2025_10-k.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
  - `financials/balance_sheet/schw_balance_sheet.json`
  - `financials/cash_flow/schw_cash_flow.json`
- For growth, lending, and capital deployment:
  - `sec_filings/10-k/schw_2025_10-k.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
  - `press_releases/schw_2026-01-21_8-k.txt`
  - `press_releases/schw_2026-04-16_8-k.txt`
  - `financials/balance_sheet/schw_balance_sheet.json`
  - `financials/cash_flow/schw_cash_flow.json`
- For peer context:
  - `company_profiles.json`
  - `financials/income_statement/ibkr_income_statement.json`
  - `financials/income_statement/lpla_income_statement.json`
  - `financials/income_statement/ms_income_statement.json`
  - The associated peer cash-flow files where they contain a genuinely comparable measure

**Observable trajectory signals**

- Targeted searches are run for cash sorting, sweep, transactional cash, money market funds, fixed income, brokerage-client payables, deposit arrangements, balance transfers, supplemental funding, FHLB, brokered certificates, repurchase agreements, margin loans, net interest revenue, net interest margin, floating-rate assets, capital ratios, dividends, preferred stock, and repurchases.
- The ledger captures, for every usable fact:
  - Exact file path
  - Covered period
  - Table or section context
  - Units
  - Whether the figure is an ending balance, average balance, quarterly flow, year-to-date flow, or annual flow
  - Whether management describes a causal driver or the analyst is inferring one
- Historical filings are used to document why client cash left low-yield sweep products and how that affected funding, rather than starting the narrative only after recovery began.
- The 2025 annual filing is read for both the combined deposit increase and any contractual balance-transfer mechanism; these are recorded separately to avoid labeling transferred balances as entirely organic.
- The latest quarterly filing and operating release are read for the post-year-end deposit pace, funding composition, margin lending, net interest revenue, net interest margin, client assets, net new assets, repurchases, dividends, and leverage.
- Net interest tables are extracted at sufficient detail to separate asset yields, funding rates, average balances, and the effects of lending growth.
- Supplemental funding is captured by component and maturity where disclosed, not merely as an aggregate.
- Capital distributions are reconciled among financing cash flows, equity notes, capital-management discussion, and releases.
- Peer comparisons use identical line items and matching periods. If business models or accounting classifications make a comparison unreliable, that limitation is recorded rather than forced.
- Every prospective factual sentence in the eventual analysis has at least one specific file path attached before drafting begins.

## Phase 4: Counter-Evidence Engagement

**Objective**

Stress-test the favorable recovery case with the strongest evidence that deposit growth may be less durable, margin gains may decelerate, funding relief may be nearly exhausted, or growth and distributions may strain the balance sheet.

**Expected source files**

- Risk, rate sensitivity, and liquidity discussion:
  - `sec_filings/10-k/schw_2025_10-k.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
- Historical comparisons:
  - `sec_filings/10-k/schw_2023_10-k.txt`
  - `sec_filings/10-k/schw_2024_10-k.txt`
  - `sec_filings/10-q/schw_2025q1_10-q.txt`
- Current operating evidence:
  - `press_releases/schw_2026-01-21_8-k.txt`
  - `press_releases/schw_2026-04-16_8-k.txt`
  - Later pre-cutoff releases only if verified as relevant
- Balance-sheet and capital cross-checks:
  - `financials/balance_sheet/schw_balance_sheet.json`
  - `financials/cash_flow/schw_cash_flow.json`
- Peer-cycle checks:
  - `financials/income_statement/ibkr_income_statement.json`
  - `financials/income_statement/lpla_income_statement.json`
  - `financials/income_statement/ms_income_statement.json`

**Observable trajectory signals**

- A counter-evidence table pairs every major positive claim with a test that could weaken it and records the final disposition.
- Deposit durability is tested by comparing the latest quarterly increase with the prior full-year pace, while noting seasonality, measurement differences, and the contribution of balance transfers.
- The analyst distinguishes a reversal in client behavior from a one-time contractual ability to place more balances on the company’s own balance sheet.
- Rate sensitivity is examined in both directions: lower short-term rates may reduce expensive funding costs, but they may also reduce floating-rate asset yields and related fee revenue.
- Continued net interest margin expansion is compared with the change in net interest revenue growth, preventing a rising margin from being treated as proof of unchanged earnings momentum.
- The remaining supplemental-funding balance is compared with its historical size. The analyst tests whether prior funding-cost relief can recur at a similar scale.
- Margin-loan growth is compared with sweep funding growth and wholesale borrowing. This tests whether a new earning-asset opportunity could rebuild dependence on costly funding.
- Capital returns are compared with balance-sheet expansion and both reported and AOCI-sensitive leverage measures. Divergent leverage signals are explained rather than selecting only the favorable measure.
- Client-asset growth is separated from market effects, and planned client departures are isolated from underlying organic gathering.
- Peer net interest growth is used to test whether the observed recovery is entirely company-specific or partly reflects a broader funding and rate cycle.
- Conflicting figures are resolved by checking definitions, period endpoints, rounding, consolidation level, and whether the source reports an average or ending balance.
- Any unresolved discrepancy is retained in an ambiguity log and carried into the final conclusion.

## Phase 5: Quantitative Anchoring

**Objective**

Create an auditable model of the recovery and its constraints, labeling every figure as reported or derived and avoiding mismatched periods or definitions.

**Expected source files**

- Primary reported figures:
  - `sec_filings/10-k/schw_2023_10-k.txt`
  - `sec_filings/10-k/schw_2024_10-k.txt`
  - `sec_filings/10-k/schw_2025_10-k.txt`
  - `sec_filings/10-q/schw_2025q1_10-q.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
  - `press_releases/schw_2026-01-21_8-k.txt`
  - `press_releases/schw_2026-04-16_8-k.txt`
- Financial-statement validation:
  - `financials/income_statement/schw_income_statement.json`
  - `financials/balance_sheet/schw_balance_sheet.json`
  - `financials/cash_flow/schw_cash_flow.json`
- Peer calculations:
  - `financials/income_statement/ibkr_income_statement.json`
  - `financials/income_statement/lpla_income_statement.json`
  - `financials/income_statement/ms_income_statement.json`

**Observable trajectory signals**

- A model contains a **Reported** section populated directly from source tables or narrative disclosures:
  - Sweep and brokerage-client cash balances
  - Balance-transfer amounts
  - Net interest revenue and net interest margin
  - Average interest-earning assets and funding balances
  - Funding rates and asset yields
  - Supplemental-funding components
  - Margin loans
  - Core net new assets and total client assets
  - Repurchases, dividends, preferred redemptions, and total capital distributions
  - Reported and adjusted leverage measures
- A separate **Derived** section shows formulas and input citations for:
  - Year-over-year and quarter-over-quarter changes
  - Basis-point changes in net interest margin
  - The average quarterly deposit increase implied by a full-year change
  - The latest quarter’s deposit pace relative to that benchmark
  - The percentage reduction in supplemental funding and the residual amount still available for paydown
  - Net interest revenue growth-rate deceleration across comparable periods
  - Margin-loan growth relative to deposit growth
  - Net new assets before and after identified planned departures
  - Client-asset changes net of disclosed flow effects where the corpus permits
  - Capital distributions relative to earnings, cash generation, or balance-sheet growth
  - Changes in each leverage measure
  - Comparable peer net interest growth
- Derived figures retain the underlying file paths and formulas; they are never presented as company-reported values.
- Rounded narrative figures are reconciled to detailed tables. Material conclusions use the more precise table values where definitions match.
- Calculations do not annualize a single quarter without clearly labeling the result as an analytical run rate rather than guidance.
- Ending balances are not divided by quarterly income without an explicit rationale; average balances are preferred for spread and margin analysis.
- A funding bridge traces, to the extent disclosed, how deposit inflows, securities cash flows, balance transfers, earnings, and wholesale borrowing relate to supplemental-funding paydown and loan growth.
- A sensitivity frame identifies what further net interest improvement would require once the prior funding substitution has largely occurred. Inputs are limited to relationships disclosed or calculable from the corpus; unsupported macro forecasts are excluded.
- All arithmetic is independently recomputed, with discrepancies traced to rounding, units, period conventions, or classification differences.

## Phase 6: Synthesis and Position

**Objective**

Resolve the opposing evidence into a clear investment-oriented position on the durability of the deposit recovery, the remaining net-interest earnings runway, and the sustainability of simultaneous balance-sheet growth and capital return. The result should be a thesis, not an undecided catalogue of positives and negatives.

**Expected source files**

- Principal synthesis sources:
  - `sec_filings/10-k/schw_2025_10-k.txt`
  - `sec_filings/10-q/schw_2026q1_10-q.txt`
  - `press_releases/schw_2026-01-21_8-k.txt`
  - `press_releases/schw_2026-04-16_8-k.txt`
  - `financials/income_statement/schw_income_statement.json`
  - `financials/balance_sheet/schw_balance_sheet.json`
  - `financials/cash_flow/schw_cash_flow.json`
- Historical and peer files used only where they support a specific comparison:
  - `sec_filings/10-k/schw_2023_10-k.txt`
  - `sec_filings/10-k/schw_2024_10-k.txt`
  - Relevant quarterly filings in the manifest
  - `financials/income_statement/ibkr_income_statement.json`
  - `financials/income_statement/lpla_income_statement.json`
  - `financials/income_statement/ms_income_statement.json`
  - Verified relevant releases through June 30, 2026

**Observable trajectory signals**

- The draft opens with a one-sentence position that states whether the recovery is durable, how much of the margin improvement is repeatable, and what constrains the next stage.
- The written analysis follows a causal sequence:
  1. Explain the earlier client-cash reallocation and funding consequences.
  2. Establish the later deposit turn while separating organic inflows from transferred balances.
  3. Decompose the net-interest recovery into funding-cost relief, lending growth, asset yields, and balance changes.
  4. Explain why the historical funding paydown was powerful and assess how much of that lever remains.
  5. Evaluate whether organic asset gathering and margin lending can replace the fading funding benefit.
  6. Reconcile capital distributions with balance-sheet growth and the direction of leverage measures.
- Each section contains a supported claim, the strongest opposing evidence, and an explicit resolution explaining which evidence carries greater weight and why.
- The conclusion does not infer that prior margin expansion will continue merely because deposits are rising. It identifies the operating conditions needed for further improvement and the evidence that would invalidate the position.
- The treatment of capital return reaches a definite judgment about sustainability after considering earnings, cash generation, lending growth, funding needs, and both leverage presentations.
- Peer evidence is used as context, not as a substitute for company-specific analysis.
- Ambiguities involving definitions, seasonality, transfer effects, adjusted measures, or limited quarterly history are stated directly and reflected in confidence levels.
- Every numerical, event, entity, and causal claim has an inline citation to a specific corpus file. Derived claims identify their cited inputs.
- The final pass removes unsupported assertions, checks all citations against the cited files, confirms compliance with the cutoff, and verifies that the conclusion reconciles rather than merely juxtaposes the conflicting evidence.