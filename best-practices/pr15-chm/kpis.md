---
process_id: PR15
process_name: "Change Management"
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
  - "ITIL 4: Change Enablement §2.4 PSFs, §2.5 Table 2.4"
  - "FitSM-2: §PR12 CHM"
  - "IT4IT: R2D Value Stream"
  - "SIAM: Service Integration (change coordination)"
last_updated: 2026-03-13
status: draft
---

# Change Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Change management KPIs are mapped to four practice success factors: (1) ensuring changes are realized in a timely and effective manner, (2) minimizing the negative impact of changes, (3) ensuring stakeholder satisfaction, and (4) meeting governance and compliance requirements.

---

## Essential KPIs (All tiers)

### KPI-CHM-01: Change Success Rate
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of changes that were successfully completed — achieving their intended outcomes without requiring rollback or significant rework — relative to the total number of changes attempted during the reporting period. This is the primary indicator of the effectiveness of the change enablement practice. Reported by change type (standard, normal, emergency) and by change model |
| **Formula** | (Changes successfully completed / Total changes attempted) x 100; broken down by type and change model |
| **Target** | >= 95% for standard changes; >= 85% for normal changes; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Change records (ITSM tool) |
| **Owner** | Change Manager |

### KPI-CHM-02: Change-Related Incident Rate
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and duration of incidents caused by or directly related to changes implemented during the reporting period. Measures the negative impact of changes on service stability. A high or increasing rate indicates weaknesses in change assessment, testing, or realization control. Reported alongside the total number of changes to provide a ratio of incidents per change |
| **Formula** | Count of change-related incidents / Total changes implemented; reported with total incident duration (service downtime attributable to change-related incidents) |
| **Target** | Trending downward |
| **Frequency** | Monthly |
| **Data Source** | Incident records, change records (ITSM tool) |
| **Owner** | Change Manager |

### KPI-CHM-03: Emergency Change Rate
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF2, FitSM-2 §PR12 CHM -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of changes classified as emergency changes relative to the total number of changes during the reporting period. Emergency changes bypass or accelerate normal controls, so a high emergency change rate indicates instability in the environment, inadequate proactive management, or overuse of the emergency classification. Reported with trend data |
| **Formula** | (Emergency changes / Total changes) x 100 |
| **Target** | < 10%; trending downward |
| **Frequency** | Monthly |
| **Data Source** | Change records (ITSM tool) |
| **Owner** | Change Manager |

### KPI-CHM-04: Change Backlog and Throughput
<!-- sources: ITIL 4 Change Enablement §2.4.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number of open (in-progress or awaiting authorization) change requests at the end of the reporting period, reported alongside the total number of changes completed during the period (throughput). A growing backlog indicates that change demand exceeds processing capacity. Throughput measures the organization's ability to process changes at the rate required by the business |
| **Formula** | Count of open change requests at period end; count of changes completed in the period; period-over-period change |
| **Target** | Backlog stable or trending downward; throughput meeting business demand |
| **Frequency** | Monthly |
| **Data Source** | Change records (ITSM tool) |
| **Owner** | Change Manager |

---

## Intermediate KPIs (T2+)

### KPI-CHM-05: Mean Change Realization Time
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average elapsed time from change registration to confirmed completion, reported by change model. Measures the speed of change realization. Reported separately for different change types and models to enable meaningful comparison — standard changes, low-risk normal changes, high-risk normal changes, and emergency changes have inherently different timescales |
| **Formula** | Sum of (completion timestamp − registration timestamp) for all completed changes / Total completed changes; reported per change model |
| **Target** | Trending downward within each change model |
| **Frequency** | Monthly |
| **Data Source** | Change records (ITSM tool) |
| **Owner** | Change Manager |

### KPI-CHM-06: Change Timeliness Rate
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of changes completed within the timeframe agreed with the change initiator or defined by the change model. Measures whether changes are meeting the expectations and requirements of their initiators for timeliness. Failure to meet timeliness expectations can make a change ineffective or harmful, regardless of whether it achieves its technical outcome |
| **Formula** | (Changes completed within agreed timeframe / Total completed changes) x 100 |
| **Target** | >= 90%; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Change records (ITSM tool) |
| **Owner** | Change Manager |

### KPI-CHM-07: Standard Change Adoption Rate
<!-- sources: ITIL 4 Change Enablement §2.2.1, §2.4.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of total changes processed as standard changes (pre-authorized, following defined procedures) relative to the total number of changes. A higher standard change rate indicates maturity in change standardization and automation — more changes are being handled through efficient, pre-authorized procedures rather than requiring individual assessment and authorization |
| **Formula** | (Standard changes / Total changes) x 100 |
| **Target** | Trending upward as standardization matures |
| **Frequency** | Quarterly |
| **Data Source** | Change records (ITSM tool) |
| **Owner** | Change Manager |

### KPI-CHM-08: Business Impact of Change-Related Incidents
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The aggregate business impact of incidents caused by or directly related to changes — expressed in terms meaningful to the organization, such as user-hours lost, revenue impact, or service downtime. Provides a business-level view of the negative consequences of change failures that complements the technical incident count |
| **Formula** | Organization-specific composite — e.g., sum of (affected users x incident duration) for all change-related incidents, or financial impact where calculable |
| **Target** | Trending downward |
| **Frequency** | Quarterly |
| **Data Source** | Incident records, change records, business impact data (ITSM tool) |
| **Owner** | Change Manager |

