---
process_id: PR02
process_name: "Service Level Management"
category: raci
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
  - "ITIL 4: Service Level Management §4"
  - "FitSM-2: §PR2 SLM"
  - "IT4IT: R2F Service Level Component"
last_updated: 2026-03-13
status: draft
---

# Service Level Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. Organizations at lower tiers may combine roles (e.g., service owner and service level manager may be the same person at T1).

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SO | Service Owner | All |
| SLM | Service Level Manager | All |
| RM | Relationship Manager | T2+ |
| SD | Service Designer | T2+ |
| PO | Product Owner | T2+ |
| SQA | Service Quality Analyst | T3 |
| SM | Supplier Manager | T3 |
| AM | Account Manager | T3 |

## Essential Activities (All Tiers)

### Management of SLAs

| Activity | SO | SLM | RM | SD | PO | SQA | SM | AM |
|----------|:--:|:---:|:--:|:--:|:--:|:---:|:--:|:--:|
| Define the SLM approach and templates | A | R | — | — | — | — | — | — |
| Establish the initial service catalogue | I | A/R | — | — | — | — | — | — |
| Add a new service to the catalogue | A | R | — | — | — | — | — | — |
| Update or remove a service catalogue entry | A | R | — | — | — | — | — | — |
| Gather customer requirements for service levels | C | A/R | — | — | — | — | — | — |
| Conduct viability analysis | C | I | — | R | — | — | — | — |
| Draft a new SLA | A | R | — | C | — | — | — | — |
| Negotiate SLA terms with the customer | C | R | — | — | — | — | — | — |
| Approve and sign the SLA | A/R | R | — | — | — | — | — | — |
| Communicate SLA to delivery parties | I | A/R | — | — | — | — | — | — |
| Establish a default SLA | A | R | — | C | — | — | — | — |
| Define and notify SLA violation method | A | R | — | — | — | — | — | — |
| Evaluate SLA fulfilment | A | R | — | — | — | — | — | — |
| Notify customer of SLA violation | I | A/R | — | — | — | — | — | — |
| Establish OLA with internal team | I | A/R | — | C | — | — | — | — |
| Establish UA with external supplier | I | A/R | — | — | — | — | — | — |
| Evaluate OLA / UA fulfilment | I | A/R | — | — | — | — | — | — |
| Escalate OLA / UA violation | I | A/R | — | — | — | — | — | — |
| Initiate SLA withdrawal | A | R | — | — | — | — | — | — |
| Execute SLA withdrawal and offboarding | I | A/R | — | — | — | — | — | — |

### Oversight of Service Quality

| Activity | SO | SLM | RM | SD | PO | SQA | SM | AM |
|----------|:--:|:---:|:--:|:--:|:--:|:---:|:--:|:--:|
| Collect service performance data | I | A/R | — | — | — | — | — | — |
| Compare actuals against SLA targets | I | A/R | — | — | — | — | — | — |
| Record evaluation results | I | A/R | — | — | — | — | — | — |

## Intermediate Activities (T2+)

### Management of SLAs

| Activity | SO | SLM | RM | SD | PO | SQA | SM | AM |
|----------|:--:|:---:|:--:|:--:|:--:|:---:|:--:|:--:|
| Document detailed service level requirements | C | A | R | C | — | — | — | — |
| Conduct viability analysis (tailored services) | C | C | I | A/R | R | — | C | — |
| Draft SLA for tailored services | A | R | C | C | — | — | — | — |
| Negotiate SLA with customer (tailored) | C | R | A/R | C | — | — | — | — |
| Review SLA at scheduled interval | A | R | R | C | — | — | — | — |
| Prolong SLA after review | A | R | C | — | — | — | — | — |
| Renegotiate SLA terms based on review findings | C | R | A/R | C | — | — | C | — |
| Update OLA/UA to reflect SLA changes | I | A/R | I | C | — | — | C | — |

### Oversight of Service Quality

| Activity | SO | SLM | RM | SD | PO | SQA | SM | AM |
|----------|:--:|:---:|:--:|:--:|:--:|:---:|:--:|:--:|
| Conduct customer and user satisfaction surveys | I | A | R | — | — | — | — | — |
| Monitor service quality continuously | A | R | — | — | R | — | — | — |
| Prepare service review materials | I | C | — | — | R | — | — | — |
| Conduct service review meeting | A | R | R | C | C | — | — | — |
| Document service review findings and actions | I | A/R | C | — | — | — | — | — |
| Distribute service review report | I | I | A/R | — | — | — | — | — |
| Produce service quality reports | I | A | — | — | R | — | — | — |
| Distribute service quality reports to customers | I | I | A/R | — | — | — | — | — |
| Identify improvement opportunities from reviews | R | A | C | C | — | — | — | — |

## Advanced Activities (T3)

### Management of SLAs

| Activity | SO | SLM | RM | SD | PO | SQA | SM | AM |
|----------|:--:|:---:|:--:|:--:|:--:|:---:|:--:|:--:|
| Manage SLA lifecycle for key accounts | I | C | C | — | — | — | — | A/R |
| Automate SLA drafting for standardized services | I | A | — | R | — | — | — | — |
| Automate viability checking against capacity data | I | A | — | R | — | — | — | — |
| Automate SLA expiry and renewal workflows | I | A/R | — | — | — | — | — | I |
| Negotiate UAs with strategic suppliers | I | C | — | — | — | — | A/R | — |
| Coordinate cross-supplier service level governance | I | R | — | — | — | — | A | — |
| Establish service integration agreements | I | C | — | C | — | — | A/R | — |

### Oversight of Service Quality

| Activity | SO | SLM | RM | SD | PO | SQA | SM | AM |
|----------|:--:|:---:|:--:|:--:|:--:|:---:|:--:|:--:|
| Implement end-to-end service level monitoring | I | A | — | R | — | R | — | — |
| Instrument service contracts at deployment | I | C | — | R | — | — | — | — |
| Analyse service quality across multiple dimensions | I | C | — | — | — | A/R | — | — |
| Detect watermelon effects systematically | I | C | R | — | — | A/R | — | — |
| Track multi-supplier end-to-end SLA compliance | I | R | — | — | — | R | A | — |
| Conduct cross-supplier service review meetings | I | R | C | — | — | C | A | — |
| Provide self-service service contract access to customers | I | A | — | — | — | — | — | R |
| Produce predictive service quality analytics | I | C | — | — | — | A/R | — | — |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". Where the service owner is A, the service level manager typically executes (R).
2. **Role Combining:** At T1, the service owner and service level manager roles may be held by the same person. At T1, relationship manager and service designer activities are absorbed by the service level manager.
3. **Customer Involvement:** The customer participates directly in requirements definition, SLA negotiation, and service reviews. Customer involvement is represented through the Relationship Manager role, who acts as the customer liaison.
4. **Two-Process Structure:** Activities are organized into two sub-processes (Management of SLAs and Oversight of Service Quality) following the ITIL 4 practice structure. Both operate in parallel.
5. **Supplier Manager at T3:** At T2, supplier-related activities (UA negotiation, escalation) are handled by the service level manager. At T3, the supplier manager role takes accountability for these activities.
