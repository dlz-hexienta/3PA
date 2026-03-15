---
process_id: PR12
process_name: "Service Request Management"
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
  - "ITIL 4: Service Request Management §3.2.1, §3.2.2"
  - "FitSM-2: §PR9 ISRM (request scope)"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Request Management — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier. The two ITIL 4 sub-processes — service request fulfilment control and service request review and optimization — are consolidated into five procedures. Many activities have both manual and automated variants — organizations should implement the variant appropriate to their maturity and automation capabilities.

---

## Essential Procedures (All tiers)

### PROC-SRM-01: Categorize and Fulfil Service Requests
<!-- sources: ITIL 4 SRM §3.2.1 Tables 3.1, 3.2 -->

**Trigger:** Service request received through any established channel — web portal, service desk, email, chat, or other agreed channel.

**Scope:** Covers request categorization, model-based fulfilment initiation and control, and fulfilment review. Maps to definition activities 1–3.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Categorize the service request — check all prerequisites and user eligibility against the request catalogue and SLA conditions. Request missing information or paperwork from the user. Select the appropriate service request model based on request characteristics. In automated environments, the system checks prerequisites, contacts users for missing information, and selects models automatically | Fulfilment Agent | Service request, request catalogue, SLAs | Categorized request; selected model |
| 2 | Initiate model-based fulfilment — assign teams and specialists according to the request model. Follow defined fulfilment procedures. Obtain additional approvals where required by the model. Where multiple fulfilment tasks are needed, coordinate assignment and sequencing. Notify the user of progress at agreed milestones. In automated environments, the system controls the flow of procedures and scripts | Fulfilment Agent | Categorized request, request model | Fulfilment actions in progress |
| 3 | Control fulfilment progress — monitor tasks against agreed fulfilment timeframes. Update relevant configuration items upon completion where required. Escalate when fulfilment is at risk of exceeding targets. Coordinate with multiple teams where fulfilment spans organizational boundaries | Fulfilment Agent | Fulfilment actions, SLA targets | Completed fulfilment actions; updated CIs |
| 4 | Review fulfilment — check that fulfilment has produced the desired result according to the model. Collect user feedback and measure satisfaction. For cases where fulfilment deviated from plan or satisfaction is low, conduct a detailed internal review. Close the service request with user communication confirming completion | Service Request Manager | Fulfilment records, model criteria | Closed service request; satisfaction data; fulfilment review record |

**Exit criteria:** Request categorized and model selected. Fulfilment completed according to model. Outcome verified against model criteria. User notified of completion. Satisfaction data collected. Request record closed.

---

### PROC-SRM-02: Maintain Service Request Models
<!-- sources: ITIL 4 SRM §2.2, §2.4.1, FitSM-2 §PR9 -->

**Trigger:** New service or service offering introduced, existing service modified, gap identified in request model coverage, or scheduled model review cycle.

**Scope:** Covers identification, documentation, testing, and deployment of request models. Maps to definition activities 4–5.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify service request types — analyse service descriptions, SLAs, and user interaction patterns to identify all request types that should be available to users. For each type, determine whether a model already exists, needs updating, or must be created | Service Request Manager | Service descriptions, SLAs, user demand data | List of request types requiring models |
| 2 | Document request models — for each request type, define the fulfilment procedure (workflow, decision points, options), roles and responsibilities (RACI), automation and tools, third-party involvement, approval requirements, target fulfilment time, and exception handling. Derive models from service design outputs where available | Service Owner | Request type definition, service design outputs | Documented request model |
| 3 | Test and validate models — verify that fulfilment procedures produce the desired result, that timelines are achievable, and that all involved teams accept their responsibilities. Test automation scripts and workflows. Validate against SLA targets | Service Request Manager | Documented model | Validated request model |
| 4 | Deploy models and update the request catalogue — deploy validated models to operational use. Ensure corresponding request catalogue entries are created or updated — including prerequisites, required information, approval workflows, and fulfilment targets. Communicate new or updated models to fulfilment teams and service desk agents | Service Request Manager | Validated model | Deployed model; updated catalogue entries |

**Exit criteria:** All service request types identified and documented. Models tested and validated. Catalogue entries accurate and current. Fulfilment teams informed and prepared.

---

## Intermediate Procedures (T2+)

### PROC-SRM-03: Handle Fulfilment Exceptions
<!-- sources: ITIL 4 SRM §3.2.1 Table 3.2 -->

**Trigger:** Standard fulfilment procedure does not produce the desired result — due to new circumstances, non-standard user requirements, model gaps, or errors in the procedure.

