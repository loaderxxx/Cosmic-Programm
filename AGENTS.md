# MANDATORY FIRST STEP — EN / RU / AR RESEARCH

**Before any research task:** open linked English, Russian and Arabic research records in the same work cycle. **English is authoritative in `main`; Russian is maintained in `lang/ru`; Arabic is maintained in `lang/ar`.** Research and verification begin across all three languages, not as optional post-hoc translation. Track the same research ID, sources, facts, estimates and uncertainties in each edition. Missing or unreviewed language work must be marked `PENDING` / `TRANSLATION_REVIEW`, never presented as complete. See [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md).

---

# AI TEAM BOOTSTRAP

This repository participates in the owner's GitHub-based AI collaboration system.

Before material work:
1. Read `collaboration/AI_TEAM_PROTOCOL.md`.
2. Read `collaboration/AGENT_STATE.md`.
3. Read repository README, manifest and existing agent instructions.
4. Check `main`, `agent/cursor`, and `agent/chatgpt`.
5. Inspect related Issues/PRs.

Roles:
- Cursor = Lead Engineering Agent.
- ChatGPT/JARVIS = Systems Architect / Chief of Staff.
- Human owner = final authority for strategic and irreversible actions.

Canonical branch: `main`.
Working lanes: `agent/cursor`, `agent/chatgpt`.
Use `work/<agent>/<task-id>-<slug>` for substantial isolated tasks.

Required loop:
FETCH → READ → PLAN → CHANGE → TEST → COMMIT → PUSH → PR/ISSUE → REVIEW → MERGE → FETCH

Do not silently overwrite material changes. Do not push directly to `main` except explicit owner-authorized bootstrap/admin work.
Use Issues for handoffs and PRs for integration/review.
Never commit secrets or prohibited private data.

Before completion, verify changed files/tests/refs and record the result in the Issue/PR.
