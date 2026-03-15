---
process_id: PR06
process_name: "Availability Management"
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
  - "ITIL 4: Availability Management §4.1 Table 4.2, §4.2 Table 4.3"
  - "FitSM-2: §PR4 SACM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Availability Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. The availability manager is accountable for all availability management activities. In smaller organizations, availability management responsibilities may be performed by the service owner, with technical specialists providing monitoring and infrastructure expertise.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| AM | Availability Manager | All |
| SO | Service Owner | All |
| TS | Technical Specialist | All |

## Essential Activities (All tiers)

### Establish Service Availability Control
<!-- sources: ITIL 4 Availability Management §3.2.1 Table 3.2, §4.1 Table 4.2 -->

| Activity | AM | SO | TS |
|----------|:--:|:--:|:--:|
| Identify service availability requirements | A/R | R | C |
| Agree service availability requirements | A | R | C |
| Determine availability monitoring approach | A/R | C | R |
| Design availability metrics and reports | A/R | C | C |

### Monitor and Report Service Availability
<!-- sources: ITIL 4 Availability Management §3.2.2 Table 3.4, §4.1 Table 4.2, FitSM-2 §PR4 SACM -->

| Activity | AM | SO | TS |
|----------|:--:|:--:|:--:|
| Collect availability data | A | I | R |
| Validate data against availability criteria | A/R | C | R |
| Produce the availability report | A/R | C | I |
| Distribute the availability report | A | R | I |

## Intermediate Activities (T2+)

### Analyse and Improve Service Availability
<!-- sources: ITIL 4 Availability Management §3.2.2 Table 3.4, §4.1 Table 4.2 -->

| Activity | AM | SO | TS |
|----------|:--:|:--:|:--:|
| Analyse availability data | A/R | C | R |
| Identify deviations, risks, and improvement opportunities | A/R | C | C |
| Assess availability risks and design controls | A/R | C | R |
| Produce the availability management plan | A/R | C | C |
| Initiate changes and improvements | A/R | I | I |

## Advanced Activities (T3)

### Optimize Availability Controls
<!-- sources: ITIL 4 Availability Management §2.4.3 -->

| Activity | AM | SO | TS |
|----------|:--:|:--:|:--:|
| Inventory existing availability controls | A/R | C | R |
| Assess control effectiveness | A/R | C | C |
| Assess control efficiency (cost-benefit) | A/R | C | C |
| Recommend optimizations | A/R | C | C |
| Update availability management plans | A/R | I | I |

### Develop and Maintain Service Health Models
<!-- sources: ITIL 4 Availability Management §2.2.5, §2.4.2 -->

| Activity | AM | SO | TS |
|----------|:--:|:--:|:--:|
| Analyse service architecture | A | C | R |
| Map component-to-service impact relationships | A/R | C | R |
| Define impact rules and thresholds | A/R | C | R |
| Validate the model | A/R | R | C |
| Maintain the model | A | C | R |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The availability manager is accountable for all availability management activities — from establishing availability control through analysis, planning, optimization, and service health model development.
2. **Role Combining:** In smaller organizations, the availability manager role may be combined with the service continuity administrator, IT risk manager, or service owner role. The key requirement is that accountability for availability management is explicitly assigned. Where the role is combined with the service owner, the service owner performs both the service-level and the practice-level responsibilities.
3. **Availability Manager:** Accountable for ensuring cost-efficient availability management across services. Analyses availability data, designs metrics and reports, plans and designs controls, assesses control effectiveness and efficiency, and drives practice improvement. This role is advisory and analytical — the availability manager does not typically implement infrastructure changes directly but initiates changes through the change management process.
4. **Service Owner:** Provides the service-level perspective on availability requirements and achievements. Participates in identifying and agreeing requirements with customers, distributing availability reports, and reviewing availability performance. The service owner may serve as the primary interface with customers for availability discussions, working alongside the service level management practice.
5. **Technical Specialist:** Provides technical expertise on monitoring tools, infrastructure, and availability controls. Collects and validates availability data, performs component-level availability analysis, configures monitoring, and implements availability controls. Includes system administrators, infrastructure engineers, monitoring tool administrators, and service designers. Technical specialists advise on fault-tolerant technologies, resilience measures, and service health model development.
6. **Suppliers and Partners:** External suppliers are not listed as a separate RACI role but participate in availability management through their contractual arrangements. Availability requirements must be negotiated and agreed with suppliers. Suppliers may provide resilience technologies and services (fault tolerance, clustering, load balancing, backup systems). Supplier availability performance feeds into overall service availability analysis.
