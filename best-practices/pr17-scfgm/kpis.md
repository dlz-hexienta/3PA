---
process_id: PR17
process_name: "Service Configuration Management"
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
  - "ITIL 4: Service Configuration Management §2.5 Table 2.4"
  - "FitSM-2: §PR11 CONFM"
  - "IT4IT: Cross-cutting (CMDB/CMS)"
last_updated: 2026-03-13
status: draft
---

# Service Configuration Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions).

---

## Essential KPIs (All Tiers)

### KPI-SCFGM-01: CMDB Completeness Rate
<!-- sources: ITIL 4 Service Configuration Management §2.5 Table 2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of known CIs defined as in scope that have a corresponding record in the CMDB with all required attributes populated |
| **Formula** | (CIs with complete CMDB records / Total CIs defined as in scope) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | CMDB, CI scope definition, discovery tools (where available) |
| **Owner** | Configuration Manager |

### KPI-SCFGM-02: CMDB Accuracy Rate
<!-- sources: ITIL 4 Service Configuration Management §2.5 Table 2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of CI records in the CMDB that are verified as accurate — meaning their recorded attributes and relationships match the actual state of the infrastructure |
| **Formula** | (CI records verified as accurate / Total CI records verified) x 100 |
| **Target** | >= 90% (trending upward) |
| **Frequency** | Per verification cycle; reported quarterly |
| **Data Source** | CMDB verification reports |
| **Owner** | Configuration Manager |

### KPI-SCFGM-03: CI Record Currency
<!-- sources: ITIL 4 Service Configuration Management §2.5 Table 2.4, FitSM-2 §PR11 CONFM -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of CI records that were updated within the defined timeframe following a change — measuring how promptly CMDB records reflect authorized changes to the infrastructure |
| **Formula** | (CI records updated within defined timeframe after change / Total changes requiring CMDB updates) x 100 |
| **Target** | >= 90% |
| **Frequency** | Monthly |
| **Data Source** | CMDB change audit trail, change management records |
| **Owner** | Configuration Manager |

### KPI-SCFGM-04: Configuration Scope Coverage
<!-- sources: ITIL 4 Service Configuration Management §2.4 PSF1, FitSM-2 §PR11 CONFM -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of critical services whose supporting CIs (infrastructure, applications, and key dependencies) are defined and recorded in the CMDB |
| **Formula** | (Critical services with CIs recorded in CMDB / Total critical services) x 100 |
| **Target** | 100% for critical services |
| **Frequency** | Quarterly |
| **Data Source** | Service portfolio, CMDB |
| **Owner** | Configuration Manager |

---

## Intermediate KPIs (T2+)

### KPI-SCFGM-05: CMDB Verification Coverage
<!-- sources: ITIL 4 Service Configuration Management §2.5 Table 2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of CMDB data that has been verified against the actual state of the infrastructure within the defined verification period |
| **Formula** | (CI records verified within defined period / Total CI records in CMDB) x 100 |
| **Target** | 100% of CIs verified at least annually; critical CIs verified quarterly |
| **Frequency** | Quarterly |
| **Data Source** | CMDB verification reports, verification schedule |
| **Owner** | Configuration Manager |

### KPI-SCFGM-06: Verification Discrepancy Rate
<!-- sources: ITIL 4 Service Configuration Management §2.2.5, §3.2.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Number of discrepancies identified per verification cycle, categorized by type: unregistered CIs, unregistered authorized changes, unauthorized changes, incorrect attributes, and incorrect relationships |
| **Formula** | Count of discrepancies per verification cycle, segmented by type |
| **Target** | Trending downward period-over-period |
| **Frequency** | Per verification cycle |
| **Data Source** | CMDB verification reports |
| **Owner** | Configuration Manager |

### KPI-SCFGM-07: Verification Corrective Action Completion Rate
<!-- sources: ITIL 4 Service Configuration Management §3.2.3 Table 3.5 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of corrective actions arising from CMDB verification findings that were implemented within the agreed timeframe |
| **Formula** | (Corrective actions completed on time / Total corrective actions from verification) x 100 |
| **Target** | >= 90% |
| **Frequency** | Per verification cycle; reported quarterly |
| **Data Source** | CMDB verification reports, corrective action tracker |
| **Owner** | Configuration Manager |

### KPI-SCFGM-08: Stakeholder Satisfaction with Configuration Information
<!-- sources: ITIL 4 Service Configuration Management §2.5 Table 2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Satisfaction score from stakeholders who consume configuration information (incident management, change management, availability management, service owners, management), assessing the accuracy, completeness, timeliness, and usability of the information provided |
| **Formula** | Average satisfaction score from periodic stakeholder survey (scale 1–5) |
| **Target** | >= 4.0 |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder satisfaction survey |
| **Owner** | Configuration Manager |

