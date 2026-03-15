---
process_id: PR07
process_name: "Service Continuity Management"
category: kpis
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Service Continuity Management §2.4, §2.5 Table 2.8"
  - "FitSM-1: §PR4.1–§PR4.3"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Continuity Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the practice matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Service continuity management KPIs are mapped to three practice success factors: (1) developing and managing service continuity plans, (2) mitigating service continuity risks, and (3) ensuring awareness and readiness. Many metrics can only be measured during exercises or actual recovery events — the exercise programme is therefore essential for generating measurement data.

---

## Essential KPIs (T2+)

### KPI-SCM-01: Service Continuity Plan Coverage
<!-- sources: ITIL 4 SCM §2.5 Table 2.8 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of critical services within the defined scope that have documented, current service continuity plans covering response, recovery, and restoration. Services without plans cannot be recovered in a structured way during a disaster — recovery will be ad hoc, slower, and more likely to fail. Coverage should include plans at all three levels (strategic, tactical, operational) appropriate to the service's criticality |
| **Formula** | (Critical services with documented continuity plans / Total critical services in scope) × 100 |
| **Target** | 100% of in-scope critical services |
| **Frequency** | Quarterly |
| **Data Source** | Continuity plan repository, service catalogue |
| **Owner** | Service Continuity Manager |

### KPI-SCM-02: BIA Currency
<!-- sources: ITIL 4 SCM §2.5 Table 2.8 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of critical services with a current business impact analysis — defined as a BIA completed or reviewed within the agreed cycle (typically 12 months). Outdated BIA means recovery requirements may not reflect current business realities — VBFs may have changed, interdependencies may have shifted, and RTO/RPO targets may no longer be appropriate. BIA should be refreshed when context changes and otherwise at the agreed interval |
| **Formula** | (Critical services with BIA reviewed within agreed cycle / Total critical services in scope) × 100 |
| **Target** | 100% |
| **Frequency** | Annually |
| **Data Source** | BIA report registry, review dates |
| **Owner** | Service Continuity Manager |

### KPI-SCM-03: Recovery Requirements Completeness
<!-- sources: ITIL 4 SCM §2.5 Table 2.8 PSF1, FitSM-1 §PR4.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of critical services with clearly documented recovery requirements — including recovery time objective, recovery point objective, and minimum target service level. These three requirements are the foundation of all continuity planning — without them, strategies cannot be selected, plans cannot be developed, and exercises cannot be evaluated. Requirements should be traceable to BIA outputs and reflected in SLAs |
| **Formula** | (Critical services with documented RTO, RPO, and minimum target service level / Total critical services in scope) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | BIA reports, SLAs |
| **Owner** | Service Continuity Manager |

### KPI-SCM-04: Plan Currency
<!-- sources: ITIL 4 SCM §2.5 Table 2.8 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service continuity plans updated within the agreed review cycle — reflecting current service architecture, team assignments, contact information, and recovery procedures. Plans become stale as services, teams, and infrastructure change. Stale plans are less likely to work during actual invocation. Plans should be updated after exercises, after recovery events, and when services or team members change — in addition to scheduled reviews |
| **Formula** | (Plans updated within agreed review cycle / Total plans) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Continuity plan repository, version dates |
| **Owner** | Service Continuity Manager |

---

## Intermediate KPIs (T2+)

### KPI-SCM-05: Exercise Completion Rate
<!-- sources: ITIL 4 SCM §2.5 Table 2.8 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of scheduled exercises and awareness sessions performed on time according to the exercise programme. Missed or postponed exercises mean parts of the practice remain untested — reducing confidence in plans and team readiness. All parts of the practice should be tested at least annually. Higher-impact services should be exercised more frequently |
| **Formula** | (Exercises performed on schedule / Total exercises scheduled) × 100 |
| **Target** | ≥ 90% |
| **Frequency** | Semi-annually |
| **Data Source** | Exercise programme, exercise records |
| **Owner** | Service Continuity Manager |

### KPI-SCM-06: RTO Achievement Rate
<!-- sources: ITIL 4 SCM §2.5 Table 2.8 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of exercises and actual recovery events where the recovery time objective was achieved — service was resumed within the agreed maximum time. RTO failure during an exercise indicates plan or capability deficiency. RTO failure during an actual disaster means business impact exceeds acceptable levels. Should be measured for every exercise type that involves timed recovery (command-post, live, test) and every actual invocation |
| **Formula** | (Recoveries achieving RTO / Total recoveries measured) × 100 |
| **Target** | 100% |
| **Frequency** | Per exercise/recovery event |
| **Data Source** | Exercise reports, recovery reports |
| **Owner** | Service Continuity Manager |

