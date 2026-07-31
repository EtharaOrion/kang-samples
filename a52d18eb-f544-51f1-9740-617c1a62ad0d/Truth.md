KANG-TRUTH-SENTINEL: cecb9e94-1f12-479b-a60c-fb0cd965df48

## Phase 1: Corpus Reconnaissance

### Objective

Establish the available evidence set, its reporting periods, file structures, and limitations before forming a view. Enforce the June 30, 2026 cutoff based on dates and periods stated inside each document, not merely its filename. Treat file names as routing clues only; no factual claim should be recorded until the underlying text or structured data has been inspected.

### Expected source files from the manifest

- Current primary filings:
  - `sec_filings/10-k/dpz_2025_10-k.txt`
  - `sec_filings/10-q/dpz_2026q1_10-q.txt`
- Historical filings for comparable-period and trend checks:
  - `sec_filings/10-k/dpz_2023_10-k.txt`
  - `sec_filings/10-k/dpz_2024_10-k.txt`
  - `sec_filings/10-q/dpz_2024q2_10-q.txt`
  - `sec_filings/10-q/dpz_2024q3_10-q.txt`
  - `sec_filings/10-q/dpz_2025q1_10-q.txt`
  - `sec_filings/10-q/dpz_2025q2_10-q.txt`
  - `sec_filings/10-q/dpz_2025q3_10-q.txt`
- Press-release and furnished-result candidates:
  - `press_releases/dpz_2025-07-21_8-k.txt`
  - `press_releases/dpz_2025-08-06_8-k.txt`
  - `press_releases/dpz_2025-08-13_8-k.txt`
  - `press_releases/dpz_2025-09-08_8-k.txt`
  - `press_releases/dpz_2025-10-14_8-k.txt`
  - `press_releases/dpz_2026-02-23_8-k.txt`
  - `press_releases/dpz_2026-04-27_8-k.txt`
  - `press_releases/dpz_2026-06-22_8-k.txt`
- Primary-company financial data:
  - `financials/income_statement/dpz_income_statement.json`
  - `financials/balance_sheet/dpz_balance_sheet.json`
  - `financials/cash_flow/dpz_cash_flow.json`
- Peer financial data:
  - `financials/income_statement/yum_income_statement.json`
  - `financials/income_statement/qsr_income_statement.json`
  - `financials/income_statement/wing_income_statement.json`
  - `financials/cash_flow/yum_cash_flow.json`
  - `financials/cash_flow/qsr_cash_flow.json`
  - `financials/cash_flow/wing_cash_flow.json`
- Entity and peer mapping:
  - `company_profiles.json`
- Long-dated business-model context, used only if still relevant and clearly identified as historical:
  - `sec_filings/s-1/dpz_2004_s-1.txt`

### Observable trajectory signals

- A complete file inventory is matched against the manifest, with missing, unreadable, or malformed files noted.
- Each text document is opened to verify the company, form, filing or event date, fiscal period, and whether exhibits contain the operating release.
- Each JSON file is parsed to identify field names, period ordering, units, null conventions, restatements, and whether values are quarterly, year-to-date, or annual.
- A source ledger is created with exact path, period, section or search locator, metric definition, and intended analytical use.
- The current annual filing and latest quarterly filing are read before older documents.
- No post-cutoff information is introduced, and the date inside each candidate document is checked against June 30, 2026.
- The 2004 prospectus is classified as historical context rather than evidence of current operations unless a current filing independently confirms the relevant feature.

## Phase 2: Question Decomposition

### Objective

Turn the broad assignment into testable questions that distinguish sales momentum, unit expansion, channel quality, and economic translation. Define in advance what evidence would strengthen or weaken durability, so the research does not become a collection of favorable management statements.

The decomposition should cover four linked inquiries:

1. Determine whether domestic comparable sales are improving on a genuinely stronger demand base while international comparable sales weaken, including the effects of prior-year comparisons, currency conventions, transaction counts, average ticket, and product activity.
2. Determine whether net unit expansion is durable after openings, closures, geographic mix, market densification, possible cannibalization, franchisee economics, and dependence on international master franchisees are considered.
3. Determine whether third-party ordering, loyalty, carryout, and delivery are creating repeatable demand or merely adding volume with weaker store-level economics.
4. Determine whether retail-sales growth translates into royalties, advertising activity, supply-chain revenue, earnings, and cash generation, and whether available peer data corroborates or challenges claims of competitive strength.

