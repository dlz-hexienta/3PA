---
process_id: PR01
process_name: "Service Portfolio Management"
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
  - "ITIL 4: Portfolio Management"
  - "FitSM-2: §PR1 SPM"
  - "IT4IT: Evaluate Value Stream, Portfolio Function"
last_updated: 2026-03-13
status: draft
---

# Service Portfolio Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions).

---

## Essential KPIs (All Tiers)

### KPI-SPM-01: Portfolio Completeness
<!-- sources: FitSM-2 §PR1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of known live services that have a corresponding entry in the service portfolio register |
| **Formula** | (Services in portfolio register / Total known live services) x 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Service portfolio register, service catalogue, infrastructure inventory |
| **Owner** | Service Portfolio Manager |

### KPI-SPM-02: Proposal Evaluation Rate
<!-- sources: ITIL 4 Portfolio Management §3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of submitted service proposals that are evaluated within the defined SLA |
| **Formula** | (Proposals evaluated within SLA / Total proposals submitted) x 100 |
| **Target** | >= 90% |
| **Frequency** | Monthly |
| **Data Source** | Service portfolio register (proposal records) |
| **Owner** | Service Portfolio Manager |

### KPI-SPM-03: Portfolio Currency
<!-- sources: FitSM-2 §PR1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of portfolio entries that have been reviewed or updated within the last review cycle |
| **Formula** | (Portfolio entries updated within cycle / Total portfolio entries) x 100 |
| **Target** | >= 95% |
| **Frequency** | Per review cycle |
| **Data Source** | Service portfolio register (last-updated timestamps) |
| **Owner** | Service Portfolio Manager |

### KPI-SPM-04: Service Retirement Compliance
<!-- sources: FitSM-2 §PR1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of retired services that followed the documented retirement procedure (consumer notification, migration, residual obligations addressed) |
| **Formula** | (Compliant retirements / Total retirements) x 100 |
| **Target** | 100% |
| **Frequency** | Per occurrence, reported quarterly |
| **Data Source** | Retirement records, portfolio register |
| **Owner** | Service Portfolio Manager |

---

## Intermediate KPIs (T2+)

### KPI-SPM-05: Portfolio Review Adherence
<!-- sources: ITIL 4 Portfolio Management §2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of scheduled portfolio reviews that were conducted on time with required quorum |
| **Formula** | (Reviews conducted on schedule with quorum / Total scheduled reviews) x 100 |
| **Target** | 100% |
| **Frequency** | Per review cycle (e.g., quarterly) |
| **Data Source** | Portfolio review reports, meeting records |
| **Owner** | Service Portfolio Owner |

### KPI-SPM-06: Planned vs. Actual ROI
<!-- sources: ITIL 4 Portfolio Management §2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Variance between the return on investment projected at proposal time and the actual return realized |
| **Formula** | ((Actual ROI - Planned ROI) / Planned ROI) x 100 |
| **Target** | Variance within +/- 15% |
| **Frequency** | Annually per portfolio item |
| **Data Source** | Financial management records, scope agreements |
| **Owner** | Finance Manager |

### KPI-SPM-07: Investment Balance Ratio
<!-- sources: IT4IT §5.1 Evaluate Value Stream -->

| Attribute | Value |
|-----------|-------|
| **Description** | Ratio of discretionary investment (Grow the Business) to non-discretionary investment (Run the Business) |
| **Formula** | GtB spend / RtB spend |
| **Target** | Organization-defined (typical range: 20:80 to 40:60) |
| **Frequency** | Quarterly |
| **Data Source** | Financial management records, portfolio register |
| **Owner** | Service Portfolio Owner |

### KPI-SPM-08: Stakeholder Satisfaction with Portfolio Decisions
<!-- sources: ITIL 4 Portfolio Management §2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Average satisfaction score from key stakeholders regarding portfolio governance, transparency, and decision quality |
| **Formula** | Average of stakeholder survey scores (scale 1-5) |
| **Target** | >= 3.5 / 5 |
| **Frequency** | Annually |
| **Data Source** | Stakeholder survey |
| **Owner** | Service Portfolio Manager |