**Scope:** Covers ad hoc fulfilment control and exception feedback into model improvement. Maps to definition activity 6.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify the exception — determine why the standard model cannot fulfil the request. Classify the exception type: model gap (request type not covered), procedure error (model exists but steps are incorrect or incomplete), or circumstance exception (unusual conditions not anticipated by the model) | Fulfilment Agent | Failed or blocked fulfilment attempt, model documentation | Exception classification |
| 2 | Decide on action — determine whether to proceed with tailored ad hoc fulfilment or deny the request. This decision is usually defined by the model's exception handling section. For requests requiring non-standard work, obtain authorization from the service owner or equivalent authority | Service Owner | Exception classification, model exception rules | Authorization to proceed or denial with explanation |
| 3 | Execute ad hoc fulfilment — where authorized, perform tailored fulfilment actions. Document all steps taken, deviations from standard procedure, resources used, and time consumed. Treat ad hoc fulfilment as an exception — not a precedent for future requests of the same type | Fulfilment Agent | Authorization, request details | Fulfilled request; ad hoc fulfilment record |
| 4 | Feed back to model improvement — record all exception details as input to the service request review and optimization process. Recommend whether the model should be extended to cover the exception case or whether additional categorization checks should filter such cases out of the model | Service Request Manager | Exception record, ad hoc fulfilment details | Model improvement input |

**Exit criteria:** Exception classified and decision made. Ad hoc fulfilment completed or request denied with explanation. Exception details recorded for model improvement.

---

### PROC-SRM-04: Review and Improve Request Performance
<!-- sources: ITIL 4 SRM §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Scheduled performance review cycle, significant performance issue or user satisfaction decline, or accumulation of fulfilment exceptions indicating model deficiency.

**Scope:** Covers performance analysis, model improvement initiation, and update communication. Maps to definition activities 7–8.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Analyse service request records and metrics — review fulfilment data over the period covering volumes by type, fulfilment times against SLA targets, exception rates, user satisfaction scores, and resource utilization. Identify patterns indicating model deficiencies or improvement opportunities. Review repeating changes from change management that could be formalized as request models | Service Request Manager | Request records, fulfilment metrics, satisfaction surveys, change records | Performance analysis; improvement opportunities |
| 2 | Prioritize improvements — assess identified opportunities based on impact on user satisfaction, fulfilment efficiency, exception reduction, and alignment with organizational objectives. Determine whether improvements require changes to models, procedures, tools, or organizational arrangements | Service Request Manager | Improvement opportunities | Prioritized improvement list |
| 3 | Initiate model improvements — register improvement initiatives for processing through the continual improvement practice or submit change requests for model updates requiring formal approval. Test proposed model changes before deployment. Return unsuccessful updates for further analysis | Service Request Manager | Prioritized improvements | Registered improvement initiatives; change requests; updated models |
| 4 | Track improvement outcomes — monitor the impact of implemented improvements on fulfilment performance, exception rates, and user satisfaction. Verify that model updates have been adopted by all fulfilment teams. Adjust models based on results | Service Request Manager | Implemented improvements, ongoing metrics | Improvement outcome records |

**Exit criteria:** Performance reviewed against agreed criteria. Improvements identified, prioritized, and initiated. Model updates tested and deployed. Outcomes tracked and verified.

---

## Advanced Procedures (T3)

### PROC-SRM-05: Optimize Automation and Third-Party Integration
<!-- sources: ITIL 4 SRM §2.4.1, §5.2, §6 -->

**Trigger:** Strategic review of fulfilment efficiency, high-volume request type identified for automation, new third-party fulfilment arrangement, or periodic automation optimization review.

**Scope:** Covers fulfilment automation development, third-party integration, and model update communication. Maps to definition activities 9–10.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify automation candidates — analyse request volumes, fulfilment complexity, variation rates, and cost per fulfilment to identify requests suitable for automation. Prioritize the most popular and routine requests with limited variations. Assess whether automation costs and risks are justified for each candidate | Service Request Manager | Volume data, cost analysis, complexity assessment | Automation candidates with justification |
| 2 | Develop and deploy automation — implement automated fulfilment workflows — from fully automated self-service (submission to closure without human intervention) to orchestrated workflows coordinating multiple systems and teams. Test automation thoroughly before deployment. Ensure automated fulfilment maintains or improves quality and satisfaction levels | Service Request Manager | Automation candidates, technology capabilities | Deployed automation; updated models |
| 3 | Define third-party integration interfaces — for request types involving external suppliers, define standard interfaces specifying data exchange formats, tools, processes, and service levels. Ensure interfaces create a common language in multi-vendor environments and remove formal bureaucratic barriers to collaboration | Service Owner | Supplier agreements, fulfilment requirements | Integration interface specifications |
| 4 | Communicate model updates — notify all relevant stakeholders of new or updated request models, automation capabilities, and third-party arrangements. Ensure fulfilment teams, service desk agents, service owners, and users are aware of changes. Update catalogue entries and working instructions | Service Request Manager | Updated models, automation deployments | Stakeholder communications; updated documentation |
| 5 | Monitor automation effectiveness — track automation adoption, fulfilment times, error rates, user satisfaction with automated channels, and cost per fulfilment. Compare automated vs manual fulfilment performance. Identify automation failures requiring human intervention and feed into further optimization | Service Request Manager | Automation performance data | Optimization recommendations; performance report |

**Exit criteria:** Automation candidates identified and justified. Automated workflows deployed and tested. Third-party interfaces defined. Stakeholders informed. Automation performance monitored and optimized.
