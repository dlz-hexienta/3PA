---
process_id: PR06
process_name: "Availability Management"
category: kpis
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
  - "ITIL 4: Availability Management §2.4, §2.5 Table 2.5"
  - "FitSM-2: §PR4 SACM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Availability Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Availability management KPIs are mapped to three practice success factors: (1) identifying service availability requirements, (2) measuring, assessing, and reporting service availability, and (3) treating service availability risks.

---

## Essential KPIs (All tiers)

### KPI-AM-01: Service Availability Achievement
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF3, §2.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The actual availability of each service compared against its agreed availability target during the reporting period. This is the primary indicator of the availability management practice's effectiveness. Calculated using the agreed availability formula — typically (agreed service time − downtime) / agreed service time — and reported for each service with an agreed availability target. Deviations from targets must be investigated |
| **Formula** | (Agreed service time − downtime) / Agreed service time × 100; reported per service |
| **Target** | As agreed per service in the SLA (commonly 99.5%–99.99%); all services meeting or exceeding target |
| **Frequency** | Monthly |
| **Data Source** | Monitoring tools, incident records (ITSM tool) |
| **Owner** | Availability Manager |

### KPI-AM-02: Number of Service Disruptions
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF3, §2.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The count of service disruptions (availability incidents) per service during the reporting period. Measures the frequency of service failures. A high or increasing number of disruptions indicates reliability issues even if total downtime remains within targets. Reported per service and compared against the agreed target or previous periods |
| **Formula** | Count of availability incidents per service per period |
| **Target** | Meeting agreed target or trending downward |
| **Frequency** | Monthly |
| **Data Source** | Incident records, monitoring tools (ITSM tool) |
| **Owner** | Availability Manager |

### KPI-AM-03: Total Service Downtime
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF3, §2.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The cumulative duration of service unavailability per service during the reporting period. Measures the total impact of all service disruptions. A service may meet its availability percentage target but still have unacceptable total downtime. Reported per service alongside the number of disruptions to provide a complete picture |
| **Formula** | Sum of downtime duration for all availability incidents per service per period |
| **Target** | Meeting agreed target or trending downward |
| **Frequency** | Monthly |
| **Data Source** | Monitoring tools, incident records (ITSM tool) |
| **Owner** | Availability Manager |

### KPI-AM-04: Maximum Single Service Outage
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF3, §2.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The duration of the longest single service outage per service during the reporting period. Financial and business losses often grow exponentially during an extended outage — a single long outage may be far more damaging than multiple short outages with the same total duration. Provides a critical complement to the total downtime metric. Reported per service and compared against the agreed maximum or previous periods |
| **Formula** | Maximum single outage duration per service per period |
| **Target** | Meeting agreed maximum outage target; trending downward |
| **Frequency** | Monthly |
| **Data Source** | Monitoring tools, incident records (ITSM tool) |
| **Owner** | Availability Manager |

---

## Intermediate KPIs (T2+)

### KPI-AM-05: Mean Time Between Failures (MTBF)
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF3, §2.1, §2.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average elapsed time between service failures (availability incidents) per service during the reporting period. Measures service reliability — a higher MTBF indicates greater reliability. Provides a frequency-based view that is more meaningful than simple disruption counts for services with varying reporting periods |
| **Formula** | (Agreed service time − total downtime) / Number of service disruptions; reported per service |
| **Target** | Meeting agreed target; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Monitoring tools, incident records (ITSM tool) |
| **Owner** | Availability Manager |

### KPI-AM-06: Mean Time to Restore Service (MTRS)
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF3, §2.1, §2.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average elapsed time from the start of a service disruption to the restoration of full service, per service during the reporting period. Measures the speed of service restoration — a lower MTRS indicates faster recovery. Together with MTBF, MTRS determines the overall availability of a service. Services designed for high availability should balance high MTBF with short MTRS |
| **Formula** | Total downtime / Number of service disruptions; reported per service |
| **Target** | Meeting agreed target; trending downward |
| **Frequency** | Monthly |
| **Data Source** | Monitoring tools, incident records (ITSM tool) |
| **Owner** | Availability Manager |

### KPI-AM-07: Availability Requirements Documentation Rate
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of products and services (with agreed availability targets) that have clearly documented availability criteria — including what constitutes unavailability, the vital business functions supported, and measurable availability targets. Measures the completeness of availability requirement identification |
| **Formula** | (Products/services with documented availability criteria / Total products/services with agreed availability targets) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | SLAs, availability requirements documents |
| **Owner** | Availability Manager |

