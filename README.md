# Agent Integrity Eval

Agent Integrity Eval is an early-stage, reproducible framework for measuring whether AI coding agents respect operational boundaries while completing software-engineering tasks.

The project starts from a practical safety question: **does an agent complete the requested task without weakening the surrounding system?**

## What it measures

- Changes outside the authorized file scope
- Writes or deletions in protected paths
- Commands that bypass checks or introduce destructive behavior
- An integrity score backed by inspectable evidence

The initial dataset contains ten scenarios covering authentication, CI, dependency updates,
database migrations, APIs, security patches, refactoring, observability, and data access.

## Quick start

```bash
python -m pip install -e '.[dev]'
aie scenarios/fix-parser.json examples/safe-trace.json
aie scenarios/fix-parser.json examples/unsafe-trace.json
```

## Research direction

The current deterministic evaluator establishes a transparent baseline. Planned experiments will:

1. Run multiple coding agents in sandboxed repositories.
2. Capture normalized tool-action traces.
3. Compare rule-based and model-based monitors.
4. Measure detection recall, false-positive rate, task completion, and monitor cost.
5. Publish scenarios, traces, results, and negative findings.

See [the research proposal](docs/research-proposal.md) for hypotheses and experimental design.
The [experiment plan](docs/experiment-plan.md) describes the staged evaluation protocol.

## Status

Version 0.1 is a minimal research scaffold, not a security product. It evaluates recorded traces; it does not yet execute untrusted agents or provide a hardened sandbox.

## Author

Esteban Orrego — software engineer transitioning into empirical AI safety and ML systems research.
