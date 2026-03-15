---
process_id: PR06
process_name: "Availability Management"
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
  - "ITIL 4: Availability Management §3.2.1, §3.2.2"
  - "FitSM-2: §PR4 SACM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Availability Management — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the core operational activities — establishing availability control for services (requirements, monitoring, reporting) and ongoing availability monitoring and reporting. Intermediate procedures add structured availability analysis and proactive availability planning with risk treatment. Advanced procedures cover control optimization and service health model development. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All tiers)

### PROC-AM-01: Establish Service Availability Control
<!-- sources: ITIL 4 Availability Management §3.2.1 Tables 3.1, 3.2, FitSM-2 §PR4 SACM (initial process setup, identify requirements) -->

**Trigger:** New service being designed or introduced; new or changed SLA with availability targets; existing service changing availability requirements; periodic review identifying gaps in availability control

**Inputs:** Customer requirements and business needs, service level requirements and SLA drafts, service models and configuration information, information about available resources and monitoring tools

**Outputs:** Agreed service availability requirements, availability monitoring requirements and configuration, availability report templates

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify service availability requirements | Derive availability requirements from customer needs, SLAs, and business impact analysis. Identify the vital business functions supported by the service. Work with the service level management practice to clarify what availability means for this service — considering the criticality of supported business functions, the number and type of users, and the service delivery schedule. Document requirements in a form that enables monitoring and reporting | Availability Manager / Service Owner |
| 2 | Agree service availability requirements | Analyse whether the identified requirements are achievable and affordable given available resources, technology, and supplier capabilities. Determine estimated costs and timelines for fulfilment. This analysis should include agreements with suppliers and partners to ensure they will support the required service levels. Negotiate with customers to balance availability levels with cost. Record agreed targets | Service Owner / Availability Manager |
| 3 | Determine availability monitoring approach | Define how service outages will be tracked and recorded. Select the appropriate monitoring method based on the service type, scale, and available tools — from incident-record-based tracking for small-scale providers to infrastructure monitoring or real user monitoring for larger organizations. Define which monitoring data sources will be used and how they will be translated into service availability information | Availability Manager / Technical Specialist |
| 4 | Design availability metrics and reports | Select availability metrics that reflect the business impact of service disruptions. At the essential tier, this may be limited to availability percentage and number of disruptions. Design a report or dashboard template to present the results to stakeholders. Ensure the metrics align with the agreed availability criteria | Availability Manager / Service Owner |

---

### PROC-AM-02: Monitor and Report Service Availability
<!-- sources: ITIL 4 Availability Management §3.2.2 Tables 3.3, 3.4 (reporting activity), FitSM-2 §PR4 SACM (monitor service availability) -->

**Trigger:** Scheduled monitoring and reporting cycle (weekly, monthly, quarterly); ad-hoc request from management, customers, or service owners; availability target breach detected

**Inputs:** Monitoring data (infrastructure, application, real user), incident records, agreed service availability requirements, availability report templates

**Outputs:** Service availability reports and dashboards, availability data for SLA reporting, identified deviations for investigation

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Collect availability data | Gather availability data from the configured monitoring sources for the reporting period. Sources may include incident records with outage timestamps, infrastructure monitoring tools, or business transaction monitoring. Ensure data covers all services with agreed availability targets | Technical Specialist |
| 2 | Validate data against availability criteria | Validate the collected data against the agreed availability criteria for each service. Not all incidents are availability incidents — apply the agreed criteria (underperformance thresholds, user impact scope, service schedule) to determine which events count as unavailability. Reconcile data from multiple sources where applicable | Availability Manager / Technical Specialist |
| 3 | Produce the availability report | Populate the availability report template with validated data. Calculate availability metrics for each service against agreed targets. Highlight services that have not met their targets and any significant trends. For essential tier, the report may be simple; at higher tiers, it includes trend analysis and recommendations | Availability Manager |
| 4 | Distribute the report | Distribute the availability report through agreed channels. Service availability reporting is usually part of overall service quality reporting through the service level management practice. Provide data to SLM for SLA achievement reporting. Flag any services that have breached availability targets for investigation | Availability Manager / Service Owner |

---

## Intermediate Procedures (T2+)

### PROC-AM-03: Analyse and Improve Service Availability
<!-- sources: ITIL 4 Availability Management §3.2.2 Tables 3.3, 3.4 (analysis and planning activities), FitSM-2 §PR4 SACM (maintain and implement plans, evaluate) -->

**Trigger:** Scheduled review cycle (monthly, quarterly); availability target missed or trending toward breach; trend detected in availability data; new risk identified; input from service continuity BIA or risk assessment

**Inputs:** Monitoring data, incident records, service availability reports, service models and configuration information, agreed availability requirements, risk register, service specifications

