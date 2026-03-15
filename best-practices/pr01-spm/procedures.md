---
process_id: PR01
process_name: "Service Portfolio Management"
category: procedures
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Portfolio Management"
  - "FitSM-2: §PR1 SPM"
  - "IT4IT: Evaluate Value Stream, Portfolio Function"
last_updated: 2026-03-13
status: draft
---

# Service Portfolio Management — Best Practice Procedures

## PROC-SPM-01: Submit a New Service Proposal

**Maturity:** Essential | **Trigger:** Demand for a new or significantly changed service is identified

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Identify the demand signal (customer request, strategic initiative, market opportunity, or improvement initiative) | Business Analyst / Service Requestor | — |
| 2 | Complete the Service Proposal Template, including: business justification, target consumers, estimated scope, expected value, and alignment to strategic objectives | Business Analyst | Service Proposal |
| 3 | Submit the proposal to the Service Portfolio Manager for initial completeness review | Business Analyst | Service Proposal |
| 4 | Review the proposal for completeness: all required fields populated, business justification present, no duplicate of an existing service or proposal | Service Portfolio Manager | Service Proposal |
| 5a | **If incomplete:** Return to submitter with specific gaps to address; go to step 2 | Service Portfolio Manager | — |
| 5b | **If complete:** Accept the proposal into the portfolio pipeline with status "Proposed" | Service Portfolio Manager | Service Portfolio Register |
| 6 | Notify the submitter that the proposal has been accepted for evaluation | Service Portfolio Manager | — |

### Exit Criteria
- Proposal recorded in the portfolio register with status "Proposed"
- Submitter notified of acceptance

---

## PROC-SPM-02: Evaluate a Service Proposal

**Maturity:** Essential | **Trigger:** A new proposal has been accepted into the pipeline (status: Proposed)

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Retrieve the service proposal and the documented assessment criteria | Service Portfolio Manager | Service Proposal, Assessment Criteria |
| 2 | Assess strategic alignment: does the proposal support one or more strategic objectives? | Service Portfolio Manager | — |
| 3 | Assess feasibility: are the required capabilities, resources, and budget available or obtainable? | Business Analyst / Finance Manager | — |
| 4 | Check for duplication: does a similar service already exist in the portfolio (pipeline, catalogue, or retired)? | Service Portfolio Manager | Service Portfolio Register |
| 5 | Score the proposal against the assessment criteria and document the evaluation rationale | Service Portfolio Manager | Evaluation Record |
| 6a | **If criteria met:** Recommend approval; advance proposal to the next portfolio review or, for urgent items, to the portfolio owner for expedited approval | Service Portfolio Manager | — |
| 6b | **If criteria not met:** Reject with documented rationale; update status to "Rejected" | Service Portfolio Manager | Service Portfolio Register |
| 7 | Notify the submitter of the evaluation outcome | Service Portfolio Manager | — |

### Exit Criteria
- Proposal evaluated and scored against criteria
- Status updated to "Evaluated" (pending review) or "Rejected"

---

## PROC-SPM-03: Conduct a Portfolio Review

**Maturity:** Intermediate | **Trigger:** Scheduled review cadence reached (e.g., quarterly) or ad hoc review called

### Prerequisites
- Portfolio monitoring data is current
- Portfolio assessment report has been prepared
- All pending proposals with status "Evaluated" are queued for review

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Prepare the review agenda: pending proposals, portfolio performance summary, optimization recommendations | Portfolio Coordinator | Review Agenda |
| 2 | Distribute pre-read materials to all review participants at least 5 business days before the review | Portfolio Coordinator | — |
| 3 | Open the review meeting; confirm quorum and decision authority | Service Portfolio Owner | — |
| 4 | Review portfolio performance: value realization, investment balance (GtB vs. RtB), exceptions and trends | Service Portfolio Manager | Portfolio Health Dashboard |
| 5 | For each pending proposal: present the evaluation, discuss, and decide (approve / defer / reject) | Service Portfolio Owner + Review Board | — |
| 6 | For existing portfolio items: decide on reprioritization, continued investment, or retirement candidates | Service Portfolio Owner + Review Board | — |
| 7 | Review and approve any proposed changes to the portfolio management approach or models | Service Portfolio Owner | — |
| 8 | Document all decisions, action items, and owners in the Portfolio Review Report | Portfolio Coordinator | Portfolio Review Report |
| 9 | Distribute the review report to all stakeholders within 3 business days | Portfolio Coordinator | — |
| 10 | Update the service portfolio register to reflect all decisions (status changes, priority updates) | Service Portfolio Manager | Service Portfolio Register |

