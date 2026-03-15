---
process_id: cross-cutting
process_name: "Cross-Cutting"
category: priority
frameworks:
  - itil-v4
  - fitsm
maturity:
  essential: true
  intermediate: true
  advanced: false
sources:
  - "ITIL 4 Practice Guide: Incident Management §2.2, §2.4, §3.2"
  - "ITIL 4 Practice Guide: Change Enablement §2.2, §3.2"
  - "FitSM-2 §PR9 ISRM (classification and prioritization)"
  - "FitSM-1 PR9.1 (consistent registration, classification, prioritization)"
last_updated: 2026-03-14
status: draft
---

# Priority Matrix Templates

## How to Use These Templates

Priority models define how work items are classified and sequenced for attention and resources. This document provides the standard impact/urgency matrix for incidents and service requests, SLA-linked prioritization for service target alignment, a change priority model, and priority definition templates. During P3 authoring, the `3pa-author` skill injects these models into incident management, service request management, and change management process definitions and procedures. Organizations should customize the number of priority levels, the impact/urgency definitions, and the SLA target values. Priority models are synthesized from ITIL 4 incident management (which defines impact, urgency, and priority), FitSM-1 PR9.1 (which requires consistent prioritization), and FitSM-2 §PR9 (which specifies classification and prioritization activities).

---

## Impact/Urgency Priority Matrix
<!-- essential -->
<!-- sources: ITIL 4 IM §2.4 Table 2.3; FitSM-1 PR9.1 -->

Priority is derived from the combination of **impact** (the effect on the business) and **urgency** (the speed at which resolution is required). This matrix produces a priority value that determines SLA targets, resource allocation, and escalation timing.

### Impact Definitions

| Level | Name | Definition |
|:-----:|------|------------|
| 4 | Critical | Entire organization or critical business service affected. Complete loss of a vital business function. Multiple sites or all users of a service impacted. Regulatory or contractual breach imminent |
| 3 | High | Major business function degraded or unavailable. Large number of users affected (e.g., entire department or site). Significant financial or reputational risk. No workaround available |
| 2 | Medium | Non-critical business function affected. Limited number of users impacted. Workaround available but inconvenient. Moderate disruption to productivity |
| 1 | Low | Individual user or small group affected. Minimal business impact. Workaround readily available. Cosmetic or minor functionality issue |

### Urgency Definitions

| Level | Name | Definition |
|:-----:|------|------------|
| 4 | Critical | Business operation will cease within minutes if not resolved. Time-critical regulatory or contractual deadline at risk. No alternative process available |
| 3 | High | Business operation significantly impaired and degrading. Resolution needed within hours. Alternative process available but unsustainable |
| 2 | Medium | Business operation can continue with workaround. Resolution needed within the current or next business day. Disruption is noticeable but manageable |
| 1 | Low | No immediate time pressure. Resolution can be scheduled. Issue does not affect current business operations |

### Priority Matrix

|  | **Critical Urgency (4)** | **High Urgency (3)** | **Medium Urgency (2)** | **Low Urgency (1)** |
|---|:---:|:---:|:---:|:---:|
| **Critical Impact (4)** | P1 | P1 | P2 | P3 |
| **High Impact (3)** | P1 | P2 | P2 | P3 |
| **Medium Impact (2)** | P2 | P2 | P3 | P4 |
| **Low Impact (1)** | P3 | P3 | P4 | P4 |

### Priority Levels

| Priority | Name | Description | Typical Response | Typical Resolution |
|:--------:|------|-------------|:----------------:|:------------------:|
| P1 | Critical | Major business impact requiring immediate attention. May trigger major incident process | 15 min | 4 hours |
| P2 | High | Significant impact on business operations. Elevated resource allocation | 30 min | 8 hours |
| P3 | Medium | Moderate impact with workaround available. Normal resource allocation | 2 hours | 24 hours |
| P4 | Low | Minor impact, no urgency. Scheduled resolution | 8 hours | 72 hours |

**Note:** Response and resolution targets are indicative. Organizations must define their own targets during P2 (Requirements & Decisions) and formalize them in SLAs.

---

## SLA-Linked Prioritization
<!-- intermediate -->
<!-- sources: ITIL 4 IM §2.4; ITIL 4 SLM §2.4 -->

SLA-linked prioritization extends the basic priority matrix by connecting priority levels to specific SLA clauses, enabling automated SLA timer management and escalation.

### Priority-to-SLA Mapping

| Priority | Response Target | Update Frequency | Resolution Target | Escalation at | Service Hours |
|:--------:|:--------------:|:----------------:|:-----------------:|:------------:|:-------------:|
| P1 | {15 min} | {Every 30 min} | {4 hours} | {50% elapsed} | {24×7} |
| P2 | {30 min} | {Every 2 hours} | {8 hours} | {50% elapsed} | {24×7 or extended} |
| P3 | {2 hours} | {Every 8 hours} | {24 hours} | {75% elapsed} | {Business hours} |
| P4 | {8 hours} | {At resolution} | {72 hours} | {75% elapsed} | {Business hours} |

### Priority Adjustment Rules

Priority may be adjusted after initial assignment under the following circumstances:

