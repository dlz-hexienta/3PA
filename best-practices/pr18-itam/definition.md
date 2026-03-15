---
process_id: PR18
process_name: "IT Asset Management"
category: definition
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: IT Asset Management §2.1–§2.5, §3.2.1–§3.2.3, §4.1, §5, §6"
  - "IT4IT: Cross-cutting Functions"
last_updated: 2026-03-14
status: draft
---

# IT Asset Management — Best Practice Process Definition

## How to Use This Definition

This document defines the IT Asset Management (ITAM) practice — its purpose, key concepts, activities, roles, and interfaces. Content is graduated by maturity tier. Organizations should implement Essential elements first, then layer on Intermediate and Advanced capabilities as the practice matures. ITAM has no dedicated FitSM process — asset-related content in FitSM is distributed across CONFM (CI model) and ISM (information asset inventory). This definition draws primarily from ITIL 4 with IT4IT cross-cutting alignment.

---

## Purpose
<!-- sources: ITIL 4 ITAM §2.1 -->

The purpose of IT asset management is to plan and manage the full lifecycle of all IT assets, helping the organization maximize value, control costs, manage risks, support decision-making about acquisition, re-use, retirement, and disposal, and meet regulatory and contractual requirements. The practice ensures that IT assets and related contracts deliver value at reasonable cost and acceptable risk, that IT assets are secure, reliable, and available, and that information about IT assets is trustworthy, accurate, complete, and available when and where needed.

---

## Key Concepts

### 1. IT Assets and Asset Types
<!-- sources: ITIL 4 ITAM §2.2.1, §2.2.5 -->

IT assets are components of value that the organization acquires, manages, and eventually disposes of throughout a defined lifecycle. Asset types typically include: hardware (end-user devices, network and telecom equipment, datacentre hardware, significant peripherals), software (operating systems, middleware, personal and server applications — across all environments including development, test, staging, production, and training), cloud services (IaaS, PaaS, SaaS — increasingly replacing hardware and some software), and data (organizations may choose to manage information and data as IT assets). IT assets may also be financial or fixed assets — requiring reconciliation between the IT and financial perspectives. SAM (software asset management) is a subset of ITAM; both hardware and software ITAM have been part of the practice from the beginning, with cloud services increasingly integrated to avoid uncontrolled cost growth and software non-compliance.

### 2. IT Asset Lifecycle
<!-- sources: ITIL 4 ITAM §2.2.6 -->

The IT asset lifecycle consists of stages represented by statuses and permitted status transitions, tailored for each asset type. Six stages: (1) planning and budgeting — assessing needs, selecting acquisition methods, budgeting with procurement and finance; (2) acquisition — triggered by approved procurement request, capturing all documentation (license, warranty, maintenance, invoices, proof of purchase); (3) assignment (IMAC — install, move, add, change) — delegating responsibility to a consumer, logging in the register; (4) utilization optimization — understanding contracts and pricing models, adapting stock to SLAs, monitoring for underuse, tracking key dates; (5) decommissioning — retrieving assets from consumers, data handling per security policy, deciding reuse or disposal; (6) disposal — permanently removing assets through sale, return, donation, or destruction following regulations including e-waste. Different asset types require different handling at each stage — lifecycle models define the type-specific controls and procedures.

### 3. IT Asset Register
<!-- sources: ITIL 4 ITAM §2.2.4 -->

A collection of information about IT assets including ownership, cost, and other key characteristics that makes it possible to maintain the stock count. The data structure includes entities, attributes, relationships, naming standards, lifecycle stages, interfaces between the register and related tools, and role-based access. The register should consider efficient tracking, labelling, inventory, monitoring and reporting, integration with other practices, and data exchange between functional departments. The most efficient way to maintain the register is to embed updates into purchasing and procurement procedures — capturing data as early as possible in the lifecycle reduces the need for dedicated verification and audit activities.

### 4. Software Asset Management and License Compliance
<!-- sources: ITIL 4 ITAM §2.2.2, §2.2.7 -->

