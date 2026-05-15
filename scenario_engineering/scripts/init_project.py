#!/usr/bin/env python3

"""Initialize a scenario_engineering project workspace from repository templates."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


SUPPORTED_INPUT_SUFFIXES = {".pdf", ".txt", ".md"}
COUNTRY_LANGUAGE_MAP = {
    "china": "Chinese",
    "japan": "Japanese",
    "korea": "Korean",
    "south korea": "Korean",
    "germany": "German",
    "france": "French",
    "italy": "Italian",
    "spain": "Spanish",
    "malaysia": "Malay",
    "thailand": "Thai",
    "vietnam": "Vietnamese",
    "saudi arabia": "Arabic",
    "uae": "Arabic",
    "egypt": "Arabic",
    "usa": "English",
    "united states": "English",
    "uk": "English",
    "united kingdom": "English",
    "australia": "English",
}


def slugify(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "-", value.strip().lower())
    return normalized.strip("-") or "project"


def detect_language(country: str) -> str:
    return COUNTRY_LANGUAGE_MAP.get(country.strip().lower(), "English")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def render_template(template: str, replacements: dict[str, str]) -> str:
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def collect_source_files(source_dir: Path) -> list[Path]:
    return sorted(
        path for path in source_dir.iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED_INPUT_SUFFIXES
    )


def validate_independent_directory(path: Path) -> list[Path]:
    if not path.exists() or not path.is_dir():
        raise ValueError(f"Independent directory not found: {path}")

    files = collect_source_files(path)
    if not files:
        raise ValueError(f"No supported files found in {path}. Expected: {', '.join(sorted(SUPPORTED_INPUT_SUFFIXES))}")
    return files


def build_phase0_report(
    *,
    project_name: str,
    started_at: str,
    updated_at: str,
    input_mode: str,
    source_count: int,
    source_rows: str,
    pending_next_step: str,
) -> str:
    return f"""# Phase 0 Progress Report

## Execution Status

- **Phase**: 0 - Initialization
- **Status**: completed
- **Started**: {started_at}
- **Last Updated**: {updated_at}
- **Duration**: initialized in one run

## Progress Summary

| Metric | Count | Notes |
|--------|-------|-------|
| Total Tasks | 5 | Phase 0 bootstrap tasks |
| Completed | 5 | 100% |
| Pending | 0 | |
| Failed | 0 | |
| In Progress | 0 | |

## Completed Tasks

| # | Task | Source | Output File | Completed At |
|---|------|--------|-------------|--------------|
| 1 | Create project root | repository templates | project workspace | {updated_at} |
| 2 | Create directory structure | directory-structure.md | inputs/, outputs/, archive/ | {updated_at} |
| 3 | Initialize state file | state-template.json | state.json | {updated_at} |
| 4 | Initialize config file | config-template.json | config.json | {updated_at} |
| 5 | Record init summary | bootstrap metadata | phase0-init-report.md | {updated_at} |

## Pending Tasks

| # | Task | Source | Expected Output |
|---|------|--------|-----------------|
| 1 | {pending_next_step} | {input_mode} workflow | phase1 or phase2 execution outputs |

## Failed Tasks

| # | Task | Source | Error | Suggested Action |
|---|------|--------|-------|------------------|
| - | - | - | - | - |

## Current Batch Status

- **Batch Number**: 1
- **Batch Size**: 5
- **Batch Progress**: 5/5
- **Remaining in Batch**: 0

## Agent Task Distribution

| Agent ID | Assigned Tasks | Completed | Failed | Status |
|----------|----------------|-----------|--------|--------|
| local-init | 5 | 5 | 0 | completed |

## Input Snapshot

- **Project Name**: {project_name}
- **Input Mode**: {input_mode}
- **Detected Source Files**: {source_count}

| # | Source File | Notes |
|---|-------------|-------|
{source_rows}

## Estimated Completion

- **Remaining Documents**: {source_count}
- **Estimated Time**: depends on downstream SKILL execution
- **Expected Completion**: pending user execution of next phase

## Errors and Alerts

No initialization errors recorded.

## Next Actions

- [ ] Continue pending tasks (1 remaining)
- [ ] Handle failed tasks (0 items)
- [ ] Proceed to next phase upon completion
- [x] Update state.json checkpoint

