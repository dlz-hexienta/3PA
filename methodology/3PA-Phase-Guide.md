# 3PA Phase Guide

> Authoritative reference for each phase's procedures, inputs, outputs, and exit criteria.

## Phase Overview

```
P1 Scope & Context → P2 Requirements & Decisions → P3 Document Authoring → P4 Quality Assurance → P5 Assembly & Publication
skill: 3pa-intake       3pa-requirements            3pa-author              3pa-qa                 3pa-publish
```

Each phase produces artifacts in `docs/itsm/`, verifies exit gates, obtains user confirmation, then hands off to the next phase.

---

## P1: Scope & Context

**Skill:** `3pa-intake`
**Purpose:** Understand the organization's ITSM landscape, determine complexity tier, and define scope boundaries.
**Output:** Scoping Brief (`docs/itsm/scoping-brief.md`)

### P1.0 Engagement Mode

The first question in every 3PA engagement:

> **Are you building ITSM processes from scratch (greenfield) or improving/formalizing existing processes (revision)?**

This determines the downstream flow:

| Aspect | Greenfield | Revision |
|--------|-----------|----------|
| Starting point | Templates + best practices | Existing documentation |
| P1.5 Gap Analysis | Skipped | Required |
| P2 focus | Build from zero | Delta from current state |
| P3 focus | Author everything | Fill gaps, update existing |
| P4 focus | Full QA | Focused QA on changes |
| P5 focus | Full assembly | Merge new with existing |

Record the mode in the scoping brief §1.5.

### P1.1 Framework Pack Loading

1. Match organization description to framework pack keywords
2. If a matching pack exists in `framework-packs/`, load it
3. Inject the pack's `intake_questions` into the standard question set
4. If no pack matches, proceed with framework-agnostic questions

### P1.2 Intake Questions (21 Questions in 7 Sections)

#### Section A: Engagement Mode (1 question)

| # | Question | Signal |
|---|----------|--------|
| A1 | Are you building ITSM processes from scratch (greenfield) or improving/formalizing existing processes (revision)? | Engagement mode fork |

#### Section B: Organization Context (4 questions)

| # | Question | Signal |
|---|----------|--------|
| B1 | What is your organization and what services do you deliver? | Context |
| B2 | What is your IT organizational structure? (teams, departments, reporting lines, sites) | Org complexity → tier |
| B3 | What existing ITSM roles are defined? (job titles, process roles, governance roles) | Role maturity, gap size |
| B4 | What is the organization's appetite for change and level of formality? | Adoption risk, doc depth |

#### Section C: Scope (7 questions)

| # | Question | Signal |
|---|----------|--------|
| C1 | Which ITSM processes are in scope? | Process count → tier |
| C2 | How many organizational roles interact with these processes? | Role count → tier |
| C3 | How many suppliers/vendors are involved in service delivery? | Supplier count → tier |
| C4 | How many services are in your service catalogue (or planned)? | Service count → tier |
| C5 | What compliance or certification drivers exist (ISO 20000, SOC2, etc.)? | Compliance → tier |
| C6 | How many sites or business units are in scope? | Sites → tier |
| C7 | Is multi-language documentation required? | Language → tier |

#### Section D: Framework (1 question)

| # | Question | Signal |
|---|----------|--------|
| D1 | What ITSM framework(s) does the organization follow or aspire to? | Framework pack selection |

#### Section E: Current State (3 questions)

| # | Question | Signal |
|---|----------|--------|
| E1 | What existing ITSM documentation exists? (policies, process docs, procedures, runbooks) | Gap assessment, revision scope |
| E2 | For existing processes, what is working well and what are the pain points? | Revision priorities |
| E3 | What is the current maturity level of existing processes? (ad hoc / repeatable / defined / managed / optimized) | Maturity baseline |

#### Section F: Tools (3 questions)

| # | Question | Signal |
|---|----------|--------|
| F1 | What ITSM tools are currently in use? (ticketing, monitoring, CMDB, collaboration) | Tool-aware procedures |
| F2 | What automation or integrations exist between tools? | Process design constraints |
| F3 | Are there tool constraints or planned tool changes? | Roadmap alignment |

#### Section G: Stakeholders & Use (2 questions)

| # | Question | Signal |
|---|----------|--------|
| G1 | Who are the key stakeholders for this documentation? | Stakeholder map (T2+) |
| G2 | What is the intended use of the documentation? (internal ops, audit, certification, onboarding) | Scope refinement |

**Mode-dependent behavior:**
- Greenfield: E2 and E3 are optional (may have nothing to report); F1–F3 inform tool sections in process definitions
- Revision: E1–E3 are critical (drive gap analysis); F1–F3 are required (existing tooling constrains process design)

