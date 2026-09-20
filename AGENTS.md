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
