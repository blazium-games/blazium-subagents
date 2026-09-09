# Blazium Subagents

A Blazium-only studio roster. **49 working studio/engine agents** plus a
routing **orchestrator** and **`blazium-ci-watcher`**.

[GETTING-STARTED.md](GETTING-STARTED.md) · [CONTRIBUTING.md](CONTRIBUTING.md) · [AGENTS.md](AGENTS.md)

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. GDScript-first. Skills live in
[blazium-skills](https://github.com/blazium-games/blazium-skills). Do not apply
Godot 4.7-only APIs. Do not use Unity or Unreal.

## Install

Copy or link `agents/` into a game repo:

```text
.claude/agents/   ← Claude Code
.cursor/agents/   ← Cursor
.codex/agents/    ← Codex
.agents/agents/   ← Codex (plugins layout)
```

From this repository:

```bash
python scripts/install_links.py
python scripts/validate_agents.py
```

Install [blazium-skills](https://github.com/blazium-games/blazium-skills) as a
marketplace so listed `skills:` resolve.

## How it works

1. Start with `blazium-orchestrator` (or `/start`).
2. Orchestrator reads `blazium-router` and picks design / prototype / development.
3. `producer` spawns at most two more specialists in development mode.
4. Each agent opens only the `blazium-*` skills in its frontmatter.

Never mix editor MCP **6506**, game MCP **6507**, remote_control **6508**, Hub **39218**, and Games cloud.

## Roster

See [AGENTS.md](AGENTS.md) and [mapping.yaml](mapping.yaml).

Studio seats use common production titles (`producer`, `gameplay-programmer`, …).
Engine seats are Blazium specialists (`blazium-mcp-specialist`, `blazium-luau-specialist`, …).

## Thin commands (Claude Code)

| Skill | Role |
|-------|------|
| `/start` | Run the orchestrator |
| `/help` | Print the roster |
| `/setup-blazium` | Pin engine=`blazium` 0.6.x |