### KPI-AM-08: Availability Monitoring Coverage
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of products and services (with agreed availability targets) that are covered by availability monitoring — meaning that service outages are being tracked and recorded using one or more of the defined measurement methods. Measures the organization's ability to detect and measure service unavailability |
| **Formula** | (Products/services covered by availability monitoring / Total products/services with agreed availability targets) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Monitoring configuration, ITSM tool |
| **Owner** | Availability Manager |

### KPI-AM-09: Availability Reporting Coverage
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of products and services (with agreed availability targets) that are included in regular service availability reports. Measures the completeness of availability reporting to stakeholders. Services with availability targets that are not reported on cannot be effectively managed |
| **Formula** | (Products/services included in availability reports / Total products/services with agreed availability targets) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Service availability reports |
| **Owner** | Availability Manager |

### KPI-AM-10: Availability SLA Achievement Rate
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF1, PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of services that met or exceeded all of their agreed availability targets during the reporting period. Provides an aggregate view of availability performance across the service portfolio. Combines individual service availability achievements into a single practice-level measure |
| **Formula** | (Services meeting all agreed availability targets / Total services with agreed availability targets) × 100 |
| **Target** | ≥ 95%; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Service availability reports, SLA data |
| **Owner** | Availability Manager |

---

## Advanced KPIs (T3)

### KPI-AM-11: Effectiveness of Availability Controls
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF3, §2.4.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of implemented availability controls that are achieving their intended risk reduction — measured by comparing actual service availability performance in areas covered by controls against the expected performance without those controls. Controls that are not achieving their intended effect should be reviewed, strengthened, or replaced |
| **Formula** | (Controls achieving intended risk reduction / Total implemented controls) × 100 |
| **Target** | ≥ 90%; non-effective controls identified and addressed |
| **Frequency** | Semi-annually |
| **Data Source** | Availability management plans, availability data, risk assessments |
| **Owner** | Availability Manager |

### KPI-AM-12: Availability Loss Ratio
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF3, §2.4.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The ratio between actual losses due to service unavailability and the expected losses based on risk assessments. Measures whether the organization's availability controls are reducing losses to the expected level. A ratio greater than 1.0 indicates that actual losses exceed expectations, suggesting that controls are insufficient or that risk assessments need revision. Loss categories include productivity, response costs, replacement costs, SLA fines, competitive advantage, and reputation |
| **Formula** | Actual losses due to unavailability / Expected losses (from risk assessments) |
| **Target** | ≤ 1.0; trending downward |
| **Frequency** | Semi-annually |
| **Data Source** | Loss event data, risk assessments, financial records |
| **Owner** | Availability Manager |

### KPI-AM-13: Timely Updating of Availability Requirements
<!-- sources: ITIL 4 Availability Management §2.5 Table 2.5 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service changes that triggered a timely review and update of the service's availability requirements. Business needs and customer demand change over time — availability requirements must be revised accordingly. Measures whether the organization keeps availability requirements current as services evolve |
| **Formula** | (Service changes with timely availability requirement review / Total service changes affecting availability) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Change records, availability requirements documents |
| **Owner** | Availability Manager |

### KPI-AM-14: Service Health Model Coverage
<!-- sources: ITIL 4 Availability Management §2.2.5, §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of critical services that have a validated service health model — enabling accurate service-level availability measurement from infrastructure monitoring data. Service health models are most valuable for complex, critical services where infrastructure monitoring alone cannot accurately determine service availability. Measures the organization's progress in developing sophisticated availability measurement capability |
| **Formula** | (Critical services with validated service health models / Total critical services) × 100 |
| **Target** | Trending upward; ≥ 80% for critical services |
| **Frequency** | Semi-annually |
| **Data Source** | Service health model inventory, service catalogue |
| **Owner** | Availability Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| AM-01 | Service Availability Achievement | All | Monthly |
| AM-02 | Number of Service Disruptions | All | Monthly |
| AM-03 | Total Service Downtime | All | Monthly |
| AM-04 | Maximum Single Service Outage | All | Monthly |
| AM-05 | Mean Time Between Failures (MTBF) | T2+ | Monthly |
| AM-06 | Mean Time to Restore Service (MTRS) | T2+ | Monthly |
| AM-07 | Availability Requirements Documentation Rate | T2+ | Quarterly |
| AM-08 | Availability Monitoring Coverage | T2+ | Quarterly |
| AM-09 | Availability Reporting Coverage | T2+ | Quarterly |
| AM-10 | Availability SLA Achievement Rate | T2+ | Monthly |
| AM-11 | Effectiveness of Availability Controls | T3 | Semi-annually |
| AM-12 | Availability Loss Ratio | T3 | Semi-annually |
| AM-13 | Timely Updating of Availability Requirements | T3 | Quarterly |
| AM-14 | Service Health Model Coverage | T3 | Semi-annually |
