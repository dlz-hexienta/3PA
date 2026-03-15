---
process_id: PR23
process_name: "Supplier Management"
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
tier_minimum: T2
sources:
  - "ITIL 4: Supplier Management §3.2.1, §3.2.2"
  - "FitSM-2: §PR8 SUPPM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (supplier coordination)"
last_updated: 2026-03-13
status: draft
---

# Supplier Management — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the operational core of supplier management — maintaining supplier data, evaluating and selecting suppliers, negotiating contracts, and monitoring performance. Intermediate procedures add the strategic and governance layer — developing the sourcing strategy, onboarding and offboarding suppliers, and managing supplier governance. The advanced procedure covers comprehensive supplier assessment and value realization review. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All organizations implementing this process)

### PROC-SUPPM-01: Maintain Supplier Database
<!-- sources: FitSM-2 §PR8 SUPPM (Initial Setup: set up supplier database; Ongoing: maintain supplier database), ITIL 4 Supplier Management §5.1 -->

**Trigger:** New supplier contracted; change to existing supplier information; supplier relationship ended; periodic scheduled review of database currency

**Inputs:** Information on suppliers and supplier offerings, signed contracts, OLAs with internal suppliers, UAs with external suppliers, supplier performance data

**Outputs:** Up-to-date supplier database with contact details, contracted services, agreement references, categorization, and relationship status

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify all current suppliers | Compile a list of all internal and external suppliers providing services, products, or resources to the organization. Include suppliers operating under formal contracts, OLAs, or underpinning agreements | Supplier Manager |
| 2 | Collect supplier information | For each supplier, gather contact details on both the supplier side and the organization side (supplier relationship manager), contracted services, agreement references, service levels, and performance history | Supplier Coordinator |
| 3 | Register supplier in the database | Create a record in the supplier database / SMIS with all required attributes. Link the supplier to the relevant services, contracts, and dependencies | Supplier Coordinator |
| 4 | Understand monitoring requirements | For each supplier, determine which services or service components need to be monitored, and how performance monitoring will be conducted | Supplier Manager |
| 5 | Review and update records periodically | At defined intervals, review all supplier records for accuracy and completeness. Update contact information, contract status, service associations, and categorization. Add new suppliers and archive records for relationships that have ended | Supplier Coordinator |
| 6 | Remove or archive suppliers | When a supplier relationship ends (contract terminated, expired, or services offboarded), archive the supplier record with the end date and reason. Ensure the supplier dependency matrix is updated | Supplier Coordinator |

---

### PROC-SUPPM-02: Evaluate and Select Suppliers
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4 (Identifying available suppliers, Engaging with suppliers, Evaluating and selecting), FitSM-2 §PR8 SUPPM -->

**Trigger:** New service requirement requiring external sourcing; change to an existing service requiring a different or additional supplier; dissatisfaction with incumbent supplier; supplier consolidation exercise

**Inputs:** Business requirements for sourcing, service specifications, service level requirements, budgetary and financial requirements, legal requirements, supplier evaluation and selection criteria, sourcing strategy (at T2+)

**Outputs:** Preliminary sourcing requirements, list of potential suppliers, RfX document, detailed requirements, shortlisted suppliers, selected supplier(s), supplier risk register (initial entry)

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Analyse the business requirements | Understand and document the sourcing need — what services are required, what service levels are expected, what budgetary and legal constraints apply. Determine the approach to sourcing (type of relationship preferred, service integration approach) | Supplier Manager |
| 2 | Identify available suppliers | Research the market to identify potential suppliers. Compile a preliminary list based on the sourcing requirements and preliminary selection criteria. For some organizations, this may involve an empanelment exercise or use of existing supplier panels | Supplier Coordinator |
| 3 | Prepare and issue the RfX | Create the RfX document (RFI, RFP, RFQ, or RFD as appropriate) containing the selection process details, evaluation criteria, business overview, detailed requirements and specifications, service level requirements, terms and conditions, and submission instructions. Issue the RfX through the agreed communication channels | Supplier Coordinator |
| 4 | Evaluate supplier responses | When suppliers respond to the RfX, evaluate each response against the defined evaluation criteria. Score suppliers on a consistent basis. The evaluation may include demonstrations, proofs of concept, or site visits. Shortlist the top candidates for final evaluation and negotiation | Supplier Manager |
| 5 | Conduct due diligence | For shortlisted suppliers, conduct due diligence — verify the supplier's service delivery track record, capability, financial stability, regulatory compliance, and references. Assess associated risks and document them in the supplier risk register | Supplier Manager |
| 6 | Select the supplier and communicate the decision | Based on the evaluation results and due diligence, select the preferred supplier(s). Communicate the decision to the selected and unsuccessful suppliers. Proceed to contract negotiation | Supplier Manager |