### KPI-CHM-09: Change Initiator Satisfaction
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF1, PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average satisfaction score from change initiators, measuring their assessment of: (a) whether the change achieved the desired outcomes, and (b) whether the change was completed within an acceptable timeframe. Captures the demand-side perspective on change enablement effectiveness — were the people who needed the change satisfied with the result? |
| **Formula** | Average satisfaction score from post-change surveys (scale 1–5); reported separately for outcomes satisfaction and timeliness satisfaction |
| **Target** | >= 3.8 (trending upward) |
| **Frequency** | Quarterly |
| **Data Source** | Post-change satisfaction surveys |
| **Owner** | Change Manager |

### KPI-CHM-10: Post-Implementation Review Completion Rate
<!-- sources: ITIL 4 Change Enablement §3.2.1, FitSM-2 §PR12 CHM (post implementation review) -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of changes requiring a post-implementation review (emergency changes, major changes, unsuccessful changes) that have had their review completed within the defined timeframe. Measures the organization's discipline in reviewing changes to capture lessons learned and drive improvement |
| **Formula** | (PIRs completed within defined timeframe / Total changes requiring PIR) x 100 |
| **Target** | 100% for emergency changes; >= 90% for all required PIRs |
| **Frequency** | Monthly |
| **Data Source** | Change records, PIR reports (ITSM tool) |
| **Owner** | Change Manager |

---

## Advanced KPIs (T3)

### KPI-CHM-11: Stakeholder Satisfaction with Change Practice
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average satisfaction score from stakeholders (service owners, technical teams, users, suppliers) with the change enablement practice itself — including its procedures, communications, transparency, and responsiveness. Distinct from change initiator satisfaction (which measures satisfaction with individual change outcomes), this measures satisfaction with the practice as a whole |
| **Formula** | Average satisfaction score from periodic stakeholder surveys (scale 1–5) |
| **Target** | >= 3.8 (trending upward) |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder satisfaction surveys |
| **Owner** | Change Manager |

### KPI-CHM-12: Governance and Compliance Score
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | A composite measure of the change enablement practice's adherence to governance and compliance requirements — including the number and criticality of change-related audit findings, the number and impact of change-related compliance incidents, and overall compliance as assessed in audit reports. Measures the practice's effectiveness in meeting regulatory, contractual, and internal governance requirements |
| **Formula** | Composite: count of change-related audit findings (weighted by criticality) + count of compliance incidents (weighted by impact); trending toward zero |
| **Target** | Zero critical findings; total score trending downward |
| **Frequency** | Per audit cycle; reported semi-annually |
| **Data Source** | Audit reports, compliance incident records |
| **Owner** | Change Manager |

### KPI-CHM-13: Change Model Optimization Yield
<!-- sources: ITIL 4 Change Enablement §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and measurable impact of change model improvements initiated from periodic change review analysis — including new standard change procedures created, change models updated, automation implemented, and the resulting improvements in change success rate, realization time, or incident reduction. Measures the effectiveness of the change optimization process in driving tangible improvements |
| **Formula** | Count of model improvements per review period; percentage implemented within target timeframe; measured impact (change in success rate, realization time, or incident rate attributable to improvements) |
| **Target** | Positive trend in both count and completion rate; measurable impact demonstrated |
| **Frequency** | Semi-annually |
| **Data Source** | Continual improvement register, change records (pre/post comparison) |
| **Owner** | Change Manager |

### KPI-CHM-14: Changes Identified as Sources of Problems
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and impact of changes identified as the source of problems or known errors during the reporting period. Measures the extent to which changes are introducing underlying issues that, while not immediately causing incidents, create ongoing risk and may lead to future service degradation. A high count indicates weaknesses in change assessment or testing that are not caught by immediate post-implementation review |
| **Formula** | Count of changes linked as the source of problem records / Total changes; reported with impact data (associated incident count, affected services) |
| **Target** | Trending downward |
| **Frequency** | Quarterly |
| **Data Source** | Problem records, change records (ITSM tool) |
| **Owner** | Change Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| CHM-01 | Change Success Rate | All | Monthly |
| CHM-02 | Change-Related Incident Rate | All | Monthly |
| CHM-03 | Emergency Change Rate | All | Monthly |
| CHM-04 | Change Backlog and Throughput | All | Monthly |
| CHM-05 | Mean Change Realization Time | T2+ | Monthly |
| CHM-06 | Change Timeliness Rate | T2+ | Monthly |
| CHM-07 | Standard Change Adoption Rate | T2+ | Quarterly |
| CHM-08 | Business Impact of Change-Related Incidents | T2+ | Quarterly |
| CHM-09 | Change Initiator Satisfaction | T2+ | Quarterly |
| CHM-10 | Post-Implementation Review Completion Rate | T2+ | Monthly |
| CHM-11 | Stakeholder Satisfaction with Change Practice | T3 | Semi-annually |
| CHM-12 | Governance and Compliance Score | T3 | Semi-annually |
| CHM-13 | Change Model Optimization Yield | T3 | Semi-annually |
| CHM-14 | Changes Identified as Sources of Problems | T3 | Quarterly |
