---
process_id: PR10
process_name: "Service Desk"
category: raci
frameworks:
  - itil-v4
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Service Desk §4.1 Table 4.2, §4.2"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Desk — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Unlike most other practices, the service desk typically has a dedicated team that focuses on performing its processes. The service desk team may be involved in activities of several practices — including incident management, service request management, problem management, and relationship management — but the RACI below covers only service desk practice activities. Two core roles are defined: the front-line agent and the manager who oversees the practice.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| SDA | Service Desk Agent | All |
| SDM | Service Desk Manager | All |

## Essential Activities (All tiers)

### User Query Handling
<!-- sources: ITIL 4 Service Desk §3.2.1, §4.1 Table 4.2 -->

| Activity | SDA | SDM |
|----------|:---:|:---:|
| Acknowledge and record user queries | A/R | I |
| Validate user queries | A/R | I |
| Triage user queries and initiate appropriate activities | A/R | I |

### Communicating to Users
<!-- sources: ITIL 4 Service Desk §3.2.2, §4.1 Table 4.2 -->

| Activity | SDA | SDM |
|----------|:---:|:---:|
| Identify target audience and communication channels | R | A |
| Package and send information to users | R | A/R |

## Intermediate Activities (T2+)

### Feedback and Improvement
<!-- sources: ITIL 4 Service Desk §3.2.2, §3.2.3, §4.1 Table 4.2 -->

| Activity | SDA | SDM |
|----------|:---:|:---:|
| Gather and process user feedback | R | A |
| Review service desk performance | C | A/R |
| Initiate and communicate service desk improvements | I | A/R |

## Advanced Activities (T3)

### Channel and Organizational Optimization
<!-- sources: ITIL 4 Service Desk §2.2.1, §4.2 -->

| Activity | SDA | SDM |
|----------|:---:|:---:|
| Implement and maintain omnichannel integration | C | A/R |
| Optimize service desk organization and sizing | I | A/R |

## Notes

1. **Service Desk Agent:** The front-line role handling all user interactions. Acknowledges, records, validates, and triages user queries. Identifies target audiences and communication channels for outgoing communications. Packages information using templates and corporate standards. Gathers and processes user feedback. Competency profile varies by activity: Coordinator/Communicator and Administrator (CA) for acknowledgement, Coordinator/Methods expert (CM) for validation, Methods expert/Administrator/Technical/Coordinator (MATC) for triage. Requires communication skills, writing skills, business and service awareness, some technical skills, understanding of user validation methods, and ability to demonstrate service empathy. Agents should be incentivized to record interactions — record keeping is invaluable for service quality data.
2. **Service Desk Manager:** Manages the service desk practice overall. Accountable for outgoing communication quality — approves and sends communications on behalf of the service provider. Reviews service desk performance and initiates improvement initiatives. Communicates improvements to stakeholders. Responsible for organizational model decisions, team sizing, and staffing. Competency profile: Leader/Methods expert (LM) for review, Methods expert/Administrator (MA) for improvement initiation, Coordinator/Technical (CT) for improvement communication. Requires decision-making and leadership skills, understanding of improvement processes, and technical skills for communication tools.
3. **Two-Role Model:** The service desk practice is distinctive in having only two named roles. This reflects the practice's focus on consistent, standardized operations — all agents follow the same procedures and quality standards. In larger organizations, senior agents, team leads, or shift supervisors may bridge between the agent and manager roles, but these are organizational variations rather than distinct practice roles.
4. **Organizational Structure Variations:** The service desk team may be structured as local (co-located with users), distributed (multiple locations), virtual (remote), or hybrid (combining elements — concierge, field services, offshore). Vertical structures use tiers/levels with escalation between them. Horizontal structures use swarming and shared backlogs. The choice affects how roles are performed but not the RACI structure.
5. **Cross-Practice Participation:** The service desk team frequently participates in activities of other practices — particularly incident management (first-line resolution), service request management (request fulfilment), and relationship management (satisfaction surveys). The RACI above covers only service desk practice activities. Service desk agents may hold additional RACI responsibilities in those other practices.
6. **Self-Service Automation:** Many activities — particularly query acknowledgement, validation, triage, and view delivery — may be fully automated through self-service portals, chatbots, and IVR systems. When automated, the agent role shifts from performing the activity to monitoring and maintaining the automation. The manager remains accountable.
