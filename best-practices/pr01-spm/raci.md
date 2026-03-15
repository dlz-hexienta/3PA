---
process_id: PR01
process_name: "Service Portfolio Management"
category: raci
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Portfolio Management"
  - "FitSM-2: §PR1 SPM"
  - "IT4IT: Evaluate Value Stream, Portfolio Function"
last_updated: 2026-03-13
status: draft
---

# Service Portfolio Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. Organizations at lower tiers may combine roles (e.g., portfolio owner and manager may be the same person at T1).

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SPO | Service Portfolio Owner | All |
| SPM | Service Portfolio Manager | All |
| PC | Portfolio Coordinator | T2+ |
| BA | Business Analyst | T2+ |
| FM | Finance Manager | T2+ |
| IM | Investment Manager | T3 |
| EA | Enterprise Architect | T3 |
| PMO | PMO Representative | T3 |

## Essential Activities (All Tiers)

| Activity | SPO | SPM | PC | BA | FM | IM | EA | PMO |
|----------|:---:|:---:|:--:|:--:|:--:|:--:|:--:|:---:|
| Define the portfolio management approach | A | R | — | — | — | — | — | — |
| Approve the portfolio management approach | R/A | C | — | — | — | — | — | — |
| Establish the initial service portfolio | I | A/R | — | — | — | — | — | — |
| Define service specification template | I | A/R | — | — | — | — | — | — |
| Define assessment criteria for proposals | A | R | — | — | — | — | — | — |
| Submit a new service proposal | I | I | — | R | — | — | — | — |
| Review proposal for completeness | I | A/R | — | — | — | — | — | — |
| Evaluate proposal against criteria | I | A/R | — | C | — | — | — | — |
| Approve/reject proposals (within thresholds) | I | A/R | — | — | — | — | — | — |
| Approve/reject proposals (above thresholds) | A/R | R | — | — | — | — | — | — |
| Add approved service to portfolio | I | A/R | — | — | — | — | — | — |
| Update service lifecycle stage | I | A/R | — | — | — | — | — | — |
| Initiate service retirement | A | R | — | — | — | — | — | — |
| Execute service retirement plan | I | A/R | — | — | — | — | — | — |
| Maintain the service portfolio register | I | A/R | — | — | — | — | — | — |

## Intermediate Activities (T2+)

| Activity | SPO | SPM | PC | BA | FM | IM | EA | PMO |
|----------|:---:|:---:|:--:|:--:|:--:|:--:|:--:|:---:|
| Monitor portfolio item performance | I | A | — | R | R | — | — | — |
| Produce portfolio health reports | I | A | R | C | C | — | — | — |
| Prepare portfolio review agenda and materials | I | C | A/R | — | — | — | — | — |
| Conduct portfolio review meeting | A | R | R | C | C | — | — | — |
| Make portfolio investment decisions | A/R | R | I | C | C | — | — | — |
| Reprioritize existing portfolio items | A | R | I | C | C | — | — | — |
| Document portfolio review decisions | I | C | A/R | — | — | — | — | — |
| Distribute portfolio review report | I | I | A/R | — | — | — | — | — |
| Conduct periodic portfolio assessment | I | A | R | R | R | — | — | — |
| Communicate portfolio approach to stakeholders | C | A/R | R | — | — | — | — | — |
| Review and adjust portfolio models | A | R | I | C | C | — | — | — |

## Advanced Activities (T3)

| Activity | SPO | SPM | PC | BA | FM | IM | EA | PMO |
|----------|:---:|:---:|:--:|:--:|:--:|:--:|:--:|:---:|
| Create scope agreement for approved items | I | C | — | R | C | A | — | — |
| Validate resource consumption models | I | I | — | — | C | A/R | — | C |
| Define benefits (tangible/intangible) | I | C | — | R | C | A | — | — |
| Approve scope agreements | A | R | I | — | C | C | C | — |
| Track scope agreement delivery | I | I | — | — | — | A/R | — | R |
| Compare planned vs. actual benefits | I | C | — | R | R | A | — | — |
| Align portfolio to architecture roadmap | I | C | — | — | — | C | A/R | — |
| Validate portfolio-architecture compliance | I | I | — | — | — | — | A/R | — |
| Segment portfolio (market/internal/foundational) | A | R | I | C | — | C | C | — |
| Rationalize portfolio (identify consolidation) | I | A/R | — | R | C | C | C | — |
| Coordinate programme/project portfolio alignment | I | C | — | — | — | C | — | A/R |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". Where the portfolio owner is A, the portfolio manager typically executes (R).
2. **Role Combining:** At T1, the portfolio owner and manager roles may be held by the same person. At T1, BA/FM/PC activities in intermediate rows are absorbed by the portfolio manager.
3. **Escalation:** Proposals exceeding defined investment thresholds require portfolio owner approval; those within thresholds may be approved by the portfolio manager alone.
4. **Review Board:** At T3, the portfolio review may include a formal review board comprising SPO, FM, EA, IM, and PMO. The SPO retains accountability for decisions.
