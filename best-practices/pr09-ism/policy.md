---
process_id: PR09
process_name: "Information Security Management"
category: policy
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
  - "ITIL 4: Information Security Management"
  - "FitSM-2: §PR6 ISM"
  - "IT4IT: Cross-cutting (security governance)"
last_updated: 2026-03-13
status: draft
---

# Information Security Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Information Security Management §2, FitSM-2 §PR6 -->

The organization shall protect the confidentiality, integrity, and availability of all information needed to manage and deliver its services. This protection shall be achieved through a systematic approach to identifying, assessing, and treating information security risks; establishing and enforcing security policies and controls; detecting, responding to, and learning from security incidents; and embedding security considerations into all aspects of service management. The organization shall balance preventive, detective, and corrective controls across all relevant assets — including IT systems, data, people, processes, and supplier relationships — to maintain a security posture that is proportionate to its risk appetite and regulatory obligations.

## Objectives
<!-- sources: ITIL 4 Information Security Management §2.4 PSFs, FitSM-2 §PR6 -->

1. Develop and maintain information security policies and plans that address all relevant security domains and are aligned to business requirements, legislation, and contractual obligations
2. Identify, assess, and mitigate information security risks across all assets relevant to service delivery, maintaining residual risk within the organization's stated risk appetite
3. Regularly exercise and test security plans to validate their effectiveness and organizational readiness
4. Embed information security into all aspects of the organization's value system — including governance structures, value streams, practices, and continual improvement activities
5. Ensure all parties with access to organizational information (employees, contractors, suppliers) understand their security responsibilities and are equipped to fulfil them
6. Detect, respond to, and recover from security incidents effectively, learning from each event to strengthen the organization's security posture

## Scope

This policy applies to all information processed, stored, or transmitted by the organization in the course of managing and delivering its services. It covers:

- All information assets across the scope defined in the process definition (IT systems, infrastructure, software, endpoints, IoT, business processes, people, partners/suppliers, data)
- All security requirements derived from service level agreements, legislation and regulation, contractual obligations, and internal risk appetite
- All activities related to identifying, assessing, treating, and monitoring information security risks
- All roles with responsibility for information security, from the CISO through to all staff members
- All third parties (partners, suppliers, contractors) that access or process organizational information

## Principles

### P1. Risk-Based Approach
<!-- sources: ITIL 4 Information Security Management §2.2, FitSM-2 §PR6 -->
Security investments and controls shall be driven by risk assessment, not by compliance checklists alone. The organization shall identify threats, assess vulnerabilities, and treat risks using a defined methodology. Controls shall be proportionate to the assessed risk level, and residual risk shall be formally accepted by an authorized decision-maker.

### P2. Defence in Depth
<!-- sources: ITIL 4 Information Security Management §2.4 PSF2 -->
The organization shall maintain a balanced combination of preventive, detective, and corrective controls across all four dimensions of service management (organization and people, value streams and processes, information and technology, partners and suppliers). No single control or dimension shall be relied upon in isolation.

### P3. Least Privilege
<!-- sources: ITIL 4 Information Security Management §2.4, FitSM-2 §PR6 -->
Access to information, systems, and services shall be granted on the basis of demonstrated business need and limited to the minimum level required for the individual or system to perform its function. Access rights shall be reviewed regularly and revoked promptly when no longer required.

### P4. Security as Everyone's Responsibility
<!-- sources: ITIL 4 Information Security Management §4.1.3 -->
Every person in the organization contributes to information security — positively through following policies, reporting threats, and maintaining vigilance, or negatively through negligence or ignorance. The organization shall ensure all staff are aware of their security responsibilities through training, reinforcement, and inclusion of security requirements in every job description.

### P5. Security by Design
<!-- sources: ITIL 4 Information Security Management §2.4 PSF4 -->
Security requirements shall be identified and incorporated from the earliest stages of service design, development, and deployment — not applied retrospectively. All new or significantly changed services shall undergo security assessment before entering production.

