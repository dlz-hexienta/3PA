# 3PA Overview

> **Policy, Process, Procedure Architect** — A reusable system for creating operations-ready ITSM documentation packs at enterprise depth.

## 1. What Is 3PA?

3PA produces internally consistent corpora of ITSM policy, process, and procedure documents. It is **not** a software design tool — the documentation **is** the deliverable. The framework is auto-scaling: complexity tier (T1/T2/T3) is determined during intake and controls which documents, quality gates, and effort levels apply.

3PA replicates the proven architecture of PAF, adapted for the ITSM documentation domain, with four layers instead of three.

## 2. Four-Layer Architecture

```
┌─────────────────────────────────────────────────┐
│  1. Methodology    (source of truth)            │
│     methodology/*.md                            │
├─────────────────────────────────────────────────┤
│  2. Engine          (automation)                │
│     skills/3pa-*                                │
├─────────────────────────────────────────────────┤
│  3. Framework Packs (framework metadata)        │
│     framework-packs/*.yaml                      │
├─────────────────────────────────────────────────┤
│  4. Best Practices  (reusable content)          │
│     best-practices/pr*/, cross-cutting/         │
└─────────────────────────────────────────────────┘
```

1. **Methodology** (`methodology/`) — Source of truth. Markdown documents defining phases, document taxonomy, quality gates, and tier system. Skills reference these; never the reverse.
2. **Engine** (`skills/`) — Five Claude Code skills that automate each phase. Each skill reads methodology docs, scaffolds from templates, loads framework packs, and enforces exit gates.
3. **Framework Packs** (`framework-packs/`) — YAML files encoding framework-specific knowledge (ITIL v4, FitSM, IT4IT, SIAM). Loaded at P1, injected throughout P1–P5, harvested at P5.
4. **Best Practices** (`best-practices/`) — Anonymized, framework-annotated, maturity-graduated content for each process area (PR1–PR14) plus cross-cutting patterns. Derived from the knowledge library. Loaded during P3 as starting content, harvested at P5.

## 3. Five-Phase Lifecycle

```
P1 Scope & Context → P2 Requirements & Decisions → P3 Document Authoring → P4 Quality Assurance → P5 Assembly & Publication
skill: 3pa-intake       3pa-requirements            3pa-author              3pa-qa                 3pa-publish
```

Each skill produces artifacts in `docs/itsm/`, verifies exit gates, asks for user confirmation, then hands off to the next. The phase guide (`methodology/3PA-Phase-Guide.md`) is the authoritative reference for each phase's procedures.

There is no P6 (Execution) phase — unlike software, ITSM documentation does not require a build phase. The documentation pack is the final deliverable.

## 4. Complexity Tiers

| Signal | T1 (Single Process) | T2 (Process Group) | T3 (Full SMS) |
|--------|:---:|:---:|:---:|
| Processes in scope | 1 | 2–5 | 6–14 |
| Organizational roles | 1–5 | 6–15 | 16+ |
| Supplier/vendor count | 0–1 | 2–3 | 4+ |
| Services in catalogue | 1–5 | 6–20 | 21+ |
| Compliance driver | None | Improvement | ISO 20000 / SOC2 |
| Sites / business units | 1 | 2–3 | 4+ |
| Multi-language | No | No | Yes |

| Dimension | T1 | T2 | T3 |
|-----------|:---:|:---:|:---:|
| Documents | 4–7 | 15–30 | 50–80+ |
| Gates | G1–G3, G6 | G1–G8 | G1–G8 |
| Authoring layers | 1–4 (single process) | 0–5 | 0–5 + multi-cluster |

Tier is assigned during P1 intake based on complexity signals. See `3PA-Phase-Guide.md` §P1 for the scoring procedure.

## 5. Engagement Modes

3PA supports two engagement modes, determined at the start of P1:

- **Greenfield:** Building ITSM processes from scratch. Full authoring flow using templates and best practices as starting content.
- **Revision:** Improving or formalizing existing processes. Assessment-first flow with gap analysis (P1.5), targeted authoring, and merge assembly.

