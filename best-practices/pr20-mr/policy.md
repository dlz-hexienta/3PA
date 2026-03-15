---
process_id: PR20
process_name: "Measurement & Reporting"
category: policy
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
  - "ITIL 4: Measurement & Reporting §2.1–§2.4"
  - "FitSM-2: §PR3 SRM"
  - "IT4IT: Cross-cutting"
last_updated: 2026-03-14
status: draft
---

# Measurement & Reporting — Best Practice Policy

## Policy Principles
<!-- sources: ITIL 4 Measurement & Reporting §2.1, §2.2, §2.4.1–§2.4.3, FitSM-2 §PR3 SRM Objective -->

### 1. Objective-Driven Measurement
<!-- sources: ITIL 4 Measurement & Reporting §2.4.1 -->
All measurements shall be linked to organizational objectives. Measurements have no intrinsic value — they only become valuable when applied in a management context. The organization shall not measure for the sake of measuring; every metric must serve at least one of four management purposes: influencing behaviour, justifying changes, validating decisions, or enabling intervention. The measurement and evaluation model — objectives, success factors, metrics, KPIs, aggregation — shall guide the design of all measurement systems.

### 2. Decision-Oriented Reporting
<!-- sources: ITIL 4 Measurement & Reporting §2.2.4, §2.4.3 -->
Reports and dashboards shall be designed to support decision-making, not merely to present information. Every report shall be designed to answer two questions: where are we compared to agreed targets, and what prevents us from achieving better results. Reports shall include data analysis — comparisons with targets, comparisons with past values, and correlations between relevant metrics — as well as recommendations for action where appropriate.

### 3. Data Quality Assurance
<!-- sources: ITIL 4 Measurement & Reporting §2.4.2 -->
The organization shall ensure that measurement data is of sufficient quality to support reliable decision-making. Data shall be intrinsically good (accurate and objective), contextually appropriate (complete, relevant, and timely), clearly represented (understandable and consistent), and accessible (available to designated consumers). Poor data leads to poor decisions — data quality shall be actively monitored and maintained.

### 4. Balanced Measurement
<!-- sources: ITIL 4 Measurement & Reporting §2.2.2, §2.2.3 -->
Measurement systems shall combine metrics of different types — effectiveness, efficiency, productivity, and conformance — to provide a multidimensional view of each managed object. The absence of any metric type may leave important characteristics unmeasured. KPI systems shall include both leading indicators (to predict and influence future outcomes) and lagging indicators (to report achievements and trends). KPIs should ideally be set for teams rather than individuals, to avoid driving undesirable behaviours.

### 5. Stakeholder-Appropriate Reporting
<!-- sources: ITIL 4 Measurement & Reporting §2.4.3, FitSM-2 §PR3 SRM -->
Reports shall be tailored to their intended audience. Each report shall have a clearly defined consumer, purpose, and scope. Operational reports shall provide frequent, fact-based monitoring data; analytical reports shall provide in-depth investigation and analysis for strategic and tactical decisions. Report format, frequency, and level of detail shall match the stakeholder's decision-making needs and context.

### 6. Standardization and Consistency
<!-- sources: ITIL 4 Measurement & Reporting §2.3, FitSM-2 §PR3 SRM -->
The organization shall apply a consistent measurement and reporting approach across all practices, services, and managed objects. Report specifications shall standardize report structure and content. Term definitions, calculation methods, and reporting formats shall be agreed and documented. Templates shall be used to ensure repeatable, comparable reporting across periods and across services.

### 7. Continual Optimization
<!-- sources: ITIL 4 Measurement & Reporting §2.3, §2.4.1 -->
The measurement and reporting approach shall be continually reviewed and optimized. Measurements and reports that no longer serve organizational objectives shall be retired. New measurements shall be introduced as objectives evolve. The cost of measurement and reporting shall be proportionate to the value of the decisions they support.

---

## Mandatory Requirements
<!-- sources: ITIL 4 Measurement & Reporting §2.4.1–§2.4.3, §3.2.1, §3.2.2, FitSM-2 §PR3 SRM -->

### Essential (All tiers)

| # | Requirement |
|---|-------------|
| 1 | Reporting requirements shall be identified from SLAs, customer agreements, internal stakeholder needs, and governance obligations — documenting who needs which reports, at what frequency, and for what purpose |
| 2 | Each report shall have a formal specification defining its unique identifier, purpose, audience, frequency, content, format, and delivery method |
| 3 | Report specifications shall be maintained as requirements change — new specifications created, existing ones updated, and obsolete ones terminated |
| 4 | Measurement data shall be gathered from configured sources with attention to accuracy and integrity, processed into information formatted for the target audience |
| 5 | Reports shall be produced and distributed according to their specifications and agreed schedules. Production and distribution shall be monitored, with follow-up actions initiated for inaccurate or late reporting |

### Intermediate (T2+)

| # | Requirement |
|---|-------------|
| 6 | Metrics and measurement methods shall be developed based on the purpose, objectives, and success factors of each managed object — combining effectiveness, efficiency, productivity, and conformance metrics |
| 7 | KPIs shall be defined by selecting key metrics and establishing target values, target trends, and threshold values. KPI systems shall be balanced and avoid overemphasizing any single dimension |
| 8 | Report templates and a reporting policy shall be established — covering targeted audiences, data structure requirements, term definitions, calculation methods, reporting schedules, access controls, and review meetings |
| 9 | Analytical reports shall be produced that go beyond factual reporting to identify trends, causes, bottlenecks, and improvement opportunities |

### Advanced (T3)

| # | Requirement |
|---|-------------|
| 10 | The measurement and evaluation system shall be periodically assessed for coverage of organizational objectives — identifying managed objects that lack adequate measurement and reports that are not being used as intended |
| 11 | KPI aggregation methods, weighting schemes, and scorecard designs shall be reviewed and refined to ensure composite scores accurately reflect the state of managed objects |
| 12 | The cost-effectiveness of the measurement and reporting approach shall be assessed — reducing unnecessary measurements and reports while strengthening critical ones |

---

## Related Policies
<!-- sources: ITIL 4 Measurement & Reporting §2.3 Table 2.1 -->

| Related Policy | Relationship |
|----------------|-------------|
| Service Level Management Policy (PR02) | SLAs define reporting requirements and service targets. Service quality reports are a key output of the measurement and reporting practice |
| Availability Management Policy (PR06) | Availability data feeds into service reports. The measurement and reporting practice provides methods and templates for availability reporting |
| Capacity & Performance Management Policy (PR08) | Performance and utilization data feeds into service reports. The measurement and reporting practice provides methods and templates for capacity reporting |
| Monitoring & Event Management Policy (PR14) | Monitoring tools are primary sources of measurement data. The measurement and reporting practice defines what data is needed and how it should be structured |
| Continual Improvement Policy (PR24) | Reports identify improvement opportunities. Improvement initiatives from report evaluation feed the continual improvement register |
| Relationship Management Policy (PR22) | Reports support customer relationship management. Relationship management helps clarify stakeholder reporting requirements |
| Information Security Management Policy (PR09) | Information security controls govern access to reports and data. Report accessibility is ensured through information security management |
| All Process Policies | Every practice produces reports and requires measurement. The measurement and reporting practice provides the cross-cutting framework that all practices use |
