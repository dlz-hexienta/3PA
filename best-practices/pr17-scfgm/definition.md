---
process_id: PR17
process_name: "Service Configuration Management"
category: definition
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
  - "ITIL 4: Service Configuration Management §2–§6"
  - "FitSM-2: §PR11 CONFM"
  - "IT4IT: Cross-cutting (CMDB/CMS)"
last_updated: 2026-03-13
status: draft
---

# Service Configuration Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Service Configuration Management §2.1, FitSM-2 §PR11 CONFM -->

The purpose of Service Configuration Management is to ensure that accurate, reliable, and up-to-date information about the configuration of services and the configuration items (CIs) that support them is available when and where it is needed. This information enables effective decision-making across all service management processes — supporting impact analysis, root cause investigation, risk assessment, cost allocation, change planning, and availability analysis. The process provides and maintains a logical model of CIs and their relationships in one or more configuration management databases (CMDBs), and ensures that the information held is verified against the actual state of the infrastructure and service environment.

## Scope
<!-- sources: ITIL 4 Service Configuration Management §2.2.1, §2.3, FitSM-2 §PR11 CONFM -->

Service Configuration Management covers all components that the organization needs to manage in order to deliver its services. CIs span the four dimensions of service management:

| Dimension | CI Examples |
|-----------|------------|
| **Information and Technology** | Hardware equipment, software applications, virtual infrastructure, databases, storage, network components, endpoints |
| **Partners and Suppliers** | Supplier services, service catalogues, contracts, underpinning agreements, supplier contact records, supplier locations |
| **Organizations and People** | Organizational units, physical locations, staff records (where relevant to service delivery) |
| **Value Streams and Processes** | Process definitions, workflow configurations, automation scripts, runbooks |

In addition, the scope includes **consumer-facing resources** (customer organizations, user groups, customer locations, customer-side technology) and **service agreements** (SLAs, OLAs) where these are managed as CIs.

The process encompasses:
- Defining which components are managed as CIs and at what level of detail
- Recording and maintaining CI attributes, relationships, and lifecycle states in the CMDB
- Producing configuration models that serve as the basis for impact analysis, risk analysis, cost allocation, and availability analysis across other processes
- Verifying that the configuration information held in the CMDB accurately reflects the actual state of the infrastructure and services

### Out of Scope
- Physical management of assets (covered by IT Asset Management, PR18)
- Financial valuation and lifecycle costing of assets (covered by IT Asset Management, PR18)
- Architectural design decisions about technology standards (covered by enterprise/IT architecture management)

## Key Concepts

### 1. Configuration Item (CI)
<!-- sources: ITIL 4 Service Configuration Management §2.1, FitSM-2 §PR11 CONFM -->

A configuration item is any component that needs to be managed in order to deliver an IT service. CIs vary widely in complexity, size, and type — from an entire service or a release package, through to a single hardware module or a software licence. The defining characteristic of a CI is not its nature but whether it needs to be tracked and managed to support effective service delivery. An organization must decide which components justify the overhead of being managed as CIs based on the value the resulting configuration information provides to other processes and stakeholders.

### 2. CI Model
<!-- sources: ITIL 4 Service Configuration Management §2.2.2 -->

A CI model defines the standard rules for managing a particular type of CI. Each CI model specifies: the CI type owner, naming and labelling conventions, key attributes to be recorded, key relationships (both taxonomic — such as "is a type of" — and functional — such as "runs on" or "depends on"), lifecycle stages and transitions, procedures for identification, control, verification, and audit, and the responsibility assignments for maintaining the CI data. CI models serve as the governing blueprint that ensures CIs of the same type are managed consistently across the organization.

### 3. Configuration Management Database (CMDB)
<!-- sources: ITIL 4 Service Configuration Management §2.2.4, FitSM-2 §PR11 CONFM -->

A CMDB is a database used to store configuration records throughout their lifecycle. Each configuration record contains the attributes of a CI and its relationships to other CIs. The CMDB is the primary data store that the process maintains and from which configuration information is provided to stakeholders.

### 4. Configuration Management System (CMS)
<!-- sources: ITIL 4 Service Configuration Management §2.2.4 -->

