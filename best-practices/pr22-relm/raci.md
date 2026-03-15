---
process_id: PR22
process_name: "Relationship Management"
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
  - "ITIL 4: Relationship Management §4.1, §4.2, Table 4.2"
  - "FitSM-2: §PR7 CRM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (relationship coordination)"
last_updated: 2026-03-13
status: draft
---

# Relationship Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. Organizations at lower tiers may combine roles (e.g., the relationship manager may also perform relationship agent functions at T1, or the relationship manager role may be combined with the service level manager).

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| RM | Relationship Manager | All |
| RA | Relationship Agent | T2+ |
| SLM | Service Level Manager | All |
| SO | Service Owner | All |

## Essential Activities (All Tiers)

### Stakeholder Identification and Database Management
<!-- sources: FitSM-2 §PR7 CRM (identify customers, maintain database), ITIL 4 Relationship Management §2.2.4, §3.2.2 Table 4.2 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Identify customers and stakeholders receiving or affected by services | A/R | C | C | C |
| Collect stakeholder information and communication preferences | A/R | R | C | C |
| Register stakeholders in the customer/stakeholder database | A | R | I | I |
| Map stakeholder influence and interest to determine engagement approach | A/R | C | C | C |
| Review and update stakeholder records periodically | A | R | I | I |
| Communicate database changes to dependent processes | A/R | I | I | I |

### Service Reviews
<!-- sources: FitSM-2 §PR7 CRM (perform service reviews), ITIL 4 Relationship Management §3.2.2 Table 3.4, Table 4.2 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Schedule the service review according to the agreed cadence | A/R | C | C | I |
| Prepare the review pack (performance data, SLA achievement, complaints, satisfaction) | A | R | R | C |
| Conduct the service review meeting | A/R | R | R | C |
| Document outcomes and agreed actions | A | R | C | I |
| Distribute the service review report | A | R | I | I |
| Track agreed actions to completion | A | R | C | C |

### Complaint Handling
<!-- sources: FitSM-2 §PR7 CRM (handle complaints), ITIL 4 Relationship Management §3.2.2 Table 3.4 (managing exceptions) -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Receive and register the complaint in the complaints log | A | R | — | — |
| Acknowledge receipt to the customer | A | R | — | — |
| Assign the complaint for investigation | A/R | C | C | C |
| Investigate the complaint and identify root causes | A | R | C | C |
| Determine resolution and corrective actions | A/R | C | C | C |
| Communicate the resolution to the customer | A | R | — | I |
| Close the complaint and record lessons learned | A | R | I | I |

### Satisfaction Measurement
<!-- sources: FitSM-2 §PR7 CRM (manage satisfaction), ITIL 4 Relationship Management §2.5 Table 2.5 PSF3 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Define the satisfaction measurement approach | A/R | C | C | — |
| Design or update the satisfaction survey instrument | A/R | C | C | — |
| Distribute the survey to customers | A | R | — | — |
| Collect, compile, and analyse responses | A | R | C | — |
| Report satisfaction results to management | A/R | C | I | I |
| Initiate follow-up actions where satisfaction is below target | A/R | R | C | C |

### Relationship Model Application
<!-- sources: ITIL 4 Relationship Management §3.2.2 Tables 3.3, 3.4 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Identify the applicable relationship model for new stakeholders | A/R | C | C | — |
| Follow the relationship model in ongoing interactions | A | R | — | — |

## Intermediate Activities (T2+)

### Culture and Strategy Analysis
<!-- sources: ITIL 4 Relationship Management §3.2.1 Table 3.2 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Analyse the organization's culture and its impact on relationships | A/R | C | C | C |
| Analyse the organization's strategy and implications for stakeholder relationships | A/R | C | C | C |
| Produce stakeholder maps and culture assessments | A/R | C | — | — |

### Relationship Principles and Models Development
<!-- sources: ITIL 4 Relationship Management §3.2.1 Tables 3.1, 3.2, §2.4.1 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Define key principles of relationships | A/R | C | C | C |
| Develop relationship models for key stakeholder groups | A/R | C | C | C |
| Validate principles and models with stakeholders and leadership | A/R | R | C | C |
| Communicate principles and embed through training and awareness | A/R | R | I | I |
| Publish relationship models for use by relationship agents | A/R | I | I | — |

