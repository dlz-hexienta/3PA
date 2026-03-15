---
title: "Incident Management — KPI Definitions"
organization: "Acme IT Services"
scope: "PR11"
category: kpi-definition
process_id: PR11
status: draft
version: "0.1"
date: 2026-03-15
parent: acme-im-process-definition.md
depends_on:
  - acme-im-process-definition.md
framework: fitsm
tags: [e2e-demo, t1, greenfield]
---

# Incident Management — KPI Definitions

<!-- Layer 3 document — metrics and targets for PR11 Incident Management.
     Essential KPIs only (KPI-IM-01 through KPI-IM-04) for T1 scope.
     Targets must be consistent with SLA targets from D-6. -->

## 1. KPI Framework

Acme IT Services measures Incident Management effectiveness through four essential KPIs that together provide a balanced view of process performance:

- **Speed:** Mean resolution time measures whether incidents are resolved promptly (KPI-IM-01)
- **Compliance:** SLA target achievement measures adherence to agreed service commitments (KPI-IM-02)
- **Efficiency:** First-contact resolution rate measures the effectiveness of front-line handling (KPI-IM-03)
- **Capacity:** Backlog size and trend measures whether the team can keep pace with demand (KPI-IM-04)

All KPIs are measured monthly from Jira Service Management data. The Incident Manager (Tom Weber) owns all four KPIs and is responsible for reporting results to the IT Director. RAG thresholds (Green / Amber / Red) provide at-a-glance status for management reporting.

SLA targets referenced in these KPIs are aligned with decision D-6:

| Priority | Response Target | Resolution Target | Service Hours |
|----------|----------------|-------------------|---------------|
| P1 — Critical | 15 minutes | 4 hours | 24/7 |
| P2 — High | 30 minutes | 8 hours | Business hours (Mon-Fri 08:00-18:00 CET) |
| P3 — Medium | 2 hours | 24 hours | Business hours (Mon-Fri 08:00-18:00 CET) |
| P4 — Low | 4 hours | 5 business days | Business hours (Mon-Fri 08:00-18:00 CET) |

## 2. KPI Definitions

### KPI-IM-01: Mean Incident Resolution Time (MTTR)

| Attribute | Value |
|-----------|-------|
| **Process** | PR11 Incident Management |
| **Objective** | Measures the average elapsed time from incident detection to confirmed resolution. Indicates overall speed and efficiency of the incident handling process. A declining MTTR demonstrates process improvement |
| **Formula** | Sum of (resolution timestamp - detection timestamp) for all resolved incidents in the period / Total resolved incidents in the period. Calculated per priority level and as an overall average |
| **Target** | Within SLA resolution targets per priority level: P1 <= 4 hours; P2 <= 8 hours; P3 <= 24 hours; P4 <= 5 business days |
| **Data Source** | Jira Service Management — incident records (detection timestamp, resolution timestamp, priority field) |
| **Measurement Period** | Monthly |
| **Reporting Frequency** | Monthly (included in monthly incident report) |
| **Owner** | Incident Manager (Tom Weber) |
| **Threshold — Green** | Mean resolution time <= SLA target for each priority level |
| **Threshold — Amber** | Mean resolution time between 100% and 120% of SLA target for any priority level |
| **Threshold — Red** | Mean resolution time > 120% of SLA target for any priority level |

### KPI-IM-02: Incident Resolution Within SLA Target Rate

| Attribute | Value |
|-----------|-------|
| **Process** | PR11 Incident Management |
| **Objective** | Measures the percentage of incidents resolved within the SLA resolution target defined for the incident's priority level. Directly reflects the organization's ability to meet service commitments to clients |
| **Formula** | (Incidents resolved within SLA resolution target / Total resolved incidents) x 100. Calculated per priority level and as an overall rate |
| **Target** | >= 90% overall; per priority: P1 >= 90%, P2 >= 90%, P3 >= 92%, P4 >= 95% |
| **Data Source** | Jira Service Management — incident records (resolution timestamp, SLA target, priority field, SLA breach flag) |
| **Measurement Period** | Monthly |
| **Reporting Frequency** | Monthly (included in monthly incident report) |
| **Owner** | Incident Manager (Tom Weber) |
| **Threshold — Green** | >= 90% overall SLA achievement |
| **Threshold — Amber** | 80% - 89% overall SLA achievement |
| **Threshold — Red** | < 80% overall SLA achievement |

