---
process_id: PR11
process_name: "Incident Management"
category: procedures
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
  - "ITIL 4: Incident Management §3.2.1, §3.2.2"
  - "FitSM-2: §PR9 ISRM (incident scope)"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (incident coordination)"
last_updated: 2026-03-13
status: draft
---

# Incident Management — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the core operational activities — handling and resolving incidents through their full lifecycle, and managing major incidents with a dedicated coordinated response. Intermediate procedures add incident model management and structured incident reporting. The advanced procedure covers periodic incident review and continual improvement of incident management approaches. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All tiers)

### PROC-IM-01: Handle and Resolve Incidents
<!-- sources: ITIL 4 Incident Management §3.2.1 Table 3.1, Table 3.2, FitSM-2 §PR9 ISRM (manage incidents) -->

**Trigger:** Incident reported by a user (phone, email, portal, chat); event or alert received from monitoring and event management; incident detected by technical staff during normal operations

**Inputs:** Incident report or monitoring event, known errors and workarounds from the KEDB, configuration item data from the CMS, service level targets from SLAs, existing incident models and workflows, knowledge articles

**Outputs:** Incident record (new or updated), resolved and closed incident, change request (if infrastructure change required), problem record (if root cause investigation needed), workaround record (if new workaround identified), user satisfaction data

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Detect the incident | Identify the incident from its source — a monitoring alert or event correlation engine (automatic detection), a user report via the service desk (manual detection), or observation by technical staff. The goal is to detect the incident as early as possible, ideally before users are affected | Service Desk Agent / Technical Specialist |
| 2 | Register the incident | Log the incident in the ITSM tool with all required fields: incident title (function or process and observed fault), affected user(s), affected service or CI, current impact on user/customer workflow, potential future impact, time of first symptom, time of last known good function, detail of affected item (asset ID, application, CI reference), and source of detection. Where the incident is generated from a monitoring event, registration should be automated | Service Desk Agent |
| 3 | Classify the incident | Categorize the incident using the defined classification scheme. Match the incident against existing incident models and known errors in the KEDB. Classification determines routing to the appropriate resolver group and supports reporting and trend analysis | Service Desk Agent |
| 4 | Prioritize the incident | Assess impact and urgency to determine priority using the priority matrix. Impact is based on the number of affected users, the criticality of the affected service, and the business consequences. Urgency is based on the speed at which the business requires resolution, often linked to SLA targets. Check against major incident criteria — if criteria are met, transfer to the major incident handling procedure (PROC-IM-02) | Service Desk Agent / Incident Manager |
| 5 | Diagnose the incident | Investigate to identify the cause and determine the appropriate resolution. Check the KEDB for known errors and workarounds. Consult knowledge articles and diagnostic tools. Review configuration data from the CMS and recent change/release information. For simple incidents matching an incident model, follow the model's diagnostic steps. For complex incidents requiring specialist expertise, engage technical specialists or third-party suppliers. Where multiple specialists are needed, use collaborative techniques (swarming at T3) | Technical Specialist |
| 6 | Resolve the incident | Apply the identified fix, workaround, or automated remediation to restore normal service operation. For automatic resolution, pre-defined scripts may execute the fix without manual intervention. Confirm that the service has been restored and the user can resume normal work. Document all resolution actions taken, including what was done, when it started, and when it completed | Technical Specialist |
| 7 | Close the incident | Verify with the user that the incident has been resolved satisfactorily. If the user confirms resolution, close the incident record. Complete the record with resolution details, final categorization, and all timestamps. Capture user satisfaction data where appropriate. Determine whether a problem record should be raised (for incidents without a known root cause or for recurring incidents) or a change request should be submitted (for permanent fixes requiring infrastructure changes) | Service Desk Agent |

---

### PROC-IM-02: Handle Major Incidents
<!-- sources: ITIL 4 Incident Management §2.4.2 (major incidents), §3.2.1, FitSM-2 §PR9 ISRM (manage major incidents) -->

**Trigger:** Incident identified as meeting major incident criteria during classification and prioritization (Step 4 of PROC-IM-01); direct escalation from management or a service owner based on business impact assessment

**Inputs:** Incident record with major incident classification, major incident criteria, stakeholder contact information, service dependency information from the CMS, escalation paths, emergency change authorization procedures