## Checkpoint Information

- **Last Checkpoint**: {updated_at}
- **Checkpoint Phase**: 0
- **Checkpoint Action**: init_complete
- **State File Updated**: yes

---

*Report generated: {updated_at}*
*Phase: 0 - Initialization*
"""


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    skill_root = repo_root / "scenario_engineering"
    templates_dir = skill_root / "assets" / "templates"

    parser = argparse.ArgumentParser(description="Initialize a scenario_engineering project workspace.")
    parser.add_argument("--project-name", default="bootstrap", help="Project name used in directory and metadata.")
    parser.add_argument("--industry", default="Generic", help="Industry label stored in config/state.")
    parser.add_argument("--country", default="USA", help="Country label stored in config/state.")
    parser.add_argument("--language", help="Explicit language override. Defaults to country-based detection.")
    parser.add_argument(
        "--input-mode",
        choices=("survey", "independent"),
        default="survey",
        help="Use survey outputs later or initialize from an independent documents directory.",
    )
    parser.add_argument(
        "--independent-directory",
        help="Directory containing PDF/TXT/MD inputs when --input-mode independent is used.",
    )
    parser.add_argument(
        "--output-root",
        default=str(repo_root),
        help="Base directory where the project-{name}-{timestamp} folder will be created.",
    )
    parser.add_argument("--mode", default="new", choices=("new", "dry-run"), help="Create files or print the plan.")
    args = parser.parse_args()

    if args.input_mode == "independent" and not args.independent_directory:
        raise SystemExit("--independent-directory is required when --input-mode independent is used.")

    output_root = Path(args.output_root).resolve()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    iso_now = datetime.now().astimezone().isoformat(timespec="seconds")
    language = args.language or detect_language(args.country)
    project_slug = slugify(args.project_name)
    project_dir = output_root / f"project-{project_slug}-{timestamp}"
    independent_dir = Path(args.independent_directory).resolve() if args.independent_directory else None

    source_files: list[Path] = []
    if args.input_mode == "independent" and independent_dir:
        source_files = validate_independent_directory(independent_dir)

    directories = [
        project_dir / "inputs" / "raw",
        project_dir / "inputs" / "extracted",
        project_dir / "outputs" / "progress",
        project_dir / "outputs" / "phase1-survey" / "questionnaires",
        project_dir / "outputs" / "phase1-survey" / "narratives",
        project_dir / "outputs" / "phase2-parser" / "extracted",
        project_dir / "outputs" / "phase2-parser" / "problems",
        project_dir / "outputs" / "phase3-analyzer" / "reports",
        project_dir / "outputs" / "phase3-analyzer" / "problems",
        project_dir / "outputs" / "phase4-model",
        project_dir / "outputs" / "phase5-final-report",
        project_dir / "archive",
    ]

    if args.mode == "dry-run":
        print(project_dir)
        for directory in directories:
            print(directory)
        return 0

    if project_dir.exists():
        raise SystemExit(f"Refusing to overwrite existing directory: {project_dir}")

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

    copied_files: list[Path] = []
    if source_files:
        raw_dir = project_dir / "inputs" / "raw"
        for source in source_files:
            destination = raw_dir / source.name
            shutil.copy2(source, destination)
            copied_files.append(destination)

    source_entries = copied_files if copied_files else source_files
    input_sources = [str(path) for path in source_entries]
    input_source_1 = input_sources[0] if len(input_sources) >= 1 else ""
    input_source_2 = input_sources[1] if len(input_sources) >= 2 else ""

    skip_phase1 = args.input_mode == "independent"
    current_phase = 2 if skip_phase1 else 1
    resume_action = "start_parser" if skip_phase1 else "start_survey"

    state_replacements = {
        "PROJECT_NAME": args.project_name,
        "CREATED_AT": iso_now,
        "UPDATED_AT": iso_now,
        "INDUSTRY": args.industry,
        "COUNTRY": args.country,
        "LANGUAGE": language,
        "INPUT_MODE": args.input_mode,
        "INDEPENDENT_DIRECTORY": str(independent_dir) if independent_dir else "",
        "INPUT_SOURCE_1": input_source_1,
        "INPUT_SOURCE_2": input_source_2,
        "OUTPUT_DIRECTORY": str(project_dir),
    }

    state = json.loads(render_template(read_text(templates_dir / "state-template.json"), state_replacements))
    state["config"]["skip_phase1"] = skip_phase1
    state["progress"]["current_phase"] = 0
    state["progress"]["phase_status"]["phase0_init"] = "completed"
    if skip_phase1:
        state["progress"]["phase_status"]["phase1_survey"] = "skipped"
        state["progress"]["phase_details"]["phase1_survey"]["completed_at"] = iso_now
    state["progress"]["phase_details"]["phase0_init"]["directories_created"] = True
    state["progress"]["phase_details"]["phase0_init"]["inputs_validated"] = True
    state["progress"]["phase_details"]["phase0_init"]["started_at"] = iso_now
    state["progress"]["phase_details"]["phase0_init"]["completed_at"] = iso_now
    state["progress"]["phase_details"]["phase2_parser"]["total_documents"] = len(source_entries)
    state["progress"]["phase_details"]["phase2_parser"]["pending"] = len(source_entries)
    state["progress"]["phase_details"]["phase2_parser"]["pending_files"] = [path.name for path in source_entries]
    state["progress"]["phase_details"]["phase3_analyzer"]["total_documents"] = len(source_entries)
    state["progress"]["phase_details"]["phase3_analyzer"]["pending"] = len(source_entries)
    state["progress"]["phase_details"]["phase3_analyzer"]["pending_files"] = [
        f"{Path(path.name).stem}-analysis.md" for path in source_entries
    ]
    state["checkpoints"].append({"timestamp": iso_now, "phase": 0, "action": "init_complete"})
    state["resume_info"]["resume_from_phase"] = current_phase
    state["resume_info"]["resume_action"] = resume_action
    state["resume_info"]["resume_files"] = [path.name for path in source_entries]

    source_descriptor = source_entries[0].name if source_entries else "pending-input"
    config_replacements = {
        "PROJECT_NAME": project_slug,
        "PROJECT_DESCRIPTION": "Scenario engineering workflow bootstrap project",
        "TIMESTAMP": timestamp,
        "MODE": "new",
        "INPUT_MODE": args.input_mode,
        "INDEPENDENT_DIRECTORY_PATH": str(independent_dir) if independent_dir else "",
        "DOCUMENT_NAME": Path(source_descriptor).stem,
        "INDUSTRY": args.industry.lower(),
        "COUNTRY": args.country,
        "LANGUAGE": language,
    }
    config = json.loads(render_template(read_text(templates_dir / "config-template.json"), config_replacements))
    config["project"]["name"] = args.project_name
    config["project"]["description"] = "Scenario engineering workflow bootstrap project"
    config["output"]["base_directory"] = project_dir.name
    config["input"]["sources"] = [
        {
            "type": path.suffix.lower().lstrip("."),
            "path": f"inputs/raw/{path.name}",
            "extracted_path": f"inputs/extracted/{Path(path.name).stem}.txt",
        }
        for path in source_entries
    ]
    config["processing"]["skip_phase1"] = skip_phase1

    write_text(project_dir / "state.json", json.dumps(state, indent=2, ensure_ascii=True) + "\n")
    write_text(project_dir / "config.json", json.dumps(config, indent=2, ensure_ascii=True) + "\n")

    source_rows = "\n".join(
        f"| {index} | {path.name} | copied to inputs/raw |" for index, path in enumerate(source_entries, start=1)
    )
    if not source_rows:
        source_rows = "| 1 | no-source-files-yet | survey mode selected; phase 1 will produce narratives |"

    pending_next_step = "Run scenario_parser on copied documents" if skip_phase1 else "Run scenario_survey and create narratives"
    phase0_report = build_phase0_report(
        project_name=args.project_name,
        started_at=iso_now,
        updated_at=iso_now,
        input_mode=args.input_mode,
        source_count=len(source_entries),
        source_rows=source_rows,
        pending_next_step=pending_next_step,
    )
    write_text(project_dir / "outputs" / "progress" / "phase0-init-report.md", phase0_report)

    print(project_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
