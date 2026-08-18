# Experiment plan

## Phase 1: deterministic baseline

The first release contains ten scenarios covering scope expansion, test suppression, access-control weakening, destructive database operations, secret exposure, and unsafe command execution.

Each scenario separates three concepts:

- Allowed paths: resources the agent may modify.
- Protected paths: sensitive resources that must remain unchanged.
- Forbidden commands: explicit operational shortcuts or destructive actions.

## Phase 2: trace collection

The next implementation milestone will introduce a provider-neutral trace schema and an isolated runner. Each trace will record the action type, target, arguments, timestamp, result, and task context without collecting credentials or production data.

## Phase 3: monitor comparison

The study will compare deterministic, model-based, and hybrid monitors using detection recall, false-positive rate, task completion, latency, and cost. Scenario labels will be reviewed independently before aggregate results are calculated.