Software asset management is a specialist subset of ITAM dealing with the complexity of software licensing — including license models, entitlements, compliance verification, and vendor audit readiness. Proper license management requires software inventory across all environments and platforms (including cloud), collection of all parameters used in licence models, and understanding of deployment techniques. Cloud platforms have significantly reduced the volume of licenses on physical machines while increasing the share of budget on public cloud providers — requiring integration of cloud services into ITAM scope. License compliance ensures the organization meets its contractual obligations and is prepared for vendor audits. Internal audits minimize the financial, operational, and reputational impact of external audits.

### 5. Verification, Audit, and Discovery
<!-- sources: ITIL 4 ITAM §2.2.7, §3.2.3 -->

Verification is a continuous background activity ensuring IT asset data remains accurate; audit is a planned, structured inspection covering data collection, examination, verification, and correction. Discovery locates and identifies IT assets that may exist but are not recorded in the register. Inventory is data collection and clean-up performed to build or verify register data. The register indicates what should be found; inventory and discovery reveal what is found — reconciliation of gaps is fundamental. Audits may be internal or external, scheduled or triggered by events (detection of unauthorized assets, significant changes, vendor milestones). Audit scope includes existing assets, acquisitions, related media, license compliance, and vendor compliance. Corrective actions address discrepancies: unregistered assets, unauthorized assets, missing media, incorrect records.

### 6. Progressive Implementation
<!-- sources: ITIL 4 ITAM §2.2.3 -->

ISO/IEC 19770-1 suggests a progressive approach to ITAM implementation in three tiers: (1) obtaining trustworthy data about IT assets, (2) achieving integrated management of their lifecycle, (3) optimizing efficiency and cost-effectiveness. Scope is defined as a combination of three dimensions: what (IT asset types to manage), where (parts of the organization), and how (process activities with policies and responsibilities). Whether iterative or big-bang, ITAM implementation should be based on organizational needs — scoping and implementation decisions should be verified against the practice objectives to prevent excessive and unjustified efforts and costs.

---

## Activities

### Essential Activities (T2+)

<!-- sources: ITIL 4 ITAM §3.2.1 Tables 3.1–3.2, §3.2.2 Tables 3.3–3.4 -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Analyse stakeholders' requirements and IT asset risks | Analyse and map major hardware, software, and cloud IT assets with related service expenses. Identify the most significant financial, legal, and technical risks and opportunities. Conduct questionnaires, workshops, and interviews with internal and external ITAM stakeholders to form a categorized and prioritized list of requirements aligned with the risk and opportunity register |
| 2 | Define and agree the ITAM approach | Define scope, data structure, lifecycle models, policies, controls, monitoring procedures, and verification and audit principles. Scope covers what asset types, where in the organization, and how activities are governed. Create the IT asset register as part of the data structure definition. Define lifecycle models for each asset type in scope, including type-specific controls, procedures, and compliance requirements |
| 3 | Analyse resources, identify IT assets, and verify lifecycle models | Upon request for a new IT asset, discovery of a new asset, or a change to an existing asset, identify the type and check whether it is in scope. Select the appropriate lifecycle model. The IT asset manager reviews and confirms the model is suitable for the asset |
| 4 | Follow the lifecycle model and manage records | Follow the selected lifecycle model — capturing and updating data in the register at each stage, monitoring the asset, enforcing controls, ensuring ongoing verification, maintaining compliance, and providing up-to-date information and reports to stakeholders for value maximization, cost reduction, risk management, and decision making |
| 5 | Manage lifecycle exceptions | Handle exceptions during the IT asset lifecycle in line with the organization's ITAM approach, compliance regulations, values, and established practices. Document exceptions and review for possible changes to approach, scope, and lifecycle models |

### Intermediate Activities (T2+)

<!-- sources: ITIL 4 ITAM §3.2.1 Tables 3.1–3.2, §3.2.3 Tables 3.5–3.6 -->