**Outputs:** Problem records, identified availability risks, availability management plans, new and updated availability controls, requests for change, improvement initiatives

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Analyse availability data | Review availability data and incident records to confirm achievement of requirements. All deviations from agreed levels must be investigated. Perform analysis at two levels: (1) service component and infrastructure level — identifying component reliability issues, single points of failure, and infrastructure weaknesses; (2) service level — assessing overall service availability performance and its impact on customers. Perform trend analysis to detect patterns and flaws that have not yet caused incidents | Availability Manager / Technical Specialist |
| 2 | Identify deviations, risks, and improvement opportunities | Based on the analysis, identify: services not meeting availability targets, trends indicating future target breaches, single points of failure, unreliable components, and opportunities for improvement. Log problems or risks as appropriate. Consider inputs from service continuity management (BIAs, risk assessments) and from capacity and performance management | Availability Manager |
| 3 | Assess availability risks and design controls | Assess identified risks across all four dimensions of service management. Design countermeasures — which may include fault-tolerant technology, duplexing, improved component reliability, resilient network design, improved testing, improved incident management processes, or improved supplier agreements. More preventive measures should be adopted for services with earlier and higher business impacts; for services where impacts develop more slowly, emphasis may be placed on recovery measures | Availability Manager / Technical Specialist |
| 4 | Produce the availability management plan | Document current availability levels, key service components, anticipated changes to customer requirements, availability impacts of new requirements, and recommended controls with implementation timelines. The plan may cover a single service or a group of services | Availability Manager |
| 5 | Initiate changes and improvements | Submit requests for change to implement the recommended availability controls. Register improvement initiatives in the continual improvement register. Coordinate with service design and infrastructure management for implementation. Track progress against the availability management plan | Availability Manager |

---

## Advanced Procedures (T3)

### PROC-AM-04: Optimize Availability Controls
<!-- sources: ITIL 4 Availability Management §2.4.3 (effectiveness, efficiency, FAIR loss categories) -->

**Trigger:** Periodic review of availability investments (annually or semi-annually); significant availability investment decision; post-incident review revealing control gaps; strategic planning cycle

**Inputs:** Current availability controls and their costs, availability data and incident history, risk register, loss event data, availability management plans, service specifications

**Outputs:** Updated availability management plans, recommendations for control changes, cost-benefit analysis reports, improvement initiatives

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Inventory existing availability controls | Compile an inventory of current availability controls — including fault-tolerant technologies, redundancy arrangements, monitoring configurations, and process controls. Document the cost of each control (implementation and ongoing operation) | Availability Manager / Technical Specialist |
| 2 | Assess control effectiveness | For each control, assess its effectiveness by comparing the risk reduction achieved against the expected losses due to incidents if the control were not in place. Consider how impacts change over time — losses due to outages often grow exponentially. Evaluate whether controls are achieving their intended risk reduction | Availability Manager |
| 3 | Assess control efficiency | For each control, compare its cost against its benefits. Benefits are calculated by estimating the reduction in incident likelihood multiplied by the severity of impact. Consider all forms of loss: productivity reduction, response costs, replacement costs, SLA fines and regulatory judgments, competitive advantage, and reputation. Identify controls that are cost-ineffective or that could be replaced by more efficient alternatives | Availability Manager |
| 4 | Recommend optimizations | Based on the effectiveness and efficiency assessments, recommend changes to the portfolio of availability controls — controls to add, strengthen, replace, or retire. The goal is to achieve maximum availability with available resources. Document recommendations with supporting cost-benefit analysis | Availability Manager |
| 5 | Update availability management plans | Update availability management plans to reflect recommended optimizations. Submit requests for change for approved control changes. Track the impact of changes on availability metrics over subsequent periods | Availability Manager |

---

### PROC-AM-05: Develop and Maintain Service Health Models
<!-- sources: ITIL 4 Availability Management §2.2.5 Table 2.1 (service health model), §2.4.2 -->

**Trigger:** New critical service requiring accurate availability measurement; existing monitoring unable to translate infrastructure data into meaningful service availability information; improvement initiative from availability analysis

**Inputs:** Service models and configuration information (CMDB), service architecture documentation, infrastructure monitoring data, availability criteria for the service, incident history

**Outputs:** Service health model, updated monitoring configuration, improved service-level availability measurement

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Analyse service architecture | Map the service architecture including all components, dependencies, and redundancy arrangements. Identify which components are critical to the vital business functions of the service and which have redundancy or failover capability | Availability Manager / Technical Specialist |
| 2 | Map component-to-service impact relationships | Define how the underperformance or outage of each component impacts other components and the service as a whole. Determine which component failures cause service unavailability and which are absorbed by redundancy or failover. Consider both complete outages and partial underperformance | Availability Manager / Technical Specialist |
| 3 | Define impact rules and thresholds | For each component and dependency, define the rules that determine the service availability impact — including severity thresholds, user impact scope, and cascading failure scenarios. Encode these rules in a form that can be used by monitoring and reporting tools | Availability Manager / Technical Specialist |
| 4 | Validate the model | Test the service health model against historical incidents to verify that it accurately predicts service-level availability from component data. Adjust the model based on validation results. Confirm the model with service owners | Availability Manager |
| 5 | Maintain the model | Review and update the service health model when the service architecture changes — new components added, dependencies changed, or redundancy arrangements modified. IT infrastructure changes rapidly, so maintenance is an ongoing requirement | Availability Manager / Technical Specialist |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-AM-01 | Establish Service Availability Control | All | New service; new/changed SLA; requirements change |
| PROC-AM-02 | Monitor and Report Service Availability | All | Scheduled cycle; ad-hoc request; target breach |
| PROC-AM-03 | Analyse and Improve Service Availability | T2+ | Scheduled review; target missed; trend detected; new risk |
| PROC-AM-04 | Optimize Availability Controls | T3 | Periodic review; investment decision; strategic planning |
| PROC-AM-05 | Develop and Maintain Service Health Models | T3 | New critical service; monitoring gap; improvement initiative |