### KPI-SCFGM-09: CI Model Coverage
<!-- sources: ITIL 4 Service Configuration Management §2.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of CI types in scope that have a formally defined and current CI model in the CI models library |
| **Formula** | (CI types with current CI model / Total CI types in scope) x 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | CI models library, CI scope definition |
| **Owner** | Configuration Manager |

### KPI-SCFGM-10: Bad Decisions Attributed to Incorrect Configuration Data
<!-- sources: ITIL 4 Service Configuration Management §2.5 Table 2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Number of incidents, failed changes, incorrect impact assessments, or other adverse events where incorrect or missing CMDB data was identified as a contributing factor |
| **Formula** | Count of adverse events attributed to CMDB data quality issues in the reporting period |
| **Target** | Zero; trending downward |
| **Frequency** | Monthly |
| **Data Source** | Incident records, change records, post-incident reviews, problem records |
| **Owner** | Configuration Manager |

---

## Advanced KPIs (T3)

### KPI-SCFGM-11: Automated Discovery Coverage
<!-- sources: ITIL 4 Service Configuration Management §5.2 Table 5.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of critical infrastructure CIs that are covered by automated discovery and CMDB reconciliation — meaning their configuration data is automatically collected and compared with CMDB records |
| **Formula** | (Critical CIs with automated discovery coverage / Total critical infrastructure CIs) x 100 |
| **Target** | >= 90% |
| **Frequency** | Quarterly |
| **Data Source** | Discovery tool configuration, CMDB, CI scope definition |
| **Owner** | Configuration Manager |

### KPI-SCFGM-12: Service Configuration Model Coverage
<!-- sources: ITIL 4 Service Configuration Management §2.2.1, §2.4.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of critical services that have a complete service configuration model in the CMS enabling automated impact analysis, cost allocation, and availability analysis |
| **Formula** | (Critical services with complete service configuration model / Total critical services) x 100 |
| **Target** | >= 90% |
| **Frequency** | Quarterly |
| **Data Source** | CMS, service portfolio |
| **Owner** | Configuration Manager |

### KPI-SCFGM-13: Unauthorized Change Detection Rate
<!-- sources: ITIL 4 Service Configuration Management §2.2.5 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of unauthorized changes (modifications made without change management approval) that were detected through configuration verification rather than after causing an incident or failure |
| **Formula** | (Unauthorized changes detected by verification / Total unauthorized changes detected) x 100 |
| **Target** | >= 80% (trending upward) |
| **Frequency** | Quarterly |
| **Data Source** | CMDB verification reports, incident records, change records |
| **Owner** | Configuration Manager |

### KPI-SCFGM-14: Configuration Management Cost Efficiency
<!-- sources: ITIL 4 Service Configuration Management §2.5 Table 2.4, §2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Direct costs of service configuration management (staffing, tooling, verification effort) as a proportion of total IT service management costs, tracked to ensure the practice delivers value proportionate to its cost |
| **Formula** | (Direct SCM costs / Total ITSM costs) x 100 |
| **Target** | Organization-specific; trending stable or downward while data quality targets are met |
| **Frequency** | Annually |
| **Data Source** | Financial records, SCM cost tracking |
| **Owner** | Configuration Manager |

### KPI-SCFGM-15: Cross-Supplier Configuration Data Quality
<!-- sources: ITIL 4 Service Configuration Management §6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of supplier-provided CIs with verified accurate configuration data — measuring the effectiveness of cross-supplier configuration management arrangements |
| **Formula** | (Supplier CIs verified as accurate / Total supplier CIs verified) x 100 |
| **Target** | >= 90% |
| **Frequency** | Per supplier verification cycle; reported annually |
| **Data Source** | CMDB verification reports (supplier scope), supplier data exchange records |
| **Owner** | Configuration Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SCFGM-01 | CMDB Completeness Rate | All | Quarterly |
| SCFGM-02 | CMDB Accuracy Rate | All | Per cycle |
| SCFGM-03 | CI Record Currency | All | Monthly |
| SCFGM-04 | Configuration Scope Coverage | All | Quarterly |
| SCFGM-05 | CMDB Verification Coverage | T2+ | Quarterly |
| SCFGM-06 | Verification Discrepancy Rate | T2+ | Per cycle |
| SCFGM-07 | Verification Corrective Action Completion Rate | T2+ | Per cycle |
| SCFGM-08 | Stakeholder Satisfaction with Configuration Information | T2+ | Semi-annually |
| SCFGM-09 | CI Model Coverage | T2+ | Quarterly |
| SCFGM-10 | Bad Decisions Attributed to Incorrect Configuration Data | T2+ | Monthly |
| SCFGM-11 | Automated Discovery Coverage | T3 | Quarterly |
| SCFGM-12 | Service Configuration Model Coverage | T3 | Quarterly |
| SCFGM-13 | Unauthorized Change Detection Rate | T3 | Quarterly |
| SCFGM-14 | Configuration Management Cost Efficiency | T3 | Annually |
| SCFGM-15 | Cross-Supplier Configuration Data Quality | T3 | Per cycle |
