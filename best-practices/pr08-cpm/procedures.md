---
process_id: PR08
process_name: "Capacity & Performance Management"
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
  - "ITIL 4: Capacity & Performance Management §3.2.1, §3.2.2"
  - "FitSM-2: §PR5 CAPM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Capacity & Performance Management — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the core operational activities — establishing capacity and performance control for services (requirements, monitoring, reporting) and ongoing capacity and performance monitoring and reporting. Intermediate procedures add structured performance analysis and proactive capacity planning with risk treatment. Advanced procedures cover control optimization and capacity demand modelling. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All tiers)

### PROC-CPM-01: Establish Service Capacity and Performance Control
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.1 Tables 3.1, 3.2, FitSM-2 §PR5 CAPM (initial process setup, identify requirements) -->

**Trigger:** New service being designed or introduced; new or changed SLA with performance targets; existing service changing capacity or performance requirements; periodic review identifying gaps in capacity and performance control

**Inputs:** Customer requirements and business needs, service level requirements and SLA drafts, business activity patterns and transaction volumes, service component specifications and manufacturer requirements, service models and configuration information, existing service and component performance data

**Outputs:** Agreed service capacity and performance requirements, capacity and performance monitoring requirements and configuration, capacity and performance report templates, automated scaling and load balancing controls (where applicable)

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify service capacity and performance requirements | Derive performance and capacity requirements from customer needs, SLAs, and business activity patterns. Identify the critical service actions and vital business functions that define performance priorities. Determine transaction volumes, throughput requirements, and growth forecasts. Compare requirements to the technical capacity characteristics of service components — computing power, storage, network performance, and end-user device capabilities. Propose the optimal balance of performance needs, component architecture, and sourcing models. Document requirements in a form that enables monitoring and reporting | Capacity & Performance Manager / Service Owner |
| 2 | Agree service capacity and performance requirements | Analyse whether the identified requirements are achievable and affordable given available resources, technology, and supplier capabilities. Determine estimated costs for different capacity and performance options — the cost of the service can vary considerably depending on the architecture options chosen. The capacity and performance management practice supports SLM with service component expertise during SLA negotiations, helping to balance the cost-benefit ratio of different performance levels. Record agreed targets | Service Owner / Capacity & Performance Manager |
| 3 | Determine capacity and performance monitoring approach | Define how service performance and capacity utilization will be monitored and recorded. Select appropriate monitoring methods based on the service type, scale, and available tools. Define thresholds and alerts for performance degradation and capacity exhaustion. In cloud environments, design automated capacity adjustment triggers that extend or reduce capacity based on demand. Make performance metrics available to other practices | Capacity & Performance Manager / Technical Specialist |
| 4 | Design capacity and performance metrics and reports | Design tools and reports to measure and present service performance from the consumer perspective, ensuring that technical indicators support rather than replace the business-level view. At the essential tier, this may be limited to basic performance measures and capacity utilization. Ensure the metrics align with the agreed performance criteria | Capacity & Performance Manager / Service Owner |

---

### PROC-CPM-02: Monitor and Report Service Capacity and Performance
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.2 Tables 3.3, 3.4 (reporting activity), FitSM-2 §PR5 CAPM (evaluate service performance) -->

**Trigger:** Scheduled monitoring and reporting cycle (weekly, monthly, quarterly); ad-hoc request from management, customers, or service owners; performance threshold breach detected

**Inputs:** Monitoring data (infrastructure, application, real user), incident records, agreed service capacity and performance requirements, capacity and performance report templates

**Outputs:** Service capacity and performance reports and dashboards, performance data for SLA reporting, identified deviations for investigation

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Collect capacity and performance data | Gather capacity and performance data from the configured monitoring sources for the reporting period. Sources may include infrastructure monitoring tools, application performance monitoring, real user monitoring, business transaction monitoring, and incident records. Ensure data covers all services with agreed performance targets | Technical Specialist |
| 2 | Validate data against performance criteria | Validate the collected data against the agreed performance criteria for each service. Apply the agreed criteria — acceptable delays, degradation thresholds, user impact scope — to determine which events count as performance degradation. Reconcile data from multiple sources where applicable. Incident records may be sources of disruption data but it is often difficult to obtain reliable performance and capacity data from user-reported incidents alone | Capacity & Performance Manager / Technical Specialist |
| 3 | Produce the capacity and performance report | Populate the report template with validated data. Calculate performance metrics for each service against agreed targets. Report on capacity utilization against thresholds. Focus on the consumer experience of service productivity and responsiveness — technical component reporting supports the findings but should not be the sole focus. Highlight services that have not met their targets and any significant trends | Capacity & Performance Manager |
| 4 | Distribute the report | Distribute the capacity and performance report through agreed channels. Service performance reporting is usually part of overall service quality reporting through the service level management practice. Provide data to SLM for SLA achievement reporting. Flag any services that have breached performance targets for investigation | Capacity & Performance Manager / Service Owner |

