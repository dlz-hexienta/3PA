---
process_id: PR23
process_name: "Supplier Management"
category: raci
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
  - "ITIL 4: Supplier Management §4.1, §4.2, Table 4.2"
  - "FitSM-2: §PR8 SUPPM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (supplier coordination)"
last_updated: 2026-03-13
status: draft
---

# Supplier Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. At the minimum tier (T2), the supplier manager performs all activities directly, including those assigned to the supplier coordinator at higher tiers. The supplier manager role may be combined with the service level manager at T2.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SM | Supplier Manager | All |
| SC | Supplier Coordinator | T2+ |
| SLM | Service Level Manager | All |
| SO | Service Owner | All |

## Essential Activities (All organizations implementing this process)

### Supplier Database Management
<!-- sources: FitSM-2 §PR8 SUPPM, ITIL 4 Supplier Management §5.1 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Identify all current internal and external suppliers | A/R | C | C | C |
| Collect supplier contact, contract, and service information | A | R | C | C |
| Register suppliers in the supplier database / SMIS | A | R | I | I |
| Determine performance monitoring requirements for each supplier | A/R | C | C | C |
| Review and update supplier records periodically | A | R | I | I |
| Archive records for ended supplier relationships | A | R | I | I |

### Supplier Evaluation and Selection
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4, Table 4.2 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Analyse the business requirements for sourcing | A/R | C | C | C |
| Identify available suppliers in the market | A | R | — | C |
| Prepare and issue the RfX document | A | R | C | C |
| Evaluate supplier responses against defined criteria | A/R | R | C | C |
| Conduct due diligence on shortlisted suppliers | A/R | R | — | C |
| Select the supplier and communicate the decision | A/R | I | I | I |

### Contract Negotiation and Management
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4 (Contracting suppliers), Table 4.2 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Draft the contract based on RfX requirements and supplier response | A/R | R | C | C |
| Negotiate contract terms with the supplier | A/R | C | C | C |
| Review and finalize the contract (legal and compliance) | A/R | C | — | — |
| Sign the contract and register in the supplier database | A/R | R | I | I |
| Monitor the contract through its lifecycle (amendments, renewals) | A | R | C | I |
| Review the contract for renewal or termination | A/R | C | C | C |

### Supplier Performance Monitoring and Reviews
<!-- sources: FitSM-2 §PR8 SUPPM (monitor supplier performance), ITIL 4 Supplier Management §3.2.2 Table 3.4, Table 4.2 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Collect supplier performance data and map to agreed KPIs | A | R | C | — |
| Measure performance against targets and produce reports | A | R | C | — |
| Prepare the supplier review pack | A | R | C | C |
| Conduct the supplier performance review | A/R | R | C | C |
| Agree follow-up actions for insufficient performance | A/R | C | C | C |
| Document outcomes and distribute the review report | A | R | I | I |
| Track follow-up actions to completion | A | R | C | — |

## Intermediate Activities (T2+)

### Sourcing Strategy and Procedures Development
<!-- sources: ITIL 4 Supplier Management §3.2.1 Tables 3.1, 3.2, Table 4.2 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Analyse the organizational strategy and sourcing requirements | A/R | C | C | C |
| Define the supplier categorization scheme | A/R | C | C | — |
| Develop and document the sourcing strategy | A/R | C | C | C |
| Develop supplier management procedures | A/R | C | C | — |
| Develop the contract framework and standard terms | A/R | C | C | — |
| Communicate and embed the strategy and procedures | A/R | R | I | I |

### Supplier Onboarding and Offboarding
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4, Table 4.2 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Create the onboarding or offboarding plan | A | R | C | C |
| Categorize the supplier (onboarding) | A/R | C | — | C |
| Manage access provisioning or revocation | A | R | — | I |
| Integrate or separate supplier services | A | R | C | C |
| Update the supplier dependency matrix | A | R | I | I |
| Identify and manage onboarding/offboarding risks | A | R | C | C |
| Notify stakeholders and publish status | A | R | I | I |

### Supplier Governance, Compliance, and Audits
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4, §2.4.1 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Establish governance structures (committees, compliance reviews) | A/R | C | C | — |
| Conduct compliance audits at defined intervals | A/R | R | — | — |
| Maintain the supplier risk register | A | R | C | — |
| Take corrective action for non-compliance | A/R | R | C | I |

## Advanced Activities (T3)

### Sourcing Strategy Review and Adjustment
<!-- sources: ITIL 4 Supplier Management §3.2.1 Table 3.2 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Monitor adoption and effectiveness of the sourcing strategy | A/R | R | C | C |
| Review and adjust the strategy based on outcomes and strategic changes | A/R | C | C | C |
| Update supplier management procedures based on lessons learned | A/R | C | C | — |

### Supplier Value Assessment and Improvement
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Gather value realization data (performance, innovation, strategic contribution) | A | R | C | C |
| Conduct multi-dimensional value realization assessment | A/R | R | C | C |
| Identify improvement initiatives for supplier relationships and sourcing practices | A/R | C | I | I |
| Decide on contract actions (renew, amend, terminate) | A/R | I | C | C |
| Register improvement initiatives and communicate findings | A/R | R | I | I |

### Multi-Supplier Integration and Collaboration
<!-- sources: ITIL 4 Supplier Management §2.4.3, §3.2.2 -->

| Activity | SM | SC | SLM | SO |
|----------|:--:|:--:|:---:|:--:|
| Coordinate cross-supplier collaboration and service integration | A/R | R | C | C |
| Manage cross-supplier dependencies and integration arrangements | A | R | C | C |
| Include collaboration and integration clauses in contracts | A/R | C | C | — |
| Review cross-supplier coordination effectiveness | A/R | R | C | I |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The supplier manager is accountable for all supplier management activities — both strategic (sourcing strategy, categorization, governance) and operational (database, selection, contracts, performance monitoring).
2. **Role Combining:** At the minimum tier (T2), the supplier manager performs all activities directly, including those assigned to the supplier coordinator. The supplier manager role may also be combined with the service level manager at T2. The key requirement is that accountability for supplier management is explicitly assigned.
3. **Supplier Coordinator:** The supplier coordinator is an operational role that supports the supplier manager with day-to-day supplier management activities — maintaining the SMIS, coordinating the RfX process, preparing performance reports, managing onboarding/offboarding logistics, and maintaining the supplier dependency matrix and risk register. In larger organizations, this role is often associated with the procurement management function.
4. **Service Level Manager as Partner:** The service level manager works alongside supplier management, particularly in supplier selection (providing service level requirements), contracting (defining SLA/OLA/UA terms), and performance reviews (providing service level achievement data). SLM provides the service performance framework; supplier management provides the contractual and performance management framework.
5. **Service Owner Participation:** Service owners are consulted on activities affecting their services — supplier evaluation and selection, contract negotiation, performance reviews, and onboarding/offboarding. They are informed of outcomes that affect their service delivery.
6. **Governance Bodies:** At T2+, supplier governance committees or review boards may be established. These are not separate roles but structures that bring together the supplier manager, service level manager, service owners, finance, legal, and other stakeholders for governance decisions. The RACI matrix covers the supplier management side of governance activities.
7. **Cross-Practice Integration:** Many supplier management activities interface with other processes (Relationship Management owns the stakeholder engagement approach, Service Level Management provides the SLA/OLA/UA framework, Risk Management receives supplier risk assessments). The RACI matrix covers only the supplier management side — each partnering process has its own RACI for its activities.