### P1.3 Complexity Scoring

Apply the complexity signal table from `3PA-Overview.md` §4. Count the number of T2 and T3 signals:

- **0–1 T2 signals, 0 T3 signals → T1** (Single Process)
- **2+ T2 signals, 0–1 T3 signals → T2** (Process Group)
- **2+ T3 signals → T3** (Full SMS)

### P1.4 Scope Boundaries

Define what is in-scope and out-of-scope:
- Process IDs in scope (from PR01–PR24 or custom)
- Organizational boundaries
- Service scope
- Framework alignment

### P1.5 Stakeholder Identification (T2+)

For T2 and T3, identify:
- Stakeholder name/role
- Concern (what they care about)
- Which documents they will review/approve

### P1.6 Process Decomposition (T3)

For T3 (Full SMS), decompose the 24 processes into interdependency phases:
- Phase A (Foundation): SPM, ISM, SCFGM, SFM
- Phase B (Agreements): SLM, SDES, SCATM, RELM, SUPPM
- Phase C (Operations): SDESK, IM, SRM, PM, MEM, CHM, RDM
- Phase D (Assurance): AM, SCM, CPM, ITAM, KM, MR, RM, CI

### P1.7 Exit Gate

- [ ] Scoping brief is complete with all required sections
- [ ] Complexity tier is assigned with justification
- [ ] Processes in scope are listed by ID
- [ ] Framework pack is selected (or "agnostic" is noted)
- [ ] User has confirmed the scoping brief

### P1.8 Handoff

Pass to P2 (`3pa-requirements`): scoping brief location, tier, framework pack name.

---

## P1.5: Gap Analysis (Revision Mode Only)

**Skill:** `3pa-intake` (continuation)
**Purpose:** Assess existing documentation against 3PA taxonomy, identify gaps, and prioritize improvements.
**Output:** Gap Analysis Report (`docs/itsm/gap-analysis-report.md`)

> This sub-phase is skipped in greenfield mode.

### P1.5.1 Document Inventory

1. Collect all existing ITSM documentation from the organization
2. For each document, assess:
   - What 3PA category it maps to (or "unmapped")
   - Quality rating (Good / Fair / Poor)
   - Last updated date
   - Whether it is actively used

### P1.5.2 Taxonomy Coverage Assessment

1. For each document type required by the tier, check whether an existing document covers it
2. Rate the action needed: Keep / Update / Rewrite / Create

### P1.5.3 Process Maturity Assessment

1. For each process in scope, assess current maturity (0–5 scale)
2. Define target maturity based on tier and compliance drivers
3. Identify the gap

### P1.5.4 Organizational Readiness Assessment

1. Assess people readiness (roles defined, skills available, capacity, change appetite)
2. Assess tool readiness (adequacy for target processes, gaps, constraints)
3. Assess process readiness (documentation state, adherence, pain points)

### P1.5.5 Gap Analysis Report

1. Scaffold from `templates/gap-analysis-report.md` to `docs/itsm/gap-analysis-report.md`
2. Populate all sections from the assessments above
3. Prioritize gaps: Critical (must address) / Important (should address) / Improvement Opportunity (could address)
4. Recommend the P3 authoring strategy (which docs to Keep / Update / Rewrite / Create)

### P1.5.6 Exit Gate

- [ ] Gap analysis report exists at `docs/itsm/gap-analysis-report.md`
- [ ] All existing documents are inventoried and quality-rated
- [ ] Taxonomy coverage is assessed with action ratings
- [ ] Process maturity is assessed with targets and gaps
- [ ] Organizational readiness (people, tools, processes) is assessed
- [ ] Gaps are prioritized
- [ ] P3 authoring strategy is recommended
- [ ] User has confirmed the gap analysis

### P1.5.7 Handoff

Pass to P2 (`3pa-requirements`): gap analysis report location, recommended strategy, baseline maturity levels.

---

## P2: Requirements & Decisions

**Skill:** `3pa-requirements`
**Purpose:** Elicit detailed requirements for each process in scope, make architectural decisions, and define the RACI approach.
**Output:** Decision Log (`docs/itsm/decision-log.md`), updated Scoping Brief

> **Revision mode:** Focus requirements on the delta from current state. Reference the gap analysis report for existing coverage. Decisions should document what exists and what needs to change, not rebuild from zero.

### P2.1 Requirement Categories (8 Categories, Scaled by Tier)

