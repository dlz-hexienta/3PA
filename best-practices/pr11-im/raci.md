---
process_id: PR11
process_name: "Incident Management"
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
  - "ITIL 4: Incident Management §4.1.1, §4.1.2, Table 4.2"
  - "FitSM-2: §PR9 ISRM (incident scope)"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (incident coordination)"
last_updated: 2026-03-13
status: draft
---

# Incident Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. At the minimum tier (T1), the incident manager performs major incident coordination directly. At T2+, the major incident manager role is introduced and takes over major incident coordination responsibilities. At T1, the incident manager may also perform service desk agent duties if no dedicated service desk exists.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| IM | Incident Manager | All |
| SDA | Service Desk Agent | All |
| TS | Technical Specialist | All |
| MIM | Major Incident Manager | T2+ |
| SO | Service Owner | All |

## Essential Activities (All tiers)

### Incident Detection and Registration
<!-- sources: ITIL 4 Incident Management §3.2.1 Table 3.2, §4.1.2 Table 4.2, FitSM-2 §PR9 ISRM -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Detect incidents from monitoring, events, or technical observation | A | I | R | — | — |
| Receive user-reported incidents via service desk channels | A | R | — | — | — |
| Register incidents in the ITSM tool with all required fields | A | R | C | — | — |

### Incident Classification and Prioritization
<!-- sources: ITIL 4 Incident Management §3.2.1 Table 3.2, §4.1.2 Table 4.2, FitSM-2 §PR9 ISRM -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Classify incidents using the defined classification scheme | A | R | C | — | — |
| Determine priority using the impact and urgency matrix | A | R | C | — | — |
| Check incidents against major incident criteria | A/R | C | C | — | — |
| Match incidents to existing incident models or known errors | A | R | C | — | — |

### Incident Diagnosis and Resolution
<!-- sources: ITIL 4 Incident Management §3.2.1 Table 3.2, §4.1.2 Table 4.2 -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Investigate and diagnose incidents | A | C | R | — | — |
| Engage additional specialists or suppliers for complex incidents | A/R | I | C | — | — |
| Apply resolution or workaround to restore service | A | I | R | — | — |
| Confirm service restoration with the user | A | R | C | — | — |

### Incident Closure
<!-- sources: ITIL 4 Incident Management §3.2.1 Table 3.2, §4.1.2 Table 4.2 -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Verify resolution with user and obtain confirmation | A | R | — | — | — |
| Complete the incident record with resolution details | A | R | C | — | — |
| Capture user satisfaction data | A | R | — | — | — |
| Raise problem record or change request where needed | A/R | C | C | — | — |

### Major Incident Handling
<!-- sources: ITIL 4 Incident Management §2.4.2, §4.1.1 (MIM), FitSM-2 §PR9 ISRM (manage major incidents) -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Identify incident as a major incident | A/R | C | C | — | I |
| Assign the major incident coordinator | A/R | I | I | — | I |
| Mobilize resources and coordinate the resolution effort | A/R | C | R | — | I |
| Communicate status to stakeholders at defined intervals | A/R | C | I | — | I |
| Resolve the major incident | A | I | R | — | I |
| Conduct the post-major-incident review | A/R | I | C | — | C |
| Document and distribute the major incident review report | A/R | I | I | — | I |

## Intermediate Activities (T2+)

### Major Incident Handling (T2+ — MIM role active)
<!-- sources: ITIL 4 Incident Management §4.1.1 (MIM role) -->

At T2+, the major incident manager role takes over coordination of major incidents. The essential major incident activities above are replaced by:

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Identify incident as a major incident | A | C | C | R | I |
| Assign the major incident coordinator | A | I | I | R | I |
| Mobilize resources and coordinate the resolution effort | I | C | R | A/R | I |
| Communicate status to stakeholders at defined intervals | I | C | I | A/R | I |
| Resolve the major incident | I | I | R | A | I |
| Conduct the post-major-incident review | C | I | C | A/R | C |
| Document and distribute the major incident review report | I | I | I | A/R | I |

### Incident Model Development and Maintenance
<!-- sources: ITIL 4 Incident Management §2.4.2, §3.2.2 Table 3.4, FitSM-2 §PR9 ISRM (manage workflows) -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Identify the need for new or updated incident models | A/R | C | C | C | — |
| Define the incident model (steps, roles, timescales, escalation) | A/R | C | C | — | — |
| Validate the model with resolver teams | A | C | R | — | — |
| Publish and communicate the model | A/R | I | I | I | — |
| Review models periodically for currency and effectiveness | A/R | C | C | C | — |

