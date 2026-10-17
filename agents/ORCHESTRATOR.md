# Orchestrator — task planning and indexing

Input: `internal-medicine-course/curriculum/26-week-map.csv`, weekly outlines, `research/proposals/2026-10-15/`, `research/reference_registry.csv`.

Execution order: discover curriculum → create queue per subtopic → skills validation → research source verification → synthesis evidence card → production drafts → human clinical review → completeness validation → index → publishing agent commit.

State machine: `not_started -> researching -> synthesis_pending -> draft_produced -> clinical_review_pending -> indexed_complete`. Any failed check sends unit to `blocked` with reason. Agent cannot advance `clinical_review_pending` autonomously.

Prioritize current gaps: thyroid/adrenal, pulmonary embolism, AKI, acid-base, pancreatitis, seizures, thrombosis, anxiety/substance use, ENT, ophthalmology and basic obstetrics. Publish aggregate counts without extrapolating a percentage from scaffold files.

Output: `research/agent_queue.json`, `research/AGENT_PROGRESS.md`, and weekly reference indexes (once reviewed).
