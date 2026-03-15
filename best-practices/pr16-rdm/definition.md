---
process_id: PR16
process_name: "Release & Deployment Management"
category: definition
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
  - "ITIL 4: Release Management §2–§6"
  - "ITIL 4: Deployment Management §2–§6"
  - "FitSM-2: §PR13 RDM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Release & Deployment Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Release Management §2.1, ITIL 4 Deployment Management §2.1, FitSM-2 §PR13 RDM Objective -->

Release and deployment management makes new and changed services and service components available for use by moving them to target environments and enabling user access. The practice bundles approved changes into releases, tests and deploys those releases to live environments, verifies successful deployment, and enables users to consume the new or changed services. It ensures that the integrity of service components is maintained throughout the transition from development to production and that releases are delivered in line with the organization's policies, service agreements, and user requirements.

## Scope
<!-- sources: ITIL 4 Release Management §2.3, ITIL 4 Deployment Management §2.3, FitSM-2 §PR13 RDM -->

This process covers:

- Bundling approved changes into defined release types (major, minor, emergency)
- Planning, building, testing, and packaging releases for deployment
- Moving release components to target environments (development, test, staging, live/production)
- Making deployed components available to users through release enablement activities
- Verifying that releases and deployments meet acceptance criteria and achieve intended outcomes
- Reviewing releases and deployments, documenting lessons learned
- Defining and maintaining release and deployment models, strategies, and procedures
- Managing the release schedule in coordination with the change schedule
- Removing services and components from environments when required

This process does not cover: authorization of changes (change management), development of software or infrastructure components (respective development practices), testing of services and components (service validation and testing), naming, versioning and control of service components (service configuration management), or user training (workforce and talent management). The process begins with approved changes ready for release planning and ends when the release is verified, reviewed, and closed.

**Combined practice note:** This process combines the concerns of release management (making services available to users) and deployment management (moving components to target environments). In traditional environments, release and deployment activities are often closely coupled and managed as a single flow. In modern Agile/DevOps environments with CI/CD pipelines, deployment may be automated and continuous while release management focuses on controlling when and how deployed components are enabled for users — the two may operate as distinct but coordinated activities.

## Key Concepts
<!-- sources: ITIL 4 Release Management §2.2, ITIL 4 Deployment Management §2.2, FitSM-2 §PR13 RDM -->

### 1. Release
<!-- sources: ITIL 4 Release Management §2.2.1 -->
A version of a service or other configuration item, or a collection of configuration items, that is made available for use. A release bundles one or more approved changes into a coherent package for deployment and user enablement.

### 2. Release Type
<!-- sources: FitSM-2 §PR13 RDM (initial process setup) -->
Releases are classified by scope and urgency. Common types include major releases (significant new functionality or large-scale changes), minor releases (small enhancements or fixes), and emergency releases (urgent fixes that bypass normal release planning). The release type determines the level of planning, testing, and coordination required.

### 3. Release Unit
<!-- sources: ITIL 4 Release Management §2.2.3 -->
A pre-defined set of configuration items or parts of configuration items that forms the basic size to be included in a release. Release units define the granularity at which changes are packaged and deployed — for example, a complete application, a module, or an individual component. Release units may differ between initial service releases and subsequent updates, and some release instances may include incomplete release units as an exception when a release is urgent.

### 4. Deployment
<!-- sources: ITIL 4 Deployment Management §2.1 -->
The activity of moving new or changed hardware, software, documentation, or any other service component to a target environment. Deployment moves components between controlled environments (development, test, staging, live/production) but does not in itself make them available to users — that is the function of release management. In combined approaches, deployment and release happen together; in separated approaches, components are deployed first and then released to users as a distinct step.

### 5. Environment
<!-- sources: ITIL 4 Deployment Management §2.2.1 -->
A subset of the IT infrastructure used for a particular purpose. Organizations typically maintain multiple controlled environments — development, integration, test, staging, and live/production — through which service components move during their lifecycle. The number and purpose of environments varies by organization, sourcing approach, and component type. For externally sourced components, development environments may be outside the organization's control; for externally consumed services, control over the live environment may be limited.

