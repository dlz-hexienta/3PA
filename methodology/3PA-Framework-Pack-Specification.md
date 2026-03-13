# 3PA Framework Pack Specification

> Defines the schema and lifecycle for framework packs — YAML files encoding framework-specific ITSM knowledge.

## 1. Purpose

Framework packs encode knowledge from specific ITSM frameworks (ITIL v4, FitSM, IT4IT, SIAM) so that 3PA can produce documentation aligned to any of these frameworks. Unlike PAF's domain packs (which vary by software domain), 3PA's framework packs vary by ITSM framework lens — the domain is always IT Service Management.

## 2. Schema

```yaml
# Framework Pack Schema
# Location: framework-packs/{framework-name}.yaml

meta:
  name: string              # Framework name (e.g., "FitSM v3")
  version: "x.y"            # Pack version
  framework_id: string      # fitsm | itil-v4 | it4it | siam
  description: string       # One-line description
  source_version: string    # Version of the source framework
  last_updated: YYYY-MM-DD
  keywords: []              # Matching keywords for P1 auto-detection

process_model:
  processes: []              # List of process definitions
    # - id: string           # Process ID (e.g., PR1, PR9)
    #   name: string         # Process name
    #   purpose: string      # One-line purpose
    #   scope: string        # What's in/out of scope
    #   phase: A | B | C | D # Interdependency phase
    #   inputs: []           # List of inputs
    #   outputs: []          # List of outputs
    #   interfaces: []       # Connected processes
    #   activities: []       # Key activities
    #   kpis: []             # Suggested KPIs

role_model:
  roles: []                  # List of role definitions
    # - id: string           # Role ID
    #   name: string         # Role name
    #   description: string  # Role description
    #   processes: []        # Processes this role participates in
    #   raci_default: {}     # Default RACI assignments

general_requirements:
  requirements: []           # Framework general requirements
    # - id: string           # Requirement ID (e.g., GR1)
    #   name: string         # Requirement name
    #   description: string  # What the requirement mandates
    #   evidence: []         # What documents/artifacts satisfy it
    #   tier_applicability:  # Which tiers need this
    #     t1: boolean
    #     t2: boolean
    #     t3: boolean

compliance_mapping:
  standards: []              # Mapped standards
    # - standard: string     # Standard name (e.g., "ISO/IEC 20000-1:2018")
    #   clauses: []          # Clause-to-process mapping
    #     - clause: string   # Clause number
    #       title: string    # Clause title
    #       processes: []    # Process IDs that address this clause
    #       documents: []    # Document types needed for evidence

intake_questions:
  questions: []              # Additional P1 intake questions
    # - question: string     # The question text
    #   rationale: string    # Why this question matters for this framework
    #   signal: string       # What complexity signal it provides

requirement_prompts:
  prompts: []                # Additional P2 requirement prompts
    # - category: string     # Requirement category
    #   prompt: string       # The prompt text
    #   framework_context: string  # Why this matters for this framework

document_section_templates:
  templates: []              # Framework-specific section additions
    # - document_type: string  # Category ID from taxonomy
    #   sections: []           # Additional sections to include
    #     - heading: string    # Section heading
    #       guidance: string   # What to write in this section
    #       tier: string       # Minimum tier (t1, t2, t3)

quality_checks:
  checks: []                 # Framework-specific quality checks
    # - gate: string          # Which gate this extends (G1–G8)
    #   check: string         # What to check
    #   pass_criteria: string # How to determine pass/fail
    #   tier: string          # Minimum tier

terminology:
  terms: []                  # Framework-specific terminology
    # - term: string          # The term
    #   definition: string    # Framework-specific definition
    #   aliases: []           # Alternative names in other frameworks
    #   context: string       # When/how to use this term

tooling_recommendations:
  tools: []                  # Recommended tools for this framework
    # - name: string          # Tool name
    #   purpose: string       # What it's used for
    #   url: string           # Where to find it
    #   integration: string   # How it integrates with 3PA outputs

best_practices_ref:
  mapping: []                # Links framework concepts to best practice files
    # - framework_concept: string  # Framework-specific concept name
    #   best_practice_path: string # Path to best practice file
    #   notes: string              # Adaptation notes for this framework
```

## 3. Lifecycle

### 3.1 Loading (P1)

1. During intake, match the organization's description to framework pack `keywords`
2. If a match is found, load the pack
3. Inject `intake_questions` into the standard P1 question set
4. Use `process_model` to suggest processes for scoping

### 3.2 Requirements Injection (P2)

1. Inject `requirement_prompts` into the P2 requirement elicitation
2. Use `general_requirements` to identify mandatory requirements
3. Use `compliance_mapping` to surface relevant compliance clauses

### 3.3 Authoring Injection (P3)

1. Use `document_section_templates` to add framework-specific sections to document templates
2. Use `terminology` for consistent term usage
3. Use `role_model` for RACI scaffolding
4. Use `process_model` for process definition scaffolding
5. Use `best_practices_ref.mapping` to identify which best practice files to load and apply framework-specific adaptation notes

### 3.4 Quality Injection (P4)

1. Run `quality_checks` as extensions to the standard gates
2. Use `compliance_mapping` for G8 gap analysis
3. Use `terminology` for glossary consistency checks

### 3.5 Harvest (P5)

1. Extract new patterns discovered during P1–P4
2. Add new processes, roles, requirements, or terminology to the pack
3. Increment the pack `version`
4. Anonymize organization-specific details
5. Update `last_updated` date

## 4. Pack Creation Guidelines

- Start from `_template.yaml` in `framework-packs/`
- Populate from the source framework documentation
- Validate against the schema above
- Test by running a T1 project through P1–P5
- Iterate based on quality gate findings

## 5. Pack Sharing

Framework packs must be anonymized before sharing:
- Remove organization-specific terminology entries
- Remove organization-specific intake questions
- Remove any proprietary process adaptations
- Keep only framework-standard content

## 6. Cross-References

- Pack template: `framework-packs/_template.yaml`
- Intake procedure: `3PA-Phase-Guide.md` §P1.1
- Quality gates: `3PA-Quality-Gates.md`
- Document taxonomy: `3PA-Document-Taxonomy.md`
- Best practices library: `best-practices/_index.md`
