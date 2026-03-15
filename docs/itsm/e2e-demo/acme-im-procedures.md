---
title: "Incident Management — Procedures"
organization: "Acme IT Services"
scope: "PR11"
category: procedure
process_id: PR11
status: draft
version: "0.1"
date: 2026-03-15
parent: acme-im-process-definition.md
depends_on:
  - acme-im-process-definition.md
  - acme-im-raci-matrix.md
framework: fitsm
tags: [e2e-demo, t1, greenfield]
---

# Incident Management — Procedures

<!-- Layer 4 document — step-by-step HOW-TO instructions for PR11 Incident Management.
     Essential procedures only (PROC-IM-01 and PROC-IM-02) for T1 scope.
     Role names must match RACI matrix exactly: IM, SDA, TS.
     No MIM role at T1 — IM performs major incident coordination directly. -->

---

## PROC-IM-01: Handle and Resolve Incidents

### 1. Purpose

This procedure provides step-by-step instructions for detecting, registering, classifying, prioritizing, diagnosing, resolving, and closing incidents affecting services managed by Acme IT Services. It covers the standard incident lifecycle from initial detection through confirmed resolution and closure.

### 2. Scope

This procedure covers all incidents — unplanned interruptions to a service or reductions in the quality of a service — that do not meet major incident criteria. Incidents meeting major incident criteria (see Decision Point 1 in Section 6) are transferred to PROC-IM-02 (Handle Major Incidents).

This procedure does not cover service requests, which are tagged separately in Jira Service Management per decision D-7.

### 3. Roles

| Role | Responsibility in this Procedure |
|------|--------------------------------|
| Incident Manager (IM) | Accountable for all activities. Monitors escalation timers. Arbitrates priority conflicts. Engages additional Technical Specialists when needed |
| Service Desk Agent (SDA) | Performs incident registration, classification, prioritization. Attempts first-contact resolution. Manages closure and user confirmation |
| Technical Specialist (TS) | Detects incidents from monitoring (Datadog). Provides expert diagnosis and resolution for escalated incidents. Documents resolution actions |

### 4. Prerequisites

