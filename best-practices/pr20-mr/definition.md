---
process_id: PR20
process_name: "Measurement & Reporting"
category: definition
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
  - "ITIL 4: Measurement & Reporting §2–§6"
  - "FitSM-2: §PR3 SRM"
  - "IT4IT: Cross-cutting"
last_updated: 2026-03-14
status: draft
---

# Measurement & Reporting — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Measurement & Reporting §2.1, FitSM-2 §PR3 SRM Objective -->

Measurement and reporting supports good decision-making and continual improvement by decreasing the levels of uncertainty. This is achieved through the collection of relevant data on various managed objects and the valid assessment of this data in an appropriate context. Managed objects include products and services, practices and value chain activities, teams and individuals, suppliers and partners, and the organization as a whole. The practice ensures that reports on services and processes are specified, produced, and delivered to the right stakeholders at the right time. It establishes a coherent measurement and reporting approach across the organization — linking measurements to objectives, ensuring data quality, and designing reports that support decision-making rather than merely presenting information.

## Scope
<!-- sources: ITIL 4 Measurement & Reporting §2.3, FitSM-2 §PR3 SRM -->

This process covers:

- Defining a measurement and reporting approach for the organization
- Identifying reporting requirements from SLAs, customers, and internal stakeholders
- Specifying reports — defining purpose, audience, frequency, content, format, and delivery method
- Developing metrics and measurement methods linked to organizational objectives
- Forming KPI scorecards with target values, thresholds, and aggregation methods
- Designing report templates and establishing a reporting policy
- Gathering and processing measurement data from multiple sources
- Producing and distributing operational and analytical reports
- Evaluating reports to support decision-making and identify improvement opportunities
- Monitoring the production and distribution of reports against specifications
- Continually reviewing and optimizing measurements and reports across the organization

This process does not cover: communicating with stakeholders to clarify goals and reporting requirements (relationship management, service desk, supplier management), producing the actual content of practice-specific reports (each respective practice), measurement-based incentives planning and realization (workforce and talent management), or the ongoing management and implementation of improvements identified through reports (continual improvement). The measurement and reporting practice provides the framework, tools, and methods — each practice is responsible for producing its own reports using that framework.

## Key Concepts
<!-- sources: ITIL 4 Measurement & Reporting §2.2, FitSM-2 §PR3 SRM -->

### 1. Measurement
<!-- sources: ITIL 4 Measurement & Reporting §2.2.1 -->
A means of decreasing uncertainty based on one or more observations expressed in quantifiable units. Measurements have no intrinsic value — they only become valuable when applied in a management context. Measurements help with four management tasks: influencing behaviour by setting measurable targets, justifying changes through quantitative arguments, validating decisions by confirming outcomes, and intervening with corrective actions when metrics indicate problems. The most common measurement categories are performance (what is achieved), maturity (whether necessary capabilities exist), and compliance (whether requirements are met). Methods of measurement include calculations based on data from tracking and monitoring tools, and surveys.

### 2. Metric
<!-- sources: ITIL 4 Measurement & Reporting §2.2.2 -->
A measurement or calculation that is monitored or reported for management and improvement. Metrics always describe a managed object — such as a service, practice, configuration item, or service management activity. Different metrics describe different aspects: effectiveness (degree to which purpose is fulfilled), efficiency (how resources are utilized), productivity (amount of work performed and outputs produced), and conformance (compliance with requirements). A complete measurement system combines metrics of different types to build a multidimensional view.

### 3. Key Performance Indicator (KPI)
<!-- sources: ITIL 4 Measurement & Reporting §2.2.3 -->
An important metric used to evaluate the success in meeting an objective. A metric is only a KPI when it is crucial for assessing an object's state — differentiating key information from supplementary data. KPIs help assess state in terms of acceptable or unacceptable. To use metrics as KPIs, the organization must identify the key metrics, define target values and trends, and define tolerances (acceptable deviations from target). KPIs should ideally be set for teams rather than individuals, to avoid driving undesirable behaviours. Individual guidelines should exist within the team's objectives, and all targets should focus on enabling value for the organization.

