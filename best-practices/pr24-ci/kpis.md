---
process_id: PR24
process_name: "Continual Improvement"
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
  - "ITIL 4: Continual Improvement §2.4, §2.5 Table 2.2"
  - "FitSM-2: §PR14 CSI"
  - "IT4IT: Cross-cutting"
last_updated: 2026-03-14
status: draft
---

# Continual Improvement — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the process matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Continual improvement KPIs are mapped to two practice success factors: (1) establishing and maintaining an effective approach to continual improvement, and (2) ensuring effective and efficient improvement across the organization. Measuring continual improvement is inherently challenging because value in the service value system results from complex interactions, multiple improvements may occur simultaneously, and there is usually a significant delay between implementation and value realization.

---

## Essential KPIs (All tiers)

### KPI-CI-01: Improvement Initiative Completion Rate
<!-- sources: ITIL 4 Continual Improvement §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of approved improvement initiatives that were completed (implemented and evaluated) during the reporting period. This is the primary indicator of whether the continual improvement practice is translating ideas into action. A low completion rate indicates barriers to implementation — insufficient resources, poor planning, or competing priorities |
| **Formula** | (Improvement initiatives completed / Total approved improvement initiatives) × 100 |
| **Target** | ≥ 80%; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Continual improvement register (CIR) |
| **Owner** | Continual Improvement Manager |

### KPI-CI-02: Improvement Success Rate
<!-- sources: ITIL 4 Continual Improvement §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of completed improvement initiatives that achieved their intended outcomes — measured against agreed success criteria and KPIs. Distinguishes between initiatives that were merely completed and those that actually delivered value. Initiatives that did not achieve planned outcomes should be reviewed for lessons learned and gaps prioritized for following iterations |
| **Formula** | (Improvement initiatives achieving intended outcomes / Total completed improvement initiatives) × 100 |
| **Target** | ≥ 70%; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | CIR, improvement evaluation records |
| **Owner** | Continual Improvement Manager |

### KPI-CI-03: Improvement Opportunity Volume
<!-- sources: ITIL 4 Continual Improvement §2.4.2.1, FitSM-2 §PR14 CSI -->

| Attribute | Value |
|-----------|-------|
| **Description** | The total number of improvement opportunities identified and logged in the CIR during the reporting period. The volume of opportunities identified is a metric for how well the continual improvement practice has been established within the organization. A declining volume may indicate cultural barriers to suggestion, while a healthy volume indicates broad engagement. Should be tracked by source to identify areas of the organization that are or are not contributing |
| **Formula** | Count of new improvement opportunities logged in CIR per period |
| **Target** | Stable or trending upward; distributed across organizational areas |
| **Frequency** | Monthly |
| **Data Source** | CIR |
| **Owner** | Continual Improvement Manager |

### KPI-CI-04: Improvement Initiative Timeliness
<!-- sources: ITIL 4 Continual Improvement §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of improvement initiatives realized in line with planned timelines and costs. Measures whether improvement planning is realistic and whether initiatives are being delivered as expected. Significant variance from planned timelines and costs may indicate poor scoping, insufficient resources, or unrealistic expectations |
| **Formula** | (Improvement initiatives completed within planned timeline and cost / Total completed improvement initiatives) × 100 |
| **Target** | ≥ 70%; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | CIR, improvement plans |
| **Owner** | Continual Improvement Manager |

---

## Intermediate KPIs (T2+)

### KPI-CI-05: Improvement Approach Adoption
<!-- sources: ITIL 4 Continual Improvement §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The degree of awareness and adoption of the continual improvement approach across the organization — measured through surveys, participation metrics, or compliance assessments. Indicates whether the improvement framework has been embedded beyond the continual improvement team to become a genuine organizational capability. Low adoption indicates that the practice remains centralized rather than distributed |
| **Formula** | Composite score from adoption survey or (Teams actively using the CI approach / Total teams) × 100 |
| **Target** | Trending upward; ≥ 80% of teams actively engaged |
| **Frequency** | Semi-annually |
| **Data Source** | Adoption surveys, CIR participation data |
| **Owner** | Continual Improvement Manager |

### KPI-CI-06: Stakeholder Satisfaction with Improvement
<!-- sources: ITIL 4 Continual Improvement §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Stakeholder satisfaction with the organization's ability to obtain value from improvement initiatives. Measures the perceived effectiveness of the continual improvement practice from the perspective of those who submit ideas, sponsor initiatives, and experience the outcomes. Low satisfaction may indicate slow responsiveness, poor communication, or failure to deliver expected value |
| **Formula** | Average satisfaction score from stakeholder survey (scale 1–5 or equivalent) |
| **Target** | ≥ 4.0 / 5.0; trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder satisfaction surveys |
| **Owner** | Continual Improvement Manager |

### KPI-CI-07: Lessons Learned Capture Rate
<!-- sources: ITIL 4 Continual Improvement §2.4.1.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of completed improvement initiatives for which lessons learned were captured and documented. Step 6 of the continual improvement model (did we get there?) should always capture lessons learned. If this step is skipped, improvements remain isolated initiatives and progress may be lost over time. Measures whether the organization is learning systematically from its improvement efforts |
| **Formula** | (Initiatives with documented lessons learned / Total completed initiatives) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | CIR, lessons learned reports |
| **Owner** | Continual Improvement Manager |

