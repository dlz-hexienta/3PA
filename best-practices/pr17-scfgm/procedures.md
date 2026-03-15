---
process_id: PR17
process_name: "Service Configuration Management"
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
  - "ITIL 4: Service Configuration Management §3.2.1–§3.2.3, §2.2.2, §2.2.5, §6"
  - "FitSM-2: §PR11 CONFM"
  - "IT4IT: Cross-cutting (CMDB/CMS)"
last_updated: 2026-03-13
status: draft
---

# Service Configuration Management — Best Practice Procedures

## PROC-SCFGM-01: Establish the Service Configuration Management Approach

**Maturity:** Essential | **Trigger:** Initial process establishment, major organizational change, significant change to service portfolio or technology landscape

### Steps
<!-- sources: ITIL 4 Service Configuration Management §3.2.1 Tables 3.1/3.2, FitSM-2 §PR11 CONFM initial setup -->

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Analyse stakeholder requirements for configuration information: identify who needs configuration data (incident management, change management, availability management, service owners, management), what information they need, in what format, and for what purpose | Configuration Manager | — |
| 2 | Define the scope of configuration management: determine which component types will be managed as CIs and at what level of detail. For each potential CI type, assess whether the configuration information will be used for impact analysis, cause/effect analysis, risk analysis, cost allocation, or availability analysis — if not, exclude it from scope | Configuration Manager | — |
| 3 | Identify existing sources of configuration information: survey what configuration data already exists in discovery tools, monitoring systems, asset registers, service management records, supplier systems, and manual documentation | Configuration Manager | — |
| 4 | Define CI types, attributes, and relationships: for each CI type in scope, specify the key attributes to record, the relationships to track (dependencies, containment, functional associations), and the naming conventions to follow | Configuration Manager | CI Type Definitions |
| 5 | Define the integration concept: determine how configuration data will be captured (manual entry, automated discovery, integration with other tools), how the CMDB will integrate with other data sources, and how configuration information will be provided to consumers | Configuration Manager | — |
| 6 | Document the SCM approach: compile the scope, CI type definitions, naming conventions, tool usage, data sources, integration points, verification schedule, and role responsibilities into a single SCM approach document | Configuration Manager | SCM Approach Document |
| 7 | Communicate the approach and integrate into value streams: ensure all relevant practices and teams understand when and how to interact with configuration management — embedding CI registration, updates, and verification into change, release, incident, and other workflows | Configuration Manager / Configuration Coordinator | Communications |

### Exit Criteria
- Stakeholder requirements for configuration information documented
- Scope defined: CI types, detail levels, and exclusions agreed
- Existing information sources identified and assessed
- CI types defined with attributes, relationships, and naming conventions
- SCM approach documented and communicated to all relevant parties
- Configuration management activities integrated into relevant workflows

---

## PROC-SCFGM-02: Register and Maintain Configuration Items

**Maturity:** Essential | **Trigger:** New CI deployed, existing CI modified (attributes, relationships, or configuration changed), CI retired, CI relationship changed

### Steps
<!-- sources: ITIL 4 Service Configuration Management §3.2.2 Tables 3.3/3.4, FitSM-2 §PR11 CONFM ongoing maintain -->

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Identify the applicable CI model for the resource: determine which CI type the component belongs to and confirm the CI model that governs its management | Configuration Coordinator / Configuration Librarian | — |
| 2 | Confirm the CI model is appropriate: verify that the CI model's attributes, relationships, and lifecycle stages adequately represent the resource. If the CI model does not fit, raise an exception (see step 6) | Configuration Coordinator / Configuration Librarian | — |
| 3 | Create or update the CI record in the CMDB: apply the naming convention, populate all required attributes, establish relationships to other CIs (dependencies, containment, functional associations), and set the lifecycle stage | Configuration Librarian / Resource Owner | Updated CMDB |
| 4 | Record the lifecycle stage transition if applicable: when a CI moves from one lifecycle stage to another (e.g., from deployment to live, from live to retired), update the lifecycle status and record the transition date | Configuration Librarian | Updated CMDB |
| 5 | Validate the CI record for completeness and accuracy: confirm that all required attributes are populated, relationships are correct, and the naming convention is followed | Configuration Coordinator / Configuration Librarian | — |
| 6 | **For exceptions:** If the resource does not fit an existing CI model, assess whether the exception is temporary (document the rationale and proceed with the closest applicable model) or whether it indicates a need for a new or modified CI model (escalate to the configuration manager for CI model review) | Configuration Manager | Exception Report |

