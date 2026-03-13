# How to Use 3PA

**3PA (Policy, Process, Procedure Architect)** creates operations-ready ITSM documentation packs — policies, process definitions, procedures, RACI matrices, SLAs, and more — tailored to your organization and aligned to your chosen ITSM framework.

## Quick Start

1. Open Claude Code in the `3PA/` directory
2. Run the intake skill: `/3pa-intake`
3. Choose your engagement mode: **greenfield** (building new) or **revision** (improving existing)
4. Answer the scoping questions about your organization
5. Follow the guided 5-phase workflow

## What 3PA Produces

A complete, internally consistent set of ITSM documentation, saved to `docs/itsm/` in your project. The exact documents depend on your complexity tier:

| Tier | Scope | Documents | Example |
|------|-------|:---------:|---------|
| **T1** | Single Process | 4–7 | "We need an incident management process" |
| **T2** | Process Group | 15–30 | "We need incident, change, and problem management" |
| **T3** | Full SMS | 50–80+ | "We need a complete service management system for ISO 20000" |

## Engagement Modes

### Greenfield (Building from Scratch)

Choose this if your organization has no existing ITSM documentation or is replacing everything. 3PA uses best practices from its library as starting content and guides you through full authoring.

### Revision (Improving Existing)

Choose this if your organization has existing ITSM processes and documentation. 3PA assesses what you have, identifies gaps, and focuses authoring only on what's missing or inadequate. The revision flow adds a **Gap Analysis** step (P1.5) between intake and requirements.

## The 5 Phases

### P1: Scope & Context (`/3pa-intake`)

3PA asks 21 questions across 7 sections about your organization, people, tools, services, and ITSM needs. Based on your answers, it:
- Determines your complexity tier (T1, T2, or T3)
- Captures your organizational context (people, tools, existing processes)
- Identifies which processes are in scope
- Selects a framework pack (if applicable)
- Produces a **Scoping Brief**
- In revision mode: produces a **Gap Analysis Report** (P1.5)

### P2: Requirements & Decisions (`/3pa-requirements`)

3PA elicits detailed requirements for each process and records architectural decisions:
- What each process needs to achieve
- Who is involved (roles and responsibilities)
- How processes connect to each other
- Produces a **Decision Log** with an ITSM glossary

### P3: Document Authoring (`/3pa-author`)

3PA loads best practices as starting content and authors all documents in dependency order:

```
Layer 0: SMS Policy (umbrella governance)
Layer 1: Process Policies (strategic intent per process)
Layer 2: Process Definitions (operational models)
Layer 3: RACI Matrices & KPI Definitions
Layer 4: Procedures (step-by-step instructions)
Layer 5: SLAs, OLAs, Service Catalogue, Risk & CSI Registers
```

Each layer is confirmed with you before the next begins.

### P4: Quality Assurance (`/3pa-qa`)

3PA runs 8 quality gates against your document corpus:

| Gate | What It Checks |
|------|---------------|
| G1 | Metadata integrity (valid YAML frontmatter) |
| G2 | Decision coverage (all decisions distributed) |
| G3 | Taxonomy completeness (all required docs exist) |
| G4 | Internal consistency (each doc is self-consistent) |
| G5 | Cross-document consistency (shared contracts match) |
| G6 | RACI completeness (one A per activity, roles match) |
| G7 | Process interface integrity (bidirectional matching) |
| G8 | Gap analysis (coverage vs. framework requirements) |

Findings are fixed iteratively. Produces a **Completeness Report**.

### P5: Assembly & Publication (`/3pa-publish`)

3PA assembles the final pack:
- **Documentation Pack Manifest** — inventory of all documents
- **Document Library** — organized index with reader guides
- **Cross-reference index** — all contracts and dependencies mapped
- Optional export to PDF, DOCX, or wiki format

## Complexity Tiers Explained

3PA auto-detects your tier based on these signals:

| Signal | T1 (Single Process) | T2 (Process Group) | T3 (Full SMS) |
|--------|:---:|:---:|:---:|
| Processes in scope | 1 | 2–5 | 6–14 |
| Organizational roles | 1–5 | 6–15 | 16+ |
| Suppliers/vendors | 0–1 | 2–3 | 4+ |
| Services in catalogue | 1–5 | 6–20 | 21+ |
| Compliance driver | None | Improvement | ISO 20000 / SOC2 |
| Sites / business units | 1 | 2–3 | 4+ |

## Framework Packs

3PA can align documentation to specific ITSM frameworks:

- **ITIL v4** — Industry-standard, 34 practices
- **FitSM** — Lightweight, 14 processes (PR1–PR14)
- **IT4IT** — IT management reference architecture
- **SIAM** — Service Integration and Management

Framework packs inject framework-specific questions, templates, quality checks, and terminology into each phase. You can also work framework-agnostic.

## Quality Gates

Not all gates apply to all tiers:

| Gate | T1 | T2 | T3 |
|------|:---:|:---:|:---:|
| G1–G3 | Yes | Yes | Yes |
| G4–G5 | — | Yes | Yes |
| G6 | Yes | Yes | Yes |
| G7 | — | Yes | Yes |
| G8 | — | Yes | Yes |

The two ITSM-specific gates:
- **G6 (RACI Completeness)** — Ensures every activity has exactly one accountable role
- **G7 (Process Interface Integrity)** — Ensures process outputs match connected process inputs

## Best Practices Library

3PA includes a library of anonymized best practices for each ITSM process area (PR1–PR14), derived from ITIL v4, FitSM, IT4IT, and SIAM. During P3 (Document Authoring), best practices are loaded as starting content and customized for your organization.

Best practices are graduated by maturity level:
- **Essential:** Included at all tiers — the minimum viable process
- **Intermediate:** Included at T2+ — mature implementation patterns
- **Advanced:** Included at T3 — optimized, often automated patterns

## File Locations

| What | Where |
|------|-------|
| Methodology docs | `3PA/methodology/` |
| Skills (automation) | `3PA/skills/` |
| Document templates | `3PA/templates/` |
| Framework packs | `3PA/framework-packs/` |
| Best practices library | `3PA/best-practices/` |
| Your ITSM documents | `docs/itsm/` (in your project) |
| Knowledge library | `3PA/FitSM/`, `3PA/ITIL v4/`, etc. |

## Tips

- **Start small:** If unsure, begin with T1 (single process). You can always expand later.
- **Confirm each layer:** 3PA pauses between layers for your review. Use this to course-correct.
- **Use the glossary:** Consistent terminology prevents most quality gate failures.
- **RACI is king:** The RACI matrix is the most-checked artifact. Get it right early.
- **Process interfaces matter:** At T2+, the most common issue is mismatched process interfaces. 3PA checks this automatically.
