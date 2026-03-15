---
process_id: PR23
process_name: "Supplier Management"
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
tier_minimum: T2
sources:
  - "ITIL 4: Supplier Management §2.5 Table 2.3"
  - "FitSM-2: §PR8 SUPPM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (supplier coordination)"
last_updated: 2026-03-13
status: draft
---

# Supplier Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions).

---

## Essential KPIs (All organizations implementing this process)

### KPI-SUPPM-01: Supplier Performance Against Targets
<!-- sources: ITIL 4 Supplier Management §2.5 Table 2.3 PSF2/PSF3, FitSM-2 §PR8 SUPPM (monitor supplier performance) -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of suppliers meeting or exceeding their agreed performance targets (KPIs and service levels defined in contracts) within the reporting period |
| **Formula** | (Suppliers meeting all agreed targets / Total suppliers with active contracts) x 100 |
| **Target** | >= 90% |
| **Frequency** | Quarterly |
| **Data Source** | Supplier performance reports, contract KPIs |
| **Owner** | Supplier Manager |

### KPI-SUPPM-02: Supplier Contract Compliance Rate
<!-- sources: ITIL 4 Supplier Management §2.4.1, §3.2.2 Table 3.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of supplier contracts where the supplier is meeting all contractual obligations — including service levels, deliverables, reporting requirements, and terms and conditions |
| **Formula** | (Contracts with full compliance / Total active contracts) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | Contract compliance reviews, supplier audit results |
| **Owner** | Supplier Manager |

### KPI-SUPPM-03: Supplier Review Completion Rate
<!-- sources: FitSM-2 §PR8 SUPPM, ITIL 4 Supplier Management §3.2.2 Table 3.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of scheduled supplier performance reviews that were conducted within the agreed period |
| **Formula** | (Supplier reviews conducted / Supplier reviews scheduled) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | Supplier review schedule, supplier review reports |
| **Owner** | Supplier Manager |

### KPI-SUPPM-04: Supplier Database Coverage
<!-- sources: FitSM-2 §PR8 SUPPM (maintain supplier database), ITIL 4 Supplier Management §5.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of known suppliers (internal and external) providing services to the organization that have a current, complete record in the supplier database with all required attributes populated |
| **Formula** | (Suppliers with complete database records / Total known suppliers) x 100 |
| **Target** | >= 95% |
| **Frequency** | Quarterly |
| **Data Source** | Supplier database, contract register |
| **Owner** | Supplier Manager |

---

## Intermediate KPIs (T2+)

### KPI-SUPPM-05: Supplier-Related Incident and SLA Breach Rate
<!-- sources: ITIL 4 Supplier Management §2.5 Table 2.3 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Number and impact of incidents and SLA breaches associated with third-party supplier participation in the organization's value streams — measuring the effectiveness of supplier integration and performance |
| **Formula** | Count of supplier-related incidents and SLA breaches per reporting period, segmented by severity and supplier |
| **Target** | Trending downward; zero critical supplier-related SLA breaches |
| **Frequency** | Monthly |
| **Data Source** | Incident records, SLA breach reports, service level reports |
| **Owner** | Supplier Manager |

### KPI-SUPPM-06: Regulatory Compliance and Breach Rate
<!-- sources: ITIL 4 Supplier Management §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Number and impact of breaches to relevant internal and external regulations identified through supplier compliance audits and governance reviews |
| **Formula** | Count of regulatory breaches per reporting period, segmented by severity and regulation type |
| **Target** | Zero; trending downward |
| **Frequency** | Quarterly |
| **Data Source** | Compliance audit reports, governance meeting records |
| **Owner** | Supplier Manager |

### KPI-SUPPM-07: Supplier Categorization Coverage
<!-- sources: ITIL 4 Supplier Management §2.4.1, §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of active suppliers that have been formally categorized according to the sourcing strategy's categorization scheme (generic/commodity, operational/tactical, strategic/partner) with management effort aligned to significance |
| **Formula** | (Suppliers formally categorized / Total active suppliers) x 100 |
| **Target** | 100% |
| **Frequency** | Semi-annually |
| **Data Source** | Supplier database, sourcing strategy |
| **Owner** | Supplier Manager |

### KPI-SUPPM-08: Supplier Follow-Up Action Completion Rate
<!-- sources: FitSM-2 §PR8 SUPPM (track implementation of follow-up actions), ITIL 4 Supplier Management §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of follow-up actions agreed during supplier reviews that were completed within the agreed timeframe — measuring the organization's follow-through on supplier improvement commitments |
| **Formula** | (Follow-up actions completed on time / Total follow-up actions agreed) x 100 |
| **Target** | >= 85% |
| **Frequency** | Quarterly |
| **Data Source** | Supplier review reports, action trackers |
| **Owner** | Supplier Manager |

