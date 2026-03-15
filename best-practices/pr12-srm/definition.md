---
process_id: PR12
process_name: "Service Request Management"
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
  - "ITIL 4: Service Request Management §2–§6"
  - "FitSM-2: §PR9 ISRM (request scope)"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Request Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 SRM §2.1, FitSM-0 §6.71, FitSM-2 §PR9 -->

The purpose of the service request management practice is to support the agreed quality of a service by handling all predefined, user-initiated service requests in an effective and user-friendly manner. A service request is a request from a user or a user's authorized representative that initiates a service action which has been agreed as a normal part of service delivery. Service requests are distinct from incidents — they represent planned, pre-approved actions with known outcomes and tested fulfilment procedures, not unplanned interruptions. The practice ensures that every type of service request has a documented fulfilment model, that requests are processed according to agreed procedures and timeframes, and that fulfilment performance is continually reviewed and improved. Unlike incidents, service requests do not require urgent resolution — they allow for planned fulfilment within agreed timeframes. The practice addresses all four dimensions of service management through request models that define procedures and workflows, roles and responsibilities, automation and tooling, and third-party involvement.

## Scope
<!-- sources: ITIL 4 SRM §2.3, FitSM-2 §PR9 -->

This process covers:

- Managing service request models — creating, testing, deploying, and maintaining predefined fulfilment procedures for each type of service request
- Processing service requests submitted by users or their authorized representatives through any established channel
- Managing the fulfilment of service requests according to agreed models, including approval workflows and multi-team coordination
- Reviewing and continually improving request processing and fulfilment performance

This process does not cover: communicating with users (service desk), resolving incidents (incident management), management and realization of changes to products and services (change management, deployment management, release management), monitoring services and technology (monitoring and event management), management and provision of access to services (information security management), management of the request catalogue as a view of the service catalogue (service catalogue management), creating service request models during product and service design (service design), ongoing management of improvement initiatives (continual improvement).

## Key Concepts
<!-- sources: ITIL 4 SRM §2.2 -->

### 1. Service Request
<!-- sources: ITIL 4 SRM §2.1, §2.2, FitSM-0 §6.71 -->
A request from a user or authorized representative that initiates a service action agreed as a normal part of service delivery. Service requests include four types: requests initiating a service action (performed by the service provider or jointly with the user), requests for information, requests for access to a resource or service, and feedback including compliments and complaints. The defining characteristics are that a service request is user-initiated, requires a service provider action, and has a pre-agreed outcome — meaning the outcome was tested in advance, the approval and fulfilment workflows were pre-approved, staff were trained, and service components were prepared. Service requests are business as usual — results and timelines are understood by customers, users, and operations teams. Service requests contribute to service utility as a key form of service interaction and can serve as differentiators between service offering tiers — higher-tier offerings may include additional requests not available to lower tiers.

### 2. Service Request Model
<!-- sources: ITIL 4 SRM §2.2, §3.2.1, FitSM-2 §PR9 -->
A repeatable, predefined approach to the fulfilment of a particular type of service request. Request models are typically produced during product and service design, tested, and deployed to operations alongside other service components. Each model documents the conditions and procedures for fulfilment across all four dimensions: procedures and workflows (including options and decision points), roles and teams responsible (usually as a RACI matrix), automation and tools used, and third parties involved with supporting agreements. Models range from simple (a single-step information provision) to complex (multi-team, multi-step employee onboarding). Regardless of complexity, the steps should be well-known and tested, enabling the service provider to set clear fulfilment timeframes and communicate status to users. The FitSM concept of standardised service requests serves the same purpose — pre-defined fulfilment workflows identified from service descriptions and SLAs, describing the concrete steps from recording to closure.

### 3. Request Catalogue
<!-- sources: ITIL 4 SRM §2.2 -->
A view of the service catalogue providing details on service requests for existing and new services, made available to users. The request catalogue typically shows: the service to which a request belongs, prerequisites and conditions for initiating the request, information required to submit the request, the applicable approval workflow, target fulfilment time, and other relevant information. The catalogue view should be tailored to the SLAs applicable to the accessing user, so that all information reflects the conditions and targets agreed for that user. The more relevant and accurate the information in the request catalogue, the more efficient fulfilment will be and the higher user satisfaction. The request catalogue is managed by the service catalogue management practice and consumed by service request management.

### 4. Service Requests and Changes
<!-- sources: ITIL 4 SRM §2.2 -->
Service requests may initiate changes to services or their components — these are usually standard changes but can sometimes be normal changes. Whether a service request triggers a change depends on the change typology adopted by the organization. Some requests of a given type may require one or more changes while others of the same type are fulfilled without change management involvement. The correlation between service requests and changes is mandatory — organizations must define which requests require changes as part of their change management practice. This ensures appropriate oversight for requests that modify the technical environment while avoiding unnecessary bureaucracy for requests that do not.

