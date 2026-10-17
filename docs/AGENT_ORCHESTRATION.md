# Multi-agent orchestration design

This is an **implementable task contract**, not proof of a 24/7 remotely provisioned agent.

```text
MAIN / PUBLISHER
  └── ORCHESTRATOR (queue, dependencies, status)
        ├── SKILLS (tool routing and permission checks)
        ├── RESEARCH (official guideline + R1 + X1 verification)
        ├── SYNTHESIS (one point, X1 PICOT, evidence exceptions)
        └── PRODUCTION (draft HTML + PPTX)
        └── HUMAN CLINICIAN APPROVAL
             └── ORCHESTRATOR INDEX → MAIN COMMIT
```

## Work item key
`OMM-W{01..26}-{subtopic_slug}`. Fields: topic, source refs, source_verified, r1, x1, picot, reviewer, status, output_file, provenance.

## Completion
Never interpret 26 placeholder headings, an empty registry or draft review URLs as finished clinical content. Report both completed and blocked items. Commit drafts as drafts, reviewed evidence only after clinician approval.

## Security
Minimum GitHub permission, no secrets in git, no external transmission of patient data, and human confirmation for potentially irreversible actions outside current repository scope.