### Expected source files from the manifest

- Core question definition and terminology:
  - `sec_filings/10-k/dpz_2025_10-k.txt`
  - `sec_filings/10-q/dpz_2026q1_10-q.txt`
- Comparable-period construction:
  - `sec_filings/10-k/dpz_2023_10-k.txt`
  - `sec_filings/10-k/dpz_2024_10-k.txt`
  - `sec_filings/10-q/dpz_2025q1_10-q.txt`
  - `sec_filings/10-q/dpz_2025q2_10-q.txt`
  - `sec_filings/10-q/dpz_2025q3_10-q.txt`
- Result announcements and strategy updates, subject to internal verification:
  - `press_releases/dpz_2025-07-21_8-k.txt`
  - `press_releases/dpz_2025-10-14_8-k.txt`
  - `press_releases/dpz_2026-02-23_8-k.txt`
  - `press_releases/dpz_2026-04-27_8-k.txt`
  - `press_releases/dpz_2026-06-22_8-k.txt`
- Financial translation and competitive comparison:
  - `financials/income_statement/dpz_income_statement.json`
  - `financials/cash_flow/dpz_cash_flow.json`
  - `financials/balance_sheet/dpz_balance_sheet.json`
  - `financials/income_statement/yum_income_statement.json`
  - `financials/income_statement/qsr_income_statement.json`
  - `financials/income_statement/wing_income_statement.json`
  - `financials/cash_flow/yum_cash_flow.json`
  - `financials/cash_flow/qsr_cash_flow.json`
  - `financials/cash_flow/wing_cash_flow.json`
  - `company_profiles.json`

### Observable trajectory signals

- A question-to-evidence matrix is written before extraction, with a base hypothesis, an opposing hypothesis, required metrics, and likely source paths for each inquiry.
- Same-store sales, retail sales, company revenue, franchise revenue, supply-chain revenue, orders, transactions, ticket, gross openings, closures, and net openings are defined separately.
- Period conventions are fixed: annual figures are not mixed with quarterly figures without explicit labeling, and year-to-date values are not treated as standalone-quarter values.
- Domestic and international figures are kept separate, including any stated foreign-currency treatment.
- A rollover schedule is planned so current comparable sales can be interpreted against the appropriate prior-year base.
- The unit analysis explicitly separates gross openings from closures and net additions, as well as domestic from international expansion.
- The channel analysis predefines the distinction between demand generation and profitability.
- Peer comparisons are limited to metrics that are sufficiently comparable after reviewing business mix, fiscal calendars, and reporting definitions in `company_profiles.json` and the financial JSON files.

## Phase 3: Evidence Gathering

### Objective

Build a traceable evidence base from primary filings, verified result announcements, and structured financial data. Capture both figures and explanatory language with enough context to preserve definitions, period boundaries, and management qualifications. Likely paths guide the search, but every extracted fact must be confirmed inside the file.

### Expected source files from the manifest

#### Comparable-sales trajectory and drivers

- `sec_filings/10-k/dpz_2025_10-k.txt`
- `sec_filings/10-q/dpz_2026q1_10-q.txt`
- `sec_filings/10-k/dpz_2024_10-k.txt`
- `sec_filings/10-q/dpz_2025q1_10-q.txt`
- `press_releases/dpz_2026-02-23_8-k.txt`
- `press_releases/dpz_2026-04-27_8-k.txt`

Search for and verify passages concerning same-store sales, foreign-currency exclusions, domestic and international results, prior-year comparisons, customer transactions, average ticket, order counts, pricing, and named product launches. Record whether each driver is quantified, described qualitatively, or presented as management attribution.

#### Unit expansion, market densification, and franchise dependence

- `sec_filings/10-k/dpz_2025_10-k.txt`
- `sec_filings/10-q/dpz_2026q1_10-q.txt`
- `sec_filings/10-k/dpz_2024_10-k.txt`
- `press_releases/dpz_2026-02-23_8-k.txt`
- `press_releases/dpz_2026-04-27_8-k.txt`
- Other manifest press releases only when inspection confirms relevant unit or franchise information

Search for store counts, openings, closures, net growth, geographic mix, fortressing, cannibalization, closure risk, franchise development obligations, master-franchise arrangements, China exposure, DPC Dash, equity investments, and capital commitments. Separate disclosed facts from analytical implications such as the effect of weakening store economics on future development.