**Outputs:** Resolved major incident record, major incident review report, change requests, problem records, improvement initiatives, stakeholder communications

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify the incident as major | Confirm that the incident meets the defined major incident criteria based on the severity of business impact, the number of affected users or services, or the potential for reputational or financial harm. Reclassify the incident as a major incident in the ITSM tool | Incident Manager |
| 2 | Assign the major incident coordinator | Designate a coordinator for the major incident. At T1, this is the incident manager. At T2+, a dedicated major incident manager should be assigned. The coordinator becomes the single point of contact and coordination for the duration of the major incident | Incident Manager |
| 3 | Mobilize resources and coordinate resolution | The coordinator mobilizes the required technical specialists, suppliers, and other resources. Assign the incident the highest operational priority. Coordinate the resolution effort across all involved teams, ensuring clear communication of roles, actions, and status. Where emergency changes are required, invoke the emergency change authorization procedure | Major Incident Coordinator |
| 4 | Communicate status to stakeholders | Inform affected users, service owners, management, and other relevant stakeholders that a major incident is in progress. Provide regular status updates at defined intervals throughout the major incident. Communication should include the nature of the incident, affected services, estimated resolution time (if known), and any workarounds available | Major Incident Coordinator |
| 5 | Resolve the major incident | Continue coordinated resolution efforts until normal service operation is restored. Confirm restoration with affected users and service owners. Document all actions taken, decisions made, and the resolution timeline | Technical Specialist |
| 6 | Conduct the post-major-incident review | After resolution, conduct a formal review of the major incident. Review the timeline of events, the effectiveness of the response, what went well, what could be improved, and whether the root cause has been identified. Agree follow-up actions — including problem records for root cause investigation, change requests for permanent fixes, and improvement initiatives for the incident management process itself | Incident Manager |
| 7 | Document and distribute the review report | Produce the major incident review report documenting the timeline, actions taken, root cause (if identified), lessons learned, and agreed follow-up actions with owners and target dates. Distribute the report to management, affected service owners, and all teams involved in the resolution. Register any improvement initiatives in the continual improvement register | Incident Manager |

---

## Intermediate Procedures (T2+)

### PROC-IM-03: Develop and Maintain Incident Models
<!-- sources: ITIL 4 Incident Management §2.4.2 (incident models), §3.2.2 Table 3.4, FitSM-2 §PR9 ISRM (identify well-known and recurring incidents, manage workflows) -->

**Trigger:** New recurring or well-known incident type identified; existing incident model found to be ineffective or outdated; periodic scheduled review of incident models; new service or technology introduced requiring incident handling procedures; findings from periodic incident review

**Inputs:** Incident records and trend data, known errors and workarounds from the KEDB, resolution knowledge from knowledge management, service and configuration information, feedback from service desk agents and technical specialists, findings from periodic incident reviews

**Outputs:** New or updated incident models, updated classification scheme entries, updated escalation criteria, communications to resolver teams and service desk agents

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify the need for a new or updated model | Review incident data to identify recurring incident types that would benefit from a pre-defined handling approach, or existing models that are no longer effective. Consider input from service desk agents, technical specialists, and periodic incident reviews. Prioritize model development based on incident frequency, impact, and resolution complexity | Incident Manager |
| 2 | Define the incident model | For each model, document: the incident type and matching criteria, classification and categorization, diagnostic steps (in sequence), resolution actions, escalation criteria and paths, target timescales for each step, required roles and skills, and any tools or access requirements. Where known errors exist in the KEDB, reference the applicable workaround or resolution | Incident Manager |
| 3 | Validate the model | Review the draft model with the technical specialists and service desk agents who will use it. Validate that the steps are accurate, complete, and practical. Test the model against recent incidents of the same type to verify that it would have led to effective resolution | Technical Specialist |
| 4 | Publish and communicate the model | Publish the approved model in the ITSM tool or knowledge base so that it is available to all resolver groups. Communicate the new or updated model to service desk agents and technical specialists. Provide training where the model introduces new steps or changes to existing workflows | Incident Manager |
| 5 | Review models periodically | At defined intervals, review all active incident models for currency and effectiveness. Retire models for incident types that no longer occur. Update models based on changes to services, technology, or resolution techniques. Use incident review findings and resolver feedback as inputs to the review | Incident Manager |

---

### PROC-IM-04: Produce Incident Reports and Analysis
<!-- sources: ITIL 4 Incident Management §2.4.3, §2.5 Table 2.2, FitSM-2 §PR9 ISRM (regular incident reports) -->

**Trigger:** Scheduled reporting cycle (weekly, monthly, quarterly); ad-hoc request from management or service owners; SLA review preparation

