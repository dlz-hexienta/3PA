---
process_id: PR08
process_name: "Capacity & Performance Management"
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
  - "ITIL 4: Capacity & Performance Management §2.4, §2.5 Table 2.2"
  - "FitSM-2: §PR5 CAPM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Capacity & Performance Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Capacity and performance management KPIs are mapped to three practice success factors: (1) identifying service capacity and performance requirements, (2) measuring, assessing, and reporting service performance and capacity, and (3) treating service capacity and performance risks.

---

## Essential KPIs (All tiers)

### KPI-CPM-01: Service Performance Achievement
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF2, §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The actual performance of each service compared against its agreed performance target during the reporting period. This is the primary indicator of the capacity and performance management practice's effectiveness. Performance is measured using the agreed metrics — typically including response times, transaction throughput, and processing rates — and reported for each service with agreed performance targets. Deviations from targets must be investigated |
| **Formula** | Per service: actual performance measured against agreed performance criteria (response time, throughput, etc.) |
| **Target** | As agreed per service in the SLA; all services meeting or exceeding target |
| **Frequency** | Monthly |
| **Data Source** | Monitoring tools, application performance monitoring, incident records (ITSM tool) |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-02: Number of Performance Degradations
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF3, §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The count of performance degradation incidents per service during the reporting period. Measures the frequency of performance failures where service degradation exceeded the agreed acceptable threshold and affected a significant number of users. A high or increasing number of degradations indicates capacity constraints or architectural issues even if total degradation duration remains within targets |
| **Formula** | Count of performance degradation incidents per service per period |
| **Target** | Meeting agreed target or trending downward |
| **Frequency** | Monthly |
| **Data Source** | Monitoring tools, incident records (ITSM tool) |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-03: Capacity Utilization Against Thresholds
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.3, §3.2.1 Table 3.2, FitSM-2 §PR5 CAPM -->

| Attribute | Value |
|-----------|-------|
| **Description** | The capacity utilization of key service components compared against agreed thresholds during the reporting period. Measures whether the organization is maintaining adequate capacity headroom. Components approaching or exceeding capacity thresholds require action — either scaling, load balancing, or architectural change. Reported per component or component group alongside the agreed threshold |
| **Formula** | Current utilization / agreed capacity threshold per key component; percentage of components within threshold |
| **Target** | All key components within agreed thresholds; no unplanned threshold breaches |
| **Frequency** | Monthly |
| **Data Source** | Infrastructure monitoring tools, cloud orchestration tools |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-04: Unplanned Capacity and Performance Upgrades
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number of unplanned capacity and performance upgrades to products, services, and components during the reporting period. Unplanned upgrades indicate that capacity planning has failed to anticipate demand — either requirements were not properly identified, demand forecasts were inaccurate, or capacity plans were not implemented in time. A decreasing trend indicates improving proactive capacity management |
| **Formula** | Count of unplanned capacity/performance upgrades per period |
| **Target** | Trending downward; ≤ agreed maximum |
| **Frequency** | Monthly |
| **Data Source** | Change records, incident records (ITSM tool) |
| **Owner** | Capacity & Performance Manager |

---

## Intermediate KPIs (T2+)

### KPI-CPM-05: Capacity and Performance Requirements Documentation Rate
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of products and services (with agreed performance targets) that have capacity and performance requirements clearly documented in SLAs — including critical service actions, performance criteria, metrics, and monitoring approach. Measures the completeness of capacity and performance requirement identification |
| **Formula** | (Products/services with documented CPM requirements / Total products/services with agreed performance targets) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | SLAs, capacity and performance requirements documents |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-06: Performance Requirements Match Rate
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of new or changed operational products and services that match the capacity and performance requirements documented in SLAs. Measures whether services are being designed and deployed with adequate capacity to meet their agreed performance levels. A gap between documented requirements and actual service delivery indicates issues in the service design or transition process |
| **Formula** | (New/changed products/services matching CPM requirements / Total new/changed operational products/services) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Service acceptance records, performance testing results, SLAs |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-07: Capacity and Performance Monitoring Coverage
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of products and services (with agreed performance targets) that have defined capacity and performance metrics and are actively monitored. Measures the organization's ability to detect and measure performance degradation and capacity exhaustion. Services with performance targets that are not monitored cannot be effectively managed |
| **Formula** | (Products/services with active CPM monitoring / Total products/services with agreed performance targets) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Monitoring configuration, ITSM tool |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-08: Capacity and Performance Reporting Coverage
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of products and services (with agreed performance targets) that are included in regular service capacity and performance reports. Measures the completeness of performance reporting to stakeholders. Services with performance targets that are not reported on cannot be effectively governed |
| **Formula** | (Products/services included in CPM reports / Total products/services with agreed performance targets) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Service capacity and performance reports |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-09: Performance SLA Achievement Rate
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF1, PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of services that met or exceeded all of their agreed capacity and performance targets during the reporting period. Provides an aggregate view of capacity and performance across the service portfolio. Combines individual service performance achievements into a single practice-level measure |
| **Formula** | (Services meeting all agreed CPM targets / Total services with agreed performance targets) × 100 |
| **Target** | ≥ 95%; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Service capacity and performance reports, SLA data |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-10: Capacity Plan Coverage
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.2 Table 3.3, FitSM-2 §PR5 CAPM -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of services requiring capacity plans that have current, maintained capacity plans in place. Capacity plans document current levels, anticipated demand changes, and recommended actions. A service without a current capacity plan is at risk of unplanned capacity shortfalls |
| **Formula** | (Services with current capacity plans / Total services requiring capacity plans) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Capacity plan inventory |
| **Owner** | Capacity & Performance Manager |