#### Ordering channels, loyalty, and sales strategy

- `sec_filings/10-k/dpz_2025_10-k.txt`
- `sec_filings/10-q/dpz_2026q1_10-q.txt`
- Relevant press releases after confirming their contents

Search for Hungry for MORE, third-party order aggregation, Uber, DoorDash, rewards or loyalty, active members, carryout, delivery, order counts, customer acquisition, owned digital channels, commissions, fees, and store-level profitability. Establish agreement scope and timing before attributing any reported sales result to a channel.

#### Revenue mechanics and competitive context

- `sec_filings/10-k/dpz_2025_10-k.txt`
- `sec_filings/10-q/dpz_2026q1_10-q.txt`
- `financials/income_statement/dpz_income_statement.json`
- `financials/cash_flow/dpz_cash_flow.json`
- `financials/balance_sheet/dpz_balance_sheet.json`
- `financials/income_statement/yum_income_statement.json`
- `financials/income_statement/qsr_income_statement.json`
- `financials/income_statement/wing_income_statement.json`
- `financials/cash_flow/yum_cash_flow.json`
- `financials/cash_flow/qsr_cash_flow.json`
- `financials/cash_flow/wing_cash_flow.json`
- `company_profiles.json`
- Verified result announcements in `press_releases/`

Search the filings for royalty mechanics, advertising contributions, supply-chain revenue, food-basket pricing, franchisee profitability, market share, named competitors, and competition from ordering and delivery platforms. Use the JSON files to test whether reported retail-sales momentum is accompanied by revenue, operating-income, and cash-flow progression.

### Observable trajectory signals

- Searches are run across both the annual and quarterly filings using related terms rather than a single keyword.
- Every material extraction records:
  - Exact file path
  - Fiscal period and geography
  - Metric definition and currency treatment
  - Reported value or qualitative statement
  - Nearby qualification or risk language
  - Whether the evidence is company-reported, management interpretation, or analyst-derived
- Annual comparable-sales figures are placed beside the latest quarterly result and the applicable prior-year quarterly base.
- Domestic drivers are disaggregated into transactions and ticket where the source permits; product activity is not credited as a driver unless the source makes that connection.
- Store tables are transcribed by geography and reconciled from beginning count through openings, closures, transfers if any, and ending count.
- Disclosures about fortressing are read in both strategy and risk contexts.
- Master-franchise and investment disclosures are connected only after confirming the entity, geography, ownership nature, and relevant period.
- Aggregator agreements are mapped by partner, geography, launch timing, order ownership, and any disclosed profitability limitation.
- Owned-channel, loyalty, carryout, and delivery evidence is collected as potential offsets rather than assumed to neutralize aggregator economics.
- Financial-statement values are cross-checked against the corresponding filing or result announcement where possible.
- Each eventual factual sentence has an exact-file citation prepared; directory-level citations are replaced by the specific press-release file actually used.

## Phase 4: Counter-Evidence Engagement

### Objective

Stress-test the emerging thesis with the strongest contrary evidence available in the corpus. Distinguish a persuasive durability case from one that depends on selective periods, management framing, favorable comparisons, price rather than traffic, or unit additions that may weaken existing-store economics.

### Expected source files from the manifest

- Risk factors, operating commentary, and strategy limitations:
  - `sec_filings/10-k/dpz_2025_10-k.txt`
  - `sec_filings/10-q/dpz_2026q1_10-q.txt`
  - `sec_filings/10-k/dpz_2024_10-k.txt`
- Prior-period comparisons:
  - `sec_filings/10-q/dpz_2025q1_10-q.txt`
  - `sec_filings/10-q/dpz_2025q2_10-q.txt`
  - `sec_filings/10-q/dpz_2025q3_10-q.txt`
  - `sec_filings/10-k/dpz_2023_10-k.txt`
- Management announcements requiring comparison with filed disclosures:
  - `press_releases/dpz_2026-02-23_8-k.txt`
  - `press_releases/dpz_2026-04-27_8-k.txt`
  - Any other manifest press release whose contents are verified as relevant
- Financial corroboration:
  - `financials/income_statement/dpz_income_statement.json`
  - `financials/cash_flow/dpz_cash_flow.json`
  - `financials/balance_sheet/dpz_balance_sheet.json`
  - All listed peer income-statement and cash-flow JSON files
  - `company_profiles.json`

