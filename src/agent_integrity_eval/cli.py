from __future__ import annotations

import argparse
import json
from pathlib import Path

from .evaluator import evaluate_trace
from .io import load_scenario, load_trace


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate an AI agent action trace")
    parser.add_argument("scenario", type=Path)
    parser.add_argument("trace", type=Path)
    args = parser.parse_args()
    result = evaluate_trace(load_scenario(args.scenario), load_trace(args.trace))
    print(json.dumps(result.as_dict(), indent=2))
    raise SystemExit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
