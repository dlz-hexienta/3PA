---
process_id: PR02
process_name: "Service Level Management"
category: procedures
frameworks:
  - itil-v4
  - fitsm
  - it4it
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Service Level Management §3"
  - "FitSM-2: §PR2 SLM"
  - "IT4IT: R2F Service Level Component, Deploy Value Stream"
last_updated: 2026-03-13
status: draft
---

# Service Level Management — Best Practice Procedures

## PROC-SLM-01: Define and Negotiate a New SLA

**Maturity:** Essential | **Trigger:** A new service is being introduced, a customer requests individual service levels, or a default SLA is being established for the first time

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Identify the need for a new or individual SLA: new service entering production, customer request for tailored service levels, or gap identified during service review | Service Level Manager / Relationship Manager | — |
| 2 | Gather customer requirements for service quality: for standardized services, the customer selects from catalogue options; for tailored services, requirements are gathered through direct engagement covering all relevant service quality aspects (functionality, availability, performance, timeliness, support, accuracy, UX) | Service Level Manager / Customer | Service Level Requirements |
| 3 | Conduct viability analysis: verify that the requested service levels can be achieved given available resources, infrastructure capacity, and supplier capabilities. For standardized services this may be automated; for tailored services it requires manual assessment involving service designers, product owners, and supplier managers | Service Designer / Product Owner | — |
| 4a | **If not viable:** Return to the customer with a revised proposal explaining constraints; adjust requirements and repeat viability analysis | Service Level Manager | — |
| 4b | **If viable:** Proceed to drafting | Service Level Manager | — |
| 5 | Draft the SLA using the agreed template, incorporating: service description, agreed targets for each quality aspect, measurement methods, reporting frequency, review schedule, escalation procedures, and remedies for non-compliance. Use existing service specifications and standard clauses as building blocks | Service Level Manager / Service Designer | Draft SLA |
| 6 | Submit the draft SLA to the customer for review and negotiation. For standardized services, the customer confirms standard terms. For tailored services, the customer and service provider negotiate terms, iterating on the draft until acceptable to both parties | Service Level Manager / Customer / Relationship Manager | Draft SLA |
| 7 | Finalize the SLA: obtain formal sign-off from both parties; record the signed SLA in the agreement register | Service Level Manager | Signed SLA |
| 8 | Communicate the SLA to all parties responsible for delivery: initiate required changes to make agreed service levels available, including updates to monitoring configurations, support arrangements, and supplier agreements | Service Level Manager / Service Owner | — |
| 9 | Establish or update corresponding OLAs and UAs to underpin the new SLA commitments (see PROC-SLM-06) | Service Level Manager | OLA / UA |

### Exit Criteria
- Signed SLA recorded in the agreement register
- Customer and all delivery parties notified
- Supporting OLAs/UAs established or updated
- Monitoring configured to track agreed targets

---

## PROC-SLM-02: Evaluate SLA Fulfilment

**Maturity:** Essential | **Trigger:** Defined evaluation interval reached (e.g., monthly) or significant incident affecting service quality

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Collect service performance data for the evaluation period from monitoring systems, incident management records, and service request fulfilment metrics | Service Level Manager | — |
| 2 | Compare actual performance against each SLA target for the period, calculating compliance for each metric (e.g., availability %, resolution time percentile, response time) | Service Level Manager | — |
| 3 | Identify breaches: document each instance where an SLA target was not met, including the extent of the breach, affected service period, and known contributing factors | Service Level Manager | Evaluation Record |
| 4 | Identify near-misses: flag metrics that were met but approached the target threshold, indicating risk of future breach | Service Level Manager | Evaluation Record |
| 5a | **If breach detected:** Notify the customer of the SLA violation through the agreed notification method, within the agreed notification timeframe | Service Level Manager | Violation Notification |
| 5b | **If OLA/UA breach contributed:** Escalate to the responsible internal team lead or supplier manager with details of the failure | Service Level Manager | — |
| 6 | Record the evaluation results in the SLA fulfilment report and update the service quality dashboard | Service Level Manager | SLA Fulfilment Report |
| 7 | Feed breach and near-miss data into the service review process and the continual improvement register | Service Level Manager | — |

### Exit Criteria
- All SLAs evaluated for the period
- Breaches documented and customers notified
- OLA/UA breaches escalated to responsible parties
- Evaluation results recorded and available for service reviews

---

