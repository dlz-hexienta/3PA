---
process_id: PR18
process_name: "IT Asset Management"
category: policy
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: IT Asset Management §2.1, §2.2.3, §2.3, §2.4, §2.5, §6"
  - "IT4IT: Cross-cutting Functions"
last_updated: 2026-03-14
status: draft
---

# IT Asset Management — Best Practice Policy

## How to Use This Policy Template

This policy establishes the governing principles and mandatory requirements for the IT asset management practice. It should be customized to reflect the organization's IT asset portfolio, regulatory environment, financial materiality thresholds, and relationship to the broader asset management function. Requirements are graduated by maturity — organizations should implement Essential requirements first, then layer on Intermediate and Advanced requirements as the practice matures. ITAM has no dedicated FitSM process — this policy draws primarily from ITIL 4 with IT4IT cross-cutting alignment.

---

## Policy Principles

### 1. Full Lifecycle Management
<!-- sources: ITIL 4 ITAM §2.1, §2.2.6 -->

IT asset management shall plan and manage IT assets through their complete lifecycle — from planning and budgeting through acquisition, assignment, utilization optimization, decommissioning, and disposal. Each lifecycle stage shall have defined controls, procedures, and data capture requirements appropriate to the asset type. Assets shall not exist outside managed lifecycle stages.

### 2. Value Optimization
<!-- sources: ITIL 4 ITAM §2.1, §2.4.2 -->

IT asset management shall maximize the value derived from IT assets while controlling costs and managing risks. The practice shall support traceability of IT expenditures, assessment of return on investment, and optimization of value for money. Underused assets — including sleeping stock, redundant contracts, and excessive license pools — shall be identified and addressed through utilization monitoring and analysis.

### 3. Trustworthy Data
<!-- sources: ITIL 4 ITAM §2.1, §2.2.4 -->

Information about IT assets shall be accurate, up-to-date, reliable, comprehensible, easy to use, and relevant. The IT asset register shall be the authoritative source of asset information. Data shall be captured as early as possible in the lifecycle — embedding register updates into purchasing, procurement, and assignment procedures to reduce the need for dedicated verification activities. The careful selection of relevant data and optimal ways to maintain it is a key component of the ITAM approach.

### 4. Risk-Based Compliance
<!-- sources: ITIL 4 ITAM §2.1, §2.4.1 -->

IT asset management shall ensure compliance with contracts (including software license agreements), regulations (financial, tax, electronic waste), and organizational policies (security, HR, architecture, sourcing). The practice shall protect IT assets against theft, damage, and loss, including protection of related contracts and entitlements. Required evidence to demonstrate compliance shall be identified and maintained.

### 5. Progressive Implementation
<!-- sources: ITIL 4 ITAM §2.2.3 -->

ITAM implementation shall be based on organizational needs — verified against the practice objectives of maximizing value, controlling costs, managing risks, supporting decisions, and meeting regulatory requirements. The practice may be implemented progressively — first obtaining trustworthy data, then achieving integrated lifecycle management, then optimizing cost-effectiveness — expanding scope incrementally by asset type, organizational unit, and activity depth.

### 6. Integration with Value Streams
<!-- sources: ITIL 4 ITAM §3.2.1 Table 3.2 Activity 3 -->

ITAM controls and procedures shall be embedded into the organization's value streams and related practices — not managed as a stand-alone bureaucratic function. People requesting and handling IT assets shall understand the associated financial, security, and legal stakes. The practice shall provide adequate and valuable IT asset information in convenient and useful form, not create overhead without corresponding benefit.

### 7. Continual Improvement
<!-- sources: ITIL 4 ITAM §3.2.1 Table 3.2 Activity 4, §3.2.3 Table 3.6 Activity 4 -->

The ITAM approach, scope, lifecycle models, and procedures shall be subject to continual review and improvement — informed by audit findings, utilization analysis, compliance results, industry trends, and stakeholder feedback. The practice shall adapt to changes in technology, vendor practices, regulatory requirements, and organizational needs. Review shall occur on both event-based and interval-based cycles.

---

## Mandatory Requirements

