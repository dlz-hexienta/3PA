---
process_id: PR16
process_name: "Release & Deployment Management"
category: policy
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Release Management §2.1–§2.4"
  - "ITIL 4: Deployment Management §2.1–§2.4"
  - "FitSM-2: §PR13 RDM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Release & Deployment Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Release Management §2.1, ITIL 4 Deployment Management §2.1, FitSM-2 §PR13 RDM Objective -->

The organization shall bundle approved changes into appropriate types of releases and effectively deploy them to target environments, making new and changed services and service components available for use. Release and deployment activities shall follow defined models that specify the approach for different product and component types — including release types, deployment flows, automation levels, verification criteria, and user enablement procedures. The organization shall maintain the integrity of service components throughout the transition from development to production and ensure that releases are delivered in line with service agreements, user requirements, and regulatory obligations. The organization shall continually optimize release and deployment models and procedures to increase throughput, improve automation, and reduce failures.

## Objectives
<!-- sources: ITIL 4 Release Management §2.4 PSFs, ITIL 4 Deployment Management §2.4 PSFs, FitSM-2 §PR13 RDM Key Questions -->

1. Establish and maintain effective approaches to the release of services and service components — defining release models, strategies, and plans that are appropriate for the organization's products, services, and service relationships
2. Ensure the effective release of services and service components — coordinating release instances across the organization's value streams and service relationships, enabling users to consume new and changed services
3. Establish and maintain effective approaches to the deployment of services and service components — defining deployment models, procedures, and automation that are appropriate for different component types and environments
4. Ensure the effective deployment of services and service components — moving components to target environments while maintaining their integrity, aligning with change and release requirements, and meeting schedule and cost objectives

## Scope

This policy applies to all releases and deployments within the scope of the organization's service management system. It covers:

- Planning, building, testing, and packaging releases from approved changes
- Moving release components to target environments through controlled deployment
- Making deployed components available to users through release enablement
- Verifying that releases and deployments meet acceptance criteria
- Reviewing releases and deployments for success and lessons learned
- Defining and maintaining release and deployment models, strategies, and procedures
- Managing the release schedule in coordination with the change schedule
- Removing services and components from environments when required

This policy does not cover: change authorization (change management), software or infrastructure development (respective development practices), service testing (service validation and testing), configuration item control (service configuration management), or user training (workforce and talent management).

## Principles

### P1. Model-Based Management
<!-- sources: ITIL 4 Release Management §2.2.2, ITIL 4 Deployment Management §2.4.1 -->
The organization shall define release and deployment models for different product and component types. Release models shall specify the target audience, release packaging rules, push/pull conditions, verification criteria, and experimentation terms. Deployment models shall specify the flow through controlled environments, responsibilities, triggers, automation approach, and interactions with other practices. Models provide consistency and repeatability while allowing adaptation to the specific characteristics of each product, service, and component type. An organization may define multiple models for a single product where different markets, consumer types, or service relationships require different approaches.

### P2. Automation and Standardization
<!-- sources: ITIL 4 Release Management §2.2.1, ITIL 4 Deployment Management §5.2, FitSM-2 §PR13 RDM -->
The organization shall automate release and deployment activities where possible. In CI/CD environments, most release and deployment activities — from component verification through deployment execution to release verification — can be automated through pipeline tooling, reducing manual effort and increasing consistency, speed, and reliability. Even in environments that are not fully automated, the organization shall standardize procedures and use tooling to reduce manual errors and improve throughput. The effective use of technology and automation can significantly improve the consistency, agility, and efficiency of the practice.

### P3. Component Integrity
<!-- sources: ITIL 4 Deployment Management §2.4.2 -->
The organization shall maintain the integrity of service components throughout the transition process. Any unauthorized change through manual, process, or technology errors during deployment can negatively impact the objectives and outcomes of changes and releases, often significantly impacting the organization. Deployment models shall include appropriate controls — version control, configuration management, verification steps, and access controls — to ensure that what is deployed matches what was approved and tested.

### P4. User-Centric Release
<!-- sources: ITIL 4 Release Management §2.1, §2.2.4 -->
Releases are user-facing — the definition of release units and the design of release procedures shall consider which components affect users' ability to use the service and their experience. The organization shall plan for user enablement activities including communication, training, and knowledge sharing. The choice between push and pull release approaches shall balance security and regulatory requirements, version consistency, user flexibility, and the organization's ability to support multiple versions simultaneously.

