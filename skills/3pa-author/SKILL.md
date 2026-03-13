---
name: 3pa-author
description: "P3 Document Authoring — Author all ITSM documents in dependency layer order, enforcing the document hierarchy."
user_invocable: true
---

# 3PA Author — P3 Document Authoring

## Methodology Reference

- Primary: `methodology/3PA-Phase-Guide.md` §P3
- Document types: `methodology/3PA-Document-Taxonomy.md`
- Quality awareness: `methodology/3PA-Quality-Gates.md`
- Templates: `templates/`
- Best Practices: `best-practices/_index.md`
- Framework Packs: `methodology/3PA-Framework-Pack-Specification.md` §3.3

## Prerequisites

- P1 complete: `docs/itsm/scoping-brief.md` exists and is confirmed
- P2 complete: `docs/itsm/decision-log.md` exists and is confirmed
- Tier, processes in scope, role definitions, and RACI approach are established

## Procedure

### Step 1: Load Context

1. Read `docs/itsm/scoping-brief.md` for tier, scope, framework, processes
2. Read `docs/itsm/decision-log.md` for decisions, roles, glossary
3. If a framework pack is loaded, prepare `document_section_templates` for injection
4. Determine the full document list required by the tier (from `3PA-Document-Taxonomy.md` §1)

### Step 1.5: Load Best Practices

1. For each process in scope, check `best-practices/pr{NN}-{abbrev}/` for available content
2. Load best practice files that match the process IDs (definition, policy, procedures, raci, kpis)
3. Filter by maturity level based on tier:
   - T1 engagements: load `essential` content only
   - T2 engagements: load `essential` + `intermediate` content
   - T3 engagements: load all maturity levels
4. If a framework pack is loaded, apply `best_practices_ref.mapping` adaptation notes
5. In revision mode: also load existing documents marked "Update" or "Rewrite" from the gap analysis

> **Revision mode:** For documents marked Keep in the gap analysis, verify and retain as-is. For Update, load existing and revise using best practices as quality targets. For Rewrite, start from best practices. For Create, start from template + best practices.

### Step 2: Present Authoring Plan

Show the user:
1. Complete list of documents to author
2. Layer order (0→5) with documents assigned to each layer
3. Process interdependency phases (A→D) for Layer 2 (T2+)
4. Estimated document count

Wait for user confirmation before authoring begins.

### Step 3: Author Layer 0 — SMS Policy (T2+)

1. Copy `templates/sms-policy.md` to `docs/itsm/{org}-sms-policy.md`
2. Fill frontmatter
3. Inject best practice content from `best-practices/cross-cutting/policy-patterns.md` as starting material
4. Author all sections, incorporating decisions from the decision log
5. Reference the framework's general requirements (if framework pack loaded)
6. Present to user for confirmation before proceeding to Layer 1

### Step 4: Author Layer 1 — Process Policies

For each process in scope:
1. Copy `templates/process-policy.md` to `docs/itsm/{org}-{process-id}-process-policy.md`
2. Fill frontmatter with process_id and parent (SMS Policy)
3. Author policy statements aligned with SMS Policy
4. Define process-specific objectives

Present Layer 1 for user confirmation before proceeding.

### Step 5: Author Layer 2 — Process Definitions

Author in Phase A→B→C→D interdependency order (T2+):

For each process in scope (in dependency order):
1. Copy `templates/process-definition.md` to `docs/itsm/{org}-{process-id}-process-definition.md`
2. Fill frontmatter with process_id, parent (process policy), depends_on (phase dependencies)
3. Author all 12 sections
4. Include Mermaid process flow diagram
5. Define interfaces to other processes
6. Track shared contracts

Present each phase (A, B, C, D) for user confirmation before proceeding.

### Step 6: Author Layer 3 — RACI Matrices & KPI Definitions

1. For each process (or consolidated): copy `templates/raci-matrix.md`, fill role definitions, populate RACI table
2. Enforce: one A per activity, at least one R, roles match definitions
3. Copy `templates/kpi-definition.md`, define KPIs aligned with process objectives
4. Verify KPI targets match process definition targets

Present Layer 3 for user confirmation.

### Step 7: Author Layer 4 — Procedures

For each process in scope:
1. Copy `templates/procedure.md` to `docs/itsm/{org}-{process-id}-{procedure-name}-procedure.md`
2. Fill frontmatter with parent (process definition)
3. Author step-by-step instructions
4. Ensure all roles reference RACI matrix role names exactly
5. Include decision points and exception handling

Present Layer 4 for user confirmation.

### Step 8: Author Layer 5 — Templates & Records

Based on tier requirements, author:
- SLA templates (T2+)
- OLA templates (T3)
- Service catalogue entries (T2+)
- Risk register (T2 optional, T3 required)
- CSI register (T2 optional, T3 required)

Present Layer 5 for user confirmation.

### Step 9: Shared Contract Verification

Before exiting P3, verify all shared contracts from `3PA-Overview.md` §9:
- Role names consistent across all documents
- Process interfaces bidirectional
- Service definitions consistent
- Decision distributions complete

## Exit Gate

- [ ] All documents required by the tier are authored
- [ ] Layer order respected (no Layer N+1 before Layer N)
- [ ] Process interdependency order respected (T2+)
- [ ] All YAML frontmatter is complete and valid
- [ ] All Mermaid diagrams use valid syntax
- [ ] RACI matrices enforce one-A-per-activity rule
- [ ] Shared contracts are tracked and consistent
- [ ] User has confirmed each layer
- [ ] All documents are at `draft` status

## Handoff

Pass to `3pa-qa` (P4):
- Document corpus location: `docs/itsm/`
- Assigned tier
- List of authored documents with categories and layers
- Known shared contract issues (if any)

## When Things Go Wrong

| Problem | Resolution |
|---------|-----------|
| User wants to skip a layer | Warn about dependency impact; allow skip only if dependent layers are not needed |
| Process definition is too complex for one session | Break into sub-sessions by activity group; maintain state across sessions |
| RACI conflicts between processes | Escalate as a decision (D-{n}); resolve role ambiguity before proceeding |
| Mermaid diagram too complex to render | Simplify by splitting into sub-diagrams; use swimlane layout for complex flows |
| Framework pack section templates conflict with user needs | User overrides framework defaults; note the deviation |
| Document count exceeds context window | Author in batches by layer; maintain a running summary of shared contracts |