| # | Activity | Description |
|---|----------|-------------|
| 6 | Communicate and integrate ITAM approach into value streams | Communicate the defined approach, scope, lifecycle models, and procedures to all stakeholders. Decide the level of formality for training — formal training may be prerequisite for procurement teams, with periodic awareness training for others. Integrate and embed ITAM controls and procedures into other practices and value streams |
| 7 | Plan and execute IT asset audits | Plan audits in response to detected unauthorized or unregistered assets, before significant changes, before vendor milestones, or at planned intervals. Collect data using discovery, inventory, and monitoring tools. Verify collected data against the register — investigate and correct discrepancies including unregistered assets, unauthorized assets, missing media, and incorrect records |
| 8 | Review and adjust the ITAM approach | Monitor and review adoption, compliance, and effectiveness of the agreed approach and procedures — on both event-based and interval-based cycles. Evaluate the impact of new requirements across all four dimensions of service management. Categorize changes by implementation complexity. Feed results and findings into continual improvement |

### Advanced Activities (T3)

<!-- sources: ITIL 4 ITAM §3.2.3 Tables 3.5–3.6, §2.4.2 -->

| # | Activity | Description |
|---|----------|-------------|
| 9 | Review and analyse audit findings and optimize utilization | Review audit results to drive improvements — analyse risks, assess compliance, optimize costs, identify trends in utilization, and evaluate approach adoption. Initiate improvements including automation of repetitive tasks, simplification of solutions, better operational integration, and optimization of register structure |
| 10 | Compose audit reports and drive cost optimization | Formalize audit reports with stakeholders, distribute through agreed channels, and safely store for future reuse. Appoint owners for post-audit actions with sufficient time and authority. Combine utilization monitoring data with industry development trends to optimize contracts, decrease ownership and utilization costs, and improve financial performance |

---

## Inputs

<!-- sources: ITIL 4 ITAM §3.2.1 Table 3.1, §3.2.2 Table 3.3, §3.2.3 Table 3.5 -->

| # | Input | Source |
|---|-------|--------|
| 1 | IT strategy and plans | Service Portfolio Management (PR01) |
| 2 | List of prioritized IT services | Service Portfolio Management (PR01) |
| 3 | Risk registers | Risk Management (PR21) |
| 4 | Industry and vendor trends | Supplier Management (PR23) |
| 5 | Organization policies and compliance requirements | Information Security Management (PR09) |
| 6 | IT asset monitoring reports | Monitoring & Event Management (PR14) |
| 7 | IT asset register (existing data) | IT Asset Management (PR18) |
| 8 | ITAM and ITSM tool capabilities | Internal |
| 9 | Internal and external compliance regulations | Legal / Regulatory |

## Outputs

<!-- sources: ITIL 4 ITAM §3.2.1 Table 3.1, §3.2.2 Table 3.3, §3.2.3 Table 3.5 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | ITAM approach document | All stakeholders |
| 2 | Updated IT asset register | All practices requiring asset data |
| 3 | ITAM communications and knowledge materials | Workforce, stakeholders |
| 4 | Requests for changes and implementation initiatives | Change Management (PR15) |
| 5 | ITAM approach performance reports | Management, Continual Improvement (PR24) |
| 6 | IT asset utilization optimization initiatives | Service Financial Management (PR03) |
| 7 | Exception reports | IT Asset Manager, management |
| 8 | IT asset lifecycle reports | Service Portfolio Management (PR01) |
| 9 | IT asset audit reports | Management, Compliance, Supplier Management (PR23) |

---

## Roles

<!-- sources: ITIL 4 ITAM §4.1.1–§4.1.5, §4.1 Table 4.2 -->

| Abbreviation | Role | Description | Tier |
|-------------|------|-------------|------|
| ITAM | IT Asset Manager | Oversees the IT asset lifecycle with related data for all IT assets in scope. Manages the ITAM approach, communicates procedures, integrates ITAM into value streams, makes scoping decisions, handles exceptions, ensures register data validity and compliance, participates in risk management, liaises with monitoring, optimizes utilization, and reports on ITAM and compliance. Role may be specialized by asset type (software, hardware, cloud). Competency profile: TMCA for approach activities, TCA for lifecycle activities | T2+ |
| LM | License Manager | Subject matter expert for all licensing aspects related to software and cloud products — including stock of available licenses, compliance with license terms, and vendor audit readiness. Collaborates with supplier and contract management to ensure IT-asset-related contracts are appropriate in terms of cost-value balance and compliance. Due to license model complexity, the role may be dedicated to a specific platform type or software publisher. Commonly combined with the software IT asset manager role | T2+ |
| AO | IT Asset Owner | The organizational entity that holds rights to the IT asset and sponsors the asset throughout its lifecycle. Makes decisions about asset inclusion in scope, acquisition methods, assignment policies, and disposal. Validates that ITAM procedures serve the organization's interests. In the ITAM practice, also encompasses custodianship — ensuring the right utilization of assets and consistent application of ITAM procedures | T2+ |

