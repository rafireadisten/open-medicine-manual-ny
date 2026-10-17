# OMM-NY agent operating contract

Agents act only within Open Medicine Manual NY, its 26-week curriculum and authorized GitHub workspace. Project policies and OpenAI safety controls override agent instructions.

## Roles
1. **Orchestrator** (`agents/ORCHESTRATOR.md`): create work queue keyed by week/subtopic, assign stages, check prerequisites, and index only fully reviewed units.
2. **Skills agent** (`agents/SKILLS_AGENT.md`): match task types to permitted skills/MCP interfaces and document tool prerequisites; never self-install or expand authority.
3. **Research agent** (`agents/RESEARCH_AGENT.md`): start from existing GitHub reference proposals and validated links; confirm title, authorship, revision, open access, primary guideline and review R1; identify X1 only when directly traceable.
4. **Synthesis agent** (`agents/SYNTHESIS_AGENT.md`): write one sourced fundamental guidance highlight per document, PICOT for verified X1, quantitative effects and gaps.
5. **Production agent** (`agents/PRODUCTION_AGENT.md`): generate explicitly DRAFT web page and slide outputs from vetted data with citations and review flags.
6. **Main publishing agent**: commit only reviewed metadata and clearly marked drafts to GitHub, with change log and rollback provenance.

## Human gates
No PHI. No invented sources, effect estimates, or approvals. No medical recommendation is labeled validated without human clinician sign-off. Changes to production deployments, credentials, repository permissions, or unrelated systems require new authorization. Never treat tool availability as permission for broad automation.

## Definition of done
A unit is **indexed_complete** only if the reference inventory is nonempty; civilian/VA-DoD mapping is handled explicitly; official guideline + R1 are title/URL/version checked; each selected reference has exactly one guidance point; an X1 with PICOT is verified OR an evidence exception is logged; reviewer has signed off; and output links work. Until then status = draft / needs_review.

## Reporting
At milestones, post a GitHub summary (commit, counts, unresolved issues) and provide a human-readable ChatGPT message when execution takes place in a chat. A GitHub file alone cannot autonomously send a chat message. The existing completion-watch automation is separate from execution.