### 6. Release Model
<!-- sources: ITIL 4 Release Management §2.2.2 -->
A product-specific model that defines the approach to releasing a particular service or product, including the target user audience, release packaging rules, push/pull conditions, verification and acceptance criteria, and terms for experimentation. An organization may define multiple release models for different products, markets, or consumer types. The release model is influenced by the organization's scope of control over the product — full control over the development and deployment lifecycle allows greater flexibility than reliance on third-party components.

### 7. Deployment Model
<!-- sources: ITIL 4 Deployment Management §2.4.1 -->
A defined approach for deploying specific types of service components to target environments, covering all four dimensions of service management: the people and teams involved, the tools and automation used, the value stream activities and controls, and the involvement of partners and suppliers. Deployment models vary by component type — hardware, vendor-sourced software, in-house-developed software — and by the level of automation. Models define the flow through controlled environments, responsibilities, triggers, and interactions with other practices.

### 8. Push and Pull Release Approaches
<!-- sources: ITIL 4 Release Management §2.2.4 -->
In a push approach, new or changed components are enabled for all users without requiring their consent — users are obliged to use the new version. In a pull approach, new components are made available but users choose whether to adopt them. The choice depends on security and regulatory requirements, the benefits of version consistency versus user flexibility, the organization's ability to support multiple versions simultaneously, and the criticality of the change (security updates are typically pushed).

### 9. Continuous Integration, Continuous Delivery, and Continuous Deployment
<!-- sources: ITIL 4 Release Management §2.2.1, ITIL 4 Deployment Management §2.2.2 -->
A spectrum of automation approaches for integrating, delivering, and deploying service components. Continuous integration automates code integration, building, and testing. Continuous delivery extends this so that built software can be released to production at any time. Continuous deployment further automates the process so that changes flow automatically into production, enabling multiple production deployments per day. The degree of CI/CD adoption fundamentally affects how release and deployment management is practiced — from fully manual planning and coordination to fully automated pipelines with manual intervention only for exceptions.

## Activities
<!-- sources: ITIL 4 Release Management §3.2.1, §3.2.2, ITIL 4 Deployment Management §3.2.1, §3.2.2, FitSM-2 §PR13 RDM -->

### Essential (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Plan the release | Identify approved changes for inclusion in the release based on the applicable release and deployment strategy. Define the release scope, target audience, components, schedule, and acceptance criteria. Coordinate with the change schedule to align release timing with approved change windows |
| 2 | Build and test the release | Assemble the release components into the defined release unit. Test the assembled release against acceptance criteria to confirm it is ready for deployment. Testing may range from automated pipeline tests to formal acceptance testing, depending on the release and deployment model |
| 3 | Plan and prepare the deployment | Schedule the deployment to target environments. Verify that required resources, tools, and personnel are available. Confirm that target environments are prepared and meet the requirements for the deployment. Define the deployment sequence, back-out approach, and communication plan |
| 4 | Execute the deployment | Move the release components to the target environment according to the deployment plan. This may be automated (CI/CD pipeline), semi-automated, or manual depending on the deployment model. Maintain the integrity of components throughout the transition and invoke the back-out plan if the deployment fails |
| 5 | Execute the release | Make the deployed components available to users. This may be as simple as changing an application status or enabling a feature toggle, or as involved as coordinating user communications, training, and staged rollout. For combined release-deployment approaches, this activity is integrated with deployment execution |
| 6 | Verify the release and deployment | Confirm that all components were deployed and released successfully. Verify against the defined acceptance criteria that the release achieves its intended outcomes and that no unintended consequences have been introduced |
| 7 | Review and close the release | Conduct a post-release review to assess outcomes, identify lessons learned, and document any issues. Update release and deployment records. Inform stakeholders of the results. Close the release record |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 8 | Define and maintain release and deployment models | Establish and maintain models that define the approach for releasing and deploying specific product and component types — including release types, deployment flows, automation levels, verification criteria, push/pull conditions, and responsibilities. Review models periodically for effectiveness and update when services, technology, or regulations change |
| 9 | Manage the release schedule | Maintain a forward schedule of planned releases. Coordinate with the change schedule to ensure alignment. Communicate the release schedule to stakeholders including service owners, service desk, and incident management |
| 10 | Produce release and deployment reports | Extract and analyse release and deployment data — volumes by type, success rates, failure analysis, timeliness, and trends. Compile reports for management and service owners. Provide input to continual improvement |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 11 | Analyse and optimize release and deployment models | Review release and deployment data to identify recurring failures, bottlenecks, and opportunities for further automation or standardization. Conduct structured reviews of deployment failures. Initiate improvement actions, update models, and track the measurable impact of changes |
| 12 | Support experimentation through release techniques | Enable hypothesis testing and controlled experimentation using release techniques such as canary releases, blue/green deployments, A/B testing, and feature toggles. Define the conditions, sample audiences, measurement criteria, and rollback procedures for experiments |