| Condition | Adjustment | Authority |
|-----------|-----------|-----------|
| Additional users or services found to be affected | Increase priority (higher impact) | Incident Manager |
| Workaround found that restores business function | Decrease urgency (lower priority) | Incident Manager |
| VIP user or critical business period affected | Increase priority per policy | Service Desk Supervisor |
| Customer contractual obligations at risk | Increase priority (higher urgency) | Service Level Manager |
| Original assessment was incorrect after investigation | Correct priority to match actual impact/urgency | Incident Manager |

**Principle:** Priority adjustments shall be documented with justification. Decreasing priority requires the same authority level as the current priority assignment.

---

## Change Priority Model
<!-- intermediate -->
<!-- sources: ITIL 4 Change Enablement §2.2, §3.2 -->

Changes use a distinct priority model that considers business benefit, risk, and scheduling constraints rather than impact/urgency.

### Change Types and Default Priority

| Change Type | Description | Default Priority | Approval Authority | Lead Time |
|-------------|-------------|:----------------:|-------------------|:---------:|
| Standard | Pre-approved, low-risk, well-understood. Follows a defined procedure | P4 (Scheduled) | Pre-approved (no individual approval needed) | Per procedure |
| Normal – Minor | Low risk, limited scope, single team | P3 (Normal) | Change Manager or delegated authority | {e.g., 5 business days} |
| Normal – Significant | Moderate risk, multiple teams or services affected | P2 (Elevated) | CAB or Change Authority | {e.g., 10 business days} |
| Normal – Major | High risk, major business impact, complex implementation | P1 (Urgent) | CAB + Senior Management | {e.g., 15+ business days} |
| Emergency | Must be implemented immediately to restore service or prevent imminent failure | P1 (Emergency) | Emergency CAB (eCAB) or delegated authority | Immediate |

### Change Risk Assessment Matrix

Risk assessment determines the approval authority and lead time required for each change:

| | **Low Impact** | **Medium Impact** | **High Impact** |
|---|:---:|:---:|:---:|
| **Low Likelihood of Failure** | Low Risk (Minor) | Medium Risk (Significant) | High Risk (Major) |
| **Medium Likelihood of Failure** | Medium Risk (Significant) | High Risk (Major) | Very High Risk (Major) |
| **High Likelihood of Failure** | High Risk (Major) | Very High Risk (Major) | Very High Risk (Major) |

### Change Scheduling Priority

When multiple approved changes compete for the same maintenance window:

| Priority | Criterion |
|:--------:|-----------|
| 1 (Highest) | Emergency changes — restoring service or preventing imminent failure |
| 2 | Changes linked to regulatory or contractual deadlines |
| 3 | Changes addressing P1/P2 known errors or security vulnerabilities |
| 4 | Changes supporting approved business projects with committed dates |
| 5 | Changes for optimization, improvement, or technical debt reduction |
| 6 (Lowest) | Discretionary changes with no external deadline |

---

## Priority Definition Templates
<!-- essential -->

### Incident/Service Request Priority Template

Use this template to define organization-specific priority levels:

| Priority | Name | Response Target | Resolution Target | Description | Escalation Rules |
|:--------:|------|:--------------:|:----------------:|-------------|-----------------|
| P1 | {Critical} | {15 min} | {4 hours} | {Describe business impact threshold} | {Automatic hierarchical escalation to H2 at declaration, H3 at 50% elapsed} |
| P2 | {High} | {30 min} | {8 hours} | {Describe business impact threshold} | {Automatic hierarchical escalation to H1 at 50% elapsed, H2 at 75% elapsed} |
| P3 | {Medium} | {2 hours} | {24 hours} | {Describe business impact threshold} | {Functional escalation at 50% elapsed} |
| P4 | {Low} | {8 hours} | {72 hours} | {Describe business impact threshold} | {Notification to team lead at 75% elapsed} |

### Problem Priority Template

Problems use a simplified priority model based on the frequency and severity of related incidents:

| Priority | Name | Investigation Target | Description |
|:--------:|------|:-------------------:|-------------|
| P1 | Critical | {1 business day} | Causing recurring P1 incidents, no workaround, affecting critical service |
| P2 | High | {5 business days} | Causing recurring P2 incidents or multiple P3 incidents, workaround available but fragile |
| P3 | Medium | {20 business days} | Causing occasional incidents, stable workaround in place |
| P4 | Low | {Scheduled} | Rare occurrence, effective workaround, minimal business impact |

---

## Notes

1. **Shared contract:** The priority matrix is a shared contract (verified by gate G5) — the same impact, urgency, and priority definitions must be used consistently in incident management, service request management, SLAs, escalation models, and reporting.
2. **FitSM alignment:** FitSM-1 PR9.1 requires that "all incidents and service requests shall be registered, classified and prioritized in a consistent manner." These models satisfy this requirement by providing a structured, repeatable prioritization framework.
3. **VIP handling:** Organizations may define VIP policies that automatically elevate urgency for specific users or roles. VIP policies should be documented in the SMS policy and communicated to the service desk.
4. **Service-specific priorities:** Some organizations define service-specific priority matrices where the same impact/urgency combination yields different priorities depending on the affected service. This is valid but increases complexity — consider carefully before implementing.
5. **Priority vs. severity:** Some frameworks distinguish priority (sequence of resolution) from severity (inherent seriousness). In 3PA, priority is the primary classification used for SLA management and escalation. Severity may be captured as an additional attribute where needed for reporting.
