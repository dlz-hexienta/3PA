---
process_id: PR15
process_name: "Change Management"
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
  - "ITIL 4: Change Enablement §3.2.1, §3.2.2"
  - "FitSM-2: §PR12 CHM"
  - "IT4IT: R2D Value Stream"
  - "SIAM: Service Integration (change coordination)"
last_updated: 2026-03-13
status: draft
---

# Change Management — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the core operational activities — managing the full change lifecycle from registration through closure, and handling emergency changes through an expedited path. Intermediate procedures add change model and standard change management, and structured change reporting. The advanced procedure covers periodic change review analysis and practice optimization. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All tiers)

### PROC-CHM-01: Manage the Change Lifecycle
<!-- sources: ITIL 4 Change Enablement §3.2.1 Tables 3.1, 3.2, FitSM-2 §PR12 CHM (Manage change evaluation and approval, Manage change implementation and review) -->

**Trigger:** Request for change (RFC) received from a change initiator — which may be any role or process (incident management, problem management, service request fulfilment, project management, security remediation, etc.)

**Inputs:** Change requests, change models and standard change procedures, configuration information from the CMS, service level agreements, financial guidelines and constraints, risk information, capacity and performance information, security policies

**Outputs:** Change records (new and updated), change schedule (updated), authorized changes for deployment, change review reports, information on implemented changes to CIs

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Register the change | Receive the RFC through defined channels. Create a change record in the ITSM tool with all required information: what is to be changed, the reason and expected benefits, estimated time and cost, risks and regulatory considerations, and the identity of the change initiator. Send confirmation of receipt to the initiator. For backlog-managed changes, requests are accumulated in the product or service backlog and the development team decides which requests to take into development | Change Manager / Change Coordinator |
| 2 | Classify the change | Categorize the change by type — standard, normal, or emergency — using defined criteria. Check against major change and emergency change criteria. Determine the applicable change model based on the classification. For standard changes, identify the applicable pre-authorized procedure and proceed directly to planning (step 5). For emergency changes, transfer to the emergency change procedure (PROC-CHM-02) | Change Manager / Change Coordinator |
| 3 | Assess the change | Evaluate the change to understand its potential impact on services, users, infrastructure, and other planned or ongoing changes. Assess benefits, risks, potential impact, cost and effort, and technical feasibility. Consult subject matter experts and review configuration data, service dependencies, and recent change history as needed. Assessment depth is determined by the change model — from lightweight for low-risk normal changes to comprehensive for high-risk or major changes. Add assessment information to the change record | Change Manager / Technical Specialist |
| 4 | Authorize the change | Present the assessed change to the designated change authority for authorization. The change authority reviews the assessment and provides authorization, requests additional assessment, or rejects the change. If not authorized, the change is sent to step 7 for closure. For low-risk normal changes, authorization may be delegated and rapid. For high-risk changes, a more formal authorization involving multiple stakeholders may be required. Authorization decisions and rationale are recorded | Change Authority |
| 5 | Plan and schedule the change | Plan the authorized change in detail — defining implementation steps, resources, timescales, communication requirements, testing approach, and back-out plan. Update the change schedule with planned implementation dates. Coordinate with other planned changes and with release management to avoid conflicts and align with deployment windows. Planning depth is determined by the change model — for standard changes, planning may be minimal as the pre-defined procedure already specifies the steps | Change Manager / Service Owner |
| 6 | Control change realization | Monitor the implementation of the change by internal and external specialist teams. Ensure that implementation proceeds according to plan and that deviations are detected and corrected. For automated standard changes, realization control includes automated validation, testing, configuration control, version control, and backup/restoration. For manually managed changes, the change manager coordinates activities and monitors progress. If the change fails or cannot be completed, invoke the back-out plan | Change Manager / Technical Specialist |
| 7 | Review and close the change | After the change is complete (or if it fails or is rejected), review the change to assess: whether it achieved its intended outcomes, was completed on time and within budget, and introduced any unintended consequences. Complete the change record with review findings, close it, and update the CMS with information on implemented changes. For unsuccessful changes, document the reasons for failure and any lessons learned. Notify the change initiator of the outcome | Change Manager / Service Owner |

---

### PROC-CHM-02: Handle Emergency Changes
<!-- sources: ITIL 4 Change Enablement §2.2.1 (emergency changes), FitSM-2 §PR12 CHM (define criteria for identifying emergency changes, special conditions for emergency changes) -->

**Trigger:** Incident or situation requiring an immediate change to restore or protect services — typically a major incident, an urgent security vulnerability, or a regulatory mandate with an immediate deadline

