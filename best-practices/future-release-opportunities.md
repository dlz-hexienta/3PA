---
title: "Best Practices Library — Future Release Opportunities"
version: "1.0"
last_updated: 2026-03-14
status: active
---

# Best Practices Library — Future Release Opportunities

Identified gaps and enrichment opportunities from the initial knowledge crawl (v0.2, 2026-03-14). Items are prioritized by engagement likelihood and client impact.

---

## 1. IT4IT Per-Process Enrichment

**Priority:** High (if IT4IT-primary engagements are expected)

**Gap:** IT4IT content across all 24 processes is limited to value-stream alignment labels (S2P, R2D, R2F, D2C). No per-process depth — activities, artefacts, and KPIs are not sourced from IT4IT.

**Affected:** All 24 process files (definition, procedures, kpis)

**Action:** Extract per-process content from the IT4IT Reference Architecture v3.0, mapping functional components to each PR01–PR24 process area. Enrich definitions with IT4IT data objects, procedures with IT4IT automation patterns, and KPIs with IT4IT metrics.

**Source:** `it4it.pdf` (deeper extraction required — initial crawl used high-level mapping only)

---

## 2. SIAM Multi-Supplier Integration Patterns

**Priority:** High (if SIAM engagements are expected)

**Gap:** SIAM content is limited to brief multi-supplier integration notes in a subset of processes. Not deep enough to support a SIAM-primary engagement.

**Affected:** PR11 IM, PR13 PM, PR15 CHM, PR17 SCFGM, PR22 RELM, PR23 SUPPM, and cross-cutting/interface-patterns.md

**Action:** Extract SIAM-specific content from SIAM PDFs — service integration layer patterns, cross-supplier escalation models, end-to-end process orchestration across providers, SIAM tooling integration requirements, and SIAM-specific RACI patterns (service integrator vs. retained organization vs. service providers).

**Source:** `SIAM-*.pdf` files in the knowledge library

---

## 3. ISO 20000 Requirements Cross-Reference for FitSM-Gap Processes

**Priority:** Medium

**Gap:** Eight processes have no FitSM process-specific requirements to cross-reference against. They rely solely on ITIL v4 practice success factors for their "mandatory requirements" sections. Adding ISO 20000-1 clause references would provide a standards-based requirements baseline.

**Affected processes:**
- PR03 Service Financial Management
- PR04 Service Design
- PR10 Service Desk
- PR14 Monitoring & Event Management
- PR18 IT Asset Management
- PR19 Knowledge Management
- PR20 Measurement & Reporting
- PR21 Risk Management

**Action:** Map ISO 20000-1:2018 clauses to these 8 processes and enrich their policy and definition files with standards-aligned mandatory requirements. Also useful for T3 engagements pursuing ISO 20000 certification.

**Source:** ISO 20000-1:2018 (not currently in knowledge library — would need to be added). The FitSM guide `FitSM_Guide_Achieving_compliance_with_ISO_IEC_20000-1.pdf` provides a mapping that could serve as an interim source.

---

## 4. FitSM-6 Maturity Criteria for Non-FitSM Processes

**Priority:** Medium

**Gap:** The maturity model (`cross-cutting/maturity-model.md`) has FitSM-6 requirement-level maturity criteria for only 8 process areas (PR01, PR02, PR09, PR11, PR13, PR15, PR17, PR24 — mapped from FitSM PR1–PR14). The remaining 16 processes use a generic 0–4 pattern.

**Affected:** cross-cutting/maturity-model.md — Per-Process Maturity Criteria section

**Action:** Develop process-specific maturity criteria (levels 0–4) for the 16 processes not covered by FitSM-6, using the ITIL 4 capability criteria tables and the Capability Maturity Model pattern. This would enable meaningful per-process maturity assessment for the full 24-process model.

**Affected processes:** PR03, PR04, PR05, PR06, PR07, PR08, PR10, PR12, PR14, PR16, PR18, PR19, PR20, PR21, PR22, PR23

---

## 5. Cross-Cutting Interface Completeness Verification

**Priority:** Low–Medium

**Gap:** Interface patterns (`cross-cutting/interface-patterns.md`) are synthesized from the 24 individual process crawls rather than extracted from a single authoritative interface reference. Some interface pairs may be incomplete or asymmetric (source process claims an output that the target process does not list as an input).

**Action:** Systematic verification pass — for every interface listed, confirm both the source and target process definition files acknowledge the interface. Add any missing interfaces discovered. This could be partially automated by parsing the interface sections of all 24 definition files.

---

## 6. COBIT Integration Layer

**Priority:** Low (unless COBIT governance engagements arise)

**Gap:** COBIT is not represented in the knowledge library or framework packs. For organizations with COBIT-based IT governance, the best practices lack alignment to COBIT management objectives and governance components.

**Action:** Add COBIT 2019 mapping to the framework packs and enrich governance-oriented processes (PR01 SPM, PR03 SFM, PR09 ISM, PR20 MR, PR21 RM, PR24 CI) with COBIT management objective references.

**Source:** COBIT 2019 Framework (would need to be added to knowledge library)

---

## 7. Industry-Specific Compliance Overlays

**Priority:** Low (build on demand per engagement)

**Gap:** Best practices are industry-agnostic. Organizations in regulated industries (healthcare, finance, government) need compliance-specific requirements woven into process definitions and policies.

**Potential overlays:**
- **Healthcare:** HIPAA, HITECH — affects PR09 ISM, PR21 RM, PR17 SCFGM
- **Finance:** SOX, PCI-DSS — affects PR09 ISM, PR15 CHM, PR21 RM, PR20 MR
- **Government:** FedRAMP, NIST 800-53 — affects PR09 ISM, PR21 RM, PR06 AM, PR07 SCM
- **General EU:** GDPR, NIS2 — affects PR09 ISM, PR21 RM, PR11 IM (breach notification)

**Action:** Create compliance overlay files (e.g., `cross-cutting/compliance-gdpr.md`) that the `3pa-author` skill can inject when a compliance driver is identified during P1 intake.

---

## Summary

| # | Opportunity | Priority | Processes Affected | Source Available |
|---|------------|:--------:|:------------------:|:---------------:|
| 1 | IT4IT per-process enrichment | High | All 24 | Yes (deeper read) |
| 2 | SIAM multi-supplier patterns | High | 7 + cross-cutting | Yes (deeper read) |
| 3 | ISO 20000 cross-reference | Medium | 8 FitSM-gap processes | Partial (FitSM guide) |
| 4 | FitSM-6 maturity for all processes | Medium | 16 non-FitSM processes | No (requires authoring) |
| 5 | Interface completeness verification | Low–Medium | cross-cutting | Automated feasible |
| 6 | COBIT integration | Low | 6 governance processes | No (new source needed) |
| 7 | Industry compliance overlays | Low | Varies | No (new sources needed) |