| # | Category | T1 | T2 | T3 |
|---|----------|:---:|:---:|:---:|
| 1 | Process scope & objectives | Required | Required | Required |
| 2 | Roles & responsibilities | Required | Required | Required |
| 3 | Interfaces with other processes | — | Required | Required |
| 4 | KPIs & metrics | Optional | Required | Required |
| 5 | Tooling & automation | Optional | Required | Required |
| 6 | Compliance & audit requirements | — | Optional | Required |
| 7 | Supplier/vendor management | — | Optional | Required |
| 8 | Continual improvement approach | — | Optional | Required |

### P2.2 Decision Format

Decisions use `D-{number}` IDs with:

```
### D-{number}: {Title}

**Context:** {Why this decision is needed}
**Options Considered:**
1. {Option A} — {pros/cons}
2. {Option B} — {pros/cons}

**Decision:** {Chosen option with reasoning}
**Applies To:** {Process IDs affected, e.g., PR01, PR11, PR15}
**Distribute To:** {Target documents that must reflect this decision}
**Version Gate:** v1.0 | future | out-of-scope
```

### P2.3 Process Interface Mapping (T2+)

For each process in scope, define:
- Inputs: what triggers the process, what data it receives
- Outputs: what it produces
- Interfaces: which other processes it connects to and how

### P2.4 RACI Approach

Define the organizational role model:
- Role names and definitions
- RACI convention (one A per activity, R can be multiple, C/I as needed)
- Escalation hierarchy

### P2.5 ITSM Glossary

Begin the ITSM glossary in the Decision Log:
- Organization-specific term definitions
- Framework-specific terminology mappings
- Acronym definitions

### P2.6 Exit Gate

- [ ] All requirement categories (per tier) are addressed
- [ ] Decision log contains at least one decision per process in scope
- [ ] Process interfaces are mapped (T2+)
- [ ] RACI approach is defined
- [ ] Glossary has initial entries
- [ ] User has confirmed requirements and decisions

### P2.7 Handoff

Pass to P3 (`3pa-author`): decision log location, requirement summary, framework pack name.

---

## P3: Document Authoring

**Skill:** `3pa-author`
**Purpose:** Author all documents in dependency layer order, enforcing the ITSM document hierarchy.
**Output:** Complete document corpus in `docs/itsm/`

> **Revision mode:** Load existing documents alongside best practices. Author only documents marked Create or Rewrite in the gap analysis. Update documents marked Update. Skip documents marked Keep. Best practices serve as reference for both new authoring and revision quality targets.

### P3.1 Authoring Layer Order

Documents must be authored in dependency layer order (see `3PA-Document-Taxonomy.md`):

```
Layer 0: SMS Policy (umbrella governance)
Layer 1: Process Policies (per-process strategic intent)
Layer 2: Process Definitions (what/why/who/interfaces)
Layer 3: RACI Matrices, KPI Definitions (cross-cutting assignments)
Layer 4: Procedures (step-by-step how-to)
Layer 5: Templates & Records (SLA, OLA, Service Catalogue, Risk Register, CSI Register)
```

A document at Layer N must reach draft status before any Layer N+1 document begins.

### P3.2 Process Interdependency (Within Layer 2)

When authoring multiple process definitions (T2/T3), follow the interdependency phases:

- **Phase A (Foundation):** PR01 SPM, PR09 ISM, PR17 SCFGM, PR03 SFM (T3)
- **Phase B (Agreements):** PR02 SLM, PR04 SDES (T3), PR05 SCATM (T2+), PR22 RELM, PR23 SUPPM (T2+)
- **Phase C (Operations):** PR10 SDESK, PR11 IM, PR12 SRM, PR13 PM, PR14 MEM (T2+), PR15 CHM, PR16 RDM (T2+)
- **Phase D (Assurance):** PR06 AM, PR07 SCM (T2+), PR08 CPM, PR18 ITAM (T2+), PR19 KM (T2+), PR20 MR, PR21 RM (T2+), PR24 CI

T1 authors one process only. T2 authors the group in dependency order (includes T2+ processes). T3 authors all 24 in A→B→C→D.

### P3.3 Template Scaffolding

For each document:
1. Select the appropriate template from `templates/`
2. Fill YAML frontmatter with organization, scope, process_id, framework
3. Author content section by section
4. Insert Mermaid diagrams where specified by the template
5. Mark cross-references to other documents

### P3.4 RACI Enforcement

During authoring:
- Every activity in a process definition must appear in the RACI matrix
- Every role in the RACI matrix must be defined in the role definitions section
- One and only one "A" (Accountable) per activity

### P3.5 Shared Contract Tracking

Maintain consistency across documents for all shared contracts listed in `3PA-Overview.md` §9. When authoring a document that defines a contract, note it. When authoring a document that references a contract, verify it matches the definition.

### P3.6 Exit Gate

