# Kang — Sample Tasks

Kang is a reinforcement-learning environment for training and evaluating agents on hard,
open-ended **financial-analyst reasoning**. This repository is the public **sample task
library**: 30 complete, self-contained, ready-to-run environments.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

![Kang](./assets/banner.jpeg)

Each task drops an agent into a sandboxed container stocked with a point-in-time corpus of
regulatory filings and financial statements, hands it an open-ended research topic, and scores
the written analysis against an explicit rubric of the analytical *moves* a competent analyst
would make. That rubric-anchored score is the reward.

Where most finance benchmarks terminate in a keyed answer, Kang rewards **the argument itself**:
decomposing a theme into the right sub-questions, grounding every claim in the source documents,
engaging the strongest counter-evidence, and reconciling conflicting data points into a single
defensible view.

Nothing here is scraped from analyst notes, forums, or any public answer key. The corpus is
fetched directly from primary regulatory sources; the rubrics are authored against those filings
and fact-checked line by line before a task ships.

---

## What's in this repository

| | |
|---|---|
| **Tasks** | 30 |
| **Companies** | 30 distinct US-listed issuers |
| **Point-in-time cutoff** | `2026-06-30` (uniform) |
| **Corpus** | 808 files, ~109 MB total (~27 files / ~3.5 MB per task) |
| **Rubric shape** | 4 themes per task, 12–14 lettered moves |
| **Per task** | prompt, corpus, Dockerfile, rubric, 3-pass grader, reference reasoning trace, one recorded baseline trajectory |

Every task directory is named by a stable UUID, so task identity survives renaming a ticker,
a topic, or a cutoff.

---

## Task anatomy

```text
<uuid>/
  Instruction.md                  # The open-ended prompt the agent sees
  Truth.md                        # Reference reasoning trace (phase-by-phase analyst process)
  task.toml                       # Harbor config: artifacts, timeouts, resources, difficulty note
  environment/
    Dockerfile                    # ubuntu:24.04 + python3 + uv; copies data/ to /app/data
    data/                         # Point-in-time corpus (mounted read-only at /app/data)
      company_profiles.json       #   primary + peer profiles
      financials/
        income_statement/         #   up to 16 quarters, primary + peers
        balance_sheet/            #   up to 16 quarters, primary only
        cash_flow/                #   up to 16 quarters, primary + peers
      sec_filings/
        10-k/                     #   ~3 annual reports (full text)
        10-q/                     #   ~6 quarterly reports (full text)
        s-1/                      #   IPO prospectus (13 of 30 tasks)
      press_releases/             #   ~8 earnings press releases (8-K EX-99 exhibits)
  tests/
    test.sh                       # Verifier entry point
    grade.py                      # Three-pass LLM-as-judge grader
    grading_prompt_task1..3.md    # Grounding, coverage, synthesis prompts
    ground_truth.txt              # The rubric: themes, lettered moves, source files
    rubrics.json                  # Process-level criteria for trajectory verification
    test_outputs.py               # Deterministic invariants (answer present, cited files real, …)
  trajectories/
    claude-opus-4-8/              # One recorded baseline run: answer, trajectory, score breakdown
```

The agent writes its full analysis to **`/app/answer.txt`**, which is the only artifact graded.

---

## Where the data comes from

Every corpus is machine-fetched from **primary regulatory sources**. No vendor feeds, no scraped
analyst content, no LLM-generated documents.

### The four gates

A source is only wired into the pipeline if it passes **all four**:

1. **Free** — no paid subscription (a free-registration key is tolerated, not preferred).
2. **English** — the filing *text* must be English, because the grader verifies quotes **verbatim**.
3. **Clean API** — a machine-readable JSON/XBRL endpoint, not a fragile page scrape or a pile of PDFs.
4. **Point-in-time** — real filing dates, so nothing dated after the cutoff can leak into the corpus.

### Sources in the pipeline