## Inputs
<!-- sources: ITIL 4 Release Management §3.2.1, §3.2.2, ITIL 4 Deployment Management §3.2.1, FitSM-2 §PR13 RDM -->

| # | Input | Source |
|---|-------|--------|
| 1 | Approved changes and change schedule | Change management |
| 2 | Release and deployment models and strategies | Internal (release & deployment management) |
| 3 | Configuration information (CMDB) | Service configuration management |
| 4 | Service level agreements | Service level management |
| 5 | Service components and release components | Development teams, suppliers |
| 6 | Acceptance and verification criteria | Service validation & testing, service owners |
| 7 | Environment details and specifications | Infrastructure & platform management |
| 8 | IT asset information and authorized repositories | IT asset management |
| 9 | Policies and regulatory requirements (security, continuity, capacity) | Respective management practices |
| 10 | Product and service architecture information | Architecture management, service design |
| 11 | Release and deployment planning constraints | Project management, service owners |

## Outputs
<!-- sources: ITIL 4 Release Management §3.2.1, §3.2.2, ITIL 4 Deployment Management §3.2.1, §3.2.2, FitSM-2 §PR13 RDM -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Deployed and released services and service components | Users, service consumers |
| 2 | Release records | Change management (for post-implementation review) |
| 3 | Deployment records | Service configuration management, change management |
| 4 | Release schedule (updated) | Change management, incident management, service desk |
| 5 | Release review reports | Continual improvement, change management |
| 6 | Release and deployment communications | Users, service desk, stakeholders |
| 7 | Updated release and deployment models | Internal (release & deployment management) |
| 8 | Improvement initiatives | Continual improvement |
| 9 | Information on deployed changes to CIs | Service configuration management (CMDB updates) |

## Roles
<!-- sources: ITIL 4 Release Management §4.1.1, ITIL 4 Deployment Management §4.1.1, §4.1.2, FitSM-2 §PR13 RDM -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Release Manager | Plans, coordinates, and manages releases and the release schedule. Maintains release models and approaches. Promotes adoption of agreed release approaches across the organization. Reviews release effectiveness and drives practice improvement. In smaller organizations, this role may be combined with the deployment manager role | T2+ |
| Deployment Manager | Plans, coordinates, and manages deployments to target environments. Maintains deployment models and procedures. Ensures the integrity of components throughout the deployment process. Manages deployment resources and monitors deployment performance against defined KPIs. May be combined with the release manager role | T2+ |
| Technical Specialist | Executes deployments to target environments. Performs technical verification of components and environments. Provides technical expertise on deployment feasibility, risks, and procedures. May include internal staff or third-party supplier personnel | T2+ |
| Service Owner | Provides the service-level perspective on releases and deployments affecting their services. Participates in release planning, acceptance decisions, and post-release reviews. May serve as release authority for releases within their service scope | T2+ |

