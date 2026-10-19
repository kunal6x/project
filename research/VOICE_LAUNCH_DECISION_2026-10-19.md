# Founder decision — Voice-first, outcome-first launch
**Date:** 19 October 2026 | **Decision:** Conditional, to validate with paying customers | **Owner:** Founding team

## Decision in one sentence
Launch the existing Haptica AI voice calling platform as an **outcome-driven, compliant lead-response and appointment-setting product**, initially for **real-estate sales teams handling consented inbound enquiries**. Keep the underlying agent builder extensible; do not attempt a general-purpose AI-native business operating system at launch.

### Why this sequence
- Voice model and agent-platform features are commoditizing. Sarvam offers a complete voice-agent stack from ₹3.50/agent-minute PAYG (telephony charged separately), including Indian-language support, campaigns, workflows, testing and analytics. Do **not** compete only on voice quality, basic builder features, or lowest minute rate.
- Real estate is a sensible **first distribution wedge** because this team already has scripts, campaigns, domain knowledge and CRM/site-visit booking abstractions. It is **not proved** to be the best long-term vertical.
- Sell verified **lead-to-confirmed-site-visit** workflow results; the caller experience is only one step.

## Product promise
“When an opted-in property lead arrives, Haptica responds quickly, qualifies the requirements in the customer's language, books a real slot, confirms it, keeps CRM current, and hands hot leads to the human closer.”

**Never claim a booked, attended or revenue outcome without confirmation from the authoritative destination system.**

## First buyer and offer
- **Economic buyer:** sales director/marketing head of real-estate developers or brokerages with a meaningful monthly inbound lead volume and measurable lost-lead problem.
- **Minimum customer fit:** reliable opt-in lead provenance; a calendar or authoritative booking system; CRM or clean spreadsheet; sales team that will follow up; ability to access baseline outcomes and pay for pilot.
- **First workflow:** inbound lead form -> consent check -> prompt voice contact (or inbound missed-call recovery) -> qualification (project, location, budget, intent, timeframe) -> real slot check and booking -> SMS/WhatsApp/email confirmation **where permitted and integrated** -> handoff -> attendance reconciliation.
- **Secondary workflow after proof:** missed-call recovery/inbound appointment booking for home services; do not simultaneously launch many verticals.

## Launch website and signup
- Public pages: landing page with a **live sandbox demo**, use-case-specific solution pages, explicit transparent pricing (not unlimited), security/privacy/compliance, documentation/API, ROI explanation, customer proof once real, Book a Pilot.
- Top CTAs: “Try a live demo” and “Start building”; sales-assisted “Book a pilot” for deployment.
- Signup: Google/email OTP -> organisation/country/timezone -> use-case template -> agent naming/goal -> paste website or upload knowledge -> **browser audio test with mock data** -> invite teammate -> connect real calendar/CRM -> verify business and telephony/number ownership -> consent/DNC/calling-hours checks -> set spend cap and funding -> preview test call -> activate.
- No card required merely to explore/sandbox; phone calls and large uploads require verification and prepaid budget to prevent abuse.
- Trial credits tiny and bounded; no arbitrary outbound dialing before approval and suppression controls.

