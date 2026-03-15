---
process_id: PR09
process_name: "Information Security Management"
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
  - "ITIL 4: Information Security Management §2.4 (Table 2.3)"
  - "FitSM-2: §PR6 ISM"
  - "IT4IT: Cross-cutting (security governance)"
last_updated: 2026-03-13
status: draft
---

# Information Security Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions).

---

## Essential KPIs (All Tiers)

### KPI-ISM-01: Security Incident Rate
<!-- sources: ITIL 4 Information Security Management §2.4 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Total number of confirmed security incidents during the reporting period, categorized by severity (low, medium, high, critical) |
| **Formula** | Count of confirmed security incidents in period, segmented by severity |
| **Target** | Trending downward period-over-period; zero critical incidents |
| **Frequency** | Monthly |
| **Data Source** | Security incident records, incident management system |
| **Owner** | Information Security Manager |

### KPI-ISM-02: Security Policy Coverage
<!-- sources: ITIL 4 Information Security Management §2.4 Table 2.3 PSF1, FitSM-2 §PR6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of required security policy domains (access control, classification, remote access, malware protection, personal data, etc.) that have a formally approved and current policy in place |
| **Formula** | (Security domains with approved current policy / Total required security domains) x 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Security policy register, document management system |
| **Owner** | Information Security Manager |

### KPI-ISM-03: Risk Assessment Coverage
<!-- sources: ITIL 4 Information Security Management §2.4 Table 2.3 PSF2, FitSM-2 §PR6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of critical information assets that have a current (within-validity) risk assessment on record |
| **Formula** | (Critical assets with current risk assessment / Total critical assets in inventory) x 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Information asset inventory, risk assessment reports |
| **Owner** | Information Security Manager |

### KPI-ISM-04: Security Control Coverage
<!-- sources: ITIL 4 Information Security Management §2.4 Table 2.3 PSF2, FitSM-2 §PR6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of identified security risks that have at least one documented and implemented control in the security controls register |
| **Formula** | (Risks with implemented controls / Total identified risks requiring treatment) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | Security controls register, risk assessment reports |
| **Owner** | Information Security Manager |

### KPI-ISM-05: Access Rights Review Compliance
<!-- sources: FitSM-2 §PR6, ITIL 4 Information Security Management §2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of scheduled access rights reviews that were completed on time within the reporting period |
| **Formula** | (Access reviews completed on schedule / Total scheduled access reviews) x 100 |
| **Target** | 100% |
| **Frequency** | Per review cycle (semi-annually for privileged, annually for standard) |
| **Data Source** | Access review reports, access rights register |
| **Owner** | Information Security Manager |

---

## Intermediate KPIs (T2+)

### KPI-ISM-06: Security Audit Completion Rate
<!-- sources: ITIL 4 Information Security Management §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of scheduled security audits that were conducted on time with documented findings and recommendations |
| **Formula** | (Audits completed on schedule / Total scheduled audits) x 100 |
| **Target** | 100% |
| **Frequency** | Per audit cycle (at minimum annually) |
| **Data Source** | Security audit reports, audit schedule |
| **Owner** | Information Security Auditor |

### KPI-ISM-07: Security Awareness Training Completion
<!-- sources: ITIL 4 Information Security Management §4.1.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of all staff (employees and relevant contractors) who have completed the required security awareness training within the defined training cycle |
| **Formula** | (Staff who completed training within cycle / Total staff required to complete training) x 100 |
| **Target** | >= 95% |
| **Frequency** | Per training cycle (at minimum annually) |
| **Data Source** | Training completion records, HR system |
| **Owner** | Information Security Manager |

### KPI-ISM-08: Mean Time to Detect (MTTD) Security Incidents
<!-- sources: ITIL 4 Information Security Management §2.4 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Average elapsed time from the estimated start of a security incident to the point at which it was detected and confirmed |
| **Formula** | Average(Detection time - Estimated incident start time) for all incidents in period |
| **Target** | Trending downward; organization-specific baseline |
| **Frequency** | Monthly |
| **Data Source** | Security incident records |
| **Owner** | Information Security Manager |

### KPI-ISM-09: Mean Time to Contain (MTTC) Security Incidents
<!-- sources: ITIL 4 Information Security Management §2.4 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Average elapsed time from security incident detection to successful containment (incident is prevented from causing further damage) |
| **Formula** | Average(Containment time - Detection time) for all incidents in period |
| **Target** | Trending downward; critical incidents <= 4 hours |
| **Frequency** | Monthly |
| **Data Source** | Security incident records |
| **Owner** | Information Security Manager |

