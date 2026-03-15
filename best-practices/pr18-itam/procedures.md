---
process_id: PR18
process_name: "IT Asset Management"
category: procedures
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: IT Asset Management §3.2.1–§3.2.3, §2.2.6, §2.2.7"
  - "IT4IT: Cross-cutting Functions"
last_updated: 2026-03-14
status: draft
---

# IT Asset Management — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier. The three ITIL 4 sub-processes — managing a common approach, managing lifecycle and records, and verifying/auditing/analysing — are consolidated into five procedures. ITAM has no dedicated FitSM process — these procedures draw primarily from ITIL 4. Different asset types (hardware, software, cloud) require different handling at each lifecycle stage — lifecycle models define the type-specific controls within these general procedures.

---

## Essential Procedures (T2+)

### PROC-ITAM-01: Define ITAM Approach and Establish Register
<!-- sources: ITIL 4 ITAM §3.2.1 Tables 3.1–3.2 Activities 1–2 -->

**Trigger:** Initiation of ITAM practice, expansion of scope to new asset types or organizational units, significant change in organizational strategy, or scheduled review of ITAM approach.

**Scope:** Covers stakeholder analysis, scope definition, data structure design, lifecycle model definition, register establishment, and policy setting. Maps to definition activities 1–2.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Analyse stakeholders' requirements — map major hardware, software, and cloud IT assets with related service expenses. Identify the most significant financial, legal, and technical risks and opportunities. Conduct questionnaires, workshops, and interviews with ITAM stakeholders (internal and external) to form a categorized and prioritized list of requirements aligned with the risk and opportunity register. Review IT strategy, vendor trends, and compliance requirements | IT Asset Manager | IT strategy, risk registers, vendor trends, compliance requirements, existing IT asset data | Prioritized requirements, risk and opportunity analysis |
| 2 | Define and agree the ITAM approach — specify scope (what asset types, where in the organization, how governed), data structure (entities, attributes, relationships, naming standards, lifecycle stages, interfaces, role-based access), and lifecycle models for each asset type. Define ITAM policies, controls, monitoring procedures, and verification and audit principles. Consider progressive implementation — whether to expand scope incrementally by asset type, geography, and activity depth | IT Asset Manager | Stakeholder requirements, risk analysis, organizational context, tool capabilities | ITAM approach document, data structure definition |
| 3 | Establish the IT asset register — create the register as part of the data structure definition. If starting from existing data (spreadsheets, other systems), organize, normalize according to new naming conventions, and upload. Define reconciliation keys and data synchronization rules between the register and related repositories (CMDB, financial systems, procurement systems). Define media libraries and hardware store support | IT Asset Manager | Data structure definition, existing IT asset data | IT asset register |
| 4 | Define lifecycle models — for each asset type in scope, document controls and procedures for each lifecycle stage (plan, acquire, assign/IMAC, optimize, decommission, dispose). Include reporting cycles, compliance regulations, monitoring methods, IMAC procedures, labelling and naming conventions, and shared support and maintenance procedures. Validate that lifecycle models reflect the different handling required by software licenses, hardware, and cloud assets | IT Asset Owner | ITAM approach, asset types in scope, compliance requirements | IT asset lifecycle models |

**Exit criteria:** Stakeholder requirements analysed and prioritized. ITAM approach defined and agreed. IT asset register established with data structure. Lifecycle models documented for each asset type in scope.

---

### PROC-ITAM-02: Manage IT Asset Lifecycle and Records
<!-- sources: ITIL 4 ITAM §3.2.2 Tables 3.3–3.4, §2.2.6 -->

**Trigger:** Request for a new IT asset, discovery of a new asset, change to an existing asset, lifecycle stage transition, or scheduled lifecycle review.

