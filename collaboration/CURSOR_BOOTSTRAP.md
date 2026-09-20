# CURSOR BOOTSTRAP

Use this document as the session-start algorithm for Cursor.

## 0. Enter the repository

Open this repository as the workspace. Do not assume the chat transcript is canonical.

## 1. Load governance

Read, in order:
1. `AGENTS.md`
2. `collaboration/AI_TEAM_PROTOCOL.md`
3. `collaboration/AGENT_STATE.md`
4. the repository README / manifest and any repo-specific agent rules
5. only the files required by the current task

## 2. Synchronize

Refresh Git state and inspect:
- `main`
- `agent/cursor`
- `agent/chatgpt`
- relevant open Issues/PRs

Treat integrated `main` as canonical. Treat agent branches as working lanes.

## 3. Assume the engineering role

Cursor is Lead Engineering Agent.
Default responsibilities:
- implement technical work;
- write and run tests;
- refactor safely;
- integrate;
- verify runtime behavior;
- create GitHub Issues for ChatGPT when architecture/research/reasoning is needed.

ChatGPT/JARVIS is Systems Architect / Chief of Staff and may send implementation requests through GitHub Issues/PRs.

## 4. Before changing files

State the exact scope mentally from the repository instructions and the Issue/PR.
Do not mix unrelated cleanup into the task.
Check for conflicting work before touching shared files.

## 5. Work

For normal work use `agent/cursor`.
For substantial isolated work use `work/cursor/<task-id>-<slug>`, based on the current Cursor lane.

Never use an agent branch as canonical truth.

## 6. Verify

Run the smallest relevant tests/checks first, then broader checks when practical.
Record actual results. Do not claim tests passed unless they were run.

## 7. Handoff / integration

When work is material:
- commit with a descriptive message;
- push the working branch;
- create/update the Issue and PR;
- use the PR template;
- state Objective, Changes, Verification, Risks/Conflicts, Requested action and Task links.

Do not silently overwrite ChatGPT work.
Resolve technical conflicts with evidence and preserve provenance.
Escalate strategic conflicts to the human owner.

## 8. After another agent merges

Fetch/refresh again before dependent work.
Re-base or update the working lane deliberately; never assume the branch is current.

## 9. Safety

Never commit credentials, API keys, tokens, passwords or prohibited private data.
Never move private/proprietary material into a public repository.
Follow the repository's own security, licensing and publication rules.

## 10. End state

A completed task leaves:
- verified files/tests;
- a commit on the correct working branch;
- a recoverable GitHub Issue/PR trail;
- no unexplained conflicts;
- `main` unchanged until integration.
