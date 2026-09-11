#!/usr/bin/env python3
"""Validate blazium-subagents against mapping.yaml + mapping.d and the skills marketplace."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "mapping.yaml"
MAPPING_D = ROOT / "mapping.d"
AGENTS = ROOT / "agents"
DEFAULT_MARKET_URL = (
    "https://raw.githubusercontent.com/blazium-games/blazium-skills"
    "/main/.claude-plugin/marketplace.json"
)
FRONT = re.compile(r"^---\s*\n(.*?)\n---", re.S)
BANNED = re.compile(
    r"\b(Unity|Unreal|Godot 4\.7|town-sdk|DDDBrowser|Shader Graph)\b",
    re.I,
)


def load_mapping() -> dict:
    data = yaml.safe_load(MAPPING.read_text(encoding="utf-8"))
    if MAPPING_D.is_dir():
        for extra in sorted(MAPPING_D.glob("*.yaml")):
            chunk = yaml.safe_load(extra.read_text(encoding="utf-8")) or {}
            data.setdefault("agents", {}).update(chunk.get("agents") or {})
    return data


def published_skills(catalog: object) -> set[str]:
    names: set[str] = set()
    if not isinstance(catalog, dict):
        return names
    for plugin in catalog.get("plugins") or []:
        for rel in plugin.get("skills") or []:
            names.add(Path(rel).name)
    return names


def _load_json_file(path: Path) -> object | None:
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _load_json_url(url: str) -> object | None:
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        return None


def resolve_marketplace(data: dict) -> tuple[str, object | None]:
    """Env path/URL, then local mapping path, then published catalog on main."""
    candidates: list[str] = []
    env = (os.environ.get("BLAZIUM_SKILLS_MARKETPLACE") or "").strip()
    if env:
        candidates.append(env)
    mapped = (data.get("marketplace") or "").strip()
    if mapped:
        candidates.append(mapped)
    sibling = ROOT.parent / "blazium-skills" / ".claude-plugin" / "marketplace.json"
    candidates.append(str(sibling))
    url = (data.get("marketplace_url") or DEFAULT_MARKET_URL).strip()
    if url:
        candidates.append(url)

    seen: set[str] = set()
    for raw in candidates:
        if not raw or raw in seen:
            continue
        seen.add(raw)
        if raw.startswith("http://") or raw.startswith("https://"):
            catalog = _load_json_url(raw)
            if catalog is not None:
                return raw, catalog
            continue
        path = Path(raw)
        if not path.is_absolute():
            path = (ROOT / path).resolve()
        catalog = _load_json_file(path)
        if catalog is not None:
            return str(path), catalog
    return "", None


def main() -> int:
    data = load_mapping()
    expected = set(data["agents"])
    errors: list[str] = []
    files = {p.stem for p in AGENTS.glob("*.md")}
    missing = sorted(expected - files)
    extra = sorted(files - expected)
    if missing:
        errors.append(f"missing agent files: {missing}")
    if extra:
        errors.append(f"extra agent files: {extra}")

    source, catalog = resolve_marketplace(data)
    if catalog is None:
        errors.append(
            "missing skills marketplace (set BLAZIUM_SKILLS_MARKETPLACE "
            "to a path or https URL, or clone blazium-skills next to this repo)"
        )
        published: set[str] = set()
    else:
        published = published_skills(catalog)

    withdrawn = set(data.get("withdrawn") or [])
    retired = set(data.get("retired") or [])
    unassigned = set(data.get("unassigned") or [])
    studio = [n for n, s in data["agents"].items() if s.get("seat") == "studio"]
    blazium = [n for n, s in data["agents"].items() if s.get("seat") == "blazium"]
    orch = [n for n, s in data["agents"].items() if s.get("seat") == "orchestrator"]
    ops = [n for n, s in data["agents"].items() if s.get("seat") == "ops"]
    if len(studio) != 34:
        errors.append(f"expected 34 studio seats, got {len(studio)}")
    if len(blazium) != 15:
        errors.append(f"expected 15 blazium seats, got {len(blazium)}")
    if orch != ["blazium-orchestrator"]:
        errors.append(f"orchestrator seats: {orch}")
    if ops != ["blazium-ci-watcher"]:
        errors.append(f"ops seats: {ops}")
    if "blazium-orchestrator" not in expected:
        errors.append("mapping missing blazium-orchestrator")

    for name, spec in data["agents"].items():
        path = AGENTS / f"{name}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if BANNED.search(text) and "Do not use Unity, Unreal" not in text and "Do not apply Godot 4.7" not in text:
            for match in BANNED.finditer(text):
                snippet = text[max(0, match.start() - 40) : match.end() + 40]
                if re.search(r"do not|no |not apply|not use|not clone", snippet, re.I):
                    continue
                errors.append(f"{name}: banned product {match.group(0)!r}")
                break
        for skill in spec.get("skills") or []:
            if skill in withdrawn or skill in retired:
                errors.append(f"{name} lists withdrawn/retired skill {skill}")
            elif published and skill not in published:
                errors.append(f"{name} lists unpublished skill {skill}")
        block = FRONT.search(text)
        if not block:
            errors.append(f"{name}: missing YAML frontmatter")
        elif f"name: {name}" not in block.group(1):
            errors.append(f"{name}: frontmatter name mismatch")

    working = expected - {"blazium-orchestrator"}
    if len(working) != 50:
        errors.append(f"expected 50 working agents (49 studio/engine + ci-watcher), got {len(working)}")

    assigned: set[str] = set()
    for spec in data["agents"].values():
        assigned.update(spec.get("skills") or [])
    if published:
        missing_assign = sorted(
            skill
            for skill in published
            if skill not in withdrawn
            and skill not in retired
            and skill not in unassigned
            and skill not in assigned
        )
        if missing_assign:
            errors.append(f"published skills not assigned to any agent: {missing_assign}")
        extra_unassigned = sorted(unassigned - published)
        if extra_unassigned:
            errors.append(f"unassigned allow-list not in marketplace: {extra_unassigned}")

    if errors:
        for item in errors:
            print(item, file=sys.stderr)
        print(f"{len(errors)} agent validation error(s)", file=sys.stderr)
        return 1
    print(
        f"validated {len(expected)} agents "
        f"({len(studio)} studio, {len(blazium)} blazium, {len(orch)} orchestrator, {len(ops)} ops)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
