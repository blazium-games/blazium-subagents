# Blazium Subagents

A Blazium-only studio roster. **49 working studio/engine agents** plus a
routing **orchestrator** and **`blazium-ci-watcher`**.

[GETTING-STARTED.md](GETTING-STARTED.md) · [CONTRIBUTING.md](CONTRIBUTING.md) · [AGENTS.md](AGENTS.md) · [GROK.md](GROK.md)

Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. GDScript-first. Skills live in
[blazium-skills](https://github.com/blazium-games/blazium-skills). Do not apply
non-`blazium_4.8` APIs. Do not use Unity or Unreal.

This roster publishes its own semver to [subagents.json](https://cdn.blazium.app/subagents/subagents.json).

## Community

- Official website: [https://blazium.app/](https://blazium.app/)
- IndieDB blog: [https://www.indiedb.com/engines/blazium-engine](https://www.indiedb.com/engines/blazium-engine)
- Official community: [Blazium Discord](https://discord.gg/sZaf9KYzDp)
- Docs: [docs.blazium.app](https://docs.blazium.app)

## Ecosystem

| Product | Role | Release |
|---------|------|---------|
| [CLI](https://github.com/blazium-games/blazium-cli) | Install editors, projects, remote control, Steam/itch deploy | Linux and Windows, x86_64 and x86_32. Catalog: [cli.json](https://cdn.blazium.app/cli/cli.json) |
| [Hub](https://github.com/blazium-games/blazium-hub) | Desktop companion; installers bundle the CLI | Linux and Windows, x86_64 and x86_32. Engine builds track `blazium_4.8` |
| [Crash reporter](https://github.com/blazium-games/blazium_crash_reporter) | Sidecar UI for engine and Hub crash reports | Linux and Windows, x86_64 and x86_32. Catalog: [crash_reporter.json](https://cdn.blazium.app/crash_reporter/crash_reporter.json). Engine builds track `blazium_4.8` |
| [Toolchain](https://github.com/blazium-games/blazium-toolchain) | PS1, PS2, N64, and Interactive DVD | Linux and Windows, x86_64 and x86_32. Catalog: [toolchain.json](https://cdn.blazium.app/toolchain/toolchain.json) |
| [Skills](https://github.com/blazium-games/blazium-skills) | Agent skill packs for Claude, Cursor, Codex, and Grok | Own semver, separate from the 0.8.x API baseline. Catalog: [skills.json](https://cdn.blazium.app/skills/skills.json) |
| [Subagents](https://github.com/blazium-games/blazium-subagents) | Studio roster that loads those skills | Own semver. Catalog: [subagents.json](https://cdn.blazium.app/subagents/subagents.json) |

## Install

```text
npm install @blazium-engine/subagents
```

The package contains `agents/`, this README, and the MIT license. Host zip packs stay on the CDN catalog.

Copy or link `agents/` into a game repo:

```text
.claude/agents/   ← Claude Code
.cursor/agents/   ← Cursor
.codex/agents/    ← Codex
.agents/agents/   ← Codex (plugins layout)
.grok/agents/     ← Grok
```

From this repository:

```bash
python scripts/install_links.py
python scripts/validate_agents.py
```

Install [blazium-skills](https://github.com/blazium-games/blazium-skills) as a
marketplace so listed `skills:` resolve. Grok also auto-reads the Claude
marketplace; see [GROK.md](GROK.md).

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
| `/setup-blazium` | Pin engine=`blazium` 0.8.x |

On Grok, ignore frontmatter `model:` and paste one agent file as the specialist system prompt.
