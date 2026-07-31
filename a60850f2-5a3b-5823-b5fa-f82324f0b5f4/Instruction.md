You are a financial analyst with access to the data in `/app/data/`.

Topic: HOKA and UGG growth durability and brand concentration

Cover these themes:

1. Divergent Growth Trajectories of HOKA and UGG
2. Brand Concentration and the Collapsing "Other" Portfolio
3. Channel and Geographic Mix as a Quality-of-Growth Signal
4. Seasonality, Competition, and the Durability Verdict

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
- `company_profiles.json` — company + peer profiles, point-in-time

The titles of the files within each folder provide additional context. Work with whatever is present.