### KPI-CI-08: CIR Backlog Health
<!-- sources: ITIL 4 Continual Improvement §2.4.2.2, §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The age distribution and throughput of improvement initiatives in the CIR — measuring whether the backlog is being actively managed or accumulating stale items. A healthy CIR shows regular intake, steady throughput, and limited aging. High proportions of old, unactioned items indicate that the prioritization and resource allocation processes are not keeping pace with demand |
| **Formula** | Continual improvement productivity index: (N + C) / (O + C), where N = new items registered but not closed in period, O = total items open at period end, C = items processed and closed in period |
| **Target** | Ratio ≥ 1.0 (indicating throughput matches or exceeds intake); trending upward |
| **Frequency** | Quarterly |
| **Data Source** | CIR |
| **Owner** | Continual Improvement Manager |

---

## Advanced KPIs (T3)

### KPI-CI-09: Return on Improvement Investment
<!-- sources: ITIL 4 Continual Improvement §2.5 Table 2.2 PSF2, §2.4.2.5 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The return on investment and value on investment achieved from improvement initiatives during the reporting period. Measures whether the organization's improvement investments are generating proportionate value. Return on investment captures financial returns; value on investment captures broader business value including time to market, customer retention, risk reduction, and capability enhancement. Both should be considered, as ROI alone does not capture the real value of service improvement |
| **Formula** | (Value delivered by improvement initiatives / Total investment in improvement initiatives); or qualitative assessment of value on investment |
| **Target** | Positive and trending upward; value proportionate to investment |
| **Frequency** | Annually |
| **Data Source** | Improvement initiative outcomes, financial records, stakeholder assessments |
| **Owner** | Continual Improvement Manager / Senior Manager |

### KPI-CI-10: Negative Outcome Rate
<!-- sources: ITIL 4 Continual Improvement §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage and effect of improvement initiatives for which negative outcomes and realized risks outweighed the planned positive outcomes. Some improvement initiatives will not achieve intended results — this is expected in a safe-to-fail culture. However, a high rate of negative outcomes or significant negative effects indicates issues with assessment, planning, or risk management. Should be tracked alongside lessons learned to ensure the organization is learning from negative outcomes |
| **Formula** | (Initiatives with net negative outcomes / Total completed initiatives) × 100; plus qualitative assessment of negative effects |
| **Target** | ≤ 10%; trending downward; all negative outcomes reviewed for lessons |
| **Frequency** | Semi-annually |
| **Data Source** | CIR, improvement evaluation records |
| **Owner** | Continual Improvement Manager |

### KPI-CI-11: Improvement Culture Maturity
<!-- sources: ITIL 4 Continual Improvement §2.5 Table 2.2 PSF1, §2.4.1.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | A composite assessment of the degree to which a continual improvement culture has been adopted across the organization — including willingness to suggest improvements, risk tolerance, knowledge sharing practices, leadership modelling, and safe-to-fail environment. Measured through cultural assessment surveys, participation metrics, and qualitative evaluation. Provides a holistic view of whether the improvement practice is embedded as a genuine organizational norm rather than a mandated process |
| **Formula** | Composite score from cultural maturity assessment (defined rubric) |
| **Target** | Trending upward; target calibrated to organizational starting point |
| **Frequency** | Annually |
| **Data Source** | Cultural assessment surveys, participation metrics, qualitative evaluation |
| **Owner** | Continual Improvement Manager / Senior Manager |

### KPI-CI-12: Supplier Improvement Engagement
<!-- sources: ITIL 4 Continual Improvement §6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of key suppliers and partners actively engaged in continual improvement — submitting suggestions to the CIR, participating in joint improvement initiatives, or engaged in regular improvement discussions. Measures whether the organization has extended its improvement culture beyond its own boundaries into the supply chain |
| **Formula** | (Key suppliers actively engaged in CI / Total key suppliers) × 100 |
| **Target** | Trending upward; ≥ 50% of key suppliers engaged |
| **Frequency** | Annually |
| **Data Source** | CIR, supplier management records |
| **Owner** | Continual Improvement Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| CI-01 | Improvement Initiative Completion Rate | All | Quarterly |
| CI-02 | Improvement Success Rate | All | Quarterly |
| CI-03 | Improvement Opportunity Volume | All | Monthly |
| CI-04 | Improvement Initiative Timeliness | All | Quarterly |
| CI-05 | Improvement Approach Adoption | T2+ | Semi-annually |
| CI-06 | Stakeholder Satisfaction with Improvement | T2+ | Semi-annually |
| CI-07 | Lessons Learned Capture Rate | T2+ | Quarterly |
| CI-08 | CIR Backlog Health | T2+ | Quarterly |
| CI-09 | Return on Improvement Investment | T3 | Annually |
| CI-10 | Negative Outcome Rate | T3 | Semi-annually |
| CI-11 | Improvement Culture Maturity | T3 | Annually |
| CI-12 | Supplier Improvement Engagement | T3 | Annually |
