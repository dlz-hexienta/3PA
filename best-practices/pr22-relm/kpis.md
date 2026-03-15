---
process_id: PR22
process_name: "Relationship Management"
category: kpis
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
  - "ITIL 4: Relationship Management §2.5 Table 2.5"
  - "FitSM-2: §PR7 CRM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (relationship coordination)"
last_updated: 2026-03-13
status: draft
---

# Relationship Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions).

---

## Essential KPIs (All Tiers)

### KPI-RELM-01: Customer Satisfaction Score
<!-- sources: ITIL 4 Relationship Management §2.5 Table 2.5 PSF3, FitSM-2 §PR7 CRM (manage satisfaction) -->

| Attribute | Value |
|-----------|-------|
| **Description** | Overall satisfaction score from service customers, measuring their perception of service quality, relationship health, communication effectiveness, and responsiveness to their needs |
| **Formula** | Average satisfaction score from periodic customer satisfaction surveys (scale 1–5 or equivalent) |
| **Target** | >= 4.0 (trending stable or upward) |
| **Frequency** | Per survey cycle (at least annually; semi-annually recommended) |
| **Data Source** | Customer satisfaction surveys, feedback forms |
| **Owner** | Relationship Manager |

### KPI-RELM-02: Customer Complaint Resolution Rate
<!-- sources: FitSM-2 §PR7 CRM (handle complaints), ITIL 4 Relationship Management §2.5 Table 2.5 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of customer complaints that are resolved within the agreed timeframe, measuring the effectiveness and responsiveness of the complaints handling process |
| **Formula** | (Complaints resolved within agreed timeframe / Total complaints received) x 100 |
| **Target** | >= 90% |
| **Frequency** | Monthly |
| **Data Source** | Complaints register |
| **Owner** | Relationship Manager |

### KPI-RELM-03: Service Review Completion Rate
<!-- sources: FitSM-2 §PR7 CRM (perform service reviews), ITIL 4 Relationship Management §2.5 Table 2.5 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of scheduled customer service reviews that were actually conducted within the agreed period, measuring adherence to the review cadence |
| **Formula** | (Service reviews conducted / Service reviews scheduled) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | Service review schedule, service review reports |
| **Owner** | Relationship Manager |

### KPI-RELM-04: Stakeholder Database Coverage
<!-- sources: FitSM-2 §PR7 CRM (maintain customer database), ITIL 4 Relationship Management §2.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of known service customers and key stakeholders who have a current, complete record in the customer/stakeholder database with all required attributes populated |
| **Formula** | (Stakeholders with complete database records / Total known stakeholders) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | Customer/stakeholder database, service agreements |
| **Owner** | Relationship Manager |

---

## Intermediate KPIs (T2+)

### KPI-RELM-05: Stakeholder Map Completeness
<!-- sources: ITIL 4 Relationship Management §2.5 Table 2.5 PSF1, §2.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of identified stakeholder groups that have been formally mapped by influence and interest, with a defined engagement approach documented for each quadrant |
| **Formula** | (Stakeholder groups with current mapping and engagement approach / Total identified stakeholder groups) x 100 |
| **Target** | 100% |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder maps |
| **Owner** | Relationship Manager |

### KPI-RELM-06: Relationship Principles Adoption Rate
<!-- sources: ITIL 4 Relationship Management §2.5 Table 2.5 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Degree to which the agreed relationship principles are known, understood, and practised across the organization — measured through staff awareness surveys, observation, and feedback from relationship agents |
| **Formula** | Average adoption score from periodic staff awareness assessment (scale 1–5) or percentage of staff who can demonstrate awareness of the key principles |
| **Target** | >= 80% awareness; trending upward |
| **Frequency** | Annually |
| **Data Source** | Staff awareness surveys, training completion records |
| **Owner** | Relationship Manager |

### KPI-RELM-07: Internal Relationship Health Score
<!-- sources: ITIL 4 Relationship Management §2.5 Table 2.5 PSF2, §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Measure of the health of relationships within the organization — between teams, departments, and individuals — based on employee engagement data, internal collaboration assessments, and the incidence of internal relationship conflicts |
| **Formula** | Composite score from employee engagement surveys (relationship-relevant items), internal collaboration ratings, and conflict incidence (scale 1–5 or equivalent) |
| **Target** | >= 3.5 (trending upward) |
| **Frequency** | Semi-annually |
| **Data Source** | Employee engagement surveys, internal collaboration assessments, conflict/incident reports |
| **Owner** | Relationship Manager |

### KPI-RELM-08: Relationship Incident and Conflict Rate
<!-- sources: ITIL 4 Relationship Management §2.5 Table 2.5 PSF2, §2.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Number and severity of relationship incidents — situations where relationship breakdown, toxic behaviours, or unresolved conflicts have materially affected service delivery, collaboration, or stakeholder satisfaction |
| **Formula** | Count of relationship incidents per reporting period, segmented by severity (minor, moderate, severe) |
| **Target** | Trending downward; zero severe incidents |
| **Frequency** | Quarterly |
| **Data Source** | Relationship review reports, HR records, escalation logs |
| **Owner** | Relationship Manager |