**Inputs:** Emergency change request, incident records, configuration information, emergency change criteria, emergency change authorization contacts

**Outputs:** Change record (emergency), emergency change authorization, implemented emergency change, post-implementation review report

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify the change as emergency | Confirm that the change meets the defined emergency change criteria — typically based on the severity of the incident being addressed, the immediacy of the threat, or the regulatory deadline. Reclassify the change as an emergency in the ITSM tool. If the change does not meet emergency criteria, route it through the normal change lifecycle (PROC-CHM-01) | Change Manager |
| 2 | Register the emergency change | Create the change record with all available information. Registration may be abbreviated — some details can be completed after implementation — but the change must be recorded to maintain an audit trail. The focus is on capturing what is being changed, why it is urgent, and what the expected outcome is | Change Manager / Change Coordinator |
| 3 | Perform expedited assessment | Assess the emergency change for impact and risk, using the information available within the time constraints. Engage the relevant technical specialists for a rapid assessment. The assessment may be less comprehensive than for a normal change, but the key risks and potential impacts must be identified | Change Manager / Technical Specialist |
| 4 | Obtain emergency authorization | Present the emergency change to the designated emergency change authority — which should be a pre-defined individual or small group with the authority and availability to authorize emergency changes outside normal working hours. Authorization may be obtained verbally or through expedited electronic means, with formal documentation completed after the fact | Emergency Change Authority |
| 5 | Implement the emergency change | Implement the change as quickly as possible, following the emergency change model. Ensure that a back-out plan exists, even if simplified. Monitor the implementation and confirm that the intended outcome has been achieved — the incident is resolved, the vulnerability is mitigated, or the regulatory requirement is met | Technical Specialist |
| 6 | Complete the change record | After implementation, complete the change record with all details that were abbreviated during the expedited process — including full impact assessment, authorization documentation, implementation details, and outcome confirmation. Update the change schedule and the CMS | Change Manager / Change Coordinator |
| 7 | Conduct the post-implementation review | Conduct a mandatory post-implementation review of the emergency change. Assess: whether the change achieved its intended outcome, whether it introduced any unintended consequences, whether the emergency classification was justified, and whether the emergency change procedure worked effectively. Document findings and lessons learned. Identify whether the root cause should be addressed through a normal change or problem investigation to prevent future emergencies | Change Manager / Service Owner |

---

## Intermediate Procedures (T2+)

### PROC-CHM-03: Develop and Maintain Change Models and Standard Changes
<!-- sources: ITIL 4 Change Enablement §2.2.1, §3.2.2 Tables 3.3, 3.4, FitSM-2 §PR12 CHM (identify well-known and recurring changes, create standardised changes) -->

**Trigger:** New change type identified that would benefit from a defined model; existing change model found to be ineffective or outdated; recurring low-risk change identified as a candidate for standardization; change review analysis identifying optimization opportunities; new service or technology introduced requiring change handling procedures

**Inputs:** Change records and review data, current change models and standard change procedures, configuration information, service catalogue, risk information, regulatory requirements, feedback from change coordinators and technical specialists

**Outputs:** New or updated change models, new or updated standard change procedures, communications to affected teams

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify the need for a new or updated model | Review change data to identify change types that would benefit from a defined model (recurring changes currently handled as normal changes), existing models that are producing poor outcomes, or recurring low-risk changes suitable for standardization. Consider input from change coordinators, technical specialists, and service owners | Change Manager |
| 2 | Define the change model | For each change model, document: the change types it applies to and matching criteria, the assessment criteria and depth, the authorization level and authority, the planning requirements, the realization controls, the review procedures, the back-out approach, and the involvement of third parties. For standard change procedures, define the specific implementation steps, controls, and conditions under which the procedure applies. Perform a full risk assessment of the standard change procedure | Change Manager / Service Owner |
| 3 | Validate the model | Review the draft model with the technical specialists, change coordinators, and service owners who will use it. Validate that the model is accurate, practical, and provides appropriate risk control. For standard change procedures, confirm that the risk assessment is complete and the procedure can be pre-authorized | Technical Specialist / Service Owner |
| 4 | Authorize and publish the model | Obtain authorization for the change model or standard change procedure from the appropriate authority. Publish the model in the ITSM tool or knowledge base so that it is available to all relevant roles. For standard change procedures, the authorization of the procedure constitutes pre-authorization of all future change instances that follow it | Change Manager |
| 5 | Review models periodically | At defined intervals, review all active change models and standard change procedures for currency and effectiveness. Retire models for change types that no longer occur. Update models based on changes to services, technology, regulations, or operational experience. Use change review analysis findings as input to the review | Change Manager |

