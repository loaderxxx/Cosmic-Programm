# AI TEAM PROTOCOL

## Purpose

This repository is a shared work surface for the human owner, Cursor and ChatGPT/JARVIS.
GitHub Issues, PRs, commits and branches are the recoverable coordination bus.

## Roles

### Cursor — Lead Engineering Agent
Owns day-to-day technical execution: implementation, code, tests, refactoring, integration, local/runtime verification and technical task decomposition.

### ChatGPT / JARVIS — Systems Architect / Chief of Staff
Owns architecture reasoning, requirements, research, synthesis, cross-project coordination, decision records, task decomposition, verification/review and durable knowledge capture.

### Human owner
Final authority for strategy, legal/financial matters, public disclosure, destructive or irreversible actions and material long-term architecture choices.

## Branch model

- `main` — canonical integrated state.
- `agent/cursor` — persistent Cursor lane.
- `agent/chatgpt` — persistent ChatGPT lane.
- `work/<agent>/<task-id>-<slug>` — optional short-lived isolated task branch.

Agent branches are working lanes, not canonical truth.

## Synchronization

Before material work:

1. fetch/refresh repository state;
2. read manifests and agent instructions;
3. compare the working lane to `main`;
4. inspect related Issues/PRs;
5. define the exact scope.

After material work:

1. test/verify;
2. commit with a descriptive message;
3. push to the agent lane;
4. update the Issue/PR or create one;
5. integrate through PR;
6. refresh from `main` after merge.

Canonical loop:

FETCH → READ → PLAN → CHANGE → TEST → COMMIT → PUSH → PR/ISSUE → REVIEW → MERGE → FETCH

## Handoff protocol

Every agent handoff must state:
- objective;
- context;
- expected output;
- acceptance criteria;
- dependencies;
- target files/project;
- recipient;
- verification;
- next action.

## Conflict protocol

Do not overwrite conflicting work silently.
Compare diffs and provenance.
If the conflict is strategic, escalate to the human owner.
If it is a clear implementation conflict, Cursor resolves it as lead engineer while preserving provenance in the PR.

## Safety / disclosure

No secrets or prohibited personal data in commits.
Do not move private material into a public repository.
Repository-specific privacy, licensing and publication rules always apply.

## Main-branch protection

The intended policy is:
- changes reach `main` through PRs;
- status checks run where available;
- direct pushes and force-pushes to `main` are blocked by repository settings.

The policy is documented here; GitHub enforcement must be verified in repository settings.

## Definition of done

The work is synchronized when the same `main` baseline is known to both agents, in-flight work is visible in Issues/PRs, no material change was silently overwritten, and the resulting state is reproducible from Git history.
