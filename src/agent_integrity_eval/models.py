from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

ActionKind = Literal["read", "write", "delete", "command", "network"]


@dataclass(frozen=True)
class Action:
    kind: ActionKind
    target: str
    detail: str = ""

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Action:
        return cls(kind=value["kind"], target=value["target"], detail=value.get("detail", ""))


@dataclass(frozen=True)
class Scenario:
    id: str
    title: str
    task: str
    allowed_paths: tuple[str, ...]
    forbidden_commands: tuple[str, ...] = ()
    protected_paths: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Scenario:
        return cls(
            id=value["id"],
            title=value["title"],
            task=value["task"],
            allowed_paths=tuple(value.get("allowed_paths", [])),
            forbidden_commands=tuple(value.get("forbidden_commands", [])),
            protected_paths=tuple(value.get("protected_paths", [])),
        )


@dataclass(frozen=True)
class Violation:
    rule: str
    severity: Literal["low", "medium", "high", "critical"]
    evidence: str


@dataclass(frozen=True)
class EvaluationResult:
    scenario_id: str
    passed: bool
    integrity_score: int
    violations: tuple[Violation, ...] = field(default_factory=tuple)

    def as_dict(self) -> dict[str, Any]:
        return {
            "scenario_id": self.scenario_id,
            "passed": self.passed,
            "integrity_score": self.integrity_score,
            "violations": [
                {"rule": item.rule, "severity": item.severity, "evidence": item.evidence}
                for item in self.violations
            ],
        }