## Key Artefacts
<!-- sources: ITIL 4 Release Management §3.2, §5, ITIL 4 Deployment Management §3.2, §5, FitSM-2 §PR13 RDM -->

| Artefact | Purpose |
|----------|---------|
| Release Record | Documents a specific release instance — components, scope, schedule, acceptance criteria, outcomes, and review findings |
| Deployment Record | Documents a specific deployment — components moved, target environment, execution details, verification results |
| Release Plan | Defines the scope, schedule, components, acceptance criteria, communication plan, and responsibilities for a specific release instance |
| Deployment Plan | Defines the deployment sequence, target environments, resource requirements, back-out approach, and verification steps |
| Release Schedule | Forward schedule of planned releases, coordinated with the change schedule and communicated to stakeholders |
| Release Model | Product-specific model defining the release approach — audience, packaging, push/pull conditions, verification criteria, experimentation terms |
| Deployment Model | Component-type-specific model defining the deployment approach — environment flow, automation level, responsibilities, triggers |
| Release Review Report | Documents the findings of the post-release review — outcomes achieved, issues identified, lessons learned, improvement recommendations |

## Process Interfaces
<!-- sources: ITIL 4 Release Management §2.3, §3, ITIL 4 Deployment Management §2.3, §3, FitSM-2 §PR13 RDM Key Interfaces -->

| Interface | Relationship |
|-----------|-------------|
| Change Management (PR15) | Receives authorized changes for inclusion in releases. The change schedule informs release scheduling. Release and deployment outcomes feed post-implementation reviews. Emergency changes may trigger emergency releases |
| Service Configuration Management (PR17) | Receives configuration data from the CMDB for release planning and deployment impact assessment. Provides information on deployed changes for CMDB updates and introduction of new CI types |
| Incident Management (PR11) | Provides information on planned and recent releases and deployments to support incident correlation and resolution. Release and deployment failures may be registered as incidents |
| Service Validation & Testing | Testing of release components before deployment and verification of deployed components. Provides acceptance criteria and test results that inform release readiness decisions |
| Service Request Management (PR12) | Releases may fulfil service requests. Service request patterns inform release planning and user enablement activities |
| Problem Management (PR13) | Release and deployment failures may trigger problem investigations. Problem resolutions may require changes that are bundled into releases |
| Service Level Management (PR02) | SLAs inform release acceptance criteria, deployment scheduling, and user communication requirements. Release data contributes to SLA achievement reporting |
| IT Asset Management (PR18) | Provides hardware and software assets from authorized repositories and the definitive media library for deployment. Deployment information updates asset records |
| Service Desk (PR10) | Receives release communications and knowledge articles to support users during and after releases. Provides user feedback on releases |
| Information Security Management (PR09) | Security policies and requirements inform deployment controls, environment access, and release procedures. Security-related releases follow defined procedures with appropriate urgency |
| Capacity & Performance Management (PR08) | Capacity constraints inform deployment scheduling and environment preparation. Performance data contributes to deployment verification |
| Continual Improvement (PR24) | Improvement initiatives from release and deployment reviews feed the continual improvement register. Release and deployment model optimization is tracked as improvement work |
| Monitoring & Event Management (PR14) | Provides monitoring data for deployment verification and post-deployment health checks. Monitoring events may trigger deployment rollbacks |
| Knowledge Management (PR19) | Release documentation, procedures, and lessons learned are stored in the knowledge base. Knowledge articles support user enablement and service desk operations |
| Supplier Management (PR23) | Third-party components require coordination with suppliers for deployment timing, compatibility, and support. Supplier contracts define deployment responsibilities and version support commitments |
| Service Continuity Management (PR07) | Continuity requirements inform deployment approaches, environment resilience, and rollback procedures |