| Region | Source | Tier | Role |
|---|---|---|---|
| 🇺🇸 US + global ADRs | **SEC EDGAR + XBRL Company Facts** | structured | The backbone. Every task in this repo. |
| 🇮🇳 India | **BSE** | text | Keyless route for India-only names; financials best-effort. |
| 🇭🇰 Hong Kong | **HKEXnews** | text | The English doorway to HK/mainland-Chinese names with no US listing. |

**The insight that shapes the whole pipeline:** a foreign company with a **US listing** files its
annual report as a **20-F / 40-F / 6-K / F-1 — in English, free, on SEC**. So most large European
and Asian names are best fetched through SEC, *not* their home regulator. A local source only
matters for a company with **no** US listing. All 30 tasks in this release are SEC-sourced.

Sources evaluated and rejected — Canada (SEDAR+, CAPTCHA-walled), Australia (ASX, no point-in-time
fetch), Taiwan (MOPS, Chinese labels + latest-period-only), EU (ESEF, 27 fragmented national
systems), India NSE (Akamai anti-bot, redundant with BSE), Singapore, UK FCA NSM, and company IR
pages.

### What SEC gives, and what it doesn't

**Gives:** up to 16 quarters of authoritative XBRL financials (US-GAAP *and* IFRS-tagged foreign
filers), full 10-K / 10-Q / S-1 text, 8-K EX-99 earnings press releases, and company profiles —
all with real filing dates.

**Doesn't give, and we don't fake:**

- **No earnings-call transcripts.** SEC has none. This is structural across every free source.
  Rubric themes are authored so they never require what management said on a call.
- **No market prices.** Optional yfinance enrichment exists in the fetcher but is not used in
  this release.
- **Q4 gaps** — many issuers report Q4 only inside the 10-K, so the quarterly series has holes.
- **Tables flatten** in HTML→text conversion. Prose reads cleanly; filing tables lose structure.
  Numbers are therefore taken from the XBRL JSON, not from filing tables.

---

## The rubric

`tests/ground_truth.txt` is a preface (concept-match rule, synthesis requirement, grounding rule)
followed by numbered themes. Each theme carries a one-paragraph thesis, its lettered moves, and
its `Source:` line:

```text
2. Billings / RPO / Deferred-Revenue Durability as a Forward-Demand Signal
Remaining performance obligations grew from $15.8 billion to $18.4 billion, but management
cautions that RPO and deferred revenue should be viewed independently of GAAP revenue, so
their durability as a demand signal must be tested rather than assumed.
[a] Track RPO growth ($15.8B at July 31, 2025 to $18.4B at April 30, 2026) and the near-term
    recognizable portion (~$7.0B rising to $8.3B over the next 12 months) …
[b] Cross-check RPO against current and long-term deferred-revenue balances, and separate
    organically driven backlog from growth pulled forward by financing terms and by M&A.
[c] Engage the strongest counter-evidence: management's own caveats that these metrics do not
    represent revenue under U.S. GAAP or a revenue forecast.
Source: sec_filings/10-k/panw_2025_10-k.txt, sec_filings/10-q/panw_2026q3_10-q.txt, …
```

Credit is awarded on **concept match, not vocabulary match** — the example phrasing illustrates
the move; any equivalent framing satisfies it.

Beyond covering the themes, `Instruction.md` requires the agent to take a clear position rather
than survey both sides, engage the strongest counter-evidence in the data, reconcile conflicting
data points into a unified conclusion, note ambiguity instead of smoothing it over, and
**inline-cite the source file behind every claim**. Claims that cannot be grounded in a provided
file earn no credit.

---

## Reward

Kang grades long-form prose with no single correct wording, so scoring runs an LLM judge
(default `gpt-5.6-sol`, temperature 0, JSON-constrained) against the rubric. The judge
runs as **three passes**, so factual grounding and analytical coverage are scored separately and
then combined:

**1. Grounding.** The grader reconstructs the evidence the agent relied on by loading exactly the
files it cited, extracts every specific factual claim (figures, quotes, named entities, dates,
comparisons), and flags any the cited sources don't support. Framings and inferences are fine as
long as their building blocks are present. The bar is: *did the agent invent a fact.*

**2. Coverage.** For each theme, the judge reports which lettered moves the answer hits by concept
match. A move whose supporting evidence was flagged in pass 1 is marked **tainted** and does not
count — so a fabricated figure forfeits only the move it taints, not the whole answer.

**3. Synthesis.** The judge checks for at least one explicit synthesis that reconciles opposing
data points into a unified conclusion, as opposed to listing considerations in parallel. This
gates the top score.

### Theme coverage

A theme with `n` moves counts as covered once the agent lands enough **untainted** moves to clear:

```
tau = max(1, min(n - 1, 3))
```

The `n - 1` term allows one miss per theme; the cap at `3` keeps move-rich themes from demanding a
near-perfect hit rate. In this library that means a 3-move theme needs 2, and a 4-move theme
needs 3.

### Score

Every task in this release has `T = 4` themes. From the number of covered themes `C`:

| `C` covered | 0 | 1 | 2 | 3 | 4 | 4 + synthesis |
|---|---|---|---|---|---|---|
| **Dense score** | 0 | 1 | 2 | 2 | 3 | **4** |

The sparse pass/fail signal is derived from the dense score: **a trial passes only at a perfect 4**.

The harness writes the sparse reward to `/logs/verifier/reward.txt` (`1` or `0`) and the full
breakdown to `/logs/verifier/details.json`.

### Reading `details.json`

| Field | Meaning |
|---|---|
| `score` | Dense 0–4. |
| `sparse_reward` | `1` iff `score == 4`. This is pass@1. |
| `valid_trial` | `false` when a judge pass returned unparsable output. **Exclude these from any metric** — they are grader failures, not agent failures. |
| `themes_hit` / `themes_missed` | Per theme: `moves_hit`, `moves_tainted`, `move_reasoning`, `threshold`/`n_moves`. |
| `unverifiable_claims` | Every claim the grounding pass could not verify, with the file searched and why it was flagged. |
| `hallucinations_detected` | Whether pass 1 flagged anything. |
| `synthesis_found` | The quoted synthesis sentence, or `null`. |
| `cited_files` | The data files the answer actually cited — the exact evidence set pass 1 verified against. |

> A judge failure writes `0` to `reward.txt` **and** sets `valid_trial: false`. Averaging
> `reward.txt` without filtering on `valid_trial` silently contaminates your metric with grader
> infrastructure failures.

Use the dense score for reward shaping during training and pass@1 for evaluation.

## Composition

30 tasks across the recurring topics that define analyst work — valuation, growth durability,
M&A integration, competitive positioning, operational execution, and risk. All are point-in-time
as of **2026-06-30**, each with 2–3 named peers whose income statements and cash flows ship in
the corpus.

**Software, Security & Infrastructure (7)**

| Ticker | Topic |
|---|---|
| ADBE | Generative-AI disruption risk vs. the Creative Cloud moat |
| CRM | Growth deceleration vs. operating-margin expansion |
| CRWD | Durability of security growth and retention after the 2024 outage |
| DDOG | Usage-based growth durability and platform competition |
| NET | Growth durability and operating-leverage inflection |
| PANW | Platformization strategy and billings/RPO durability |
| SNOW | Consumption-revenue growth durability and margin path |

**Financials (7)**

| Ticker | Topic |
|---|---|
| AXP | Premium-spend durability and credit-cost normalization |
| BLK | Net flows, fee-rate mix, and the private-markets buildout |
| COF | Credit normalization and the Discover acquisition integration |
| KKR | Franchise growth and insurance-driven earnings mix |
| MA | Cross-border volume durability and value-added-services growth |
| PYPL | Branded-checkout turnaround and transaction-margin stabilization |
| SCHW | Deposit and net-interest-income recovery post cash-sorting |

