---
name: 3pa-requirements
description: "P2 Requirements & Decisions — Elicit detailed requirements, make architectural decisions, define RACI approach."
user_invocable: true
---

# 3PA Requirements — P2 Requirements & Decisions

## Methodology Reference

- Primary: `methodology/3PA-Phase-Guide.md` §P2
- Supporting: `methodology/3PA-Overview.md` §9 (Shared Contracts), `methodology/3PA-Quality-Gates.md` (gate awareness)
- Framework Packs: `methodology/3PA-Framework-Pack-Specification.md` §3.2

## Prerequisites

- P1 complete: `docs/itsm/scoping-brief.md` exists and is confirmed
- Tier is assigned
- Processes in scope are identified

## Procedure

### Step 1: Load Context

1. Read `docs/itsm/scoping-brief.md` for tier, scope, and framework
2. If a framework pack is loaded, inject its `requirement_prompts`
3. Determine which requirement categories apply (per `3PA-Phase-Guide.md` §P2.1)

### Step 2: Elicit Requirements

For each process in scope, work through the applicable requirement categories:

1. **Process scope & objectives** (all tiers)
2. **Roles & responsibilities** (all tiers)
3. **Interfaces with other processes** (T2+)
4. **KPIs & metrics** (T1 optional, T2+ required)
5. **Tooling & automation** (T1 optional, T2+ required)
6. **Compliance & audit requirements** (T2 optional, T3 required)
7. **Supplier/vendor management** (T2 optional, T3 required)
8. **Continual improvement approach** (T2 optional, T3 required)

Present requirements in conversational batches. For T1, focus on categories 1–2. For T2+, cover all applicable categories.

### Step 3: Record Decisions

For each architectural or operational decision that emerges:

1. Assign a D-{number} ID
2. Record using the decision format from `3PA-Phase-Guide.md` §P2.2
3. Include the `Applies To` field with affected process IDs
4. Specify `Distribute To` target documents

### Step 4: Map Process Interfaces (T2+)

For each process in scope:
1. Define inputs and triggers
2. Define outputs and destinations
3. Map interfaces to other in-scope processes
4. Verify bidirectional consistency

### Step 5: Define RACI Approach

1. Identify organizational roles from the intake
2. Define role names and descriptions
3. Establish RACI conventions (one A per activity, etc.)
4. Define escalation hierarchy

### Step 6: Begin ITSM Glossary

Populate the glossary section of the decision log:
1. Organization-specific terms
2. Framework-specific terminology
3. Acronym definitions

### Step 7: Scaffold Decision Log

1. Copy `templates/decision-log.md` to `docs/itsm/decision-log.md`
2. Fill frontmatter
3. Populate decisions, glossary, and summary table

### Step 8: User Confirmation

Present the decision log summary. Wait for confirmation.

## Exit Gate

- [ ] Decision log exists at `docs/itsm/decision-log.md`
- [ ] All applicable requirement categories are addressed (per tier)
- [ ] At least one decision per process in scope
- [ ] Process interfaces mapped (T2+)
- [ ] RACI approach defined with role names
- [ ] ITSM glossary has initial entries
- [ ] All decisions have `Applies To` and `Distribute To` fields
- [ ] YAML frontmatter is valid
- [ ] User has confirmed requirements and decisions

## Handoff

Pass to `3pa-author` (P3):
- Decision log location: `docs/itsm/decision-log.md`
- Requirement summary
- Role definitions
- Process interface map (T2+)
- Framework pack name

## When Things Go Wrong

| Problem | Resolution |
|---------|-----------|
| User unsure about a requirement | Record as TBD with a rationale note; flag at exit gate |
| Conflicting requirements between processes | Record as a decision (D-{n}); present options to user |
| Too many processes for a single session | Batch by Phase A→D; complete one phase before starting the next |
| Framework pack requirements conflict with user needs | User needs override framework defaults; record the deviation as a decision |
| Roles are undefined or vague | Use framework pack role model as starting point; refine with user |