### Exit Criteria
- All agenda items addressed with documented decisions
- Portfolio register updated to reflect review outcomes
- Review report distributed to stakeholders

---

## PROC-SPM-04: Monitor Portfolio Performance

**Maturity:** Intermediate | **Trigger:** Ongoing (continuous or at defined intervals)

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Collect performance data for each portfolio item: service levels achieved, financial actuals, adoption metrics, customer satisfaction | Service Portfolio Manager | — |
| 2 | Compare actuals against the planned value-realization criteria defined in the service proposal or scope agreement | Service Portfolio Manager | — |
| 3 | Identify exceptions: services significantly over/under budget, missing service level targets, or with declining adoption | Service Portfolio Manager | — |
| 4 | Produce portfolio item health reports highlighting exceptions, trends, and risks | Service Portfolio Manager | Portfolio Item Health Report |
| 5 | Escalate critical exceptions to the Service Portfolio Owner for immediate attention | Service Portfolio Manager | — |
| 6 | Feed monitoring results into the next periodic portfolio assessment | Service Portfolio Manager | — |

### Exit Criteria
- Portfolio item health reports produced
- Critical exceptions escalated
- Data available for periodic assessment

---

## PROC-SPM-05: Retire a Service

**Maturity:** Essential | **Trigger:** Portfolio review decision to retire a service, or end-of-life reached

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Confirm the retirement decision is recorded in the portfolio register and a portfolio review report | Service Portfolio Manager | Portfolio Review Report |
| 2 | Identify all current consumers of the service and their dependencies | Service Portfolio Manager | Service Portfolio Register |
| 3 | Develop a retirement plan: consumer communication timeline, migration path to replacement service (if any), data retention requirements, contractual obligations | Service Portfolio Manager | Retirement Plan |
| 4 | Communicate the retirement plan to all affected consumers with adequate notice (as defined by policy) | Service Portfolio Manager / Relationship Manager | — |
| 5 | Execute consumer migration: support transition to replacement services, update service catalogue | Service Portfolio Manager | Service Catalogue |
| 6 | Verify all consumers have migrated and no active dependencies remain | Service Portfolio Manager | — |
| 7 | Decommission the service: remove from the service catalogue, retain in the portfolio register with status "Retired" | Service Portfolio Manager | Service Portfolio Register |
| 8 | Address residual obligations: data retention, audit trails, contractual wind-down | Service Portfolio Manager | — |
| 9 | Conduct a post-retirement review to capture lessons learned | Service Portfolio Manager | Lessons Learned Record |

### Exit Criteria
- Service removed from catalogue, retained in portfolio register as "Retired"
- All consumers migrated or notified
- Residual obligations documented and assigned
- Lessons learned captured

---

## PROC-SPM-06: Manage Scope Agreements

**Maturity:** Advanced | **Trigger:** A portfolio backlog item is approved for implementation

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Create a scope agreement from the approved portfolio backlog item, capturing: description, business entity, anticipated business value, proposed budget (build + run), acceptance criteria, and delivery timeline | Investment Manager / Service Portfolio Manager | Scope Agreement |
| 2 | Validate the labour and asset consumption model against available resource pools | Investment Manager | — |
| 3 | Define tangible and intangible benefits with measurable targets | Investment Manager / Business Analyst | — |
| 4 | Submit the scope agreement for approval through the governance model (expedited for urgent items, structured for planned cycles) | Service Portfolio Manager | — |
| 5 | **If approved:** Update status to "Active"; link to delivery project and architecture roadmap item | Service Portfolio Manager | Scope Agreement, Portfolio Register |
| 6 | **If deferred/rejected:** Update status accordingly; notify requesting party with rationale | Service Portfolio Manager | — |
| 7 | During delivery: track progress against the scope agreement; review change requests for scope, budget, or timeline adjustments | Investment Manager | — |
| 8 | On delivery completion: compare actual outcomes against planned benefits; update the scope agreement with actuals | Investment Manager | Scope Agreement |
| 9 | Feed value-realization results back into portfolio monitoring | Service Portfolio Manager | — |

### Exit Criteria
- Scope agreement created, approved, and linked to delivery
- Benefits tracked from approval through delivery
- Value realization data fed back into portfolio monitoring