---

### PROC-SUPPM-03: Negotiate and Manage Supplier Contracts
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4 (Contracting suppliers) -->

**Trigger:** New supplier selected requiring a contract; existing contract requiring amendment, renewal, or termination

**Inputs:** Evaluation results, detailed service requirements and specifications, service level requirements, RfX responses, contract framework and standard terms (at T2+), legal requirements

**Outputs:** Signed contract covering service descriptions, service levels, terms, performance baselines, reward/penalty mechanisms; amended, renewed, or terminated contract

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Draft the contract | Frame the contract based on the RfX requirements and the supplier's response. Cover the detailed service description, service performance targets, statement of work or scope framework, technical schedules, payment schedules, and terms and conditions. Include performance baselines, reward and penalty mechanisms, and contract management arrangements | Supplier Manager |
| 2 | Negotiate contract terms | Negotiate the contract terms with the supplier. Ensure that roles and responsibilities, warranty targets, utility targets, service experience targets, and other service-specific requirements are clearly agreed. For cooperative and partnership relationships, include collaboration and service integration clauses | Supplier Manager |
| 3 | Review and finalize the contract | Conduct legal review. Ensure alignment with the sourcing strategy and compliance requirements. Finalize the contract document | Supplier Manager |
| 4 | Sign the contract | Obtain signatures from the authorized parties on both sides. Register the signed contract in the supplier database and contract management system | Supplier Manager |
| 5 | Monitor the contract through its lifecycle | Track the contract through its lifecycle. Monitor for amendment triggers (requirement changes, technological changes, performance changes, mergers, new service needs). Manage contract amendments following the same negotiation and approval process | Supplier Coordinator |
| 6 | Review the contract for renewal or termination | Before the contract review date or expiry, assess whether to renew, amend, or terminate. Base the decision on supplier performance, value realization, strategic alignment, and changing business needs. Execute the renewal or termination as appropriate | Supplier Manager |

---

### PROC-SUPPM-04: Monitor Supplier Performance and Conduct Reviews
<!-- sources: FitSM-2 §PR8 SUPPM (Ongoing: monitor supplier performance), ITIL 4 Supplier Management §3.2.2 Table 3.4 (Managing consumption and monitoring supplier performance) -->

**Trigger:** Scheduled performance reporting cycle; scheduled supplier review date; significant supplier performance issue

**Inputs:** Supplier contracts with agreed performance targets, supplier performance data, service reports from Measurement & Reporting, OLA/UA achievement data from Service Level Management, complaints and escalation records

**Outputs:** Supplier performance reports and scorecards, agreed follow-up actions for insufficient performance, input to supplier reviews and governance meetings

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Collect supplier performance data | Gather performance data from monitoring systems, service reports, and supplier-provided data. Map data to the agreed KPIs and service level targets defined in the contract | Supplier Coordinator |
| 2 | Measure performance against targets | Compare collected data with the agreed targets. Calculate KPI achievement rates, identify deviations and trends. Produce the supplier performance report | Supplier Coordinator |
| 3 | Prepare the supplier review | Compile the review pack — performance reports, compliance status, open issues, contractual adherence, risk register updates, and status of previously agreed actions. Schedule the review and invite participants | Supplier Coordinator |
| 4 | Conduct the supplier review | Discuss performance against targets, contractual compliance, service quality, open issues, risks, and improvement opportunities. Review status of previously agreed follow-up actions. For cooperative and partnership suppliers, also discuss collaboration effectiveness, innovation contributions, and strategic alignment | Supplier Manager |
| 5 | Agree follow-up actions | Where performance is insufficient or improvement opportunities are identified, agree specific follow-up actions with the supplier — with owners, target dates, and success criteria. Determine whether reward or penalty mechanisms should be triggered | Supplier Manager |
| 6 | Document outcomes and distribute | Record the review outcomes, decisions, and agreed actions. Distribute the supplier review report to relevant parties. Update the supplier database with performance and review data | Supplier Coordinator |
| 7 | Track follow-up actions | Monitor the implementation of agreed follow-up actions. Escalate overdue actions. Report action status at the next review | Supplier Coordinator |

