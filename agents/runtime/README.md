# Executable OMM-NY pilot

This is a deterministic, locally executed draft pipeline, not six independent remote agents. ChatGPT performed the source research and authored the input evidence card. The Python program validates and renders that card; it does not autonomously search the literature or synthesize new medical claims.

## Run from the repository root

```
python3 agents/runtime/run_batch.py --root .
python3 -m unittest discover -s tests -v
npm install --prefix agents/runtime
NODE_PATH=agents/runtime/node_modules node agents/runtime/build_slides.js .
```

The only optional dependency is PptxGenJS 4.0.0 for slides. The local QA pass used the installed slide-layout helpers through OMM_SLIDE_HELPERS; that optional path is not required for the standalone production script. Node dependency installation is a user-run prerequisite, not an installation performed in GitHub by this commit.

## Execution evidence

The first batch produced a 78-unit queue covering the 26-week provisional source inventory; one hypertension draft; zero approvals; zero completed clinical units. Ten unit tests passed. A nine-slide PPTX was generated, rendered and passed the overflow check in the chat workspace. The PPTX binary is available in the chat download package; the reproducible generator is in GitHub.

The published queue is a compact status snapshot keyed to research/normalized/curriculum_subtopics.json. The complete 78-item input was recovered from the conversation attachment because the historical GitHub JSON export ends at line 1000 mid-record. Original proposal files were not overwritten. Re-running preserves the draft-only classification. The source inventory is provisional and does not prove exhaustive clinical subtopic coverage.

## Safety and runtime boundary

The attempt to assign issue #1 to a remote coding agent was blocked by an OpenAI tool safety check. It was not retried or routed through another service. No unattended agent, recurring runner, new account, paid API, GitHub Actions workflow or deployment was activated. This source publication does not change that status.

The program makes no network requests, uses no secrets, does not push git, does not edit research/reference_registry.csv, and cannot accept or issue clinical approval. Existing guideline and review proposals remain historical, not verified evidence. It rejects empty inventories, duplicate or mismatched IDs, missing weeks, invalid PICOT and reviews mislabeled as the pilot trial. HTML is escaped. Legacy CSV extraction wrappers are normalized only when recognized, without changing original files.

## Outputs and remaining work

research/agent_queue.json; research/batch_01_report.json; docs/drafts/batch-01/hypertension.html; hypertension.md; draft_index.json; and optionally OMM_NY_Hypertension_Pilot.pptx.

The evidence card lists the remaining source linkage, final SPRINT report, VA/DoD, L1-L4 and human-review gaps. The completion index stays empty. Continue research under the existing project contracts; do not auto-approve these drafts or bypass the remote-assignment safety stop.
