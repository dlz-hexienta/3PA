---
process_id: PR09
process_name: "Information Security Management"
category: procedures
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
  - "ITIL 4: Information Security Management §3, §4, §6"
  - "FitSM-2: §PR6 ISM"
  - "IT4IT: Cross-cutting (security governance)"
last_updated: 2026-03-13
status: draft
---

# Information Security Management — Best Practice Procedures

## PROC-ISM-01: Perform Risk Assessment

**Maturity:** Essential | **Trigger:** Initial process establishment, periodic review cycle (at minimum annually), significant change to asset landscape, threat environment, or business context

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Define or confirm the risk assessment methodology: establish criteria for evaluating likelihood and impact, define the risk rating scale, and set the threshold for acceptable residual risk aligned to the organization's risk appetite | CISO / Information Security Manager | Risk Assessment Methodology |
| 2 | Identify the assets in scope: retrieve the current information asset inventory, confirm completeness, and add any new or changed assets discovered since the last assessment | Information Security Manager | Information Asset Inventory |
| 3 | For each critical asset, identify applicable threats: consider threat actors (external attackers, insiders, automated systems), threat types (technical, physical, human), and current threat intelligence | Information Security Manager / Security Analyst | — |
| 4 | For each critical asset, identify vulnerabilities: assess weaknesses in controls, configurations, processes, and human factors that could be exploited by identified threats | Information Security Manager / Security Analyst | — |
| 5 | Assess risk for each threat–vulnerability pair: evaluate the likelihood of the threat exploiting the vulnerability and the potential impact on confidentiality, integrity, and availability. Assign a risk rating using the defined scale | Information Security Manager / Security Analyst | — |
| 6 | Determine risk treatment for each assessed risk: select from avoidance (eliminate the risk source), modification (apply or strengthen controls), sharing (transfer to a third party), or retention (formally accept the residual risk) | CISO / Information Security Manager | — |
| 7 | Document the risk assessment results: record all identified risks, their ratings, selected treatments, required controls, and accepted residual risks in the risk assessment report | Information Security Manager | Risk Assessment Report |
| 8 | Obtain formal acceptance of residual risks from the CISO or delegated risk owner | CISO | Signed Risk Acceptance |
| 9 | Feed risk treatment actions into the security controls register and submit change requests for any new or modified controls required | Information Security Manager | Security Controls Register |

### Exit Criteria
- All critical assets assessed for threats and vulnerabilities
- Risk ratings assigned using the defined methodology
- Risk treatment decisions documented for every identified risk
- Residual risks formally accepted by an authorized decision-maker
- Control implementation actions submitted to change management

---

## PROC-ISM-02: Define and Implement Security Controls

**Maturity:** Essential | **Trigger:** Risk assessment identifies controls needed, new security requirement from SLA or regulation, audit finding identifies a control gap

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Identify the control requirement: determine what risk or requirement the control must address, and the target risk reduction level | Information Security Manager | — |
| 2 | Design the control: specify the control type (preventive, detective, or corrective), the dimension it operates in (people, process, technology, or supplier), the implementation approach, and the expected effectiveness | Information Security Manager / Security Architect | — |
| 3 | Validate feasibility: confirm that the control can be implemented within available resources, infrastructure constraints, and supplier capabilities, and that it does not create unacceptable operational impact | Information Security Manager / Service Owner | — |
| 4 | Document the control in the security controls register: record the control description, the risks it mitigates, the responsible owner, testing requirements, and review schedule | Information Security Manager | Security Controls Register |
| 5 | Submit a change request to implement the control through the change management process, including the security justification and any rollback plan | Information Security Manager | Change Request |
| 6 | Implement the control following change management approval: deploy technical controls, update procedures, deliver training, or update supplier contracts as appropriate | Information Security Manager / Responsible Implementer | — |
| 7 | Verify the control is operating as intended: test effectiveness through validation checks appropriate to the control type (e.g., access testing, penetration testing, procedure walkthrough) | Information Security Manager / Security Analyst | Verification Record |
| 8 | Update the risk assessment to reflect the new control and recalculate the residual risk level | Information Security Manager | Updated Risk Assessment |

