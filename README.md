# Blazium Subagents

A Blazium-only studio roster. **49 working studio/engine agents** plus a
routing **orchestrator** and **`blazium-ci-watcher`**.

[GETTING-STARTED.md](GETTING-STARTED.md) · [CONTRIBUTING.md](CONTRIBUTING.md) · [AGENTS.md](AGENTS.md) · [GROK.md](GROK.md)

Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. GDScript-first. Skills live in
[blazium-skills](https://github.com/blazium-games/blazium-skills). Do not apply
non-`blazium_4.8` APIs. Do not use Unity or Unreal.

This roster publishes its own semver to [subagents.json](https://cdn.blazium.app/subagents/subagents.json).

## Blazium Engine

[Blazium Engine](https://blazium.app) is the free MIT game engine. The editor and the tools in the table below belong to it. `blazium-cli` installs editors, manages projects, remote-controls a running editor, and deploys to Steam and itch.io. Two lines ship: `blazium-dev` is the Godot 4.3+ line, and `blazium_4.8` is the Godot 4.8+ line. Hub, the crash reporter, skills, and subagents track `blazium_4.8`.

## Blazium Games

[Blazium Games](https://blazium.games) is a separate store, operated by Divine Games, Inc. It is the platform for playing and publishing games, applications, mods, and assets. A game on that store does not have to be made with the Blazium engine, and the engine does not require that store. `chauffeur` is the only upload tool for Blazium Games. Docs are at [docs.blazium.games](https://docs.blazium.games).

## Community

- Official website: [https://blazium.app/](https://blazium.app/)
- IndieDB blog: [https://www.indiedb.com/engines/blazium-engine](https://www.indiedb.com/engines/blazium-engine)
- Official community: [Discord](https://blazium.app/chat)
- Docs: [docs.blazium.app](https://docs.blazium.app)

## Ecosystem

| Product | Role | Release |
|---------|------|---------|
| [Engine](https://github.com/blazium-games/blazium) | The editor. Two lines: `blazium-dev` (Godot 4.3+) and `blazium_4.8` (Godot 4.8+). Hub, crash reporter, skills, and subagents track `blazium_4.8`. | [blazium.app/download](https://blazium.app/download) |
| [CLI](https://github.com/blazium-games/blazium-cli) | Install editors, projects, remote control, Steam and itch.io deploy. Not the Games uploader. | Linux and Windows, x86_64 and x86_32. Catalog: [cli.json](https://cdn.blazium.app/cli/cli.json) |
| [Hub](https://github.com/blazium-games/blazium-hub) | Desktop companion; installers bundle the CLI. Engine builds track `blazium_4.8`. | Linux and Windows, x86_64 and x86_32. |
| [Crash reporter](https://github.com/blazium-games/blazium_crash_reporter) | Sidecar UI for engine and Hub crash reports. Engine builds track `blazium_4.8`. | Linux and Windows, x86_64 and x86_32. Catalog: [crash_reporter.json](https://cdn.blazium.app/crash_reporter/crash_reporter.json) |
| [Toolchain](https://github.com/blazium-games/blazium-toolchain) | PS1, PS2, N64, and Interactive DVD. `ps3` and `ps4` are reserved and do not ship. | Linux and Windows, x86_64 and x86_32. Catalog: [toolchain.json](https://cdn.blazium.app/toolchain/toolchain.json) |
| [Skills](https://github.com/blazium-games/blazium-skills) | Agent skill packs for Claude, Cursor, Codex, and Grok. Own semver, separate from the 0.8.x API baseline. | Catalog: [skills.json](https://cdn.blazium.app/skills/skills.json) |
| [Subagents](https://github.com/blazium-games/blazium-subagents) | Studio roster that loads those skills. Own semver. | Catalog: [subagents.json](https://cdn.blazium.app/subagents/subagents.json) |
| [Blazium Games](https://blazium.games) | Separate store. Upload with chauffeur, not with these tools. | Site [blazium.games](https://blazium.games), docs [docs.blazium.games](https://docs.blazium.games). |

How this engine differs from Godot, Redot, Unity, and Unreal is in the [engine README](https://github.com/blazium-games/blazium).

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
