# Contributing

Agent Integrity Eval welcomes reproducible scenarios, monitor implementations, and analysis improvements.

## Development

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
```

## Scenario contributions

A useful scenario should define:

- A realistic software-engineering task
- Explicitly allowed paths
- Protected paths or controls
- Actions that constitute integrity violations
- A safe trace and at least one violating trace

Do not include credentials, production targets, or instructions that meaningfully enable abuse.
