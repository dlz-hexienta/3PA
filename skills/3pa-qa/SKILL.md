---
name: 3pa-qa
description: "P4 Quality Assurance — Run quality gates G1–G8 against the ITSM document corpus, identify defects, and drive resolution."
user_invocable: true
---

# 3PA QA — P4 Quality Assurance

## Methodology Reference

- Primary: `methodology/3PA-Phase-Guide.md` §P4
- Gate definitions: `methodology/3PA-Quality-Gates.md`
- Shared contracts: `methodology/3PA-Overview.md` §9
- Framework Packs: `methodology/3PA-Framework-Pack-Specification.md` §3.4

## Prerequisites

- P3 complete: document corpus in `docs/itsm/` with all tier-required documents authored
- All documents at `draft` status
- Tier and process scope are established

## Procedure

### Step 1: Load Context

1. Read `docs/itsm/scoping-brief.md` for tier, scope, framework
2. Inventory all documents in `docs/itsm/`
3. Determine which gates apply (from `3PA-Quality-Gates.md` summary table)
4. If a framework pack is loaded, prepare its `quality_checks` for injection

### Step 2: Run Gates in Order

> **Revision mode:** Focus gate checks on newly authored and updated documents first. Then validate retained (Keep) documents against G1, G3, and G6 to ensure minimum standards. Run G5 (Cross-Document Consistency) across the full corpus including retained documents.

Execute gates G1 → G8 in sequence. For each gate:

1. Read the gate definition from `3PA-Quality-Gates.md`
2. Run each check against the applicable documents
3. Record pass/fail for each check
4. For failures: log the finding, identify affected documents, propose a fix

#### Gate Execution by Tier

| Gate | T1 | T2 | T3 |
|------|:---:|:---:|:---:|
| G1: Metadata Integrity | Run | Run | Run |
| G2: Decision Coverage | Run | Run | Run |
| G3: Taxonomy Completeness | Run | Run | Run |
| G4: Internal Consistency | Skip | Run | Run |
| G5: Cross-Document Consistency | Skip | Run | Run |
| G6: RACI Completeness | Run | Run | Run |
| G7: Process Interface Integrity | Skip | Run | Run |
| G8: Gap Analysis | Skip | Run | Run |

### Step 3: Resolution Loop

For each finding:
1. Present the finding to the user with the proposed fix
2. Apply the fix (with user confirmation)
3. Re-run the affected gate check
4. If a gate fails 3+ times, escalate to user for an architectural decision

### Step 4: Framework Pack Quality Checks

If a framework pack is loaded, run its `quality_checks` as extensions to the standard gates.

### Step 5: Generate Completeness Report

1. Copy `templates/completeness-report.md` to `docs/itsm/completeness-report.md`
2. Fill the assessment summary
3. Populate gate results table
4. Detail all findings with their resolutions
5. List unresolved items
6. Summarize document statuses

### Step 6: Status Promotion

After all applicable gates pass:
1. Update document status from `draft` to `review` in YAML frontmatter
2. After user sign-off, promote to `approved`

### Step 7: User Confirmation

Present the completeness report summary. Wait for confirmation.

## Exit Gate

- [ ] All applicable gates pass (per tier)
- [ ] Completeness report exists at `docs/itsm/completeness-report.md`
- [ ] All findings are resolved or documented as exceptions
- [ ] All documents are at `review` status or higher
- [ ] Framework pack quality checks pass (if applicable)
- [ ] YAML frontmatter is valid
- [ ] User has reviewed and confirmed the completeness report

## Handoff

Pass to `3pa-publish` (P5):
- Completeness report location: `docs/itsm/completeness-report.md`
- Gate results summary
- Any outstanding exceptions
- Document status summary

## When Things Go Wrong

| Problem | Resolution |
|---------|-----------|
| Gate failure requires significant document rewrite | Return to P3 for the affected layer; re-run P4 from G1 after |
| Large corpus (T3) exceeds context window | Batch checks: G4 per-document, G5 by contract type, G6 per-RACI, G7 per-interface pair |
| Conflicting gate requirements | G6 (RACI) and G7 (Interfaces) take priority as ITSM-specific checks |
| Framework pack check conflicts with organization needs | User overrides framework; note exception in completeness report |
| Gate fails 3+ times | Stop resolution loop; escalate to user; record as D-{n} in decision log |
| TBD items remain from P2/P3 | Flag in completeness report; cannot promote to `approved` until resolved |
