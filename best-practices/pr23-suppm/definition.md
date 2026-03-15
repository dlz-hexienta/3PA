---
process_id: PR23
process_name: "Supplier Management"
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
tier_minimum: T2
sources:
  - "ITIL 4: Supplier Management §2–§6"
  - "FitSM-2: §PR8 SUPPM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (supplier coordination)"
last_updated: 2026-03-13
status: draft
---

# Supplier Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Supplier Management §2.1, FitSM-2 §PR8 SUPPM -->

The purpose of Supplier Management is to ensure that the organization's suppliers and their performances are managed appropriately to support the seamless provision of quality products and services. This includes establishing a common approach to sourcing strategy and managing supplier relationships, maintaining a single point of control over active and planned supplier contracts, and creating closer, more collaborative relationships with key suppliers to uncover new value and reduce the risk of failure. The practice enables organizations to define strategies for the use of suppliers' and partners' services, to evaluate and select suppliers, and to ensure that consumed services meet or exceed agreed service levels, that costs are optimal, and that associated risks are understood and controlled. In the context of IT service management, this specifically involves establishing and maintaining healthy relationships with internal and external suppliers and monitoring their performance against agreed targets.

## Scope
<!-- sources: ITIL 4 Supplier Management §2.3, FitSM-2 §PR8 SUPPM -->

The scope of Supplier Management focuses on three key aspects:

- **Supplier evaluation, selection, and onboarding** — evaluating, selecting, and onboarding suppliers, and maintaining their information in supplier management information systems
- **Contract negotiation and management** — negotiating contracts and ensuring that suppliers adhere to them, meeting all contractual obligations and deliverables, and managing the contracts through their lifecycle (creation, amendment, renewal, termination)
- **Supplier performance management** — measuring, tracking, and reporting on supplier performance, and triggering reward or penalty aspects of the contract to ensure that the organization obtains value for money

The extended scope includes:

- Enforcing the supplier management policy
- Creating and maintaining supplier selection and performance evaluation criteria and procedures
- Establishing and maintaining the sourcing strategy and supplier categorization standards
- Defining sourcing requirements and evaluation parameters for supplier selection
- Creating and maintaining standard contract terms and conditions
- Developing, negotiating, agreeing, reviewing, renewing, and terminating contracts
- Auditing suppliers' adherence to contracts and compliance with regulations
- Creating and maintaining supplier onboarding and offboarding procedures
- Collaborating with suppliers and resolving conflicts
- Maintaining data in supplier management information systems
- Categorizing suppliers and managing supplier risk
- Identifying, tracking, and reporting on continual improvement measures

### Related Activities in Other Processes
<!-- sources: ITIL 4 Supplier Management §2.3 Table 2.1 -->

Several closely related activities are managed by other processes:

| Activity | Primary Process |
|----------|---------------|
| Manage stakeholder relationships in supplier relations | Relationship Management (PR22) |
| Document relationships between suppliers' services, the organization's services, and other CIs | Service Configuration Management (PR17) |
| Maintain and provide information on suppliers' services to stakeholders | Service Catalogue Management (PR05) |
| Define the organization's requirements for supporting services | Service Design (PR04) |
| Ongoing management and improvement of supplier performance, driving service improvement | Continual Improvement (PR24) |
| Design and control of financial models for supplier contracts | Service Financial Management (PR03) |
| Manage supplier risks | Risk Management (PR21) |
| Manage supplier-related projects | Project Management |
| Capture and manage supplier knowledge | Knowledge Management (PR19) |
| Manage supplier's access to resources and tools | Information Security Management (PR09) |

## Key Concepts

### 1. Sourcing Strategy
<!-- sources: ITIL 4 Supplier Management §2.4.1, §3.2.1 Table 3.2 -->

The sourcing strategy defines the organization's overall approach to using third-party suppliers and partners. It supports the organizational strategy by defining which resources should be created and managed internally and which should be obtained from third parties, and to what extent. The strategy includes supplier categorization criteria, evaluation and selection criteria, applicable service relationship types, due diligence requirements, contracting standards, compliance and audit requirements, reward and penalty mechanisms, service integration and disintegration options, collaboration guidelines, performance measurement standards, and reporting and communication standards. The strategy can also define whether supplier management is retained internally, delegated to a key supplier, or assigned to a specialized service integrator.

