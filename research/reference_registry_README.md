# Reference evidence registry

The CSV is a **schema only**. Zero populated evidence rows means zero reviewed reference documents, not completion.

## Workflow
1. Inventory a real official reference document and unique reference_id; assign one or more week/subtopic mappings.
2. Specify civilian L1-L4 track or separate VA/DoD track; do not merge tracks.
3. Record ONE fundamental guidance point, with precise source section/page and grade/strength when provided.
4. Verify ONE primary study X1 directly supporting that point; record official journal/PubMed/DOI link.
5. Summarize X1 in PICOT and quantitative effects, uncertainty, safety and limitations. For guidelines supported by indirect or multiple studies, flag inability to choose a defensible X1; do not fabricate a direct link.
6. Record source-verified status and submit to human clinical reviewer. Only human signoff permits clinical_approval_status=approved.

## Completion rule
A non-empty explicitly approved source inventory, all documented references mapped to a verified X1 or a documented exception, PICOT analyses completed, schema validation passed, and clinical approvals recorded. An empty CSV is never complete.