### KPI-ISM-10: Security Finding Remediation Rate
<!-- sources: ITIL 4 Information Security Management §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of security findings (from audits, incident reviews, and risk assessments) that were remediated within the agreed timeframe |
| **Formula** | (Findings remediated on time / Total findings with agreed remediation date) x 100 |
| **Target** | >= 80% |
| **Frequency** | Quarterly |
| **Data Source** | Continual improvement register, security audit reports, post-incident review reports |
| **Owner** | Information Security Manager |

### KPI-ISM-11: Supplier Security Compliance Rate
<!-- sources: ITIL 4 Information Security Management §6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of suppliers with access to organizational information or systems that meet all defined security requirements (contractual, technical, and certification) |
| **Formula** | (Compliant suppliers / Total suppliers with information access) x 100 |
| **Target** | 100% |
| **Frequency** | Per supplier review cycle (at minimum annually) |
| **Data Source** | Supplier compliance records, contract register |
| **Owner** | Supplier Security Coordinator / Information Security Manager |

---

## Advanced KPIs (T3)

### KPI-ISM-12: Security Exercise Completion Rate
<!-- sources: ITIL 4 Information Security Management §2.4 Table 2.3 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of planned security exercises and tests (tabletop exercises, red team exercises, incident response drills) that were conducted within the defined schedule |
| **Formula** | (Exercises completed on schedule / Total planned exercises) x 100 |
| **Target** | 100% |
| **Frequency** | Per exercise cycle (at minimum annually) |
| **Data Source** | Exercise schedule, exercise reports |
| **Owner** | Information Security Manager |

### KPI-ISM-13: End-to-End Security Monitoring Coverage
<!-- sources: ITIL 4 Information Security Management §5.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of critical infrastructure, application, and network assets that are covered by centralized security monitoring (SIEM event collection and correlation) |
| **Formula** | (Critical assets with SIEM coverage / Total critical assets in inventory) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | SIEM configuration, information asset inventory |
| **Owner** | Security Analyst |

### KPI-ISM-14: Security-by-Design Adoption Rate
<!-- sources: ITIL 4 Information Security Management §2.4 Table 2.3 PSF4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of new or significantly changed services that underwent a formal security assessment before entering production |
| **Formula** | (Services with pre-production security assessment / Total new or significantly changed services deployed) x 100 |
| **Target** | 100% |
| **Frequency** | Per release cycle, reported quarterly |
| **Data Source** | Change management records, release records, security assessment reports |
| **Owner** | Security Architect |

### KPI-ISM-15: Post-Incident Improvement Implementation Rate
<!-- sources: ITIL 4 Information Security Management §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of improvement actions identified in post-incident reviews that were implemented within the agreed timeframe |
| **Formula** | (Post-incident improvements implemented on time / Total post-incident improvements agreed) x 100 |
| **Target** | >= 90% |
| **Frequency** | Quarterly |
| **Data Source** | Post-incident review reports, continual improvement register |
| **Owner** | Information Security Manager |

### KPI-ISM-16: Vulnerability Remediation Timeliness
<!-- sources: ITIL 4 Information Security Management §2.4 PSF2, §5.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of identified vulnerabilities (from scanning, penetration testing, or vendor advisories) that were remediated within the defined timeframe based on their severity rating |
| **Formula** | (Vulnerabilities remediated within SLA by severity / Total vulnerabilities identified by severity) x 100 |
| **Target** | Critical: 100% within 72 hours; High: >= 95% within 30 days; Medium: >= 90% within 90 days |
| **Frequency** | Monthly |
| **Data Source** | Vulnerability scanning tools, patch management records |
| **Owner** | Information Security Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| ISM-01 | Security Incident Rate | All | Monthly |
| ISM-02 | Security Policy Coverage | All | Quarterly |
| ISM-03 | Risk Assessment Coverage | All | Quarterly |
| ISM-04 | Security Control Coverage | All | Quarterly |
| ISM-05 | Access Rights Review Compliance | All | Per cycle |
| ISM-06 | Security Audit Completion Rate | T2+ | Per cycle |
| ISM-07 | Security Awareness Training Completion | T2+ | Per cycle |
| ISM-08 | Mean Time to Detect (MTTD) | T2+ | Monthly |
| ISM-09 | Mean Time to Contain (MTTC) | T2+ | Monthly |
| ISM-10 | Security Finding Remediation Rate | T2+ | Quarterly |
| ISM-11 | Supplier Security Compliance Rate | T2+ | Per cycle |
| ISM-12 | Security Exercise Completion Rate | T3 | Per cycle |
| ISM-13 | End-to-End Security Monitoring Coverage | T3 | Quarterly |
| ISM-14 | Security-by-Design Adoption Rate | T3 | Quarterly |
| ISM-15 | Post-Incident Improvement Implementation Rate | T3 | Quarterly |
| ISM-16 | Vulnerability Remediation Timeliness | T3 | Monthly |