### Exit Criteria
- Control documented in the security controls register with risk linkage
- Control implemented through the change management process
- Control effectiveness verified through appropriate testing
- Residual risk recalculated and within acceptable threshold

---

## PROC-ISM-03: Manage a Security Incident

**Maturity:** Essential | **Trigger:** A security event is detected or reported that may compromise the confidentiality, integrity, or availability of organizational information

### Prerequisites
- Security incident response plan is established and communicated
- Roles and escalation paths are defined
- Critical assets and services are identified

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| **Phase 1: Detection and Escalation** | | | |
| 1 | Detect the potential security event: through monitoring tools, user reports, supplier notification, or external intelligence | Security Analyst / Service Desk / Monitoring System | — |
| 2 | Perform initial assessment: determine whether the event constitutes a security incident based on defined criteria (unauthorized access, data breach, malware, denial of service, policy violation) | Security Analyst / Information Security Manager | — |
| 3 | Log the security incident: create an incident record capturing the detection time, source, initial description, and affected assets or services | Security Analyst | Security Incident Record |
| 4 | Escalate the confirmed incident: notify the Information Security Manager and, for high-severity incidents, the CISO. Escalate to incident management if the incident affects service availability | Information Security Manager | — |
| **Phase 2: Triage and Analysis** | | | |
| 5 | Assess severity and scope: determine the classification (e.g., low, medium, high, critical) based on the sensitivity of affected data, the number of affected assets/users, and the potential business impact | Information Security Manager / Security Analyst | — |
| 6 | Identify affected assets, services, and data: use the CMDB and asset inventory to map the blast radius of the incident | Security Analyst | — |
| 7 | Preserve evidence: secure logs, system images, and other forensic data that may be needed for investigation, legal proceedings, or regulatory reporting | Security Analyst | Forensic Evidence |
| **Phase 3: Containment and Recovery** | | | |
| 8 | Contain the incident: take immediate action to prevent further damage — isolate affected systems, revoke compromised credentials, block malicious traffic, or disable affected services as appropriate | Information Security Manager / Security Analyst | — |
| 9 | Eradicate the root cause: identify and remove the underlying vulnerability or threat (patch vulnerabilities, remove malware, close unauthorized access paths) | Security Analyst | — |
| 10 | Restore affected services and data: recover from known-good backups, rebuild from definitive media, or restore configurations from the CMDB. Verify integrity of restored assets before returning to production | Information Security Manager / Security Analyst | — |
| 11 | Confirm recovery: validate that services are operating normally, monitoring is in place for recurrence, and affected users and stakeholders are notified of the resolution | Information Security Manager | — |
| **Phase 4: Post-Incident Review** | | | |
| 12 | Conduct a post-incident review: analyse the incident timeline, root cause, effectiveness of the response, and adequacy of existing controls. Include all relevant participants | CISO / Information Security Manager | Post-Incident Review Report |
| 13 | Identify improvement actions: document changes needed to policies, controls, procedures, training, or tooling to prevent recurrence or improve response | Information Security Manager | — |
| 14 | Submit improvement actions to the continual improvement register and track through to completion | Information Security Manager | Improvement Register Entry |
| 15 | Update the security incident record with final classification, resolution details, timeline, and lessons learned | Information Security Manager | Updated Security Incident Record |

### Exit Criteria
- Incident contained and services restored to normal operation
- Evidence preserved for investigation or compliance purposes
- Post-incident review conducted with documented root cause and lessons learned
- Improvement actions logged and tracked in the continual improvement register
- Security incident record completed with full timeline and resolution

---

## PROC-ISM-04: Manage Access Rights