### P6. Transparency and Accountability
<!-- sources: ITIL 4 Information Security Management §2.4 PSF1 -->
Accountability for information security shall be clearly assigned at all levels. Security policies, risk assessments, incident outcomes, and compliance status shall be reported to relevant stakeholders on a regular basis. The organization shall maintain audit trails that support accountability and non-repudiation.

### P7. Supplier Security Alignment
<!-- sources: ITIL 4 Information Security Management §6 -->
Partners and suppliers that access, process, or store organizational information shall be subject to security requirements that are aligned with the organization's own policies. Supplier access shall be controlled through technical measures (network isolation, authentication, encryption) and contractual measures (security clauses, audit rights, certification requirements).

### P8. Continual Security Improvement
<!-- sources: ITIL 4 Information Security Management §2.4 PSF3, PSF4 -->
The organization's security posture shall be subject to continual assessment and improvement. Security incidents, audit findings, exercise outcomes, and changes to the threat environment shall drive updates to policies, controls, and plans. Security improvement actions shall be tracked through the continual improvement register.

## Mandatory Requirements

### Essential (All Tiers)

| ID | Requirement |
|----|------------|
| ISM-R01 | An information asset inventory shall be maintained covering all assets critical to service delivery, with each asset classified by sensitivity and criticality |
| ISM-R02 | A risk assessment shall be performed and documented for all critical information assets, using a defined methodology |
| ISM-R03 | An overarching information security policy shall be defined, approved by management, and communicated to all relevant parties |
| ISM-R04 | Security controls shall be documented and mapped to the risks they mitigate, covering prevention, detection, and correction |
| ISM-R05 | Access rights shall be managed based on the principle of least privilege, with provisioning and de-provisioning procedures in place |
| ISM-R06 | A security incident management process shall be established covering detection, escalation, response, and post-incident review |
| ISM-R07 | All new or modified security controls shall be implemented through the change management process |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| ISM-R08 | Security audits shall be conducted at a defined cadence (at minimum annually) with documented findings and recommendations |
| ISM-R09 | Security awareness training shall be delivered to all staff at defined intervals, with completion tracked and reported |
| ISM-R10 | Security compliance shall be monitored on an ongoing basis, with periodic security reports produced for management |
| ISM-R11 | Supplier security requirements shall be documented in contracts and underpinning agreements, with compliance assessed regularly |
| ISM-R12 | Subordinate security policies shall be maintained for key domains: access control, information classification, remote access, malware protection, and personal data protection |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| ISM-R13 | End-to-end security monitoring shall be implemented using SIEM capabilities that correlate events across infrastructure, application, and network layers |
| ISM-R14 | Security incident response plans shall be exercised and tested at defined intervals (at minimum annually) through simulations or tabletop exercises |
| ISM-R15 | Security requirements shall be integrated into service design, development, and deployment processes, with security review gates in change and release workflows |
| ISM-R16 | Intrusion detection and prevention capabilities shall be deployed at critical network boundaries |

## Compliance and Review

- This policy shall be reviewed at least annually or following a significant security incident, a material change to the threat environment, or a change to applicable legislation or regulation
- Compliance with this policy shall be verified through scheduled security audits and management reviews
- Non-compliance shall be escalated to the Information Security Manager and CISO for remediation
- Exceptions to this policy require documented risk acceptance and approval from the CISO

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Level Management Policy (PR02) | SLAs may contain security targets that drive security requirements |
| Availability Management Policy (PR06) | Availability targets and redundancy requirements overlap with security resilience |
| Service Continuity Management Policy (PR07) | Business continuity and disaster recovery plans must address security scenarios |
| Service Desk Policy (PR10) | Service desk staff must recognize and escalate security incidents |
| Incident Management Policy (PR11) | Security incidents follow the incident management escalation path and may trigger major incident procedures |
| Change Management Policy (PR15) | Security controls are implemented through change management; security-sensitive changes require security assessment |
| Release & Deployment Policy (PR16) | Release processes must include security verification before deployment |
| Service Configuration Management Policy (PR17) | CMDB provides the asset and relationship data that underpins security risk assessment |
| Supplier Management Policy (PR23) | Supplier security requirements are coordinated through supplier governance |
| Continual Improvement Policy (PR24) | Security audit findings and incident lessons drive improvement initiatives |
