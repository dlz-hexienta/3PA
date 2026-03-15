---
process_id: PR08
process_name: "Capacity & Performance Management"
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
  - "ITIL 4: Capacity & Performance Management §4.1 Table 4.2, §4.2"
  - "FitSM-2: §PR5 CAPM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Capacity & Performance Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. The capacity and performance manager is accountable for all capacity and performance management activities. In smaller organizations, capacity and performance management responsibilities may be performed by the service owner or combined with other practice roles, with technical specialists providing monitoring and infrastructure expertise.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| CPM | Capacity & Performance Manager | All |
| SO | Service Owner | All |
| TS | Technical Specialist | All |

## Essential Activities (All tiers)

### Establish Service Capacity and Performance Control
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.1 Table 3.2, §4.1 Table 4.2 -->

| Activity | CPM | SO | TS |
|----------|:---:|:--:|:--:|
| Identify service capacity and performance requirements | A/R | R | C |
| Agree service capacity and performance requirements | A | R | C |
| Determine capacity and performance monitoring approach | A/R | C | R |
| Design capacity and performance metrics and reports | A/R | C | C |

### Monitor and Report Service Capacity and Performance
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.2 Table 3.4, §4.1 Table 4.2, FitSM-2 §PR5 CAPM -->

| Activity | CPM | SO | TS |
|----------|:---:|:--:|:--:|
| Collect capacity and performance data | A | I | R |
| Validate data against performance criteria | A/R | C | R |
| Produce the capacity and performance report | A/R | C | I |
| Distribute the capacity and performance report | A | R | I |

## Intermediate Activities (T2+)

### Analyse and Improve Service Capacity and Performance
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.2 Table 3.4, §4.1 Table 4.2 -->

| Activity | CPM | SO | TS |
|----------|:---:|:--:|:--:|
| Analyse capacity and performance data | A/R | C | R |
| Identify deviations, risks, and improvement opportunities | A/R | C | C |
| Assess capacity and performance risks and design controls | A/R | C | R |
| Produce the capacity plan | A/R | C | C |
| Initiate changes and improvements | A/R | I | I |

## Advanced Activities (T3)

### Optimize Capacity and Performance Controls
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.3 -->

| Activity | CPM | SO | TS |
|----------|:---:|:--:|:--:|
| Inventory existing capacity and performance controls | A/R | C | R |
| Assess control effectiveness | A/R | C | C |
| Assess control efficiency (cost-benefit) | A/R | C | C |
| Recommend optimizations | A/R | C | C |
| Update capacity plans | A/R | I | I |

### Model and Forecast Capacity Demand
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.1, §3.2.1 Table 3.2, §3.2.2 Table 3.4 -->

| Activity | CPM | SO | TS |
|----------|:---:|:--:|:--:|
| Analyse business activity patterns and demand forecasts | A/R | C | R |
| Model resource requirements for demand scenarios | A/R | C | R |
| Evaluate architectural options and scaling strategies | A/R | C | R |
| Produce long-term capacity forecasts | A/R | C | C |
| Provide input to IT budget planning | A/R | I | I |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The capacity and performance manager is accountable for all capacity and performance management activities — from establishing capacity and performance control through analysis, planning, optimization, and demand modelling.
2. **Role Combining:** In smaller organizations, the capacity and performance manager role may be combined with the availability manager, service owner, or other practice roles. Where service providers are responsible for a limited number of services and components, a dedicated capacity and performance manager coordinates practices, functions, and organizations. The key requirement is that accountability for capacity and performance management is explicitly assigned.
3. **Capacity & Performance Manager:** Accountable for ensuring cost-efficient service capacity and sufficient performance levels across services. Analyses capacity and performance data, designs metrics and reports, produces capacity plans, and drives practice improvement. This role requires strong business and technical knowledge combined with communication and advocacy skills — practitioners must ensure that capacity concerns and prognoses are heard, measured, and addressed during service design, negotiations, and operation.
4. **Service Owner:** Provides the service-level perspective on capacity and performance requirements and achievements. Participates in identifying and agreeing requirements with customers, distributing performance reports, and reviewing capacity plans. The service owner may serve as the primary interface with customers for performance discussions, working alongside the service level management practice.
5. **Technical Specialist:** Provides technical expertise on infrastructure, applications, monitoring tools, and capacity technologies. Collects and validates capacity and performance data, performs component-level analysis, configures monitoring, and implements capacity controls. Includes system administrators, infrastructure engineers, cloud architects, monitoring tool administrators, and service designers. Technical specialists advise on scaling options, load balancing configurations, and architectural alternatives.
6. **Suppliers and Partners:** External suppliers are not listed as a separate RACI role but participate in capacity and performance management through their contractual arrangements. In multi-vendor environments, a service integration function should maintain the end-user focus of all performance management efforts. Suppliers may provide capacity and scaling technologies and services. Service providers should be incentivized to communicate performance issues to a centralized entity to support rapid coordination.
