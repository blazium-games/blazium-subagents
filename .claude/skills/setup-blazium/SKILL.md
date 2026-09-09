---
name: setup-blazium
description: Pin this repo to Blazium 0.6.x. Use when starting a Blazium game or confirming the editor.
user-invocable: true
---

# Setup Blazium

Load `blazium-cli` and `blazium-project-config`. Confirm a 0.6.x editor exists.

Write or update `.claude/docs/technical-preferences.md` (create the folder if needed) with:

```text
engine: blazium
product: 0.6.x
godot_compat: 4.3.2
languages: gdscript-first
```

Do not offer Unity, Unreal, or Godot 4.7. Empty tree → `blazium-new-project`, not a `project.godot` generator.