---

## Intermediate Procedures (T2+)

### PROC-CPM-03: Analyse and Improve Service Capacity and Performance
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.2 Tables 3.3, 3.4 (analysis and planning activities), FitSM-2 §PR5 CAPM (maintain and implement plans, evaluate) -->

**Trigger:** Scheduled review cycle (monthly, quarterly); performance target missed or trending toward breach; trend detected in capacity or performance data; new risk identified; new service design or proposed architecture requiring review

**Inputs:** Monitoring data, incident records, capacity and performance reports, service models and configuration information, agreed requirements, risk register, change schedule, performance-related incident and problem records, new service designs and proposed architectures

**Outputs:** Problem records, identified capacity and performance risks, capacity plans, new and updated controls, requests for change, improvement initiatives, service design and architecture recommendations, IT budget planning updates

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Analyse capacity and performance data | Review capacity and performance data and incident records to confirm achievement of requirements. All deviations from agreed levels must be investigated. Perform analysis at two levels: (1) service component and infrastructure level — identifying component capacity constraints, bottlenecks, and reliability issues; (2) service level — assessing overall service performance and its impact on customers. Perform trend analysis on business activity patterns to detect patterns that signal current service architecture may need to change. Cloud orchestration and load balancing toolsets allow automated adjustment but trend analysis may reveal that architectural changes are needed | Capacity & Performance Manager / Technical Specialist |
| 2 | Identify deviations, risks, and improvement opportunities | Based on the analysis, identify: services not meeting performance targets, trends indicating future target breaches, components approaching capacity limits, single points of capacity constraint, and opportunities for improvement. Log problems or risks as appropriate. Consider inputs from related practices — availability management, service continuity management, and risk management | Capacity & Performance Manager |
| 3 | Assess capacity and performance risks and design controls | Assess identified risks across all four dimensions of service management. Design countermeasures — which may include scaling adjustments, load balancing changes, application optimization, middleware reconfiguration, improved monitoring, or architectural redesign. More preventive measures should be adopted for services with earlier and higher business impacts; for services where impacts develop more slowly, emphasis may be placed on detective and responsive measures | Capacity & Performance Manager / Technical Specialist |
| 4 | Produce the capacity plan | Document current capacity and performance levels, business activity patterns and demand forecasts, anticipated changes to requirements, key service components and their capacity characteristics, and recommended controls with implementation timelines and costs. The plan may cover individual services, service groups, or the entire infrastructure. Include short-term, medium-term, and long-term perspectives | Capacity & Performance Manager |
| 5 | Initiate changes and improvements | Submit requests for change to implement recommended capacity and performance controls. Register improvement initiatives in the continual improvement register. Coordinate with service design and infrastructure management for implementation. Track progress against the capacity plan. Provide service design and architecture review recommendations where designs need to change to accommodate demand | Capacity & Performance Manager |

---

## Advanced Procedures (T3)

### PROC-CPM-04: Optimize Capacity and Performance Controls
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.3, §3.2.2 Table 3.4 -->

**Trigger:** Periodic review of capacity and performance investments (annually or semi-annually); significant capacity investment decision; post-incident review revealing control gaps; strategic planning cycle

**Inputs:** Current capacity and performance controls and their costs, performance data and incident history, risk register, loss event data, capacity plans, service specifications