**Inputs:** Incident records from the ITSM tool, SLA targets and achievement data, major incident review reports, incident model usage data, user satisfaction survey results

**Outputs:** Incident reports (regular and ad-hoc), trend analysis data, input to SLA achievement reporting, input to Problem Management for pattern analysis

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Extract incident data | Extract incident data from the ITSM tool for the reporting period. Include volumes by classification, priority, status, resolver group, and service. Include resolution times, SLA achievement rates, escalation counts, and backlog data | Incident Manager |
| 2 | Analyse trends and patterns | Analyse the data for trends — increasing or decreasing volumes, shifts in classification distribution, changes in resolution times, recurring incident types, services with high incident rates, and SLA breach patterns. Compare with previous periods to identify emerging issues | Incident Manager |
| 3 | Compile the incident report | Produce the incident report covering: total incident volumes and breakdown by classification, priority distribution, mean resolution time and SLA achievement, first-contact resolution rate, escalation rate, incident backlog size and trend, major incident summary, and key observations or recommendations | Incident Manager |
| 4 | Distribute the report | Distribute the report to management, service owners, and other relevant stakeholders. Provide incident trend data to Problem Management for pattern and root cause analysis. Provide SLA achievement data to Service Level Management for service review input | Incident Manager |

---

## Advanced Procedures (T3)

### PROC-IM-05: Conduct Periodic Incident Review and Drive Improvement
<!-- sources: ITIL 4 Incident Management §2.4.3, §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Scheduled periodic review (quarterly or semi-annually); completion of a significant volume of incidents or major incidents warranting analysis; strategic planning cycle requiring incident management input

**Inputs:** Incident records and reports, incident model usage and effectiveness data, major incident review reports, user satisfaction data, resolver team feedback, service level achievement data, improvement initiative status from previous reviews

**Outputs:** Updated incident models and handling procedures, improvement initiatives registered in the continual improvement register, updated classification schemes and escalation paths, communications to affected teams, input to sourcing and team structure decisions

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Prepare the review | Compile the review data set — incident reports, trend analyses, major incident review reports, model usage statistics, SLA achievement data, user satisfaction scores, resolver feedback, and the status of improvement initiatives from previous reviews. Schedule the review and invite participants (incident manager, service owners, technical specialists, suppliers as appropriate) | Incident Manager |
| 2 | Review incident records and analyse data | Analyse incident data across the review period for systemic issues — recurring incident types without effective models, services with declining resolution performance, persistent SLA breaches, classification or prioritization inconsistencies, and patterns suggesting underlying problems not yet identified by Problem Management | Incident Manager |
| 3 | Assess incident model effectiveness | Evaluate the usage and effectiveness of existing incident models. Identify models with low usage (potential awareness or matching issues), models with high usage but poor resolution outcomes (potential model quality issues), and incident types without models that would benefit from one | Incident Manager |
| 4 | Identify improvement opportunities | Based on the analysis, identify specific improvement opportunities — new or updated incident models, changes to classification schemes or escalation paths, automation opportunities, training needs, team structure adjustments, or tool enhancements. Prioritize improvements by expected impact and feasibility | Incident Manager |
| 5 | Initiate improvement actions | Register improvement initiatives in the continual improvement register with owners, target dates, and success criteria. For incident model improvements, initiate the model development or update process (PROC-IM-03). For broader changes (team structures, tooling, automation), raise through the appropriate governance channels | Incident Manager |
| 6 | Communicate review findings and model updates | Communicate the review findings, decisions, and updated models to all affected teams — service desk agents, technical specialists, service owners, and management. Ensure that updated incident models, classification schemes, and escalation paths are published and accessible | Incident Manager |
| 7 | Track improvement implementation | Monitor the implementation of agreed improvement initiatives. Report on progress at the next periodic review. Escalate stalled or blocked improvements through management channels | Incident Manager |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-IM-01 | Handle and Resolve Incidents | All | Incident reported or detected |
| PROC-IM-02 | Handle Major Incidents | All | Incident meets major incident criteria |
| PROC-IM-03 | Develop and Maintain Incident Models | T2+ | Recurring type identified; model review; new service |
| PROC-IM-04 | Produce Incident Reports and Analysis | T2+ | Scheduled reporting cycle; ad-hoc request |
| PROC-IM-05 | Conduct Periodic Incident Review and Drive Improvement | T3 | Scheduled review; strategic planning cycle |
