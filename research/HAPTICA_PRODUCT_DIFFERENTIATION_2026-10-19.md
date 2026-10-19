# Haptica founder product call — Revenue Missions, not voice bots
**Decision date:** 2026-10-19
**Status:** Product thesis for implementation design and customer validation. Existing code and deploy state must be audited first.

## Founder call
Keep Haptica's existing AI voice agent platform and expose it as **Voice Studio**, but **make Haptica Missions (Revenue Autopilot) the flagship product**. Its unit of work is a persistent *business outcome*, not a call or campaign. The first vertical solution uses opted-in real-estate enquiries and tracks **lead -> qualification -> slot -> confirmed visit -> visit held -> rep disposition**. It operates until completion, explicit customer refusal/opt-out, blocked/human escalated, or workflow closure. The broader AI-native business infrastructure vision is modular future expansion of this verified mission engine.

### No false novelty
Sarvam, Vapi, Retell and EliseAI already offer many combinations of voice agents, workflows, tool calls, analytics, lead qualification, reminders and follow-up. These individual features are table stakes. The differentiated hypothesis is to **combine source-of-truth execution, multi-party coordination, exception recovery, outcome evidence and measurement** into a simple usable system, for one underserved buyer, and prove an advantage with pilots. Do not claim no competitors offer this.

## Five signature product capabilities (ranked)
**P0-A Revenue Leak Radar:** ingest opted-in enquiry/CRM/calendar events and detect specific objectively recorded stalled transitions (no response within customer SLA, interested but unbooked, booking pending confirmation, missing assigned rep, canceled/no-show, unresolved post-visit). Present severity based on configured business value/urgency and evidence availability. "Revenue at risk" is an **estimate**, not booked revenue, and requires grounded assumptions.

**P0-B Recovery Missions:** a durable per-lead workflow with next action, permissible channel, explicit business owner, retry policy, opt-out, budget, time window, state and outcome. AI chooses among authorized voice call, message, human task and approved API action. Record intents vs successful side effects separately. No endless loops or automated unapproved follow-up.

**P0-C Two-sided coordination:** orchestrate the prospect and the business operator: find a real calendar slot, ask a human sales rep to accept/confirm an assignment via approved channel, share a concise handoff packet, confirm the appointment, reconcile attendance/no-show, schedule a respectful authorized recovery. A bot saying "booked" is not a successful booking.

**P0-D Outcome Evidence Ledger:** for each claimed outcome retain authoritative source (booking ID, calendar event, CRM field, visit check-in or rep confirmation), timestamp, verification state, attribution method, and reversible action log. Show 'proposed', 'committed', 'externally verified', and 'unverified'; compute conversion funnel and cost per verified held visit. When the source isn't available, never invent conversion proof.

**P1-E Failure-to-Regression Lab:** taxonomy for transcript/data errors, false tool success, slow calls, mistaken names, no-shows and lost handoffs; generate replayable synthetic/sanitized tests, approve fixes in staging, canary compare against baseline, detect regressions; never deploy autonomous prompt mutations uncontrolled. Build after product loop works.

### Additional product design bets
- Channel-switch assistance: instead of forcing email or property codes over voice, send a verification link on an allowed channel, preserving mission context. No broad WhatsApp promise without actual legal/technical integration.
- Business memory: permission-scoped customer preferences, events and live authoritative records rather than an ever-growing prompt. Don't join tenant data.
- ROI lab: instrument matched cohorts/holdouts where feasible; distinguish correlation and attribution, separate booked vs attended vs closed, factor provider costs and human QA.
- Smart economics: configurable per-mission and tenant spend caps; retries based on explicit policy, not guessed conversion uplift.
- Honest autonomy: approval policies, explainable next actions, human rescue queue, no unsafe financial promises.

## Exact first customer story
1. A prospective buyer submits a first-party inquiry with documented calling consent.
2. An event creates a **Mission** with prospect ID, consent provenance, campaign/project, source/expected value assumptions, SLA and permitted actions.
3. Radar checks owner assignment, contact freshness and whether an action is overdue.
4. Voice calls in an allowed window. AI confirms identity, qualifies requirement, checks live data and offers a real slot.
5. System atomically reserves/commits the slot via authoritative scheduling tool; it does not invent availability. Confirm via approved channel and write CRM.
6. Assigned sales rep gets context, appointment and acceptance task. If not accepted by policy deadline, escalate/notify backup (not an unapproved infinite call cascade).
7. Before the meeting, a consented reminder or response flow can reschedule or cancel, making the calendar consistent.
8. After the meeting, attendance is verified from source (CRM/check-in/rep); no reply -> 'unverified', not 'attended'. The mission routes to the next human step or a permitted follow-up.
9. Outcome Ledger logs source evidence, total metered cost and verified milestone.
10. Pilot dashboard compares with a valid historical/matched baseline; never call estimated uplift 'attributed revenue'.

## UX navigation decision
**Home: Outcome Command Center** — verified outcomes, at-risk missions, blocked action queue, fully-loaded cost and SLA.
**Missions** — grouped by event stage + evidence status; timeline and next best authorized action; human takeover.
**Radar** — funnel leak breakdown with linked actual records; **not** speculative fake sales numbers.
**Voice Studio** — existing agent creator/configuration/scripts/KB/test audio.
**Campaigns** — existing compliant contact and schedule tools.
**Experiment Lab** — stage later.
**Integrations & Guardrails** — CRM/calendar/messages/telephony, identity, consent, approvals, budgets.
**Billing** — model-minute and phone costs, cap and per-outcome metrics.
Avoid building a replacement full CRM or visual automation platform at first release.