**Consumer & Retail (7)**

| Ticker | Topic |
|---|---|
| CMG | Traffic and margin durability against maturing unit growth |
| COST | Membership-growth durability and margin/fee dynamics |
| DECK | HOKA and UGG growth durability and brand concentration |
| DPZ | Same-store-sales recovery and unit-growth durability |
| LOW | Comparable-sales recovery and Pro penetration vs. Home Depot |
| SBUX | US traffic turnaround and China competitive pressure |
| TGT | Traffic recovery and operating-margin normalization |

**Industrials, Aerospace & Transport (6)**

| Ticker | Topic |
|---|---|
| BA | Recovery credibility, cash burn, and 737/787 execution |
| CAT | Construction cycle and backlog durability |
| DAL | Premium-revenue mix and balance-sheet deleveraging |
| DE | Ag-cycle downturn severity and precision-agriculture durability |
| RTX | Commercial-aftermarket recovery vs. the GTF powder-metal charge |
| UAL | Unit-revenue and margin durability against capacity growth |

**Internet & Marketplaces (2)**

| Ticker | Topic |
|---|---|
| ABNB | Growth durability and take-rate expansion vs. regulatory risk |
| DASH | Margin inflection and new-vertical expansion durability |

**Healthcare (1)**

| Ticker | Topic |
|---|---|
| REGN | Eylea competitive erosion and pipeline offset |

---

## Baseline results

One recorded trial per task ships under `<uuid>/trajectories/claude-opus-4-8/`, including the
agent's `answer.txt`, its full tool trajectory, and the grader's `details.json`.

Across all 30 tasks (`claude-opus-4-8`, `k=1`):

| Dense score | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Tasks | 22 | 6 | 2 | 0 | 0 |

**pass@1 = 0/30.** The synthesis gate was cleared on 30/30 — coverage, not synthesis, is the
binding constraint. Grounding flagged a median of ~49 claims per answer, and **79% of all moves
the coverage pass credited were subsequently tainted**.

Read these numbers with the limitation below in mind: they are a floor, not a clean difficulty
measurement.

---

## Known limitations

**Monolithic grounding context.** The shipped `grade.py` verifies claims by concatenating every
cited file whole into a single judge request. A 10-K in this corpus runs 400 KB+, so the grounding
pass can be asked to confirm ~50 specific strings against ~700 KB of filing text in one call. That
is a retrieval problem, and retrieval failure is indistinguishable from hallucination — the judge
can only report "not present," never "I didn't find it." Spot-checking the shipped baselines
confirms false positives: quotes flagged as absent that appear **verbatim** in the cited filing.
Because tainting deletes credit, each false positive costs a real move.

Anyone training on these tasks should treat the *tainting rate* as a diagnostic, not just the
score, and should prefer a **retrieval-based grounding pass** (extract → local harvest → batched
verify) over the monolithic path. Peer-ticker auto-expansion was already removed from
`discover_cited_files` for the same reason: it blew past the judge's input cap.

**Dense-score plateau.** With `T = 4` on every task, `C = 2` and `C = 3` both map to a dense
score of `2`. There is no gradient across that step — worth knowing before using the dense score
as a shaping signal.

**Threshold is non-monotonic in move count.** `tau = max(1, min(n-1, 3))` requires 67% of a
3-move theme, 75% of a 4-move theme, and 60% of a 5-move theme. The 4-move theme is the strictest
in the library, and it is always the one carrying the synthesis move.

**Self-grading bias.** Running an agent and a judge from the same model family inflates scores.
For an unbiased number, grade cross-family — the shipped default (`gemini-3.1-pro-preview`)
against a Claude or GPT agent already does this.

**No earnings-call transcripts.** A structural gap in every free source. Rubrics are authored
around it, never through it.

---

## License

Released under the MIT License. Copyright (c) 2026 Ethara.AI. See [LICENSE](LICENSE).
