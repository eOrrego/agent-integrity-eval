from __future__ import annotations

import json
from pathlib import Path

from .models import Action, Scenario


def load_scenario(path: Path) -> Scenario:
    return Scenario.from_dict(json.loads(path.read_text(encoding="utf-8")))


def load_trace(path: Path) -> list[Action]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Action.from_dict(item) for item in data["actions"]]