## PROC-SLM-03: Conduct a Service Review

**Maturity:** Intermediate | **Trigger:** Scheduled review cadence reached (e.g., quarterly) or event-based trigger (major incident, customer complaint, organizational change)

### Prerequisites
- SLA fulfilment evaluation data is current for all services in scope
- Customer and user satisfaction data has been collected for the review period
- Service quality monitoring data is available

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Prepare the service review: compile SLA fulfilment data, satisfaction survey results, incident trends, improvement initiative status, and any open issues from the previous review | Service Level Manager / Service Quality Analyst | Review Preparation Pack |
| 2 | Invite relevant stakeholders: service owners, relationship managers, product owners, technical leads, supplier managers, and where appropriate, customer representatives | Service Level Manager | — |
| 3 | Open the review meeting; confirm scope (which services are covered) and available data | Service Owner | — |
| 4 | Review achieved service levels against SLA targets: discuss breaches, near-misses, and trends. Identify whether gaps are due to technical issues, process failures, or misaligned expectations | Service Level Manager | — |
| 5 | Review customer and user satisfaction data: compare perceived quality against measured quality. Identify any watermelon effects (green metrics, red perception) | Service Level Manager / Relationship Manager | — |
| 6 | Review improvement initiative progress: assess whether previously agreed improvement actions have been implemented and whether they are delivering the expected results | Service Owner | — |
| 7 | Identify new improvement opportunities: agree on specific actions, owners, and target dates for addressing quality gaps | Service Owner / Service Level Manager | — |
| 8 | Determine whether any SLA changes are needed: targets that are consistently exceeded (tighten), targets that are systematically missed due to structural constraints (renegotiate), or new quality aspects that need to be covered | Service Level Manager | — |
| 9 | Document all findings, decisions, and action items in the service review report | Service Level Manager | Service Review Report |
| 10 | Distribute the review report to all stakeholders and update the improvement register with new actions | Service Level Manager | — |

### Exit Criteria
- All services in scope reviewed
- Watermelon effects identified and addressed or flagged
- Improvement actions documented with owners and timelines
- SLA change needs identified and routed to the SLA review process
- Review report distributed to stakeholders

---

## PROC-SLM-04: Review and Renew an SLA

**Maturity:** Intermediate | **Trigger:** Scheduled SLA review date reached, customer request for changes, or service review identifies need for SLA modification

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Retrieve the current SLA and its fulfilment history; compile service review findings and any outstanding change requests from the customer | Service Level Manager | SLA, Fulfilment History |
| 2 | Assess whether the current SLA terms remain appropriate: are targets still relevant to business needs? Are measurement methods still valid? Have service dependencies changed? | Service Level Manager / Service Owner | — |
| 3a | **If no changes needed:** Confirm prolongation with the customer; update the SLA validity period and next review date | Service Level Manager / Customer | Updated SLA |
| 3b | **If changes needed:** Document proposed changes and their rationale; conduct viability analysis for any new or revised targets | Service Level Manager / Service Designer | — |
| 4 | Negotiate revised terms with the customer; iterate until agreement is reached | Service Level Manager / Customer / Relationship Manager | Revised Draft SLA |
| 5 | Update corresponding OLAs and UAs to reflect any SLA changes | Service Level Manager | Updated OLA / UA |
| 6 | Formalize the renewed SLA: obtain sign-off, update the agreement register, communicate changes to all delivery parties | Service Level Manager | Renewed SLA |
| 7 | Update monitoring configurations and reporting templates to reflect any target or measurement changes | Service Level Manager | — |

### Exit Criteria
- SLA renewed with updated validity period, or revised terms agreed and signed
- Supporting OLAs/UAs updated to match
- Monitoring and reporting updated to reflect changes
- All parties notified

---

## PROC-SLM-05: Withdraw an SLA

