#!/usr/bin/env python3
"""Validate a 3PA framework pack YAML file against the schema."""
import sys
import os
import re
import yaml

def validate_pack(path):
    errors = []
    warnings = []

    # 1. YAML parses
    try:
        with open(path) as f:
            pack = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"FATAL: YAML parse error: {e}")
        return False
    if not isinstance(pack, dict):
        print("FATAL: Root element is not a mapping")
        return False

    # 2. Top-level keys
    required_keys = [
        "meta", "process_model", "role_model", "general_requirements",
        "compliance_mapping", "intake_questions", "requirement_prompts",
        "document_section_templates", "quality_checks", "terminology",
        "tooling_recommendations", "best_practices_ref"
    ]
    for key in required_keys:
        if key not in pack:
            errors.append(f"Missing top-level key: {key}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return False

    # 3. meta
    meta = pack["meta"]
    for field in ["name", "version", "framework_id", "description", "source_version", "last_updated", "keywords"]:
        if field not in meta or not meta[field]:
            errors.append(f"meta.{field} is missing or empty")

    # 4. framework_id
    if meta.get("framework_id") not in ("fitsm", "itil-v4", "it4it", "siam"):
        errors.append(f"meta.framework_id '{meta.get('framework_id')}' not in allowed values")

    # 5. date format
    if meta.get("last_updated") and not re.match(r"\d{4}-\d{2}-\d{2}", str(meta["last_updated"])):
        errors.append(f"meta.last_updated '{meta['last_updated']}' does not match YYYY-MM-DD")

    # 6-7. process_model
    processes = pack.get("process_model", {}).get("processes", [])
    if not processes:
        errors.append("process_model.processes is empty")
    proc_ids = set()
    for i, proc in enumerate(processes):
        for field in ["id", "name", "purpose", "phase"]:
            if field not in proc or not proc[field]:
                errors.append(f"process_model.processes[{i}] missing {field}")
        pid = proc.get("id", "")
        if pid and not re.match(r"PR\d{2}$", pid):
            errors.append(f"process_model.processes[{i}].id '{pid}' does not match PR\\d{{2}}")
        if proc.get("phase") not in ("A", "B", "C", "D"):
            errors.append(f"process_model.processes[{i}].phase '{proc.get('phase')}' not in A/B/C/D")
        if pid in proc_ids:
            errors.append(f"Duplicate process id: {pid}")
        proc_ids.add(pid)

    # 8. role_model
    roles = pack.get("role_model", {}).get("roles", [])
    if not roles:
        errors.append("role_model.roles is empty")
    for i, role in enumerate(roles):
        for field in ["id", "name", "description", "processes"]:
            if field not in role:
                errors.append(f"role_model.roles[{i}] missing {field}")

    # 9-10. general_requirements
    reqs = pack.get("general_requirements", {}).get("requirements", [])
    for i, req in enumerate(reqs):
        for field in ["id", "name", "description", "tier_applicability"]:
            if field not in req:
                errors.append(f"general_requirements.requirements[{i}] missing {field}")
        ta = req.get("tier_applicability", {})
        for tier in ["t1", "t2", "t3"]:
            if tier not in ta:
                errors.append(f"general_requirements.requirements[{i}].tier_applicability missing {tier}")

    # 11-12. quality_checks
    checks = pack.get("quality_checks", {}).get("checks", [])
    for i, check in enumerate(checks):
        for field in ["gate", "check", "pass_criteria", "tier"]:
            if field not in check:
                errors.append(f"quality_checks.checks[{i}] missing {field}")
        gate = check.get("gate", "")
        if gate and not re.match(r"G[1-8]$", gate):
            errors.append(f"quality_checks.checks[{i}].gate '{gate}' does not match G[1-8]")

    # 13. terminology
    terms = pack.get("terminology", {}).get("terms", [])
    for i, term in enumerate(terms):
        for field in ["term", "definition"]:
            if field not in term:
                errors.append(f"terminology.terms[{i}] missing {field}")

    # 14-15. best_practices_ref
    mappings = pack.get("best_practices_ref", {}).get("mapping", [])
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(path)))
    for i, m in enumerate(mappings):
        for field in ["framework_concept", "best_practice_path"]:
            if field not in m:
                errors.append(f"best_practices_ref.mapping[{i}] missing {field}")
        bp_path = m.get("best_practice_path", "")
        if bp_path:
            full_path = os.path.join(project_root, bp_path)
            if not os.path.exists(full_path):
                warnings.append(f"best_practices_ref.mapping[{i}].best_practice_path '{bp_path}' not found on disk")

    # Report
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")

    if errors:
        print(f"\nFAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return False
    else:
        print(f"\nPASSED: 0 errors, {len(warnings)} warning(s)")
        print(f"  Processes: {len(processes)}")
        print(f"  Roles: {len(roles)}")
        print(f"  Requirements: {len(reqs)}")
        print(f"  Quality checks: {len(checks)}")
        print(f"  Terms: {len(terms)}")
        print(f"  BP mappings: {len(mappings)}")
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate-pack.py <pack.yaml>")
        sys.exit(1)
    ok = validate_pack(sys.argv[1])
    sys.exit(0 if ok else 1)
