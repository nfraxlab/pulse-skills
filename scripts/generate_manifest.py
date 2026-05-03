#!/usr/bin/env python3
"""Generate the Pulse system skill manifest and human-readable index."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MANIFEST_PATH = ROOT / "manifest.json"
INDEX_PATH = ROOT / "INDEX.md"


def _frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    parsed = yaml.safe_load(text[3:end])
    return parsed if isinstance(parsed, dict) else {}


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return []


def _skill_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        content = skill_file.read_text(encoding="utf-8")
        frontmatter = _frontmatter(content)
        name = str(frontmatter.get("name") or skill_file.parent.name).strip()
        description = str(frontmatter.get("description") or "").strip()
        if not name or not description:
            raise ValueError(f"{skill_file} must define name and description")
        if name != skill_file.parent.name:
            raise ValueError(f"{skill_file} name must match directory name")
        metadata = frontmatter.get("metadata")
        metadata = metadata if isinstance(metadata, dict) else {}
        entries.append(
            {
                "name": name,
                "description": description,
                "path": f"skills/{name}/SKILL.md",
                "version": str(metadata.get("version") or ""),
                "tags": _as_list(frontmatter.get("tags") or metadata.get("tags")),
                "trigger_phrases": _as_list(
                    frontmatter.get("trigger_phrases") or metadata.get("trigger_phrases")
                ),
                "checksum": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                "updated_at": datetime.fromtimestamp(
                    skill_file.stat().st_mtime,
                    tz=timezone.utc,
                ).isoformat(),
            }
        )
    return entries


def main() -> None:
    generated_at = datetime.now(timezone.utc).isoformat()
    entries = _skill_entries()
    manifest = {
        "schema_version": 1,
        "generated_at": generated_at,
        "skills": entries,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# Pulse Skills Index",
        "",
        f"Generated at: `{generated_at}`",
        "",
        "| Skill | Description | Tags | Version |",
        "| --- | --- | --- | --- |",
    ]
    for entry in entries:
        tags = ", ".join(entry["tags"]) if entry["tags"] else ""
        version = entry["version"] or ""
        lines.append(
            f"| [{entry['name']}]({entry['path']}) | {entry['description']} | {tags} | {version} |"
        )
    lines.append("")
    INDEX_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
