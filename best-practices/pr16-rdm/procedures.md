---
process_id: PR16
process_name: "Release & Deployment Management"
category: procedures
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
  - "ITIL 4: Release Management §3.2.1, §3.2.2"
  - "ITIL 4: Deployment Management §3.2.1, §3.2.2"
  - "FitSM-2: §PR13 RDM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Release & Deployment Management — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the core operational activities — managing the full release and deployment lifecycle from planning through closure, and handling emergency releases through an expedited path. Intermediate procedures add release and deployment model management, release schedule management, and structured reporting. The advanced procedure covers periodic review analysis and optimization of release and deployment models. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (T2+)

### PROC-RDM-01: Manage the Release and Deployment Lifecycle
<!-- sources: ITIL 4 Release Management §3.2.2 (release coordination), ITIL 4 Deployment Management §3.2.1 (deployment process), FitSM-2 §PR13 RDM (release planning, release deployment) -->

**Trigger:** Approved changes ready for inclusion in a release — typically triggered by the change schedule, a product or service owner decision, or a project milestone indicating that a set of changes is ready for release

**Inputs:** Approved changes and change schedule, applicable release and deployment model, configuration information from the CMDB, acceptance and verification criteria, environment details, IT asset information, service level agreements

**Outputs:** Deployed and released services/components, release records, deployment records, release review report, updated release schedule, release communications, information on deployed changes for CMDB updates

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify applicable model and plan the release | Determine the applicable release and deployment model based on the product, service, and change characteristics. Plan the release: define the scope (which approved changes are included), the target audience, the release unit, the schedule, the acceptance criteria, and the communication plan. Coordinate with the change schedule to align timing. For backlog-managed products, the development team assesses which changes are potentially releasable | Release Manager / Service Owner |
| 2 | Build and test the release | Assemble the release components into the defined release unit. Run pre-defined component tests and acceptance verification. In CI/CD environments, this may be automated through the pipeline — each committed change runs through automated tests. Verification may include releasing to a test user group for functional and non-functional tests. If components do not meet acceptance criteria, return to development for remediation | Release Manager / Technical Specialist |
| 3 | Verify release procedures and deployment readiness | Confirm that all prerequisites for the release and deployment model are met — all required resources are available, target environments are prepared and verified, deployment tools and scripts are ready, and back-out procedures are in place. For manual deployments, verify that installation locations meet physical requirements. For automated deployments, verify pipeline configuration. Release execution may start only when all requirements of the selected model are met | Technical Specialist |
| 4 | Execute the deployment | Move the release components to the target environment according to the deployment plan. For automated deployments, this is executed through the CI/CD pipeline. For manual deployments, the technical team installs and activates components according to installation instructions with intermediate checks. Maintain component integrity throughout the transition. If the deployment fails, invoke the back-out plan | Technical Specialist |
| 5 | Execute the release | Make the deployed components available to users. This may involve granting access to user groups, changing application status, enabling feature toggles, or routing service traffic to the environment containing new components. Plan and perform user communications and training where required by the release model. For combined release-deployment approaches, this activity is integrated with deployment execution | Release Manager / Service Owner |
| 6 | Verify the release and deployment | Confirm that all components were deployed and released successfully. Verify against acceptance criteria that the release achieves its intended outcomes. Perform post-deployment health checks. If verification fails, investigate and either remediate or invoke rollback procedures | Release Manager / Technical Specialist |
| 7 | Review and close the release | Conduct a post-release review: assess whether the release achieved intended outcomes, was completed on time and within budget, and introduced any unintended consequences. Gather feedback from users, customers, and involved team members. Document findings and lessons learned. Update release and deployment records, update the CMDB with deployment information, and close the release record. Communicate results to stakeholders | Release Manager / Service Owner |

---

### PROC-RDM-02: Handle Emergency Releases
<!-- sources: ITIL 4 Release Management §2.2.2, ITIL 4 Deployment Management §3.2.1, FitSM-2 §PR13 RDM (emergency releases) -->

**Trigger:** An emergency change requiring immediate deployment — typically triggered by a major incident, urgent security vulnerability, or regulatory mandate with an immediate deadline

**Inputs:** Emergency change authorization, incident records, applicable deployment model, configuration information, emergency release criteria

