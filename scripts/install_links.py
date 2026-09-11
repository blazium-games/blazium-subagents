#!/usr/bin/env python3
"""Junction host agent dirs to canonical agents/ (Claude, Cursor, Codex, Grok)."""

from __future__ import annotations

import os
import shutil
import stat
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "agents"
TARGETS = (
    ROOT / ".claude" / "agents",
    ROOT / ".cursor" / "agents",
    ROOT / ".codex" / "agents",
    ROOT / ".agents" / "agents",
    ROOT / ".grok" / "agents",
)


def _is_reparse(path: Path) -> bool:
    if path.is_symlink():
        return True
    if os.name != "nt" or not path.exists():
        return False
    try:
        attrs = os.lstat(path).st_file_attributes
    except AttributeError:
        return False
    return bool(attrs & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def link_dir(dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() or dest.is_symlink():
        if _is_reparse(dest) or dest.is_symlink():
            dest.unlink()
        elif dest.is_dir():
            shutil.rmtree(dest)
        else:
            dest.unlink()
    if os.name == "nt":
        os.system(f'cmd /c mklink /J "{dest}" "{SRC}" >nul')
        if dest.exists():
            return
    dest.symlink_to(SRC, target_is_directory=True)


def main() -> int:
    if not SRC.is_dir():
        print(f"missing {SRC}", file=sys.stderr)
        return 1
    for dest in TARGETS:
        link_dir(dest)
        print(f"linked {dest.relative_to(ROOT)} -> agents/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
