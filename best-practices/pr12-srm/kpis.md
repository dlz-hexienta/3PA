---
process_id: PR12
process_name: "Service Request Management"
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
  - "ITIL 4: Service Request Management §2.4, §2.5 Table 2.3"
  - "FitSM-1: §PR9.1–§PR9.5"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Request Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the practice matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Service request management KPIs are mapped to two practice success factors: (1) ensuring that service request fulfilment procedures for all services are optimized, and (2) ensuring that all service requests are fulfilled according to agreed procedures and to user satisfaction. Metrics should be aggregated into composite indicators appropriate to the organization's strategy and the value streams to which the practice contributes.

---

## Essential KPIs (All tiers)

### KPI-SRM-01: Request Catalogue Completeness
<!-- sources: ITIL 4 SRM §2.5 Table 2.3 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of active services that have fully documented request models and corresponding request catalogue entries. Completeness means every request type available to users has a tested model with defined procedures, responsibilities, approvals, and fulfilment targets. Gaps in catalogue coverage mean users cannot access pre-agreed service actions — forcing ad hoc handling that is slower, more expensive, and less predictable |
| **Formula** | (Service request types with documented and deployed models / Total identified service request types) × 100 |
| **Target** | ≥ 95% |
| **Frequency** | Quarterly |
| **Data Source** | Request catalogue, service request model repository |
| **Owner** | Service Request Manager |

### KPI-SRM-02: SLA Fulfilment Rate
<!-- sources: ITIL 4 SRM §2.5 Table 2.3 PSF2, FitSM-1 §PR9.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service requests fulfilled within the target fulfilment time defined in the applicable SLA. This is the primary measure of fulfilment performance — directly reflecting whether the practice delivers on its commitments to users. Unlike incidents, service requests have predictable timelines. Consistently meeting SLA targets validates that request models are realistic and that capacity is adequate |
| **Formula** | (Service requests fulfilled within SLA target / Total service requests fulfilled) × 100 |
| **Target** | ≥ 90%; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Service request management system |
| **Owner** | Service Request Manager |

### KPI-SRM-03: Request Recording Completeness
<!-- sources: ITIL 4 SRM §3.2.1, FitSM-1 §PR9.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service requests that are properly registered, classified, and prioritised according to the agreed scheme. Consistent recording is essential for performance analysis, demand forecasting, and model improvement. Incomplete or inconsistent recording undermines all downstream metrics and improvement efforts |
| **Formula** | (Requests registered with complete classification and priority / Total requests received) × 100 |
| **Target** | 100% |
| **Frequency** | Monthly |
| **Data Source** | Service request management system |
| **Owner** | Service Request Manager |

### KPI-SRM-04: First-Time Fulfilment Rate
<!-- sources: ITIL 4 SRM §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service requests fulfilled correctly on the first attempt — without requiring rework, reclassification, or re-routing. A high first-time rate indicates that request models are accurate, categorization is effective, and fulfilment teams are well-trained. A low rate suggests model deficiencies, categorization errors, or capability gaps that increase cost and delay fulfilment |
| **Formula** | (Requests fulfilled without rework or reclassification / Total requests fulfilled) × 100 |
| **Target** | ≥ 85%; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Service request management system, reclassification records |
| **Owner** | Service Request Manager |

---

## Intermediate KPIs (T2+)

### KPI-SRM-05: User Satisfaction with Request Fulfilment
<!-- sources: ITIL 4 SRM §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Satisfaction of users with the quality and timeliness of service request fulfilment — the primary user-facing measure of PSF2. Covers both the outcome (did the user get what they requested?) and the experience (was the process convenient and well-communicated?). Should be measured for different request types and channels to identify type-specific and channel-specific issues |
| **Formula** | Average satisfaction score from post-fulfilment survey (scale 1–5 or equivalent) |
| **Target** | ≥ 4.0 / 5.0; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Post-fulfilment satisfaction surveys |
| **Owner** | Service Request Manager |

### KPI-SRM-06: Average Fulfilment Time
<!-- sources: ITIL 4 SRM §2.5 Table 2.3 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average time from service request submission to fulfilment completion — measured by request type and model. Provides a basis for validating SLA targets, identifying bottlenecks, and assessing model efficiency. Should be analysed alongside SLA fulfilment rate — a high SLA rate with long average times suggests generous targets rather than efficient fulfilment |
| **Formula** | Average (Fulfilment completion timestamp − Request submission timestamp); by request type |
| **Target** | Trending downward; within SLA targets |
| **Frequency** | Monthly |
| **Data Source** | Service request management system |
| **Owner** | Service Request Manager |

