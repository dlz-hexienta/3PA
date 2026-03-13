# 3PA Quality Gates

> Defines the 8 quality gates run during P4 (Quality Assurance). Each gate specifies what it checks, pass/fail criteria, and tier applicability.

## Gate Summary

| Gate | Name | T1 | T2 | T3 | Focus |
|------|------|:---:|:---:|:---:|-------|
| G1 | Metadata Integrity | Required | Required | Required | YAML frontmatter validity |
| G2 | Decision Coverage | Required | Required | Required | Decision-to-document traceability |
| G3 | Taxonomy Completeness | Required | Required | Required | All required documents exist |
| G4 | Internal Consistency | — | Required | Required | Each document is self-consistent |
| G5 | Cross-Document Consistency | — | Required | Required | Shared contracts match across docs |
| G6 | RACI Completeness | Required | Required | Required | One A per activity, role matching |
| G7 | Process Interface Integrity | — | Required | Required | Bidirectional interface matching |
| G8 | Gap Analysis | — | Required | Required | Coverage vs framework requirements |

---

## G1: Metadata Integrity

**Tier:** All tiers
**Purpose:** Verify that every document has valid, complete YAML frontmatter.

### Checks

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1.1 | Frontmatter exists | Every `.md` file in `docs/itsm/` has a YAML frontmatter block |
| 1.2 | Required fields present | All required fields per document type are populated (see `3PA-Document-Taxonomy.md` §4) |
| 1.3 | Category valid | `category` value is one of the 17 defined category IDs |
| 1.4 | Status valid | `status` is one of: `draft`, `review`, `approved` |
| 1.5 | Version format | `version` matches pattern `x.y` |
| 1.6 | Date format | `date` matches `YYYY-MM-DD` |
| 1.7 | Process ID valid | `process_id` is `PR1`–`PR14` or `~` |
| 1.8 | Framework valid | `framework` is one of: `fitsm`, `itil-v4`, `it4it`, `siam`, or `~` |

### Failure Action

Fix the frontmatter field in the affected document. Re-run G1.

---

## G2: Decision Coverage

**Tier:** All tiers
**Purpose:** Verify that every decision in the Decision Log has been distributed to its target documents.

### Checks

| # | Check | Pass Criteria |
|---|-------|---------------|
| 2.1 | Distribution complete | Every D-{n} with `Distribute To` targets has corresponding content in those documents |
| 2.2 | Process application | Every D-{n} with `Applies To` process IDs references valid processes in scope |
| 2.3 | Version gate | Decisions marked `v1.0` are fully implemented; `future` and `out-of-scope` are noted but not required |

### Failure Action

Identify the missing distribution. Add the decision content to the target document or update the decision's distribution list. Re-run G2.

---

## G3: Taxonomy Completeness

**Tier:** All tiers
**Purpose:** Verify that all documents required by the assigned tier exist and have content.

### Checks

| # | Check | Pass Criteria |
|---|-------|---------------|
| 3.1 | Required docs exist | All document types marked "Required" for the tier in `3PA-Document-Taxonomy.md` §1 have corresponding files |
| 3.2 | Per-process docs complete | For each process in scope, required per-process documents (policy, definition, procedure, RACI) exist |
| 3.3 | Content minimum | Each required document has at least its mandatory sections populated (not empty/placeholder) |

### Failure Action

Create missing documents using templates. Author missing sections. Re-run G3.

**Revision mode note:** Documents marked "Keep" in the gap analysis report count toward taxonomy completeness. Their content is assessed but not required to match 3PA template structure exactly.

---

## G4: Internal Consistency

**Tier:** T2+
**Purpose:** Verify that each document is internally self-consistent.

### Checks

| # | Check | Pass Criteria |
|---|-------|---------------|
| 4.1 | Section completeness | All template-defined sections are present |
| 4.2 | Internal cross-refs valid | References within the document point to existing sections |
| 4.3 | Mermaid diagrams valid | All Mermaid blocks use valid syntax |
| 4.4 | Role consistency | Roles mentioned in the body match the roles section |
| 4.5 | Process ID consistency | `process_id` in frontmatter matches the process described in the body |

### Failure Action

Fix the inconsistency within the document. Re-run G4.

---

## G5: Cross-Document Consistency

**Tier:** T2+
**Purpose:** Verify that shared contracts are consistent across the entire document corpus.

### Checks (11 Shared Contract Checks)

