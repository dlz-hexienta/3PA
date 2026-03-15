---
process_id: PR13
process_name: "Problem Management"
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
  - "ITIL 4: Problem Management §4.1.1, §4.1.2 Table 4.2, §4.2"
  - "FitSM-2: §PR10 PM"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (problem coordination)"
last_updated: 2026-03-13
status: draft
---

# Problem Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. At the minimum tier (T1), the problem manager performs problem coordination activities directly. At T2+, the problem coordinator role is introduced and takes over routine activities (problem registration, tracking, KEDB maintenance, report compilation). At T1, the problem manager may also perform some technical specialist duties for problem investigation if no dedicated specialists are available.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| PM | Problem Manager | All |
| TS | Technical Specialist | All |
| PC | Problem Coordinator | T2+ |
| IM | Incident Manager | All |
| SO | Service Owner | All |

## Essential Activities (All tiers)

### Reactive Problem Identification
<!-- sources: ITIL 4 Problem Management §3.2.2 Tables 3.4, 3.5, §4.1.2 Table 4.2 -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Detect the need for problem investigation from incident data | A | C | — | R | C |
| Register the problem in the ITSM tool | A/R | C | — | C | — |
| Perform initial categorization of the problem | A/R | C | — | C | — |
| Assign the problem to the appropriate specialist group | A/R | I | — | I | — |

### Problem Investigation (Problem Control)
<!-- sources: ITIL 4 Problem Management §3.2.3 Tables 3.6, 3.7, §4.1.2 Table 4.2 -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Investigate the problem using structured analysis techniques | A | R | — | C | C |
| Determine the relevance and status of the problem | A/R | C | — | — | C |
| Document the known error in the KEDB | A/R | C | — | I | I |
| Communicate known error findings to incident management and relevant teams | A/R | C | — | I | I |

### Problem Resolution and Closure (Error Control)
<!-- sources: ITIL 4 Problem Management §3.2.4 Tables 3.8, 3.9, §4.1.2 Table 4.2 -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Develop the problem solution (select mitigation approach) | A | R | — | C | C |
| Initiate problem resolution (submit change requests or other actions) | A/R | C | — | I | I |
| Verify the resolution (confirm problem is eliminated) | A | R | — | C | C |
| Close the problem and update the KEDB | A/R | C | — | I | I |

## Intermediate Activities (T2+)

### Reactive Problem Identification (T2+ — PC role active)
<!-- sources: ITIL 4 Problem Management §4.1.2 Table 4.2 (problem coordinator) -->

At T2+, the problem coordinator takes over routine problem registration and tracking activities. The essential reactive identification activities above are augmented by:

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Register the problem in the ITSM tool | A | C | R | C | — |
| Perform initial categorization of the problem | A | C | R | C | — |
| Assign the problem to the appropriate specialist group | A/R | I | C | I | — |

### Proactive Problem Identification
<!-- sources: ITIL 4 Problem Management §3.2.1 Tables 3.1, 3.2, 3.3, §4.1.2 Table 4.2 -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Review submitted information (vendor advisories, monitoring data, community reports) | A | R | C | — | — |
| Register the proactively identified problem | A | C | R | — | — |
| Perform initial categorization and assignment | A/R | C | C | — | I |

### Problem Investigation (T2+ — PC role active)
<!-- sources: ITIL 4 Problem Management §4.1.2 Table 4.2 -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Investigate the problem using structured analysis techniques | A | R | C | C | C |
| Document the known error in the KEDB | A | C | R | I | I |
| Communicate known error findings to incident management and relevant teams | A | C | R | I | I |

### Problem Model Development and Maintenance
<!-- sources: ITIL 4 Problem Management §2.2.4, §3.2.4 Table 3.8 (problem models output) -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Identify the need for new or updated problem models | A/R | C | C | C | — |
| Define the problem model (techniques, steps, roles, timescales) | A/R | C | C | — | — |
| Validate the model with specialist teams | A | R | C | — | — |
| Publish and communicate the model | A/R | I | I | I | — |

### Problem Reporting and Analysis
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3, FitSM-2 §PR10 PM -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Extract problem data and KEDB data | A | — | R | — | — |
| Analyse trends and patterns | A/R | C | C | C | — |
| Compile the problem report | A/R | — | C | — | — |
| Distribute reports and provide data to incident management and service level management | A/R | I | I | I | I |

## Advanced Activities (T3)

### Known Error Monitoring and Review
<!-- sources: ITIL 4 Problem Management §3.2.4 Table 3.9 (known error monitoring and review), §4.1.2 Table 4.2 -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Review active known errors (incident dynamics, workaround effectiveness, resolution options) | A/R | C | C | C | C |
| Reassess the mitigation approach and re-initiate solution development where needed | A | R | C | C | C |
| Update or create problem models based on review findings | A/R | C | C | I | — |
| Assess accumulated technical debt from deferred resolutions | A/R | C | C | — | C |

### Continual Improvement of Problem Management
<!-- sources: ITIL 4 Problem Management §2.4.2 -->

| Activity | PM | TS | PC | IM | SO |
|----------|:--:|:--:|:--:|:--:|:--:|
| Review problem management effectiveness (techniques, KEDB quality, collaboration) | A/R | C | C | C | C |
| Identify improvement opportunities | A/R | C | C | C | C |
| Register improvement initiatives and assign owners | A/R | I | I | I | I |
| Track improvement implementation and report progress | A/R | — | C | — | I |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The problem manager is accountable for all problem management activities — from problem identification through investigation, resolution, closure, and continual improvement.
2. **Role Combining:** At the minimum tier (T1), the problem manager performs all coordination activities directly, including the routine activities that the problem coordinator would handle at T2+. In many organizations, the problem manager role is not a full-time position — it may be combined with other roles or rotated among experienced specialists, particularly in smaller organizations or those with a lower volume of problems.
3. **Problem Coordinator:** At T2+, the problem coordinator is introduced to handle routine problem management activities — problem registration, tracking, KEDB maintenance, and report compilation. This allows the problem manager to focus on coordination, prioritization, and process effectiveness. In some organizations, the problem coordinator role is delegated to existing specialist roles.
4. **Technical Specialist:** Technical specialists provide domain-specific expertise for problem investigation and root cause analysis. Investigation teams are typically temporary — formed for the duration of a specific problem investigation and disbanded after resolution. The specialist team responsible for the CI, service, or product associated with the problem usually leads the investigation.
5. **Incident Manager Participation:** The incident manager is a key contributor to reactive problem identification — detecting the need for problem investigation from incident patterns, recurring incidents, and major incident reviews. The incident manager is also a primary consumer of known error and workaround information from the KEDB. Maintaining effective collaboration between problem management and incident management is critical to the value of both practices.
6. **Service Owner Participation:** Service owners provide the business-level perspective on problems affecting their services — including impact assessment, prioritization input, and acceptance of risk when problems are managed through workarounds rather than permanent fixes. Service owners participate in problem reviews and mitigation approach decisions for problems affecting their services.
7. **Third-Party Suppliers:** External suppliers are not listed as a separate RACI role but participate in problem investigation and resolution as technical specialists under their contractual arrangements. Problem models should define how third parties are involved in problem control and error control for each problem type. The possibility of resolving third-party errors depends on the architecture of the solution, the flexibility of the supplier, and the contractual terms.