### KPI-RELM-09: Service Review Action Completion Rate
<!-- sources: ITIL 4 Relationship Management §3.2.2 Table 3.4, FitSM-2 §PR7 CRM -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of actions agreed during customer service reviews that were completed within the agreed timeframe, measuring the organization's follow-through on commitments made to customers |
| **Formula** | (Service review actions completed on time / Total service review actions agreed) x 100 |
| **Target** | >= 85% |
| **Frequency** | Quarterly |
| **Data Source** | Service review reports, action trackers |
| **Owner** | Relationship Manager |

### KPI-RELM-10: Customer Complaint Volume and Trend
<!-- sources: FitSM-2 §PR7 CRM (complaints records), ITIL 4 Relationship Management §2.5 Table 2.5 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Number of customer complaints received per reporting period, analysed by category, service, and customer group, with trend analysis to identify systemic issues or improvement patterns |
| **Formula** | Count of complaints per period, segmented by category and service area; period-over-period trend |
| **Target** | Trending downward; no complaint category with increasing trend for more than two consecutive periods |
| **Frequency** | Monthly |
| **Data Source** | Complaints register |
| **Owner** | Relationship Manager |

---

## Advanced KPIs (T3)

### KPI-RELM-11: Relationship Model Coverage
<!-- sources: ITIL 4 Relationship Management §2.5 Table 2.5 PSF1, §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of key stakeholder groups (as defined in the stakeholder map) that have a formally developed and current relationship model in active use |
| **Formula** | (Key stakeholder groups with active relationship model / Total key stakeholder groups) x 100 |
| **Target** | >= 90% |
| **Frequency** | Semi-annually |
| **Data Source** | Relationship models library, stakeholder maps |
| **Owner** | Relationship Manager |

### KPI-RELM-12: Non-Service Stakeholder Engagement Coverage
<!-- sources: ITIL 4 Relationship Management §2.4.3.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of identified non-service stakeholder groups (regulators, media, industry associations, investors, communities) that have a defined engagement approach and active relationship management |
| **Formula** | (Non-service stakeholder groups with active engagement / Total identified non-service stakeholder groups) x 100 |
| **Target** | >= 80% |
| **Frequency** | Annually |
| **Data Source** | Stakeholder maps, non-service stakeholder engagement records |
| **Owner** | Relationship Manager |

### KPI-RELM-13: Cross-Boundary Relationship Coordination Effectiveness
<!-- sources: ITIL 4 Relationship Management §6, SIAM Service Integration -->

| Attribute | Value |
|-----------|-------|
| **Description** | In multi-supplier environments, the effectiveness of cross-boundary relationship coordination — measured through stakeholder satisfaction with the end-to-end service experience, the incidence of cross-boundary relationship issues, and the timeliness of cross-boundary information sharing |
| **Formula** | Composite score from: (1) stakeholder satisfaction with multi-supplier coordination, (2) cross-boundary relationship incident count, (3) percentage of information sharing commitments met on time |
| **Target** | Satisfaction >= 3.5; incidents trending downward; information sharing >= 90% on time |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder surveys, cross-boundary incident logs, information sharing records |
| **Owner** | Relationship Manager |

### KPI-RELM-14: Relationship Approach Effectiveness
<!-- sources: ITIL 4 Relationship Management §2.5 Table 2.5 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Overall assessment of how well the organization's relationship approach and models are working — measured through a combination of stakeholder satisfaction with the approach itself, the degree of adoption across the organization, and the measurable impact on relationship outcomes (fewer conflicts, higher satisfaction, better collaboration) |
| **Formula** | Composite score from: stakeholder satisfaction with relationship approach, adoption rate, and relationship outcome trends (scale 1–5) |
| **Target** | >= 4.0 |
| **Frequency** | Annually |
| **Data Source** | Stakeholder feedback, adoption assessments, relationship review reports |
| **Owner** | Relationship Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| RELM-01 | Customer Satisfaction Score | All | Per survey cycle |
| RELM-02 | Customer Complaint Resolution Rate | All | Monthly |
| RELM-03 | Service Review Completion Rate | All | Quarterly |
| RELM-04 | Stakeholder Database Coverage | All | Quarterly |
| RELM-05 | Stakeholder Map Completeness | T2+ | Semi-annually |
| RELM-06 | Relationship Principles Adoption Rate | T2+ | Annually |
| RELM-07 | Internal Relationship Health Score | T2+ | Semi-annually |
| RELM-08 | Relationship Incident and Conflict Rate | T2+ | Quarterly |
| RELM-09 | Service Review Action Completion Rate | T2+ | Quarterly |
| RELM-10 | Customer Complaint Volume and Trend | T2+ | Monthly |
| RELM-11 | Relationship Model Coverage | T3 | Semi-annually |
| RELM-12 | Non-Service Stakeholder Engagement Coverage | T3 | Annually |
| RELM-13 | Cross-Boundary Relationship Coordination Effectiveness | T3 | Semi-annually |
| RELM-14 | Relationship Approach Effectiveness | T3 | Annually |
