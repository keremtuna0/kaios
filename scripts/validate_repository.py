#!/usr/bin/env python3
"""Small, dependency-free consistency checks for the KAIOS documentation repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_HEADINGS = {
    "Purpose", "Responsibilities", "Inputs", "Outputs", "Activation Criteria",
    "Dependencies", "Non-Goals", "Workflow", "Quality Gates",
    "Review Checklist", "Extension Rules", "Example",
}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def local_links(root: Path) -> list[str]:
    errors: list[str] = []
    for document in root.rglob("*.md"):
        text = document.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            if "://" in target or target.startswith("mailto:"):
                continue
            path = (document.parent / target).resolve()
            if not path.exists():
                errors.append(f"broken link in {document.relative_to(root)}: {target}")
    return errors


def main() -> int:
    errors: list[str] = []
    manifest_path = ROOT / "manifest" / "kaios.manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read manifest: {exc}")
        return 1

    for path in [manifest["activeVersionPath"], *manifest["assistantPrompts"].values(),
                 *manifest["contractTemplates"], *manifest["examples"]]:
        check((ROOT / path).exists(), f"missing registered path: {path}", errors)

    for module in manifest["modules"]:
        path = ROOT / module["path"]
        check(path.exists(), f"missing module file: {module['path']}", errors)
        if path.exists():
            headings = set(re.findall(r"^## (.+)$", path.read_text(encoding="utf-8"), re.M))
            missing = REQUIRED_HEADINGS - headings
            check(not missing, f"{module['id']} missing headings: {', '.join(sorted(missing))}", errors)

    errors.extend(local_links(ROOT))
    if errors:
        print("Repository validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Repository validation passed: {len(manifest['modules'])} modules, local links, and registered paths.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
