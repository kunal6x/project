# AGENTS.md — Mandatory startup context for coding and research agents

## Mission
Build a commercially differentiated **AI-native business infrastructure** platform. Existing streaming **AI voice calling** is one input/output channel, not the whole product. The north star is completion of real cross-system business processes with measurable profit/revenue or time-to-cash improvements.

## Read before changing anything
1. `README.md` — repository structure, evidence limitations.
2. `research/STRATEGY.md` — market choices and differentiation thesis.
3. `research/RESEARCH_PROTOCOL.md` — evidence and update standard.
4. `data/research.json` — canonical company, signals, opportunities, source links.
5. `research/INTERVIEW_PLAN.md` — customer validation requirements.

## Behaviors
- Act as a skeptical product researcher: proactively look for counterevidence, market saturation, failed pilots, margins, compliance, and sales friction.
- **Never fabricate funding, investors, pricing, ARR, valuations, customer count, or deployment facts**. Record unknown as unknown.
- Research each startup along: who pays; what job it performs; exact workflow; integrations; product model; customer outcomes; sales cycle; strengths; limitations; what can be learned or avoided.
- Date the source and classify `primary announcement`, `independent press`, `accelerator/product profile`, `community anecdote`, `secondary directory`, or `unverified`.
- Read community comments for real workflows and failures but never extrapolate anecdote to prevalence or TAM.
- Keep opportunity scores marked as unvalidated assumptions. Change score only with documented reasoning.
- Every product proposal includes **workflow baseline, economic buyer, source-of-truth, actions, approval/fallback, success metrics, unit economics and competitor context**.
- Favor wedge-to-platform sequencing. Do not propose rebuilding generic CRM/ERP on day one.
- Business state actions must be bounded by permissions, audited, idempotent where possible, reversible or compensatable where necessary, and escalated to humans at uncertainty thresholds.
- Do not mutate private product repositories during research. This repo is research-only and intentionally public; never commit client leads, private credentials, customer PII, telephony keys, access tokens or confidential infrastructure diagrams.

## Data contract
- `data/research.json` is canonical and must remain valid JSON.
- `companies[]`: id, name, category, vertical, description, site, funding, fundingDate, source, confidence, and other fields. Do not delete verification labels.
- `sources[]`: id, title, date, url, quality, group.
- `opportunities[]`: id, workflow, score, scores, evidence IDs, thesis, outcome metrics, stage.
- `problems[]`: id, claim, source IDs, quality, implication.
- For every material new financing claim, add or update a direct source. Where possible use official announcement as the citation URL.
- Generate frontend assets with `python tools/build_frontend_data.py`, run validation, and keep changes reviewable.

## Changes protocol
Create an issue/PR per research batch, attach primary sources, explain changed conclusions, and label which scores are still hypotheses. If the facts are uncertain, log a research task and do not ship a certainty claim. In any edit affecting homepage stats, recompute counts from actual data; do not hardcode.

## Default founder strategy (subject to validation)
Test (a) home-services lead→booked paid job, and (b) wholesale order→invoice→collections, using actual paid design partners. Real estate qualification is an additional lower-friction distribution possibility given the team's existing voice use cases. Do not treat this prioritization as settled before customer interviews.
## Current launch decision (19 October 2026)
Read `research/VOICE_LAUNCH_DECISION_2026-10-19.md` before creating voice product requirements, prioritizing launch features, or advising on GTM. It prioritizes **consented inbound real-estate lead → qualified lead → confirmed site visit** as the first paid commercial workflow, subject to customer-validation gates. The broad AI-native business infrastructure strategy remains longer term; do not interpret it as a mandate to build a general-purpose platform now. Current deployment readiness is not established by READMEs alone.

## Specific product differentiation decision (19 October 2026)
Before proposing launch features or modifying the voice product, read `research/HAPTICA_PRODUCT_DIFFERENTIATION_2026-10-19.md`. The flagship is **Haptica Missions / Revenue Autopilot**: consented event-triggered lead → verified outcome, leak detection, two-sided coordination, human approvals, trustworthy action receipts and outcome ledger. Voice Studio and existing services remain, no rewrite by default. Existing competitor features (agent builder, KB, calls, workflows, A/B tests, CRM, generic analytics) are not differentiators on their own. Product decisions remain hypotheses until pilots validate conversion economics.