### 4. Leading and Lagging Indicators
<!-- sources: ITIL 4 Measurement & Reporting §2.2.2.5 -->
Lagging indicators report what has already been achieved — they provide useful information to managers and customers but there is limited ability to influence them directly. Leading indicators help to predict what is likely to happen in the future — they are often difficult to measure but fairly easy to influence. A balanced measurement system includes both types: lagging indicators for accountability and trend analysis, leading indicators for proactive management and early intervention.

### 5. Operational Reports
<!-- sources: ITIL 4 Measurement & Reporting §2.2.4.1 -->
Reports created to monitor performance, identify deviations, and initiate corrective actions to support operations. Operational reports are fact-based, including calculations, comparisons, and correlations. If automated, they can be produced promptly and frequently. A dashboard is an operational report that displays only the most relevant data on a single screen and is accessible online. Dashboard data can be updated in real time, by schedule, or on demand.

### 6. Analytical Reports
<!-- sources: ITIL 4 Measurement & Reporting §2.2.4.2 -->
Reports that reveal hidden problems or bottlenecks, identify possible causes, and surface improvement opportunities. Unlike operational reports, analytical reports deal with data analysis, trends and their explanations, and deep investigations. They are usually produced by skilled analysts and created much less frequently than operational reports — sometimes supporting decisions for over a year. Analytical reports are typically paginated and may be subject to a formal approval process before use.

### 7. KPI Aggregation and Scorecards
<!-- sources: ITIL 4 Measurement & Reporting §2.4.1 -->
The process of normalizing and combining individual KPIs into composite scores to provide an overall assessment of a managed object. KPIs expressed in different units and with different target trends are transformed into percentage ratings using normalization formulas, then grouped into green (target achieved), yellow (between threshold and target), and red (below threshold) zones. Normalized KPIs can be aggregated using weighted arithmetic averages, multiplication, dynamic weights, or other methods. This produces performance scorecards that enable rapid assessment of overall service or practice health.

### 8. Data Quality
<!-- sources: ITIL 4 Measurement & Reporting §2.4.2 -->
High-quality measurement data has four characteristics: intrinsically good (accurate, objective, believable, reputable source), contextually appropriate (complete, relevant, timely, appropriate volume), clearly represented (understandable, consistent, interpretable), and accessible (available to designated consumers as agreed). The measurement and reporting practice is primarily focused on ensuring contextual and representational quality. Intrinsic quality is ensured by the practices that produce the data; accessibility is ensured by availability management and information security management.

### 9. Report Specification
<!-- sources: FitSM-2 §PR3 SRM -->
A formal description of a report that defines its unique name or identifier, purpose, audience or addressee, frequency, intended content, format, and method of delivery. Report specifications standardize reporting and enable repeatable, consistent report production. Specifications must be maintained as reporting requirements change — new specifications created, existing ones updated, and obsolete ones terminated.

### 10. Measurement and Evaluation Model
<!-- sources: ITIL 4 Measurement & Reporting §2.4.1 -->
A structured approach to building measurement systems that connects purpose, objectives, success factors, metrics, and KPIs in a logical chain. The model follows five steps: define objectives (based on managed object purpose), identify success factors (conditions for success), select metrics and measurement tools (considering available technology), form KPI scorecards (with targets, trends, and thresholds), and aggregate measurement data (into composite scores). This model ensures that measurements are driven by objectives rather than by what is easy to measure.