---

## Intermediate Procedures (T2+)

### PROC-SUPPM-05: Develop Sourcing Strategy and Procedures
<!-- sources: ITIL 4 Supplier Management §3.2.1 Tables 3.1, 3.2 -->

**Trigger:** Initial establishment of the supplier management practice; significant change to organizational strategy, business requirements, or the supplier landscape; periodic scheduled review of the sourcing strategy

**Inputs:** Organization's strategy, service relationship type requirements, budgetary and financial considerations, legal requirements and regulations, existing supplier management policy and processes

**Outputs:** Sourcing strategy, supplier management policy, supplier evaluation and selection criteria, contract framework, compliance and audit criteria, collaboration framework, supplier dependency matrix, supplier management procedures

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Analyse the organizational strategy and requirements | Review the organization's strategy and its implications for sourcing. Identify which capabilities and services need to be sourced externally. Assess budgetary, legal, and regulatory constraints | Supplier Manager |
| 2 | Define the supplier categorization scheme | Establish categories for classifying suppliers based on their importance, the type of service relationship (basic, cooperative, partnership), and the associated risks. Define the management approach for each category | Supplier Manager |
| 3 | Develop the sourcing strategy | Document the organization's approach to sourcing, including: supplier categorization and applicable relationship types, evaluation and selection criteria, due diligence requirements, contracting standards, compliance and audit requirements, reward and penalty mechanisms, integration and disintegration options, collaboration guidelines, performance measurement standards, and reporting standards | Supplier Manager |
| 4 | Develop supplier management procedures | Create detailed procedures for each stage of the supplier journey — identifying available suppliers, engaging with suppliers, evaluation and selection, contracting, onboarding and offboarding, performance management, governance and compliance, and supplier assessment and review | Supplier Manager |
| 5 | Communicate and embed the strategy | Communicate the sourcing strategy and procedures to all relevant stakeholders across the organization. Provide training for staff involved in supplier management. Publish technical integration standards and methods for potential suppliers. Communicate the sourcing approach through the agreed external channels | Supplier Manager |
| 6 | Develop the contract framework | Create standard contract templates and frameworks covering different service relationship types. Include standard terms, performance measurement clauses, compliance requirements, and collaboration provisions | Supplier Manager |
| 7 | Review and adjust the strategy periodically | Monitor the adoption, compliance, and effectiveness of the sourcing strategy and procedures. Review based on supplier-related incidents, conflicts, complaints, and periodic assessment results. Update the strategy based on lessons learned and changing organizational needs | Supplier Manager |

---

### PROC-SUPPM-06: Onboard and Offboard Suppliers
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4 (On/offboarding suppliers) -->

**Trigger:** New supplier contract signed requiring onboarding; existing supplier contract terminated requiring offboarding; supplier transition (switching from one supplier to another)

**Inputs:** Signed contract, sourcing strategy and categorization scheme, service specifications, supplier dependency matrix, risk register, service catalogue, information security requirements

