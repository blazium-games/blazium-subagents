---
name: setup-blazium
description: Pin this repo to Blazium 0.8.x. Use when starting a Blazium game or confirming the editor.
user-invocable: true
---

# Setup Blazium

Load `blazium-cli` and `blazium-project-config`. Confirm a 0.8.x editor exists.

Write or update `.claude/docs/technical-preferences.md` (create the folder if needed) with:

```text
engine: blazium
product: 0.8.x
godot_compat: 4.8.x
languages: gdscript-first
```

Use Blazium 0.8.x on `blazium_4.8`, not a stock Godot editor. Do not offer Unity or Unreal. Empty tree → `blazium-new-project`, not a `project.godot` generator.
