---
process_id: PR18
process_name: "IT Asset Management"
category: raci
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: IT Asset Management §4.1 Table 4.2, §4.1.1–§4.1.5, §4.2"
  - "IT4IT: Cross-cutting Functions"
last_updated: 2026-03-14
status: draft
---

# IT Asset Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

ITAM involves many organizational roles across IT, procurement, finance, legal, and supplier management. The three roles below consolidate the practice-specific responsibilities described in ITIL 4 Table 4.2. In organizations with large or complex IT asset portfolios, the IT asset manager role may be specialized by asset type (software, hardware, cloud) and the license manager role may be dedicated to specific platforms or publishers.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| ITAM | IT Asset Manager | T2+ |
| LM | License Manager | T2+ |
| AO | IT Asset Owner | T2+ |

## Essential Activities (T2+)

### Approach Definition and Lifecycle Management
<!-- sources: ITIL 4 ITAM §4.1 Table 4.2, §3.2.1, §3.2.2 -->

| Activity | ITAM | LM | AO |
|----------|:----:|:--:|:--:|
| Analyse stakeholders' requirements and IT asset risks | A/R | C | C |
| Define and agree the ITAM approach | A/R | R | C |
| Analyse resources, identify IT assets, and verify lifecycle models | A/R | C | I |
| Follow the lifecycle model and manage records | A/R | R | I |
| Manage lifecycle exceptions | A/R | C | C |

## Intermediate Activities (T2+)

### Communication, Verification, and Review
<!-- sources: ITIL 4 ITAM §4.1 Table 4.2, §3.2.1, §3.2.3 -->

| Activity | ITAM | LM | AO |
|----------|:----:|:--:|:--:|
| Communicate and integrate ITAM approach into value streams | A/R | C | I |
| Plan and execute IT asset audits | A/R | R | I |
| Review and adjust the ITAM approach | A/R | C | C |

## Advanced Activities (T3)

### Analysis, Optimization, and Partner Integration
<!-- sources: ITIL 4 ITAM §4.1 Table 4.2, §3.2.3, §2.4.2, §6 -->

| Activity | ITAM | LM | AO |
|----------|:----:|:--:|:--:|
| Review and analyse audit findings and optimize utilization | A/R | R | C |
| Compose audit reports and drive cost optimization | A/R | C | I |

## Notes

1. **IT Asset Manager:** The central role overseeing the IT asset lifecycle for all IT assets in scope. Accountable for the ITAM approach, communication, value stream integration, scoping decisions, exception handling, register data validity, compliance, risk participation, utilization optimization, and reporting. Manages the approach definition, lifecycle execution, and audit coordination. Competency profile: TMCA for approach activities (methods, technical, coordinator, administrator), TCA for lifecycle activities, TCMA for audit planning. In organizations with specialized asset portfolios, this role may be split into software ITAM, hardware ITAM, and cloud ITAM managers. Corresponds to the ITIL practice owner role with competency profile CLA.
2. **License Manager:** Subject matter expert for all licensing aspects — including software and cloud products, stock of available licenses, compliance with license terms, and vendor audit readiness. Collaborates with supplier and contract management to ensure IT-asset-related contracts are appropriate in terms of cost-value balance and compliance. Due to the complexity of licence models, the role may be dedicated to a specific platform type (workplace, datacentre) or specific software publisher. Competency profile: TA for data collection and verification, TCM for compliance analysis. Commonly combined with the software IT asset manager role. Responsible for software inventory, entitlement reconciliation, and vendor audit preparation.
3. **IT Asset Owner:** The organizational entity that holds rights to IT assets and sponsors assets throughout their lifecycle. Makes decisions about asset inclusion in scope, acquisition methods, assignment policies, and disposal approaches. Validates that ITAM procedures serve the organization's interests. Encompasses custodianship responsibilities — ensuring the right utilization of assets and consistent application of ITAM procedures in the best interests of the asset owner. Competency profile: CM for scope decisions, LC for policy validation. Multiple IT asset owners may exist — one per business unit, product, or service, each sponsoring assets within their domain.
4. **IT Asset Consumer:** Not a practice-specific role but a responsibility held by any person using an IT asset for service delivery or consumption. Consumers are responsible for their assigned assets during use — following practical guidance, BYOD policies, and reporting issues. The consumer role can be performed by a member of the service provider organization or by a customer. Consumers are informed of ITAM policies and are subject to assignment records in the register.
5. **Procurement and Finance Integration:** ITAM depends heavily on procurement, finance, and supplier management for data capture, contract management, and compliance verification. These functions are not shown as dedicated roles in the RACI matrix because their ITAM-related activities are governed by their own practices (supplier management, service financial management). The IT asset manager coordinates with these functions through established integration points.
6. **Organizational Structure:** ITIL 4 notes that central ITAM teams help develop expertise and facilitate collaboration with procurement, finance, and risk management, but centralization can create distance from day-to-day operations. Global organizations often centrally define their ITAM practice and deploy in a decentralized manner — achieving global convergence while considering local aspects including regulatory requirements, language, currency, and supplier contracts.