## Activities
<!-- sources: ITIL 4 Measurement & Reporting §3.2.1, §3.2.2, FitSM-2 §PR3 SRM -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Identify reporting requirements | Derive reporting requirements from SLAs, customer agreements, internal stakeholder needs, and governance obligations. Identify which services, processes, and managed objects require regular reporting. Determine who needs which reports, at what frequency, and for what purpose. Consider both customer-facing service reports and internal management reports |
| 2 | Specify and maintain reports | Create a report specification for each identified report — defining its unique identifier, purpose, audience, frequency, content outline, format, and delivery method. Define templates to standardize report structure and support repeatable production. Review and update specifications as requirements change; terminate specifications for reports no longer needed |
| 3 | Gather and process measurement data | Collect measurement data from configured sources — service management tools, monitoring tools, investigation and discovery systems, and manual or semi-manual procedures such as surveys. Ensure data accuracy and integrity. Process raw data into information formatted for the target audience — sorting, ordering, normalizing, mapping, labelling, grouping, and correlating |
| 4 | Produce and distribute reports | Generate reports according to specifications and schedules. Present data in the agreed format — whether as periodic reports, dashboards, or ad-hoc outputs. Distribute through agreed channels. Verify that reports are produced and distributed according to specifications; initiate follow-up actions in case of inaccurate or late reporting |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 5 | Develop metrics and measurement methods | Based on the purpose, objectives, and success factors of each managed object, develop metrics and select measurement methods. Ensure the measurement system combines effectiveness, efficiency, productivity, and conformance metrics for a multidimensional view. Select metrics considering available measurement tools and technology capabilities |
| 6 | Form KPI scorecards | Define KPIs by selecting the most important metrics and establishing target values, target trends, and threshold values for each. Ensure the resulting system of KPIs is balanced — covering the key properties of the managed object without overemphasizing any single dimension. Define normalization and aggregation methods for composite scoring |
| 7 | Design report templates and reporting policy | Design report templates and dashboards that present data clearly and concisely. Establish a reporting policy covering: targeted audiences and tailored views, data structure requirements, agreed measurements, term definitions, calculation methods, reporting schedules, access controls, interface and usability requirements, and review meetings |
| 8 | Analyse data and produce analytical reports | Transform information into knowledge about the current situation — how it affects the organization and how it relates to goals and objectives. Go beyond automated processing to ask key questions: are targets met, are there clear trends, are we operating according to plan, are changes needed, are there underlying problems. Present findings in reports that provide value and inform decision-making |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 9 | Evaluate and optimize the measurement system | Assess whether the organization's measurements are effectively driving decision-making and improvement. Evaluate whether the measurement and evaluation system covers all key objectives. Identify objectives, success factors, or managed objects that lack adequate measurement. Review whether reports are being used as intended — supporting decisions, not just consuming resources |
| 10 | Optimize KPI aggregation and reporting effectiveness | Review and refine KPI aggregation methods, weighting schemes, and scorecard designs. Evaluate whether composite scores accurately reflect the state of managed objects. Optimize the balance between lagging and leading indicators. Assess the cost-effectiveness of the measurement and reporting approach — reducing unnecessary measurements and reports while strengthening critical ones |

## Inputs
<!-- sources: ITIL 4 Measurement & Reporting §3.2.1, §3.2.2, §5.1, FitSM-2 §PR3 SRM -->

| # | Input | Source |
|---|-------|--------|
| 1 | Organizational objectives and strategy | Senior management |
| 2 | Service level agreements and service level requirements | Service level management |
| 3 | Infrastructure, application, and business transaction monitoring data | Monitoring & event management |
| 4 | Service management records (incidents, changes, problems, requests) | All operational practices |
| 5 | Customer and user feedback and survey results | Relationship management, service desk |
| 6 | External reporting requirements (regulatory, contractual) | Compliance, supplier management |
| 7 | Available measurement tools and capabilities | Infrastructure & platform management |
| 8 | Service availability data | Availability management |
| 9 | Performance and utilization data | Capacity & performance management |

## Outputs
<!-- sources: ITIL 4 Measurement & Reporting §3.2.1, §3.2.2, FitSM-2 §PR3 SRM -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Report specifications (list and detailed specifications of all agreed reports) | All practices, customers |
| 2 | Metrics and measurement methods | All practices |
| 3 | KPI scorecards with target values and thresholds | All practices, management |
| 4 | Report templates | All practices |
| 5 | Reporting policy | All practices |
| 6 | Operational reports and dashboards | Management, customers, service owners |
| 7 | Analytical reports | Management, continual improvement |
| 8 | Improvement initiatives | Continual improvement |

