---
title: "Decision Log"
organization: "Acme IT Services"
scope: "PR11"
category: decision-log
process_id: ~
status: draft
version: "0.1"
date: 2026-03-15
parent: ~
depends_on: []
framework: fitsm
tags: [e2e-demo, t1, greenfield]
---

# Decision Log

## 1. Purpose

This document records all architectural and operational decisions made during the Acme IT Services incident management documentation engagement. Each decision is traceable to the documents it affects and the processes it applies to.

## 2. Decision Format

```
### D-{number}: {Title}

**Context:** {Why this decision is needed}
**Options Considered:**
1. {Option A} — {pros/cons}
2. {Option B} — {pros/cons}

**Decision:** {Chosen option with reasoning}
**Applies To:** {Process IDs affected}
**Distribute To:** {Target documents that must reflect this decision}
**Version Gate:** v1.0 | future | out-of-scope
```

## 3. Decisions

### D-1: Priority Matrix Model

**Context:** Acme has no formal priority matrix. Incidents are currently prioritized ad-hoc by whoever picks up the ticket. A consistent prioritization model is needed for the incident management process definition.

**Options Considered:**
1. 3-level priority (High/Medium/Low) — simple but lacks granularity for SLA differentiation
2. 4-level priority based on Impact × Urgency matrix — balanced granularity, standard FitSM approach
3. 5-level priority (Critical/High/Medium/Low/Planning) — more granular but may be overkill for T1

**Decision:** Option 2 — 4-level priority matrix (P1 Critical, P2 High, P3 Medium, P4 Low) derived from a 3×3 Impact × Urgency grid. This aligns with FitSM's prioritization approach and provides enough granularity for meaningful SLA targets without overcomplicating the model for a T1 engagement.

| | High Urgency | Medium Urgency | Low Urgency |
|---|:---:|:---:|:---:|
| **High Impact** | P1 Critical | P2 High | P3 Medium |
| **Medium Impact** | P2 High | P3 Medium | P4 Low |
| **Low Impact** | P3 Medium | P4 Low | P4 Low |

**Applies To:** PR11
**Distribute To:** Process definition (§8 KPIs, §4 Activities), procedures (prioritization step), KPI definitions (SLA targets per priority)
**Version Gate:** v1.0

---

### D-2: Major Incident Criteria

**Context:** Acme has no defined criteria for what constitutes a major incident. Major incidents are currently declared informally by the IT Director when she notices something is seriously wrong. Formal criteria are needed per FitSM-1 requirement.

**Options Considered:**
1. Impact-only trigger: any P1 Critical incident is automatically a major incident
2. Multi-criteria trigger: P1 Critical OR multiple services affected OR VIP client affected OR financial impact above threshold
3. Management-only trigger: only the IT Director can declare a major incident

**Decision:** Option 2 — Multi-criteria trigger. An incident is classified as a major incident when ANY of the following criteria are met:
- Priority is P1 Critical
- 2 or more services are simultaneously affected by the same root cause
- An external client's service is completely unavailable
- The IT Director or Service Desk Lead declares a major incident based on business impact assessment

At T1, the Incident Manager (Service Desk Lead) serves as the major incident coordinator.

**Applies To:** PR11
**Distribute To:** Process definition (§11 Exceptions & Escalations), procedures (PROC-IM-02), process policy (§3 Policy Statements)
**Version Gate:** v1.0

---

### D-3: Escalation Model

**Context:** Acme currently has no documented escalation paths. The informal "who to call" list in Confluence is incomplete and outdated. FitSM requires defined escalation procedures.

**Options Considered:**
1. Two-tier functional escalation: Service Desk → Team Leads (no further escalation)
2. Three-tier functional + hierarchical escalation: Service Desk → Technical Specialists → Team Leads (functional) + IT Director (hierarchical)
3. Swarming model: no tiers, collaborative resolution from the start

