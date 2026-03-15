---
process_id: PR04
process_name: "Service Design"
category: raci
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T3
sources:
  - "ITIL 4: Service Design §4.1 Table 4.2, §4.1.1, §4.1.2, §4.2"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Design — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. This process applies only at T3 complexity but activities are still graduated by maturity within the practice. It is unusual to find a dedicated organizational structure for the service design practice — in product-based organizations, service design is integrated into product development and management teams. In more service-based or complex organizations, dedicated service design consultants or leaders may be appointed. The service design leader role may be performed by an enterprise architect, product owner, service delivery manager, or IT solution architect.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SDL | Service Design Leader | All |
| SDC | Service Design Consultant | All |
| SO | Service/Product Owner | All |

## Essential Activities (All tiers)

### Design Approach Development
<!-- sources: ITIL 4 Service Design §3.2.1 Table 3.2, §4.1 Table 4.2 -->

| Activity | SDL | SDC | SO |
|----------|:---:|:---:|:--:|
| Analyse service/product environment and requirements | A/R | C | R |
| Review and develop the service design approach | A/R | C | C |
| Review and develop service design models | A | R | C |
| Plan service design instances | I | A/R | R |
| Communicate service design plans | A/R | I | R |

## Intermediate Activities (T2+)

### Design Coordination
<!-- sources: ITIL 4 Service Design §3.2.2 Table 3.4, §4.1 Table 4.2 -->

| Activity | SDL | SDC | SO |
|----------|:---:|:---:|:--:|
| Identify applicable design model and plan activities | C | A/R | R |
| Orchestrate and coordinate service design execution | I | A/R | C |
| Review service design outcomes | A/R | R | R |

## Advanced Activities (T3)

### Risk Modelling and Practice Optimization
<!-- sources: ITIL 4 Service Design §2.2.5, §2.4, §4.1 Table 4.2 -->

| Activity | SDL | SDC | SO |
|----------|:---:|:---:|:--:|
| Model and manage service risk tiers | A/R | R | C |
| Optimize the service design practice | A/R | R | C |

## Notes

1. **Service Design Leader:** Accountable for the service design practice overall. Provides strategic direction and manages practice maturity. Develops the practice including training, communications, and processes. Governs service design processes and controls. Builds, utilizes, and governs service design packages. Competency profile: Leader, Methods expert, Coordinator (LMC). Requires good knowledge of the organization's products — architecture, services, and interdependencies — combined with solid design thinking skills and good risk management skills. This role may be performed by an enterprise architect, service delivery manager, or IT solution architect where a dedicated design role is not adopted.
2. **Service Design Consultant:** Develops and industrializes detailed service design activities. Focuses on detailed procedures, elements of service design packages, provision of consultancy to change initiatives, and orchestrating service provisioning. Accountable for coordinating design execution — managing requirements tracking, communications, information exchange, fast feedback, and data flow. Competency profile: Methods expert, Coordinator (MC). In less complex organizations, this role may be combined with the service design leader or performed by business analysts and service introduction specialists.
3. **Service/Product Owner:** Participates in environment and requirements analysis, instance planning, plan communication, and design review. Provides the product and service perspective, ensuring design outcomes meet business requirements. In product-based organizations, the product owner often performs the service design leader role as design is integrated into day-to-day product development and management.
4. **Role Combining:** In many organizations, dedicated service design roles are not adopted. Service design activities are undertaken by architects, business analysts, service introduction and readiness specialists, or product management teams. Only organizations with a complex mix of services and products typically elect to have a dedicated organizational structure for the practice.
5. **Additional Participants:** Beyond the three core roles, numerous other roles participate in service design activities — enterprise architects, project managers, development team members, systems administrators, account managers, delivery managers, customer representatives, information security specialists, risk managers, testing specialists, and users. Their involvement varies by activity and design instance complexity.
6. **Multi-Disciplinary Teams:** Design thinking is best applied by multi-disciplinary teams that balance the perspectives of customers, technology, the organization, partners, and suppliers. Design execution involves many internal and external teams coordinated by the service design consultant.
