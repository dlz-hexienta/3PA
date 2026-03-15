---
process_id: PR11
process_name: "Incident Management"
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
  - "ITIL 4: Incident Management §2.5 Table 2.2"
  - "FitSM-2: §PR9 ISRM (incident scope)"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (incident coordination)"
last_updated: 2026-03-13
status: draft
---

# Incident Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions).

---

## Essential KPIs (All tiers)

### KPI-IM-01: Mean Incident Resolution Time (MTTR)
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average elapsed time from incident detection to confirmed resolution across all incidents in the reporting period. Measures the overall speed and efficiency of the incident handling and resolution process |
| **Formula** | Sum of (resolution timestamp − detection timestamp) for all resolved incidents / Total resolved incidents |
| **Target** | Within agreed SLA resolution targets for each priority level |
| **Frequency** | Monthly |
| **Data Source** | Incident records (ITSM tool) |
| **Owner** | Incident Manager |

### KPI-IM-02: Incident Resolution Within SLA Target Rate
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of incidents resolved within the resolution target defined in the applicable SLA for the incident's priority level. Measures the organization's ability to meet its service level commitments for incident resolution |
| **Formula** | (Incidents resolved within SLA resolution target / Total resolved incidents) x 100 |
| **Target** | >= 90% |
| **Frequency** | Monthly |
| **Data Source** | Incident records, SLA targets (ITSM tool) |
| **Owner** | Incident Manager |

### KPI-IM-03: First-Contact Resolution Rate
<!-- sources: ITIL 4 Incident Management §2.4.2, §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of incidents resolved at first contact by the service desk agent without escalation to specialist resolver groups. A high first-contact resolution rate indicates effective use of incident models, knowledge articles, and the KEDB at the first point of contact |
| **Formula** | (Incidents resolved at first contact / Total incidents received at service desk) x 100 |
| **Target** | >= 60% (trending upward) |
| **Frequency** | Monthly |
| **Data Source** | Incident records (ITSM tool) |
| **Owner** | Incident Manager |

### KPI-IM-04: Incident Backlog Size and Trend
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number of open (unresolved) incidents at the end of the reporting period, reported with trend data showing whether the backlog is growing, stable, or shrinking. A growing backlog indicates that incident arrival rate exceeds resolution capacity |
| **Formula** | Count of open incidents at period end; period-over-period change (absolute and percentage) |
| **Target** | Stable or trending downward; no incidents older than defined ageing threshold |
| **Frequency** | Monthly |
| **Data Source** | Incident records (ITSM tool) |
| **Owner** | Incident Manager |

---

## Intermediate KPIs (T2+)

### KPI-IM-05: Proactive Incident Detection Rate
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of incidents detected through monitoring, event correlation, or automated systems before users report them. Measures the effectiveness of proactive detection mechanisms and integration with monitoring and event management |
| **Formula** | (Incidents detected before user report / Total incidents) x 100 |
| **Target** | >= 30% (trending upward) |
| **Frequency** | Monthly |
| **Data Source** | Incident records — detection source field (ITSM tool) |
| **Owner** | Incident Manager |

### KPI-IM-06: Mean Time from Occurrence to Detection
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average elapsed time between the estimated time of incident occurrence (time of first symptom or last known good function) and the time the incident was detected and registered. Measures the speed of incident detection — shorter detection times reduce impact duration |
| **Formula** | Sum of (detection timestamp − estimated occurrence time) for all incidents / Total incidents |
| **Target** | Trending downward |
| **Frequency** | Monthly |
| **Data Source** | Incident records — first symptom and detection timestamps (ITSM tool) |
| **Owner** | Incident Manager |

### KPI-IM-07: Incident Model Usage Rate
<!-- sources: ITIL 4 Incident Management §2.4.2, §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of incidents that were resolved using a pre-defined incident model. Measures the extent to which the organization has codified repeatable handling approaches for known incident types and the effectiveness of model matching during classification |
| **Formula** | (Incidents resolved using an incident model / Total resolved incidents) x 100 |
| **Target** | >= 40% (trending upward as model library grows) |
| **Frequency** | Quarterly |
| **Data Source** | Incident records — model reference field (ITSM tool) |
| **Owner** | Incident Manager |

### KPI-IM-08: Incident Escalation Rate
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of incidents that required functional escalation beyond the initial resolver group, and percentage that required hierarchical escalation to management. Excessive functional escalation may indicate classification or routing issues; excessive hierarchical escalation may indicate resource or priority conflicts |
| **Formula** | (Incidents escalated [functional or hierarchical] / Total incidents) x 100; reported separately for functional and hierarchical |
| **Target** | Functional: trending stable or downward; Hierarchical: < 5% |
| **Frequency** | Monthly |
| **Data Source** | Incident records — escalation history (ITSM tool) |
| **Owner** | Incident Manager |