**Decision:** Option 2 — Three-tier model with both functional and hierarchical paths. This provides enough structure for a T1 engagement without the complexity of swarming (which is a T3 approach).

**Functional escalation:**
- L1: Service Desk Agent (first-contact resolution)
- L2: Technical Specialist (domain-specific diagnosis)
- L3: Team Lead (complex issues requiring architectural decisions)

**Hierarchical escalation:**
- Service Desk Lead → IT Director (for resource conflicts, SLA breach risk, or major incidents)

**Escalation timescales:**
- P1: Escalate to L2 within 15 min, hierarchical within 30 min
- P2: Escalate to L2 within 1 hour
- P3: Escalate to L2 within 4 hours
- P4: Escalate to L2 within 1 business day

**Applies To:** PR11
**Distribute To:** Process definition (§11 Exceptions & Escalations, §7 Process Interfaces), procedures (escalation steps), RACI matrix (escalation activities)
**Version Gate:** v1.0

---

### D-4: Role Assignments

**Context:** FitSM's role model defines four generic role types per process: Process Owner, Process Manager, Case Owner, Process Staff Member. For a T1 engagement, these need to be mapped to real people at Acme.

**Options Considered:**
1. Separate Incident Manager and Process Owner — full separation of strategic and operational accountability
2. Combined Incident Manager / Process Owner — Service Desk Lead fills both roles at T1
3. IT Director as Process Owner, Service Desk Lead as Process Manager — governance separation

**Decision:** Option 2 — Combined roles at T1. The Service Desk Lead (Tom Weber) is both the Incident Manager (operational coordination) and the Process Owner (strategic accountability). This is appropriate for T1 where the process is small enough for one person to own. Three operational roles are defined:

| Role | FitSM Role Type | Assigned To | Responsibility |
|------|----------------|-------------|----------------|
| Incident Manager | Process Owner + Process Manager | Tom Weber (Service Desk Lead) | Owns the process; coordinates incident handling; manages escalation; conducts major incident reviews |
| Service Desk Agent | Case Owner | Service Desk team (8 staff) | First-contact handling: registration, classification, prioritization, first-contact resolution, closure |
| Technical Specialist | Process Staff Member | Infrastructure & Applications teams | Domain-specific diagnosis and resolution; participates in major incident resolution |

**Applies To:** PR11
**Distribute To:** Process policy (§5 Roles & Authorities), process definition (§6 Roles & Responsibilities), RACI matrix (all activities), procedures (role assignments per step)
**Version Gate:** v1.0

---

### D-5: Classification Scheme

**Context:** Acme has no formal incident classification scheme. Jira SM uses a flat category field that is inconsistently populated. A defined scheme is needed for routing, reporting, and trend analysis.

**Options Considered:**
1. Service-based classification: classify by affected service only
2. Two-dimensional classification: Service × Technology layer (Infrastructure/Application/End User)
3. Three-dimensional classification: Service × Technology × Incident Type (Availability/Performance/Functionality)

**Decision:** Option 2 — Two-dimensional classification (Service × Technology). This provides enough structure for routing and reporting without the overhead of a third dimension. With ~12 services and 3 technology layers, the classification matrix is manageable.

**Services:** Email, File Storage, ERP, CRM, Network, VPN, Printing, Collaboration Platform, Client Devices, Hosting (external client A), Hosting (external client B), Hosting (external client C)

**Technology layers:** Infrastructure, Application, End User

**Applies To:** PR11
**Distribute To:** Process definition (§4 Activities — classification step), procedures (PROC-IM-01 Step 3)
**Version Gate:** v1.0

---

### D-6: SLA Resolution Targets by Priority

**Context:** Acme has no formal SLA targets for incident resolution. Response and resolution times need to be defined per priority level to support the KPI framework and align with FitSM requirements.

**Decision:** Initial resolution targets based on industry benchmarks for a mid-sized organization:

| Priority | Response Target | Resolution Target | Business Hours |
|----------|:--------------:|:-----------------:|:--------------:|
| P1 Critical | 15 minutes | 4 hours | 24/7 |
| P2 High | 30 minutes | 8 hours | Business hours |
| P3 Medium | 2 hours | 24 hours | Business hours |
| P4 Low | 4 hours | 5 business days | Business hours |

Business hours: Monday-Friday, 08:00-18:00 CET

**Applies To:** PR11
**Distribute To:** KPI definitions (SLA targets), process definition (§8 KPIs), procedures (escalation timescales)
**Version Gate:** v1.0

---

### D-7: FitSM Split Process Handling (ISRM → IM + SRM)

**Context:** FitSM combines Incident Management and Service Request Management into a single process (PR9 ISRM). 3PA splits this into PR11 (IM) and PR12 (SRM). Since only PR11 is in scope, the split handling needs to be documented.

**Options Considered:**
1. Document PR11 as fully standalone — no reference to PR12
2. Document PR11 with explicit interface to PR12 — acknowledge the split and define the boundary

**Decision:** Option 2 — Document the boundary explicitly. The process definition will note that service requests (pre-defined, standard changes that do not represent service degradation) are out of scope and should be routed to Service Request Management when that process is formalized. For now, service requests received at the service desk will be tagged as "Service Request" in Jira SM and handled informally.

**Applies To:** PR11
**Distribute To:** Process definition (§2 Scope — Out of Scope), process policy (§2 Scope)
**Version Gate:** v1.0

## 4. ITSM Glossary

| Term | Definition | Framework Origin | Used In |
|------|-----------|-----------------|---------|
| Incident | An unplanned interruption to a service or a reduction in the quality of a service | FitSM-0, ITIL v4 | All PR11 documents |
| Major Incident | An incident with significant business impact requiring an immediate coordinated resolution effort (see D-2 for criteria) | FitSM-2 PR9 | Process definition, procedures |
| Priority Matrix | A matrix mapping combinations of impact and urgency to priority levels (see D-1) | FitSM-2 PR9 | Process definition, KPIs |
| Incident Model | A repeatable, pre-defined approach to managing a particular type of incident | FitSM-2 PR9 | Process definition (future — T2+) |
| KEDB | Known Error Database — a database of known errors with documented root causes and workarounds | FitSM-2 PR10 | Process definition (interface to PR13) |
| SLA | Service Level Agreement — an agreement between the service provider and customer defining service targets | FitSM-0 | KPI definitions, process definition |
| ISRM | Incident and Service Request Management — FitSM's combined process (PR9) that 3PA splits into PR11 (IM) and PR12 (SRM) | FitSM-0 | Process definition (scope), decision log (D-7) |
| RFC | Request for Change — a formal request to make a change to the IT infrastructure or services | FitSM-0 | Process definition (output to PR15) |
| CI | Configuration Item — any component that needs to be managed to deliver a service | FitSM-0 | Process definition (inputs from PR17) |
| Workaround | A solution that reduces or eliminates the impact of an incident for which a full resolution is not yet available | FitSM-0 | Procedures, process definition |
| SMS | Service Management System — the entirety of policies, processes, procedures, roles, agreements, plans, and resources needed to manage service delivery | FitSM-0 | Process policy |

## 5. Decision Summary

| ID | Title | Applies To | Version Gate | Status |
|----|-------|-----------|-------------|--------|
| D-1 | Priority Matrix Model | PR11 | v1.0 | Confirmed |
| D-2 | Major Incident Criteria | PR11 | v1.0 | Confirmed |
| D-3 | Escalation Model | PR11 | v1.0 | Confirmed |
| D-4 | Role Assignments | PR11 | v1.0 | Confirmed |
| D-5 | Classification Scheme | PR11 | v1.0 | Confirmed |
| D-6 | SLA Resolution Targets by Priority | PR11 | v1.0 | Confirmed |
| D-7 | FitSM Split Process Handling (ISRM → IM + SRM) | PR11 | v1.0 | Confirmed |