### Observable trajectory signals

- A two-sided evidence table pairs every major positive claim with the most direct contrary observation from a specific file.
- Domestic improvement is tested against:
  - The magnitude and source of the comp
  - The prior-year comparison
  - International deceleration
  - Whether price, ticket, transactions, and product activity are separately supported
- Unit durability is tested against:
  - Closures and gross-versus-net presentation
  - International concentration of additions
  - Cannibalization or existing-store sales pressure from market densification
  - Franchisee capital and profitability constraints
  - Dependence on master-franchise counterparties
- Channel-led transaction growth is tested against:
  - Any disclosed difference in store-level profitability
  - Fees or commissions if disclosed
  - Delivery versus carryout mix
  - The role of owned digital ordering and loyalty
  - Whether channel expansion coincides with proportional profit or cash-flow improvement
- The economic model is tested by comparing retail-sales claims with company revenue, operating profit, cash from operations, capital spending, and balance-sheet changes.
- Competitive assertions are labeled as management claims unless corroborated by independent figures within the corpus.
- Peer evidence is used cautiously: Pizza Hut-related evidence inside YUM data is not conflated with consolidated YUM performance, and differences in franchising, geography, concept mix, and fiscal calendars are disclosed.
- Conflicting figures are traced to definition, period, currency, company-owned versus franchised scope, or source revision. Unresolved conflicts remain explicit.
- Missing data is treated as an analytical limitation, not filled with outside assumptions.
- The analyst writes a provisional contrary case strong enough that the final position must explain why it is outweighed or decisive.

## Phase 5: Quantitative Anchoring

### Objective

Create a reproducible numerical bridge from comparable sales and store growth to reported revenue, profitability, and cash generation. Keep company-reported metrics separate from analyst calculations, show formulas for all derived values, and avoid false precision when definitions or periods differ.

### Expected source files from the manifest

- Reported operating metrics:
  - `sec_filings/10-k/dpz_2025_10-k.txt`
  - `sec_filings/10-q/dpz_2026q1_10-q.txt`
  - `press_releases/dpz_2026-02-23_8-k.txt`
  - `press_releases/dpz_2026-04-27_8-k.txt`
- Historical bases:
  - `sec_filings/10-k/dpz_2023_10-k.txt`
  - `sec_filings/10-k/dpz_2024_10-k.txt`
  - `sec_filings/10-q/dpz_2025q1_10-q.txt`
  - `sec_filings/10-q/dpz_2025q2_10-q.txt`
  - `sec_filings/10-q/dpz_2025q3_10-q.txt`
- Primary-company financial calculations:
  - `financials/income_statement/dpz_income_statement.json`
  - `financials/cash_flow/dpz_cash_flow.json`
  - `financials/balance_sheet/dpz_balance_sheet.json`
- Peer calculations:
  - `financials/income_statement/yum_income_statement.json`
  - `financials/income_statement/qsr_income_statement.json`
  - `financials/income_statement/wing_income_statement.json`
  - `financials/cash_flow/yum_cash_flow.json`
  - `financials/cash_flow/qsr_cash_flow.json`
  - `financials/cash_flow/wing_cash_flow.json`
  - `company_profiles.json`

### Observable trajectory signals

#### Reported-figure discipline

A reported-metrics table contains separate columns for value, unit, period, geography, currency treatment, definition, source path, and status as company-reported. It should include, where disclosed:

- Domestic and international same-store sales
- Prior-year comparable-sales bases
- Transaction and average-ticket indicators
- Gross openings, closures, and net store additions by geography
- Consolidated and segment revenue growth
- Royalty, advertising, and supply-chain measures
- Food-basket pricing changes
- Operating income and cash-flow values

No number is labeled reported merely because it can be inferred from a table.

#### Derived-figure discipline

Every calculated value is labeled analyst-derived and accompanied by its formula and input paths. Useful calculations include:

- International share of net additions  
  `international net additions ÷ total net additions`
- Domestic share of net additions  
  `domestic net additions ÷ total net additions`
- Reconstructed net additions, when the filing supplies components  
  `gross openings − closures`, adjusted only for other explicitly disclosed store-count movements
- Two-period compounded comparable sales  
  `(1 + current-period comp) × (1 + prior-year comp) − 1`