### P5. Controlled Environments
<!-- sources: ITIL 4 Deployment Management §2.2.1 -->
The organization shall maintain defined, controlled environments through which service components move during their lifecycle. Each environment shall have a defined purpose, and the deployment model shall define the flow of components through these environments. Target environment verification shall be performed before deployment to confirm that environments are prepared and meet the requirements for the deployment.

### P6. Aligned Scheduling
<!-- sources: ITIL 4 Release Management §2.3, FitSM-2 §PR13 RDM -->
The organization shall coordinate release and deployment scheduling with the change schedule. Releases shall be planned in alignment with approved change windows and service availability requirements. The release schedule shall be published and made available to all relevant stakeholders — including service owners, incident management, and the service desk — to ensure visibility of planned changes to the live environment.

### P7. Continual Optimization
<!-- sources: ITIL 4 Release Management §2.4.1, ITIL 4 Deployment Management §3.2.2 -->
The organization shall periodically review release and deployment data to identify recurring failures, bottlenecks, and opportunities for further automation or standardization. Release and deployment models shall be updated based on review findings, operational experience, and changing technology. Improvement initiatives shall be registered and tracked through the continual improvement process with an aim to eliminate waste and increase effectiveness and efficiency.

## Mandatory Requirements

### Essential (T2+)

| ID | Requirement |
|----|------------|
| RDM-R01 | All releases shall be planned based on approved changes and defined release and deployment strategies, with the release scope, schedule, and acceptance criteria documented |
| RDM-R02 | Releases shall be classified by type — major, minor, or emergency — using defined criteria, and the applicable release and deployment model shall be determined based on the classification |
| RDM-R03 | Release components shall be assembled into defined release units and tested against acceptance criteria before deployment proceeds |
| RDM-R04 | Deployments shall be planned with defined deployment sequences, resource requirements, target environment verification, and back-out procedures |
| RDM-R05 | Deployed and released components shall be verified against acceptance criteria to confirm that intended outcomes are achieved and no unintended consequences are introduced |
| RDM-R06 | Completed releases shall be reviewed, with findings documented, stakeholders informed, and release records closed. Emergency releases shall have mandatory post-release reviews |
| RDM-R07 | Release and deployment records shall be maintained to provide an audit trail and to support post-implementation reviews, incident correlation, and CMDB updates |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| RDM-R08 | Release and deployment models shall be defined for different product and component types, specifying the release approach, deployment flow, automation level, verification criteria, responsibilities, and back-out approach |
| RDM-R09 | A release schedule shall be maintained, coordinated with the change schedule, and published to all relevant stakeholders |
| RDM-R10 | Release and deployment strategies shall define criteria for identifying different release types and the planning depth, testing approach, and coordination required for each type |
| RDM-R11 | Release and deployment data shall be reported regularly to management and service owners, including volumes, success rates, failure analysis, and trends |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| RDM-R12 | Release and deployment models shall be subject to periodic review and optimization based on release data, deployment failure analysis, operational experience, and improvement initiatives |
| RDM-R13 | Where applicable, the organization shall support controlled experimentation through release techniques — defining conditions, sample audiences, measurement criteria, and rollback procedures |

## Compliance and Review

- This policy shall be reviewed at least annually or following a significant change to the organization's service portfolio, technology landscape, CI/CD adoption, or regulatory environment
- Compliance with this policy shall be assessed through release and deployment reports, success rates, post-release review data, and periodic model reviews
- Non-compliance shall be escalated to the release manager and service management leadership for remediation
- Exceptions to this policy require documented justification and approval from the release manager or senior leadership

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Change Management Policy (PR15) | Change management authorizes changes that are bundled into releases. The change schedule informs release scheduling. Release and deployment outcomes feed post-implementation reviews |
| Service Configuration Management Policy (PR17) | The CMS provides configuration data for release planning and deployment impact assessment. Implemented deployments are reflected in the CMS to maintain accurate configuration records |
| Incident Management Policy (PR11) | Release and deployment information supports incident correlation. Release and deployment failures may be registered as incidents |
| Service Level Management Policy (PR02) | SLAs inform release acceptance criteria, deployment scheduling, and user communication requirements. Release data contributes to SLA achievement reporting |
| Information Security Management Policy (PR09) | Security policies inform deployment controls and release procedures. Security-related releases follow defined procedures with appropriate urgency |
| IT Asset Management Policy (PR18) | Assets are sourced from authorized repositories for deployment. Deployment information updates asset records |
| Continual Improvement Policy (PR24) | Improvement initiatives from release and deployment reviews feed the continual improvement register |
| Service Continuity Management Policy (PR07) | Continuity requirements inform deployment approaches, environment resilience, and rollback procedures |