### KPI-IM-09: User Satisfaction with Incident Resolution
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Average user satisfaction score from post-resolution surveys, measuring users' assessment of the quality, timeliness, and communication of incident resolution. Satisfaction scores complement time-based metrics by capturing the user's subjective experience |
| **Formula** | Average satisfaction score from post-incident surveys (scale 1–5) |
| **Target** | >= 3.8 (trending upward) |
| **Frequency** | Monthly |
| **Data Source** | Post-incident satisfaction surveys |
| **Owner** | Incident Manager |

### KPI-IM-10: Major Incident Resolution Time
<!-- sources: ITIL 4 Incident Management §2.4.2, §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average elapsed time from major incident identification to confirmed resolution. Reported alongside the number of major incidents in the period. Major incidents have disproportionate business impact, so their resolution time is tracked separately from standard incidents |
| **Formula** | Sum of (resolution timestamp − major incident identification timestamp) for all resolved major incidents / Total resolved major incidents |
| **Target** | Within major incident SLA targets; trending downward |
| **Frequency** | Per event; reported monthly |
| **Data Source** | Major incident records (ITSM tool) |
| **Owner** | Incident Manager / Major Incident Manager |

---

## Advanced KPIs (T3)

### KPI-IM-11: Monitoring vs User-Reported Detection Ratio
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The ratio of incidents detected by automated monitoring and event correlation to those reported by users, and separately the ratio of incidents detected by event correlation to those detected by manual monitoring. Measures the maturity of the organization's automated detection capabilities and the effectiveness of event correlation in identifying incidents before they require manual observation |
| **Formula** | (1) Monitoring-detected incidents / User-reported incidents; (2) Event-correlation-detected incidents / Manually-monitored incidents |
| **Target** | Both ratios trending upward; monitoring-detected > user-reported |
| **Frequency** | Quarterly |
| **Data Source** | Incident records — detection source and method fields (ITSM tool) |
| **Owner** | Incident Manager |

### KPI-IM-12: Business Impact of Incidents
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The aggregate business impact of incidents in the reporting period, expressed in terms meaningful to the organization — such as total user-hours lost, revenue impact, number of affected customers, or operational downtime. Provides a business-level view of incident impact that complements technical resolution metrics |
| **Formula** | Organization-specific composite measure — e.g., sum of (affected users x incident duration) for all incidents, or financial impact where calculable |
| **Target** | Trending downward year-on-year |
| **Frequency** | Quarterly |
| **Data Source** | Incident records, business impact assessments, financial data |
| **Owner** | Incident Manager |

### KPI-IM-13: Incident Model Improvement Rate
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number of incident model improvements initiated as a result of periodic incident reviews, measured alongside the number of active incident models. Indicates the organization's commitment to continually improving its incident handling approaches based on operational evidence |
| **Formula** | Count of incident model improvements initiated per reporting period; reported as a percentage of the total active model library |
| **Target** | Positive trend; all models reviewed within defined cycle |
| **Frequency** | Quarterly |
| **Data Source** | Incident model register, periodic incident review records |
| **Owner** | Incident Manager |

### KPI-IM-14: Periodic Review Improvement Yield
<!-- sources: ITIL 4 Incident Management §2.5 Table 2.2 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and measurable impact of improvement initiatives generated from periodic incident reviews — including improvements to incident models, classification schemes, escalation paths, team structures, and automation. Measures the effectiveness of the periodic review process in driving tangible improvements to incident management |
| **Formula** | Count of improvement initiatives per review; percentage of initiatives completed within target timeframe; measured impact (e.g., reduction in MTTR, increase in first-contact resolution, decrease in escalation rate) attributable to implemented improvements |
| **Target** | Positive trend in both count and completion rate; measurable impact demonstrated |
| **Frequency** | Semi-annually |
| **Data Source** | Continual improvement register, incident reports (pre/post comparison) |
| **Owner** | Incident Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| IM-01 | Mean Incident Resolution Time (MTTR) | All | Monthly |
| IM-02 | Incident Resolution Within SLA Target Rate | All | Monthly |
| IM-03 | First-Contact Resolution Rate | All | Monthly |
| IM-04 | Incident Backlog Size and Trend | All | Monthly |
| IM-05 | Proactive Incident Detection Rate | T2+ | Monthly |
| IM-06 | Mean Time from Occurrence to Detection | T2+ | Monthly |
| IM-07 | Incident Model Usage Rate | T2+ | Quarterly |
| IM-08 | Incident Escalation Rate | T2+ | Monthly |
| IM-09 | User Satisfaction with Incident Resolution | T2+ | Monthly |
| IM-10 | Major Incident Resolution Time | T2+ | Per event |
| IM-11 | Monitoring vs User-Reported Detection Ratio | T3 | Quarterly |
| IM-12 | Business Impact of Incidents | T3 | Quarterly |
| IM-13 | Incident Model Improvement Rate | T3 | Quarterly |
| IM-14 | Periodic Review Improvement Yield | T3 | Semi-annually |
