# mapping.yaml restore instructions

Origin `mapping.yaml` on `lucas/growth-ship-grok-host` is TRUNCATED (orchestrator-only after 14dbcd).

Do not regenerate `agents/*.md` from current HEAD.
Do not merge this PR.

Last intact blob on this branch: `8669e1ac` at commit `c35539bd` (~843 lines, all seats through `blazium-ci-watcher`).

Apply these extras onto that blob, then replace origin:

1. `game-designer` and `systems-designer` skills: add `blazium-genre-idle` after puzzle.
2. `economy-designer` skills: `[blazium-genre-card-game, blazium-clicker, blazium-genre-idle]`.
3. `release-manager` skills: add `blazium-itch-publish`, `blazium-steam-publish`.
4. Orchestrator + producer extras: Grok ignore `model:`; child prompts name skills + evidence; idle → genre-idle; BigNum-only → clicker.

A complete 850-line patched file exists locally (`artifacts/mapping.patched.yaml`). Next write must upload that entire file, not a fragment.