### Exit Criteria
- CI record created or updated in the CMDB with all required attributes populated
- Relationships to other CIs established and accurate
- Lifecycle stage current and transition recorded
- Naming convention followed
- Exceptions documented and escalated where applicable

---

## PROC-SCFGM-03: Verify Configuration Data

**Maturity:** Essential (ad-hoc) / Intermediate (scheduled formal) | **Trigger:** Scheduled verification cycle, post-deployment verification, suspected data quality issue, audit requirement

### Steps
<!-- sources: ITIL 4 Service Configuration Management §3.2.3 Tables 3.5/3.6, FitSM-2 §PR11 CONFM ongoing verify -->

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Identify the scope of verification: determine which CIs and which aspects of data quality to verify. Identify the applicable CI model(s) and the verification procedures defined within them | Configuration Manager | — |
| 2 | Collect inventory data: use discovery tools, manual inspection, or third-party data to capture the actual state of CIs in scope. This comparison should be automated wherever possible | Configuration Coordinator / Configuration Librarian | Inventory Data |
| 3 | Compare inventory data with CMDB records: identify discrepancies including unregistered CIs (components that exist but are not recorded in the CMDB), unregistered authorized changes (approved changes not reflected in the CMDB), unauthorized changes (modifications made without change management approval), incorrect attributes, and missing or incorrect relationships | Configuration Coordinator / Configuration Librarian | — |
| 4 | Review the verification output: all cases of incompleteness, incorrectness, non-compliance, or unauthorized changes must be reviewed by the configuration manager, resource owner, or other people assigned according to the CI model. Assess each discrepancy for significance and determine the appropriate response | Configuration Manager / Resource Owner | — |
| 5 | Define corrective actions for each discrepancy: determine the appropriate response — update the CMDB to reflect actual state (for authorized changes not yet recorded), correct the actual state to match the baseline (for unauthorized changes), or investigate further (for unresolved discrepancies). Improvement initiatives to the CI model or SCM approach may also be raised | Configuration Manager | — |
| 6 | Implement corrective actions: submit updates to the CMDB, raise change requests for infrastructure corrections, and log improvement initiatives in the continual improvement register | Configuration Coordinator / Configuration Librarian | Updated CMDB, RFCs, Improvement Register Entries |
| 7 | Compose and communicate a CMDB verification report: document the scope verified, discrepancies found (categorized by type), corrective actions taken and outstanding, and improvement recommendations. Distribute to relevant stakeholders | Configuration Manager | CMDB Verification Report |

### Exit Criteria
- All CIs in scope compared against actual state
- All discrepancies categorized, documented, and assessed
- Corrective actions defined for every discrepancy
- Corrective actions implemented or tracked to completion
- CMDB verification report produced and distributed to stakeholders
- Improvement initiatives logged where applicable

---

## PROC-SCFGM-04: Develop and Maintain CI Models

**Maturity:** Intermediate | **Trigger:** New CI type identified, existing CI model review cycle, CI model exception pattern identified, organizational or technology change

### Steps
<!-- sources: ITIL 4 Service Configuration Management §2.2.2, §3.2.2 (review CI model activity) -->

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Identify the need for a new or revised CI model: triggered by a new resource type entering the organization, a pattern of exceptions to an existing model, a scheduled review cycle, or a change in technology or organizational context | Configuration Manager | — |
| 2 | Define the CI model: specify the CI type owner, naming and labelling conventions, key attributes to be recorded, key relationships (both taxonomic — "is a type of", "is a component of" — and functional — "runs on", "depends on", "is used by"), lifecycle stages and permitted transitions | Configuration Manager | — |
| 3 | Define the procedures for identification, control, verification, and audit of CIs governed by this model: how CIs of this type are discovered, how their records are created and maintained, how frequently they are verified, and what audit procedures apply | Configuration Manager | — |
| 4 | Define responsibility assignments: specify who creates, updates, verifies, and reviews CIs of this type — typically the resource owner for domain knowledge and the configuration librarian or coordinator for CMDB operations | Configuration Manager | — |
| 5 | Validate the CI model with the resource owner and relevant stakeholders: confirm that the model captures the information needed by consumers of configuration data and is practical to maintain | Configuration Manager / Resource Owner | — |
| 6 | Publish the CI model to the CI models library and communicate to all relevant parties: ensure that everyone who creates, updates, or consumes CI records of this type knows the model and its procedures | Configuration Manager / Configuration Coordinator | CI Models Library (updated) |
| 7 | Periodically review CI models: at defined intervals (at minimum annually), assess whether each model remains fit for purpose — considering exception rates, stakeholder feedback, technology changes, and the cost-effectiveness of the attributes and relationships maintained | Configuration Manager / Resource Owner | CI Model Review Report |

