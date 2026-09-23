# Contributing to blazium-subagents

Canonical agents live in [`mapping.yaml`](mapping.yaml). Do not hand-edit
`agents/*.md` except to inspect a generate result — regenerate owns those
files. Verbs and APIs live in
[blazium-skills](https://github.com/blazium-games/blazium-skills).
Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

## Community

- Official website: [https://blazium.app/](https://blazium.app/)
- IndieDB blog: [https://www.indiedb.com/engines/blazium-engine](https://www.indiedb.com/engines/blazium-engine)
- Official community: [Blazium Discord](https://discord.gg/sZaf9KYzDp)

Grok host notes: [GROK.md](GROK.md).

## Add or change an agent

1. Edit the agent block in `mapping.yaml` (`skills`, `role`, `when_not`,
   optional `extras`).
2. Seat rules: 34 `studio`, 15 `blazium`, one `orchestrator`, one `ops`
   (`blazium-ci-watcher`). Do not invent a 16th engine specialist unless
   the roster plan changes.
3. Every published `blazium-*` skill must appear on at least one agent,
   except names listed under `unassigned` (example servers).
4. Generate and validate:

```bash
python scripts/generate_agents.py
python scripts/install_links.py
python scripts/validate_agents.py
```

`extras` is appended after the shared surfaces table so regenerate keeps
orchestrator modes and specialist handoffs.

`validate_agents.py` reads the skills marketplace from
`BLAZIUM_SKILLS_MARKETPLACE` (path or `https://` URL), then a local
checkout of blazium-skills if present, then the published catalog on
`main`.

## Hosts

`install_links.py` links `agents/` to:

| Host | Path |
|------|------|
| Claude Code | `.claude/agents/` |
| Cursor | `.cursor/agents/` |
| Codex | `.codex/agents/` and `.agents/agents/` |
| Grok | `.grok/agents/` |

Copy those folders into a game repo the same way. Load blazium-skills so
frontmatter `skills:` resolve. On Grok, ignore `model: opus` / `sonnet`.
