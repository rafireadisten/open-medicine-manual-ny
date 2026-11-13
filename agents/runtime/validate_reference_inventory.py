#!/usr/bin/env python3
"""Fail-closed OMM-NY research registry and clinical-completion audit.

Draft validation checks structure and source provenance. A passing draft audit
NEVER indicates clinical approval or full reference-document coverage.
"""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

FIELDS = ("reference_id", "week", "subtopic", "official_url",
          "fundamental_guidance_point", "guidance_quote_location",
          "x1_study_title", "x1_primary_url", "x1_doi", "x1_study_design",
          "picot_population", "picot_intervention", "picot_comparator",
          "picot_outcomes", "picot_time", "x1_effect_size", "x1_uncertainty",
          "x1_limitations", "clinical_approval_status", "source_verified")
PICOT_KEYS = ("P", "I", "C", "O", "T")


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def audit(root):
    registry = root / "research/reference_registry.csv"
    manifest_file = root / "research/reference_inventory_manifest.json"
    queue_file = root / "research/agent_queue.json"
    issues, completion_blockers = [], []
    if not registry.exists():
        return {"draft_schema_valid": False, "completion_eligible": False,
                "errors": ["Reference registry missing"], "completion_blockers": []}
    with registry.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        headers = set(reader.fieldnames or ())
    if not rows:
        issues.append("Empty registry is not completion")
    if not set(FIELDS).issubset(headers):
        issues.append("Required registry columns missing: " +
                      ", ".join(sorted(set(FIELDS) - headers)))
    ids = [r.get("reference_id", "").strip() for r in rows]
    if len(ids) != len(set(ids)):
        issues.append("Duplicate reference_id values")
    card_count = 0
    for row in rows:
        rid = row.get("reference_id", "")
        for field in FIELDS:
            if not (row.get(field) or "").strip():
                issues.append(f"{rid}: missing {field}")
        for link_field in ("official_url", "x1_primary_url"):
            if not (row.get(link_field) or "").startswith("https://"):
                issues.append(f"{rid}: bad {link_field}")
        if row.get("reference_track") not in ("CIVILIAN", "VA/DOD"):
            issues.append(f"{rid}: invalid reference track")
        card_file = root / "research/drafts" / (row.get("audit_file") or "")
        if not row.get("audit_file") or not card_file.is_file():
            issues.append(f"{rid}: missing evidence card")
            continue
        try:
            card = load_json(card_file)
            card_count += 1
            docs = card.get("documents", [])
            sources = {s["id"]: s["url"] for s in card.get("sources", [])}
            study = card.get("x1", {})
            picot = study.get("picot", {})
            if card.get("inventory_reference_id") != rid:
                issues.append(f"{rid}: mismatched evidence card inventory ID")
            if len(docs) != 1:
                issues.append(f"{rid}: expected exactly ONE selected document")
            elif docs[0].get("source_id") not in sources or not docs[0].get("highlight") or not docs[0].get("locator"):
                issues.append(f"{rid}: guidance point/source locator invalid")
            if not docs or not docs[0].get("x1_linkage_status", "").startswith("direct_"):
                issues.append(f"{rid}: X1 direct linkage not documented")
            if study.get("source_id") not in sources or not study.get("doi"):
                issues.append(f"{rid}: study source/DOI missing")
            if study.get("design") != "randomized_controlled_trial":
                issues.append(f"{rid}: study is not the expected primary trial type")
            if not all(isinstance(picot.get(k), str) and picot[k].strip() for k in PICOT_KEYS):
                issues.append(f"{rid}: sourced PICOT fields incomplete")
            if study.get("doi") != row.get("x1_doi"):
                issues.append(f"{rid}: X1 DOI differs from registry")
            if card.get("clinical_approval_status") != row.get("clinical_approval_status"):
                issues.append(f"{rid}: approval status differs from registry")
        except (KeyError, ValueError, TypeError, OSError) as error:
            issues.append(f"{rid}: invalid card: {error}")
    manifest = load_json(manifest_file) if manifest_file.exists() else {}
    if not manifest.get("inventory_complete", False):
        completion_blockers.append("Exhaustive reference-document inventory not certified")
    if not manifest.get("inventory_audit_url"):
        completion_blockers.append("Missing independently checkable inventory audit")
    if manifest.get("expected_total_reference_documents") != len(rows) or not rows:
        completion_blockers.append("Document inventory count not certified or nonempty")
    if set(manifest.get("reference_ids", [])) != set(ids):
        completion_blockers.append("Manifest IDs do not match registry")
    if not manifest.get("curriculum_mapping_reviewed"):
        completion_blockers.append("Full 26-week curriculum coverage/mapping not reviewed")
    if not queue_file.exists():
        completion_blockers.append("Agent queue missing")
    else:
        queue = load_json(queue_file)
        units = queue.get("units", [])
        if not units or any(u.get("complete") is not True for u in units):
            completion_blockers.append("At least one curriculum unit is not complete")
    all_cards = sorted((root / "research/drafts").glob("OMM-W*-S*.json"))
    for path in all_cards:
        card = load_json(path)
        if card.get("clinical_approval_status") != "approved" or not card.get("clinical_reviewer") or not card.get("clinical_review_date"):
            completion_blockers.append(f"{path.name}: human clinical sign-off not documented")
    for row in rows:
        rid = row.get("reference_id", "")
        if row.get("source_verified") != "independently_verified" or row.get("extraction_status") != "validated":
            completion_blockers.append(f"{rid}: independent source/evidence validation incomplete")
        if (row.get("clinical_approval_status") != "approved" or
            not row.get("clinical_reviewer") or not row.get("clinical_review_date") or
            not (row.get("clinical_review_evidence_url") or "").startswith("https://")):
            completion_blockers.append(f"{rid}: documented signed human approval missing")
        if not row.get("reference_tier") or row.get("reference_tier", "").startswith("pending"):
            completion_blockers.append(f"{rid}: reference tier unresolved")
    approved = sum(r.get("clinical_approval_status") == "approved" for r in rows)
    return {
        "reference_documents": len(rows),
        "evidence_cards_linked": card_count,
        "human_approved_registry_documents": approved,
        "draft_schema_valid": not issues,
        "completion_eligible": not issues and not completion_blockers,
        "errors": issues,
        "completion_blockers": sorted(set(completion_blockers)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--completion", action="store_true",
                        help="Exit nonzero unless every clinical completion gate passes")
    args = parser.parse_args()
    result = audit(args.root)
    print(json.dumps(result, indent=2))
    return 0 if (result["completion_eligible"] if args.completion else result["draft_schema_valid"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
