---
process_id: PR05
process_name: "Service Catalogue Management"
category: raci
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Service Catalogue Management §4.1 Table 4.2, §4.1.1, §4.2"
  - "FitSM-2: §PR2 SLM"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Catalogue Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. The service catalogue manager is the central role accountable for the practice overall. In larger organizations, one or more employees may be fully dedicated to this role. In smaller organizations, the role may be combined with other service management roles. The second process (providing catalogue views) is normally fully automated — manual RACI assignments apply only to exception cases.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SCM | Service Catalogue Manager | All |
| SO | Service Owner | All |
| TS | Technical Specialist | All |

## Essential Activities (All tiers)

### Design and Structure the Catalogue
<!-- sources: ITIL 4 Service Catalogue Management §3.2.1 Table 3.2, §4.1 Table 4.2 -->

| Activity | SCM | SO | TS |
|----------|:---:|:--:|:--:|
| Analyse stakeholder requirements | A/R | C | I |
| Define service catalogue data structure | A/R | I | R |
| Define and agree standard catalogue views | A/R | C | R |
| Collect and maintain service catalogue data | A/R | R | R |

## Intermediate Activities (T2+)

### Deliver Views and Maintain Quality
<!-- sources: ITIL 4 Service Catalogue Management §3.2.2 Table 3.4, §4.1 Table 4.2 -->

| Activity | SCM | SO | TS |
|----------|:---:|:--:|:--:|
| Provide catalogue views to stakeholders | A/R | I | R |
| Monitor and maintain catalogue data quality | A/R | R | C |
| Gather and process user feedback | A/R | I | I |

## Advanced Activities (T3)

### Integration and Optimization
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2, §6, §4.1 Table 4.2 -->

| Activity | SCM | SO | TS |
|----------|:---:|:--:|:--:|
| Integrate with external data sources and supplier catalogues | A/R | I | R |
| Optimize catalogue usability and user experience | A/R | C | R |

## Notes

1. **Service Catalogue Manager:** Accountable for the service catalogue practice overall. Defines, designs, and maintains the catalogue. Understands and manages stakeholder relationships. Continually improves catalogue structure, automation, and views. Integrates the catalogue into value streams. Acts as customer for catalogue automation solutions — participating in requirements definition, selection, and implementation. Requires understanding of stakeholders' work and needs, analytical skills, knowledge of data architecture, communication skills, and design thinking. In larger organizations, this may be a dedicated full-time position; in smaller organizations, it may be combined with service management, business analysis, or relationship management roles.
2. **Service Owner:** Responsible for maintaining the accuracy of catalogue data for their services — providing service descriptions, status updates, target audience information, and other service-specific content. Consulted during stakeholder requirements analysis and standard view definition. Multiple service owners contribute to the catalogue, each for their own services.
3. **Technical Specialist:** Responsible for the technical implementation of the catalogue — data modelling, integration development, view implementation, and tooling. Supports the service catalogue manager in defining the data structure and implementing standard views. Manages external data integrations and resolves technical issues. May include service architects, database administrators, and ITSM tool administrators.
4. **Dedicated Team Conditions:** A dedicated service catalogue management team is more common when the catalogue is complex and critical for the organization's business, there is insufficient automation requiring manual work, or requirements for structure and content are constantly changing.
5. **Additional Participants:** Beyond the three core roles, relationship managers, business analysts, supplier managers, service desk agents, and account managers participate in various activities — particularly requirements analysis, view definition, and manual view request processing. Their involvement depends on the organization's structure and the level of automation.
6. **Automation Impact:** The second process (providing catalogue views) is normally fully automated through self-service portals. The manual RACI assignments for activity 5 apply only to exception and non-standard requests. When fully automated, the SCM and TS roles shift to monitoring and maintaining the automation rather than processing individual requests.
