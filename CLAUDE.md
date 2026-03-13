# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What is 3PA

**Policy, Process, Procedure Architect** — a reusable system for creating operations-ready ITSM documentation packs at enterprise depth. It produces internally consistent document corpora through a 5-phase lifecycle with automated quality gates. The framework is auto-scaling: complexity tier (T1/T2/T3) is determined during intake and controls which documents, quality gates, and effort levels apply.

3PA is separate from PAF but replicates PAF's proven architecture, adapted for the ITSM documentation domain with four layers. The documentation IS the deliverable — there is no software to build.

## Four-Layer Architecture

1. **Methodology** (`methodology/`) — Source of truth. Markdown docs defining phases, document taxonomy, quality gates, and tier system. Skills reference these; never the reverse.
2. **Engine** (`skills/`) — Five Claude Code skills that automate each phase. Each skill reads methodology docs, scaffolds from templates, loads framework packs, and enforces exit gates.
3. **Framework Packs** (`framework-packs/`) — YAML files encoding framework-specific knowledge (ITIL v4, FitSM, IT4IT, SIAM). Loaded at P1, injected throughout P1–P5, harvested at P5.
4. **Best Practices** (`best-practices/`) — Anonymized, maturity-graduated content for each process area (PR01–PR24) plus cross-cutting patterns. Derived from the knowledge library. Loaded during P3 as starting content, harvested at P5.

## Phase Chain

```
P1 Scope & Context → P2 Requirements & Decisions → P3 Document Authoring → P4 Quality Assurance → P5 Assembly & Publication
skill: 3pa-intake       3pa-requirements            3pa-author              3pa-qa                 3pa-publish
```

Each skill produces artifacts in `docs/itsm/`, verifies exit gates, asks for user confirmation, then hands off to the next.

## Complexity Tiers

- **T1 (Single Process):** 1 process, 1–5 roles, no compliance driver. 4–7 docs, gates G1–G3 + G6.
- **T2 (Process Group):** 2–5 processes, 6–15 roles, improvement-driven. 15–30 docs, gates G1–G8.
- **T3 (Full SMS):** 6–24 processes, 16+ roles, ISO 20000/SOC2. 50–80+ docs, all 8 gates.

Tier is assigned during P1 intake based on complexity signals (processes, roles, suppliers, services, compliance, sites, language).

## Engagement Modes

- **Greenfield:** Building processes from scratch. Templates + best practices → full authoring flow.
- **Revision:** Improving existing processes. Gap analysis (P1.5) → targeted authoring → merge assembly.

Mode is determined at P1 start and affects every downstream phase. P1 collects organizational context (people, tools, existing processes) in addition to scope.

## Document Authoring Order

P3 documents must be authored in dependency layer order:

- **Layer 0:** SMS Policy (umbrella governance) — T2+ only
- **Layer 1:** Process Policies (per-process strategic intent)
- **Layer 2:** Process Definitions (what/why/who/interfaces) — authored in Phase A→B→C→D order
- **Layer 3:** RACI Matrices, KPI Definitions (cross-cutting assignments)
- **Layer 4:** Procedures (step-by-step how-to)
- **Layer 5:** Templates & Records (SLA, OLA, Service Catalogue, Risk Register, CSI Register)

A document at Layer N must reach draft before any Layer N+1 document begins.

## Process Interdependency (Layer 2 Ordering)

- **Phase A (Foundation):** PR01 SPM, PR09 ISM, PR17 SCFGM, PR03 SFM (T3)
- **Phase B (Agreements):** PR02 SLM, PR04 SDES (T3), PR05 SCATM (T2+), PR22 RELM, PR23 SUPPM (T2+)
- **Phase C (Operations):** PR10 SDESK, PR11 IM, PR12 SRM, PR13 PM, PR14 MEM (T2+), PR15 CHM, PR16 RDM (T2+)
- **Phase D (Assurance):** PR06 AM, PR07 SCM (T2+), PR08 CPM, PR18 ITAM (T2+), PR19 KM (T2+), PR20 MR, PR21 RM (T2+), PR24 CI

## Shared Contracts

These must stay consistent across documents — verified by gate G5:
- Role Definitions (RACI Matrix → All)
- Process Interfaces (Process Definitions ↔ All)
- Service Definitions (Service Catalogue → SLA, process defs, reporting)
- Priority Matrix (Incident Process / SMS Policy → SLA, Change, Problem)
- Change Categories (Change Process → Release, Config, Incident)
- ITSM Glossary (Decision Log → All)
- Policy ↔ Process alignment
- KPIs ↔ Process objectives
- Compliance clauses (SMS Policy → process defs, audit evidence)
- Escalation Paths (Incident Process → Problem, procedures, SLA)
- Approval Authorities (Change Process / SMS Policy → Release, procedures)

## Decision Format

Decisions use `D-{number}` IDs with: Context, Options Considered, Decision (with reasoning), Applies To (process IDs), Distribute To (target documents), Version Gate (v1.0/future/out-of-scope).

## YAML Frontmatter Standard

All documents use this frontmatter:
```yaml
---
title: string
organization: string
scope: string              # Process IDs or "SMS"
category: enum             # One of 17 category IDs
process_id: string | ~     # PR01–PR24 or ~
status: draft | review | approved
version: "x.y"
date: YYYY-MM-DD
parent: filename | ~
depends_on: []
framework: string | ~      # fitsm | itil-v4 | it4it | siam | ~
tags: []
---
```

## Artifact Location

All ITSM artifacts are saved to `docs/itsm/`. Naming convention: `{organization}-{document-type}.md` for ITSM docs, plain type names for shared artifacts (scoping-brief, decision-log, completeness-report, documentation-pack-manifest).

## Diagrams

Process flow diagrams use Mermaid syntax in Markdown fenced blocks. Diagram types scale by tier: T1 gets flowcharts only, T2 adds sequence/state, T3 adds Gantt/C4 context. Templates include Mermaid scaffolds with placeholders.

## Key Relationships

- **Skills → Methodology:** Skills reference methodology as source of truth for procedures and rules
- **Skills → Templates:** P3 skill (`3pa-author`) scaffolds documents from `templates/`
- **Skills → Framework Packs:** Loaded at P1, injected throughout P1–P5
- **Skills → Best Practices:** P3 skill loads best practices as starting content for document authoring
- **Quality Gates → Documents:** P4 skill (`3pa-qa`) runs gates G1–G8; definitions in `methodology/3PA-Quality-Gates.md`
- **Gap Analysis → Authoring:** Revision mode gap analysis determines which documents to create/update/keep

## Error Handling

- Unanswerable questions → record as TBD, flag at exit gate
- Gate fails 3+ times → escalate to user for architectural decision
- Large corpus exceeds context → batch checks by shared contract type
- Missing templates → warn and scaffold manually from taxonomy descriptions

## Security

ITSM documentation corpora may contain sensitive organizational information. For proprietary deployments, treat `docs/itsm/` as confidential. Framework packs must be anonymized before sharing.

## Knowledge Library

The `FitSM/`, `ITIL v4/`, `it4it.pdf`, and `SIAM-*.pdf` files are the source knowledge library. These are reference materials only — they are not modified by 3PA.