## Canonical mission data (minimum)
```
Mission {
  id, tenant_id, playbook_id, contact_ref, source_system, source_record_id,
  mission_state, outcome_state, consent_provenance, channel_permissions,
  configured_sla, assigned_human_id, action_policy, budget_cap,
  last_attempt_at, next_action_at, next_action_kind, next_action_reason,
  verification_state, proof_refs[], total_real_cost, created_at, updated_at
}
MissionEvent {
  event_id, mission_id, source, event_type, occurred_at, payload_ref,
  idempotency_key, precondition_ref, external_action_ref, actor, status, error
}
OutcomeProof {
  mission_id, milestone, external_system, record_id, observed_at,
  captured_at, verification_method, confidence_label, disputed_at
}
```
Voice calls are *events/actions* within missions, not the root object. The event ledger needs tenancy enforcement, immutable audit, idempotency, safe PII references, limited retention, and compensation for failed partial actions. State transitions must be deterministic where possible.

## Workflow state and escalation
`new -> contacted -> qualified -> booking_requested -> booked_confirmed -> visit_held -> rep_followup`; terminal `won/lost/declined/opted_out/expired`; exception `needs_human/unverified/integration_error/blocked`. Do not conflate proposed booking, slot held, booking confirmed or visit attended. Permission-gated actions only; retries with defined caps; follow local consent/Do Not Call restrictions.

## Integration/adoption strategy
**Never rip-and-replace the existing CRM**: attach to existing source-of-truth and generate an action receipt for each write. Start with one real calendar provider and one CRM/webhook path. After first two paying implementations succeed without customer-specific branching, add reusable packs. Customer setup must only ask for business goal, agent, authorized contacts/integrations, spend cap and workflow template.

## Existing repos: audit before work
- `haptica-voice-agent-service` README already documents versions, packs, workflows, tools and guarded evaluations — reuse rather than rebuilding a second workflow engine.
- `haptica-campaign-service` README documents contact lists, schedules, idempotency, spend-triggering runs and caps — attach Mission scheduling carefully to existing ownership/contracts.
- `haptica-crm-service` README has contact timeline, opportunities and **atomic collision-safe booking**; however it says calendar sync and outbound confirmation delivery are not built yet.
- `haptica-analytics-service` README has call/campaign/lead event ingestion and booked funnel fields, but it is not proof of externally verified visits or causality.
- `haptica-frontend` README describes Next 15 UI and localStorage `X-Auth` tokens and some security/pruning issues.
- `haptica-identity-service` README labels its state as a walking skeleton. Public signup should follow audited identity completion.
- Don't touch existing product repos until versioned API/event contracts and deployment-state audit are understood. Preserve senior team production changes. Research repo is separate/public.

## Work sequence (no speculative reskin)
**Sprint 0 — 3 days:** current working call audit, delivery/code versus docs gap, domain event and booking source-of-truth mapping, 12 negative test scenarios; 3 live interview recordings if appropriately consented. Establish baseline and live code versions.
**Sprint 1 — 7 days:** Mission object + ingestion + event provenance + Radar first two leak rules + CRM-linked action receipts; narrow single funnel.
**Sprint 2 — 7 days:** real booking external confirmation, salesperson acceptance/handoff queue, safe retry/escalation, cancellation/reschedule; test truthfulness.
**Sprint 3 — 7–14 days:** outcome proof, verified funnel with costs, pilot deployment to 1–2 paid design partners; iterate from failures. Studio and generic features not rewritten.
**Sprint 4 — after pilots:** staging replay/regression lab, multi-channel integration, better analytics and pack templates; only if economics and renewal signal support it.

### Kill criteria
- Customer cannot provide consent evidence or authoritative outcome records -> do not use automated outbound/win claims.
- Verified outcome is worse than control/baseline after fully loaded costs -> change approach, not vanity report.
- Every customer requires bespoke integration patching -> narrow CRM or vertical; fix repeatability.
- Customer refuses to pay for reliable workflow despite effective prototype -> reconsider ICP or outcome promise.

## Commercial hypothesis
Charge for infrastructure/usage transparently and optional premium for verified, attributable outcome milestones; don't advertise a guarantee without attribution and written conditions. *Buyers pay for reliable conversions and saved labor, not minutes spoken.* Initial focus on sales teams with incoming qualified inquiries, not indiscriminate cold dialing. Later expand mission templates to home-services bookings, e-commerce abandoned checkout, account renewals, operational handoffs and legitimate collections under separate compliance controls.

## Sources checked Oct 19, 2026
- Sarvam full feature and workflow support: https://www.sarvam.ai/products/voice-agents
- Sarvam voice agents Genie: https://docs.sarvam.ai/voice-agents/build/genie
- Vapi features/testing/AB: https://vapi.ai/platform
- Retell post-call analytics: https://www.retellai.com/features/post-call-analysis
- EliseAI follow-ups including no-show (2026 update): https://support.meetelise.com/hc/en-us/articles/32499730992653-LeasingAI-Outreach-Messages-and-Follow-ups
- A community member reports fewer interruptions but potential ~8% conversion drop (unverified anecdote, no causal inference): https://www.reddit.com/r/AI_Agents/comments/1x7x6rf/what_ive_learnt_from_using_an_ai_voice_agent_in/
- Developer's reported production lessons (anecdote): https://www.reddit.com/r/AiAutomations/comments/1svvt7h/what_i_learned_after_1500_ai_calls_for_a_client/
- Prior research: `data/research.json`, `research/STRATEGY.md`, `research/VOICE_LAUNCH_DECISION_2026-10-19.md`.

**Confidence:** Product hypothesis; no signed buyer commitments, no verified product revenue lift, and no live end-to-end production audit implied.
