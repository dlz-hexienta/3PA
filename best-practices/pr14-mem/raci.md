---
process_id: PR14
process_name: "Monitoring & Event Management"
category: raci
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Monitoring & Event Management §4.1 Table 4.1, §4.2"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Monitoring & Event Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

ITIL 4 notes that it is rare for a dedicated monitoring and event management team to exist — monitoring is usually performed by people responsible for service delivery and operations. The event handling process should be fully automated, with roles focusing on oversight rather than execution. The three roles below are synthesized from ITIL 4's activity-role mappings across the monitoring planning, event handling, and MEM review processes.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| MC | MEM Coordinator | T2+ |
| MS | Monitoring Specialist | T2+ |
| SO | Service Owner | T2+ |

## Essential Activities (T2+)

### Monitoring Planning and Event Handling
<!-- sources: ITIL 4 MEM §3.2.1 Table 3.2, §3.2.2, §4.1 Table 4.1 -->

| Activity | MC | MS | SO |
|----------|:--:|:--:|:--:|
| Define monitoring objectives and scope | A/R | C | R |
| Assess monitoring capabilities and define metrics | C | A/R | I |
| Define event types, thresholds, and classification rules | C | A/R | C |
| Detect, log, and classify events | I | A/R | I |
| Execute event response procedures | I | A/R | I |

## Intermediate Activities (T2+)

### Health Models, Correlation, and Action Plans
<!-- sources: ITIL 4 MEM §3.2.1 Table 3.2, §4.1 Table 4.1 -->

| Activity | MC | MS | SO |
|----------|:--:|:--:|:--:|
| Define service health models | C | A/R | R |
| Define event correlations and rule sets | C | A/R | C |
| Map events to action plans and responsible teams | A/R | R | C |

## Advanced Activities (T3)

### Review and Technology Optimization
<!-- sources: ITIL 4 MEM §3.2.3 Table 3.6, §4.1 Table 4.1 -->

| Activity | MC | MS | SO |
|----------|:--:|:--:|:--:|
| Conduct post-mortem reviews and optimize event management | A/R | R | C |
| Evaluate and adopt monitoring technologies | A/R | R | I |

## Notes

1. **MEM Coordinator:** Manages the practice overall — coordinates monitoring planning across services, oversees event handling effectiveness, initiates reviews, and ensures stakeholder access to monitoring data. Competency profile: Coordinator/Administrator (CA) for planning, Administrator/Technical/Methods (ATM) for action mapping, Technical/Methods/Administrator (TMA) for reviews. In many organizations, this role is performed by an operations manager, delivery manager, or service management office function rather than a dedicated MEM role.
2. **Monitoring Specialist:** The primary technical role — implements monitoring systems, defines thresholds and correlation rules, builds health models, configures automation, and evaluates new technologies. Competency profile: Technical/Methods (TM) for threshold and metric work, Technical/Methods/Administrator (TMA) for health models and correlation. This role requires deep expertise in monitoring tools, infrastructure, network and application monitoring, AI/ML techniques, and automation. Multiple specialists may be needed depending on the breadth of the technology estate.
3. **Service Owner:** Provides the business context for monitoring — defines what matters from a service value perspective, contributes user experience requirements to health models, and participates in post-mortem reviews. Competency profile: Coordinator/Administrator (CA) for objective definition, Technical/Methods/Administrator (TMA) for health models. Multiple service owners participate depending on which services are being planned or reviewed.
4. **No Dedicated Teams:** It is rare for a dedicated MEM team to exist. Monitoring is typically planned during service design and operated by service delivery teams. People responsible for monitoring should be involved at the design stage, and teams that developed the service should be available for service handover to operations. This includes architects, software development teams, infrastructure teams, designers, availability/continuity/capacity/performance specialists, and testers.
5. **Event Handling Automation:** The event handling process (activities 4–5) should be fully automated. The monitoring specialist role in these activities is oversight — ensuring automation is functioning correctly, reviewing response errors, and maintaining correlation rules. Human intervention in individual event processing should be the exception, not the norm.
6. **Cross-Practice Involvement:** Monitoring planning involves input from many practices — service design, service level management, availability management, capacity and performance management, information security management, and infrastructure management. The RACI above covers only MEM practice activities. Monitoring specialists and service owners participate in these other practices' activities when monitoring requirements are being defined.
