---
process_id: PR02
process_name: "Service Level Management"
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
  - "ITIL 4: Service Level Management §2.4"
  - "FitSM-2: §PR2 SLM"
  - "IT4IT: R2F Service Level Component"
last_updated: 2026-03-13
status: draft
---

# Service Level Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions).

---

## Essential KPIs (All Tiers)

### KPI-SLM-01: SLA Coverage
<!-- sources: FitSM-2 §PR2, ITIL 4 Service Level Management §2.4 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of critical and customer-facing services that have a formal SLA in place (individual or default) |
| **Formula** | (Services with active SLA / Total customer-facing services) x 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Agreement register, service catalogue |
| **Owner** | Service Level Manager |

### KPI-SLM-02: SLA Compliance Rate
<!-- sources: ITIL 4 Service Level Management §2.4 PSF2, FitSM-2 §PR2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of SLA targets that were met during the reporting period across all active SLAs |
| **Formula** | (SLA targets met / Total SLA targets evaluated) x 100 |
| **Target** | >= 95% |
| **Frequency** | Monthly |
| **Data Source** | SLA fulfilment reports, monitoring systems |
| **Owner** | Service Level Manager |

### KPI-SLM-03: Service Catalogue Completeness
<!-- sources: FitSM-2 §PR2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of live services in the service portfolio that have a corresponding, up-to-date entry in the service catalogue |
| **Formula** | (Services in catalogue / Total live services in portfolio) x 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Service catalogue, service portfolio register |
| **Owner** | Service Level Manager |

### KPI-SLM-04: SLA Violation Notification Timeliness
<!-- sources: FitSM-2 §PR2, ITIL 4 Service Level Management §2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of SLA violations where the customer was notified within the agreed notification timeframe |
| **Formula** | (Violations notified within SLA / Total violations) x 100 |
| **Target** | 100% |
| **Frequency** | Monthly |
| **Data Source** | Violation notification records, SLA fulfilment reports |
| **Owner** | Service Level Manager |

### KPI-SLM-05: Supporting Agreement Coverage
<!-- sources: FitSM-2 §PR2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of SLA commitments that are underpinned by corresponding OLAs and/or UAs |
| **Formula** | (SLA targets with OLA/UA backing / Total SLA targets requiring operational support) x 100 |
| **Target** | >= 90% |
| **Frequency** | Quarterly |
| **Data Source** | Agreement register |
| **Owner** | Service Level Manager |

---

## Intermediate KPIs (T2+)

### KPI-SLM-06: Service Review Adherence
<!-- sources: ITIL 4 Service Level Management §2.4 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of scheduled service reviews that were conducted on time with required stakeholder participation |
| **Formula** | (Reviews conducted on schedule / Total scheduled reviews) x 100 |
| **Target** | 100% |
| **Frequency** | Per review cycle (e.g., quarterly) |
| **Data Source** | Service review reports, meeting records |
| **Owner** | Service Level Manager |

### KPI-SLM-07: Customer Satisfaction Score
<!-- sources: ITIL 4 Service Level Management §2.4 PSF1, PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Average satisfaction score from customer surveys regarding service quality, communication, and service level management effectiveness |
| **Formula** | Average of customer satisfaction survey scores (scale 1-5) |
| **Target** | >= 3.5 / 5 |
| **Frequency** | Semi-annually |
| **Data Source** | Customer satisfaction surveys |
| **Owner** | Relationship Manager |

### KPI-SLM-08: User Satisfaction Score
<!-- sources: ITIL 4 Service Level Management §2.4 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Average satisfaction score from end-user surveys regarding the usability, responsiveness, and quality of services they consume |
| **Formula** | Average of user satisfaction survey scores (scale 1-5) |
| **Target** | >= 3.5 / 5 |
| **Frequency** | Quarterly |
| **Data Source** | User satisfaction surveys, feedback tools |
| **Owner** | Service Level Manager |

### KPI-SLM-09: OLA/UA Compliance Rate
<!-- sources: FitSM-2 §PR2, ITIL 4 Service Level Management §2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of OLA and UA targets that were met during the reporting period |
| **Formula** | (OLA/UA targets met / Total OLA/UA targets evaluated) x 100 |
| **Target** | >= 95% |
| **Frequency** | Monthly |
| **Data Source** | OLA/UA fulfilment reports, monitoring systems |
| **Owner** | Service Level Manager |

### KPI-SLM-10: Improvement Initiative Completion Rate
<!-- sources: ITIL 4 Service Level Management §2.4 PSF4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of service-level-related improvement initiatives identified in service reviews that were completed within the agreed timeframe |
| **Formula** | (Improvement actions completed on time / Total improvement actions agreed) x 100 |
| **Target** | >= 80% |
| **Frequency** | Per review cycle |
| **Data Source** | Service review reports, improvement register |
| **Owner** | Service Owner |