**Maturity:** Essential | **Trigger:** New joiner, role change (mover), leaver, periodic access review cycle, or request for access to a specific system or resource

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Receive the access request: triggered by HR process (joiner/mover/leaver), a service request from a user or manager, or a scheduled access review | Information Security Manager / Service Desk | Access Request |
| 2 | Validate the request: confirm the requestor has authorization, the requested access level is appropriate for the role, and the request complies with the principle of least privilege | Information Security Manager | — |
| 3a | **For joiners:** Provision access rights based on the role profile, applying the minimum access required. Record the granted access in the access rights register | Information Security Manager / System Administrator | Access Rights Register |
| 3b | **For movers:** Review current access rights against the new role profile. Revoke access no longer required and grant access for the new role. Update the register | Information Security Manager / System Administrator | Access Rights Register |
| 3c | **For leavers:** Revoke all access rights immediately upon departure notification. Disable accounts and recover any physical access tokens or devices. Update the register | Information Security Manager / System Administrator | Access Rights Register |
| 3d | **For specific access requests:** Grant the requested access if validated; deny and document the reason if not appropriate | Information Security Manager / System Administrator | Access Rights Register |
| 4 | Conduct periodic access reviews: at defined intervals (at minimum semi-annually for privileged accounts, annually for standard accounts), review all access rights to confirm they remain appropriate | Information Security Manager | Access Review Report |
| 5 | Remediate findings: revoke any access rights found to be excessive, outdated, or no longer justified during the review | Information Security Manager / System Administrator | — |

### Exit Criteria
- Access rights granted, modified, or revoked as appropriate
- Access rights register updated to reflect current state
- Periodic access reviews completed on schedule
- All findings from access reviews remediated

---

## PROC-ISM-05: Conduct Security Audit and Review

**Maturity:** Intermediate | **Trigger:** Scheduled audit cycle (at minimum annually), significant change to business context or threat environment, regulatory requirement, or management request

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Define the audit scope: determine which assets, controls, policies, and processes are covered, and which security standards or frameworks will be used as the assessment baseline | CISO / Information Security Manager | Audit Scope |
| 2 | Identify changes to the business, technology, or threat environment since the last review: consider new services, changed infrastructure, emerging threats, new legislation, and organizational changes | CISO / Information Security Manager | — |
| 3 | Identify missing controls: compare the current security controls register against the applicable standards and the current threat landscape to identify gaps where controls should exist but do not | Information Security Auditor / Security Analyst | — |
| 4 | Assess control effectiveness: for each existing control, evaluate whether it is operating as designed, achieving its intended risk reduction, and remaining appropriate to the current threat environment | Information Security Auditor / Security Analyst | — |
| 5 | Assess compliance: verify that security policies are being followed, access rights are appropriate, training is current, and incident management procedures are being executed as defined | Information Security Auditor | — |
| 6 | Compile the audit report: document all findings categorized by severity, with specific recommendations for remediation and improvement. Include an assessment of the overall security posture | Information Security Auditor / Information Security Manager | Security Audit Report |
| 7 | Present findings to the CISO and relevant stakeholders; agree on remediation priorities, owners, and target dates | CISO / Information Security Manager | — |
| 8 | Submit agreed improvement actions to the continual improvement register and track through to completion | Information Security Manager | Improvement Register Entry |
| 9 | Update the risk assessment if the audit has identified new risks, changed threat levels, or ineffective controls | Information Security Manager | Updated Risk Assessment |

### Exit Criteria
- All areas in scope audited against the defined baseline
- Audit report produced with categorized findings and recommendations
- Remediation actions agreed with owners and target dates
- Findings submitted to the continual improvement register
- Risk assessment updated to reflect audit findings

---

## PROC-ISM-06: Deliver Security Awareness Training