The mode affects every phase. See `3PA-Phase-Guide.md` §P1.0 for details.

## 6. ITSM Domain Context

3PA operates exclusively in the IT Service Management domain. The framework draws on four established ITSM frameworks:

- **ITIL v4** — Industry-standard service management framework with 34 practices
- **FitSM** — Lightweight, standards-compatible ITSM framework with 14 processes (PR1–PR14)
- **IT4IT** — IT management reference architecture from The Open Group
- **SIAM** — Service Integration and Management for multi-supplier environments

Framework packs encode framework-specific knowledge so that 3PA can produce documentation aligned to any of these frameworks, or a hybrid approach.

## 7. Document Hierarchy

ITSM documentation follows a natural hierarchy:

```
Policy (strategic intent — WHY)
  └── Process Definition (operational model — WHAT/WHO/WHEN)
        └── Procedure (step-by-step instructions — HOW)
              └── Templates & Records (evidence — PROOF)
```

This hierarchy drives the authoring layer order in P3. See `3PA-Document-Taxonomy.md` for the full taxonomy.

## 8. Artifact Location

All ITSM artifacts are saved to `docs/itsm/` when installed in a project. Naming convention: `{organization}-{document-type}.md` for ITSM docs, plain type names for shared artifacts (scoping-brief, decision-log, completeness-report, documentation-pack-manifest).

## 9. Key Relationships

- **Skills → Methodology:** Skills reference methodology as source of truth for procedures and rules
- **Skills → Templates:** P3 skill (`3pa-author`) scaffolds documents from `templates/`
- **Skills → Framework Packs:** Loaded at P1, injected throughout P1–P5 (extra questions, prompts, sections, checks)
- **Skills → Best Practices:** P3 skill (`3pa-author`) loads best practices as starting content for document authoring
- **Best Practices → Framework Packs:** Best practices are framework-annotated; framework pack selection determines which annotations are active
- **Quality Gates → Documents:** P4 skill (`3pa-qa`) runs gates G1–G8 against the document corpus; gate definitions in `3PA-Quality-Gates.md`
- **Gap Analysis → Authoring:** Revision mode gap analysis (P1.5) determines which documents to create/update/keep in P3

## 10. Shared Contracts

These must stay consistent across documents — verified by gate G5 (Cross-Document Consistency):

| Contract | Defined In | Referenced By |
|----------|-----------|--------------|
| Role Definitions | RACI Matrix | All process defs, all procedures |
| Process Interfaces | Process Definitions | Other process defs, procedures |
| Service Definitions | Service Catalogue | SLA, process defs, reporting |
| Priority Matrix | Incident Process / SMS Policy | SLA, Change, Problem |
| Change Categories | Change Process | Release, Config, Incident |
| CI Types | Config Process | Change, Incident, Problem |
| Escalation Paths | Incident Process | Problem, procedures, SLA |
| Approval Authorities | Change Process / SMS Policy | Release, procedures |
| ITSM Glossary | Decision Log | All documents |
| Compliance Clauses | SMS Policy | Process defs, audit evidence |
| Reporting Periods | Service Reporting Process | KPIs, SLAs |

## 11. Security

ITSM documentation corpora may contain sensitive organizational information (org structures, security processes, escalation contacts, compliance details). For proprietary deployments, treat `docs/itsm/` as confidential. Framework packs must be anonymized before sharing.

## 12. Error Handling

Each skill has a "When Things Go Wrong" section covering common failure modes. Key principles:

- Unanswerable questions → record as TBD, flag at exit gate
- Gate fails 3+ times → escalate to user for architectural decision
- Large corpus exceeds context → batch checks by shared contract type
- Missing templates → warn and scaffold manually from taxonomy descriptions

## 13. Cross-References

- Phase procedures: `3PA-Phase-Guide.md`
- Document types and layers: `3PA-Document-Taxonomy.md`
- Quality gate definitions: `3PA-Quality-Gates.md`
- Framework pack schema: `3PA-Framework-Pack-Specification.md`
- Tooling and export: `3PA-Tooling-Guide.md`
- Best practices library: `best-practices/_index.md`