### KPI-IM-03: First-Contact Resolution Rate

| Attribute | Value |
|-----------|-------|
| **Process** | PR11 Incident Management |
| **Objective** | Measures the percentage of incidents resolved at first contact by a Service Desk Agent (SDA) without functional escalation to a Technical Specialist (TS). A high first-contact resolution rate indicates effective use of knowledge articles and diagnostic tools at the front line, reducing resolution time and improving user experience |
| **Formula** | (Incidents resolved at first contact by SDA / Total incidents received at Service Desk) x 100 |
| **Target** | >= 60% (trending upward) |
| **Data Source** | Jira Service Management — incident records (resolver field, escalation history, resolution level field) |
| **Measurement Period** | Monthly |
| **Reporting Frequency** | Monthly (included in monthly incident report) |
| **Owner** | Incident Manager (Tom Weber) |
| **Threshold — Green** | >= 60% first-contact resolution rate |
| **Threshold — Amber** | 45% - 59% first-contact resolution rate |
| **Threshold — Red** | < 45% first-contact resolution rate |

### KPI-IM-04: Incident Backlog Size and Trend

| Attribute | Value |
|-----------|-------|
| **Process** | PR11 Incident Management |
| **Objective** | Measures the number of open (unresolved) incidents at the end of the reporting period with trend data showing whether the backlog is growing, stable, or shrinking. A growing backlog indicates that incident arrival rate exceeds resolution capacity and requires management attention |
| **Formula** | Count of open incidents at period end; period-over-period change (absolute number and percentage). Broken down by priority level |
| **Target** | Stable or trending downward; no P1/P2 incidents open longer than 2 business days; no P3 incidents older than 5 business days; no P4 incidents older than 10 business days |
| **Data Source** | Jira Service Management — incident records (status field, priority field, created date, current date) |
| **Measurement Period** | Monthly |
| **Reporting Frequency** | Monthly (included in monthly incident report) |
| **Owner** | Incident Manager (Tom Weber) |
| **Threshold — Green** | Backlog stable or decreasing; no incidents exceeding ageing thresholds |
| **Threshold — Amber** | Backlog growing < 10% month-over-month OR 1-2 incidents exceeding ageing thresholds |
| **Threshold — Red** | Backlog growing >= 10% month-over-month OR 3+ incidents exceeding ageing thresholds |

## 3. KPI Summary Table

| KPI ID | Name | Process | Target | Owner |
|--------|------|---------|--------|-------|
| KPI-IM-01 | Mean Incident Resolution Time (MTTR) | PR11 | Within SLA targets per priority | Incident Manager (Tom Weber) |
| KPI-IM-02 | Incident Resolution Within SLA Target Rate | PR11 | >= 90% | Incident Manager (Tom Weber) |
| KPI-IM-03 | First-Contact Resolution Rate | PR11 | >= 60% | Incident Manager (Tom Weber) |
| KPI-IM-04 | Incident Backlog Size and Trend | PR11 | Stable or decreasing | Incident Manager (Tom Weber) |

## 4. Measurement Calendar

All four essential KPIs are measured and reported monthly. The measurement cycle aligns with the calendar month.

| KPI | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|-----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| KPI-IM-01 MTTR | M | M | M | M | M | M | M | M | M | M | M | M |
| KPI-IM-02 SLA Rate | M | M | M | M | M | M | M | M | M | M | M | M |
| KPI-IM-03 FCR Rate | M | M | M | M | M | M | M | M | M | M | M | M |
| KPI-IM-04 Backlog | M | M | M | M | M | M | M | M | M | M | M | M |

**Legend:** M = Measured and reported this month

**Reporting Timeline:**
- Data extraction from Jira SM: 1st business day of the following month
- KPI calculation and analysis: 2nd business day
- Monthly incident report distribution: by 5th business day of the following month
- Report recipients: IT Director, Service Desk Lead, Team Leads

## 5. Related Documents

| Document | Relationship |
|----------|-------------|
| acme-im-process-definition.md | Process definition — source of objectives and activity descriptions that these KPIs measure |
| acme-im-process-policy.md | Process policy — KPI targets support the policy objectives defined in Section 4 |
| acme-im-raci-matrix.md | RACI matrix — KPI Owner (IM) is consistent with RACI accountability assignments |
| acme-im-procedures.md | Procedures — KPI measurement points align with procedure steps (e.g., detection timestamp at PROC-IM-01 Step 1, resolution timestamp at Step 6) |
