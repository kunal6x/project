# InfraAtlas — AI-Native Business Infrastructure Intelligence

**Research snapshot: 18 October 2026** | Source-backed market mapping and business design hypotheses.

InfraAtlas is a mobile-responsive, dependency-light research workspace for a startup that wants to build **AI-native business infrastructure**. It tracks voice agents, vertical AI operating systems, enterprise workflow players, finance and orchestration software, observed customer friction, financial reporting sources, product strategy, and unit economics.

## What is included

- Interactive company directory (280 records, **mixed diligence depth**; many voice company entries originate in secondary landscape indexes)
- 40 curated direct links (company announcements, accelerator listings, institutional research, and qualitative community signals)
- 14 opportunities with explicit *subjective hypothetical* scores and linked underlying evidence
- 11 pain/problem hypotheses; community posts are anecdotes, not validated demand
- Voice-to-outcome strategy, 12-layer reference architecture, decision-gated pilot plan
- Dynamic unit-economics calculator with editable assumptions; **not** a forecast
- Browser-only competitor watchlist and research notes + export functions
- Reusable machine-readable source data, research update protocol, agent instructions

## Run locally

```bash
python -m http.server 8000
# open http://localhost:8000
```

A recent browser can also load `index.html` directly; the site data is embedded in JS rather than relying on a `fetch` from file URLs.

## Hosting

The supplied `.github/workflows/pages.yml` deploys the site with GitHub Actions when GitHub Pages is enabled for this repository using the `GitHub Actions` build source. The workflow may need the first GitHub Pages activation in Settings → Pages and repository Actions permissions. Do not claim the public Pages URL is live until the deployment finishes and is verified.

## Research data and confidence

`data/research.json` is the canonical research file. `data/research-base.js` and `data/companies-*.js` are generated static frontend assets from the canonical dataset.

**Funding rules**: display the amount, round, date, source URL, and confidence. Primary company press releases should be rechecked for currency and round-vs-total distinctions. Secondary directories are **not a funding verification**. Not publicly disclosed ≠ zero. Do not infer revenue or valuation from fundraising.

**Company research depth**: many records are shortlist entries and **not** deep product audits. Deep audits require current vendor primary docs, hands-on demo, real pricing verification, integration details, customer evidence, and counterevidence.

**Demand signals**: posts from Reddit and similar communities are anecdotes. They should generate interview questions, not market share, willingness-to-pay, or TAM claims.

**Opportunity ranking**: the displayed score is a weighted *founder assumption* on seven 1–5 dimensions; customer evidence has not validated any of them.

## File map

| Path | Use |
|---|---|
| `index.html`, `styles.css`, `app.js` | Static interactive dashboard |
| `data/research.json` | Canonical machine-readable market intelligence |
| `data/research-base.js`, `data/companies-*.js` | Generated deploy assets |
| `tools/build_data.py` | One-off initial dataset assembly using older research files; not required for normal refresh |
| `tools/build_frontend_data.py` | Regenerate public static JS from canonical JSON |
| `research/STRATEGY.md` | Narrative strategic thesis and critical risks |
| `research/RESEARCH_PROTOCOL.md` | Source verification, update/refresh SOP |
| `research/COMPETITIVE_AUDIT.md` | Diligence checklist and competitor battlecards |
| `research/INTERVIEW_PLAN.md` | First-customer discovery and pilot design |
| `AGENTS.md` | AI coding/research agent handoff |

## Important limitation

This is a working static research dashboard with persistence on **one browser** for bookmarks and notes. It does **not** autonomously crawl X, LinkedIn, Reddit, or the wider web in real time; those often require accounts and/or APIs. The review/update protocol exists so a permitted future agent can refresh research through version-controlled PRs, with human source verification.

## Strategic thesis

**Make the business workflow complete, not the conversation impressive.** Position voice as one communication channel in a vertically differentiated system of action. Connect existing CRMs/ERPs, stage all meaningful changes as governed and auditable actions, handle edge cases, and measure booked revenue, completed jobs, hours saved, or accelerated cash collections.