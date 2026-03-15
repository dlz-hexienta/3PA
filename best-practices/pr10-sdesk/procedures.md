---
process_id: PR10
process_name: "Service Desk"
category: procedures
frameworks:
  - itil-v4
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Service Desk §3.2.1, §3.2.2, §3.2.3"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Desk — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier. The three ITIL 4 sub-processes — user query handling, communicating to users, and service desk optimization — are consolidated into five procedures. Many activities have both human interaction and automated (self-service) variants — organizations should implement the variant appropriate to their maturity and automation capabilities.

---

## Essential Procedures (All tiers)

### PROC-SDESK-01: Handle User Queries
<!-- sources: ITIL 4 Service Desk §3.2.1 Tables 3.1, 3.2 -->

**Trigger:** User query received through any established communication channel — phone, email, chat, walk-in, web portal, social media, or other agreed channel.

**Scope:** Covers acknowledgement, recording, validation, and triage of all user queries. Maps to definition activities 1–3.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Acknowledge the user query politely and to the agreed quality standard. In self-service scenarios, the user interacts with the application interface (portal, IVR, chatbot). In human interaction scenarios, the agent welcomes the user and begins dialogue. Record the interaction — uniquely identify it in the query log with time, duration, and content at minimum | Service Desk Agent | User query | Recorded user query |
| 2 | Validate the query — verify the user's identity (authentication), their entitlement to consume the specified service, whether the query falls within the service provider's area of responsibility, and whether additional identity checks are needed for protected information. In automated scenarios, validation is built into the user journey (portal login, entitlement matching against service catalogue) | Service Desk Agent | User query, access rules, service catalogue | Validated query; or rejection with relevant message |
| 3 | Triage the query — categorize it and determine the appropriate value stream and practice. For known query types, apply predefined activity sequences. Resolve elementary queries at first contact where possible. For queries requiring further processing, route to the appropriate practice (incident management, service request management, or other). Capture sufficient classification data for routing | Service Desk Agent | Validated query, triage criteria, knowledge base | Classified query; initiated processing in appropriate value stream |

**Exit criteria:** Query recorded with unique identifier. User identity validated. Query triaged and routed — or resolved at first contact. Sufficient information captured for all queries, including those requiring no further action.

---

### PROC-SDESK-02: Communicate to Users
<!-- sources: ITIL 4 Service Desk §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Requirement for outgoing communication to users — triggered by incident status change, planned change notification, mass announcement, satisfaction survey, or any other practice requiring user communication.

**Scope:** Covers audience identification, channel selection, information packaging, sending, and feedback gathering. Maps to definition activities 4–5 (and partially 6).

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify and confirm the target audience — for individual communications, the audience is defined by the query record. For mass communications, the requesting practice proposes the audience, but the service desk verifies based on understanding of who users are, their communication preferences, and their context | Service Desk Agent | Communication requirement, user records | Confirmed target audience |
| 2 | Identify and confirm the communication channel — select the appropriate channel based on the message type, audience preferences, and SLA requirements. In omnichannel scenarios, users may choose their preferred channel. For mass communications, select the channel that best reaches the target audience | Service Desk Agent | Target audience, channel capabilities, SLA requirements | Selected communication channel |
| 3 | Package the information — format using agreed templates and corporate standards. Ensure the message is clear, uses user-friendly language, and states its purpose. Verify template data sources are current. Avoid overly complex or pseudo-personalized templates. For mass communications, review and compile the message so it uses terms and styles users understand | Service Desk Agent | Message content, templates | Formatted communication |
| 4 | Send the communication through the selected channel. Obtain approval from the service desk manager or equivalent authority where required. For automated notifications, verify templates produce correct output | Service Desk Manager (approval); Service Desk Agent (send) | Formatted communication, approval | Communicated message; communication report |

**Exit criteria:** Target audience identified and verified. Appropriate channel selected. Message formatted to corporate standards. Communication sent and recorded.

---

## Intermediate Procedures (T2+)

### PROC-SDESK-03: Gather and Process User Feedback
<!-- sources: ITIL 4 Service Desk §3.2.2, §2.2.3 -->

**Trigger:** Scheduled feedback collection cycle, mass communication requiring response tracking, validation failure during query handling, or user-initiated feedback through any channel.

