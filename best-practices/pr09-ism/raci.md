---
process_id: PR09
process_name: "Information Security Management"
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
  - "ITIL 4: Information Security Management §4"
  - "FitSM-2: §PR6 ISM"
  - "IT4IT: Cross-cutting (security governance)"
last_updated: 2026-03-13
status: draft
---

# Information Security Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. Organizations at lower tiers may combine roles (e.g., the CISO and information security manager may be the same person at T1).

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| CISO | Chief Information Security Officer | All |
| ISM | Information Security Manager | All |
| ISA | Information Security Auditor | T2+ |
| SA | Security Analyst | T2+ |
| SecA | Security Architect | T3 |
| SSC | Supplier Security Coordinator | T3 |
| SO | Service Owner | All |
| SLM | Service Level Manager | All |

## Essential Activities (All Tiers)

### Risk Assessment and Controls

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Define risk assessment methodology | A | R | — | — | — | — | — | — |
| Inventory and classify information assets | I | A/R | — | — | — | — | C | — |
| Identify threats and vulnerabilities for critical assets | I | A/R | — | — | — | — | — | — |
| Assess risk levels and determine treatment | A | R | — | — | — | — | — | — |
| Accept residual risks | A/R | R | — | — | — | — | — | — |
| Define overarching security policy | A/R | R | — | — | — | — | I | I |
| Define subordinate security policies | A | R | — | — | — | — | I | — |
| Communicate security policies to all parties | I | A/R | — | — | — | — | I | I |
| Identify required security controls | I | A/R | — | — | — | — | — | — |
| Document controls in the security controls register | I | A/R | — | — | — | — | — | — |
| Submit change requests for control implementation | I | A/R | — | — | — | — | — | — |
| Verify control effectiveness after implementation | I | A/R | — | — | — | — | — | — |

### Access Rights Management

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Define access rights policy and role profiles | A | R | — | — | — | — | C | — |
| Provision access for joiners | I | A/R | — | — | — | — | — | — |
| Update access for movers | I | A/R | — | — | — | — | — | — |
| Revoke access for leavers | I | A/R | — | — | — | — | — | — |
| Process specific access requests | I | A/R | — | — | — | — | — | — |
| Conduct periodic access rights reviews | I | A/R | — | — | — | — | — | — |

### Security Incident Management

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Develop and maintain incident response plans | A | R | — | — | — | — | I | — |
| Define security incident roles and escalation paths | A | R | — | — | — | — | I | — |
| Detect potential security events | I | A | — | R | — | — | — | — |
| Perform initial assessment and classify incident | I | A/R | — | — | — | — | — | — |
| Log the security incident | I | A/R | — | — | — | — | — | — |
| Escalate confirmed incidents | I | A/R | — | — | — | — | I | — |
| Assess severity and scope | I | A | — | R | — | — | — | — |
| Preserve forensic evidence | I | I | — | A/R | — | — | — | — |
| Contain the incident | I | A | — | R | — | — | I | — |
| Eradicate root cause | I | A | — | R | — | — | — | — |
| Restore affected services | I | A | — | R | — | — | I | — |
| Confirm recovery and notify stakeholders | I | A/R | — | I | — | — | I | I |
| Conduct post-incident review | A | R | — | C | — | — | C | — |
| Identify and log improvement actions | A | R | — | C | — | — | — | — |

## Intermediate Activities (T2+)

### Security Audit and Review

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Define audit scope and baseline standards | A | R | C | — | — | — | — | — |
| Identify changes to business, technology, or threat environment | A | R | C | C | — | — | — | — |
| Identify missing controls (gap analysis) | I | A | R | R | — | — | — | — |
| Assess control effectiveness | I | A | R | R | — | — | — | — |
| Assess compliance with policies and procedures | I | I | A/R | C | — | — | — | — |
| Compile security audit report | I | A | R | C | — | — | — | — |
| Present findings to CISO and stakeholders | A | R | C | — | — | — | I | I |
| Submit remediation actions to improvement register | I | A/R | I | — | — | — | — | — |
| Update risk assessment based on audit findings | I | A/R | C | — | — | — | — | — |