**Outputs:** Release record (emergency), deployment record, deployed emergency fix, post-release review report, information for CMDB updates

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Confirm emergency classification and plan | Confirm that the change meets the defined emergency release criteria. Identify the release scope — which components must be deployed urgently. Planning is abbreviated but must include: what is being deployed, to which environment, the expected outcome, and the back-out approach | Release Manager |
| 2 | Build and perform expedited testing | Assemble the emergency release. Testing may be reduced in scope but must confirm that the fix addresses the immediate issue and does not introduce critical regressions. In automated environments, the change runs through the standard pipeline tests. The release unit may be incomplete as an exception when the release is urgent | Technical Specialist |
| 3 | Execute the emergency deployment | Deploy the emergency release to the target environment as quickly as possible. Ensure a back-out plan exists, even if simplified. Monitor the deployment closely. If the deployment fails, invoke the back-out plan immediately | Technical Specialist |
| 4 | Execute the emergency release | Make the emergency fix available to users. For push releases (security patches, critical fixes), enable for all affected users without requiring consent. Notify stakeholders and the service desk of the emergency release | Release Manager |
| 5 | Verify the emergency release | Confirm that the emergency fix achieves its intended outcome — the incident is resolved, the vulnerability is mitigated, or the regulatory requirement is met. Perform basic health checks on affected services | Release Manager / Technical Specialist |
| 6 | Complete records | Complete the release and deployment records with all details that were abbreviated during the expedited process — including full acceptance information, authorization documentation, and deployment details. Update the CMDB and the release schedule | Release Manager |
| 7 | Conduct the mandatory post-release review | Conduct a mandatory review of the emergency release. Assess: whether the fix achieved its intended outcome, whether it introduced any unintended consequences, whether the emergency classification was justified, and whether the emergency release procedure worked effectively. Document findings and lessons learned. Identify whether the root cause should be addressed through a normal release or problem investigation to prevent future emergencies | Release Manager / Service Owner |

---

## Intermediate Procedures (T2+)

### PROC-RDM-03: Develop and Maintain Release and Deployment Models
<!-- sources: ITIL 4 Release Management §3.2.1 (release planning process), ITIL 4 Deployment Management §3.2.2 (deployment models development and review), FitSM-2 §PR13 RDM (initial process setup — define release and deployment strategies) -->

**Trigger:** New product or service introduced requiring release and deployment procedures; existing model producing poor outcomes; recurring deployment failures highlighting model inadequacy; change in technology, architecture, or CI/CD capability; periodic model review cycle

**Inputs:** Current release and deployment models, release and deployment records, failure reports, product and service architecture information, service level agreements, policies and regulatory requirements, agreements and contracts with suppliers and partners, feedback from technical teams and service owners

**Outputs:** New or updated release models, new or updated deployment models, updated procedures and automation scripts, communications to affected teams

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Analyse product architecture and service relationships | Together with service owners, architects, and technical teams, analyse the factors that influence release and deployment approaches: the nature of the products and services, the organization's architecture, the main release audiences and relationships, existing SLAs, risk appetite, compliance requirements, technology constraints, the level of control over product components, and sourcing arrangements. Based on the analysis, define a new approach or propose changes to the existing approach | Release Manager / Service Owner |
| 2 | Define or update the release and deployment model | For each model, document: the product and component types it applies to, the release types and matching criteria, the deployment flow through controlled environments, the automation approach, verification and acceptance criteria, push/pull conditions, release unit definitions, back-out procedures, responsibilities, and interactions with other practices and third parties. For deployment models, address all four dimensions: people and teams, tools and automation, value stream activities and controls, and partner/supplier involvement. Perform a risk assessment of the model | Release Manager / Deployment Manager |
| 3 | Validate and test the model | Review the draft model with technical specialists, service owners, and deployment practitioners. Validate that the model is accurate, practical, and provides appropriate controls. For deployment models, test the model — either in a test environment or by closely overseeing the first live deployment using the model. Confirm edge-case handling and workflow. Where testing is not possible, the deployment manager oversees the first live runs of the model | Technical Specialist / Service Owner |
| 4 | Publish and communicate the model | Publish the model in the ITSM tool or knowledge base so that it is available to all relevant roles. Configure pipeline tooling to support the model where applicable — access settings, code support, branching procedures. Communicate the new or updated model to all affected teams. Provide training where the model introduces new workflows | Release Manager |
| 5 | Review models periodically | At defined intervals, review all active release and deployment models for currency and effectiveness. Retire models for products or component types that no longer exist. Update models based on changes to services, technology, CI/CD capabilities, regulations, or operational experience. Use release and deployment review findings as input to the review | Release Manager / Deployment Manager |

---

