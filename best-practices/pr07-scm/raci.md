---
process_id: PR07
process_name: "Service Continuity Management"
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
  - "ITIL 4: Service Continuity Management §4.1 Table 4.2, §4.2"
  - "FitSM-3: §6.4 SACM Roles"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Continuity Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Service continuity management uses different organizational structures during business-as-usual (planning, testing) and during actual disasters (response, recovery). During recovery, the structure is based on three levels of continuity plans: executive (strategic), coordination (tactical), and specialist (operational). The three roles below cover the practice-specific activities across both modes.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SCM | Service Continuity Manager | T2+ |
| SO | Service Owner | T2+ |
| RC | Recovery Coordinator | T2+ |

## Essential Activities (T2+)

### Governance, BIA, and Planning
<!-- sources: ITIL 4 SCM §3.2.1, §3.2.2, §3.2.3, §4.1 Table 4.2 -->

| Activity | SCM | SO | RC |
|----------|:---:|:--:|:--:|
| Define scope and policy | A/R | C | I |
| Identify vital business functions and perform BIA | A/R | R | I |
| Develop service continuity strategies and plans | A/R | C | R |
| Invoke and execute service continuity plans | A/R | I | R |
| Develop and maintain awareness and exercise programme | A/R | I | C |

## Intermediate Activities (T2+)

### Testing and Auditing
<!-- sources: ITIL 4 SCM §3.2.4, §4.1 Table 4.2 -->

| Activity | SCM | SO | RC |
|----------|:---:|:--:|:--:|
| Perform exercises and test plans | A/R | C | R |
| Conduct service continuity audits | A/R | C | I |
| Assess and manage risk mitigation measures | A/R | C | I |

## Advanced Activities (T3)

### Review and Optimization
<!-- sources: ITIL 4 SCM §2.4.2, §6, §4.1 Table 4.2 -->

| Activity | SCM | SO | RC |
|----------|:---:|:--:|:--:|
| Review and optimize continuity arrangements | A/R | C | C |
| Integrate continuity with partners and suppliers | A/R | C | I |

## Notes

1. **Service Continuity Manager:** The central role managing the practice — accountable for governance, BIA coordination, strategy development, plan documentation, exercise programme, and audit coordination. Competency profile: Methods/Technical/Administrator (MTA) for plan development, Administrator/Coordinator/Methods (ACM) for exercise programme, Methods/Coordinator (MC) for scope definition. Corresponds to ITIL continuity administrator and FitSM process manager SACM (continuity scope). In smaller organizations, this role may be combined with availability management or risk management.
2. **Service Owner:** Provides business context and service-specific knowledge to BIA — identifies VBFs, analyses disruption consequences, validates recovery requirements, and inputs to strategy selection. Competency profile: Coordinator/Methods (CM) for VBF identification, Methods/Coordinator (MC) for disruption analysis. Multiple service owners participate depending on the scope of the BIA cycle. The service owner is consulted during planning and exercises to ensure continuity arrangements reflect current service architecture and business needs.
3. **Recovery Coordinator:** Leads recovery teams during exercises and actual invocations — coordinates response, recovery, and restoration activities at the tactical level. Responsible for plan development (ensuring plans are executable), initial and ongoing testing, and actual recovery execution. Competency profile: Coordinator/Administrator/Technical/Leader (CATL) for exercises and invocation. Multiple recovery coordinators may exist — one per product, service, business unit, site, or location, each with their own recovery team. Corresponds to FitSM case owner (continuity plan owner).
4. **Crisis Management Group:** Not a practice-specific role but an organizational structure that makes the invocation decision. Typically the executive level of the organization — senior management with overall authority. The SCM supports the crisis management group with information and recommendations; the group decides whether and how to invoke. During actual invocations, the SCM is accountable for practice execution while the crisis management group provides strategic direction.
5. **Recovery Team Structure:** During recovery, the organizational structure shifts from business-as-usual to a three-level structure: executive (strategic — crisis management, external communications, media), coordination (tactical — resource allocation, priority management, conflict resolution), and specialist (operational — recovery teams performing procedures by service or product). Recovery teams should be grouped by services and products within IT.
6. **Cross-Practice Involvement:** BIA involves service designers, architects, technical experts, relationship managers, and customers in addition to the roles above. Strategy development involves service designers and technical experts. Audits may involve internal or external auditors. The RACI above covers only service continuity management practice activities. Participants from other practices contribute as consulted parties through the service owner and recovery coordinator roles.
