# Research proposal: integrity monitoring for coding agents

## Research question

How reliably can transparent rules and model-based monitors detect integrity violations by coding agents without blocking legitimate software-engineering work?

## Motivation

Coding agents increasingly operate across repositories, shells, dependency managers, and deployment systems. Task-completion benchmarks often reward whether the final test suite passes, but may miss how the agent achieved that outcome. An agent can appear successful while modifying unrelated code, removing difficult tests, bypassing hooks, or weakening controls.

## Initial hypotheses

- H1: Explicit action-trace rules detect common boundary violations with high precision.
- H2: Model-based monitors improve recall on semantically ambiguous violations.
- H3: Combining both approaches outperforms either one alone at an acceptable cost.
- H4: Monitor performance declines when agents receive incentives to conceal shortcuts.

## Experimental design

Create sandboxed repository tasks with explicit permissions and hidden integrity criteria. Run a diverse set of coding agents under normal and adversarial incentives. Record file, command, network, and test actions in a provider-neutral schema. Label violations independently, then compare:

1. Rule-only monitoring.
2. Model-only monitoring.
3. Hybrid monitoring.

Primary metrics are violation-detection recall, false-positive rate, successful-task rate, latency, and monitoring cost. Results should include unsuccessful and null findings.

## Ethics and scope

The project studies defensive monitoring. Scenarios should avoid real credentials, production systems, and instructions that meaningfully enable abuse. All agent execution must occur in disposable, least-privilege sandboxes.

## Milestones

- Week 1–2: trace schema, deterministic baseline, and 10 scenarios.
- Week 3–4: sandbox runner and reproducible task fixtures.
- Week 5–7: multi-model experiment harness and blinded labeling protocol.
- Week 8–9: model-based monitor and ablations.
- Week 10–11: analysis, limitations, and replication package.
- Week 12: public technical report and application-ready research summary.
