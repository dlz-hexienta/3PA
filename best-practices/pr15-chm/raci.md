---
process_id: PR15
process_name: "Change Management"
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
tier_minimum: all
sources:
  - "ITIL 4: Change Enablement §4.1.1, §4.1.2, §4.1.3 Table 4.2, §4.2"
  - "FitSM-2: §PR12 CHM"
  - "IT4IT: R2D Value Stream"
  - "SIAM: Service Integration (change coordination)"
last_updated: 2026-03-13
status: draft
---

# Change Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. At the minimum tier (T1), the change manager performs coordination activities directly. At T2+, the change coordinator role is introduced and takes over routine processing within defined scopes. The change authority role varies by change model — from automated authorization for standard changes, through delegated authority for low-risk normal changes, to formal management authorization for high-risk changes.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| CM | Change Manager | All |
| CC | Change Coordinator | T2+ |
| CA | Change Authority | All |
| SO | Service Owner | All |
| TS | Technical Specialist | All |

## Essential Activities (All tiers)

### Change Lifecycle Management
<!-- sources: ITIL 4 Change Enablement §3.2.1 Tables 3.1, 3.2, §4.1.3 Table 4.2, FitSM-2 §PR12 CHM -->

| Activity | CM | CC | CA | SO | TS |
|----------|:--:|:--:|:--:|:--:|:--:|
| Register the change request | A/R | — | — | C | — |
| Classify the change (standard, normal, emergency) | A/R | — | — | C | C |
| Assess the change (impact, risk, resources, feasibility) | A | — | C | C | R |
| Authorize the change | I | — | A/R | C | C |
| Plan and schedule the change | A/R | — | — | C | C |
| Control change realization | A/R | — | — | C | R |
| Review and close the change | A/R | — | C | C | C |

### Emergency Change Handling
<!-- sources: ITIL 4 Change Enablement §2.2.1 (emergency changes), FitSM-2 §PR12 CHM (emergency changes) -->

| Activity | CM | CC | CA | SO | TS |
|----------|:--:|:--:|:--:|:--:|:--:|
| Identify the change as emergency | A/R | — | — | C | C |
| Register the emergency change | A/R | — | — | I | I |
| Perform expedited assessment | A | — | C | C | R |
| Obtain emergency authorization | I | — | A/R | C | C |
| Implement the emergency change | A | — | I | I | R |
| Complete the change record | A/R | — | — | I | C |
| Conduct the post-implementation review | A/R | — | C | C | C |

## Intermediate Activities (T2+)

### Change Lifecycle Management (T2+ — CC role active)
<!-- sources: ITIL 4 Change Enablement §4.1.1 (change coordinator) -->

At T2+, the change coordinator takes over routine change processing within defined scopes. The essential lifecycle activities above are augmented by:

| Activity | CM | CC | CA | SO | TS |
|----------|:--:|:--:|:--:|:--:|:--:|
| Register the change request | A | R | — | C | — |
| Classify the change (standard, normal, emergency) | A | R | — | C | C |
| Plan and schedule the change | A | R | — | C | C |
| Control change realization | A | R | — | C | R |
| Review and close the change | A | R | C | C | C |

### Change Model and Standard Change Development
<!-- sources: ITIL 4 Change Enablement §3.2.2 Tables 3.3, 3.4, §4.1.3 Table 4.2 -->

| Activity | CM | CC | CA | SO | TS |
|----------|:--:|:--:|:--:|:--:|:--:|
| Identify the need for new or updated change models | A/R | C | — | C | C |
| Define the change model or standard change procedure | A/R | C | C | C | C |
| Validate the model with specialist teams and service owners | A | C | C | R | R |
| Authorize and publish the model | A/R | I | C | I | I |
| Review models periodically for currency and effectiveness | A/R | C | — | C | C |

### Change Schedule Management
<!-- sources: ITIL 4 Change Enablement §2.3, §3.2.1, FitSM-2 §PR12 CHM (create a schedule of changes) -->

| Activity | CM | CC | CA | SO | TS |
|----------|:--:|:--:|:--:|:--:|:--:|
| Maintain and publish the change schedule | A/R | C | — | I | I |
| Identify and resolve scheduling conflicts | A/R | C | — | C | C |
| Coordinate change windows with release management | A/R | C | — | C | I |

### Change Reporting
<!-- sources: ITIL 4 Change Enablement §2.5 Table 2.4 -->

| Activity | CM | CC | CA | SO | TS |
|----------|:--:|:--:|:--:|:--:|:--:|
| Extract change data | A | R | — | — | — |
| Analyse trends and patterns | A/R | C | — | C | — |
| Compile the change report | A/R | C | — | — | — |
| Distribute reports to stakeholders | A/R | I | I | I | I |

## Advanced Activities (T3)

### Change Review Analysis and Optimization
<!-- sources: ITIL 4 Change Enablement §3.2.2 Tables 3.3, 3.4, §4.1.3 Table 4.2 -->

| Activity | CM | CC | CA | SO | TS |
|----------|:--:|:--:|:--:|:--:|:--:|
| Select and analyse changes for detailed review | A/R | C | — | C | C |
| Assess change model effectiveness | A/R | C | C | C | C |
| Identify improvement opportunities | A/R | C | C | C | C |
| Initiate improvements and register in CI register | A/R | I | I | I | I |
| Communicate updated models and findings | A/R | I | I | I | I |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The change manager is accountable for all change management activities — from change registration through review and closure, as well as change model development and practice optimization. The change authority is accountable specifically for authorization decisions.
2. **Role Combining:** At the minimum tier (T1), the change manager performs all coordination activities directly, including the routine processing that the change coordinator would handle at T2+. In smaller organizations, the change manager role may be combined with other roles. The key requirement is that accountability for change management is explicitly assigned.
3. **Change Coordinator:** At T2+, the change coordinator is introduced to handle routine change processing within defined scopes — specific change types, territories, or parts of the organization. This allows the change manager to focus on practice-level coordination, change model management, and practice optimization.
4. **Change Authority:** The change authority role varies by change model and change type. For standard changes, authorization is pre-granted through the approved standard change procedure (no per-instance authorization needed). For low-risk normal changes, the change authority may be a service owner, technical lead, or automated system. For high-risk normal changes, the change authority may be a management board or equivalent. For emergency changes, a dedicated emergency change authority with high availability is designated. The organization should avoid establishing formal committees (CABs) as the default change authority, as these can become bottlenecks.
5. **Service Owner:** Service owners provide the service-level perspective on changes affecting their services — including impact assessment, risk evaluation, and authorization input. Service owners may serve as change authority for changes within their service scope. They participate in change reviews and post-implementation reviews for changes affecting their services.
6. **Technical Specialist:** Technical specialists provide domain-specific expertise for change assessment, planning, and realization. They perform the actual implementation of changes and may be internal staff or third-party supplier personnel. Technical specialists are consulted during assessment and authorization for their expert input on feasibility, risks, and dependencies.
7. **Third-Party Suppliers:** External suppliers are not listed as a separate RACI role but participate in change realization as technical specialists under their contractual arrangements. Change models should define how third parties are involved in change planning and realization and how the organization ensures the flow of changes through supplier boundaries.
