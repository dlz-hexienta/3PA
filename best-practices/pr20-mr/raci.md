---
process_id: PR20
process_name: "Measurement & Reporting"
category: raci
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
  - "ITIL 4: Measurement & Reporting §4.1 Table 4.2, §4.2"
  - "FitSM-2: §PR3 SRM"
  - "IT4IT: Cross-cutting"
last_updated: 2026-03-14
status: draft
---

# Measurement & Reporting — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. The reporting manager is accountable for the measurement and reporting practice. In smaller organizations, measurement and reporting responsibilities may be distributed among practice managers and service owners, with analysts providing data gathering and tool expertise.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| RM | Reporting Manager / Quality Manager | All |
| SME | Subject Matter Expert | All |
| AN | Analyst / Analytics Tool Administrator | All |

## Essential Activities (All tiers)

### Specify and Maintain Reports
<!-- sources: ITIL 4 Measurement & Reporting §3.2.1 Table 3.2, FitSM-2 §PR3 SRM -->

| Activity | RM | SME | AN |
|----------|:--:|:---:|:--:|
| Identify reporting requirements | A/R | R | C |
| Create or update report specifications | A/R | C | C |
| Define report templates | A/R | C | R |
| Review and approve specifications | A | R | I |

### Produce and Distribute Reports
<!-- sources: ITIL 4 Measurement & Reporting §3.2.2 Table 3.4, FitSM-2 §PR3 SRM -->

| Activity | RM | SME | AN |
|----------|:--:|:---:|:--:|
| Gather measurement data | A | I | R |
| Process data | A | C | R |
| Produce reports | A/R | C | R |
| Distribute and verify | A/R | I | I |

## Intermediate Activities (T2+)

### Design the Measurement and Reporting System
<!-- sources: ITIL 4 Measurement & Reporting §3.2.1 Tables 3.1, 3.2, §4.1 Table 4.2 -->

| Activity | RM | SME | AN |
|----------|:--:|:---:|:--:|
| Define objectives | A | R | I |
| Identify success factors | A | R | C |
| Develop metrics and select measurement methods | A/R | R | R |
| Form KPI scorecards | A/R | C | C |
| Design report templates and reporting policy | A/R | C | R |

### Analyse Data and Produce Analytical Reports
<!-- sources: ITIL 4 Measurement & Reporting §3.2.2 Table 3.4, §4.1 Table 4.2 -->

| Activity | RM | SME | AN |
|----------|:--:|:---:|:--:|
| Define the analysis scope and questions | A | R | C |
| Analyse data | A | C | R |
| Produce the analytical report | A/R | C | R |
| Evaluate and decide | I | A | I |

## Advanced Activities (T3)

### Evaluate and Optimize the Measurement System
<!-- sources: ITIL 4 Measurement & Reporting §2.4.1, §2.4.2, §2.4.3 -->

| Activity | RM | SME | AN |
|----------|:--:|:---:|:--:|
| Assess objective coverage | A/R | R | C |
| Assess data quality | A/R | C | R |
| Assess reporting effectiveness | A/R | R | C |
| Optimize KPI aggregation and scoring | A/R | C | R |
| Update the measurement and reporting approach | A/R | I | I |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The reporting manager is accountable for all measurement and reporting practice activities — from specifying reports through system design, report production, analysis, and optimization. The exception is "Evaluate and decide" within analytical reporting, where accountability shifts to the senior manager or subject matter expert who owns the decision being supported.
2. **Role Combining:** The measurement and reporting practice underpins everything the organization does, making it effectively everyone's responsibility. In organizations with a dedicated quality management team, the reporting manager function typically resides there. In smaller organizations, practice managers measure and assess their own practices, while service managers provide service quality reports — the reporting manager role ensures coordination and consistency across these distributed activities.
3. **Reporting Manager / Quality Manager:** Accountable for the measurement and reporting practice. Ensures that reports are specified, produced, and delivered. Designs report templates and reporting policy. Forms KPI scorecards. Oversees data quality. Drives measurement system optimization. Requires understanding of data-structuring and presentation techniques, the decision-making processes the reports support, and visual design skills for effective reporting.
4. **Subject Matter Expert:** Provides domain expertise for developing metrics and measurement methods within their area of responsibility. Understands the purpose, objectives, and success factors of the managed objects being measured. Participates in defining objectives, identifying success factors, and selecting metrics. Evaluates reports and makes decisions based on measurement data. Includes practice managers, service managers, functional managers, and HR professionals.
5. **Analyst / Analytics Tool Administrator:** Gathers and processes measurement data from multiple sources. Builds and maintains reports and dashboards using analytics and reporting tools. Performs data analysis to identify trends, bottlenecks, and improvement opportunities. Maintains reporting tool configurations and ensures data integration across sources. Requires strong analytical skills, experience with analytics tools and spreadsheets, and understanding of data manipulation techniques.
6. **Senior Managers:** Not listed as a separate RACI role but participate in report evaluation and decision-making — especially for analytical reports that support strategic and tactical decisions. Senior managers are the primary consumers of aggregated KPI scorecards and the decision-makers who translate measurement insights into organizational action.