**Scope:** Covers asset identification, lifecycle model selection, lifecycle execution, records management, and exception handling. Maps to definition activities 3–5.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify and classify — upon request, discovery, or change, identify the asset type and check whether it is in scope of the ITAM practice. Select the appropriate lifecycle model. Confirm that the model is suitable for the specific asset. For acquisitions, ensure the person responsible reviews the request, checks availability, and verifies asset model substitution rules before triggering procurement | IT Asset Manager | Request or discovery event, ITAM approach, lifecycle models | Asset classified, lifecycle model selected |
| 2 | Execute lifecycle stage — follow the selected lifecycle model for the current stage. For acquisition: capture all documentation (license, warranty, maintenance, invoices, proof of purchase, entitlements, license keys). For assignment (IMAC): log assignment in the register, capture consumer identity, follow BYOD or practical guidance policies. For decommissioning: assess change impact, verify decommissioning condition, handle data per security policy, recover licenses for re-use. For disposal: terminate contracts, comply with e-waste regulations, update financial data | IT Asset Manager | Lifecycle model, request details, register data | Updated IT asset register, lifecycle documentation |
| 3 | Maintain register data — update the IT asset register at each lifecycle stage transition. Embed register updates into purchasing, procurement, and assignment procedures. Capture IT asset data from procurement orders, supplier invoices, delivery slips, and fixed asset registers. Verify data accuracy at the point of capture to reduce the need for dedicated verification activities | IT Asset Manager | Lifecycle events, procurement data, supplier data | Current and accurate register data |
| 4 | Handle exceptions — when deviations from standard lifecycle procedures occur, handle in line with the ITAM approach, compliance regulations, and established practices. Take care to maintain compliance and controls during exceptions. Document all exceptions and review for possible changes to approach, scope, and lifecycle models. Feed lessons learned into continual improvement | IT Asset Manager | Exception event, ITAM approach, compliance requirements | Exception records, lessons learned |

**Exit criteria:** Asset identified and classified. Lifecycle model followed with appropriate controls. Register data captured and verified at each stage. Exceptions documented and reviewed.

---

## Intermediate Procedures (T2+)

### PROC-ITAM-03: Verify and Audit IT Assets
<!-- sources: ITIL 4 ITAM §3.2.3 Tables 3.5–3.6, §2.2.7 -->

**Trigger:** Scheduled audit interval, detection of unauthorized or unregistered assets, significant technical or organizational change, upcoming vendor milestone, or compliance event.

**Scope:** Covers audit planning, data collection, verification, finding review, and reporting. Maps to definition activities 7 and part of 9.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Plan audit — determine scope and frequency based on financial stakes, risks, and detected errors. Plan audits where and when the most significant discrepancies could be discovered and before they penalize the organization. Include: timeframe and schedule, assets and units in scope, discovery and inventory tools, reconciliation methods, compliance controls to check, reporting plan, and post-audit corrective actions. Plan for both internal audits and management of external vendor audits | IT Asset Manager | ITAM approach, risk registers, previous audit findings, vendor milestones | Audit plan |
| 2 | Collect IT asset data — use discovery, inventory, and monitoring tools to collect data for comparison with the register. Cover acquired assets identified by procurement, finance, suppliers, and resellers across all environments (not only production). Verify that asset descriptions and technical characteristics match the register data model. Collect related media: contractual documents, installation media, practical documentation. Automate data collection wherever possible; use manual collection only where automation is not financially viable | License Manager | Audit plan, discovery tools, register data, procurement records | Collected audit data |
| 3 | Verify IT asset data — compare collected data against the register. Investigate and correct discrepancies: register records that do not match assets in infrastructure, discovered assets not in the register, unauthorized assets, missing or incorrect media, incorrect entitlements. Corrections may include removal of unauthorized assets, regularization of unregistered actions, claims against suppliers, archiving of obsolete data, or creation of security incident records for stolen or lost assets | IT Asset Manager | Collected data, register data, compliance regulations | Verified and corrected register, discrepancy records |
| 4 | Produce audit report — document findings, discrepancies, corrective actions taken, compliance status, and recommendations for improvement. Formalize with concerned stakeholders. Distribute through agreed channels. Safely store for future reuse as baseline. Appoint owners for post-audit actions with sufficient time, means, and authority | IT Asset Manager | Verification results, discrepancy records | Audit report, post-audit action assignments |

**Exit criteria:** Audit planned and scoped. Data collected and verified against register. Discrepancies investigated and corrected. Audit report produced with assigned post-audit actions.

---

### PROC-ITAM-04: Review and Optimize ITAM Approach
<!-- sources: ITIL 4 ITAM §3.2.1 Table 3.2 Activity 4, §3.2.2 Table 3.4 Activity 5, §3.2.3 Table 3.6 Activity 4 -->

**Trigger:** Scheduled review interval, significant audit findings, IT-asset-related incidents, compliance issues, technology changes, or organizational changes.