| # | Contract | Defined In | Referenced By | Check |
|---|----------|-----------|--------------|-------|
| 5.1 | Role Definitions | RACI Matrix | All process defs, all procedures | Role names match exactly |
| 5.2 | Process Interfaces | Process Definitions | Other process defs, procedures | Interface descriptions match |
| 5.3 | Service Definitions | Service Catalogue | SLA, process defs, reporting | Service names and IDs match |
| 5.4 | Priority Matrix | Incident Process / SMS Policy | SLA, Change, Problem | Priority levels and definitions match |
| 5.5 | Change Categories | Change Process | Release, Config, Incident | Category names and criteria match |
| 5.6 | Glossary | Decision Log | All documents | Terms used consistently |
| 5.7 | Policy ↔ Process | Process Policy | Process Definition | Policy statements reflected in process |
| 5.8 | KPIs ↔ Process | KPI Definition | Process Definition | KPI targets match process objectives |
| 5.9 | Compliance | SMS Policy | Process defs, audit evidence | Compliance requirements addressed |
| 5.10 | Escalation Paths | Incident Process | Problem, procedures, SLA | Escalation levels and contacts match |
| 5.11 | Approval Authorities | Change Process / SMS Policy | Release, procedures | Approval roles and thresholds match |

### Failure Action

Identify the source-of-truth document (Defined In) and update the referencing document to match. Re-run G5.

---

## G6: RACI Completeness

**Tier:** All tiers
**Purpose:** Verify RACI matrix integrity — the highest-value ITSM-specific quality check.

### Checks

| # | Check | Pass Criteria |
|---|-------|---------------|
| 6.1 | One A per activity | Every activity row has exactly one "A" (Accountable) |
| 6.2 | At least one R per activity | Every activity row has at least one "R" (Responsible) |
| 6.3 | Role name matching | All role names in the RACI matrix match the role definitions |
| 6.4 | Activity coverage | All activities described in the process definition appear in the RACI |
| 6.5 | No orphan roles | Every role in the RACI appears in at least one activity |
| 6.6 | Cross-process role consistency (T2+) | Same role name means the same role across all RACI matrices |

### Failure Action

Fix the RACI matrix. Common fixes: add missing A assignments, resolve duplicate A's, align role names. Re-run G6.

---

## G7: Process Interface Integrity

**Tier:** T2+ (required), T3 (required with full interface map)
**Purpose:** Verify that process interfaces are bidirectional and consistent — the most common ITSM documentation inconsistency.

### Checks

| # | Check | Pass Criteria |
|---|-------|---------------|
| 7.1 | Bidirectional matching | If Process A declares an output to Process B, Process B declares that input from Process A |
| 7.2 | Interface naming | Interface names match across connected processes |
| 7.3 | Trigger consistency | Triggers in one process match outputs in the triggering process |
| 7.4 | Data flow consistency | Data objects passed between processes are described consistently |
| 7.5 | Completeness (T3) | All 14 processes have their interfaces fully mapped |

### Failure Action

Identify the mismatched interface. Determine the authoritative process (earlier in Phase A→D order) and update the other. Re-run G7.

---

## G8: Gap Analysis

**Tier:** T2+
**Purpose:** Identify gaps between the documentation corpus and framework requirements.

### Checks

| # | Check | Pass Criteria |
|---|-------|---------------|
| 8.1 | Framework coverage | All processes required by the selected framework are documented |
| 8.2 | Requirement mapping | Framework-specific requirements (e.g., FitSM GR1–GR7) are addressed |
| 8.3 | Compliance readiness | Documents needed for certification/audit are complete (T3) |
| 8.4 | TBD resolution | No unresolved TBD markers remain in approved documents |

### Failure Action

Document the gaps in the completeness report. Prioritize resolution. Author missing content. Re-run G8.

**Revision mode note:** G8 checks should reference the gap analysis report from P1.5. Gaps identified there and addressed in P3 should show as resolved. Remaining gaps should be documented with justification.

---

## Resolution Escalation

If any gate fails 3 or more consecutive times:

1. Stop automated resolution
2. Present the finding and attempted fixes to the user
3. Escalate as an architectural decision
4. Record the decision in the Decision Log with D-{n} format
5. Apply the decision and re-run the gate

## Gate Execution in Large Corpora

For T3 corpora (50–80+ documents), batch gate checks by:

1. **G1–G3, G8:** Can run across the full corpus
2. **G4:** Run per-document
3. **G5:** Batch by shared contract type (run all Role Definition checks, then all Process Interface checks, etc.)
4. **G6:** Run per-RACI matrix
5. **G7:** Run per-process-interface pair

## Cross-References

- Gate execution procedure: `3PA-Phase-Guide.md` §P4
- Document types and layers: `3PA-Document-Taxonomy.md`
- Shared contract definitions: `3PA-Overview.md` §9
- Framework pack quality checks: `3PA-Framework-Pack-Specification.md`
