---
process_id: PR17
process_name: "Service Configuration Management"
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
  - "ITIL 4: Service Configuration Management §2–§6"
  - "FitSM-2: §PR11 CONFM"
  - "IT4IT: Cross-cutting (CMDB/CMS)"
last_updated: 2026-03-13
status: draft
---

# Service Configuration Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Service Configuration Management §2.1, §2.4, FitSM-2 §PR11 CONFM -->

The organization shall maintain accurate, reliable, and up-to-date information about the configuration of its services and the configuration items (CIs) that support them. This information shall be held in one or more configuration management databases (CMDBs) and made available to all service management processes and stakeholders that depend on it. The organization shall define which components are managed as CIs, at what level of detail, and shall establish systematic processes for recording, maintaining, and verifying configuration data. The cost of maintaining configuration information shall be continually balanced against the value it provides to the organization's decision-making, with scope and detail adjusted to ensure that only information that genuinely supports effective service management is collected and maintained.

## Objectives
<!-- sources: ITIL 4 Service Configuration Management §2.4 PSF1–PSF2, FitSM-2 §PR11 CONFM -->

1. Ensure that the organization has relevant, accurate, and timely configuration information available to support effective decision-making across all service management processes — including impact analysis, root cause investigation, change planning, risk assessment, cost allocation, and availability analysis
2. Maintain a logical model of all CIs and their relationships in the CMDB, providing a trusted single source of configuration truth for the organization
3. Define and maintain CI models that ensure consistent management of CIs of the same type across their full lifecycle
4. Verify that configuration information held in the CMDB accurately reflects the actual state of the infrastructure and services, and correct discrepancies promptly
5. Continually optimize the cost of service configuration management by ensuring that the scope, detail level, and tooling are proportionate to the value of the configuration information produced
6. Integrate configuration management into all relevant value streams and practices so that configuration data is captured and consumed as a natural part of service management activities

## Scope

This policy applies to all components that the organization manages as configuration items in the course of delivering and supporting its services. It covers:

- All CI types across the four dimensions of service management: information and technology, partners and suppliers, organizations and people, and value streams and processes
- All configuration management activities: defining scope and CI models, recording and maintaining CI data, verifying CMDB accuracy, and producing configuration information for stakeholders
- All roles with responsibility for configuration management, from the configuration manager through to resource owners
- All tools and data sources that form part of the configuration management system (CMS)
- All third parties (partners, suppliers) whose resources are managed as CIs or who contribute to the organization's configuration data

## Principles

### P1. Value-Driven Scope
<!-- sources: ITIL 4 Service Configuration Management §2.4.1 -->
The scope of configuration management — which components are managed as CIs and at what level of detail — shall be determined by the value the resulting information provides to the organization. Before adding a CI type or increasing the detail level, the organization shall assess whether the configuration information will be used for impact analysis, cause/effect analysis, risk analysis, cost allocation, or availability analysis. If the information does not demonstrably serve at least one of these purposes, it should not be collected.

### P2. Trustworthy Data
<!-- sources: ITIL 4 Service Configuration Management §2.4 PSF1, FitSM-2 §PR11 CONFM -->
Configuration information shall be treated as a shared organizational asset whose value depends entirely on its accuracy and completeness. All processes and roles that create, modify, or consume configuration data share responsibility for its quality. The organization shall establish verification mechanisms to detect and correct data quality issues, and shall not rely on unverified configuration data for critical decisions.

### P3. Cost Optimization
<!-- sources: ITIL 4 Service Configuration Management §2.4 PSF2, §2.4.2 -->
The direct and indirect costs of service configuration management shall be continually optimized. The organization shall avoid the twin traps of maintaining too little configuration information (leading to poor decisions and uncontrolled infrastructure) and too much (leading to excessive maintenance burden and data quality decay). Automation, existing data sources, and integration with other tools shall be leveraged to reduce the cost of maintaining accurate data.

### P4. Start Where You Are
<!-- sources: ITIL 4 Service Configuration Management §2.4.2 -->
Configuration management shall build on existing information sources rather than starting from scratch. The organization shall identify what configuration data already exists in discovery tools, monitoring systems, asset registers, service management records, and supplier systems, and integrate these sources before creating new data collection processes. Incremental improvement is preferred over large-scale CMDB population projects.

### P5. Consistency Through CI Models
<!-- sources: ITIL 4 Service Configuration Management §2.2.2 -->
CIs of the same type shall be managed consistently through defined CI models. Each CI model shall specify naming conventions, key attributes, key relationships, lifecycle stages, verification procedures, and ownership. CI models ensure that configuration data is predictable, comparable, and usable across the organization regardless of who created or maintains the CI records.