**Outputs:** Onboarded or offboarded supplier, updated supplier dependency matrix, updated service catalogue, updated risk register, onboarding/offboarding status reports

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Create the onboarding or offboarding plan | Based on the contract and service requirements, create a plan covering the services and sub-services, the supplier's processes, tools, and team members to be integrated or separated, the cutover plan for go-live or transition, and delivery risk identification | Supplier Coordinator |
| 2 | Categorize the supplier (onboarding) | Classify the new supplier according to the categorization scheme based on their importance, relationship type, and associated risks. Ensure that management effort will be proportionate to significance | Supplier Manager |
| 3 | Manage access (onboarding) or revoke access (offboarding) | For onboarding: determine what organizational resources the supplier needs access to and ensure access is provisioned. For offboarding: revoke the organization's access to the supplier's resources and the supplier's access to the organization's resources. Recover assets assigned to or managed by supplier team members | Supplier Coordinator |
| 4 | Integrate or separate services | For onboarding: integrate the supplier's services with the organization's information systems, tools, and products. Update the service catalogue with new services and the mapping of services to supplier teams. For offboarding: remove the supplier's services and ensure transition to alternative arrangements | Supplier Coordinator |
| 5 | Update the supplier dependency matrix | Update the dependency matrix to reflect the new supplier and their service contributions (onboarding), or to remove the offboarded supplier's services (offboarding) | Supplier Coordinator |
| 6 | Identify and manage risks | Identify delivery risks associated with the onboarding or offboarding. Document risks in the supplier risk register. Monitor risks through the transition period | Supplier Coordinator |
| 7 | Notify stakeholders and publish status | Notify all relevant stakeholders of the onboarding or offboarding. Publish status reports. Ensure that all consuming processes are aware of the change and its implications for service delivery | Supplier Coordinator |

---

## Advanced Procedures (T3)

### PROC-SUPPM-07: Assess Supplier Value and Drive Improvement
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4 (Assessing and reviewing suppliers), §3.2.1 Table 3.2 (Review and adjust) -->

**Trigger:** Scheduled periodic supplier assessment; completion of a major contract milestone; strategic planning cycle requiring sourcing input

**Inputs:** Supplier monitoring reports and performance data, service consumption and value realization data, sourcing strategy and procedures, supplier risk register, supplier dependency matrix, stakeholder feedback

**Outputs:** Updated supplier list and categorization, updated sourcing strategy and procedures, improvement initiatives, supplier risk register updates, recommendations for contract renewal, amendment, or termination

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Gather value realization data | Collect comprehensive data on the supplier's contribution — not only operational performance against KPIs but also year-on-year benefit, innovation contributions, strategic alignment, collaboration effectiveness, and cost efficiency | Supplier Manager |
| 2 | Conduct the value realization assessment | Assess the supplier's overall value to the organization using multi-dimensional scorecards. Evaluate performance, compliance, innovation, improvement, resourcing, knowledge contribution, and cultural alignment. Compare with the expectations defined in the sourcing strategy for the supplier's category | Supplier Manager |
| 3 | Identify improvement initiatives | Based on the assessment, identify specific improvement opportunities — for the individual supplier relationship, for the sourcing strategy, for evaluation and selection procedures, or for supplier management procedures more broadly | Supplier Manager |
| 4 | Review the sourcing strategy and procedures | Use the assessment findings as input to the periodic review of the sourcing strategy. Determine whether categorization criteria, evaluation standards, contracting terms, or governance arrangements need adjustment | Supplier Manager |
| 5 | Decide on contract actions | Based on the value assessment, determine the appropriate contract action — renewal (if the supplier delivers expected value), amendment (if terms need updating), or termination (if value is insufficient and improvement is unlikely). Communicate decisions to the supplier | Supplier Manager |
| 6 | Register improvement initiatives | Submit improvement initiatives to the continual improvement register. Communicate findings and recommendations to leadership and relevant stakeholders | Supplier Manager |
| 7 | Update supplier records | Update the supplier database with assessment results, revised categorization, and any changes to the relationship. Update the risk register with newly identified risks or changed risk levels | Supplier Coordinator |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-SUPPM-01 | Maintain Supplier Database | All | New supplier; information change; periodic review |
| PROC-SUPPM-02 | Evaluate and Select Suppliers | All | New sourcing need; supplier change |
| PROC-SUPPM-03 | Negotiate and Manage Supplier Contracts | All | New contract; amendment; renewal; termination |
| PROC-SUPPM-04 | Monitor Supplier Performance and Conduct Reviews | All | Scheduled reporting cycle; scheduled review; performance issue |
| PROC-SUPPM-05 | Develop Sourcing Strategy and Procedures | T2+ | Practice establishment; strategy change; periodic review |
| PROC-SUPPM-06 | Onboard and Offboard Suppliers | T2+ | New contract signed; contract terminated; supplier transition |
| PROC-SUPPM-07 | Assess Supplier Value and Drive Improvement | T3 | Periodic assessment; major milestone; strategic planning cycle |
