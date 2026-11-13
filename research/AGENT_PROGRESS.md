# OMM-NY Evidence Agent Progress

Last research batch: 2026-11-12 (bounded ChatGPT-assisted GitHub connector execution, branch `agentic/evidence-batch-02-2026-11-12`).

## Actual status, not provisional completion

- Curriculum: 26 weeks / 78 provisional unit slots; **not** an exhaustive reference-document inventory.
- Reference-document registry: **2 research-stage rows**, not independently clinically validated. The inventory is explicitly **nonexhaustive**.
- Evidence cards: **3 drafts** total (legacy hypertension pilot + 2 new cards); **75 curriculum units not started**.
- New cards: `OMM-W02-S03` atrial fibrillation anticoagulation; `OMM-W07-S02` CKD SGLT2 risk reduction.
- Newly research-checked direct X1-to-guideline associations: **2**, both bounded to the single intervention/trial population; **0 clinically validated evidence associations**.
- New sourced PICOT summaries: **2**, pending independent clinician evaluation. The hypertension pilot's third PICOT remains a candidate with unresolved direct linkage.
- Human clinical approvals: **0**. Indexed-complete curriculum units: **0**.
- Remote persistent autonomous research agent: **not provisioned or running**. This batch used ChatGPT tool calls; a repository Markdown agent specification does not constitute a deployed agent.
- Clinical completion condition: **FAILED / NOT MET**. The signed reviewer evidence required for *every* card is absent.

## Batch-02 sources and audit

1. [Atrial fibrillation card](drafts/OMM-W02-S03.json): [2023 ACC/AHA/ACCP/HRS AF guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11095842/) Section 6.3.1 and [ARISTOTLE original RCT](https://pubmed.ncbi.nlm.nih.gov/21870978/). The class-wide DOAC recommendation is broader than one apixaban RCT.
2. [CKD risk reduction card](drafts/OMM-W07-S02.json): [KDIGO 2024 CKD guideline](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf) Recommendation 3.7.2 and [DAPA-CKD original RCT](https://pubmed.ncbi.nlm.nih.gov/32970396/). DAPA-CKD does not test the entire guideline eGFR/heart-failure population.
3. [Reference registry](reference_registry.csv) and [nonexhaustive inventory manifest](reference_inventory_manifest.json).
4. [Audit validator](../agents/runtime/validate_reference_inventory.py) and [regression tests](../tests/test_reference_inventory.py).

## Next research stage

Continue with one or two nonduplicative, high-yield topic/source pairs per bounded run. First prioritize targeted references for PE, adrenal insufficiency, AKI, seizures and other gaps noted in the orchestrator. Verify direct bibliography linkage and PICOT, log any unresolved evidence exceptions, keep civilian L1-L4 classification distinct from VA/DoD, and request human sign-off rather than assigning it programmatically. Do not merge or publish a draft as clinically complete based on a passing software test.

Daily-account token allowance visibility is not available to the repository process. The per-run work is intentionally capped at 2 new cards to conserve usage. Do not assert a numerical percentage of actual account consumption.
