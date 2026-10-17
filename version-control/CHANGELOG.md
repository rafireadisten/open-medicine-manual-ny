# OMM-NY Development Changelog

Project: **Open Medicine Manual NY (OMM-NY)**  
Canonical path: `version-control/CHANGELOG.md`  
Updated: 2026-10-16  
Purpose: Milestone-oriented record of **project decisions, chat-requested deliverables, actual repository changes, and remaining work**.

Status legend: **MERGED** = verified on GitHub `main`; **DESIGNED** = specified in chat or draft artifacts; **GENERATED** = deliverable created in chat, not necessarily published; **PENDING** = outstanding; **MONITORING** = scheduled completion check, not remote agent execution. A source proposal is not approved clinical evidence. Dates reflect conversations or verified Git commits rather than claims about work performed asynchronously.

## Milestone 01 — Course conception and training model (2026-10-01) — DESIGNED
- Initiated **Agentic Devpd PCP Med Staff Training Course**, a 26-week Internal Medicine Review Course, one session/week.
- Set approximate clinical relevance weighting: 75% outpatient / 25% inpatient.
- Prioritized critical organ systems; retained adult internal medicine, basic OB/GYN and surgical principles.
- Requested subtopic focus lists, curriculum outline, developer-oriented README/schema, flow diagram, and eventual GitHub/Codex support.
- Requested reference documents aligned to *individual subtopics*, not just weekly themes.
- Established civilian **L1–L4** reference hierarchy and separate, matching **VA/DoD** guidelines; design intent reflects approximately 90% civilian / 10% former VA/DoD affiliated clinical population.
- Asked for an agent to keep the reference map versioned/current and for supporting project graphics/charts and GitHub publication.
- Status: foundational instructions incorporated; exhaustive verified subtopic-reference matrix PENDING.

## Milestone 02 — Standalone manual project and naming (2026-10-11 to 2026-10-14) — DESIGNED
- Proposed separate project **NY Medical Open Manual**, distinct from Agent PCP Office and other clinical projects, while incorporating the preexisting course.
- Finalized canonical name **Open Medicine Manual NY (OMM-NY)**.
- Requested initial GitHub directory check and repository generation.
- Defined modular areas: curriculum, clinical reference, clinical protocols, civilian L1–L4 guidelines, VA/DoD guidelines, research, graphics, version control.
- Generated downloadable scaffold archives in the chat; archive creation is not the same as publication to GitHub.
- Status: repository later created privately; comprehensive local archive parity with remote repo not established.

## Milestone 03 — Clinical evidence extraction model (2026-10-14) — DESIGNED / PARTIALLY MERGED
- Required **exactly one fundamental clinically consequential guidance highlight** for each selected reference document.
- Required **X1**, one directly relevant supporting *primary* study when defensible; note exceptions transparently rather than invent evidence.
- Required structured **PICOT**: Population, Intervention/exposure, Comparator, Outcomes (including quantitative effects, uncertainty, safety), and Time.
- Required unique reference IDs, official document links, precise location of recommendation, evidence strength where available, study DOI/URL, extraction/verification states, and clinician sign-off.
- Added reference registry schema, workflow documentation, agent instructions and progress tracking to GitHub in milestone 05.
- Status: workflow schema MERGED; source-level study extraction and approved PICOT entries PENDING.

## Milestone 04 — Remote MCP agent governance and completion reporting (2026-10-14) — DESIGNED / MONITORING
- Requested bounded MCP-assisted completion under the project scope, task boundaries, and OpenAI safety policies.
- Set rules: do not change unrelated repositories; do not fabricate data or claim clinical approval; avoid PHI; use auditable source links and human review.
- Requested report to the human in the ChatGPT window when the actual task is complete.
- Agent policy/task and progress documents were generated in chat archives; verify individual deployment before claiming they are on remote main.
- A daily **OMM-NY Completion Watch** was created to check GitHub and notify only when a non-empty approved inventory, fundamental guidance, X1/PICOT evidence, validation, and human signoff are confirmed.
- Status: watch MONITORING; it is **not** a remotely running research agent. Independent remote agent provisioning remains PENDING.

