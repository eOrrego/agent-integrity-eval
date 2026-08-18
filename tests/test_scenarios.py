from pathlib import Path

from agent_integrity_eval.io import load_scenario


def test_scenario_catalog_has_ten_unique_entries() -> None:
    paths = sorted(Path("scenarios").glob("*.json"))
    scenarios = [load_scenario(path) for path in paths]

    assert len(scenarios) == 10
    assert len({scenario.id for scenario in scenarios}) == 10


def test_every_scenario_defines_integrity_boundaries() -> None:
    for path in Path("scenarios").glob("*.json"):
        scenario = load_scenario(path)
        assert scenario.allowed_paths, path
        assert scenario.protected_paths, path
        assert scenario.forbidden_commands, path
