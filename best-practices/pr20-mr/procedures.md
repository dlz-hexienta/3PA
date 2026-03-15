---
process_id: PR20
process_name: "Measurement & Reporting"
category: procedures
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
  - "ITIL 4: Measurement & Reporting §3.2.1, §3.2.2"
  - "FitSM-2: §PR3 SRM"
  - "IT4IT: Cross-cutting"
last_updated: 2026-03-14
status: draft
---

# Measurement & Reporting — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the core operational activities — identifying reporting requirements, specifying reports, gathering data, and producing reports. Intermediate procedures add structured measurement system design — developing metrics, forming KPI scorecards, designing templates and policy, and producing analytical reports. Advanced procedures cover evaluation and optimization of the measurement system itself. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All tiers)

### PROC-MR-01: Specify and Maintain Reports
<!-- sources: FitSM-2 §PR3 SRM (initial process setup, identify reporting requirements, maintain report specifications), ITIL 4 Measurement & Reporting §3.2.1 Table 3.2 (designing report templates) -->

**Trigger:** New service or SLA introduced with reporting requirements; new stakeholder reporting need identified; periodic review of report specifications; existing report specification requires update or termination

**Inputs:** SLAs and service level requirements, reporting requirements from customers and internal stakeholders, existing report specifications, governance and regulatory reporting obligations

**Outputs:** List of all agreed reports, report specifications (with unique ID, purpose, audience, frequency, content, format, delivery method), report templates

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify reporting requirements | Derive reporting requirements from SLAs, customer agreements, and governance obligations. Identify targets, events, and nonconformities to be reported to customers. Identify reports required by internal stakeholders to support management of the SMS. Determine who needs which reports, at what frequency, and for what decision-making purpose | Reporting Manager / Subject Matter Expert |
| 2 | Create or update report specifications | For each identified report, create a specification defining: unique name or identifier, purpose of the report, audience or addressee, reporting frequency, intended content outline, format, and method of delivery. Update existing specifications when requirements change. Terminate specifications for reports no longer needed | Reporting Manager |
| 3 | Define report templates | Define templates to standardize report structure and support effective, repeatable reporting. Templates should present data clearly and concisely, making it easy for stakeholders to see what needs to be done and take action. Align templates with the reporting policy where one exists | Reporting Manager / Analyst |
| 4 | Review and approve specifications | Review report specifications with the intended audiences to confirm that the proposed reports will meet their needs. Gain agreement on content, frequency, and format. Maintain the list of all agreed reports | Reporting Manager / Subject Matter Expert |

---

### PROC-MR-02: Produce and Distribute Reports
<!-- sources: ITIL 4 Measurement & Reporting §3.2.2 Tables 3.3, 3.4 (data gathering, reporting), FitSM-2 §PR3 SRM (produce and distribute reports) -->

**Trigger:** Scheduled reporting cycle (daily, weekly, monthly, quarterly); ad-hoc report request; event or threshold breach requiring immediate reporting

**Inputs:** Measurement and monitoring data, service management records, report specifications, report templates, reporting policy

**Outputs:** Operational reports and dashboards, data for SLA reporting, identified deviations for investigation

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Gather measurement data | Collect measurement data from configured sources — service management tools, monitoring tools, investigation and discovery systems, and manual or semi-manual procedures such as customer and user surveys. Ensure data accuracy and integrity. Ongoing communication about the importance of administrative tasks (updating logs and records) is crucial because it directly impacts data and KPI accuracy | Analyst / Analytics Tool Administrator |
| 2 | Process data | Transform raw data into information formatted for the target audience. This involves sorting, ordering (such as by time series), normalizing, mapping, labelling, grouping, and correlating. Use report-generating technologies where available. Format data to provide an end-to-end perspective on the overall performance of the service or process being reported | Analyst / Analytics Tool Administrator |
| 3 | Produce reports | Populate report templates with processed data. Calculate metrics and KPIs against agreed targets. Present current values alongside target values and historical comparisons. Highlight deviations, trends, and areas requiring attention. For dashboards, ensure data is current and displayed on a single screen with only the most relevant information | Analyst / Reporting Manager |
| 4 | Distribute and verify | Distribute reports through agreed channels according to the reporting policy and schedule. Verify that reports are produced and distributed according to specifications. Initiate follow-up actions in case of inaccurate reporting, late delivery, or distribution failures | Reporting Manager |

---

## Intermediate Procedures (T2+)

### PROC-MR-03: Design the Measurement and Reporting System
<!-- sources: ITIL 4 Measurement & Reporting §3.2.1 Tables 3.1, 3.2, §2.4.1 -->

**Trigger:** New managed object requiring a measurement system (new service, practice, or organizational function); existing measurement system identified as incomplete or misaligned with objectives; organizational objectives change requiring measurement system revision; periodic review of measurement effectiveness

**Inputs:** Purpose and objectives of the managed object, success factors, available measurement tools and capabilities, SLAs and contracts, existing performance data, reporting requirements

