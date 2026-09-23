# Grok host — blazium-subagents

How Grok should spawn and run this roster. Agents are generated from
`mapping.yaml` plus `mapping.d/*.yaml` shards (`scripts/generate_agents.py`).
Prefer regenerating after mapping edits. Small extras already on origin may
stay as targeted `agents/*.md` patches.

Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. GDScript-first. Skills live in
[blazium-skills](https://github.com/blazium-games/blazium-skills). Read that
repo's `GROK.md` first.

## Community

- Official website: [https://blazium.app/](https://blazium.app/)
- IndieDB blog: [https://www.indiedb.com/engines/blazium-engine](https://www.indiedb.com/engines/blazium-engine)
- Official community: [Blazium Discord](https://discord.gg/sZaf9KYzDp)

## Install

```bash
python scripts/install_links.py
python scripts/validate_agents.py
```

`install_links.py` should junction `agents/` to:

| Host | Path |
|------|------|
| Claude Code | `.claude/agents/` |
| Cursor | `.cursor/agents/` |
| Codex | `.codex/agents/` and `.agents/agents/` |
| Grok | `.grok/agents/` |

Grok does not need a new marketplace file. Point it at `.grok/agents/*.md`
or paste one agent file as the specialist system prompt.

## Mapping layout

| File | Seats |
|------|--------|
| `mapping.yaml` | header, modes, orchestrator → game-designer |
| `mapping.d/01-studio-leads.yaml` | lead-programmer → localization-lead |
| `mapping.d/02-studio-design.yaml` | systems-designer → live-ops-designer |
| `mapping.d/03-programmers.yaml` | gameplay-programmer → technical-artist |
| `mapping.d/04-engine.yaml` | blazium-specialist → autowork-specialist |
| `mapping.d/05-engine-ship.yaml` | cli-specialist → ci-watcher |
| `mapping.d/06-studio-ops.yaml` | performance-analyst → community-manager |

`generate_agents.py` and `validate_agents.py` both call `load_mapping()` and
merge those shards. Do not collapse them into one 32KB `mapping.yaml` through
the write gateway — it truncates.

## Model field

Frontmatter `model: opus` / `sonnet` is the Claude default. On Grok, ignore it
and use the current Grok model.

| Agent tool | Grok tool |
|------------|-----------|
| Read | `read_file` |
| Glob / Grep | `bash` (`find`, `rg`) |
| Write | `write_file` |
| Edit | `edit_file` |
| Team spawn | specialist prompt or `chatroom_send` — not Claude `Task` |

## Spawn contract

1. Start from `blazium-orchestrator`. Do not load all 51 files.
2. Fingerprint `project.blazium`, pick design / prototype / development.
3. Development mode: **producer + at most two** more specialists.
4. Each specialist reads only the `blazium-*` skills in its frontmatter.
5. Skills own APIs. Agents do not invent CLI verbs or JustAMCP tools.

Child context is empty. The spawn prompt must include mode, fingerprints,
skills to read, and the evidence required.

## Systems and genre composition

| Ask | Spawn | Skills |
|-----|-------|--------|
| Genre loop / pillars | `game-designer` | matching `blazium-genre-*` including `blazium-genre-idle` |
| Formulas / matrices | `systems-designer` | same genre set + save/dialogue/feel |
| Economy / prestige / BigNum | `economy-designer` | `blazium-genre-idle` + `blazium-clicker` |
| CharacterBody / scenes | `gameplay-programmer` | `blazium-2d-movement`, `blazium-nodes-scenes` |

Idle composition is `blazium-genre-idle`. BigNum-only math stays on
`blazium-clicker`. Do not treat clicker as the whole idle game.

## Four surfaces (never mix)

| Surface | Default | Owner |
|---------|---------|-------|
| Editor JustAMCP | `:6506/mcp` | `blazium-mcp-specialist` |
| Game JustAMCP | `:6507/mcp` | `blazium-game-mcp-specialist` |
| remote_control | `:6508/v1` | `tools-programmer` / `blazium-cli-remote` |
| Hub remote | `:39218` | `blazium-hub-specialist` |
| Games cloud | `https://mcp.blazium.games/mcp` | `blazium-live-ops-specialist` |

## Output / handoff

Every specialist finishes with from/to, mode, files, evidence (Autowork /
JustAMCP / CLI `--json` / `INCONCLUSIVE`), next agent, and **one** surface.

Host Python, `code_execution`, and screenshots are not evidence.
