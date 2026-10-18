# Strategic memo — AI-native business infrastructure
**Decision date:** 2026-10-18. **Status:** Hypothesis pending customer validation.

## Core idea

The company should not identify solely as an AI voice-agent vendor. Its product may use voice, SMS/WhatsApp, web, email and document automation, but the differentiated layer is a **governed business execution engine** that joins customer events, system-of-record data, approved actions, industry-specific workflows and financial outcome measurement.

**Offer definition:** "We take one recurring, expensive business process from trigger to verified completion, while humans remain accountable for exceptions." The full business OS vision is a *sequenced platform* built from validated workflow wedges.

## Why now and why not generic

Many voice and horizontal workflow products exist; cheap speech and language models reduce entry barriers to basic interactions. Enterprises and vertical OSs (EliseAI, Covera, Parrot, Marble, Flott, Rillet) are expanding toward domain-specific actions. Major platforms (Oracle, Salesforce, SAP, ServiceNow) are embedding agentic execution inside core objects and authorization controls. Therefore, generic “AI agent builder” is crowded. The startup must earn distribution, execution context and trust.

**Evidence:** See `data/research.json` and original links. Primary examples: EliseAI 2026 financing; Rillet Series C; Oracle July 2026 agents; YC Covera / CarSignal / Marble. Business skepticism and operating failures: r/n8n, r/Dentistry, r/ERP, r/PropertyManagement. These Reddit comments are anecdotes, not quantified market prevalence.

## Market architecture

1. **Distribution channel:** integrate inside existing business workflows and existing software; no rip-and-replace requirement.
2. **System of context:** linked contacts, organizations, jobs, reservations, invoices, permissions, event history and customer preferences, with source-of-truth pointers.
3. **System of action:** deterministic workflow engine; bounded agent proposals; action adapters with policy checks; human approval queues.
4. **Measurement:** verified conversions, booked/fulfilled jobs, recovered cash, resolution times, actual API/voice/human costs, margin.
5. **Retention moat:** one onboarding integration and domain process should make next cross-functional workflow 10x easier for customers to adopt, without creating a fragile universal platform too early.

## Initial candidates and realistic downsides

| Wedge | Buyer and visible ROI | Strength | Risk |
|---|---|---|---|
| Home-services lead→booked job | Owner/GM; recovered jobs and revenue | Can reuse existing voice infra; frequent transaction | crowded reception market; reliable FSM integrations essential |
| Wholesale/distribution order→cash | Ops/CFO; error rate, DSO, overtime | End-to-end process with strong dollar outcomes | ERP integrations and payment dispute edge cases |
| Insurance brokerage quote→renew | Principal/COO; CSR hours, bind speed, retention | Deep workflows and compliance moat | portals, carrier rules, E&O risk; big incumbents |
| Real-estate lead→site visit→sale | Broker; attended visits, closed deals | Existing voice-agent domain competence | market noise; attribution and low-quality leads |
| Property management maintenance→resolved | PM operator; time to repair and tenant satisfaction | High cross-party coordination burden | some buyers actively reject AI phone agents |
| Healthcare patient admin→completed visit | Practice manager; no-show rate, collections | high volume and important pain | medical data, patient safety, complex integrations |

Do not select the wedge based only on market-size decks. Test access to actual customer documents, source-of-truth APIs, total costs, willingness to pay and safe operational workflow.

## Commercial model hypotheses

- Base monthly fee to cover fixed onboarding/support/controls, plus transparent usage.
- Verified outcome fee only where attributable: kept booking, paid job, resolved denial, or recovered invoice. Use a contractual definition and independent data source.
- Offer a human takeover/exception desk as paid reliability, not a failure state to hide.
- Enterprise plans may have integration, observability, and compliance premiums. Price against realized customer contribution margin, not token-count alone.

## Key differentiated design bets

- **Finish-rate, not bot-count:** product UX centered on completion graph, SLA, exception queue, revenue outcomes.
- **Action accuracy:** calendar and ERP commit logic deterministic; follow-up agents cannot invent availability or financial figures.
- **Business memory:** reusable canonical domain objects with lineage; integrate legacy systems, don't force full migration.
- **Honest autonomy:** per-workflow escalation settings, not “100% AI” claims.
- **Evidence loop:** every production failure creates a regression case; every strategy claim links to a field interview or source.
- **Global multi-channel:** voice first where it is strongest; asynchronous channels may be cheaper and more accepted depending on workflow.

## Ways we could lose

Distribution dominated by vertical incumbents; long/expensive implementation; absence of reliable vendor APIs; high customer churn because only low-value FAQs automated; consent/dialing rules vary widely; abuse/compliance exposure; marginal cost of model, staff supervision and telephony erases gross margin; benchmark demos mask real-world scheduling/payment failures; weak data rights and cross-client learning constraints.

## Decision cadence

Week 1–2: 20 problem interviews, five actual workflow shadows, two paid LOIs, baseline customer measurements. Weeks 3–4: one workflow prototype on one customer system with event log, tool approvals, tests. Weeks 5–6: controlled pilot measuring true cost and finished outcomes. Weeks 7–8: second customer onboarding without one-off code. Month 3: expand to one adjacent revenue-bearing workflow only after initial wedge proves positive contribution.

**Do not confuse a polished dashboard or source database with validated market demand or a deployed business execution platform.**