**Scope:** Covers feedback collection, receipt confirmation processing, and feedback analysis. Maps to definition activity 6.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Collect user feedback through all available channels — surveys, ratings, direct responses, social media monitoring. Welcome feedback rather than discouraging it. Ensure each mass communication includes a clear reference to the feedback channel | Service Desk Agent | Feedback requests, survey tools, user responses | Raw feedback data |
| 2 | Process receipt confirmations for communications requiring user response — follow up on unanswered requests through alternative channels. Control follow-up thresholds to avoid user irritation | Service Desk Agent | Outstanding response requirements, follow-up thresholds | Processed confirmations; escalation records |
| 3 | Identify and record incoming queries relating to specific mass communications. Route feedback to the initiator of the communication where appropriate. Ensure mass communication feedback is acted upon — failure to process it damages credibility | Service Desk Agent | Incoming feedback, communication records | Categorized feedback; routing to initiators |
| 4 | Analyse feedback data — identify trends, satisfaction levels, channel preferences, and improvement opportunities. Feed analysis into the service desk optimization process and relationship management | Service Desk Manager | Feedback data, trend analysis | Feedback analysis report; improvement inputs |

**Exit criteria:** Feedback collected from all channels. Receipt confirmations processed. Feedback categorized and routed. Analysis completed and fed into improvement.

---

### PROC-SDESK-04: Review and Improve the Service Desk
<!-- sources: ITIL 4 Service Desk §3.2.3 Tables 3.5, 3.6 -->

**Trigger:** Scheduled performance review (periodic), significant performance issue or complaint (event-driven), new technology opportunity, or request from management.

**Scope:** Covers performance review, improvement initiation, and improvement communication. Maps to definition activities 7–8.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Review service desk performance — analyse performance reports, satisfaction survey results, technology opportunities, and incident and service request reports. Engage relevant stakeholders in the review | Service Desk Manager | Performance reports, satisfaction data, technology opportunities, incident/request reports | Performance assessment; identified improvement opportunities |
| 2 | Prioritize improvement opportunities based on impact, feasibility, and alignment with organizational objectives. Assess whether improvements require change requests or can be handled as improvement initiatives | Service Desk Manager | Improvement opportunities | Prioritized improvement list |
| 3 | Register improvement initiatives for processing through the continual improvement practice, or initiate change requests for changes requiring formal approval. Assign ownership and track progress | Service Desk Manager | Prioritized improvements | Registered improvement initiatives; change requests |
| 4 | Communicate successful improvements to relevant stakeholders through the communication process (PROC-SDESK-02). Ensure the service desk team and users are aware of changes to channels, processes, or tools | Service Desk Manager | Completed improvements | Improvement communications |

**Exit criteria:** Performance reviewed against agreed criteria. Improvements identified, prioritized, and initiated. Successful improvements communicated to stakeholders.

---

## Advanced Procedures (T3)

### PROC-SDESK-05: Optimize Channels and Organization
<!-- sources: ITIL 4 Service Desk §2.2.1, §4.2 -->

**Trigger:** Strategic review of service desk organization, channel integration project, significant change in user base or service portfolio, or periodic optimization review.

**Scope:** Covers omnichannel integration and organizational model optimization. Maps to definition activities 9–10.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Assess current channel integration status — identify gaps in information sharing between channels, points where users lose context during channel switches, and opportunities for contextual intelligence (pre-populated data, communication history, user profiles) | Service Desk Manager | Channel usage data, user feedback, technology capabilities | Channel integration assessment |
| 2 | Plan and implement omnichannel improvements — integrate communication channels to provide seamless user journeys. Ensure user context is preserved across channel transitions. Integrate contextual data from service management systems into agent interfaces | Service Desk Manager | Integration assessment, technology options | Omnichannel integration plan; implemented improvements |
| 3 | Evaluate the service desk organizational model — assess the current model (local, distributed, virtual, hybrid) against user needs, cost constraints, and service delivery requirements. Consider concierge, field services, and offshore options as appropriate | Service Desk Manager | Current model assessment, user requirements, cost analysis | Organizational model evaluation |
| 4 | Assess service desk sizing — analyse query arrival rates, acceptable waiting times, dropout rates, queue lengths, additional workload from other practices, service level expectations, and expected staff turnover. Determine optimal team size and structure (vertical vs horizontal, specialization) | Service Desk Manager | Demand data, queueing analysis, staffing data | Sizing assessment; staffing plan |
| 5 | Implement organizational changes and monitor outcomes — track the impact of model and sizing changes on performance, satisfaction, and cost. Adjust based on results | Service Desk Manager | Implementation plan | Updated organizational model; performance tracking |

**Exit criteria:** Channel integration assessed and improved. Organizational model evaluated and optimized. Sizing assessed using demand analysis. Changes implemented and monitored.