### 5. Fulfilment Workflow
<!-- sources: ITIL 4 SRM §3.2.1, FitSM-2 §PR9 -->
The lifecycle of a service request from submission to closure. A typical fulfilment workflow involves: request categorization (validating prerequisites, checking user eligibility, selecting the appropriate model), model-based fulfilment (assigning teams, following procedures, obtaining approvals, coordinating tasks), and fulfilment review (checking outcomes against the model, collecting user feedback). Multiple practices may contribute to fulfilment — the service desk processes the user query, service request management routes and guides fulfilment, technical teams perform operations, release management makes components available, change management coordinates changes, and information security manages access. The specific practices involved and the procedures for each request type are documented in the request model.

### 6. Fulfilment Authorization
<!-- sources: ITIL 4 SRM §2.1 -->
The approach to approving and authorizing service request fulfilment. Service requests and their fulfilment should be standardized and automated as far as possible. Organizations should establish policies defining which requests can be fulfilled with limited or no additional approvals, enabling streamlined fulfilment for low-risk, high-volume requests. User expectations regarding fulfilment times should be clearly set based on what the organization can realistically deliver. Policies and workflows should also address how to handle requests submitted as service requests that should actually be managed as incidents or changes — ensuring proper redirection without delay.

## Activities
<!-- sources: ITIL 4 SRM §3.2.1, §3.2.2, FitSM-2 §PR9 -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Categorize service requests | Receive service requests through established channels. Check all prerequisites and user eligibility — wholly or partly manually at lower maturity, automatically at higher maturity. Request missing information or paperwork from the user. Select the appropriate service request model based on request characteristics. In automated environments, the system checks prerequisites, contacts users for missing information, and selects models automatically |
| 2 | Initiate and control model-based fulfilment | Assign teams and specialists according to the request model. Follow defined fulfilment procedures — obtaining approvals, coordinating tasks across multiple teams where required, and managing notifications to the user. Control the flow of procedures and track progress against agreed fulfilment timeframes. Update relevant configuration items upon fulfilment where required |
| 3 | Review fulfilment outcomes | Check service request fulfilment against the model — verifying that the desired result has been produced. Collect user feedback and measure satisfaction. The review scope is defined by the model — ranging from a simple satisfaction survey to a detailed internal review for cases where fulfilment deviated from plan or satisfaction is low |
| 4 | Maintain service request models | Identify standardised service request types from service descriptions, SLAs, and operational experience. Document fulfilment procedures — workflows, decision points, roles, automation, and third-party involvement. Test models during service design and transition. Deploy models to operations alongside service components. Maintain step-by-step fulfilment workflows for recurring request types |
| 5 | Manage request catalogue entries | Ensure all service request types are accurately described in the request catalogue — including prerequisites, required information, approval workflows, and fulfilment targets. Verify that catalogue entries reflect the SLA conditions applicable to each user group. Coordinate with service catalogue management to maintain accuracy and currency |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Control ad hoc fulfilment | Handle exceptions where standard fulfilment procedures do not produce the desired result — due to new circumstances, non-standard requirements, or model gaps. Decide whether to proceed with tailored fulfilment or deny the request. Ad hoc fulfilment is an exception and should be treated as such. Record all details as input to the request model review and optimization process — either to extend the model or to add categorization checks that filter such cases |
| 7 | Analyse service request performance | Review service request records, metrics, and fulfilment data over the period. Identify patterns in fulfilment times, exception rates, user satisfaction, and resource utilization. Identify opportunities for new request models and improvements to existing models. Analyse repeating changes from change management that could be formalized as request models |
| 8 | Initiate service request model improvements | Register improvement initiatives and submit them for processing through the continual improvement practice or as change requests. Where proposed model updates require testing, validate effectiveness before deployment. Return unsuccessful updates for further analysis |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 9 | Communicate model updates | When service request models are successfully updated, communicate changes to all relevant stakeholders — including fulfilment teams, service desk agents, service owners, and users. Ensure updated procedures, workflows, and catalogue entries are deployed consistently across all channels |
| 10 | Optimize fulfilment automation and third-party integration | Develop automation for the most popular and routine requests — from fully automated self-service to workflow orchestration across multiple systems and teams. Define standard interfaces for third-party involvement in request fulfilment — specifying data exchange rules, tools, and processes that create a common language in multi-vendor environments. Ensure automation costs and risks are justified by volume and complexity analysis |

## Inputs
<!-- sources: ITIL 4 SRM §3.2.1, §3.2.2, §5.1, FitSM-2 §PR9 -->

| # | Input | Source |
|---|-------|--------|
| 1 | Service request queries (via all channels) | Users, service desk |
| 2 | Service request models | Service design, service request management |
| 3 | Service level agreements | Service level management |
| 4 | Request catalogue and service catalogue | Service catalogue management |
| 5 | Configuration information and CI relationships | Service configuration management |
| 6 | IT asset information | IT asset management |
| 7 | Policies and regulatory requirements | Information security management, compliance |
| 8 | Capacity and performance information | Capacity and performance management |
| 9 | Fulfilment action records and reports | Previous fulfilment cycles |