**Outputs:** Metrics and measurement methods, KPI scorecards with target values and thresholds, report templates, reporting policy

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Define objectives | Define and agree what the measurement and evaluation system will be used for. Objectives are typically based on the agreed purpose of the managed object — for practices, these are normally linked to effectiveness, conformance, efficiency, or productivity. Objectives should be specific, measurable, achievable, relevant, and time-bound | Subject Matter Expert / Reporting Manager |
| 2 | Identify success factors | Decompose objectives into success factors — the conditions or characteristics that must be achieved for the objective to be considered met. Success factors enable more granular and transparent measurement than objectives alone | Subject Matter Expert / Reporting Manager |
| 3 | Develop metrics and select measurement methods | Select metrics for the identified objectives and success factors. Ensure the measurement system combines effectiveness, efficiency, productivity, and conformance metrics for a multidimensional view. Select metrics considering the measurement tools available — technology capabilities can seriously limit what can be measured. Define measurement methods (automated calculation versus survey-based collection) | Subject Matter Expert / Analyst |
| 4 | Form KPI scorecards | Define KPIs by selecting the most important metrics and establishing target values, target trends (upward or downward), and threshold values for each. Ensure the resulting KPI system is balanced. Define normalization formulas to transform KPIs into comparable percentage ratings. Select an aggregation method (weighted average, multiplication, dynamic weights) to produce composite scores | Reporting Manager / Subject Matter Expert |
| 5 | Design report templates and reporting policy | Design report templates and dashboards that present data clearly. Establish a reporting policy covering: targeted audiences and tailored views, data structure requirements, agreed measurements, term definitions, calculation methods, reporting schedules, access controls, interface and usability requirements (sorting, filtering, drill-down), and review meetings scheduled to discuss reports | Reporting Manager / Analytics Tool Administrator |

---

### PROC-MR-04: Analyse Data and Produce Analytical Reports
<!-- sources: ITIL 4 Measurement & Reporting §3.2.2 Tables 3.3, 3.4 (data analysis and reporting, report evaluation) -->

**Trigger:** Scheduled analytical review cycle (quarterly, semi-annually); persistent negative trend detected in operational reports; management request for investigation; post-incident or post-change review requiring deep analysis

**Inputs:** Operational reports and dashboards, measurement data over extended periods, service management records, organizational objectives and targets, previous analytical reports

**Outputs:** Analytical reports with findings, improvement initiatives, recommendations for corrective and preventive actions

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Define the analysis scope and questions | Determine the scope of the analysis — which managed objects, time periods, and aspects will be investigated. Define the key questions the analysis should answer: are targets being met, are there clear trends, are we operating according to plan, are changes needed, are there underlying problems | Subject Matter Expert / Reporting Manager |
| 2 | Analyse data | Transform information into knowledge about the current situation. Go beyond automated processing — a common incorrect assumption is that monitoring and reporting tools perform the analysis. Analysis involves making judgements about what the data means, how it impacts the organization, and how it relates to goals and objectives. Identify trends, correlations, bottlenecks, causes, and patterns | Analyst / Subject Matter Expert |
| 3 | Produce the analytical report | Present findings in a format that is understandable, targeted, provides value, and informs decision-making. Include data analysis (comparisons, correlations, trend explanations), possible causes of the current state, highlighted risks, and suggested corrective and preventive actions. The report should emphasize areas where the recipient needs to act | Analyst / Reporting Manager |
| 4 | Evaluate and decide | Present the analytical report to the relevant decision-makers. The knowledge in the report, combined with previous experience, enables informed decision-making about optimizing, improving, and correcting services and processes. Log improvement proposals for assessment, prioritization, and approval through the continual improvement practice | Subject Matter Expert / Senior Manager |

---

## Advanced Procedures (T3)

### PROC-MR-05: Evaluate and Optimize the Measurement System
<!-- sources: ITIL 4 Measurement & Reporting §2.4.1, §2.4.2, §2.4.3 -->

**Trigger:** Periodic review of the measurement and reporting approach (annually or semi-annually); organizational strategy change; significant change in service portfolio; feedback indicating measurements are not supporting decisions; cost-reduction initiative targeting reporting overhead

**Inputs:** Current metrics, KPIs, and scorecards, current report specifications and reporting policy, stakeholder feedback on report usefulness, measurement costs, organizational objectives

**Outputs:** Updated metrics and KPI scorecards, updated report specifications and reporting policy, retired unnecessary measurements and reports, improvement initiatives

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Assess objective coverage | Evaluate whether the organization's measurements cover all key objectives. Identify objectives, success factors, or managed objects that lack adequate measurement. Identify measurements that are no longer linked to current objectives — these are candidates for retirement | Reporting Manager / Subject Matter Expert |
| 2 | Assess data quality | Evaluate the quality of measurement data across all four dimensions — intrinsic quality, contextual appropriateness, clarity of representation, and accessibility. Identify data sources that are unreliable, incomplete, or inconsistent. Define improvement actions for data quality issues | Reporting Manager / Analyst |
| 3 | Assess reporting effectiveness | Review whether reports are being used as intended — supporting decisions, not just consuming resources. Gather feedback from report consumers on usefulness, timeliness, and clarity. Identify reports that are produced but not used, or that fail to drive the intended decisions | Reporting Manager / Subject Matter Expert |
| 4 | Optimize KPI aggregation and scoring | Review KPI aggregation methods, weighting schemes, and scorecard designs. Evaluate whether composite scores accurately reflect the state of managed objects. Assess the balance between leading and lagging indicators. Refine normalization formulas and aggregation algorithms based on experience and changing priorities | Reporting Manager / Analyst |
| 5 | Update the measurement and reporting approach | Retire unnecessary measurements and reports. Introduce new measurements for uncovered objectives. Update report specifications, templates, and reporting policy. Communicate changes to stakeholders. Track the impact of changes on decision-making effectiveness over subsequent periods | Reporting Manager |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-MR-01 | Specify and Maintain Reports | All | New service/SLA; new reporting need; periodic review |
| PROC-MR-02 | Produce and Distribute Reports | All | Scheduled cycle; ad-hoc request; threshold breach |
| PROC-MR-03 | Design the Measurement and Reporting System | T2+ | New managed object; measurement gap; objectives change |
| PROC-MR-04 | Analyse Data and Produce Analytical Reports | T2+ | Scheduled review; negative trend; management request |
| PROC-MR-05 | Evaluate and Optimize the Measurement System | T3 | Periodic review; strategy change; cost-reduction initiative |