**Outputs:** Updated capacity plans, recommendations for control changes, cost-benefit analysis reports, improvement initiatives

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Inventory existing capacity and performance controls | Compile an inventory of current capacity and performance controls — including automated scaling configurations, load balancing arrangements, monitoring setups, capacity reservation arrangements, and process controls. Document the cost of each control (implementation and ongoing operation) | Capacity & Performance Manager / Technical Specialist |
| 2 | Assess control effectiveness | For each control, assess whether it is achieving its intended risk reduction by comparing actual capacity and performance levels in areas covered by controls against the expected performance without those controls. Evaluate whether controls are preventing the capacity and performance risks they were designed to address | Capacity & Performance Manager |
| 3 | Assess control efficiency | For each control, compare its cost against its benefits. Benefits are calculated by estimating the reduction in incident likelihood multiplied by the severity of impact. Consider all forms of loss: productivity reduction, response costs, replacement costs, SLA fines, competitive advantage, and reputation. Identify controls that are cost-ineffective or could be replaced by more efficient alternatives. Evaluate whether linear scaling costs have exceeded the point where architectural changes would be more prudent | Capacity & Performance Manager |
| 4 | Recommend optimizations | Based on the effectiveness and efficiency assessments, recommend changes to the portfolio of capacity and performance controls — controls to add, strengthen, replace, or retire. Suggest alternative architectural arrangements where they would improve performance at lower cost. Document recommendations with supporting cost-benefit analysis | Capacity & Performance Manager |
| 5 | Update capacity plans | Update capacity plans to reflect recommended optimizations. Submit requests for change for approved control changes. Track the impact of changes on capacity and performance metrics over subsequent periods | Capacity & Performance Manager |

---

### PROC-CPM-05: Model and Forecast Capacity Demand
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.1, §2.4.3, §3.2.1 Table 3.2, §3.2.2 Table 3.4 -->

**Trigger:** Long-term planning cycle; significant demand growth anticipated; new market or business expansion; major service or architectural decision; IT budget planning cycle

**Inputs:** Business activity patterns and demand forecasts, service models and configuration information, current capacity and performance data, architectural options and scaling strategies, financial constraints and investment parameters

**Outputs:** Capacity demand models, long-term capacity forecasts, architecture recommendations, IT budget planning inputs, service design recommendations

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Analyse business activity patterns and demand forecasts | Gather and analyse business demand forecasts — seasonal variations, growth trends, campaign-driven spikes, cyclical workload patterns, and planned business changes. Identify the demand drivers that translate into capacity requirements for service components. Differentiate between short-term demand spikes (which may be handled through automated scaling) and sustained growth (which requires architectural planning) | Capacity & Performance Manager / Technical Specialist |
| 2 | Model resource requirements for demand scenarios | Develop capacity models that relate business demand forecasts to resource requirements across all service components — computing power, storage, network bandwidth, and staffing. Model how different demand scenarios translate into infrastructure, application, and third-party resource needs. Consider the interaction between demand on different components | Capacity & Performance Manager / Technical Specialist |
| 3 | Evaluate architectural options and scaling strategies | Model the performance impact of different architectural options and scaling strategies. Evaluate when continued linear scaling ceases to be cost-effective and alternative architectures become necessary — for example, altering network design, middleware configurations, or application architectures to accommodate changed demand patterns. Compare the total cost of ownership for each option | Capacity & Performance Manager / Technical Specialist |
| 4 | Produce long-term capacity forecasts | Produce capacity forecasts covering medium-term and long-term horizons that translate business growth projections into resource and investment requirements. Document assumptions, confidence levels, and key variables that could alter the forecast. Present forecasts in terms meaningful to both technical and business stakeholders | Capacity & Performance Manager |
| 5 | Provide input to IT budget planning | Translate capacity forecasts and architectural recommendations into investment requirements for IT budget planning. Present the cost implications of different capacity strategies, including the cost of under-provisioning risks. Coordinate with financial management to align capacity investment with organizational financial planning cycles | Capacity & Performance Manager |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-CPM-01 | Establish Service Capacity and Performance Control | All | New service; new/changed SLA; requirements change |
| PROC-CPM-02 | Monitor and Report Service Capacity and Performance | All | Scheduled cycle; ad-hoc request; threshold breach |
| PROC-CPM-03 | Analyse and Improve Service Capacity and Performance | T2+ | Scheduled review; target missed; trend detected; new risk |
| PROC-CPM-04 | Optimize Capacity and Performance Controls | T3 | Periodic review; investment decision; strategic planning |
| PROC-CPM-05 | Model and Forecast Capacity Demand | T3 | Long-term planning; demand growth; budget planning |