## Milestone 05 — GitHub setup, initial curriculum publication (2026-10-14) — MERGED
- Private repository created: `rafireadisten/open-medicine-manual-ny`; main is the active branch.
- `1e8f3fc`: initial repository commit.
- `79b134a`: GitHub Actions Jekyll GitHub Pages workflow added (configuration does not itself prove public site deployment).
- `5c0581d`: README updated to describe scope and evidence/agent policies.
- `d33b913`: published 26-week draft curriculum map, individual week outline files, empty `research/reference_registry.csv` schema, companion registry README, and reference X1/PICOT agent instructions.
- The authoritative curriculum table is `internal-medicine-course/curriculum/26-week-map.csv`; 26 weekly files are draft outlines, **not** finished lessons.
- Evidence registry started as headers only: zero populated/approved study records. Existing repository changelog recorded this stage as **0.4.0**.
- Status: repository and scaffolds MERGED; completed lessons and validated evidence PENDING.

## Milestone 06 — Project-history consolidation and graphic development-status map (2026-10-14 to 2026-10-15) — GENERATED
- Requested relevant account/project conversations be consolidated into current working history: course design, naming, reference hierarchy, MCP governance, GitHub and X1/PICOT.
- Requested a graphic status map of curriculum development.
- Generated conceptual dashboard graphics; their displayed completion percentages are **illustrative**, not audited measures.
- Status: chat-level synthesis/graphics GENERATED; no GitHub graphics publication independently verified for this milestone.

## Milestone 07 — Initial open-access article proposals (2026-10-15) — GENERATED / SUPERSEDED
- Requested freely readable reference article proposals and human-readable TXT plus machine-readable CSV, JSON and XLSX for future web application integration.
- Initial set of 14 candidates included guideline/article links but did **not** cover the real 26-week plan adequately; some week assignments were incorrect.
- User explicitly rejected insufficient curriculum complementarity.
- Status: first proposal set preserved as **historical**, not a validated or current map; superseded by the revised aligned dataset.

## Milestone 08 — 26-week and subtopic-oriented reference reconciliation (2026-10-15) — GENERATED / MERGED
- Reconciled against actual GitHub 26-week curriculum: cardiovascular weeks 1–2; pulmonary 3–4; endocrine 5–6; renal 7–8; GI 9–10; ID 11–12; neuro 13–14; hematology 15; oncology 16; rheumatology 17; MSK 18; psychiatry 19; geriatrics 20; prevention 21; dermatology/ENT/ophthalmology 22; OB/GYN 23; surgical/perioperative 24; hospital/critical care 25; clinical integration 26.
- Created a proposed 78-slot three-subtopics-per-week mapping and 26 weekly reference anchors; sources included some broad guideline portals requiring document-level verification.
- Preserved standalone civilian L1–L4 and VA/DoD track requirement.
- Created TXT, CSV, JSON, XLSX editorial artifacts locally.
- Status: CSV/JSON/TXT MERGED in milestone 10; not proof of comprehensive subtopic-level clinical coverage; XLSX not included in that commit.

## Milestone 09 — Complementary open-access medical review tier (2026-10-15) — GENERATED / MERGED
- Requested **R1** companion full-text medical reviews for each curriculum section alongside primary guidance and X1 evidence.
- Proposed 26 weekly review anchors (typically PubMed Central URLs) cross-linked to guideline sources and subtopics.
- Explicitly identified content gaps: thyroid/adrenal, pulmonary embolism, AKI, acid-base, pancreatitis, seizures, thrombosis, anxiety/substance use, ENT, ophthalmology, basic obstetrics.
- Open access/full text, correct article-title matching, currentness and reuse rights require **document-level re-verification**; review articles do not substitute for X1 primary trials.
- Created machine-readable and editorial TXT/CSV/JSON/XLSX outputs.
- Status: TXT/CSV/JSON MERGED in milestone 10; final verification and XLSX publication PENDING.

## Milestone 10 — Publication of 2026-10-15 reference work (committed 2026-10-16 UTC) — MERGED
- Git commit `9348a0855c90536c01ed0db2d7ad1badce96466f` published **10 files** under `research/proposals/2026-10-15/` to `main`:
  - original open-access proposals TXT/CSV/JSON;
  - corrected curriculum-aligned proposals TXT/CSV/JSON;
  - integrated review proposals TXT/CSV/JSON;
  - directory README with verification limitations.