### KPI-SLM-11: SLA Renegotiation Cycle Time
<!-- sources: ITIL 4 Service Level Management §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Average elapsed time from SLA review initiation to formal agreement on renewed or revised terms |
| **Formula** | Average(Sign-off date - Review initiation date) for all SLA renewals in period |
| **Target** | <= 30 calendar days |
| **Frequency** | Per occurrence, reported quarterly |
| **Data Source** | Agreement register (SLA review timestamps) |
| **Owner** | Service Level Manager |

---

## Advanced KPIs (T3)

### KPI-SLM-12: Watermelon Detection Rate
<!-- sources: ITIL 4 Service Level Management §2.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of services where a significant gap is detected between technical SLA compliance (green) and customer/user satisfaction (below target), indicating a watermelon effect |
| **Formula** | (Services with SLA compliance >= 95% AND satisfaction < 3.0) / Total services monitored) x 100 |
| **Target** | Trending toward 0% (fewer undetected watermelons) |
| **Frequency** | Quarterly |
| **Data Source** | SLA fulfilment reports, satisfaction survey results |
| **Owner** | Service Quality Analyst |

### KPI-SLM-13: End-to-End Service Quality Index
<!-- sources: ITIL 4 Service Level Management §2.3, IT4IT §5.4 Deploy Value Stream -->

| Attribute | Value |
|-----------|-------|
| **Description** | Composite score measuring service quality across all seven quality aspects (functionality, availability, performance, timeliness, user support, accuracy, UX), weighted by business importance |
| **Formula** | Weighted average of normalized scores across all quality aspects (organization-defined weighting) |
| **Target** | Positive trend quarter-over-quarter |
| **Frequency** | Quarterly |
| **Data Source** | Service quality dashboard, monitoring systems, satisfaction surveys |
| **Owner** | Service Quality Analyst |

### KPI-SLM-14: SLA Lifecycle Automation Rate
<!-- sources: ITIL 4 Service Level Management §5.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of SLA lifecycle activities (drafting, viability checking, renewal notification, expiry management) that are automated for standardized services |
| **Formula** | (Automated SLA lifecycle steps / Total SLA lifecycle steps for standardized services) x 100 |
| **Target** | >= 70% |
| **Frequency** | Annually |
| **Data Source** | ITSM tool configuration, process audit |
| **Owner** | Service Level Manager |

### KPI-SLM-15: Multi-Supplier SLA Integration Compliance
<!-- sources: SIAM concepts, IT4IT §8 R2F -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of multi-supplier services where end-to-end SLA compliance is tracked and reported, with individual supplier contributions identified |
| **Formula** | (Multi-supplier services with integrated SLA tracking / Total multi-supplier services) x 100 |
| **Target** | >= 90% |
| **Frequency** | Quarterly |
| **Data Source** | Agreement register, supplier performance reports, monitoring systems |
| **Owner** | Supplier Manager |

### KPI-SLM-16: Predictive Breach Detection Rate
<!-- sources: ITIL 4 Service Level Management §5.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of SLA breaches that were predicted by trend analysis or automated alerting before the breach actually occurred, enabling proactive intervention |
| **Formula** | (Breaches predicted before occurrence / Total breaches in period) x 100 |
| **Target** | >= 50% |
| **Frequency** | Monthly |
| **Data Source** | Monitoring and alerting systems, SLA fulfilment reports |
| **Owner** | Service Quality Analyst |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SLM-01 | SLA Coverage | All | Quarterly |
| SLM-02 | SLA Compliance Rate | All | Monthly |
| SLM-03 | Service Catalogue Completeness | All | Quarterly |
| SLM-04 | SLA Violation Notification Timeliness | All | Monthly |
| SLM-05 | Supporting Agreement Coverage | All | Quarterly |
| SLM-06 | Service Review Adherence | T2+ | Per cycle |
| SLM-07 | Customer Satisfaction Score | T2+ | Semi-annually |
| SLM-08 | User Satisfaction Score | T2+ | Quarterly |
| SLM-09 | OLA/UA Compliance Rate | T2+ | Monthly |
| SLM-10 | Improvement Initiative Completion Rate | T2+ | Per cycle |
| SLM-11 | SLA Renegotiation Cycle Time | T2+ | Quarterly |
| SLM-12 | Watermelon Detection Rate | T3 | Quarterly |
| SLM-13 | End-to-End Service Quality Index | T3 | Quarterly |
| SLM-14 | SLA Lifecycle Automation Rate | T3 | Annually |
| SLM-15 | Multi-Supplier SLA Integration Compliance | T3 | Quarterly |
| SLM-16 | Predictive Breach Detection Rate | T3 | Monthly |