## Minimum lovable launch (P0)
1. Stable natural multilingual agent with interruption handling, silence timeout, no fabricated facts and human transfer.
2. Outbound to **consented** inbound leads and inbound overflow/missed calls, with timezone and retry controls.
3. One real booking integration (Google Calendar or customer's scheduling system), idempotent write, confirmation state and failure recovery; CRM sync/webhook.
4. Import only verified lead lists, consent evidence, opt-out/DNC, compliance-approved dialer routing and recording controls.
5. Per-call timeline, transcript where permitted, disposition, lead qualification, tool traces, errors, billing, answer rate, lead-to-visit funnel.
6. Tenant auth/role isolation, prepaid metering, spending cap, kill switch, alerting, operator controls, safe secrets.
7. Minimum regression suite across interruptions, Indian names/numbers, Hinglish, negative answers, no-slot, double booking, opt-out and handoff.

## Critical repo-documentation caveats to verify before public launch
- `haptica-identity-service/README.md` labels identity as a "walking skeleton" and doesn't demonstrate public signup readiness.
- `haptica-frontend/README.md` says auth token is stored in localStorage and notes hardening issues; review before opening public onboarding.
- `haptica-crm-service/README.md` explicitly says booking confirmation/reminder delivery and calendar sync are **not yet built**.
- Existence of code/docs is **not evidence of production deployment**. Do a live end-to-end test with current versions and consent-safe phone numbers.
- Preserve existing senior-engineer changes and working production paths. Fix only audited release blockers.

## Commercial model: TEST, not announced pricing
- Free controlled browser-only demo.
- 14–30-day **paid** design-partner pilot with defined onboarding/setup and bounded usage (example negotiation anchor: ₹10k–₹25k for a pilot, final quote set after scope/COGS).
- Later: monthly platform fee + transparent consumed minutes + optional premium CRM actions/onboarding; optional verified held-appointment fee only with auditable attribution.
- Compute full cost per **billable** minute including active/idle GPU, STT/LLM/TTS, telephony, retries, monitoring, fraud and human QA. `Min sustainable price = blended fully loaded variable cost / (1 - target contribution margin)`. No unlimited plan without a carefully modeled cap.
- Track **cost per verified held visit**, lead conversion lift and margin; do not sell a speculative ARR forecast.

## Four-week commercialization sequence
- **Week 1 — sell before polishing:** talk to 10–15 eligible sales heads, inspect 3 anonymized funnels and baseline lead-response times; secure 2 signed *paid* pilot commitments. Prospect through warm industry connections; never scrape/spam cold recipients with AI calls.
- **Week 2 — unblock:** run production-readiness audit; finish 1 booking integration, identity, consent controls, billing limits, failure observability; record 30+ adversarial scenario tests.
- **Week 3 — controlled live pilots:** activate opted-in lead workflow for 1–2 design partners at capped minutes; compare against their previous or holdout process; inspect failed calls every day.
- **Week 4 — retention proof:** deliver one-page customer ROI report; ask for second paid month/expansion. If pilot economics/reliability fail, fix or narrow workflow before pursuing signups.

## Decision gates
- **Safety:** zero unauthorized external state changes; no unapproved campaigns; verifiable consent provenance and opt-out suppression.
- **Reliability:** >95% passing relevant scripted critical-path integration cases before production pilot; 100% observed failures traceable. These are initial team thresholds, not universal benchmarks.
- **Value:** at least 2 paying pilot customers, clean baseline, independently verified booked/held visits, measurable lift relative to spend, positive contribution after telephony/AI/support.
- **Pivot trigger:** if no paid pilot from ~15 qualified conversations, or if booked-visit attribution and integration are unavailable, investigate home-services missed-call-to-booked-job before adding features.
- **Expansion trigger:** only after retention and repeatable setup; then productize adjacent workflow(s), not generic CRM/ERP rewrite.

## What we do NOT build for launch
All-industry templates, 33-language fine-tuned proprietary models, a full replacement CRM/ERP, complex autonomous workflows with financial side effects, a vanity features marketplace, uncontrolled free live outbound calls, unverified “100% human” claims, or price-war discounts without contribution math.

## Platform future
Re-use the voice-first foundations: contacts, consent/provenance, workflow execution, business objects, role/approval policy, integrations, event log, outcome ledger. Expand channels later (WhatsApp/email/web) only after an outcome-driven voice wedge proves recurring revenue.

## Primary pricing and capability references
- Sarvam Voice Agents official pricing: https://docs.sarvam.ai/voice-agents/pricing
- Sarvam voice-agent capabilities: https://www.sarvam.ai/products/voice-agents
- Retell AI pricing: https://www.retellai.com/pricing
- Bolna pricing: https://www.bolna.ai/pricing
- TRAI advice to senders: https://trai.gov.in/advice-to-senders
- TRAI advice to telemarketers: https://trai.gov.in/advice-telemarketers

## Qualitative, **non-representative** buyer signals
- Real-estate price/ROI objection: https://www.reddit.com/r/PropTech/comments/1x0qbu0/had_a_meeting_with_a_real_estate_client_yesterday/
- Real-estate manual lead flow anecdote: https://www.reddit.com/r/AI_Agents/comments/1u8m13n/i_automated_a_real_estate_teams_entire_lead_flow/
- Voice agent receptionist customer frustration and handoff: https://www.reddit.com/r/AIReceptionists/comments/1trosk4/has_anybody_tried_one_of_those_ai_receptionists/

**Evidence and ethics:** public data snapshot only; no direct user-data access in this research repository. Validate claims in live calls and agreements. Local telecom rules and consent requirements vary; do legal/provider onboarding before dialing at scale.