- [x] Jira Service Management is operational and accessible to all SDA and TS roles
- [x] Datadog monitoring is active and alerting to the Service Desk and TS teams
- [x] Slack channels are configured for incident communication (#incidents, #major-incidents)
- [x] Classification scheme (Service x Technology Layer) is configured in Jira SM
- [x] Priority matrix (P1-P4) with SLA targets is configured in Jira SM
- [x] Escalation rules and timescales are configured in Jira SM automation

### 5. Steps

#### Step 1: Detect the Incident

**Performed by:** SDA (for user-reported incidents) / TS (for monitoring-detected incidents)

1. **User-reported incidents:** SDA receives the incident report through a Service Desk channel (phone, email, Jira SM portal, or Slack). Record the user's description of the issue, the affected service, and the time the user first noticed the problem
2. **Monitoring-detected incidents:** TS receives a Datadog alert indicating service degradation, threshold breach, or component failure. Verify the alert is a genuine incident (not a false positive or planned maintenance window)
3. **Technical observation:** TS identifies an issue during routine operations or maintenance that constitutes an unplanned service interruption or degradation
4. Note the detection timestamp — this starts the SLA response clock in Jira SM

#### Step 2: Register the Incident

**Performed by:** SDA

1. Create a new incident ticket in Jira Service Management
2. Complete all required fields:
   - **Incident title:** Brief description of the fault (format: [Service] - [Observed Fault])
   - **Affected user(s):** Name and contact details of the reporting user(s)
   - **Affected service:** Select from the service catalogue (~12 services)
   - **Affected CI:** Identify the configuration item if known (asset ID, application name, server name)
   - **Impact:** Assess current impact on user/customer workflow (High / Medium / Low)
   - **Urgency:** Assess the speed at which business requires resolution (High / Medium / Low)
   - **Time of first symptom:** When the user first noticed the issue or when the monitoring alert was generated
   - **Detection source:** User report / Datadog alert / Technical observation
3. If the incident was detected by Datadog, attach the alert details (alert ID, triggered metric, threshold values) to the Jira SM ticket
4. Confirm the incident has been acknowledged to the reporting user (email or Slack acknowledgment)

#### Step 3: Classify the Incident

**Performed by:** SDA

1. Assign the **Service** dimension: select the affected service from the service catalogue
2. Assign the **Technology Layer** dimension:
   - **Infrastructure:** Network, server, storage, data center components
   - **Application:** Software, middleware, database, integration components
   - **End User:** Workstation, endpoint, user account, access components
3. Review available knowledge articles in Confluence for matching issues
4. If a matching resolution is found in the knowledge base, note it for use in Step 5 (first-contact resolution attempt)

#### Step 4: Prioritize the Incident

**Performed by:** SDA, with IM oversight

1. Confirm the **Impact** assessment:
   - **High:** Multiple users/teams affected; business-critical service unavailable; external client impact
   - **Medium:** Single team or limited users affected; non-critical service degraded; workaround available
   - **Low:** Single user affected; non-critical service; minimal business impact
2. Confirm the **Urgency** assessment:
   - **High:** Immediate business need; no workaround; SLA breach imminent
   - **Medium:** Business need within business hours; workaround available but limited
   - **Low:** No immediate business pressure; acceptable workaround in place
3. Apply the priority matrix to determine priority (P1-P4):

   | | Urgency: High | Urgency: Medium | Urgency: Low |
   |---|:---:|:---:|:---:|
   | Impact: High | **P1** | **P2** | **P3** |
   | Impact: Medium | **P2** | **P3** | **P4** |
   | Impact: Low | **P3** | **P4** | **P4** |

4. **Check major incident criteria** (see Decision Point 1 in Section 6). If criteria are met, transfer to PROC-IM-02 immediately
5. Jira SM starts the SLA clock based on the assigned priority and service hours (P1: 24/7; P2-P4: Mon-Fri 08:00-18:00 CET)

#### Step 5: Diagnose and Resolve the Incident

**Performed by:** SDA (first-contact attempt) / TS (escalated incidents)

1. **First-contact resolution attempt (SDA):**
   - Check Confluence knowledge articles for known resolution steps
   - Apply the documented resolution if a matching article exists
   - If the incident is resolved at first contact, proceed to Step 6
   - If the incident cannot be resolved at first contact, proceed to functional escalation (sub-step 2)

2. **Functional escalation to L2 (TS):**
   - Escalate the Jira SM ticket to the appropriate Technical Specialist team (Infrastructure or Applications) based on the Technology Layer classification
   - Escalation timescales per D-3: P1 = 15 min, P2 = 1 hr, P3 = 4 hr, P4 = 1 business day
   - TS investigates using diagnostic tools, Datadog dashboards, configuration data, and technical expertise
   - If TS identifies a resolution or workaround, apply it and confirm service restoration

3. **Further escalation to L3 (Team Lead):**
   - If TS cannot resolve the incident and it requires architectural decision, vendor engagement, or cross-team coordination, escalate to the relevant Team Lead
   - IM monitors escalation progress and arbitrates if resource conflicts arise

4. **Hierarchical escalation:**
   - If SLA breach is imminent, escalate hierarchically to IM (Tom Weber)
   - For P1 incidents: hierarchical escalation to IT Director within 30 minutes if not yet resolved
   - IM may reallocate resources, adjust priorities, or authorize emergency measures

5. Document all diagnostic steps taken, resolution actions applied, and the resolution outcome in the Jira SM ticket

#### Step 6: Close the Incident

**Performed by:** SDA

1. Contact the affected user to confirm that the service has been restored and they can resume normal work
2. If the user confirms resolution:
   - Update the Jira SM ticket status to "Resolved"
   - Complete the incident record with:
     - Resolution details (what was done)
     - Resolution timestamp
     - Final service and technology layer classification (update if initial classification was incorrect)
     - Resolver name and group
3. Trigger the post-resolution satisfaction survey in Jira SM
4. Determine whether follow-up actions are needed:
   - **Flag for future problem investigation (PR13):** If the root cause is unknown or the incident is recurring, add a "problem-candidate" label in Jira SM
   - **Flag for future change request (PR15):** If a permanent fix requires an infrastructure or application change, add a "change-candidate" label in Jira SM
5. If the user does not confirm resolution or reports the issue persists:
   - Reopen the incident and return to Step 5
   - Notify the IM if the incident has been reopened

#### Step 7: Record and Report

**Performed by:** SDA (record) / IM (report)

1. SDA ensures the completed incident record in Jira SM contains all required fields and timestamps
2. IM includes the incident in the monthly incident report (volumes, classification breakdown, resolution times, SLA achievement)
3. For incidents flagged as problem or change candidates, IM reviews the flags during the monthly report preparation

### 6. Decision Points

| Decision Point | Criteria | If Yes | If No |
|---------------|----------|--------|-------|
| DP-1: Is this a major incident? | P1 Critical priority OR 2+ services affected OR external client service unavailable OR declared by IT Director/SDL (D-2) | Transfer immediately to PROC-IM-02 (Handle Major Incidents) | Continue with standard handling (Step 5) |
| DP-2: Can SDA resolve at first contact? | Matching knowledge article exists AND SDA has access/skills to apply the resolution | SDA applies resolution; proceed to Step 6 | Escalate to TS per escalation timescales (D-3) |
| DP-3: Can TS resolve the incident? | TS identifies root cause or workaround within their technical domain | TS applies resolution; proceed to Step 6 | Escalate to L3 (Team Lead) or hierarchically to IM |
| DP-4: Does the user confirm resolution? | User confirms service is restored and they can resume normal work | Close incident (Step 6) | Reopen and return to Step 5 |
| DP-5: Is follow-up needed? | Root cause unknown, incident is recurring, or permanent fix requires a change | Flag for future PR13 (problem) or PR15 (change) | No further action; close incident |

### 7. Forms & Templates

| Form | Purpose | Location |
|------|---------|----------|
| Jira SM Incident Form | Standard incident registration with all required fields | Jira Service Management > Service Desk Project > Create Issue > Incident |
| Post-Resolution Satisfaction Survey | Captures user satisfaction after incident closure | Jira SM automation (triggered on incident resolution) |
| Monthly Incident Report Template | Template for monthly incident KPI reporting | Confluence > IT Service Management > Incident Management > Reports |

### 8. Expected Outcomes

- [x] Incident is registered in Jira SM with all required fields within the SLA response target
- [x] Incident is classified (Service x Technology Layer) and prioritized (P1-P4) accurately
- [x] Incident is resolved within the SLA resolution target for its priority level
- [x] User confirms service restoration and is satisfied with the resolution
- [x] Incident record is complete with resolution details, timestamps, and final classification
- [x] Follow-up actions (problem/change candidates) are flagged where appropriate

### 9. Exceptions

| Exception | Action | Escalate To |
|-----------|--------|------------|
| Incident meets major incident criteria during handling | Transfer to PROC-IM-02 immediately | IM declares major incident |
| SLA breach is imminent | Hierarchical escalation; IM reallocates resources | IM (Tom Weber), then IT Director |
| User unreachable for resolution confirmation | Attempt contact 3 times over 2 business days. If no response, IM may authorize closure with documented note | IM (Tom Weber) |
| Jira SM system unavailable | Register incident in a spreadsheet (backup template on Confluence). Enter into Jira SM once restored | IM (Tom Weber) |
| Incident reclassified to service request | Change Jira SM ticket type to "Service Request" and apply SR handling per D-7 | SDA handles; IM informed |

---

## PROC-IM-02: Handle Major Incidents

### 1. Purpose

This procedure provides step-by-step instructions for handling major incidents — incidents with significant business impact that require an immediate, coordinated resolution effort. At T1, the Incident Manager (Tom Weber) acts as the major incident coordinator. There is no dedicated Major Incident Manager role at this tier.

### 2. Scope

This procedure is triggered when an incident meets any of the major incident criteria defined in decision D-2:

1. Priority is P1 (Critical)
2. Two or more services are simultaneously affected
3. An external client-facing service is completely unavailable
4. The IT Director or Service Desk Lead (Tom Weber) explicitly declares a major incident

This procedure covers the major incident lifecycle from declaration through resolution, post-incident review, and report distribution.

### 3. Roles

| Role | Responsibility in this Procedure |
|------|--------------------------------|
| Incident Manager (IM) | Acts as Major Incident Coordinator at T1. Declares major incidents, mobilizes resources, coordinates resolution across teams, manages stakeholder communication, conducts post-incident review, documents review report |
| Service Desk Agent (SDA) | Supports communication (user updates, phone bridge). Provides incident registration data. Assists with user confirmation of restoration |
| Technical Specialist (TS) | Provides technical expertise for diagnosis and resolution. Works under IM coordination. Multiple TS from different domains may be mobilized simultaneously |

### 4. Prerequisites

- [x] Major incident criteria (D-2) are documented and understood by all SDA and IM roles
- [x] Slack channel #major-incidents is configured and accessible to all roles
- [x] Stakeholder contact list is maintained in Confluence (IT Director, service owners, client contacts)
- [x] Jira SM major incident workflow is configured with elevated priority handling
- [x] Confluence space for major incident review reports is established
- [x] Escalation to IT Director is possible within 30 minutes (phone/Slack)

### 5. Steps

#### Step 1: Identify and Declare the Major Incident

**Performed by:** IM

1. Confirm the incident meets at least one major incident criterion:
   - P1 (Critical) priority
   - 2+ services simultaneously affected
   - External client-facing service completely unavailable
   - IT Director or Service Desk Lead declaration
2. Reclassify the incident as a major incident in Jira Service Management (set Major Incident flag = Yes; Priority = P1 if not already)
3. Record the major incident declaration timestamp in Jira SM — this starts the major incident timeline
4. Post initial notification in Slack #major-incidents channel:
   - Incident ID and title
   - Affected service(s)
   - Current impact assessment
   - "Major incident declared — IM coordinating"

#### Step 2: Assume Major Incident Coordinator Role

**Performed by:** IM

1. IM (Tom Weber) assumes the major incident coordinator role for the duration of this major incident
2. Notify the IT Director of the major incident within 30 minutes (Slack direct message or phone)
3. Set up a dedicated Slack thread or huddle in #major-incidents for real-time coordination
4. All further coordination, decisions, and status updates will flow through the IM as single point of contact

#### Step 3: Mobilize Resources and Coordinate Resolution

**Performed by:** IM (coordination) / TS (resolution work)

1. IM identifies and mobilizes the Technical Specialists required for resolution based on the affected services and technology layers:
   - Infrastructure TS for infrastructure-layer issues
   - Application TS for application-layer issues
   - Both teams if the incident spans multiple layers
2. IM assigns the highest operational priority to this incident — all mobilized TS resources focus on resolution
3. IM coordinates the resolution effort:
   - Ensure TS teams are communicating via the dedicated Slack thread
   - Remove blockers (access, information, tooling)
   - Track diagnostic progress and resolution attempts
4. If an emergency change is required to resolve the incident, IM authorizes it directly (at T1, formal emergency change process via PR15 is future-scope; document the change in the Jira SM ticket for future tracking)
5. If external vendor support is needed, IM contacts the vendor and coordinates their involvement

#### Step 4: Communicate Status to Stakeholders

**Performed by:** IM

1. Post status updates in Slack #major-incidents at the following intervals:
   - **P1 major incident:** Every 30 minutes until resolved
   - **Multi-service / client-facing:** Every 30 minutes until resolved
2. Each status update shall include:
   - Current status (investigating / identified / implementing fix / monitoring)
   - Affected service(s) and impact summary
   - Actions in progress
   - Estimated time to resolution (if known)
   - Workaround available (if any)
3. SDA communicates directly with affected users who have open incident tickets, providing status updates aligned with IM's stakeholder communications
4. For external client-facing outages: IM coordinates client communication with IT Director

#### Step 5: Resolve the Major Incident

**Performed by:** TS (resolution) / IM (coordination and confirmation)

1. TS applies the identified fix, workaround, or remediation to restore service
2. TS confirms that the affected service(s) are restored and functioning normally
3. IM verifies restoration:
   - Check Datadog dashboards for service health indicators
   - Confirm with SDA that user reports have stopped
   - Obtain confirmation from affected users (for critical client-facing services)
4. IM posts resolution notification in Slack #major-incidents:
   - "Major incident [ID] resolved at [timestamp]"
   - Brief description of resolution applied
   - Any ongoing monitoring or follow-up needed
5. Document all resolution actions, decisions, and timeline in the Jira SM ticket

#### Step 6: Conduct Post-Major-Incident Review

**Performed by:** IM (leads review) / TS (contributes)

1. Schedule the post-major-incident review within 5 business days of resolution
2. Invite participants: IM, involved TS, SDA team lead, IT Director (for significant incidents)
3. Review the following:
   - **Timeline:** Chronological sequence of events from first detection to resolution
   - **Response effectiveness:** Was the major incident identified promptly? Were resources mobilized effectively? Was communication adequate?
   - **Resolution quality:** Was the root cause identified? Is the fix permanent or a workaround? Are further actions needed?
   - **What went well:** Identify positive aspects of the response
   - **What could be improved:** Identify areas for improvement in detection, response, communication, or tooling
4. Agree on follow-up actions:
   - Flag for future problem investigation (PR13) if root cause is unknown
   - Flag for future change request (PR15) if a permanent fix requires a change
   - Process improvement actions (to be tracked when PR24 Continual Improvement is established)
5. Record all findings and action items

#### Step 7: Document and Distribute the Review Report

**Performed by:** IM

1. Create the major incident review report in Confluence with the following structure:
   - **Incident Summary:** ID, title, affected services, duration, impact
   - **Timeline:** Chronological sequence of key events and actions
   - **Root Cause:** Identified root cause (or "Under investigation" if unknown)
   - **Resolution:** Description of the fix or workaround applied
   - **Impact Assessment:** Number of affected users, services, duration of outage, client impact
   - **Lessons Learned:** What went well, what could be improved
   - **Follow-Up Actions:** Action items with owners and target dates
2. Distribute the report to:
   - IT Director
   - Affected service owners / client account managers
   - All TS teams involved in the resolution
   - SDA team (for awareness and learning)
3. Store the report in Confluence > IT Service Management > Incident Management > Major Incident Reviews
4. Update the Jira SM major incident ticket with a link to the Confluence report
5. Close the major incident in Jira SM

### 6. Decision Points

| Decision Point | Criteria | If Yes | If No |
|---------------|----------|--------|-------|
| DP-1: Does the incident meet major incident criteria? | Any criterion from D-2 is met (P1, 2+ services, client unavailable, declared) | Proceed with this procedure (PROC-IM-02) | Handle as standard incident via PROC-IM-01 |
| DP-2: Is an emergency change required? | Resolution requires a change to infrastructure, application, or configuration that would normally follow change management | IM authorizes change directly at T1; document in Jira SM for future tracking | Proceed with resolution using existing capabilities |
| DP-3: Is external vendor support needed? | Internal TS teams cannot resolve; vendor expertise or access is required | IM contacts vendor, coordinates involvement, tracks vendor response | Continue with internal resolution |
| DP-4: Is the root cause identified? | Root cause is confirmed through diagnosis | Document root cause in review report; assess if permanent fix is needed | Flag for future problem investigation (PR13); document as "Under investigation" |
| DP-5: Is a permanent fix needed? | The resolution applied was a workaround; a permanent fix requires a change | Flag for future change request (PR15) with priority recommendation | No further change action needed; monitor for recurrence |

### 7. Forms & Templates

| Form | Purpose | Location |
|------|---------|----------|
| Jira SM Major Incident Form | Major incident registration and tracking with elevated priority | Jira Service Management > Service Desk Project > Major Incident flag |
| Major Incident Review Report Template | Structured template for post-major-incident review documentation | Confluence > IT Service Management > Incident Management > Templates |
| Stakeholder Contact List | Contact details for IT Director, service owners, client contacts | Confluence > IT Service Management > Incident Management > Contacts |
| Major Incident Slack Template | Standard format for Slack status updates during major incidents | Confluence > IT Service Management > Incident Management > Templates |

### 8. Expected Outcomes

- [x] Major incident is declared and classified within 15 minutes of detection
- [x] IM assumes coordinator role and IT Director is notified within 30 minutes
- [x] Resources are mobilized and resolution effort is coordinated across teams
- [x] Stakeholders receive status updates every 30 minutes during the major incident
- [x] Service is restored and user confirmation is obtained
- [x] Post-major-incident review is conducted within 5 business days
- [x] Review report is documented in Confluence and distributed to all stakeholders
- [x] Follow-up actions are identified, assigned, and tracked

### 9. Exceptions

| Exception | Action | Escalate To |
|-----------|--------|------------|
| IM (Tom Weber) is unavailable when major incident occurs | Most senior available SDA assumes coordinator role temporarily; contact IM and IT Director immediately | IT Director designates interim coordinator |
| Major incident occurs outside business hours (P1 incidents have 24/7 SLA) | IM is contacted via on-call phone; TS on-call is mobilized per on-call roster | IM (on-call), then IT Director |
| Multiple simultaneous major incidents | IM coordinates both if manageable; if not, IT Director designates a second coordinator from senior TS | IT Director |
| Vendor SLA breach during major incident resolution | IM documents vendor response time; escalates through vendor escalation path | IM manages vendor escalation; IT Director if vendor unresponsive |
| Post-MI review identifies systemic process failure | IM documents as high-priority improvement action; presents to IT Director within 2 business days | IT Director for resource and priority decision |

## 10. Related Documents

| Document | Relationship |
|----------|-------------|
| acme-im-process-definition.md | Parent process definition — defines activities, roles, and process flow |
| acme-im-raci-matrix.md | RACI matrix — role-activity assignments must match procedure role assignments (IM, SDA, TS) |
| acme-im-kpi-definitions.md | KPI definitions — measurement points in these procedures (detection timestamp, resolution timestamp) feed KPI calculations |
| acme-im-process-policy.md | Process policy — governing principles and mandatory requirements that these procedures implement |