---

## Artefacts

<!-- sources: ITIL 4 ITAM §2.2.4, §2.2.6.7, §3.2.1, §3.2.3 -->

| # | Artefact | Description | Tier |
|---|----------|-------------|------|
| 1 | IT Asset Register | Collection of information about IT assets including ownership, cost, key characteristics, lifecycle status, and relationships. Enables stock count, utilization tracking, compliance verification, and reporting | T2+ |
| 2 | ITAM Approach Document | Defines scope, data structure, lifecycle models, policies, controls, monitoring procedures, audit principles, and organizational structure for ITAM. Based on stakeholder requirements and organizational needs | T2+ |
| 3 | IT Asset Lifecycle Models | Type-specific definitions of controls, procedures, compliance requirements, monitoring methods, and audit approaches for each lifecycle stage — tailored to hardware, software, cloud, and other asset types | T2+ |
| 4 | IT Asset Audit Reports | Documented results of verification and audit activities — including findings, discrepancies, corrective actions, compliance status, utilization analysis, and recommendations for improvement | T2+ |
| 5 | IT Asset Utilization Reports | Analysis of asset utilization data — identifying underused assets, redundant contracts, excessive license pools, optimization opportunities, and financial performance metrics | T3 |

---

## Interfaces

<!-- sources: ITIL 4 ITAM §2.3 Table 2.2, §6 -->

| # | Process | Interface Description | Direction |
|---|---------|----------------------|-----------|
| 1 | Service Configuration Management (PR17) | CI attributes and relationships in the CMDB — IT asset register and CMDB should be reconciled with clear data synchronization rules | Bidirectional |
| 2 | Service Financial Management (PR03) | Budgeting, accounting, and financial analysis of IT asset data in the context of products and services — reconciliation between IT asset and fixed asset registers | Bidirectional |
| 3 | Supplier Management (PR23) | Sourcing and procuring IT assets, managing vendor contracts, ensuring alignment between ITAM policies and supplier contracts, coordinating vendor audits | Bidirectional |
| 4 | Change Management (PR15) | Analysing impacts of changes involving IT assets, authorizing and planning changes requiring asset assignment or decommissioning | Outbound |
| 5 | Incident Management (PR11) | Fixing IT asset technical issues, detecting stolen or lost assets, triggering decommissioning of failed assets | Outbound |
| 6 | Problem Management (PR13) | Defining spare requirements considering SLAs and potential incidents, requesting replacements when reliability is insufficient | Outbound |
| 7 | Service Level Management (PR02) | Defining minimum stock levels to meet provisioning obligations in SLAs, ensuring service contracts appropriately support SLAs, aligning asset contracts with SLAs | Bidirectional |
| 8 | Information Security Management (PR09) | Securing access to IT asset data, defining procedures for stolen or lost assets, data handling at decommissioning and disposal | Bidirectional |
| 9 | Service Continuity Management (PR07) | Defining required IT assets for service continuity plans, protecting IT assets in case of disaster | Outbound |
| 10 | Service Request Management (PR12) | Managing service requests to provide, move, change, recover, or reclaim IT assets — IMAC fulfilment | Inbound |
| 11 | Monitoring & Event Management (PR14) | Monitoring IT asset utilization, discovery of unregistered assets, detecting deviations from policies and controls | Inbound |
| 12 | Service Catalogue Management (PR05) | Managing the request catalogue with related IT assets, defining service pricing for cost-efficient usage | Bidirectional |
