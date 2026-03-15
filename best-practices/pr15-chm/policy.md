---
process_id: PR15
process_name: "Change Management"
category: policy
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
  - "ITIL 4: Change Enablement §2.1, §2.2, §2.3, §2.4"
  - "FitSM-2: §PR12 CHM"
  - "IT4IT: R2D Value Stream"
  - "SIAM: Service Integration (change coordination)"
last_updated: 2026-03-13
status: draft
---

# Change Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Change Enablement §2.1, §2.2, FitSM-2 §PR12 CHM Objective -->

The organization shall maximize the number of successful service and product changes by ensuring that risks have been properly assessed, authorizing changes to proceed through appropriate change authorities, and managing the change schedule. All changes — additions, modifications, or removals of anything that could have a direct or indirect effect on services — within the defined scope shall be registered, classified, assessed, authorized, planned, controlled, reviewed, and closed using a complexity-based approach that balances change effectiveness, change throughput, and risk control. The organization shall define change models for different change types that determine the level of formalization, assessment depth, authorization authority, and control appropriate to each type. Standard changes shall be pre-authorized and automated where possible. Emergency changes shall follow an expedited procedure with mandatory post-implementation review. The organization shall continually optimize change models and standard change procedures to increase throughput while maintaining appropriate risk control.

## Objectives
<!-- sources: ITIL 4 Change Enablement §2.4 PSFs, FitSM-2 §PR12 CHM Key Questions -->

1. Ensure that changes are realized in a timely and effective manner — achieving intended outcomes (not just intended outputs), meeting the change initiator's requirements for timeliness, and contributing to the organization's overall service quality and value delivery
2. Minimize the negative impact of changes on services, users, and the organization — through appropriate risk assessment, impact analysis, standardization, automation, reduction of change size, and the ability to quickly revert unsuccessful changes
3. Ensure stakeholder satisfaction with changes and the change enablement practice — by identifying stakeholders, capturing their expectations, communicating change plans and progress, and monitoring satisfaction during and after change realization
4. Meet change-related governance and compliance requirements — by including required controls in change models, providing required information and audit trails, and initiating improvements to prevent or correct non-compliance

## Scope

This policy applies to all changes within the scope of the organization's service management system. It covers:

- Planning changes to controlled environments in the organization
- Planning change models and the standardization of change procedures
- Planning individual change workflows, activities, and controls
- Scheduling and coordinating all ongoing changes
- Controlling the progress of changes from initiation to completion
- Communicating change plans and progress to relevant stakeholders
- Assessing change success — including outputs, outcomes, efficiency, risks, and costs
- The continual optimization of change models and standard change procedures

This policy typically applies to changes to the information and technology dimension of the organization's products and services (hardware, software, service architecture, technical documentation). Changes to other dimensions — organizations and people, value streams and processes, partners and suppliers — may also fall within scope depending on the organization's scope decisions.

This policy does not cover: change initiation (which is the responsibility of any practice that identifies the need for a change), change realization (which is performed by specialist teams using relevant practices such as release management, deployment management, and infrastructure management), or testing (which is addressed under service validation and testing).

## Principles

### P1. Complexity-Based Approach
<!-- sources: ITIL 4 Change Enablement §2.2.1 -->
Different situations require different approaches to change planning, authorization, and control. The organization shall select the approach based on the complexity and predictability of each change type. For well-understood, recurring changes in predictable situations, standard changes with pre-authorized procedures are appropriate. For changes requiring individual expert judgement, a normal change process with assessment and authorization is required. For emergency situations where the cost of delay exceeds the risk of an unsuccessful change, an expedited emergency change procedure shall be used. Change models shall codify the appropriate approach for each change type across this spectrum.

### P2. Risk-Based Authorization
<!-- sources: ITIL 4 Change Enablement §2.2.1, §4.1.2 -->
Changes shall be authorized by an appropriate change authority whose level matches the risk and impact of the change. Change models shall delegate the change authority role as close to the work as possible while maintaining appropriate risk control — from automated authorization for standard changes, through delegated authority for low-risk normal changes, to formal management authorization for high-risk changes. Formal committees that accumulate and batch-process changes can become bottlenecks that limit throughput and should be used only where the level of risk genuinely requires collective review.

### P3. Standardization and Automation
<!-- sources: ITIL 4 Change Enablement §2.2.1, §2.2.3, FitSM-2 §PR12 CHM (identify well-known and recurring changes) -->
The organization shall identify recurring low-risk changes and create standard change procedures with pre-authorized workflows. Standard changes shall be automated where possible — including registration, validation, configuration control, version control, testing, and closure. Standardization and automation significantly increase change throughput while retaining sufficient risk control. In highly automated environments (CI/CD pipelines), most change enablement activities may be automated, with manual intervention required only for exceptions.

### P4. Minimize Change Size
<!-- sources: ITIL 4 Change Enablement §2.2.1, §2.4.2 -->
The organization shall favour smaller, more frequent changes over large, infrequent changes wherever practical. Smaller changes are less risky, less costly to implement, easier to control, faster to deliver, and less expensive to reverse if unsuccessful. Many organizations limit the maximum size of individual changes, particularly for software and digital resources. Where a large change is required, the organization should consider deconstructing it into iterations, each below an agreed risk-level threshold.

