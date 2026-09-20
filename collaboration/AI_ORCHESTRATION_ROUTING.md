# AI ORCHESTRATION AND COST-AWARE ROUTING

## Orchestrator

When this repository is operated through Claude Code/Fable, the Fable-level session is the orchestration and judgment layer.

Fable should:
- understand the whole migration/task;
- decompose it into independent subtasks;
- decide sequencing and dependencies;
- create/launch specialized worker agents where useful;
- route routine/mechanical work to cheaper capable models;
- keep architecture, security, conflict resolution and final verification at the strongest available reasoning layer;
- collect worker results and integrate them into the GitHub workflow.

The orchestrator should not do expensive bulk work inline when a cheaper capable worker can perform it reliably.

## Default routing

1. **Fable / frontier session**
   - system orientation;
   - architecture and decomposition;
   - task routing;
   - conflict decisions;
   - final synthesis;
   - final verification.

2. **Grok worker lane**
   - preferred cost-efficient general implementation/research worker;
   - use the latest available Grok model;
   - as of 2026-09, xAI documentation identifies `grok-4.6` as the current generation;
   - use the strongest available Grok configuration needed for the assigned task, while keeping the task narrowly scoped.

3. **Cheaper/basic workers**
   - file discovery;
   - grep/search;
   - formatting;
   - deterministic transformations;
   - simple extraction;
   - repetitive mechanical edits.

## Escalation

Cheap does not mean trusted by default.

Escalate to a stronger worker or back to Fable when:
- requirements are ambiguous;
- the worker output fails tests;
- authentication/concurrency/data migration/security is involved;
- the change is difficult to verify mechanically;
- multiple agents produce conflicting results;
- the worker cannot satisfy acceptance criteria.

Judge output quality, not model price.

## Parallelism

Parallelize independent subtasks when they do not touch the same files/state.
Do not parallelize conflicting writes to the same important files.
Each worker receives only the minimum context required.

## GitHub integration

Every material worker result must become recoverable through GitHub:
- branch and commit;
- Issue/PR reference;
- verification result;
- files changed;
- unresolved risks/questions.

Workers must not bypass the repository collaboration protocol.

## Migration-specific rule

For the migration task, Fable is the orchestrator:
- split migration into auditable subtasks;
- delegate routine discovery/conversion/file preparation to cheaper workers;
- prefer latest capable Grok workers for general implementation/execution where cost-effective;
- keep canonical Git changes, merge decisions, conflict resolution and final verification under the collaboration protocol;
- never declare migration complete from a worker's claim alone.

## Provider independence

Routing is a policy, not a hard dependency.
If Grok/Fable is unavailable, use another available capable worker and record the fallback.
Do not encode proprietary provider assumptions into the project architecture.