### KPI-SPM-09: Portfolio Pipeline Throughput
<!-- sources: ITIL 4 Portfolio Management §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Average time from proposal submission to approval/rejection decision |
| **Formula** | Average(Decision date - Submission date) for all proposals in period |
| **Target** | <= 30 calendar days (standard), <= 5 business days (expedited) |
| **Frequency** | Monthly |
| **Data Source** | Service portfolio register (proposal timestamps) |
| **Owner** | Service Portfolio Manager |

---

## Advanced KPIs (T3)

### KPI-SPM-10: Portfolio-Architecture Alignment
<!-- sources: IT4IT §6.1.3 Enterprise Architecture -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of portfolio items that are mapped to at least one enterprise architecture roadmap item and value stream |
| **Formula** | (Portfolio items with architecture mapping / Total active portfolio items) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | Service portfolio register, architecture repository |
| **Owner** | Enterprise Architect |

### KPI-SPM-11: Scope Agreement Delivery Variance
<!-- sources: IT4IT §6.2.2 Proposal -->

| Attribute | Value |
|-----------|-------|
| **Description** | Variance between scope agreement commitments (budget, timeline) and actual delivery |
| **Formula** | ((Actual - Approved) / Approved) x 100, for both budget and timeline |
| **Target** | Budget variance <= 10%, Timeline variance <= 15% |
| **Frequency** | Per scope agreement completion |
| **Data Source** | Scope agreements, project delivery records |
| **Owner** | Investment Manager |

### KPI-SPM-12: Portfolio Rationalization Rate
<!-- sources: IT4IT §6.2.3 Product Portfolio -->

| Attribute | Value |
|-----------|-------|
| **Description** | Number of duplicate or overlapping services identified and resolved through rationalization in the review period |
| **Formula** | Count of services consolidated, merged, or deduplicated in period |
| **Target** | Trending downward over time (fewer remaining duplicates) |
| **Frequency** | Annually |
| **Data Source** | Portfolio review reports, rationalization records |
| **Owner** | Service Portfolio Manager |

### KPI-SPM-13: End-to-End Value Realization
<!-- sources: IT4IT §5.1, ITIL 4 Portfolio Management §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of delivered portfolio items where actual benefits met or exceeded the anticipated business value defined in the scope agreement |
| **Formula** | (Items meeting benefit targets / Total delivered items) x 100 |
| **Target** | >= 70% |
| **Frequency** | Annually |
| **Data Source** | Scope agreements, benefit realization reports |
| **Owner** | Investment Manager |

### KPI-SPM-14: Portfolio Effectiveness Dynamics
<!-- sources: ITIL 4 Portfolio Management §2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Trend of overall portfolio effectiveness measured as the weighted score of value delivery, cost efficiency, risk exposure, and strategic alignment across all active portfolio items |
| **Formula** | Composite index (organization-defined weighting of value, cost, risk, alignment scores) |
| **Target** | Positive trend quarter-over-quarter |
| **Frequency** | Quarterly |
| **Data Source** | Portfolio health dashboard, financial records, risk register |
| **Owner** | Service Portfolio Owner |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SPM-01 | Portfolio Completeness | All | Quarterly |
| SPM-02 | Proposal Evaluation Rate | All | Monthly |
| SPM-03 | Portfolio Currency | All | Per cycle |
| SPM-04 | Service Retirement Compliance | All | Quarterly |
| SPM-05 | Portfolio Review Adherence | T2+ | Per cycle |
| SPM-06 | Planned vs. Actual ROI | T2+ | Annually |
| SPM-07 | Investment Balance Ratio | T2+ | Quarterly |
| SPM-08 | Stakeholder Satisfaction | T2+ | Annually |
| SPM-09 | Pipeline Throughput | T2+ | Monthly |
| SPM-10 | Portfolio-Architecture Alignment | T3 | Quarterly |
| SPM-11 | Scope Agreement Delivery Variance | T3 | Per completion |
| SPM-12 | Rationalization Rate | T3 | Annually |
| SPM-13 | End-to-End Value Realization | T3 | Annually |
| SPM-14 | Portfolio Effectiveness Dynamics | T3 | Quarterly |