**Maturity:** Intermediate | **Trigger:** New joiner onboarding, annual refresh cycle, significant change to security policies or threat landscape, post-incident requirement

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Define or update the training content: cover topics including authentication and password safety, phishing and social engineering, malware recognition, data classification and handling, remote working security, incident reporting procedures, and relevant security policies | Information Security Manager | Training Content |
| 2 | Identify the target audience and delivery method: all staff receive baseline awareness training; specialized training is delivered to roles with elevated security responsibilities (system administrators, developers, service desk staff, managers) | Information Security Manager | Training Plan |
| 3 | Schedule and deliver training: for new joiners, include in the onboarding programme; for existing staff, deliver at the defined refresh interval (at minimum annually). Use a combination of methods appropriate to the organization (classroom, e-learning, briefings, exercises) | Information Security Manager | — |
| 4 | Track completion: record attendance or completion status for all target participants. Follow up with non-completers and escalate persistent non-compliance to line management | Information Security Manager | Training Completion Record |
| 5 | Assess effectiveness: use quizzes, phishing simulations, or feedback surveys to evaluate whether training has improved security awareness and behaviour | Information Security Manager / Security Analyst | Training Effectiveness Report |
| 6 | Reinforce security awareness on an ongoing basis: use communications, posters, briefings, or other methods to keep security at the forefront of staff awareness between formal training events | Information Security Manager | — |
| 7 | Review and update training content at least annually or following significant changes to security policies, the threat landscape, or post-incident findings | Information Security Manager | — |

### Exit Criteria
- Training delivered to all target participants on schedule
- Completion tracked and non-compliance escalated
- Training effectiveness assessed through at least one validation method
- Training content reviewed and updated at least annually

---

## PROC-ISM-07: Coordinate Supplier Security

**Maturity:** Advanced | **Trigger:** New supplier onboarding, supplier contract renewal, periodic supplier security review, security audit finding related to supplier access

### Steps

| # | Action | Role | Artefact |
|---|--------|------|----------|
| 1 | Define security requirements for the supplier engagement: determine what organizational information, systems, and networks the supplier will access, and derive appropriate security requirements based on the sensitivity and criticality of those assets | Supplier Security Coordinator / Information Security Manager | Supplier Security Requirements |
| 2 | Include security requirements in the supplier contract or underpinning agreement: specify access control requirements, data handling obligations, incident notification requirements, audit rights, and security certification expectations | Supplier Security Coordinator / Supplier Manager | Contract / UA Security Clauses |
| 3 | Implement technical controls for supplier access: configure network isolation to prevent access to more sensitive parts of the network; enforce strong authentication and encryption for supplier sessions; restrict access to only the systems and data required for the engagement | Information Security Manager / Security Architect | — |
| 4 | Verify supplier compliance at onboarding: confirm that the supplier meets the defined security requirements before granting access. Where required, obtain evidence of security certifications (e.g., ISO 27001, SOC 2) | Supplier Security Coordinator | Supplier Compliance Record |
| 5 | Monitor supplier security on an ongoing basis: review supplier security performance at defined intervals, including audit of supplier access logs, review of security incident notifications from the supplier, and assessment of continued certification status | Supplier Security Coordinator / Security Analyst | Supplier Security Review Report |
| 6 | Conduct or commission supplier security assessments: for high-risk suppliers, perform or require vulnerability assessments, security audits, or penetration testing of the supplier's security controls as they relate to the organization's data | Supplier Security Coordinator / Information Security Auditor | Supplier Security Assessment |
| 7 | Address supplier security findings: work with the supplier and supplier management to remediate any identified security gaps. Escalate to the CISO if a supplier presents unacceptable security risk | Supplier Security Coordinator / Information Security Manager | — |
| 8 | Review and update supplier security requirements at contract renewal or following a significant change to the threat environment, the supplier's services, or the organization's risk appetite | Supplier Security Coordinator | Updated Requirements |

### Exit Criteria
- Security requirements documented and included in supplier contracts
- Technical access controls implemented and verified
- Supplier compliance confirmed before access is granted
- Ongoing supplier security monitoring established
- Supplier security findings remediated or escalated