### Essential (T2+)
<!-- sources: ITIL 4 ITAM §2.2.3, §2.2.4, §2.2.6, §3.2.1, §3.2.2 -->

| # | Requirement |
|---|-------------|
| 1 | The scope of IT asset management shall be defined — specifying which IT asset types (hardware, software, cloud, data), which parts of the organization (sites, business units, departments), and which activities are governed by the practice |
| 2 | An IT asset register shall be established and maintained — recording ownership, cost, key characteristics, lifecycle status, and relationships for all IT assets within scope. The register shall be the authoritative source for IT asset data |
| 3 | IT asset lifecycle models shall be defined for each asset type within scope — specifying controls, procedures, compliance requirements, and data capture points for each lifecycle stage (plan, acquire, assign, optimize, decommission, dispose) |
| 4 | Roles and responsibilities for IT asset management — including IT asset manager, license manager, and IT asset owner — shall be documented, assigned, and communicated to all relevant parties |
| 5 | IT asset data shall be captured and recorded in the IT asset register at each lifecycle stage — including acquisition documentation (licenses, warranties, maintenance contracts, invoices, proofs of purchase) and assignment records |

### Intermediate (T2+)
<!-- sources: ITIL 4 ITAM §2.2.7, §2.4.1, §2.4.2, §3.2.1 -->

| # | Requirement |
|---|-------------|
| 6 | Verification activities shall be embedded in lifecycle procedures — ensuring IT asset data is checked and corrected at each stage, reducing the need for stand-alone verification efforts. Last verification and audit dates shall be tracked per asset |
| 7 | IT asset audits shall be conducted at planned intervals and in response to significant events — covering existing assets, acquisitions, related media, and compliance controls. Audit scope and frequency shall be adjusted based on financial stakes, risks, and detected errors |
| 8 | IT asset utilization shall be monitored for all controlled asset types — identifying underused assets, redundant contracts, approaching contract end dates, product obsolescence, and optimization opportunities. Monitoring shall be automated wherever possible |
| 9 | The ITAM approach, scope, lifecycle models, and procedures shall be communicated to all stakeholders and integrated into the organization's value streams — with appropriate training for procurement, service desk, deployment, and other participating teams |

### Advanced (T3)
<!-- sources: ITIL 4 ITAM §2.2.2, §2.4.2, §6 -->

| # | Requirement |
|---|-------------|
| 10 | Software license compliance shall be verified through dedicated SAM procedures — including software inventory across all environments and platforms, collection of license parameters, verification of entitlements, and preparation for vendor audits. Cloud service compliance shall be integrated into SAM scope |
| 11 | ITAM shall be coordinated with partners and suppliers through contractual terms — specifying duties and responsibilities for each ITAM activity that suppliers contribute to, including asset reception, storage, stock management, IMAC, incident detection, and inventory. NDAs shall protect sensitive IT asset data |
| 12 | The ITAM approach shall be reviewed at planned intervals — evaluating adoption, compliance, and effectiveness. Reviews shall assess impact across all four dimensions of service management and drive cost optimization through utilization analysis, contract optimization, and technology assessment |

---

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Configuration Management Policy (PR17) | CI/asset data reconciliation — CMDB and IT asset register should share data with clear synchronization rules |
| Service Financial Management Policy (PR03) | Asset budgeting, accounting, depreciation, cost tracking — reconciliation between IT asset and financial asset perspectives |
| Supplier Management Policy (PR23) | IT asset procurement, vendor contracts, license compliance, vendor audit management |
| Change Management Policy (PR15) | Changes involving IT assets require impact analysis; IMAC activities may require change authorization |
| Information Security Management Policy (PR09) | IT asset protection, data handling at decommissioning, access control to IT asset data and registers |
| Service Request Management Policy (PR12) | Service requests for asset provision, move, change, recovery, and reclaim — IMAC fulfilment |
| Monitoring & Event Management Policy (PR14) | IT asset utilization monitoring, discovery of unregistered assets, deviation detection |
| Service Level Management Policy (PR02) | Minimum stock levels, provisioning SLAs, asset contract alignment with service agreements |
