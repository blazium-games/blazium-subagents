#!/usr/bin/env python3
"""Render agents/*.md from mapping.yaml plus mapping.d/*.yaml shards."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "mapping.yaml"
SHARDS = ROOT / "mapping.d"
TEMPLATE = ROOT / "templates" / "AGENT.template.md"
OUT = ROOT / "agents"


ACRONYMS = {
    "mcp": "MCP",
    "cli": "CLI",
    "ci": "CI",
    "ui": "UI",
    "ux": "UX",
    "qa": "QA",
    "ai": "AI",
    "gdscript": "GDScript",
    "csharp": "C#",
    "luau": "Luau",
}


def pretty_title(name: str) -> str:
    parts = []
    for part in name.split("-"):
        parts.append(ACRONYMS.get(part, part.title()))
    return " ".join(parts)


def fold_description(text: str) -> str:
    lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
    return "\n  ".join(lines)


def load_mapping() -> dict:
    data = yaml.safe_load(MAPPING.read_text(encoding="utf-8"))
    agents = dict(data.get("agents") or {})
    if SHARDS.is_dir():
        for shard in sorted(SHARDS.glob("*.yaml")):
            extra = yaml.safe_load(shard.read_text(encoding="utf-8")) or {}
            agents.update(extra.get("agents") or extra)
    data["agents"] = agents
    return data


def main() -> int:
    data = load_mapping()
    template = TEMPLATE.read_text(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    for name, spec in data["agents"].items():
        skills = spec["skills"]
        skills_csv = ", ".join(skills)
        skills_list = "\n".join(f"- `{s}`" for s in skills)
        title = pretty_title(name)
        extras = (spec.get("extras") or "").strip()
        body = template.format(
            name=name,
            description=fold_description(spec["description"]),
            model=spec["model"],
            max_turns=spec["max_turns"],
            skills_csv=skills_csv,
            title=title,
            role=spec["role"].strip(),
            skills_list=skills_list,
            when_not=spec["when_not"].strip(),
            handoff=spec["handoff"].strip(),
            extras=extras,
        )
        (OUT / f"{name}.md").write_text(body, encoding="utf-8", newline="\n")
    print(f"wrote {len(data['agents'])} agents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