---

## Advanced KPIs (T3)

### KPI-CPM-11: Capacity and Performance Loss Ratio
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The ratio between actual losses due to insufficient capacity and performance and the expected losses based on risk assessments. Measures whether the organization's capacity and performance controls are reducing losses to the expected level. A ratio greater than 1.0 indicates that actual losses exceed expectations, suggesting that controls are insufficient or that risk assessments need revision. Loss categories include productivity reduction, response costs, replacement costs, SLA fines, competitive advantage, and reputation |
| **Formula** | Actual losses due to insufficient capacity/performance / Expected losses (from risk assessments) |
| **Target** | ≤ 1.0; trending downward |
| **Frequency** | Semi-annually |
| **Data Source** | Loss event data, risk assessments, financial records |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-12: Improvement Initiative Enactment Rate
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of improvement initiatives logged by capacity and performance management practitioners that have been enacted — submitted through the change process and implemented. Measures whether the practice's analysis and recommendations are being translated into actual improvements. A low enactment rate may indicate barriers to implementation, insufficient business case support, or misalignment with organizational priorities |
| **Formula** | (Enacted improvement initiatives / Total logged CPM improvement initiatives) × 100 |
| **Target** | ≥ 80%; trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Continual improvement register, change records |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-13: Timely Updating of CPM Requirements
<!-- sources: ITIL 4 Capacity & Performance Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of major service changes that triggered a timely review and update of the service's capacity and performance requirements. Business needs and customer demand change over time — capacity and performance requirements must be revised accordingly. Measures whether the organization keeps capacity and performance requirements current as services evolve |
| **Formula** | (Service changes with timely CPM requirement review / Total major service changes affecting capacity/performance) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Change records, capacity and performance requirements documents |
| **Owner** | Capacity & Performance Manager |

### KPI-CPM-14: Capacity Model Accuracy
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.1, §2.4.3, §3.2.2 Table 3.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of capacity forecasts that accurately predicted resource requirements within an acceptable tolerance during the reporting period. Measures the quality and reliability of the organization's capacity modelling and demand forecasting capability. Inaccurate forecasts lead to either under-provisioning (causing performance degradation) or over-provisioning (causing unnecessary cost). Models should be validated against actual outcomes and refined iteratively |
| **Formula** | (Capacity forecasts within acceptable tolerance / Total capacity forecasts produced) × 100 |
| **Target** | ≥ 80%; trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Capacity plans (forecasted), actual capacity utilization data |
| **Owner** | Capacity & Performance Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| CPM-01 | Service Performance Achievement | All | Monthly |
| CPM-02 | Number of Performance Degradations | All | Monthly |
| CPM-03 | Capacity Utilization Against Thresholds | All | Monthly |
| CPM-04 | Unplanned Capacity and Performance Upgrades | All | Monthly |
| CPM-05 | Capacity and Performance Requirements Documentation Rate | T2+ | Quarterly |
| CPM-06 | Performance Requirements Match Rate | T2+ | Quarterly |
| CPM-07 | Capacity and Performance Monitoring Coverage | T2+ | Quarterly |
| CPM-08 | Capacity and Performance Reporting Coverage | T2+ | Quarterly |
| CPM-09 | Performance SLA Achievement Rate | T2+ | Monthly |
| CPM-10 | Capacity Plan Coverage | T2+ | Quarterly |
| CPM-11 | Capacity and Performance Loss Ratio | T3 | Semi-annually |
| CPM-12 | Improvement Initiative Enactment Rate | T3 | Semi-annually |
| CPM-13 | Timely Updating of CPM Requirements | T3 | Quarterly |
| CPM-14 | Capacity Model Accuracy | T3 | Semi-annually |
