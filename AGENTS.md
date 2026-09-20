# AI TEAM BOOTSTRAP

This repository participates in the owner's GitHub-based AI collaboration system.

## First actions for an AI agent

1. Read `collaboration/AI_TEAM_PROTOCOL.md`.
2. Read `collaboration/AGENT_STATE.md`.
3. Read the repository's own README / manifest / agent instructions.
4. Check current `main`, `agent/cursor`, and `agent/chatgpt` refs.
5. Inspect open Issues/PRs relevant to the task before changing shared material.

## Roles

- Cursor = Lead Engineering Agent: implementation, code, tests, refactoring, integration and runtime verification.
- ChatGPT/JARVIS = Systems Architect / Chief of Staff: architecture, requirements, research, decomposition, cross-project coordination, review and durable knowledge.
- Human owner = final authority for strategic, legal, financial, public, destructive and irreversible decisions.

## Branch invariant

`main` is the canonical integrated state.
Do not use `main` as an agent work branch.
Use `agent/cursor` for Cursor and `agent/chatgpt` for ChatGPT.
Use `work/<agent>/<task-id>-<slug>` for substantial isolated work.

## Required loop

FETCH → READ → PLAN → CHANGE → TEST → COMMIT → PUSH → PR/ISSUE → REVIEW → MERGE → FETCH

Do not silently overwrite another agent's work. Do not force-push shared canonical history.

## Communication

Important cross-agent coordination must be recoverable from GitHub Issues, PRs, review comments, commits and coordination files.

## Security

Never commit credentials, tokens, passwords, secrets or prohibited private data. Follow this repository's privacy and publication rules before copying information across repositories.

## Completion

Before declaring a task done, verify the changed files, tests/checks and resulting Git refs, then update the relevant issue/PR and durable documentation.
