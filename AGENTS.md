# Agent hierarchy

Spawn through `blazium-orchestrator`. Do not load all 49 studio/engine seats.
Junctions: `.claude/agents`, `.cursor/agents`, `.codex/agents`, `.agents/agents`.

## Tier 0 — Router

| Agent | Use |
|-------|-----|
| `blazium-orchestrator` | Fingerprint Blazium, pick mode, spawn producer + specialists |

## Tier 1 — Directors (Opus)

| Agent | Use |
|-------|-----|
| `creative-director` | Vision, tone, pillar conflicts |
| `technical-director` | Architecture, 4.3.2 pin, surface choice |
| `producer` | Coordination, review mode, smallest team |

## Tier 2 — Leads (Sonnet)

| Agent | Use |
|-------|-----|
| `game-designer` | Loops and progression |
| `lead-programmer` | Code structure, GDScript-first reviews |
| `art-director` | Visual standards |
| `audio-director` | Buses and palette |
| `narrative-director` | Story architecture |
| `qa-lead` | Autowork strategy, go/no-go |
| `release-manager` | Export, CI, stores |
| `localization-lead` | `tr()` and locales |

## Tier 3 — Studio specialists

Design: `systems-designer`, `level-designer`, `economy-designer`, `ux-designer`, `world-builder`, `writer`, `live-ops-designer`

Engineering: `gameplay-programmer`, `engine-programmer`, `ai-programmer`, `network-programmer`, `tools-programmer`, `ui-programmer`, `technical-artist`, `performance-analyst`, `security-engineer`, `analytics-engineer`, `prototyper`

Craft / QA: `sound-designer`, `qa-tester`, `accessibility-specialist`, `devops-engineer`, `community-manager`

## Blazium engine seats (replace Godot/Unity/Unreal)

| Agent | Surface / module |
|-------|------------------|
| `blazium-specialist` | Product vs Godot, `project.blazium` |
| `blazium-gdscript-specialist` | GDScript 2.0 |
| `blazium-luau-specialist` | Luau |
| `blazium-csharp-specialist` | C# (existing .NET projects) |
| `blazium-shader-specialist` | Text `.gdshader` |
| `blazium-mcp-specialist` | Editor JustAMCP `:6506` |
| `blazium-game-mcp-specialist` | `res://mcp` `:6507` |
| `blazium-autowork-specialist` | Native tests |
| `blazium-cli-specialist` | `blazium-cli` install/update |
| `blazium-hub-specialist` | Hub `:39218` |
| `blazium-export-specialist` | Desktop / web / specialty |
| `blazium-toolchain-specialist` | GPL retro sidecar |
| `blazium-live-ops-specialist` | Login, lobby, Steam, Discord, Games cloud |
| `blazium-modules-specialist` | ENV, HTTP, Socket.IO, streaming, Xbox |
| `blazium-content-specialist` | Tags, search, SQLite, GOAP |

## Ops

| Agent | Use |
|-------|-----|
| `blazium-ci-watcher` | First failing export/CI job (`blazium-ci-watch`) |

## Modes

| Mode | Spawn |
|------|--------|
| Design | orchestrator, producer, creative-director, game-designer, art-director |
| Prototype | orchestrator, producer, prototyper, blazium-specialist, blazium-gdscript-specialist, blazium-autowork-specialist |
| Development | producer + classifier from `blazium-router` (max +2) |

## Rules

- Ask → options → approve. No autopilot file writes.
- Skills own APIs. Agents do not invent `blazium-cli hub install`.
- Never mix MCP layers or Hub remote with editor catalog.
- Review modes: `full` | `lean` | `solo` (producer).