### KPI-SCM-07: RPO Achievement Rate
<!-- sources: ITIL 4 SCM §2.5 Table 2.8 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of exercises and actual recovery events where the recovery point objective was achieved — data was restored to within the acceptable loss period. RPO failure means unacceptable data loss has occurred (or would occur during an exercise). RPO achievement depends on backup frequency, backup integrity, and restoration procedures. Should be verified during both exercises and actual recovery |
| **Formula** | (Recoveries achieving RPO / Total recoveries measured) × 100 |
| **Target** | 100% |
| **Frequency** | Per exercise/recovery event |
| **Data Source** | Exercise reports, recovery reports, backup records |
| **Owner** | Service Continuity Manager |

### KPI-SCM-08: Exercise Finding Resolution Rate
<!-- sources: ITIL 4 SCM §3.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of findings and recommendations from exercise and recovery reports that have been resolved within agreed timeframes. Unresolved findings represent known gaps in continuity capability — each unresolved finding means the plan is less likely to succeed during actual invocation. Failed exercises should be rescheduled as soon as possible. All findings should be tracked through to resolution |
| **Formula** | (Findings resolved within agreed timeframe / Total findings) × 100 |
| **Target** | ≥ 90%; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Exercise reports, finding tracking system |
| **Owner** | Service Continuity Manager |

---

## Advanced KPIs (T3)

### KPI-SCM-09: Continuity Measure Effectiveness
<!-- sources: ITIL 4 SCM §2.4.2, §2.5 Table 2.8 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The ratio between actual losses from disruptive events and the expected losses estimated during BIA — measuring whether continuity measures are delivering the risk reduction they were designed to provide. A ratio below 1.0 indicates measures are effective (actual losses less than expected). A ratio above 1.0 indicates measures are insufficient. Should be assessed for every actual recovery event and used to calibrate BIA estimates and strategy selection |
| **Formula** | Actual losses from disruptive events / Expected losses from BIA |
| **Target** | < 1.0; trending downward |
| **Frequency** | Per recovery event; aggregated annually |
| **Data Source** | Recovery reports, BIA reports, financial records |
| **Owner** | Service Continuity Manager |

### KPI-SCM-10: Stakeholder Satisfaction with Continuity Readiness
<!-- sources: ITIL 4 SCM §2.4.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Satisfaction of key stakeholders — including service owners, executive management, and customers — with the organization's service continuity readiness. Covers confidence in plans, exercise quality, communication effectiveness, and perceived preparedness for disaster scenarios. Low satisfaction may indicate insufficient exercise rigour, inadequate communication, or unresolved concerns about capability gaps |
| **Formula** | Average satisfaction score from stakeholder survey (scale 1–5 or equivalent) |
| **Target** | ≥ 4.0 / 5.0 |
| **Frequency** | Annually |
| **Data Source** | Stakeholder satisfaction surveys |
| **Owner** | Service Continuity Manager |

### KPI-SCM-11: Audit Compliance Rate
<!-- sources: ITIL 4 SCM §3.2.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service continuity audit findings resolved within agreed timeframes — measuring the organization's responsiveness to identified compliance gaps and improvement opportunities. Audits verify that BIA, strategies, and plans remain appropriate. Unresolved audit findings may represent regulatory compliance risks in addition to capability gaps |
| **Formula** | (Audit findings resolved within agreed timeframe / Total audit findings) × 100 |
| **Target** | 100% |
| **Frequency** | Per audit cycle |
| **Data Source** | Audit reports, remediation tracking |
| **Owner** | Service Continuity Manager |

### KPI-SCM-12: Partner Continuity Integration
<!-- sources: ITIL 4 SCM §6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of critical partners and suppliers with agreed, documented, and tested service continuity arrangements that align with the organization's continuity plans. Third-party dependencies are increasingly significant — cloud services and integrated digital services create critical dependencies that may be outside the organization's direct control. Partners without aligned continuity arrangements represent uncontrolled recovery risks |
| **Formula** | (Critical partners with aligned and tested continuity arrangements / Total critical partners) × 100 |
| **Target** | ≥ 80%; trending toward 100% |
| **Frequency** | Annually |
| **Data Source** | Supplier agreements, partner continuity documentation, joint exercise records |
| **Owner** | Service Continuity Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SCM-01 | Service Continuity Plan Coverage | T2+ | Quarterly |
| SCM-02 | BIA Currency | T2+ | Annually |
| SCM-03 | Recovery Requirements Completeness | T2+ | Quarterly |
| SCM-04 | Plan Currency | T2+ | Quarterly |
| SCM-05 | Exercise Completion Rate | T2+ | Semi-annually |
| SCM-06 | RTO Achievement Rate | T2+ | Per event |
| SCM-07 | RPO Achievement Rate | T2+ | Per event |
| SCM-08 | Exercise Finding Resolution Rate | T2+ | Quarterly |
| SCM-09 | Continuity Measure Effectiveness | T3 | Per event / Annually |
| SCM-10 | Stakeholder Satisfaction with Readiness | T3 | Annually |
| SCM-11 | Audit Compliance Rate | T3 | Per audit cycle |
| SCM-12 | Partner Continuity Integration | T3 | Annually |