### P5. Stakeholder Visibility and Communication
<!-- sources: ITIL 4 Change Enablement §2.2.3, §2.4.3 -->
The organization shall maintain visibility of planned and ongoing changes for all relevant stakeholders — including service owners, technical teams, incident management, users, and affected suppliers. The change schedule shall be published and kept current. Stakeholders shall be informed of change plans, progress, and outcomes. In highly automated environments where the full scope of changes may be difficult to oversee, the organization shall ensure that sufficient visibility is maintained through appropriate tooling and reporting.

### P6. Governance and Compliance
<!-- sources: ITIL 4 Change Enablement §2.4.4, FitSM-2 §PR12 CHM -->
The organization shall include required governance and compliance controls in change models, processes, and procedures. Changes subject to regulatory requirements shall follow defined authorization and documentation procedures that provide auditable evidence. The change enablement practice shall support the organization's governance framework by providing required information, maintaining traceable records, and initiating improvements to prevent or correct non-compliance.

### P7. Continual Optimization
<!-- sources: ITIL 4 Change Enablement §3.2.2, §2.4 -->
The organization shall periodically review change data to identify unsuccessful changes, recurring issues, bottlenecks, and opportunities for further standardization or automation. Change models and standard change procedures shall be updated based on review findings and operational experience. Improvement initiatives shall be registered and tracked through the continual improvement process. The goal is to continually increase change throughput and effectiveness while reducing risk and negative impacts.

## Mandatory Requirements

### Essential (All tiers)

| ID | Requirement |
|----|------------|
| CHM-R01 | All changes within the defined scope shall be registered in the ITSM tool with the information required for assessment and authorization — including what is to be changed, the reason, expected benefits, and estimated impact and risk |
| CHM-R02 | Changes shall be classified by type — standard, normal, or emergency — using defined criteria, and the applicable change model shall be determined based on the classification |
| CHM-R03 | Changes shall be assessed for impact on services, users, and infrastructure, and for associated risks, required resources, costs, and technical feasibility. Assessment depth shall be proportionate to the change type and risk |
| CHM-R04 | Changes shall be authorized by an appropriate change authority before implementation proceeds. The change authority level shall be determined by the change model and shall be proportionate to the risk and impact of the change |
| CHM-R05 | Authorized changes shall be planned and scheduled, with planned dates recorded in the change schedule. Changes shall be coordinated to avoid conflicts with other planned changes and with service availability requirements |
| CHM-R06 | Completed changes shall be reviewed to assess whether they achieved intended outcomes and introduced any unintended consequences. Change records shall be completed with review findings and closed |
| CHM-R07 | Criteria for identifying emergency changes shall be defined and consistently applied. Emergency changes shall follow an expedited procedure with a mandatory post-implementation review |
| CHM-R08 | A change manager role shall be assigned with accountability for the change enablement practice — including processing change requests, maintaining the change schedule, and ensuring changes follow defined procedures |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| CHM-R09 | Change models shall be defined for different change types, specifying the assessment criteria, authorization level, planning requirements, realization controls, and review procedures appropriate for each type |
| CHM-R10 | Standard change procedures shall be created and maintained for recurring low-risk changes, with pre-authorized workflows that have been fully risk-assessed. Standard change procedures shall be reviewed and updated when the underlying conditions change |
| CHM-R11 | The change schedule shall be published and made available to all relevant stakeholders, including incident management, release management, and affected users |
| CHM-R12 | A change coordinator role shall be assigned to support change management activities within defined scopes — specific change types, territories, or parts of the organization |
| CHM-R13 | Post-implementation reviews shall be conducted for all emergency changes, all major changes, and all unsuccessful changes, producing documented findings and lessons learned |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| CHM-R14 | Periodic change review analysis shall be conducted to identify patterns in unsuccessful changes, recurring issues, bottlenecks, and opportunities for further standardization or automation |
| CHM-R15 | Change models and standard change procedures shall be subject to continual optimization based on change review analysis, operational experience, and improvement initiatives |

## Compliance and Review

- This policy shall be reviewed at least annually or following a significant change to the organization's service portfolio, technology landscape, or regulatory environment
- Compliance with this policy shall be assessed through change reports, change success rates, post-implementation review data, and periodic change review analyses
- Non-compliance shall be escalated to the change manager and service management leadership for remediation
- Exceptions to this policy require documented justification and approval from the change manager or senior leadership

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Release & Deployment Management Policy (PR16) | Release management bundles approved changes into releases and manages their deployment. The change schedule informs release planning, and release information feeds post-implementation reviews |
| Service Configuration Management Policy (PR17) | The CMS provides configuration data that supports change impact assessment. Implemented changes are reflected in the CMS to maintain an accurate record of the infrastructure |
| Incident Management Policy (PR11) | Incidents may trigger changes (including emergency changes). The change schedule informs incident management about recent changes that may be the cause of incidents |
| Problem Management Policy (PR13) | Problem resolutions often require changes to eliminate root causes. Problem management is a key source of changes aimed at improving service stability |
| Service Level Management Policy (PR02) | SLAs define service availability requirements that inform change scheduling and authorization. Change data contributes to SLA achievement reporting |
| Information Security Management Policy (PR09) | Security policies and requirements must be considered during change assessment. Security-related changes (patches, vulnerability remediation) follow change management procedures |
| Risk Management Policy (PR21) | Risk assessments support change impact analysis and authorization decisions. Change-related risks are managed within the organization's risk framework |
| Continual Improvement Policy (PR24) | Improvement initiatives from change review analysis feed the continual improvement register. Change management is a key enabler of service improvement |
