# Customer discovery + pilots

## Strong starting bets (still hypothetical)
1. **Home services:** 2–20 branch operators with >200 inquiries/month and valuable jobs; job booking and schedule authority matter more than speech demos.
2. **Wholesale/distribution:** operations director or CFO with high-volume purchase orders and painful ERP cash application; end-to-end order-to-cash ROI is directly measurable.
3. **Alternative leveraging prior context:** property leads to attended site visits, but must measure visits held and deals closed, not simply call-connect metrics.

## Interview sample: 20 calls, not one-sided
6 home-services operators (including skeptical businesses), 6 wholesale/distribution ops/finance leaders, 4 field-service/PM firms, 4 independent integrators or industry consultants. Mix small/mid-market and multiple regions. Ask about failures and why they don't buy AI.

## Seven questions
1. Show the most recent *specific* work item that fell through. What exactly happened?
2. What did it cost in missed gross profit, employee hours, late cash, or customer churn?
3. How often does this failure occur? Can the logs/data confirm it?
4. What system contains the true state? Can we safely read AND write it?
5. Which part must be performed by a human or require permission?
6. What are you already spending on labor, software and outsourcing to solve it?
7. Would you run a **paid** 30-day pilot with an outcome target? Who signs?

## Pilot measurement template
Record baseline period, inquiry volume, lead/transaction quality, conversion and fulfilled outcome. Then record agent influence, handoffs, false positives, incorrect action attempts, latency, cancellation, cloud+telephony costs, human QA, setup costs, customer NPS and consent compliance. Propose holdout or matched comparison if practical.

### Minimum reliability gates (initial engineering proposals, not industry standards)
- 0 unauthorized state mutations or unsafe financial commitments
- >95% deterministic integration test success on supported happy-path + failure scenarios before customer pilot
- 100% high-risk actions governed by explicit approval policy
- Every failed action inspectable via trace; source-of-truth always remains consistent
- Error budget and process-specific completion target must be negotiated per workflow

## Decision rules
Keep/expand only when customer reports meaningful finished-outcome gains and fully loaded incremental contribution is positive after support costs. Pause if one-off integration engineering makes onboarding impossible to repeat. Do not claim agent has “fully automated a business” based on a one-week phone test.