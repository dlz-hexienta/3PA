---
process_id: PR12
process_name: "Service Request Management"
category: raci
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
  - "ITIL 4: Service Request Management §4.1 Table 4.2, §4.2"
  - "FitSM-3: §6.9 ISRM Roles"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Request Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

ITIL 4 notes that there are no specialist roles specific to the service request management practice — the key activities are typically performed by technical specialists, service owners, and user support agents using generic competency profiles. The three roles below are synthesized from ITIL 4's activity-role mappings and FitSM's ISRM role model to provide a consistent RACI structure.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SRM | Service Request Manager | All |
| SO | Service Owner | All |
| FA | Fulfilment Agent | All |

## Essential Activities (All tiers)

### Service Request Fulfilment Control
<!-- sources: ITIL 4 SRM §3.2.1 Table 3.2, §4.1 Table 4.2 -->

| Activity | SRM | SO | FA |
|----------|:---:|:--:|:--:|
| Categorize service requests | I | C | A/R |
| Initiate and control model-based fulfilment | I | C | A/R |
| Review fulfilment outcomes | A/R | C | R |
| Maintain service request models | A/R | R | C |
| Manage request catalogue entries | A/R | C | I |

## Intermediate Activities (T2+)

### Exception Handling and Performance Review
<!-- sources: ITIL 4 SRM §3.2.1, §3.2.2, §4.1 Table 4.2 -->

| Activity | SRM | SO | FA |
|----------|:---:|:--:|:--:|
| Control ad hoc fulfilment | C | A/R | R |
| Analyse service request performance | A/R | C | I |
| Initiate service request model improvements | A/R | C | I |

## Advanced Activities (T3)

### Automation and Optimization
<!-- sources: ITIL 4 SRM §2.4.1, §3.2.2, §6 -->

| Activity | SRM | SO | FA |
|----------|:---:|:--:|:--:|
| Communicate model updates | A/R | R | I |
| Optimize fulfilment automation and third-party integration | A/R | R | C |

## Notes

1. **Service Request Manager:** Manages the practice overall — accountable for model maintenance, catalogue accuracy, performance review, and improvement initiation. Competency profile: Methods expert/Administrator (MA) for model work, Technical/Methods expert (TM) for analysis, Coordinator (C) for communications. Corresponds to FitSM process manager ISRM (request scope). In smaller organizations, this role may be combined with the incident management practice manager or service desk manager — the practices share tooling and often team structures.
2. **Service Owner:** Accountable for request models related to their services — participates in model design and testing, makes ad hoc fulfilment decisions, and reviews outcomes for their services. Competency profile: Coordinator/Technical/Administrator (CTA) for ad hoc control, Methods/Coordinator/Technical (MCT) for fulfilment review. Multiple service owners may be involved depending on the request type and affected services.
3. **Fulfilment Agent:** Front-line role performing categorization and fulfilment coordination. Checks prerequisites, selects models, assigns tasks, obtains approvals, and communicates with users. Competency profile: Coordinator/Technical/Methods (CTM) for categorization, Coordinator/Administrator/Technical (CAT) for fulfilment control. Corresponds to FitSM case owner (service request owner) — one assigned per service request, responsible for all lifecycle activities of that specific request.
4. **No Dedicated Teams:** It is unusual to see dedicated organizational structures for service request management. The practice is typically integrated into the day-to-day activities of service delivery and realization teams. The same team structures are often used for service request management as for incident management. However, where services include service requests as part of service utility and demand is very high, dedicated fulfilment teams may be formed for specific request types.
5. **Automation Impact:** As fulfilment automation increases, the fulfilment agent role shifts from performing categorization and fulfilment manually to monitoring and maintaining automated workflows. The service request manager and service owner roles remain — they are responsible for model design, testing, and continuous optimization of automation.
6. **Cross-Practice Involvement:** Fulfilment of a single service request may involve activities from multiple practices — change management, release management, information security, infrastructure management. The RACI above covers only service request management practice activities. Fulfilment agents and service owners may hold additional responsibilities in those practices for the duration of request fulfilment.