### KPI-SRM-07: Fulfilment Procedure Adherence
<!-- sources: ITIL 4 SRM §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service requests fulfilled by following the agreed request model procedure — without deviations, workarounds, or ad hoc steps. Measures whether fulfilment teams are using the designed procedures. Low adherence indicates model deficiencies (procedures are impractical), training gaps, or tooling limitations. Deviations should trigger model review |
| **Formula** | (Requests fulfilled according to agreed procedure / Total requests fulfilled) × 100 |
| **Target** | ≥ 90%; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Service request management system, quality audits |
| **Owner** | Service Request Manager |

### KPI-SRM-08: Ad Hoc Fulfilment Rate
<!-- sources: ITIL 4 SRM §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service requests requiring ad hoc (non-standard) fulfilment — where the standard model could not be followed due to exceptions, model gaps, or procedure errors. A high ad hoc rate indicates that request models are incomplete or that categorization is misdirecting requests to inappropriate models. Each ad hoc fulfilment should be analysed and fed into model improvement |
| **Formula** | (Requests requiring ad hoc fulfilment / Total requests) × 100 |
| **Target** | ≤ 10%; trending downward |
| **Frequency** | Monthly |
| **Data Source** | Service request management system, exception records |
| **Owner** | Service Request Manager |

---

## Advanced KPIs (T3)

### KPI-SRM-09: Fulfilment Automation Rate
<!-- sources: ITIL 4 SRM §2.5 Table 2.3 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service requests with fully or largely automated fulfilment — measured both as a proportion of the request catalogue (how many types are automated) and as a proportion of total request volume (how much demand is handled automatically). Automation reduces per-request cost, improves fulfilment speed, and enables self-service. Should be monitored alongside satisfaction to ensure automation does not degrade user experience |
| **Formula** | (Requests fulfilled via automated workflow / Total requests) × 100; and (Automated request types / Total request types) × 100 |
| **Target** | Trending upward; target calibrated to organization |
| **Frequency** | Quarterly |
| **Data Source** | Service request management system, automation platform |
| **Owner** | Service Request Manager |

### KPI-SRM-10: Fulfilment Cost per Request
<!-- sources: ITIL 4 SRM §2.5 Table 2.3 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average cost of fulfilling a service request — including staff time, technology costs, third-party charges, and overhead — measured by request type and model. Provides a basis for automation business cases, model optimization, and service pricing. Lower cost per request indicates operational efficiency, but must be balanced against satisfaction and quality |
| **Formula** | Total fulfilment costs / Total requests fulfilled; by request type |
| **Target** | Stable or declining; proportionate to request value |
| **Frequency** | Quarterly |
| **Data Source** | Financial records, service request management system |
| **Owner** | Service Request Manager |

### KPI-SRM-11: Request Model Improvement Rate
<!-- sources: ITIL 4 SRM §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service request models reviewed and improved within the review period — indicating the pace of continual improvement in the practice. Covers model updates initiated from performance analysis, exception feedback, user satisfaction data, and technology opportunities. A low improvement rate may indicate stagnation — models not keeping pace with evolving services and user expectations |
| **Formula** | (Request models improved in period / Total active request models) × 100 |
| **Target** | Trending upward; target calibrated to organizational maturity |
| **Frequency** | Quarterly |
| **Data Source** | Improvement records, model change log |
| **Owner** | Service Request Manager |

### KPI-SRM-12: Fulfilment-Attributable Incident Rate
<!-- sources: ITIL 4 SRM §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and impact of incidents caused by incorrect fulfilment of service requests — measuring the quality risk of fulfilment activities. Incorrect fulfilment (misconfigured access, wrongly deployed software, improperly moved equipment) can cause service disruptions. A high rate indicates model deficiencies, quality check gaps, or fulfilment team capability issues. Each fulfilment-attributable incident should trigger review of the relevant request model |
| **Formula** | Number of incidents attributed to incorrect service request fulfilment; and business impact of those incidents |
| **Target** | Zero or near-zero; trending downward |
| **Frequency** | Monthly |
| **Data Source** | Incident records, problem records, service request management system |
| **Owner** | Service Request Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SRM-01 | Request Catalogue Completeness | All | Quarterly |
| SRM-02 | SLA Fulfilment Rate | All | Monthly |
| SRM-03 | Request Recording Completeness | All | Monthly |
| SRM-04 | First-Time Fulfilment Rate | All | Monthly |
| SRM-05 | User Satisfaction with Request Fulfilment | T2+ | Monthly |
| SRM-06 | Average Fulfilment Time | T2+ | Monthly |
| SRM-07 | Fulfilment Procedure Adherence | T2+ | Monthly |
| SRM-08 | Ad Hoc Fulfilment Rate | T2+ | Monthly |
| SRM-09 | Fulfilment Automation Rate | T3 | Quarterly |
| SRM-10 | Fulfilment Cost per Request | T3 | Quarterly |
| SRM-11 | Request Model Improvement Rate | T3 | Quarterly |
| SRM-12 | Fulfilment-Attributable Incident Rate | T3 | Monthly |