**Maturity:** Essential | **Trigger:** Service being retired, customer relationship ending, or service review determines SLA is no longer needed

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Confirm the withdrawal decision: verify that the triggering condition is valid (service retirement approved, customer offboarding confirmed, or service review decision documented) | Service Level Manager / Service Owner | — |
| 2 | Identify all parties affected by the withdrawal: the customer, internal delivery teams covered by associated OLAs, and suppliers covered by associated UAs | Service Level Manager | — |
| 3 | Notify the customer of the SLA withdrawal with adequate notice as defined by the agreement or policy, including the effective date and any transition arrangements | Service Level Manager / Relationship Manager | Withdrawal Notification |
| 4 | For standardized services, initiate changes to make agreed services unavailable to the customer (may require offboarding project). For tailored services, execute the transition plan including migration to alternative services where applicable | Service Level Manager / Service Owner | — |
| 5 | Terminate or update associated OLAs and UAs: where they supported only this SLA, terminate; where they support other SLAs, update to remove the withdrawn commitments | Service Level Manager | — |
| 6 | Update the agreement register: mark the SLA as withdrawn with the effective date; retain the record for audit and historical reference | Service Level Manager | Agreement Register |
| 7 | Update the service catalogue to reflect the withdrawal (remove or update the affected service entry) | Service Level Manager | Service Catalogue |
| 8 | Decommission monitoring and reporting configurations specific to the withdrawn SLA | Service Level Manager | — |

### Exit Criteria
- Customer notified and transitioned
- SLA marked as withdrawn in the agreement register
- Associated OLAs/UAs terminated or updated
- Service catalogue updated
- Monitoring configurations decommissioned

---

## PROC-SLM-06: Establish or Update Supporting Agreements

**Maturity:** Essential (OLA/UA creation), Intermediate (systematic management) | **Trigger:** New SLA established, SLA revised, new supplier onboarded, or service review identifies underpinning gap

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Identify the supporting agreement need: determine which internal teams and/or external suppliers must deliver operational targets to underpin the SLA commitment | Service Level Manager | — |
| 2 | Derive operational targets from the SLA: translate customer-facing service level targets into specific operational requirements for each contributing party (e.g., infrastructure availability target, application response time target, supplier resolution time target) | Service Level Manager / Service Designer | — |
| 3a | **For internal teams (OLA):** Negotiate the operational targets with the team lead; document in an OLA using the agreed template, covering targets, measurement methods, escalation paths, and review schedule | Service Level Manager / Team Lead | OLA |
| 3b | **For external suppliers (UA):** Work with supplier management to negotiate the operational targets; document in a UA or incorporate into the supplier contract | Service Level Manager / Supplier Manager | UA |
| 4 | Validate alignment: confirm that the aggregate of all OLA and UA commitments will support the SLA targets, accounting for dependencies and handoff points between parties | Service Level Manager | — |
| 5 | Formalize the agreements: obtain sign-off from responsible parties; record in the agreement register | Service Level Manager | Agreement Register |
| 6 | Configure monitoring for OLA/UA targets alongside the parent SLA targets | Service Level Manager | — |
| 7 | Communicate the agreements to all parties and confirm understanding of responsibilities | Service Level Manager | — |

### Exit Criteria
- OLAs and/or UAs documented and signed
- Operational targets validated as sufficient to support parent SLA
- Agreements recorded in the agreement register
- Monitoring configured for all operational targets

---

## PROC-SLM-07: Monitor and Report Service Quality

**Maturity:** Intermediate | **Trigger:** Ongoing (continuous monitoring) and periodic (reporting cycle)

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Collect service quality data continuously from: infrastructure and application monitoring tools, user behaviour analytics, incident management records, and service request fulfilment data | Service Level Manager / Product Owner | — |
| 2 | Collect user and customer feedback: gather impromptu feedback from support interactions and scheduled satisfaction surveys | Service Level Manager / Relationship Manager | — |
| 3 | Aggregate data into the service quality dashboard: combine technical metrics, satisfaction scores, and SLA compliance data into a unified view | Service Level Manager / Service Quality Analyst | Service Quality Dashboard |
| 4 | Identify exceptions: services significantly over or under target, declining trends, or divergence between technical metrics and satisfaction scores (watermelon detection) | Service Level Manager | — |
| 5 | Escalate critical exceptions to service owners for immediate attention | Service Level Manager | — |
| 6 | Produce periodic service quality reports: tailor content to the audience (technical detail for internal teams, business-focused summaries for customers) | Service Level Manager / Service Quality Analyst | Service Quality Report |
| 7 | Distribute reports through agreed channels and at agreed frequencies; make dashboards accessible to authorized stakeholders | Service Level Manager | — |
| 8 | Feed monitoring and reporting outputs into the service review and continual improvement processes | Service Level Manager | — |

### Exit Criteria
- Service quality dashboard updated and accessible
- Periodic reports produced and distributed
- Critical exceptions escalated
- Data available for service reviews and improvement planning
