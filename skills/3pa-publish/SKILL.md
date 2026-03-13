---
name: 3pa-publish
description: "P5 Assembly & Publication — Assemble the final documentation pack, generate supporting artifacts, and export."
user_invocable: true
---

# 3PA Publish — P5 Assembly & Publication

## Methodology Reference

- Primary: `methodology/3PA-Phase-Guide.md` §P5
- Tooling: `methodology/3PA-Tooling-Guide.md`
- Framework Packs: `methodology/3PA-Framework-Pack-Specification.md` §3.5

## Prerequisites

- P4 complete: `docs/itsm/completeness-report.md` exists, all applicable gates pass
- All documents at `review` or `approved` status
- No unresolved critical findings

## Procedure

### Step 1: Load Context

1. Read `docs/itsm/completeness-report.md` for gate results and document status
2. Read `docs/itsm/scoping-brief.md` for tier and scope
3. Inventory all documents in `docs/itsm/`

### Step 2: Assemble Pack Manifest

> **Revision mode:** The pack manifest should distinguish between documents authored new in this engagement, documents updated/revised, and documents retained from existing documentation. Include a "Changes from Baseline" section in the document library.

1. Copy `templates/documentation-pack-manifest.md` to `docs/itsm/documentation-pack-manifest.md`
2. Fill the pack summary
3. Populate the document inventory table (all documents with category, process ID, status, version)
4. Generate the dependency graph (Mermaid diagram)
5. Build the shared contract index
6. Build the decision distribution index
7. Record approval status for each document

### Step 3: Generate Cross-Reference Index

Build a comprehensive cross-reference showing:
1. All shared contracts — where defined, where referenced, consistency status
2. All decision distributions — D-{n} to target documents
3. All process interfaces — bidirectional pairs
4. All role references — RACI to process definitions to procedures

### Step 4: Generate Document Library

1. Copy `templates/document-library.md` to `docs/itsm/document-library.md`
2. Organize documents by type (governance, policies, definitions, etc.)
3. Add version and status information
4. For T2+: add the reader guide section with role-specific recommendations

### Step 5: Reader Guides (T2+)

For each stakeholder identified in the scoping brief:
1. Recommend a "start here" document
2. List key documents by concern area
3. Suggest a reading order

### Step 6: Format Export (Optional)

If the user requests export:
1. Determine target format (PDF, DOCX, Wiki)
2. Follow the export procedures in `3PA-Tooling-Guide.md` §4
3. Pre-render Mermaid diagrams if needed
4. Record export formats and locations in the pack manifest

### Step 7: Framework Knowledge Harvest

If new patterns were discovered during P1–P4:
1. Identify reusable knowledge (new processes, roles, requirements, terminology)
2. Update the framework pack or create a new one
3. Anonymize organization-specific details
4. Increment the pack version
5. Update `last_updated` date

### Step 8: Final Status Promotion

1. Promote all documents to `approved` status (with user sign-off)
2. Update the pack manifest with final approval summary
3. Set the pack version to 1.0

### Step 9: User Confirmation

Present the final documentation pack summary. Confirm delivery.

## Exit Gate

- [ ] Documentation pack manifest exists at `docs/itsm/documentation-pack-manifest.md`
- [ ] Document library exists at `docs/itsm/document-library.md`
- [ ] Cross-reference index is complete
- [ ] Dependency graph is generated (Mermaid)
- [ ] All documents are at `approved` status
- [ ] Reader guides are complete (T2+)
- [ ] Format exports are done (if requested)
- [ ] Framework pack is updated (if applicable)
- [ ] Pack manifest YAML frontmatter is valid
- [ ] User has confirmed the final deliverable

## Handoff

None — P5 is the final phase. The documentation pack is the deliverable.

## When Things Go Wrong

| Problem | Resolution |
|---------|-----------|
| Documents still at `review` status | Return to P4 for final sign-off; cannot publish until `approved` |
| Cross-reference reveals inconsistency | Return to P3/P4 for the affected documents; re-run P5 after |
| Export tooling not available | Deliver Markdown as-is; document the export steps for the user to run later |
| Framework pack harvest produces org-specific content | Anonymize thoroughly; if unsure, do not include in the pack |
| User wants partial publication | Generate manifest for the approved subset; note pending documents |
| Pack is too large for single delivery | Organize by process group or Phase A–D; deliver in segments |