### Incident Escalation Management
<!-- sources: ITIL 4 Incident Management §2.4.2, FitSM-2 §PR9 ISRM (define escalation procedure) -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Define functional and hierarchical escalation paths | A/R | C | C | C | C |
| Apply escalation criteria and execute escalation | A | R | C | — | I |
| Monitor escalated incidents and manage priority conflicts | A/R | I | C | C | I |
| Review and update escalation paths periodically | A/R | C | C | C | — |

### Incident Reporting and Analysis
<!-- sources: ITIL 4 Incident Management §2.4.3, §2.5 Table 2.2, FitSM-2 §PR9 ISRM (regular incident reports) -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Extract incident data and analyse trends | A/R | — | C | C | — |
| Compile the incident report | A/R | — | — | C | — |
| Distribute reports and provide trend data to Problem Management | A/R | I | I | I | I |

## Advanced Activities (T3)

### Periodic Incident Review
<!-- sources: ITIL 4 Incident Management §2.4.3, §3.2.2 Tables 3.3, 3.4, §4.1.2 Table 4.2 -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Prepare the review (compile data, schedule, invite participants) | A/R | — | I | I | I |
| Review incident records and analyse data for systemic issues | A/R | C | C | C | C |
| Assess incident model effectiveness | A/R | C | C | C | — |
| Identify improvement opportunities | A/R | C | C | C | C |
| Register improvement initiatives and assign owners | A/R | I | I | I | I |

### Incident Model Improvement and Communication
<!-- sources: ITIL 4 Incident Management §3.2.2 Table 3.4 -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Initiate specific improvements to models and procedures | A/R | C | C | C | — |
| Communicate updated models and procedures to all affected teams | A/R | I | I | I | I |
| Track improvement implementation and report progress | A/R | — | C | C | I |

### Collaborative Resolution Approaches
<!-- sources: ITIL 4 Incident Management §4.2.1, §4.2.2 -->

| Activity | IM | SDA | TS | MIM | SO |
|----------|:--:|:---:|:--:|:---:|:--:|
| Design and implement swarming and collaborative resolution practices | A/R | C | C | C | C |
| Monitor effectiveness of collaborative resolution approaches | A/R | C | R | C | I |
| Adjust team structures and practices based on outcomes | A/R | I | C | C | C |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The incident manager is accountable for all incident management activities — from operational incident handling through to periodic review and improvement. At T2+, the major incident manager is accountable for major incident coordination activities.
2. **Role Combining:** At the minimum tier (T1), the incident manager performs all coordination activities directly, including major incident coordination and activities that would otherwise be performed by the major incident manager. The incident manager role may be combined with the service desk agent role at T1 if no dedicated service desk exists. The key requirement is that accountability for incident management is explicitly assigned.
3. **Major Incident Manager:** At T2+, the major incident manager is a dedicated role (or designated individual) responsible for coordinating the response to major incidents. The MIM has similar responsibilities to the incident manager but focuses exclusively on major incidents, with wider authority to mobilize resources and invoke emergency procedures. In some organizations, the MIM role rotates among experienced incident managers.
4. **Service Desk Agent:** The service desk agent is the first point of contact for user-reported incidents. They perform initial registration, classification, prioritization, and first-contact resolution. For incidents beyond first-contact resolution capability, the service desk agent escalates to technical specialists. At T1, the service desk agent role may be combined with the incident manager.
5. **Technical Specialist:** Technical specialists provide domain-specific expertise for incident diagnosis and resolution. They may be organized by technical domain, product/service, territory, or consumer type. At T3, technical specialists participate in swarming — working collaboratively across domain boundaries on complex incidents rather than following rigid tiered escalation.
6. **Service Owner Participation:** Service owners are informed of incidents affecting their services, particularly major incidents. They participate in post-major-incident reviews and periodic incident reviews, providing the service-level perspective on incident impact, resolution effectiveness, and improvement priorities.
7. **Third-Party Suppliers:** External suppliers are not listed as a separate RACI role but participate in incident diagnosis and resolution as technical specialists under their contractual arrangements. The incident manager (or MIM for major incidents) coordinates supplier involvement through the supplier management process. Incident models should define how third parties are involved in resolution for each incident type.
