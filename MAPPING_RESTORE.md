# mapping.yaml status

Do not regenerate `agents/*.md` until `mapping.yaml` is ~848 lines and the last agent key is `blazium-ci-watcher`.

Last intact blob on `main`: `8669e1ac` (~842 lines).

Local patched copy (848 lines, 54 keys) lives in the agent sandbox at `artifacts/ben-push/mapping.yaml` with:

- `blazium-genre-idle` on `game-designer`, `systems-designer`, `economy-designer`
- `blazium-itch-publish` + `blazium-steam-publish` on `release-manager`
- Grok extras on orchestrator + producer

Remote `push_files` calls have been dropping the tail of this 32KB file. Restore locally:

```bash
git show 8669e1ac:mapping.yaml > mapping.yaml
# apply extras from this file, then:
python scripts/generate_agents.py
python scripts/validate_agents.py
```