### Security Awareness and Training

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Define security awareness training content | A | R | — | C | — | — | — | — |
| Identify target audience and delivery method | I | A/R | — | — | — | — | — | — |
| Deliver training to all staff | I | A/R | — | — | — | — | — | — |
| Track training completion and follow up | I | A/R | — | — | — | — | — | — |
| Assess training effectiveness | I | A | — | R | — | — | — | — |
| Reinforce security awareness through ongoing communications | I | A/R | — | — | — | — | — | — |

### Security Monitoring and Reporting

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Monitor security compliance continuously | I | A | — | R | — | — | — | — |
| Monitor for policy violations and unauthorized access | I | A | — | R | — | — | — | — |
| Produce periodic security reports | A | R | C | C | — | — | — | — |
| Distribute security reports to stakeholders | I | A/R | — | — | — | — | I | I |

## Advanced Activities (T3)

### End-to-End Security Monitoring

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Design and deploy SIEM capabilities | I | A | — | R | R | — | — | — |
| Implement IDS/IPS at critical boundaries | I | A | — | R | R | — | — | — |
| Define automated alerting and correlation rules | I | A | — | R | R | — | — | — |
| Integrate security monitoring with service monitoring | I | A | — | R | R | — | I | — |

### Security Testing and Exercises

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Plan and schedule security exercises | A | R | C | — | C | — | — | — |
| Conduct tabletop or red team exercises | I | R | C | R | C | — | C | — |
| Evaluate exercise outcomes and update plans | A | R | C | C | — | — | — | — |

### Security by Design

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Define security requirements for new services | I | C | — | — | A/R | — | C | C |
| Embed security review gates in change and release workflows | A | R | — | — | R | — | I | — |
| Conduct security assessment of new or changed services | I | C | — | R | A/R | — | — | — |

### Supplier Security Coordination

| Activity | CISO | ISM | ISA | SA | SecA | SSC | SO | SLM |
|----------|:----:|:---:|:---:|:--:|:----:|:---:|:--:|:---:|
| Define security requirements for supplier engagements | I | C | — | — | C | A/R | — | — |
| Include security clauses in contracts and UAs | I | C | — | — | — | A/R | — | — |
| Implement technical controls for supplier access | I | C | — | — | R | A | — | — |
| Verify supplier compliance at onboarding | I | I | — | — | — | A/R | — | — |
| Monitor supplier security on an ongoing basis | I | I | — | R | — | A | — | — |
| Conduct or commission supplier security assessments | I | I | R | — | — | A | — | — |
| Remediate supplier security findings | I | R | — | — | — | A | — | — |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The CISO is accountable for strategic and policy activities; the Information Security Manager is accountable for operational activities.
2. **Role Combining:** At T1, the CISO and Information Security Manager roles may be held by the same person. At T1, activities assigned to Security Analyst, Auditor, and Architect are absorbed by the Information Security Manager.
3. **Security as Cross-Cutting:** The Service Owner and Service Level Manager participate as consulted or informed parties because security requirements affect all services. They do not own security activities but must be engaged when security decisions impact service delivery.
4. **Incident Escalation:** At T1, security incidents are detected and managed by the Information Security Manager. At T2+, the Security Analyst takes the responsible role for detection, triage, containment, and recovery under the Information Security Manager's accountability.
5. **Two-Process Structure:** Activities are organized following the ITIL 4 structure of two processes (security incident management and audit/review) plus cross-cutting security governance activities. All operate in parallel.
6. **Supplier Security at T3:** At T1–T2, supplier security activities are handled by the Information Security Manager. At T3, the Supplier Security Coordinator takes accountability, working with the Security Architect for technical controls and the Information Security Auditor for supplier assessments.
