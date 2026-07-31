You are a financial analyst with access to the data in `/app/data/`.

Topic: consumption-revenue growth durability and margin path

Cover these themes:

1. Consumption-Revenue Growth Durability and Net Revenue Retention
2. Bookings and RPO Quality Versus Recognized Revenue
3. Margin Path — Gross Margin, GAAP Loss Versus Non-GAAP, and Stock-Based Comp Dilution
4. Competitive and AI Durability — A Position on Growth-and-Margin Sustainability

Develop a view on this topic — covering each theme above — and write your full analysis to `/app/answer.txt`.

Your answer must:

- Take a clear position (not a balanced survey)
- Ground every claim in a specific file in `/app/data/` (inline cite the file)
- Engage with the strongest counter-evidence in the data
- Reconcile conflicting data points into a unified conclusion
- Note ambiguity rather than smoothing over it

Claims you can't ground in `/app/data/` (numbers, events, entities) are discarded by the grader and won't count toward your score.

## Data layout

`/app/data/` contains the following:

- `financials/income_statement/` — quarterly income statements (primary + peers)
- `financials/balance_sheet/` — quarterly balance sheet (primary ticker only)
- `financials/cash_flow/` — quarterly cash flow (primary + peers)
- `press_releases/` — wire press releases, one file per release
- `sec_filings/10-k/` — annual SEC reports (Risk Factors, MD&A)
- `sec_filings/10-q/` — quarterly SEC reports
- `sec_filings/s-1/` — IPO prospectus (recent IPOs only)
- `company_profiles.json` — company + peer profiles, point-in-time

The titles of the files within each folder provide additional context. Work with whatever is present.