### PROC-RDM-04: Produce Release and Deployment Reports
<!-- sources: ITIL 4 Release Management §2.5 Table 2.2, ITIL 4 Deployment Management §2.5 Table 2.4 -->

**Trigger:** Scheduled reporting cycle (monthly, quarterly); ad-hoc request from management or service owners; governance or compliance audit preparation

**Inputs:** Release records, deployment records, release schedule data, post-release review reports, incident data related to releases and deployments, pipeline metrics

**Outputs:** Release and deployment reports (regular and ad-hoc), trend analysis data, input to SLA achievement reporting, input to continual improvement

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Extract release and deployment data | Extract data from the ITSM tool and deployment pipeline for the reporting period. Include volumes by release type and deployment model, success and failure rates, timeliness against schedule, incident correlation, emergency release counts, and deployment lead times | Technical Specialist |
| 2 | Analyse trends and patterns | Analyse the data for trends — changes in volumes, shifts in type distribution, products or services with high failure rates, changes in deployment lead times, emergency release patterns, and correlation between deployments and incidents. Compare with previous periods to identify emerging issues or improvements | Release Manager |
| 3 | Compile the report | Produce the report covering: total release and deployment volumes with breakdown by type and model, success rates, mean cycle times and lead times, emergency release count and justifications, release- and deployment-related incidents, schedule adherence, and key observations or recommendations | Release Manager |
| 4 | Distribute the report | Distribute the report to management, service owners, and other relevant stakeholders. Provide release and deployment data to incident management for correlation analysis. Provide input to SLA achievement reporting for service level management. Provide input to governance and compliance reviews as required | Release Manager |

---

## Advanced Procedures (T3)

### PROC-RDM-05: Analyse and Optimize Release and Deployment Models
<!-- sources: ITIL 4 Release Management §3.2.1 (regular review scenario), ITIL 4 Deployment Management §3.2.2 (deployment review and analysis, improvement initiation) -->

**Trigger:** Scheduled periodic review (quarterly or semi-annually); accumulation of release or deployment failures warranting analysis; significant change in CI/CD capability or technology; strategic planning cycle

**Inputs:** Release and deployment records, current models and procedures, failure reports, post-release review reports, stakeholder satisfaction data, incident correlation data, improvement initiative status from previous reviews

**Outputs:** Review analysis report, improvement initiatives registered in the continual improvement register, change requests for model updates, updated models and procedures, communications to affected teams

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Select releases and deployments for review | Select a representative sample for detailed review — prioritizing unsuccessful releases, failed deployments, emergency releases, and instances where the model may have been inadequate. Include both automated and manual releases and deployments to assess the full range of the practice | Release Manager / Service Owner |
| 2 | Analyse failure patterns and bottlenecks | Analyse the selected releases and deployments for patterns: common causes of failure, recurring issues in specific environments or component types, bottlenecks in the lifecycle, and opportunities for further automation or standardization. Assess whether deployment models are frequently overridden or ad-hoc approaches are being used instead of defined models | Release Manager / Deployment Manager |
| 3 | Assess model effectiveness | Evaluate the usage and effectiveness of existing release and deployment models. Identify models with high failure rates, models that are underused, and product or component types that lack appropriate models. Assess whether the level of automation is appropriate and whether the deployment flow through environments is efficient. Evaluate whether release models are meeting the needs of different markets and consumer types | Release Manager / Deployment Manager |
| 4 | Identify and initiate improvements | Based on the analysis, identify specific improvement opportunities — new or updated models, automation of manual steps, changes to environment configurations, improvements to testing procedures, or enhancements to tooling. Register improvement initiatives in the continual improvement register with owners, target dates, and success criteria. For model updates, initiate the model development process (PROC-RDM-03) | Release Manager |
| 5 | Communicate findings and updated models | Communicate the review findings, decisions, and updated models to all affected teams. Ensure that updated models and procedures are published and accessible. Track the measurable impact of improvements on success rates, lead times, and failure rates | Release Manager |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-RDM-01 | Manage the Release and Deployment Lifecycle | T2+ | Approved changes ready for release |
| PROC-RDM-02 | Handle Emergency Releases | T2+ | Emergency change requiring immediate deployment |
| PROC-RDM-03 | Develop and Maintain Release and Deployment Models | T2+ | New product/service; model review; deployment failures; technology change |
| PROC-RDM-04 | Produce Release and Deployment Reports | T2+ | Scheduled reporting cycle; ad-hoc request |
| PROC-RDM-05 | Analyse and Optimize Release and Deployment Models | T3 | Scheduled review; failure accumulation; strategic planning |