**Scope:** Covers approach review, lifecycle model review, utilization analysis, and improvement initiatives. Maps to definition activities 8 and part of 9.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Review approach adoption and effectiveness — monitor compliance with the agreed ITAM approach and procedures on both event-based and interval-based cycles. Assess whether policies, controls, and procedures are being followed. Identify gaps in adoption, areas of non-compliance, and areas where the approach creates unnecessary overhead | IT Asset Manager | ITAM approach, compliance data, stakeholder feedback, audit reports | Approach review findings |
| 2 | Review lifecycle models — confirm or update lifecycle models based on collected feedback, reviewed requirements, asset records, audit reports, and new risks and opportunities. Assess whether new asset types should be brought into scope. Evaluate whether lifecycle models adequately reflect differences between hardware, software, cloud, and other asset types | IT Asset Owner | Lifecycle models, asset records, audit findings, technology trends | Updated lifecycle models |
| 3 | Analyse utilization and drive optimization — review audit data for analysis of risks, compliance assessment, cost optimization, and utilization trends. Initiate improvements: automation of repetitive tasks, simplification of solutions, better operational integration, optimization of register structure, restocking hardware stores, and awareness training | IT Asset Manager | Audit findings, utilization data, monitoring reports, industry trends | Optimization initiatives, improvement proposals |
| 4 | Evaluate and implement changes — for each proposed change, check compatibility with ITAM policies and regulations, evaluate impact across four dimensions of service management, categorize implementation complexity, and assess cost-benefit-risk. Feed approved changes into continual improvement and change management | IT Asset Manager | Improvement proposals, impact assessments | Approved changes, updated approach and procedures |

**Exit criteria:** Approach adoption and effectiveness reviewed. Lifecycle models confirmed or updated. Utilization analysed and optimization opportunities identified. Changes evaluated and approved for implementation.

---

## Advanced Procedures (T3)

### PROC-ITAM-05: Manage License Compliance and Partner Integration
<!-- sources: ITIL 4 ITAM §2.2.2, §2.4.1, §6 -->

**Trigger:** Scheduled SAM review, upcoming vendor audit, new software or cloud acquisition, new partner relationship, or compliance finding.

**Scope:** Covers software license compliance, cloud service management, partner coordination, and vendor audit management. Maps to definition activity 10 and advanced aspects of activities 7 and 9.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Conduct software inventory — inventory all software across all relevant environments (development, test, staging, production, training) and platforms (on-premise hardware, cloud, managed datacentres). Consider all deployment techniques (machine cloning, vendor media, containers). Collect all parameters used in license models. Reconcile inventory against entitlements to identify over-deployment, under-utilization, and compliance gaps | License Manager | Software register data, discovery tools, license agreements, entitlement records | Software inventory, compliance position |
| 2 | Manage cloud service compliance — integrate cloud services (IaaS, PaaS, SaaS) into ITAM scope. Verify compliance with security policy for cloud assets. Verify compatibility with license terms of software installed on cloud platforms. Monitor cloud service utilization and spending to prevent uncontrolled cost growth. Track subscription renewals and usage against contracted levels | License Manager | Cloud service agreements, utilization data, security policies | Cloud compliance report, cost optimization opportunities |
| 3 | Coordinate with partners and suppliers — include terms in third-party service contracts specifying duties and responsibilities for each ITAM activity suppliers contribute to (reception, storage, stock management, IMAC, incident detection, inventory). Sign NDAs to protect sensitive IT asset data. Discover and address conflicts of interest. Communicate achievements of mature ITAM practice to optimize vendor relationships and discourage unnecessary vendor audits | IT Asset Manager | Supplier agreements, partner contracts, ITAM approach | Updated contractual terms, partner ITAM arrangements |
| 4 | Prepare for and manage vendor audits — maintain readiness for external vendor compliance audits. Ensure proofs of purchase, entitlement documentation, and license records are complete and accessible. Internal audits should minimize the impact of external audits. When external audits occur, manage them in project mode with clear scope, timeline, and stakeholder coordination | License Manager | Entitlement records, proofs of purchase, audit scope | Vendor audit response, compliance documentation |
| 5 | Optimize financial performance — combine utilization monitoring data with understanding of industry trends, vendor practices, and technology evolution to optimize contracts, decrease ownership costs, and improve financial performance. Assess ROI, total cost of ownership, and value on investment across asset types. Propose asset strategy adjustments including cloud migration, license model optimization, and hardware refresh cycles | IT Asset Manager | Utilization reports, industry trends, financial data, technology assessments | Financial optimization recommendations, strategy adjustments |

**Exit criteria:** Software inventory completed across all environments. Cloud services integrated into compliance scope. Partner and supplier ITAM arrangements agreed. Vendor audit readiness confirmed. Financial optimization opportunities identified and acted upon.
