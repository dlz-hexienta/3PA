---
process_id: PR13
process_name: "Problem Management"
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
  - "ITIL 4: Problem Management §2.4 PSFs, §2.5 Table 2.3"
  - "FitSM-2: §PR10 PM"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (problem coordination)"
last_updated: 2026-03-13
status: draft
---

# Problem Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Problem management KPIs are mapped to two practice success factors: (1) identifying and understanding problems and their impact on services, and (2) optimizing problem resolution and mitigation.

---

## Essential KPIs (All tiers)

### KPI-PM-01: Number and Impact of Problems Identified
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The total number of problems identified during the reporting period, reported with impact data (number of associated incidents, affected services, and affected users). Tracks the organization's ability to detect underlying causes of incidents. A consistently low problem identification count alongside high incident volumes may indicate that problems are not being detected |
| **Formula** | Count of new problem records registered in the period; broken down by identification mode (reactive / proactive at T2+), category, and priority |
| **Target** | Positive trend; proportionate to incident volume and complexity |
| **Frequency** | Monthly |
| **Data Source** | Problem records (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-02: Incidents Not Associated with Known Errors
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and impact of incidents that are not associated with any known error in the KEDB. Measures the gap between problem identification coverage and incident occurrence — a high number indicates that problems causing incidents have not yet been identified and investigated. This is a key indicator of the effectiveness of problem identification activities |
| **Formula** | Count of incidents in the period that have no associated known error record / Total incidents in the period; reported with impact data (affected users, service downtime) |
| **Target** | Trending downward |
| **Frequency** | Monthly |
| **Data Source** | Incident records, KEDB (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-03: Problem Resolution Rate
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 PSF2, FitSM-2 §PR10 PM -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of problems permanently resolved (closed with confirmed resolution) during the reporting period, relative to the total number of problems that entered error control. Measures the organization's ability to eliminate the root causes of incidents rather than managing them as ongoing known errors |
| **Formula** | (Problems permanently resolved in the period / Problems in error control at period start + problems entering error control in the period) x 100 |
| **Target** | Trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Problem records (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-04: Problem Backlog Size and Trend
<!-- sources: ITIL 4 Problem Management §2.2 (problem prioritization — single backlog), FitSM-2 §PR10 PM -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number of open (unresolved) problems at the end of the reporting period — broken down by status (awaiting investigation, under investigation, known error awaiting resolution) — reported with period-over-period trend data. A growing backlog indicates that problem identification is outpacing investigation and resolution capacity. An ageing backlog (problems open beyond defined thresholds) indicates stalled investigations |
| **Formula** | Count of open problems at period end by status; period-over-period change (absolute and percentage); count of problems exceeding defined age thresholds |
| **Target** | Stable or trending downward; no problems older than defined ageing threshold without documented justification |
| **Frequency** | Monthly |
| **Data Source** | Problem records (ITSM tool) |
| **Owner** | Problem Manager |

---

## Intermediate KPIs (T2+)

### KPI-PM-05: Incidents Prevented by Problem Resolution
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The estimated number and impact of incidents prevented as a result of permanent problem resolutions implemented during the reporting period. This is the primary measure of the value delivered by problem management — demonstrating that resolving root causes has prevented incidents that would otherwise have occurred. Estimation may be based on pre-resolution incident frequency and the expected recurrence rate |
| **Formula** | Estimated count of incidents prevented based on pre-resolution incident frequency for permanently resolved problems; reported with estimated impact (user-hours saved, service availability improvement) |
| **Target** | Positive trend; increasing as problem resolution activity matures |
| **Frequency** | Quarterly |
| **Data Source** | Problem records, incident records (pre/post resolution comparison) |
| **Owner** | Problem Manager |

### KPI-PM-06: Incidents Resolved with Problem Investigation Solutions
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and impact of incidents that were resolved more effectively using solutions provided by problem investigation — including workarounds from the KEDB and incident solutions communicated during problem control. Measures the direct contribution of problem management to incident resolution quality and speed |
| **Formula** | Count of incidents resolved using KEDB workarounds or problem-investigation-derived solutions / Total resolved incidents; reported with impact data (reduction in mean resolution time for incidents matched to known errors) |
| **Target** | Trending upward |
| **Frequency** | Monthly |
| **Data Source** | Incident records, KEDB usage data (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-07: Proactive vs Reactive Identification Ratio
<!-- sources: ITIL 4 Problem Management §2.4.1, §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The ratio of problems identified proactively (before incidents occurred or from non-incident sources) to problems identified reactively (from incident data). A higher proactive ratio indicates maturity in problem identification — the organization is detecting and addressing problems before they cause service disruption |
| **Formula** | Proactively identified problems / Reactively identified problems; reported as a ratio and as percentages of total |
| **Target** | Proactive ratio trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Problem records — identification mode field (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-08: Mean Time to Resolve Problems
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average elapsed time from problem registration to confirmed permanent resolution, for problems resolved during the reporting period. Reported separately for different problem categories and priorities. Note that problem resolution times are typically much longer than incident resolution times — problems may remain open for weeks or months while root cause analysis, solution development, and change implementation proceed |
| **Formula** | Sum of (resolution timestamp − registration timestamp) for all resolved problems / Total resolved problems |
| **Target** | Trending downward within each priority level |
| **Frequency** | Quarterly |
| **Data Source** | Problem records (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-09: Active Known Errors and Impact
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and aggregate impact of known errors that remain open (unresolved) at the end of the reporting period. Reported with the selected mitigation approach for each (permanent fix planned, permanent workaround in place, optimized incident management). A high number of open known errors with increasing impact indicates growing technical debt. Known errors with effective workarounds or optimized incident management may be acceptable; the key measure is whether their aggregate impact is stable or declining |
| **Formula** | Count of active known errors at period end; aggregate impact (associated incident count, affected users, service availability impact); breakdown by mitigation approach |
| **Target** | Aggregate impact stable or trending downward |
| **Frequency** | Quarterly |
| **Data Source** | KEDB, incident records (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-10: Incidents Requiring Urgent Problem Investigation
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and impact of incidents that required urgent, unplanned problem investigation — incidents of high severity or business impact where no known error existed and existing incident models were insufficient for resolution. A high count indicates gaps in proactive problem identification or KEDB coverage |
| **Formula** | Count of incidents triggering urgent problem investigation / Total incidents; reported with impact data |
| **Target** | Trending downward |
| **Frequency** | Monthly |
| **Data Source** | Problem records, incident records (ITSM tool) |
| **Owner** | Problem Manager |

---

## Advanced KPIs (T3)

### KPI-PM-11: Known Error Review Completion Rate
<!-- sources: ITIL 4 Problem Management §3.2.4 Table 3.9 (known error monitoring and review) -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of active known errors that have been reviewed within the defined review cycle. Measures the organization's discipline in periodically reassessing known errors for changes in impact, workaround effectiveness, and resolution options. Known errors that are not reviewed may have outdated mitigation approaches or may have become eligible for permanent resolution |
| **Formula** | (Known errors reviewed within the defined review cycle / Total active known errors) x 100 |
| **Target** | 100% within defined cycle |
| **Frequency** | Quarterly |
| **Data Source** | KEDB, review records (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-12: Technical Debt Trend
<!-- sources: ITIL 4 Problem Management §2.2.3 (technical debt) -->

| Attribute | Value |
|-----------|-------|
| **Description** | The aggregate technical debt from problem management — measured as the total estimated impact of deferred problem resolutions and permanent workarounds, tracked over time. Technical debt increases when the organization chooses workarounds or optimized incident management over permanent fixes, and decreases when permanent resolutions are implemented. Persistent growth in technical debt indicates that risk is accumulating |
| **Formula** | Organization-specific composite measure — e.g., count of deferred resolutions weighted by estimated impact, or estimated remediation cost of outstanding known errors |
| **Target** | Stable or trending downward year-on-year |
| **Frequency** | Semi-annually |
| **Data Source** | KEDB, problem records, financial data |
| **Owner** | Problem Manager |

### KPI-PM-13: Problem Model Coverage and Effectiveness
<!-- sources: ITIL 4 Problem Management §2.2.4, §3.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of problem categories that have defined problem models, and the effectiveness of those models measured by investigation outcomes. Measures the organization's maturity in codifying repeatable investigation approaches for different problem types. Model effectiveness is assessed by comparing investigation times and outcomes for problems handled with models versus those handled without |
| **Formula** | (Problem categories with defined models / Total active problem categories) x 100; mean investigation time for model-guided investigations vs. non-model investigations |
| **Target** | Coverage trending upward; model-guided investigations showing shorter mean investigation times |
| **Frequency** | Semi-annually |
| **Data Source** | Problem model register, problem records (ITSM tool) |
| **Owner** | Problem Manager |

### KPI-PM-14: Problem Management Productivity Index
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3 (aggregated metric) -->

| Attribute | Value |
|-----------|-------|
| **Description** | An aggregated indicator of problem management practice productivity, combining input metrics (problems identified, investigations completed) with output metrics (incidents prevented, incidents resolved with KEDB solutions, known errors resolved) to provide a composite view of the practice's contribution to service quality. The specific aggregation formula should be defined based on the organization's service strategy and priorities |
| **Formula** | Organization-specific composite — e.g., (problems resolved + incidents prevented + incidents resolved via KEDB) / (total investigation effort + total resolution effort); see Measurement & Reporting practice guide for aggregation techniques |
| **Target** | Trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Problem records, incident records, KEDB, effort data (ITSM tool) |
| **Owner** | Problem Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| PM-01 | Number and Impact of Problems Identified | All | Monthly |
| PM-02 | Incidents Not Associated with Known Errors | All | Monthly |
| PM-03 | Problem Resolution Rate | All | Quarterly |
| PM-04 | Problem Backlog Size and Trend | All | Monthly |
| PM-05 | Incidents Prevented by Problem Resolution | T2+ | Quarterly |
| PM-06 | Incidents Resolved with Problem Investigation Solutions | T2+ | Monthly |
| PM-07 | Proactive vs Reactive Identification Ratio | T2+ | Quarterly |
| PM-08 | Mean Time to Resolve Problems | T2+ | Quarterly |
| PM-09 | Active Known Errors and Impact | T2+ | Quarterly |
| PM-10 | Incidents Requiring Urgent Problem Investigation | T2+ | Monthly |
| PM-11 | Known Error Review Completion Rate | T3 | Quarterly |
| PM-12 | Technical Debt Trend | T3 | Semi-annually |
| PM-13 | Problem Model Coverage and Effectiveness | T3 | Semi-annually |
| PM-14 | Problem Management Productivity Index | T3 | Semi-annually |
