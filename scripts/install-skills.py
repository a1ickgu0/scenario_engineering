#!/usr/bin/env python3

"""Install one or more skills from this repository into a target directory."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


def load_manifest(manifest_path: Path) -> dict:
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def build_skill_map(manifest: dict) -> dict[str, dict]:
    return {item["name"]: item for item in manifest["skills"]}


def repo_entry_ignore(_: str, names: list[str]) -> set[str]:
    excluded = {
        ".git",
        ".claude",
        ".DS_Store",
        "__pycache__",
        "agent-skills",
        "report",
        "tests",
        "project-bootstrap-demo-20260508-100509",
        "project-phase-check-20260508-101244",
        "project-phase-check-clean-20260508-101347",
    }
    return {name for name in names if name in excluded}


def install_path(repo_root: Path, source_path: str, skill_name: str, dest_root: Path, force: bool) -> None:
    source_dir = (repo_root / source_path).resolve()
    target_dir = dest_root / skill_name

    if not (source_dir / "SKILL.md").exists():
        raise FileNotFoundError(f"Missing SKILL.md for {skill_name}: {source_dir}")

    if target_dir.exists():
        if not force:
            raise FileExistsError(f"Destination already exists: {target_dir}")
        shutil.rmtree(target_dir)

    if source_path == ".":
        shutil.copytree(source_dir, target_dir, ignore=repo_entry_ignore)
    else:
        shutil.copytree(source_dir, target_dir)


def install_skill(repo_root: Path, skill_meta: dict, dest_root: Path, force: bool) -> None:
    install_path(repo_root, skill_meta["path"], skill_meta["name"], dest_root, force)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install skills from this repository.")
    parser.add_argument(
        "--manifest",
        default="skills-index.json",
        help="Path to the repository skill manifest.",
    )
    parser.add_argument(
        "--dest",
        default="~/.codex/skills",
        help="Target directory for installed skills. Use a Claude Code skill directory if needed.",
    )
    parser.add_argument(
        "--skill",
        action="append",
        default=[],
        help="Skill name to install. Can be specified multiple times.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Install all skills listed in the manifest.",
    )
    parser.add_argument(
        "--repo-entry",
        action="store_true",
        help="Install the repository root as a single entry skill bundle.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List skills in the manifest and exit.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing destination skill directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    manifest_path = (repo_root / args.manifest).resolve()
    manifest = load_manifest(manifest_path)
    skill_map = build_skill_map(manifest)

    if args.list:
        repo_entry = manifest.get("repository_entry")
        if repo_entry:
            print(f'REPO_ENTRY\t.\t{repo_entry["entry"]}')
        for skill in manifest["skills"]:
            print(f'{skill["name"]}\t{skill["version"]}\t{skill["path"]}')
        return 0

    if args.repo_entry:
        selected = []
    elif args.all:
        selected = list(skill_map)
    else:
        selected = args.skill

    if not selected and not args.repo_entry:
        print("Select at least one skill with --skill or install everything with --all.", file=sys.stderr)
        return 2

    unknown = [name for name in selected if name not in skill_map]
    if unknown:
        print(f"Unknown skill(s): {', '.join(unknown)}", file=sys.stderr)
        return 2

    dest_root = Path(args.dest).expanduser().resolve()
    dest_root.mkdir(parents=True, exist_ok=True)

    if args.repo_entry:
        install_path(repo_root, ".", "scenario_engineering", dest_root, args.force)
        print(f"Installed repository entry -> {dest_root / 'scenario_engineering'}")

    for skill_name in selected:
        install_skill(repo_root, skill_map[skill_name], dest_root, args.force)
        print(f"Installed {skill_name} -> {dest_root / skill_name}")

    print("Restart Codex or Claude Code to pick up newly installed skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