### Conflict Resolution and Exception Management
<!-- sources: ITIL 4 Relationship Management §2.2.2, §3.2.2 Table 3.4 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Identify relationship conflicts and toxic behaviour patterns | A/R | R | C | C |
| Intervene to resolve conflicts and manage exceptions | A/R | R | C | C |
| Propose updates to relationship models based on conflict patterns | A/R | C | — | — |

### Relationship Review
<!-- sources: ITIL 4 Relationship Management §3.2.1 Table 3.2, §3.2.2 Table 3.4, §2.4.2 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Gather relationship health data (satisfaction, complaints, conflicts, internal feedback) | A | R | C | C |
| Assess the health and effectiveness of key relationships | A/R | C | C | C |
| Assess internal relationship health (team collaboration, climate) | A/R | C | — | — |
| Identify improvement opportunities and document findings | A/R | C | I | I |
| Communicate review findings and register improvements | A/R | I | I | I |

## Advanced Activities (T3)

### Organization-Wide Relationship Approach Governance
<!-- sources: ITIL 4 Relationship Management §3.2.1 Table 3.2 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Monitor adoption and effectiveness of relationship principles and models | A/R | R | C | C |
| Adjust the relationship approach based on outcomes and strategic changes | A/R | C | C | C |
| Conduct formal culture analysis for cultural development recommendations | A/R | C | — | — |

### Non-Service Stakeholder Management
<!-- sources: ITIL 4 Relationship Management §2.4.3.2 -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Identify and analyse non-service stakeholders (regulators, media, industry groups, investors) | A/R | C | — | — |
| Define engagement approaches for each non-service stakeholder group | A/R | C | — | — |
| Conduct and monitor non-service stakeholder engagement activities | A | R | — | — |
| Report on non-service stakeholder relationship health | A/R | C | — | I |

### Cross-Boundary Relationship Coordination
<!-- sources: ITIL 4 Relationship Management §6, SIAM Service Integration -->

| Activity | RM | RA | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Map cross-boundary relationship touchpoints | A/R | R | C | C |
| Align relationship principles across organizational boundaries | A/R | C | C | — |
| Establish coordination mechanisms and mutual transparency arrangements | A/R | R | C | — |
| Operate coordinated cross-boundary relationship activities | A | R | C | — |
| Review and adjust cross-boundary arrangements | A/R | C | C | I |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The relationship manager is accountable for all relationship management activities — both strategic (relationship approach, principles, models) and operational (stakeholder database, service reviews, complaints, satisfaction).
2. **Role Combining:** At T1, the relationship manager performs all activities directly, including those assigned to the relationship agent at higher tiers. The relationship manager role may also be combined with the service level manager or service owner role at T1. The key requirement is that accountability for relationship health is explicitly assigned to someone.
3. **Relationship Agent:** The relationship agent role is a T2+ specialization. Relationship agents maintain day-to-day relationships with assigned stakeholder groups — they may be account managers, customer relationship managers, sales agents, or service desk leads, depending on the stakeholder type and organizational structure. They follow the relationship models developed by the relationship manager.
4. **Service Level Manager as Partner:** The service level manager works alongside relationship management, particularly in service reviews and complaint handling. SLM provides the service performance data and SLA governance framework; relationship management provides the stakeholder engagement and satisfaction management. They are complementary, not competing, roles.
5. **Service Owner Participation:** Service owners are consulted on activities affecting their services (complaint investigation, service reviews, satisfaction follow-up) because they hold domain knowledge about service delivery. They are informed of outcomes that affect their service strategy.
6. **Cross-Practice Integration:** Many relationship management activities interface with other processes (Service Level Management provides SLA data for reviews, Continual Improvement receives relationship improvement initiatives, Service Desk handles day-to-day user interactions). The RACI matrix covers only the relationship management side of these interfaces — each partnering process has its own RACI for its activities.
