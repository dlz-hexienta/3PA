---
name: 3pa-intake
description: "P1 Scope & Context — Understand the organization's ITSM landscape, determine complexity tier, and define scope boundaries."
user_invocable: true
---

# 3PA Intake — P1 Scope & Context

## Methodology Reference

- Primary: `methodology/3PA-Phase-Guide.md` §P1
- Supporting: `methodology/3PA-Overview.md` §4 (Complexity Tiers), `methodology/3PA-Document-Taxonomy.md` §1 (Document Types)
- Framework Packs: `methodology/3PA-Framework-Pack-Specification.md`

## Prerequisites

- User has a description of the organization and its ITSM needs
- `3PA/` directory structure is in place

## Procedure

### Step 0: Engagement Mode

Ask the first and most important question:

> **Are you building ITSM processes from scratch (greenfield) or improving/formalizing existing processes (revision)?**

Record the answer. This determines the entire downstream flow (see `3PA-Phase-Guide.md` §P1.0).

### Step 1: Framework Pack Detection

1. Read the user's organization description
2. Check `framework-packs/` for packs matching the description keywords
3. If a match is found, load the pack and note it for injection
4. If no match, proceed with framework-agnostic intake

### Step 2: Conduct Intake Interview

Ask the 21 intake questions from `3PA-Phase-Guide.md` §P1.2, organized in 7 sections (A–G), plus any framework pack `intake_questions`.

Present questions in conversational batches (one section at a time). Allow the user to answer naturally and extract structured data from their responses.

- Section A: Engagement Mode (already answered in Step 0)
- Section B: Organization Context (org structure, roles, change appetite)
- Section C: Scope (processes, roles, suppliers, services, compliance, sites, language)
- Section D: Framework (framework selection)
- Section E: Current State (existing docs, pain points, maturity — critical for revision mode)
- Section F: Tools (ITSM tooling, integrations, constraints)
- Section G: Stakeholders & Use

### Step 2.5: Existing Documentation Inventory (Revision Mode)

If engagement mode is **revision**:
1. Collect list of all existing ITSM documentation from the user
2. For each document, record: title, format, last updated, quality assessment
3. Map each to a 3PA taxonomy category where possible

### Step 3: Complexity Scoring

Apply the scoring procedure from `3PA-Phase-Guide.md` §P1.3:

1. Count T2 and T3 signals from the intake responses
2. Assign tier: T1 (Single Process), T2 (Process Group), or T3 (Full SMS)
3. Present the tier assignment with justification to the user

### Step 4: Scaffold Scoping Brief

1. Copy `templates/scoping-brief.md` to `docs/itsm/scoping-brief.md`
2. Fill YAML frontmatter with organization name, scope, framework
3. Populate all sections from intake responses, including:
   - §1.5 Engagement Mode
   - §2.5 Organization Profile (People, Tools, Existing Processes)
4. For T3: complete the Process Decomposition section (Phase A→D)

### Step 4.5: Gap Analysis (Revision Mode)

If engagement mode is **revision**:
1. Copy `templates/gap-analysis-report.md` to `docs/itsm/gap-analysis-report.md`
2. Populate from the existing documentation inventory (Step 2.5)
3. Assess taxonomy coverage (which required docs exist, quality ratings)
4. Assess process maturity (current vs. target per process)
5. Assess organizational readiness (people, tools, processes)
6. Prioritize gaps (Critical / Important / Improvement Opportunity)
7. Recommend the P3 authoring strategy (Keep / Update / Rewrite / Create per document)

See `3PA-Phase-Guide.md` §P1.5 for the full procedure.

### Step 5: User Confirmation

Present the scoping brief summary (and gap analysis report, if revision mode) to the user. Wait for confirmation before proceeding.

## Exit Gate

- [ ] Engagement mode is recorded (greenfield/revision)
- [ ] Scoping brief exists at `docs/itsm/scoping-brief.md`
- [ ] All 21 intake questions are addressed (or marked TBD with justification)
- [ ] Organization profile is complete (people, tools, existing processes)
- [ ] Complexity tier is assigned with signal justification
- [ ] Processes in scope are listed by ID (PR1–PR14)
- [ ] Framework pack is selected or "agnostic" is noted
- [ ] Stakeholders are identified (T2+)
- [ ] Process decomposition is complete (T3)
- [ ] Gap analysis report exists (revision mode only)
- [ ] YAML frontmatter is valid and complete
- [ ] User has confirmed the scoping brief (and gap analysis, if revision)

## Handoff

Pass to `3pa-requirements` (P2):
- Scoping brief location: `docs/itsm/scoping-brief.md`
- Engagement mode: greenfield/revision
- Assigned tier: T1/T2/T3
- Framework pack name (if loaded)
- Processes in scope
- Gap analysis report location (revision mode): `docs/itsm/gap-analysis-report.md`

## When Things Go Wrong

| Problem | Resolution |
|---------|-----------|
| User cannot answer a question | Record as TBD, flag at exit gate, continue with other questions |
| Tier is ambiguous (borderline signals) | Default to the higher tier; it can be downgraded later if the corpus proves simpler |
| No framework pack matches | Proceed with framework-agnostic intake; framework can be selected later in P2 |
| User wants to scope more processes than initially indicated | Re-run complexity scoring; tier may change |
| Existing documentation is extensive | Catalog it in §5 of the scoping brief; assess what can be reused vs. what needs rewriting |
| Existing docs are in non-standard formats | Convert to Markdown or catalog content manually; note format in gap analysis |
| Organization has undocumented processes | Interview process practitioners; capture informal processes in gap analysis |
| User unsure whether greenfield or revision | If any existing docs exist, default to revision mode — it handles both new and existing |
