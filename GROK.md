# Grok host — blazium-subagents

How Grok should spawn and run this roster. Agents are generated from
`mapping.yaml`. Do not hand-edit `agents/*.md`.

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. GDScript-first. Skills live in
[blazium-skills](https://github.com/blazium-games/blazium-skills). Read that
repo's `GROK.md` first.

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