## Outputs
<!-- sources: ITIL 4 SRM §3.2.1, §3.2.2, FitSM-2 §PR9 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Fulfilled service requests | Users |
| 2 | Fulfilment action records and reports | Measurement and reporting, continual improvement |
| 3 | User satisfaction surveys | Relationship management, service level management |
| 4 | Updated service request models | Service design, operations teams |
| 5 | Updated service request procedures and working instructions | Fulfilment teams, service desk |
| 6 | Change requests (for fulfilment requiring changes) | Change management |
| 7 | Improvement initiatives | Continual improvement |

## Roles
<!-- sources: ITIL 4 SRM §4.1 Table 4.2, §4.2, FitSM-3 §6.9 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Service Request Manager | Manages the service request management practice overall. Accountable for maintaining request models, reviewing fulfilment performance, and initiating improvements. Ensures request catalogue accuracy. Monitors fulfilment progress and identifies SLA violations. Communicates model updates to stakeholders. Requires methods and techniques expertise, understanding of service products and SLAs, and analytical skills for performance review. Corresponds to FitSM process manager ISRM (request scope) | All |
| Service Owner | Accountable for request models related to their services. Participates in model design and testing during service lifecycle. Makes decisions on ad hoc fulfilment where standard models are insufficient. Reviews fulfilment outcomes for their services. Requires understanding of business needs, service architecture, and authority to assign resources. Involved in review and optimization activities | All |
| Fulfilment Agent | Front-line role performing request categorization, model-based fulfilment, and fulfilment coordination. Checks prerequisites and user eligibility. Assigns and tracks fulfilment tasks across teams. Obtains required approvals. Updates configuration items and communicates status to users. Requires knowledge of the organization's products, services, request models, and service catalogue. Corresponds to FitSM case owner (service request owner) | All |

## Key Artefacts
<!-- sources: ITIL 4 SRM §2.2, §3.2, FitSM-2 §PR9 -->

| Artefact | Purpose |
|----------|---------|
| Service Request Record | Record of every service request — capturing submission details, classification, selected model, fulfilment actions, approvals, status updates, resolution, user feedback, and closure confirmation. Foundation for performance analysis and model improvement |
| Service Request Model | Documented predefined approach to fulfilling a particular type of service request — covering procedures and workflows, roles (RACI), automation and tools, third-party involvement, approval requirements, and target fulfilment times |
| Request Catalogue | User-facing view of the service catalogue showing available service requests — including prerequisites, required information, approval workflows, fulfilment targets, and SLA-specific conditions. Managed by service catalogue management, consumed by service request management |
| Fulfilment Performance Report | Periodic report on service request fulfilment performance — covering volumes by type, fulfilment times against SLA targets, exception rates, user satisfaction, automation coverage, and improvement progress |
| Service Request Fulfilment Procedure | Step-by-step working instructions for fulfilling a specific type of service request — derived from and consistent with the service request model. Includes decision points, escalation criteria, and quality checks |

## Process Interfaces
<!-- sources: ITIL 4 SRM §2.3, §3.2, §5.1, FitSM-2 §PR9 -->

| Interface | Relationship |
|-----------|-------------|
| Service Desk (PR10) | Service desk receives user queries, triages them as service requests, and routes them to service request management. Status updates are communicated to users through service desk channels |
| Incident Management (PR11) | Requests incorrectly submitted as service requests are redirected to incident management. Incorrect fulfilment may cause incidents. Shared tooling and team structures are common |
| Change Management (PR15) | Service request fulfilment may trigger standard or normal changes. Change typology defines which requests require changes. Change models may correspond to request models |
| Release & Deployment Management (PR16) | Release management makes service components available to users as part of request fulfilment. Release information supports fulfilment planning |
| Service Catalogue Management (PR05) | Service catalogue management maintains the request catalogue as a view of the service catalogue. Catalogue accuracy directly affects request quality and fulfilment efficiency |
| Service Level Management (PR02) | SLAs define fulfilment targets, user entitlements, and conditions for each request type. Fulfilment performance feeds SLA reviews |
| Service Design (PR04) | Request models are created during service design. Service request management participates in design to ensure models are realistic and accepted by fulfilment teams |
| Information Security Management (PR09) | Security policies govern access provisioning and identity verification in request fulfilment. Access requests are a major category of service requests |
| Service Configuration Management (PR17) | Configuration information supports request categorization and fulfilment. CI updates may be required as part of fulfilment |
| IT Asset Management (PR18) | Asset information supports fulfilment of hardware and software provision requests. Asset records are updated upon fulfilment |
| Continual Improvement (PR24) | Improvement initiatives from performance review are processed through continual improvement |
| Monitoring & Event Management (PR14) | Where user monitoring is delegated by the service provider, service requests may be used to initiate maintenance actions triggered by user-observed events |
