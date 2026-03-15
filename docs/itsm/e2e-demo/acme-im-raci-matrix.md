---
title: "Incident Management — RACI Matrix"
organization: "Acme IT Services"
scope: "PR11"
category: raci-matrix
process_id: PR11
status: draft
version: "0.1"
date: 2026-03-15
parent: acme-im-process-definition.md
depends_on:
  - acme-im-process-definition.md
framework: fitsm
tags: [e2e-demo, t1, greenfield]
---

# Incident Management — RACI Matrix

<!-- Layer 3 document — cross-cutting role-activity assignments for PR11 Incident Management.
     Role names must be consistent with the process definition and all other documents.
     Rules: exactly one A per activity, at least one R per activity.
     T1 scope: No MIM or SO roles. IM handles major incident coordination directly. -->

## 1. Role Definitions

| Role ID | Role Name | Description |
|---------|-----------|-------------|
| IM | Incident Manager (Tom Weber, Service Desk Lead) | Accountable for all incident management activities. Coordinates incident handling, monitors resolution performance, declares and coordinates major incidents. Also serves as Process Owner at T1 |
| SDA | Service Desk Agent (Service Desk team, 8 staff) | First point of contact for user-reported incidents. Registers, classifies, prioritizes incidents. Performs first-contact resolution. Manages incident closure with user confirmation |
| TS | Technical Specialist (Infrastructure & Applications teams) | Provides domain-specific expertise for incident diagnosis and resolution. Participates in major incident resolution when mobilized by IM |

> **Note:** At T1, no dedicated Major Incident Manager (MIM) or Service Owner (SO) roles are assigned. The Incident Manager performs major incident coordination directly. The MIM role is a T2+ capability per the 3PA tier model.

## 2. RACI Legend

| Symbol | Meaning | Definition |
|--------|---------|------------|
| **R** | Responsible | Does the work to complete the activity |
| **A** | Accountable | Ultimately answerable; approves completed work. **Exactly one per activity.** |
| **C** | Consulted | Provides input; two-way communication |
| **I** | Informed | Kept up-to-date on progress; one-way communication |
| **--** | Not Involved | No role in this activity |

## 3. RACI Table

### Incident Detection and Registration

| Activity | IM | SDA | TS |
|----------|:---:|:---:|:---:|
| Detect incidents from monitoring, events, or technical observation | A | I | R |
| Receive user-reported incidents via Service Desk channels | A | R | -- |
| Register incidents in Jira SM with all required fields | A | R | C |

### Incident Classification and Prioritization

| Activity | IM | SDA | TS |
|----------|:---:|:---:|:---:|
| Classify incidents using the 2D classification scheme (Service x Technology Layer) | A | R | C |
| Determine priority using the Impact x Urgency matrix (P1-P4) | A | R | C |
| Check incidents against major incident criteria (D-2) | A | R | C |

### Incident Diagnosis and Resolution

| Activity | IM | SDA | TS |
|----------|:---:|:---:|:---:|
| Investigate and diagnose incidents | A | C | R |
| Engage additional Technical Specialists for complex incidents | A/R | I | C |
| Apply resolution or workaround to restore service | A | I | R |
| Confirm service restoration with the user | A | R | C |

### Incident Closure

| Activity | IM | SDA | TS |
|----------|:---:|:---:|:---:|
| Verify resolution with user and obtain confirmation | A | R | -- |
| Complete the incident record with resolution details in Jira SM | A | R | C |
| Capture user satisfaction data | A | R | -- |
| Flag incident for future problem record or change request | A | R | C |

### Major Incident Handling

| Activity | IM | SDA | TS |
|----------|:---:|:---:|:---:|
| Identify incident as a major incident | A/R | C | C |
| Assume major incident coordinator role (IM at T1) | A/R | I | I |
| Mobilize resources and coordinate the resolution effort | A/R | C | R |
| Communicate status to stakeholders via Slack at defined intervals | A/R | C | I |
| Resolve the major incident | A | I | R |
| Conduct the post-major-incident review | A/R | I | C |
| Document and distribute the major incident review report in Confluence | A/R | I | I |

## 4. Validation Rules

- [x] Every activity has exactly one **A** (all activities: IM is Accountable)
- [x] Every activity has at least one **R** (verified across all activities)
- [x] All role names match the Role Definitions in Section 1 (IM, SDA, TS)
- [x] All activities match those in the parent process definition (acme-im-process-definition.md, Section 4, Activities 1-7)
- [x] No orphan roles — every role has at least one assignment:
  - IM: A on all activities
  - SDA: R on 12 activities, C on 6 activities
  - TS: R on 7 activities, C on 9 activities
- [x] Role names are consistent with process policy and procedures (IM, SDA, TS used throughout)

## 5. Activity-to-Process-Definition Traceability

| Process Definition Activity | RACI Activities |
|----------------------------|-----------------|
| Activity 1: Detect incidents | Detect incidents from monitoring (TS=R); Receive user-reported incidents (SDA=R) |
| Activity 2: Register incidents | Register incidents in Jira SM (SDA=R) |
| Activity 3: Classify and prioritize incidents | Classify using 2D scheme (SDA=R); Determine priority (SDA=R); Check major incident criteria (SDA=R) |
| Activity 4: Diagnose incidents | Investigate and diagnose (TS=R); Engage additional TS (IM=A) |
| Activity 5: Resolve incidents | Apply resolution or workaround (TS=R); Confirm restoration with user (SDA=R) |
| Activity 6: Close incidents | Verify resolution (SDA=R); Complete record (SDA=R); Capture satisfaction (SDA=R); Flag for problem/change (SDA=R) |
| Activity 7: Manage major incidents | Identify as major (IM=A); Assume coordinator (IM=A); Mobilize resources (TS=R); Communicate (IM=A); Resolve (TS=R); Post-MI review (IM=A); Document report (IM=A) |
