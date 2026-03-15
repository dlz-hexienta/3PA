---
process_id: PR03
process_name: "Service Financial Management"
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
  - "ITIL 4: Service Financial Management §4.1 Table 4.2, §4.1.1, §4.2"
  - "IT4IT: S2P Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Financial Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. This process applies only at T3 complexity but activities are still graduated by maturity within the practice. The service financial manager role may be performed by team managers, programme and project managers, product owners, or service owners depending on the approach adopted. In organizations where digital technology is a supporting resource, the executive IT manager and their team may perform most financial management activities. In digital organizations, dedicated staff, tools, and management efforts support the practice.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SFM | Service Financial Manager | All |
| EL | Executive Leader | All |
| FBP | Finance Business Partner | All |

## Essential Activities (All tiers)

### Define and Maintain the Approach
<!-- sources: ITIL 4 Service Financial Management §3.2.1 Table 3.2, §4.1 Table 4.2 -->

| Activity | SFM | EL | FBP |
|----------|:---:|:--:|:---:|
| Analyse stakeholder requirements | A/R | R | C |
| Define and agree the SFM approach | R | A | C |
| Communicate and integrate the approach | A/R | R | I |

### Financial Planning
<!-- sources: ITIL 4 Service Financial Management §3.2.2 Table 3.4, §4.1 Table 4.2 -->

| Activity | SFM | EL | FBP |
|----------|:---:|:--:|:---:|
| Estimate costs and income | A/R | I | R |
| Compile and agree budgets | R | A | C |

## Intermediate Activities (T2+)

### Budget Execution
<!-- sources: ITIL 4 Service Financial Management §3.2.2 Table 3.4, §4.1 Table 4.2 -->

| Activity | SFM | EL | FBP |
|----------|:---:|:--:|:---:|
| Monitor and control costs and income | A/R | I | C |
| Review and report on budgets | A/R | I | C |

### Management Accounting
<!-- sources: ITIL 4 Service Financial Management §3.2.3 Table 3.6, §4.1 Table 4.2 -->

| Activity | SFM | EL | FBP |
|----------|:---:|:--:|:---:|
| Identify and capture costs | A/R | I | R |
| Perform cost allocation | A/R | I | R |

## Advanced Activities (T3)

### Reporting and Optimization
<!-- sources: ITIL 4 Service Financial Management §3.2.1 Table 3.2, §3.2.3 Table 3.6, §4.1 Table 4.2 -->

| Activity | SFM | EL | FBP |
|----------|:---:|:--:|:---:|
| Provide standard and tailored financial reports | A/R | I | C |
| Review and adjust the approach | R | A | C |

## Notes

1. **Service Financial Manager:** Accountable for the service financial management practice overall. Performs management accounting — identifying, capturing, and allocating costs. Monitors and controls budgets. Produces financial reports. Reviews and adjusts the approach. This role requires analytical skills, knowledge of financial management theory and practice, excellent understanding of the organization's architectures and products, and good understanding of stakeholder needs. The role may be performed by team managers, programme and project managers, product owners, or service owners depending on the organization's approach.
2. **Executive Leader:** Decides whether to invest in developing the service financial management approach. Approves the approach, budgets, and changes to the approach. Provides strategic direction. In internal IT service providers, this may be the CIO or IT director. In external digital service providers, this may include the CEO, CFO, or CPO. The executive leader is accountable for the approach and budget approval decisions — ensuring that these are aligned with organizational strategy.
3. **Finance Business Partner:** Provides specialized financial management expertise to digital product and service teams. Bridges the gap between product and service management expertise and financial management expertise. May be a financial professional embedded in product teams, or a digital and IT business partner within the finance team. Responsible for the financial dimensions of cost estimation and cost capture — providing expertise in cost analysis, allocation methods, and financial data interpretation. Consulted on approach definition, cost model design, and budget compilation.
4. **Role Combining:** In smaller organizations or internal IT providers where digital technology is a supporting resource, the SFM and FBP roles may be combined — with team managers or product owners performing both the service management and financial dimensions. As the organization's digital maturity increases, dedicated financial expertise becomes more important.
5. **Organizational Solutions:** The source identifies four models for organizing the practice: (a) financial professionals embedded in digital product teams, (b) digital business partners within the finance team, (c) a dedicated finance team within IT collaborating with enterprise finance, or (d) specialized training for product managers and IT leaders. The choice of model affects how roles are assigned.
6. **Additional Participants:** Beyond the three core roles, product and service owners, programme and project managers, architects, and consultants participate in many activities. Product and service owners are particularly involved in estimation, budgeting, and cost allocation for their products. Architects contribute to approach definition and review — ensuring cost models reflect the organization's actual architectures.
