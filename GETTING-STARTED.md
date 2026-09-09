# Getting started — blazium-subagents

A Blazium-only studio roster. **49 working seats** plus `blazium-orchestrator`
and `blazium-ci-watcher`. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

Install [blazium-skills](https://github.com/blazium-games/blazium-skills) first
so listed skills resolve on Claude, Cursor, and Codex.

```bash
# Claude Code
/plugin marketplace add blazium-games/blazium-skills
/plugin install blazium@blazium-skills

# Codex
codex plugin marketplace add blazium-games/blazium-skills
```

Cursor: add `blazium-games/blazium-skills` as a marketplace, then install
`blazium` or a topic pack.

## Install agents

```bash
python scripts/install_links.py
python scripts/validate_agents.py
```

| Host | Agents |
|------|--------|
| Claude Code | `.claude/agents/` |
| Cursor | `.cursor/agents/` |
| Codex | `.codex/agents/` or `.agents/agents/` |

In a game repo, link or copy `agents/` to those paths.

## First session

1. Spawn `blazium-orchestrator` (Claude: `/start`).
2. Pick design / prototype / development.
3. Development mode: `producer` + at most **two** more specialists.
4. Each agent reads only the `blazium-*` skills in its frontmatter.

Thin Claude commands: `/start`, `/help`, `/setup-blazium`.

## Four surfaces (never mix)

| Surface | Default | Owner |
|---------|---------|-------|
| Editor JustAMCP | `:6506/mcp` | `blazium-mcp-specialist` |
| Game JustAMCP | `:6507/mcp` | `blazium-game-mcp-specialist` |
| remote_control | `:6508/v1` | `tools-programmer` / `blazium-cli-remote` |
| Hub remote | `:39218` | `blazium-hub-specialist` |

After a ship push, producer may spawn `blazium-ci-watcher`. Gameplay
evidence uses `blazium-verify`, not a screenshot.

See [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