- Preserved `research/reference_registry.csv` (clinical approvals schema) unchanged; proposals deliberately kept outside the approved evidence registry.
- GitHub head and proposal README were verified after push.
- Status: published proposal datasets MERGED; 26-week complete evidence-review pipeline PENDING.

## Milestone 11 — Development governance / paradigm documentation (2026-10-16) — DESIGNED
- User requested a general GitHub file to capture development-workflow changes and *paradigm* changes.
- Recommended `CHANGELOG.md` (what changed), `ROADMAP.md` (future priorities), and decision records/ADRs (why important architectural or methodology choices were made); also `ARCHITECTURE.md`, `AGENTS.md`, and `CONTRIBUTING.md`.
- Verified existing repository includes `version-control/CHANGELOG.md`; the proposed other top-level governance documents were not present under those names.
- **This revision** expands the existing changelog with the full documented sequence; no other governance files are silently claimed as published.
- Status: changelog update MERGED only after this commit successfully lands.

## Development paradigm progression
1. **Training course** → a 26-week primary-care-focused physician education curriculum.
2. **Standalone open manual** → a separately governed, version-controlled OMM-NY project.
3. **Tiered references** → distinct civilian L1–L4 and VA/DoD guideline tracks.
4. **Evidence traceability** → one guidance highlight → one X1 primary study → PICOT + clinical approval.
5. **Research assistance** → bounded MCP agent specification with human signoff, not autonomous clinical authority.
6. **Curriculum alignment** → weekly and finer subtopic mappings instead of an unspecific guideline list.
7. **Educational complement** → R1 open-access medical review beside primary guidelines.
8. **Web-app readiness** → stable identifiers and structured CSV/JSON alongside readable TXT.
9. **Governance** → explicit status distinctions, change history and recommended ADR architecture.

## Current audit snapshot (2026-10-16)
- **MERGED**: GitHub repo, 26-week draft curriculum, evidence registry *schema*, reference-extraction instructions, and Oct 15 proposal CSV/JSON/TXT sets.
- **GENERATED, not confirmed merged**: standalone XLSX artifacts, conceptual graphics, complete packaged local scaffolds.
- **MONITORING**: conditional ChatGPT completion watch; no guarantee of independently running agent.
- **PENDING**: verified official source inventory with direct document links and access/license checks; complete subtopic L1–L4 + separate VA/DoD matching; R1 validation; X1 selection and quantitative PICOT cards; clinical reviewer signoff; remote MCP execution; web application; release-level quality assurance.
- No percentages of clinical completion should be asserted without validated denominators and source evidence.

## Repository links and audit trail
- Repository: https://github.com/rafireadisten/open-medicine-manual-ny
- Curriculum and evidence registry commit: https://github.com/rafireadisten/open-medicine-manual-ny/commit/d33b91381145f3188418d0399c1a81ec4c5a87b0
- Proposal publication commit: https://github.com/rafireadisten/open-medicine-manual-ny/commit/9348a0855c90536c01ed0db2d7ad1badce96466f
- Proposed references: https://github.com/rafireadisten/open-medicine-manual-ny/tree/main/research/proposals/2026-10-15

## Milestone 12 — Orchestrated agent implementation and draft production (2026-10-16) — MERGED DESIGN / NOT RUNNING
- Implemented explicit orchestrator, skills routing, research, synthesis, production and main publisher roles with human clinical gate in AGENTS.md and agents/*.md.
- Added `research/agent_queue.json` as a deliberately unpopulated, non-complete task queue and `docs/AGENT_ORCHESTRATION.md` for dependencies, states and guardrails.
- Added `docs/draft_curriculum_dashboard.html` as an HTML rough draft and generated a six-slide PPTX rough draft in the ChatGPT artifact workspace; binary PowerPoint remote publication requires separate verification.
- Added `ROADMAP.md` for outstanding verification, X1/PICOT, human approval, indexing and actual runner deployment.
- **Execution truth:** documented tasks and GitHub scaffolding are not a continuously running remote agent. The Orchestrator may index only reviewed subtopics; the publishing role must never declare completion from draft data.