### 2. Supplier Categorization
<!-- sources: ITIL 4 Supplier Management §2.4.2, §3.2.2 Table 3.4 -->

Suppliers are categorized based on their relative importance to the organization, which is determined by the type of service relationship and the associated risks and dependencies. Three broad categories map to the three service relationship types:

| Category | Relationship Type | Characteristics |
|----------|------------------|----------------|
| **Generic / Commodity** | Basic | Standardized off-the-shelf services, operationally focused, transactional, interchangeable suppliers |
| **Operational / Tactical** | Cooperative | Configured or customized services, trusted adviser relationship, operational and tactical involvement |
| **Strategic / Partners** | Partnership | Custom or co-created services, strategic partner relationship, involvement at operational, tactical, and strategic levels |

Categorization ensures that the time and effort spent managing each supplier is proportionate to their significance in the supplier ecosystem. Higher-category suppliers receive more intensive engagement, governance, and performance monitoring.

### 3. Service Relationship Journey — Supplier Side
<!-- sources: ITIL 4 Supplier Management §2.4.2, Table 2.2 -->

When the organization acts as a service consumer, it follows the customer side of the service relationship journey with its suppliers. The journey progresses through defined stages: **explore** (searching and shortlisting potential suppliers), **engage** (assessing, scanning, and vetting suppliers), **offer/agree** (drafting, negotiating, and agreeing contracts), **onboard** (integrating the supplier into the organization's operational context), **co-create** (managing ongoing service delivery, performance monitoring, conflict resolution, and collaboration), and **realize** (evaluating supplier value, conducting reviews, and initiating improvement). Each stage requires specific procedures, skills, information systems, and — for cooperative and partnership relationships — the involvement of external integration services.

### 4. Supplier Contracts and Agreements
<!-- sources: ITIL 4 Supplier Management §2.2, §3.2.2 Table 3.4 -->

A supplier contract typically includes the service level agreement between the organization and the supplier, covering the utility and warranty aspects of the services, terms and conditions, payment schedules, responsibilities and deliverables, performance measurement parameters, and related reward or penalty attributes. Contract management covers the full lifecycle: creation of new contracts, amendment (triggered by requirement changes, technological changes, mergers, new performance metrics, or contract dependencies), renewal, and termination. The type of service relationship dictates the level of formality in contracts — basic relationships rely on standard terms with warranty-focused measures, while cooperative and partnership relationships include broader performance parameters covering innovation, improvement, and collaboration commitments.

### 5. Supplier Performance Measurement
<!-- sources: ITIL 4 Supplier Management §2.2.1, §2.4.1, §3.2.2 Table 3.4 -->

All suppliers must be evaluated and assessed for their performance and value realization against defined performance targets. Performance measurement criteria include performance KPIs and related metrics, expected performance levels for each KPI, the measurement methodology, and the reporting methodology (reports, dashboards, scorecards). The scope of performance measurement varies by relationship type: in basic relationships, measures are restricted to warranty parameters (availability, capacity, service levels); in cooperative relationships, measures extend to all parameters except innovation; in partnership relationships, all parameters apply including innovation, proactive initiatives, and value co-creation. Supplier performance reports and scorecards serve as key inputs to periodic supplier reviews and to decisions on reward, penalty, contract renewal, or termination.

### 6. Supplier Dependency Matrix
<!-- sources: ITIL 4 Supplier Management §2.4.3, §3.2.1 Table 3.1 -->

The supplier dependency matrix maps the relationships between the organization's services and the suppliers that contribute to their delivery. It records which suppliers support which services, the nature of the dependency, and the associated risks. This matrix is critical for understanding the impact of supplier failures on service delivery, for managing supplier onboarding and offboarding (ensuring the mapping is updated when suppliers change), and for making informed sourcing decisions. The matrix is an output of the sourcing strategy process and is updated throughout the supplier journey as suppliers are onboarded, services change, or supplier relationships end.

### 7. Supplier Risk and Compliance
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4, §2.4.1 -->

Supplier risk management is embedded throughout the supplier journey. It includes initial risk reviews and due diligence of potential suppliers during evaluation and selection, ongoing risk management during service delivery (monitoring compliance, conducting audits, maintaining the supplier risk register), and risk assessment during contract renewal or termination decisions. The governance body for supplier management focuses on managing and governing supplier risks, cross-supplier collaboration and service integration, contractual adherence, compliance with internal and external regulations, and the scheduling and conduct of supplier audits. Compliance and audit criteria define the standards against which suppliers are assessed, the audit periodicity, and the actions for non-compliance.

## Activities

### Essential Activities (All organizations implementing this process)
<!-- sources: FitSM-2 §PR8 SUPPM, ITIL 4 Supplier Management §3.2.1, §3.2.2 -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Maintain a supplier database | Establish and maintain a register of all internal and external suppliers with contact details (both on the supplier side and the organization side), contracted services, agreement references, performance data, and relationship status. Add new suppliers, update information, and remove suppliers as relationships end |
| 2 | Define supplier evaluation and selection criteria | Establish the criteria by which potential suppliers will be evaluated and selected — including their service delivery track record, capability, cost, risk profile, credit rating, and alignment with the organization's requirements. Document the evaluation and scoring methodology |
| 3 | Identify, evaluate, and select suppliers | When a sourcing need arises, identify available suppliers in the market, issue RfX documents, evaluate responses against the defined criteria, shortlist candidates, and select the preferred supplier(s) for contract negotiation |
| 4 | Negotiate, agree, and manage supplier contracts | Develop, negotiate, and finalize contracts with selected suppliers covering service descriptions, service levels, terms and conditions, performance baselines, reward and penalty mechanisms, and contract management arrangements. Manage contracts through their lifecycle including amendments, renewals, and terminations |
| 5 | Monitor supplier performance against agreed targets | Collect performance data from suppliers, measure against the agreed KPIs and service levels, produce performance reports and scorecards. Agree follow-up actions with the supplier in response to insufficient performance. Track the implementation of agreed follow-up actions |
| 6 | Conduct periodic supplier reviews | Schedule and conduct regular reviews with suppliers to discuss performance, service quality, contractual compliance, issues, risks, and improvement opportunities. Document outcomes and agreed actions |

### Intermediate Activities (T2+)
<!-- sources: ITIL 4 Supplier Management §3.2.1 Table 3.2, §3.2.2 Table 3.4, §2.4.1 -->

| # | Activity | Description |
|---|----------|-------------|
| 7 | Develop and agree the sourcing strategy | Define the organization's overall approach to sourcing — which resources will be sourced externally, the supplier categorization scheme, evaluation criteria, contracting standards, performance measurement standards, compliance requirements, and collaboration guidelines. Align the strategy with the organization's overall strategy |
| 8 | Develop and agree supplier management procedures | Develop detailed procedures for each stage of the supplier journey — identifying suppliers, engaging and communicating demand, evaluation and selection, contracting, onboarding and offboarding, performance management, compliance and auditing, and supplier assessment and review |
| 9 | Onboard and offboard suppliers | When a new supplier is contracted or an existing supplier's services are terminated, execute the onboarding or offboarding plan. Onboarding covers integrating the supplier's services, processes, people, and tools into the organization's operational context, updating the supplier dependency matrix and service catalogue, categorizing the supplier, managing access, and identifying delivery risks. Offboarding covers revoking access, recovering assets, updating the dependency matrix, notifying stakeholders, and managing the transition to alternative suppliers |
| 10 | Categorize suppliers by importance and relationship type | Classify each supplier according to the sourcing strategy's categorization scheme (generic/commodity, operational/tactical, or strategic/partner) based on the service relationship type, dependency level, and associated risks. Ensure that management effort is proportionate to supplier significance |
| 11 | Manage supplier governance, compliance, and audits | Establish governance structures (governance committees, compliance review meetings) to monitor supplier risk, contractual adherence, and regulatory compliance. Conduct periodic compliance audits. Maintain the supplier risk register. Take corrective action for non-compliance |
| 12 | Communicate and embed the sourcing strategy and procedures | Communicate the agreed sourcing strategy and supplier management procedures to all relevant stakeholders internally and externally. Provide training for staff involved in supplier management. Publish technical integration standards and methods for potential suppliers |

### Advanced Activities (T3)
<!-- sources: ITIL 4 Supplier Management §3.2.1 Table 3.2, §2.4.3, §3.2.2 Table 3.4 -->

| # | Activity | Description |
|---|----------|-------------|
| 13 | Review and adjust the sourcing strategy and procedures | Monitor the adoption, compliance, and effectiveness of the sourcing strategy and supplier management procedures. Review based on supplier-related incidents, conflicts, complaints, and periodic assessment results. Update the strategy and procedures based on lessons learned and changing organizational needs |
| 14 | Manage multi-supplier integration and collaboration | In environments with multiple suppliers contributing to the same services, coordinate cross-supplier collaboration, ensure service integration arrangements are effective, manage cross-supplier dependencies, and include collaboration and integration clauses in contracts. This may involve delegating coordination to a service integrator |
| 15 | Assess supplier value realization and drive improvement | Conduct comprehensive supplier value assessments that go beyond operational performance — evaluating the year-on-year benefit, potential value from innovation, transformation opportunities, and strategic alignment. Use assessment results to drive improvement initiatives in the sourcing strategy, selection procedures, and supplier relationships |

## Inputs
<!-- sources: ITIL 4 Supplier Management Tables 3.1, 3.3, FitSM-2 §PR8 SUPPM -->

| Input | Source |
|-------|--------|
| Organization's strategy and business requirements | Strategic planning, leadership |
| Service relationship type requirements | Service portfolio, service design |
| Budgetary and financial considerations | Service Financial Management (PR03), finance |
| Legal requirements, considerations, and regulations | Legal, compliance |
| Existing supplier management policy and processes | Internal (from previous sourcing cycles) |
| Service specifications and service level requirements | Service Level Management (PR02), service design |
| Service continuity requirements | Service Continuity Management (PR07) |
| Information on suppliers and supplier offerings | Market research, supplier communications |
| OLAs with internal suppliers | Service Level Management (PR02) |
| UAs (underpinning agreements) with external suppliers | Service Level Management (PR02) |
| Supplier performance metrics and reports | Monitoring, supplier performance data |
| Information on internal and external suppliers involved in delivering services | Service Portfolio Management (PR01) |

## Outputs
<!-- sources: ITIL 4 Supplier Management Tables 3.1, 3.3, FitSM-2 §PR8 SUPPM -->

| Output | Consumer |
|--------|----------|
| Sourcing strategy and supplier management policy | All supplier management stakeholders, leadership |
| Supplier evaluation and selection criteria | Sourcing teams, supplier coordinator |
| Contract framework and standard contract terms | Contracts manager, legal |
| Supplier dependency matrix | Service owners, risk management, availability management |
| Compliance and audit criteria | Governance body, supplier coordinator |
| Collaboration framework | Supplier manager, supplier teams |
| RfX documents | Potential suppliers |
| Signed contracts | Supplier, legal, contracts management |
| Up-to-date supplier database | Service Level Management (PR02), Service Portfolio Management (PR01), all consuming processes |
| Supplier evaluation results | Service Level Management (PR02), leadership |
| Supplier performance reports, dashboards, and scorecards | Leadership, service owners, continual improvement |
| Updated supplier risk register | Risk Management (PR21), leadership |
| Improvement initiatives | Continual Improvement (PR24) |

## Roles
<!-- sources: ITIL 4 Supplier Management §4.1.1, §4.1.2, §4.2, FitSM-2 §PR8 SUPPM -->

| Role | Tier | Responsibilities |
|------|------|-----------------|
| **Supplier Manager** | All | Gathers business requirements for outsourcing. Approves prerequisites and criteria for supplier selection. Manages the RfX process (or involves intermediaries). Categorizes suppliers based on importance. Handles due diligence and contract negotiation. Provides direction for onboarding and offboarding. Designs and institutes governance, compliance, and conflict-resolving procedures. Chairs governance and supplier review meetings. Defines, agrees, and implements supplier performance criteria. Monitors performance and publishes supplier reports, dashboards, and scorecards. Provides decisions on conflicts, rewards, penalties, and exceptions. Provides inputs for contract review, renewal, or termination. Orchestrates contract finalization and approvals. At T1, may be combined with the service level manager or service owner |
| **Supplier Coordinator** | T2+ | Formulates prerequisites and collates business requirements for supplier selection. Releases RfX documents to suppliers and communicates selection decisions. Coordinates with stakeholders and assists the supplier manager during the RfX process. Maintains supplier information in supplier management tools. Drafts and publishes agendas and minutes for governance and review meetings. Prepares performance reports and details of pending actions and exceptions. Keeps the supplier risk register. Creates and maintains the supplier dependency matrix. Onboards and offboards suppliers (people, process, services, tools). Feeds updates to the service catalogue. Monitors and audits contractual adherence. Captures requirements for new contracts or amendments |
| **Service Level Manager** | All | Provides OLAs and UAs with operational targets to support supplier performance evaluation. Provides service level requirements as input to supplier selection and contracting. Consults on supplier performance criteria. Participates in supplier reviews where service level performance is discussed |
| **Service Owner** | All | Provides service requirements and specifications as input to sourcing decisions. Participates in supplier evaluation and selection for services they own. Consulted on supplier performance affecting their services. Informed of supplier changes, onboarding, and offboarding relevant to their services |

## Artefacts
<!-- sources: ITIL 4 Supplier Management §3.2.1–§3.2.2, §5.1, FitSM-2 §PR8 SUPPM -->

| Artefact | Description | Tier |
|----------|-------------|------|
| **Supplier Database / SMIS** | Register of all suppliers with contact details, contracted services, agreement references, categorization, performance history, and relationship status | All |
| **Supplier Evaluation and Selection Criteria** | Documented criteria and scoring methodology for evaluating potential suppliers — covering service capability, cost, risk, track record, and organizational alignment | All |
| **Supplier Contracts and Agreements** | Formal contracts with suppliers covering service descriptions, service levels, terms and conditions, performance baselines, reward/penalty mechanisms, and lifecycle management arrangements | All |
| **Supplier Performance Reports** | Reports on individual supplier performance against agreed targets, including KPI achievement, compliance status, and trend analysis | All |
| **Sourcing Strategy** | The organization's documented approach to sourcing — categorization scheme, evaluation standards, contracting principles, performance measurement standards, and integration options | T2+ |
| **Supplier Dependency Matrix** | Mapping of the organization's services to the suppliers that contribute to their delivery, recording dependencies, risks, and the nature of each supplier's contribution | T2+ |
| **Supplier Risk Register** | Register of identified supplier-related risks, their assessment, mitigation actions, and current status — maintained throughout the supplier journey | T2+ |
| **Compliance and Audit Criteria** | Documented standards against which suppliers are assessed for contractual compliance and regulatory adherence, including audit periodicity and actions for non-compliance | T2+ |
| **Supplier Scorecards** | Comprehensive multi-dimensional assessments of supplier performance, value realization, and strategic contribution — used for periodic supplier reviews and sourcing decisions | T3 |

## Process Interfaces
<!-- sources: ITIL 4 Supplier Management §2.3 Table 2.1, FitSM-2 §PR8 SUPPM -->

| Process | Interface Description |
|---------|-----------------------|
| Relationship Management (PR22) | **Parallel.** Supplier relationships follow the same relationship management principles. Relationship management owns the stakeholder engagement approach; supplier management owns the contractual and performance management aspects |
| Service Level Management (PR02) | **Bidirectional.** SLM provides OLAs, UAs, and service level requirements as input to supplier selection and contracting (input). Supplier performance data and evaluation results inform SLA definition, revision, and underpinning agreement management (output) |
| Service Portfolio Management (PR01) | **Bidirectional.** Portfolio decisions drive sourcing needs — new or changed services may require new suppliers (input). Supplier capability and performance information informs portfolio planning (output) |
| Service Configuration Management (PR17) | **Output.** Supplier services and their relationships to the organization's services and CIs are documented in the CMS |
| Service Financial Management (PR03) | **Input.** Budgetary and financial considerations inform sourcing decisions, contract terms, and value-for-money assessments |
| Risk Management (PR21) | **Output.** Supplier risk assessments and the supplier risk register feed into the organization's overall risk management |
| Information Security Management (PR09) | **Bidirectional.** Security requirements inform supplier contracts and access management (input). Supplier access to the organization's resources and tools must be managed in line with security policies (output) |
| Change Management (PR15) | **Bidirectional.** Changes to supplier services or contracts may be triggered by change management (input). Supplier onboarding, offboarding, and contract changes may require formal change control (output) |
| Continual Improvement (PR24) | **Output.** Supplier assessment results and improvement initiatives feed the continual improvement register |
| Knowledge Management (PR19) | **Output.** Supplier knowledge (capabilities, performance history, lessons learned) is captured and managed as knowledge assets |

## Automation Opportunities
<!-- sources: ITIL 4 Supplier Management §5.2 Table 5.1 -->

### Process 1: Managing a Common Approach to Supplier Management

| Activity | Automation | Impact |
|----------|-----------|--------|
| Develop and agree the sourcing strategy | Collaboration and communication tools | Low |
| Develop and agree supplier management procedures | Mind mapping, brainstorming, workflow modelling, and visualization tools | Medium/High |
| Communicate and embed the sourcing strategy and procedures | Communication and collaboration tools, presentation tools, portals | Medium |
| Review and adjust the sourcing strategy and procedures | Collaboration, communication, reporting, and visualization tools | Medium |

### Process 2: Managing Supplier Journeys

| Activity | Automation | Impact |
|----------|-----------|--------|
| Identifying available suppliers | Requirement management tools, market research tools | Low to Medium |
| Engaging with suppliers and communicating demand | Supplier management tools, portals | Medium to High |
| Evaluating and selecting suppliers | Supplier management tools, assessment tools, risk management tools | High |
| Contracting suppliers | Contract management tools, CRM tools, legal/document management tools | Medium |
| On/offboarding suppliers | Communication and collaboration tools, portals, dashboards, knowledge management tools | High |
| Managing consumption and monitoring supplier performance | Communication, collaboration, portals, dashboards, knowledge management, feedback gathering, business analysis, monitoring, and reporting tools | High |
| Assessing and reviewing suppliers | Business analysis, reporting, dashboard, and action tracking tools | Medium |

## Maturity Levels
<!-- sources: ITIL 4 Supplier Management §2.4, FitSM-2 §PR8 SUPPM -->

### Level 1 — Initial
Supplier relationships are managed informally and reactively. There is no formal supplier database or register. Contracts are managed individually without standardized terms. Supplier performance is not systematically measured — issues are addressed only when they cause visible problems. No sourcing strategy or supplier categorization exists.

### Level 2 — Managed
A supplier database is established with contact and contract information for all suppliers. Basic supplier evaluation criteria are defined and used for supplier selection. Contracts are negotiated and managed with standard terms. Supplier performance is monitored against agreed targets, with regular performance reports produced. Periodic supplier reviews are conducted. A supplier manager role is assigned (possibly combined with the service level manager). Follow-up actions for insufficient performance are agreed and tracked.

### Level 3 — Defined
A formal sourcing strategy is documented and aligned with the organizational strategy. Suppliers are categorized by importance and relationship type, with management effort proportionate to significance. Detailed supplier management procedures cover all stages of the supplier journey. Supplier onboarding and offboarding follow defined plans. Governance structures (committees, compliance reviews) are established. The supplier risk register is actively maintained. A supplier coordinator role supports the supplier manager. Compliance audits are conducted at defined intervals.

### Level 4 — Quantitatively Managed
Supplier performance is measured comprehensively with multi-dimensional scorecards covering warranty, financial, compliance, innovation, and collaboration parameters. The supplier dependency matrix is maintained and used for impact analysis and sourcing decisions. Trends in supplier performance are analysed and used to drive targeted improvements. Cross-supplier collaboration and service integration are actively managed. Supplier management costs and value are tracked to ensure the practice delivers proportionate value.

### Level 5 — Optimizing
The sourcing strategy is continuously refined based on measured outcomes, market intelligence, and strategic changes. Supplier value realization assessments drive improvement initiatives across the sourcing lifecycle. Multi-supplier integration is seamless, with collaboration clauses and shared governance structures ensuring end-to-end service quality. The organization proactively manages supplier risk through predictive analytics and early warning indicators. Strategic suppliers are engaged as true partners in innovation and co-creation. Supplier management practices are benchmarked against industry standards and continuously improved.