A CMS is the broader set of tools, data sources, and information used to support service configuration management. A CMS typically combines one or more CMDBs with other data sources (discovery tools, monitoring systems, asset registers, document repositories) and integrations to provide a comprehensive view of the organization's configuration landscape. The CMS is the system of systems through which configuration information is collected, maintained, and made available.

### 5. Configuration Baseline
<!-- sources: ITIL 4 Service Configuration Management §2.2.5 -->

A configuration baseline is a formally reviewed and agreed-upon configuration of a service, product, or infrastructure component at a specific point in time. Baselines serve as a reference point for future activities — including change assessment (comparing proposed changes against the baseline), recovery (restoring to a known-good state), and verification (comparing the actual state against the expected baseline). Baselines are particularly important for critical services where the ability to detect unauthorized changes is essential.

### 6. Verification and Audit
<!-- sources: ITIL 4 Service Configuration Management §2.2.5, FitSM-2 §PR11 CONFM -->

Verification is the continual activity of comparing the configuration information held in the CMDB with the actual state of the infrastructure and services to identify and correct discrepancies. It relies on inventory — the process of collecting data about the actual state of CIs through discovery tools, manual inspection, or third-party data. A CMDB audit is a planned, structured inspection of CIs that assesses the correctness and completeness of the CMDB data. Verification helps identify three categories of gaps: unregistered CIs (components that exist but are not recorded), unregistered authorized changes (approved changes that were not reflected in the CMDB), and unauthorized changes (modifications made without going through change management).

### 7. Configuration Models for Service Analysis
<!-- sources: ITIL 4 Service Configuration Management §2.2.1, §2.4.1 -->

Beyond individual CI records, the CMDB supports the construction of higher-level configuration models that map how CIs compose services. These include service configuration models (which CIs make up a service), service resourcing models (which resources are allocated to which services), and functional and financial models. These models enable five critical analytical capabilities that other processes depend on: impact analysis (what is affected if a CI fails or changes), cause/effect analysis (what caused an incident), risk analysis (what is exposed if a CI is compromised), cost allocation (what does a service cost based on its constituent CIs), and availability analysis (what are the single points of failure).

## Activities

### Essential Activities (All Tiers)
<!-- sources: ITIL 4 Service Configuration Management §3.2.1, §3.2.2, FitSM-2 §PR11 CONFM -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Define the scope of configuration management | Determine which components will be managed as CIs, at what level of detail, and what information will be recorded for each CI type. Balance the value of the configuration information against the cost of maintaining it |
| 2 | Identify CI types, attributes, and relationships | For each category of CI in scope, define the key attributes to record, the relationships to track (dependencies, containment, functional associations), and the naming conventions to follow |
| 3 | Analyse stakeholder requirements for configuration information | Identify who needs configuration information, what information they need, in what format, and for what purpose — ensuring the CMDB serves the actual needs of other processes and decision-makers |
| 4 | Define and agree the service configuration management approach | Establish the overall approach: which CI models apply, what tools and data sources will be used, how configuration data will be captured and maintained, and how the approach integrates with other practices |
| 5 | Record new CIs and maintain existing CI records | When new components are deployed or existing components change, create or update CI records in the CMDB with accurate attributes, relationships, and lifecycle status |
| 6 | Follow CI models for CI lifecycle management | Apply the defined CI model consistently when creating, updating, transitioning, or retiring CIs — ensuring that naming conventions, attribute completeness, relationship accuracy, and lifecycle stage transitions are maintained |
| 7 | Manage CI model exceptions | When a CI does not fit an existing model or when circumstances require deviation from the standard approach, assess the exception, document the rationale, and determine whether a new CI model is needed or a temporary exception is justified |
| 8 | Perform periodic configuration verification | Compare CMDB records against the actual state of the infrastructure to identify discrepancies — including unregistered CIs, missing updates from authorized changes, and unauthorized changes. Trigger corrective actions as needed |

### Intermediate Activities (T2+)
<!-- sources: ITIL 4 Service Configuration Management §3.2.1, §3.2.2, §3.2.3 -->