### P6. Verification, Not Assumption
<!-- sources: ITIL 4 Service Configuration Management §2.2.5, FitSM-2 §PR11 CONFM -->
The accuracy of CMDB data shall be verified through systematic comparison with the actual state of the infrastructure, not assumed to be correct because processes were followed. Verification shall detect unregistered CIs, missing updates from authorized changes, and unauthorized changes. The organization shall define appropriate responses for each category of discrepancy.

### P7. Integration Over Isolation
<!-- sources: ITIL 4 Service Configuration Management §3.1, FitSM-2 §PR11 CONFM -->
Configuration management shall be embedded in the organization's value streams and practices rather than operated as an isolated discipline. CI records shall be created and updated as a natural part of change, release, and deployment activities. Configuration information shall be consumed by incident, problem, availability, and other processes through integrated tools and procedures, not through manual data requests.

## Mandatory Requirements

### Essential (All Tiers)

| ID | Requirement |
|----|------------|
| SCFGM-R01 | A CMDB shall be established and maintained, containing records for all CIs defined as in scope |
| SCFGM-R02 | The scope of configuration management shall be documented, defining which component types are managed as CIs and at what level of detail |
| SCFGM-R03 | CI types, key attributes, and key relationships shall be defined for all CIs in scope |
| SCFGM-R04 | All CIs shall be uniquely identified using a defined naming convention |
| SCFGM-R05 | CI records shall be created or updated as part of the change and deployment process — no CI shall be deployed, modified, or retired without updating the CMDB |
| SCFGM-R06 | Periodic verification of CMDB data against actual state shall be performed, with discrepancies identified and corrected |
| SCFGM-R07 | A configuration manager role shall be assigned with accountability for the accuracy and completeness of the CMDB |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| SCFGM-R08 | A formal CI models library shall be maintained, covering all CI types in scope with defined naming conventions, attributes, relationships, lifecycle stages, and ownership |
| SCFGM-R09 | Configuration baselines shall be established and maintained for critical services and infrastructure components |
| SCFGM-R10 | Scheduled CMDB verification cycles shall be executed at defined intervals, producing documented verification reports with tracked corrective actions |
| SCFGM-R11 | The SCM approach shall be formally documented and integrated into change, release, and incident management workflows |
| SCFGM-R12 | Stakeholder requirements for configuration information shall be periodically reviewed and the SCM approach adjusted accordingly |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| SCFGM-R13 | Automated CI discovery and CMDB reconciliation shall be deployed for all critical infrastructure |
| SCFGM-R14 | An integrated CMS shall be implemented combining the CMDB with discovery, monitoring, and service management data sources |
| SCFGM-R15 | Service configuration models shall be maintained for critical services, enabling automated impact analysis, risk assessment, and cost allocation |
| SCFGM-R16 | Cross-supplier configuration management arrangements shall be established for all suppliers whose resources are managed as CIs or who provide dependencies for organizational services |

## Compliance and Review

- This policy shall be reviewed at least annually or following a significant change to the organization's service portfolio, technology landscape, or organizational structure
- Compliance with this policy shall be verified through CMDB verification reports and periodic assessment of the SCM approach
- Non-compliance shall be escalated to the configuration manager for remediation
- Exceptions to this policy require documented justification and approval from the configuration manager (or CISO/CIO for exceptions affecting security or governance requirements)

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Change Management Policy (PR15) | Changes trigger CI record updates; configuration information supports change impact assessment |
| Release & Deployment Management Policy (PR16) | Deployments create or modify CIs; configuration information supports release verification |
| IT Asset Management Policy (PR18) | Asset lifecycle data feeds CI records; CMDB provides service context for asset decisions |
| Incident Management Policy (PR11) | Configuration information enables incident impact assessment and root cause investigation |
| Problem Management Policy (PR13) | Configuration models support cause/effect analysis and infrastructure pattern identification |
| Availability Management Policy (PR06) | Service configuration models identify single points of failure and dependency chains |
| Information Security Management Policy (PR09) | CMDB provides asset and relationship data for security risk assessment |
| Service Continuity Management Policy (PR07) | Configuration baselines and service models support recovery planning |
| Supplier Management Policy (PR23) | Supplier CIs must be recorded; configuration information supports supplier risk assessment |
| Monitoring & Event Management Policy (PR14) | Discovery and monitoring tools feed actual-state data into the CMS |
| Continual Improvement Policy (PR24) | Verification findings and approach review outcomes drive improvement initiatives |
