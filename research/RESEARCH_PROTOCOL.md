# Research refresh and evidence protocol

## Snapshot control
Research snapshot: **2026-10-18**. This repo hosts a *curated static database*, not an always-on live crawler. Current pages do not fetch X/Reddit/LinkedIn via account APIs. Any future automatic crawler must respect site permissions/rate limits and preserve source provenance. Human review is required for finance claims and sensitive competitive conclusions.

## Weekly refresh queue
1. **Company watchlist:** read official blog/press/news and product changelog for saved competitors and active opportunity rivals. Search funding, product integrations, pricing model and proof of outcomes. Look for counterevidence and closures/acquisitions.
2. **Community problem scan:** inspect relevant public discussions (smallbusiness, sales, ERP, accounting, logistics, property management, insurance, healthcare reception). Find recent concrete operational problems, failure modes and pricing objections. Don't collect users' personal identities.
3. **New market entrants:** search YC accelerator pages, product directories and startup newsletters for AI-native operating systems, vertical AI workforce, enterprise agent platforms and cross-system automation.
4. **Business model watch:** outcome-based pricing, per-success contracts, implementation costs, minimum commitments, deployment and data-retention terms. Price only if publicly documented.
5. **Diligence tasks:** prioritize primary source upgrades for all secondary-funded entries. Do not upgrade just because a secondary list repeats a number.

## Source record rules
Each new source gets a stable `S##` identifier, title, publisher category, original URL, verified page date and a distinction among `Company / primary`, `Independent reporting`, `Accelerator company profile`, `Institutional research`, `Community anecdote`, `Secondary index`, or `Not independently verified`.

Date and confidence rules: **publication date is not event date**. If funding announced on 2026-01-15, do not treat an Oct 2026 directory crawl as a fresh round. Round amount and cumulative funding must be different fields. Unknown funds stay blank. Do not use estimated ARR/valuation unless sourced as an explicit estimate and attributed.

## Deep competitor audit template

```
Company | Product URL | Last verified | Category | Buyers | Job-to-be-done
Exact business process (trigger → systems touched → action → outcome)
Workflow screenshots/docs and current published product limits
Communication channels + data integrations (publicly verified only)
Human oversight, approvals, escalation, audit and safety
Deployment time; revenue model; public pricing; sales motion (with evidence)
Latest announced financing (round, date, source) vs total raised
Public customers and outcomes (vendor claimed vs independent)
Differentiators, failure modes, defensibility, geographic constraints
What we should copy, avoid, test, partner with, or build
Founder recommendation confidence / unresolved questions
```

## Community signal and customer validation template

```
Problem ID | Industry | Process step | Observed friction | Thread permalink | Post date
What user said (short paraphrase, no unneeded personal details)
Sample bias/conflicts (e.g. vendor marketing, builder self-promotion)
Possible severity and recurrence — UNKNOWN until customer validated
Interview questions | Buyer role | Existing spend | Economic hypothesis
Decision: discard / research / interview / paid pilot
```

## Proposed automated refresh (not yet installed)

Scheduled discovery can pull permitted feeds and generate a **candidate changes queue**. It should **not** auto-edit verified company facts, scores or funding. A verified human or approved research agent reviews sources, updates JSON, then opens a PR. Validate data structure and links on CI before publish. This approach prevents a low-quality news snippet from silently rewriting strategy.

## Refresh commands

```
python tools/build_frontend_data.py
python tools/validate_data.py
python -m http.server 8000
```

## Update discipline
When adding new company: verify the company exists at given domain; don't merge homonyms; avoid duplicate aliases; attach original source; set depth. Recompute meta counts programmatically. If date is stale, make staleness visible. For changes impacting ranking, write what evidence changed. No invented achievements, sources, ROI, user counts or funding.