| # | Activity | Description |
|---|----------|-------------|
| 9 | Communicate and integrate the SCM approach into value streams | Ensure that all relevant practices and teams understand when and how to interact with configuration management — embedding CI registration, updates, and verification into existing workflows for change, release, incident, and other processes |
| 10 | Develop and maintain a CI models library | Create and maintain a formal library of CI models covering all CI types in scope, with defined owners, naming conventions, attribute sets, relationship types, lifecycle stages, and verification procedures |
| 11 | Conduct scheduled CMDB verification and audits | Execute formal verification cycles at defined intervals, comparing CMDB data with inventory data collected through discovery tools or manual inspection. Produce verification reports documenting all findings |
| 12 | Define and implement corrective actions from verification findings | For each discrepancy identified during verification, determine the appropriate corrective action — update the CMDB to reflect actual state, correct the actual state to match the baseline, or investigate unauthorized changes. Track actions through to completion |
| 13 | Maintain configuration baselines for critical services | Establish and maintain formally agreed configuration baselines for services and infrastructure components that require change detection, recovery capability, or compliance evidence |
| 14 | Review and adjust the SCM approach and procedures | Periodically assess whether the SCM approach remains fit for purpose — considering stakeholder feedback, changes to the organization's service landscape, technology changes, and the cost-effectiveness of the current level of configuration management |

### Advanced Activities (T3)
<!-- sources: ITIL 4 Service Configuration Management §2.2.3, §2.2.4, §5.2, §6 -->

| # | Activity | Description |
|---|----------|-------------|
| 15 | Deploy automated CI discovery and CMDB reconciliation | Implement discovery and monitoring tools that automatically detect CIs across the infrastructure, capture their attributes and relationships, and reconcile the discovered data with existing CMDB records — enabling near-real-time accuracy at scale |
| 16 | Implement an integrated CMS with cross-practice data exchange | Build a configuration management system that integrates the CMDB with discovery tools, monitoring systems, asset registers, and service management records — providing a unified view of configuration information across all practices |
| 17 | Build and maintain service configuration models for analytical use | Construct service-level configuration models that map the complete dependency chain from business service through supporting CIs, enabling automated impact analysis, cost modelling, risk assessment, and availability analysis |
| 18 | Coordinate cross-supplier configuration management | Establish agreements and interfaces with suppliers and partners for sharing configuration information, ranging from periodic data exchanges to integrated or federated CMS access — calibrated to the type and trust level of each service relationship |

## Inputs
<!-- sources: ITIL 4 Service Configuration Management Tables 3.1, 3.3, 3.5, FitSM-2 §PR11 CONFM -->

| Input | Source |
|-------|--------|
| Organizational architecture and strategy | Enterprise/IT architecture, strategic planning |
| Stakeholder requirements for configuration information | All service management processes, service owners, management |
| Organizational structure information (teams, locations, reporting lines) | HR, organizational design |
| Service and product portfolios | Service Portfolio Management (PR01) |
| Monitoring and discovery data | Monitoring & Event Management (PR14), discovery tools |
| Service management records (incidents, changes, releases, problems) | Incident (PR11), Change (PR15), Release (PR16), Problem (PR13) |
| Information on changes to CIs (deployments, retirements, modifications) | Change Management (PR15), Release & Deployment (PR16) |
| Inventory data from discovery or manual collection | Discovery tools, manual inspection, third-party data |
| IT asset data (financial, contractual, lifecycle) | IT Asset Management (PR18) |

## Outputs
<!-- sources: ITIL 4 Service Configuration Management Tables 3.1, 3.3, 3.5, FitSM-2 §PR11 CONFM -->

| Output | Consumer |
|--------|----------|
| Up-to-date CMDB as a logical model of all CIs and their relationships | All service management processes |
| Configuration information and reports for stakeholders | Incident (PR11), Problem (PR13), Change (PR15), Availability (PR06), ISM (PR09), and others |
| Service configuration management approach and procedures | Configuration management team, all practices |
| CI models library | Configuration management team, resource owners |
| Configuration baselines | Change (PR15), Release (PR16), Service Continuity (PR07) |
| CMDB verification reports | Configuration manager, management, Continual Improvement (PR24) |
| Exception reports (CIs not fitting existing models) | Configuration manager, CI model owners |
| Requests for changes (to implement corrective actions) | Change Management (PR15) |
| Improvement initiatives (from verification findings or approach reviews) | Continual Improvement (PR24) |

## Roles
<!-- sources: ITIL 4 Service Configuration Management §4.1, §4.2, FitSM-2 §PR11 CONFM -->

