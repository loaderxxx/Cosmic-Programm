# AI TEAM PROTOCOL

This repository is a shared work surface for the human owner, Cursor and ChatGPT/JARVIS. GitHub Issues, PRs, commits and branches form the recoverable coordination bus.

## Roles
- Cursor — Lead Engineering Agent: implementation, code, tests, refactoring, integration, runtime verification and technical decomposition.
- ChatGPT/JARVIS — Systems Architect / Chief of Staff: architecture, requirements, research, synthesis, coordination, decision records, decomposition and review.
- Human owner — final authority for strategy, legal/financial matters, public disclosure, destructive or irreversible actions.

## Branch model
- `main` — canonical integrated state.
- `agent/cursor` — persistent Cursor lane.
- `agent/chatgpt` — persistent ChatGPT lane.
- `work/<agent>/<task-id>-<slug>` — optional isolated task branch.

Agent branches are working lanes, not canonical truth.

## Work loop
FETCH → READ → PLAN → CHANGE → TEST → COMMIT → PUSH → PR/ISSUE → REVIEW → MERGE → FETCH

Before work: refresh state, read repository instructions/manifests, compare lane to main, inspect related Issues/PRs and define exact scope.
After work: verify, commit, push, update Issue/PR, integrate through PR and refresh after merge.

## Handoffs
Every handoff states objective, context, expected output, acceptance criteria, dependencies, target files/project, recipient, verification and next action.

## Conflicts
Do not overwrite silently. Compare diffs and provenance. Strategic conflicts go to the human owner. Clear implementation conflicts are resolved by Cursor as lead engineer, with provenance preserved.

## Communication
Important coordination must be recoverable from Issues, PRs, review comments, commits and coordination files. Chat history is not canonical coordination state.

## Security
Never commit credentials, tokens, passwords, secrets or prohibited private data. Public repositories must not receive private/proprietary material. Repository-specific privacy, licensing and publication rules always apply.

## Main branch policy
Desired enforcement: PR before main merge; relevant checks/review where applicable; no force-push; no deletion. The policy is documented here and must also be enabled/verified in GitHub repository settings.