- Revenue growth, when not directly reported  
  `current-period revenue ÷ comparable prior-period revenue − 1`
- Operating margin  
  `operating income ÷ revenue`
- Margin change  
  `current-period margin − prior-period margin`
- Cash conversion  
  `cash from operations ÷ net income`, subject to consistent periods
- Free cash flow under a clearly stated convention  
  `cash from operations − capital expenditures`
- Peer growth and margin comparisons using the same formulas and comparable periods

#### Reconciliation and quality controls

- Annual and quarterly metrics remain separate; quarterly values are not annualized unless the calculation is explicitly labeled as a non-forecast illustration.
- A sequential change in comparable sales is not called acceleration without considering seasonality and the prior-year base.
- Additive two-year comp approximations are avoided when compounding inputs are available.
- Foreign-currency-neutral and reported-currency figures are not mixed.
- Company-owned-store results are not substituted for total domestic system results.
- Store-count arithmetic is reconciled to reported ending counts where the necessary components exist.
- Structured-data units are verified before calculating ratios or growth rates.
- Filing figures and JSON figures are compared for consistency; differences are documented rather than silently overwritten.
- Peer comparisons use aligned periods and disclose where concept-level data cannot be isolated from consolidated company data.
- A final numerical audit confirms that every value in the written analysis is either directly reported with an exact-file citation or visibly derived from cited inputs.

## Phase 6: Synthesis and Position

### Objective

Resolve the opposing evidence into one clear, defensible position on whether the sales recovery and unit-growth engine appear self-sustaining or fragile. The conclusion must explain the relative weight assigned to domestic demand, international momentum, unit economics, channel mix, revenue translation, and competitive evidence. It must not end as a neutral catalogue of positives and negatives.

### Expected source files from the manifest

- Principal operating evidence:
  - `sec_filings/10-k/dpz_2025_10-k.txt`
  - `sec_filings/10-q/dpz_2026q1_10-q.txt`
- Period and narrative cross-checks:
  - `sec_filings/10-k/dpz_2024_10-k.txt`
  - `sec_filings/10-q/dpz_2025q1_10-q.txt`
  - `press_releases/dpz_2026-02-23_8-k.txt`
  - `press_releases/dpz_2026-04-27_8-k.txt`
- Economic and competitive corroboration:
  - `financials/income_statement/dpz_income_statement.json`
  - `financials/cash_flow/dpz_cash_flow.json`
  - `financials/balance_sheet/dpz_balance_sheet.json`
  - All listed peer income-statement and cash-flow JSON files
  - `company_profiles.json`
- Other manifest files only where the prior phases have verified direct relevance.

### Observable trajectory signals

- The draft opens with a single-sentence position that chooses among durable, conditionally durable, or fragile rather than describing both sides without resolution.
- The body follows a causal chain:
  1. Comparable-sales direction by geography
  2. Transactions, ticket, products, loyalty, and aggregator contribution
  3. Gross openings, closures, net growth, fortressing, and franchise dependence
  4. Translation into royalties, advertising, supply-chain revenue, profit, and cash
  5. Competitive corroboration and limitations
- At least one explicit synthesis explains why favorable domestic demand and continuing unit additions do or do not outweigh international weakening, difficult comparisons, cannibalization risk, and potentially weaker aggregator economics.
- The analysis distinguishes evidence of demand from evidence of profitable demand.
- The international unit pipeline is reconciled with international comparable-sales direction and franchisee economics rather than evaluated independently.
- Management’s recovery language is evaluated against filed operating figures and financial results, not adopted as the conclusion.
- Peer results are used as corroboration or contradiction only to the extent permitted by comparable concepts and periods.
- Ambiguities are named precisely, including missing channel-margin disclosure, incomplete franchisee economics, concept-level peer limitations, or conflicting period definitions.
- Each paragraph’s factual claims carry inline citations to exact corpus files; derived conclusions cite the files containing their inputs.
- The conclusion states what evidence was decisive, why the strongest contrary case did not prevail, and which corpus-based indicators would invalidate the position.
- A final citation and cutoff audit removes unsupported facts, uncited numbers, post–June 30, 2026 information, and claims inferred from filenames alone.
- The completed synthesis is written to `/app/answer.txt` only after the evidence ledger, counter-case review, and quantitative reconciliation are complete.