| Role | Tier | Responsibilities |
|------|------|-----------------|
| **Configuration Manager** | All | Oversees the SCM approach and CI models for all CIs in scope. Manages the overall CMDB integrity. Decides which resources and resource types to include in scope. Ensures CI models are followed. Reports on configuration management performance. At T1, performs all configuration management activities directly |
| **Configuration Coordinator** | T2+ | Dedicated specialist supporting the configuration manager, focusing on the service configuration management practice within a particular territory, industry, product group, or organizational area. Assists with CI model maintenance, exception management, and stakeholder liaison |
| **Configuration Librarian** | T2+ | Performs day-to-day CMDB maintenance: manually updating configuration data, verifying the CMDB on an ongoing and periodic basis, and processing ad-hoc requests for configuration information. Particularly important in organizations with low levels of automation |
| **Resource Owner** | All | A person or team responsible for a resource or group of resources. Ensures that CI models are consistently applied to their resources throughout the resource lifecycle. Participates in CI model reviews and verification activities for their resources |
| **Service Owner** | All | Consulted when configuration management decisions affect their services. Participates in stakeholder requirements analysis and service configuration model reviews. Receives configuration information and verification reports relevant to their services |

## Artefacts
<!-- sources: ITIL 4 Service Configuration Management §2–§3, §5, FitSM-2 §PR11 CONFM -->

| Artefact | Description | Tier |
|----------|-------------|------|
| **CMDB** | Database storing CI records with attributes, relationships, and lifecycle status for all CIs in scope | All |
| **SCM Approach Document** | Defines the overall approach to service configuration management: scope, CI types, detail levels, tools, data sources, integration with other practices, verification schedule | All |
| **CI Models** | Formal definitions for each CI type specifying naming conventions, key attributes, key relationships, lifecycle stages, verification procedures, and ownership | T2+ (informal at T1) |
| **Configuration Baselines** | Formally agreed configurations of services or infrastructure components at a specific point in time, used as reference for change assessment, recovery, and verification | T2+ |
| **CMDB Verification Reports** | Reports documenting the results of verification activities: discrepancies found, corrective actions taken or proposed, and improvement initiatives identified | T2+ |
| **Exception Reports** | Records of CIs or situations that do not conform to existing CI models, including the rationale for the exception and any resulting model changes | All |
| **Configuration Management System (CMS)** | Integrated set of tools and data sources providing comprehensive configuration information across the organization — combining CMDBs, discovery tools, monitoring data, and service management records | T3 |
| **Service Configuration Models** | Higher-level models mapping how CIs compose services — used for impact analysis, cost allocation, risk analysis, and availability analysis | T3 |

## Process Interfaces
<!-- sources: ITIL 4 Service Configuration Management §2.3 Table 2.1, FitSM-2 §PR11 CONFM -->

| Process | Interface Description |
|---------|-----------------------|
| Change Management (PR15) | **Bidirectional.** Changes trigger CI record updates in the CMDB (input). Configuration information supports change impact assessment and planning (output) |
| Release & Deployment Management (PR16) | **Bidirectional.** Deployments and releases create or modify CIs whose records must be updated (input). Configuration information supports release planning and verification (output) |
| Incident Management (PR11) | **Output.** Configuration information enables incident impact assessment, affected-service identification, and root cause investigation |
| Problem Management (PR13) | **Output.** Configuration models support cause/effect analysis and identification of infrastructure patterns contributing to recurring incidents |
| IT Asset Management (PR18) | **Bidirectional.** Asset lifecycle data feeds CI records (input). CMDB relationships provide service context for asset management decisions (output) |
| Availability Management (PR06) | **Output.** Service configuration models identify single points of failure and dependency chains used in availability analysis |
| Information Security Management (PR09) | **Output.** CMDB provides the asset and relationship data that underpins security risk assessment and impact analysis |
| Service Continuity Management (PR07) | **Output.** Configuration baselines and service models support recovery planning and disaster recovery procedures |
| Supplier Management (PR23) | **Bidirectional.** Supplier-provided CIs must be recorded and maintained in the CMDB (input). Configuration information about supplier dependencies supports supplier risk assessment (output) |
| Monitoring & Event Management (PR14) | **Input.** Discovery and monitoring tools feed actual-state data into the CMS for verification and CMDB updates |
| Continual Improvement (PR24) | **Output.** Verification findings, exception trends, and approach review outcomes feed improvement initiatives |