- [ ] All documents required by tier are authored
- [ ] Layer order was respected (no Layer N+1 before Layer N)
- [ ] Process interdependency order was respected (T2+)
- [ ] All YAML frontmatter is complete and valid
- [ ] All Mermaid diagrams render correctly
- [ ] User has confirmed each layer before proceeding to the next

### P3.7 Handoff

Pass to P4 (`3pa-qa`): document corpus location, tier, list of authored documents.

---

## P4: Quality Assurance

**Skill:** `3pa-qa`
**Purpose:** Run quality gates G1–G8 against the document corpus, identify defects, and drive resolution.
**Output:** Completeness Report (`docs/itsm/completeness-report.md`)

> **Revision mode:** Focus QA on newly authored and updated documents first. Then validate retained (Keep) documents against G1, G3, and G6 to ensure minimum standards. Run G5 across the full corpus (existing + new) to verify cross-document consistency.

### P4.1 Gate Execution Order

Run gates in order G1 → G8. See `3PA-Quality-Gates.md` for full gate definitions.

| Gate | Name | T1 | T2 | T3 |
|------|------|:---:|:---:|:---:|
| G1 | Metadata Integrity | Required | Required | Required |
| G2 | Decision Coverage | Required | Required | Required |
| G3 | Taxonomy Completeness | Required | Required | Required |
| G4 | Internal Consistency | — | Required | Required |
| G5 | Cross-Document Consistency | — | Required | Required |
| G6 | RACI Completeness | Required | Required | Required |
| G7 | Process Interface Integrity | — | Required | Required |
| G8 | Gap Analysis | — | Required | Required |

### P4.2 Resolution Loop

For each gate failure:
1. Log the finding in the completeness report
2. Identify the affected document(s)
3. Propose a fix
4. Apply the fix (with user confirmation)
5. Re-run the gate

If a gate fails 3+ times, escalate to user for an architectural decision.

### P4.3 Status Promotion

After all applicable gates pass:
- Promote document status from `draft` to `review`
- After user sign-off, promote to `approved`

### P4.4 Exit Gate

- [ ] All applicable gates pass (per tier)
- [ ] Completeness report is generated
- [ ] All documents are at `review` status or higher
- [ ] User has reviewed and confirmed the completeness report

### P4.5 Handoff

Pass to P5 (`3pa-publish`): completeness report location, gate results summary.

---

## P5: Assembly & Publication

**Skill:** `3pa-publish`
**Purpose:** Assemble the final documentation pack, generate supporting artifacts, and optionally export to other formats.
**Output:** Documentation Pack Manifest, Document Library, cross-reference index

> **Revision mode:** Merge new and updated documents with retained existing documents into the final pack. The pack manifest should distinguish between new, updated, and retained documents. Include a "Changes from Baseline" section in the document library.

### P5.1 Pack Manifest Assembly

Generate `docs/itsm/documentation-pack-manifest.md`:
- List all documents with title, category, status, version
- Dependency graph (which documents depend on which)
- Approval status summary

### P5.2 Cross-Reference Index

Generate a cross-reference index showing:
- All shared contracts and where they are defined/referenced
- All decision distributions and their target documents
- All process interfaces and their counterparts

### P5.3 Document Library

Generate `docs/itsm/document-library.md`:
- Organized by document type
- Quick-reference links
- Version history summary

### P5.4 Reader Guides (T2+)

For T2+, generate role-specific reader guides:
- "Start here" recommendations by stakeholder role
- Reading order suggestions
- Key documents by concern area

### P5.5 Format Export

Optionally export to:
- PDF (via Markdown-to-PDF tooling)
- Wiki format (Confluence, SharePoint)
- DOCX (via pandoc)

See `3PA-Tooling-Guide.md` for export procedures.

### P5.6 Framework Knowledge Harvest

If new patterns were discovered during P1–P4:
1. Extract reusable knowledge
2. Update the framework pack (or create a new one)
3. Increment the pack version
4. Anonymize organization-specific details

### P5.7 Exit Gate

- [ ] Documentation pack manifest is complete
- [ ] Cross-reference index is generated
- [ ] Document library is generated
- [ ] All documents are at `approved` status
- [ ] Format exports are complete (if requested)
- [ ] Framework pack is updated (if applicable)
- [ ] User has confirmed the final deliverable

### P5.8 Completion

The documentation pack is the final deliverable. No further phases.

---

## Cross-References

- Overview and architecture: `3PA-Overview.md`
- Document taxonomy and layers: `3PA-Document-Taxonomy.md`
- Quality gate definitions: `3PA-Quality-Gates.md`
- Framework pack schema: `3PA-Framework-Pack-Specification.md`
- Tooling and export: `3PA-Tooling-Guide.md`
- Gap analysis template: `templates/gap-analysis-report.md`