### KPI-SUPPM-09: Stakeholder Satisfaction with Supplier Relationships
<!-- sources: ITIL 4 Supplier Management §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Satisfaction score from internal stakeholders (service owners, service level managers, operational teams) who interact with or depend on third-party suppliers, assessing the quality, responsiveness, and effectiveness of supplier relationships |
| **Formula** | Average satisfaction score from periodic stakeholder survey (scale 1–5) |
| **Target** | >= 3.5 (trending upward) |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder satisfaction survey |
| **Owner** | Supplier Manager |

### KPI-SUPPM-10: Supplier Dependency Matrix Currency
<!-- sources: ITIL 4 Supplier Management §2.4.3, §3.2.1 Table 3.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Percentage of entries in the supplier dependency matrix that have been reviewed and confirmed as accurate within the defined review period — measuring the reliability of dependency information for impact analysis and sourcing decisions |
| **Formula** | (Dependency matrix entries reviewed within defined period / Total entries in dependency matrix) x 100 |
| **Target** | 100% reviewed at least annually |
| **Frequency** | Semi-annually |
| **Data Source** | Supplier dependency matrix, review records |
| **Owner** | Supplier Manager |

---

## Advanced KPIs (T3)

### KPI-SUPPM-11: Supplier Value Realization
<!-- sources: ITIL 4 Supplier Management §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Realized value from relationships with suppliers and partners, including measurable benefits (cost savings, service improvements, innovation contributions), risks mitigated, and total costs — providing a comprehensive view of the value delivered by the supplier ecosystem |
| **Formula** | Composite assessment of: (1) year-on-year financial benefit, (2) innovation and improvement contributions, (3) risk reduction, (4) strategic alignment — reported as a value score or financial metric |
| **Target** | Positive year-on-year trend; value exceeds total cost of supplier management |
| **Frequency** | Annually |
| **Data Source** | Supplier scorecards, financial records, value realization assessments |
| **Owner** | Supplier Manager |

### KPI-SUPPM-12: Third-Party Integration Effectiveness
<!-- sources: ITIL 4 Supplier Management §2.5 Table 2.3 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Stakeholder satisfaction with third-party suppliers' integration into the organization's value streams, combined with a measure of losses, delays, and waste caused by ineffective third-party integration |
| **Formula** | Composite score from: (1) stakeholder satisfaction with integration (scale 1–5), (2) count and impact of integration-related incidents or delays |
| **Target** | Satisfaction >= 4.0; integration incidents trending downward |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder surveys, incident records, service reports |
| **Owner** | Supplier Manager |

### KPI-SUPPM-13: Sourcing Strategy Effectiveness
<!-- sources: ITIL 4 Supplier Management §2.5 Table 2.3 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Assessment of how effectively the sourcing strategy supports the organization's strategic objectives — measured by the number of cases where strategic objectives could not be achieved due to third-party dependencies, and the degree of alignment between sourcing strategy objectives and organizational strategy |
| **Formula** | Composite: (1) count of strategic objectives impacted by third-party dependencies, (2) percentage of sourcing strategy objectives linked to organizational strategy |
| **Target** | Zero strategic objectives impacted; 100% alignment |
| **Frequency** | Annually |
| **Data Source** | Strategic planning records, sourcing strategy, supplier performance data |
| **Owner** | Supplier Manager |

### KPI-SUPPM-14: Supplier Onboarding and Offboarding Effectiveness
<!-- sources: ITIL 4 Supplier Management §2.4.3, §3.2.2 Table 3.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Timeliness and effectiveness of supplier onboarding and offboarding activities — measured by the percentage of onboarding/offboarding events completed on schedule and without service disruption, and the accuracy of the supplier dependency matrix following transitions |
| **Formula** | (Onboarding/offboarding events completed on schedule without disruption / Total onboarding/offboarding events) x 100 |
| **Target** | >= 90% |
| **Frequency** | Per event; reported annually |
| **Data Source** | Onboarding/offboarding records, incident records, supplier dependency matrix |
| **Owner** | Supplier Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SUPPM-01 | Supplier Performance Against Targets | All | Quarterly |
| SUPPM-02 | Supplier Contract Compliance Rate | All | Quarterly |
| SUPPM-03 | Supplier Review Completion Rate | All | Quarterly |
| SUPPM-04 | Supplier Database Coverage | All | Quarterly |
| SUPPM-05 | Supplier-Related Incident and SLA Breach Rate | T2+ | Monthly |
| SUPPM-06 | Regulatory Compliance and Breach Rate | T2+ | Quarterly |
| SUPPM-07 | Supplier Categorization Coverage | T2+ | Semi-annually |
| SUPPM-08 | Supplier Follow-Up Action Completion Rate | T2+ | Quarterly |
| SUPPM-09 | Stakeholder Satisfaction with Supplier Relationships | T2+ | Semi-annually |
| SUPPM-10 | Supplier Dependency Matrix Currency | T2+ | Semi-annually |
| SUPPM-11 | Supplier Value Realization | T3 | Annually |
| SUPPM-12 | Third-Party Integration Effectiveness | T3 | Semi-annually |
| SUPPM-13 | Sourcing Strategy Effectiveness | T3 | Annually |
| SUPPM-14 | Supplier Onboarding and Offboarding Effectiveness | T3 | Per event |