## Automation Opportunities
<!-- sources: ITIL 4 Service Configuration Management §5.2, Table 5.1 -->

### Process 1: Managing a Common Approach

| Activity | Automation | Impact |
|----------|-----------|--------|
| Analyse stakeholder requirements | Analysis and communication tools for requirements collection, discussion, and prioritization | Medium |
| Define and agree the SCM approach | Analysis tools, CMS tools for workflow modelling and data integration planning | High |
| Communicate and integrate into value streams | CMS tools, discovery/monitoring tools, service management record-keeping tools for cross-practice data exchange | High |
| Review and adjust approach and procedures | Analysis and communication tools, CMS tools for performance data and workflow modelling | High |

### Process 2: Capturing, Managing, and Providing Configuration Information

| Activity | Automation | Impact |
|----------|-----------|--------|
| Analyse resources and identify CIs | CMS tools, discovery/monitoring tools, service management record-keeping tools | High |
| Confirm a CI model | CMS tools, discovery/monitoring tools for data exchange and CI models library navigation | High |
| Follow the CI model | CMS tools, discovery/monitoring tools for automated CI record updates and relationship tracking | High |
| Manage exceptions | CMS tools, discovery/monitoring tools, service management record-keeping tools | High |
| Review the CI model | CMS tools, discovery/monitoring tools for performance data and CI models library | High |

### Process 3: Verifying Configuration Data

| Activity | Automation | Impact |
|----------|-----------|--------|
| Identify a CI model | CMS tools, discovery/monitoring tools, service management record-keeping tools | High |
| Verify configuration data | CMS tools, discovery/monitoring tools for automated comparison; data health monitoring and verification | High |
| Review the verification output | CMS tools, service management record-keeping tools for audit navigation and data health reporting | High |
| Define and implement corrective actions | CMS tools, service management record-keeping tools; configuration baselines library and CI models library | High |
| Compose and communicate a CMDB verification report | CMS tools, service management record-keeping tools, communication tools | Medium |

## Maturity Levels
<!-- sources: ITIL 4 Service Configuration Management §2.4, §2.5, FitSM-2 §PR11 CONFM -->

### Level 1 — Initial
Configuration information is maintained in isolated spreadsheets or individual knowledge. No formal CI model or CMDB exists. Configuration data is gathered reactively when needed for specific incidents or changes. Relationships between components are understood by individuals but not documented systematically.

### Level 2 — Managed
A CMDB is established with defined CI types covering the most critical infrastructure and services. Basic CI models exist (even if informal) defining which attributes and relationships to record. CIs are created and updated as part of change and deployment activities. Periodic manual verification is performed, but may be ad-hoc. A configuration manager role is assigned, potentially combined with other responsibilities.

### Level 3 — Defined
A formal SCM approach document defines scope, CI models, tool usage, and verification schedules. A CI models library covers all CI types in scope with defined naming conventions, attributes, relationships, lifecycle stages, and ownership. Configuration baselines are maintained for critical services. Scheduled CMDB verification cycles produce formal reports with tracked corrective actions. The SCM approach is integrated into change, release, and incident workflows. Dedicated configuration management roles (coordinator, librarian) support the configuration manager.

### Level 4 — Quantitatively Managed
CMDB data quality is measured against defined targets (accuracy rate, verification coverage, time-to-update). Automated discovery tools provide near-real-time CMDB reconciliation. Service configuration models enable automated impact analysis and are actively used by incident, problem, change, and availability management. CMDB verification findings are trended over time to identify systemic data quality issues. Stakeholder satisfaction with configuration information is regularly measured and used to optimize the approach.

### Level 5 — Optimizing
The CMS integrates the CMDB with all relevant data sources (discovery, monitoring, asset management, service management records) into a unified configuration information platform. Configuration models support predictive analysis — identifying potential failures, capacity constraints, and security exposures before they manifest. Cross-supplier configuration management is established with federated or integrated CMS access. The cost of configuration management is continually optimized against the value of the information provided, with automated data quality controls that self-correct common discrepancies.