## Roles
<!-- sources: ITIL 4 Measurement & Reporting §4.1 Table 4.2, §4.2, FitSM-2 §PR3 SRM -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Reporting Manager / Quality Manager | Accountable for the measurement and reporting practice. Ensures that reports are specified, produced, and delivered. Designs report templates and reporting policy. Forms KPI scorecards. Oversees data quality. Drives practice improvement. In organizations with a dedicated quality management team, this function may reside there. In smaller organizations, responsibilities may be distributed among practice managers and service owners | All |
| Subject Matter Expert | Provides domain expertise for developing metrics and measurement methods within their area of responsibility — whether a practice, service, or function. Participates in defining objectives, success factors, and KPIs for managed objects. Evaluates reports and makes decisions based on measurement data. Includes practice managers, service managers, functional managers, and HR professionals | All |
| Analyst / Analytics Tool Administrator | Gathers and processes measurement data from multiple sources. Builds and maintains reports and dashboards using analytics and reporting tools. Performs data analysis to identify trends, bottlenecks, and improvement opportunities. Maintains reporting tool configurations and ensures data integration across sources | All |

## Key Artefacts
<!-- sources: ITIL 4 Measurement & Reporting §3.2, §5, FitSM-2 §PR3 SRM -->

| Artefact | Purpose |
|----------|------------|
| Report Specification | Defines each report's unique identifier, purpose, audience, frequency, content, format, and delivery method. Enables standardized, repeatable report production |
| KPI Scorecard | Documents the set of KPIs for a managed object — including metrics, target values, target trends, threshold values, normalization formulas, and aggregation methods |
| Reporting Policy | Defines the organization's reporting approach — audiences, data structures, calculation methods, reporting schedules, access controls, review meetings, and usability requirements |
| Report Template | Standardized template for presenting measurement data — designed for specific stakeholder groups with appropriate level of detail and visualization |
| Operational Report / Dashboard | Regular output presenting current performance data against targets — fact-based, frequently updated, supporting operational decision-making |
| Analytical Report | In-depth investigation output revealing hidden problems, trends, causes, and improvement opportunities — produced less frequently, supporting strategic and tactical decisions |

## Process Interfaces
<!-- sources: ITIL 4 Measurement & Reporting §2.3 Table 2.1, §3, FitSM-2 §PR3 SRM Key Interfaces -->

| Interface | Relationship |
|-----------|-------------|
| Service Level Management (PR02) | SLAs define reporting requirements and service targets. Evaluation of SLAs, OLAs, and underpinning agreements provides data for reports. Service quality reports are a key output of the measurement and reporting practice |
| Availability Management (PR06) | Service availability data feeds into service quality reports. The measurement and reporting practice provides report templates and methods for availability reporting |
| Capacity & Performance Management (PR08) | Performance and utilization data feeds into service quality reports. The measurement and reporting practice provides report templates and methods for capacity and performance reporting |
| Incident Management (PR11) | Incident records and statistics provide data for operational and analytical reports. Incident metrics are key inputs to service quality reporting |
| Service Request Management (PR12) | Service request data contributes to operational reports on service delivery and throughput |
| Problem Management (PR13) | Problem records provide data for analytical reports. Problem metrics contribute to service quality and improvement reporting |
| Change Management (PR15) | Change records provide data for reports on change success, timeliness, and throughput. Change metrics contribute to practice effectiveness reporting |
| Monitoring & Event Management (PR14) | Monitoring tools are primary sources of measurement data — infrastructure, application, and business transaction metrics feed the measurement and reporting practice |
| Continual Improvement (PR24) | Reports identify improvement opportunities. Improvement initiatives generated from report evaluation feed the continual improvement register |
| Relationship Management (PR22) | Reports support customer relationship management and customer satisfaction assessment. Relationship management helps clarify stakeholder reporting requirements |
| Risk Management (PR21) | Risk-related metrics and reports support risk assessment and treatment. Risk reports follow the measurement and reporting framework |
| Service Portfolio Management (PR01) | Portfolio-level reporting on service performance, demand, and investment supports portfolio management decisions |
| Supplier Management (PR23) | Supplier performance reports follow the measurement and reporting framework. Third-party reporting and analytics services may enhance the organization's measurement capabilities |
| Service Configuration Management (PR17) | Configuration data from the CMDB supports analysis and reporting by providing context about service components and their relationships |
| All practices | Every practice produces reports and requires measurement. The measurement and reporting practice provides the framework, tools, templates, and methods that all practices use |