---

### PROC-CHM-04: Produce Change Reports
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4, FitSM-2 §PR12 CHM (post implementation review reports) -->

**Trigger:** Scheduled reporting cycle (weekly, monthly, quarterly); ad-hoc request from management or service owners; governance or compliance audit preparation

**Inputs:** Change records from the ITSM tool, change schedule data, post-implementation review reports, emergency change data, change-related incident data

**Outputs:** Change reports (regular and ad-hoc), trend analysis data, input to SLA achievement reporting, input to governance and compliance reviews

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Extract change data | Extract change data from the ITSM tool for the reporting period. Include volumes by type (standard, normal, emergency), status, service, and change model. Include success rates, realization times, emergency change counts, and change-related incident data | Change Coordinator |
| 2 | Analyse trends and patterns | Analyse the data for trends — changes in volumes, shifts in type distribution, services with high change failure rates, changes in realization times, emergency change patterns, and correlation between changes and incidents. Compare with previous periods to identify emerging issues or improvements | Change Manager |
| 3 | Compile the change report | Produce the change report covering: total change volumes and breakdown by type, change success rate, mean realization time by change model, emergency change count and justifications, change-related incidents, change schedule adherence, and key observations or recommendations | Change Manager |
| 4 | Distribute the report | Distribute the report to management, service owners, and other relevant stakeholders. Provide change data to incident management for correlation analysis. Provide input to SLA achievement reporting for service level management. Provide input to governance and compliance reviews as required | Change Manager |

---

## Advanced Procedures (T3)

### PROC-CHM-05: Analyse Change Reviews and Optimize Change Models
<!-- sources: ITIL 4 Change Enablement §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Scheduled periodic review (quarterly or semi-annually); accumulation of unsuccessful changes warranting analysis; regulatory or compliance changes requiring model updates; strategic planning cycle

**Inputs:** Change records and review data, current change models and standard change procedures, change-related incident data, post-implementation review reports, stakeholder satisfaction data, governance and compliance audit findings, improvement initiative status from previous reviews

**Outputs:** Change review analysis report, improvement initiatives registered in the continual improvement register, change requests for model updates, updated change models and standard change procedures, communications to affected teams

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Select and analyse changes for review | Select a representative sample of changes for detailed review — prioritizing unsuccessful changes, changes that triggered incidents, emergency changes, and changes where the change model may have been inadequate. Analyse the selected changes for patterns: common causes of failure, recurring issues, bottlenecks in the change lifecycle, and opportunities for further standardization or automation | Change Manager / Service Owner |
| 2 | Assess change model effectiveness | Evaluate the usage and effectiveness of existing change models and standard change procedures. Identify models with high failure rates, models that are frequently overridden, standard change procedures that are underused, and change types that lack appropriate models. Assess whether change authority delegation is at the right level — too centralized (causing bottlenecks) or too decentralized (insufficient risk control) | Change Manager |
| 3 | Identify improvement opportunities | Based on the analysis, identify specific improvement opportunities — new or updated change models, new standard change procedures for recurring change types, automation of manual steps, changes to authorization levels, improvements to assessment criteria, or enhancements to tooling and reporting | Change Manager |
| 4 | Initiate improvements | Register improvement initiatives in the continual improvement register with owners, target dates, and success criteria. For change model and standard change procedure updates, initiate the model development process (PROC-CHM-03). For broader changes (tooling, organizational structure, governance), raise through the appropriate governance channels | Change Manager |
| 5 | Communicate updated models and findings | Communicate the review findings, decisions, and updated change models to all affected teams. Ensure that updated models and standard change procedures are published and accessible. Provide training where models introduce new steps or change existing workflows | Change Manager |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-CHM-01 | Manage the Change Lifecycle | All | RFC received from any source |
| PROC-CHM-02 | Handle Emergency Changes | All | Major incident; urgent security vulnerability; regulatory mandate |
| PROC-CHM-03 | Develop and Maintain Change Models and Standard Changes | T2+ | New change type; model review; standardization candidate; new service |
| PROC-CHM-04 | Produce Change Reports | T2+ | Scheduled reporting cycle; ad-hoc request |
| PROC-CHM-05 | Analyse Change Reviews and Optimize Change Models | T3 | Scheduled review; unsuccessful change accumulation; strategic planning |
