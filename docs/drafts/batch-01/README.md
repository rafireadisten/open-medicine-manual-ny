# Batch 01 - publication checkpoint

Checked: 2026-10-17. Scope: the existing OMM-NY hypertension pilot, not the complete curriculum.

**PARTIALLY PUBLISHED / CLINICAL DRAFT.** Source code and text outputs are on GitHub. The PowerPoint and downloadable ZIP package are not published to a branch in this checkpoint.

## Published source and outputs

The underlying batch was published in commit [b2b9eeafe0321a364cc624f7c368f0a0425266da](https://github.com/rafireadisten/open-medicine-manual-ny/commit/b2b9eeafe0321a364cc624f7c368f0a0425266da).

- [Hypertension Markdown draft](hypertension.md)
- [Hypertension HTML source](hypertension.html) - repository source, not a newly deployed live website
- [Draft index](draft_index.json)
- [Structured evidence draft](../../../research/drafts/OMM-W01-S01.json)
- [Normalized curriculum subtopics](../../../research/normalized/curriculum_subtopics.json)
- [Agent queue](../../../research/agent_queue.json)
- [Batch execution report](../../../research/batch_01_report.json)
- [Executable runner and instructions](../../../agents/runtime/README.md)
- [PowerPoint build source](../../../agents/runtime/build_slides.js)
- [Runtime regression tests](../../../tests/test_runtime.py)
- [Execution milestone log](../../../version-control/EXECUTION_LOG.md)

## Binary artifacts not published

The conversation's existing artifacts were inspected locally. The ZIP passed its archive-integrity check; the PPTX inside it passed its ZIP-integrity check and contains nine slide XML files. This check did not rerun clinical research, runtime regression tests, or slide rendering.

| Conversation artifact | Bytes | SHA-256 | Repository publication |
| --- | ---: | --- | --- |
| OMM_NY_Hypertension_Pilot.pptx | 134020 | 833b1cf344b9a975de976e8d9251be03121527cbd9f87c6fc26ccde24abd8fb8 | Not published |
| OMM_NY_Batch01_Execution_Package.zip | 35812 | 35760c4831c394351597b3509da966c9531cb1bcc71fcb8fc73e10c2282bf3f6 | Not published |

An attempted binary transfer was blocked by a tool safety check. This checkpoint does not retry that transfer or attach unverified intermediate blobs to a branch. The source artifact downloads remain in the originating ChatGPT conversation; sandbox links are not GitHub-hosted assets.

## Clinical and execution status

The original report records 26 weeks, 78 provisional subtopic slots, one draft unit, zero clinical approvals, and zero indexed-complete units. The research draft still requires source-linkage verification and clinician review. No independent remote research agent is running according to that report.

This commit adds a navigation and publication-status record only. It does not change clinical content, approvals, workflows, repository permissions, or deployment settings. Historical milestones and proposal files are preserved.