### Exit Criteria
- CI model documented with all required elements (naming, attributes, relationships, lifecycle, procedures, responsibilities)
- Model validated with resource owners and stakeholders
- Model published to the CI models library
- All relevant parties informed and trained on the model
- Review schedule established

---

## PROC-SCFGM-05: Establish and Maintain Configuration Baselines

**Maturity:** Intermediate | **Trigger:** New critical service enters production, major change to existing critical service, recovery planning requirement, compliance requirement

### Steps
<!-- sources: ITIL 4 Service Configuration Management §2.2.5 -->

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Identify the service or infrastructure component requiring a baseline: typically critical services where unauthorized change detection is essential, services subject to regulatory or compliance requirements, or services requiring a defined recovery point for business continuity | Configuration Manager / Service Owner | — |
| 2 | Capture the current configuration: record the complete configuration state at the defined point in time, including all CI attributes, relationships, software versions, and infrastructure specifications. Use discovery data and CMDB records to ensure completeness | Configuration Coordinator / Configuration Librarian | — |
| 3 | Formally review the captured configuration with the service owner and configuration manager: confirm that it accurately represents the intended and approved configuration of the service or component | Configuration Manager / Service Owner | — |
| 4 | Approve and register the baseline: store it as a formally agreed configuration baseline linked to the relevant service or component CIs in the CMDB. Record the approval date, approver, and the purpose of the baseline | Configuration Manager | Configuration Baseline |
| 5 | Communicate the baseline to change management, release management, and service continuity as a reference point for change assessment, deployment verification, and recovery planning | Configuration Manager | — |
| 6 | Update the baseline following approved major changes: when a change intentionally and significantly alters the configuration of the baselined service or component, capture and approve a new baseline reflecting the post-change state | Configuration Coordinator / Configuration Librarian | Updated Configuration Baseline |
| 7 | Use the baseline for comparison during verification: during CMDB verification activities, compare the actual state of baselined services against their baselines and flag any deviation as a potential unauthorized change requiring investigation | Configuration Coordinator / Configuration Librarian | — |

### Exit Criteria
- Baseline configuration captured and documented
- Baseline formally reviewed and approved
- Baseline registered in the CMDB/CMS with linkage to relevant CIs
- Baseline communicated to change, release, and continuity processes
- Baseline update procedure understood and followed after approved major changes

---

## PROC-SCFGM-06: Coordinate Cross-Supplier Configuration Management

**Maturity:** Advanced | **Trigger:** New supplier onboarding with infrastructure access or CI dependencies, supplier contract renewal, periodic supplier configuration review, integration or federation of CMS

### Steps
<!-- sources: ITIL 4 Service Configuration Management §6 -->

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Assess the configuration management coordination requirements: determine what configuration information needs to be shared based on the type of service relationship and the level of trust. Identify which supplier resources are managed as CIs or are dependencies for organizational services | Configuration Manager | — |
| 2 | Define the configuration data exchange arrangements: determine the level of integration — at minimum, periodic exchange of limited configuration data (CI attributes and relationships relevant to the organization's services); at maximum, wide integration or sharing of CMS access | Configuration Manager | Data Exchange Agreement |
| 3 | Agree on CI models, naming conventions, and data formats: ensure interoperability between the organization's CMDB and the supplier's configuration data. Where the supplier uses different CI models, define the mapping between the two systems | Configuration Manager / Configuration Coordinator | — |
| 4 | Implement the data exchange: establish the integration points, data feeds, or access arrangements as agreed. This may range from manual periodic data exports to automated bidirectional synchronization | Configuration Coordinator | — |
| 5 | Ensure supplier staff integrated into the organization have appropriate CMS access: partners and suppliers working within the organization should have access to the organization's CMS to the extent needed to fulfil their roles | Configuration Manager | — |
| 6 | Verify supplier-provided configuration data through the standard verification process: include supplier CIs in regular verification cycles to ensure the data provided is accurate and current | Configuration Coordinator / Configuration Librarian | CMDB Verification Report (supplier scope) |
| 7 | Review and adjust cross-supplier configuration arrangements: at contract renewal, at periodic review intervals, and following significant changes to the supplier's services or the organization's requirements, reassess the coordination level and update arrangements as needed | Configuration Manager | Updated Data Exchange Agreement |

### Exit Criteria
- Configuration data exchange requirements assessed and agreed
- CI model alignment and data format interoperability established
- Data exchange implemented and operational
- Supplier CIs recorded in the CMDB and included in verification cycles
- Supplier staff with appropriate CMS access where needed
- Periodic review schedule established
