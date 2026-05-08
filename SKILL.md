---
name: scenario_engineering
description: "Installable repository-entry skill for the scenario_engineering GitHub repo. Use when Codex is given this repository URL directly and needs to discover, route, or install the bundled scenario_survey, scenario_parser, scenario_analyzer, scenario_modeler, and orchestration workflows."
metadata:
  short-description: Repository-entry skill pack for scenario engineering
---

# Scenario Engineering Repository Entry

This root `SKILL.md` exists so the repository itself can be recognized as an installable Codex skill when a user provides only the GitHub repository URL.

## What This Entry Skill Does

- Makes the repository root directly installable as a skill entry.
- Routes work to the appropriate bundled child skill directory.
- Provides a stable discovery path for tools that inspect only the repository root.

## Discovery Rules

When this repository is installed or opened as a single root skill:

1. Read `skills-index.json` first.
2. Treat the directories below as bundled child skills:
   - `scenario_engineering/`
   - `scenario_survey/`
   - `scenario_parser/`
   - `scenario_analyzer/`
   - `scenario_modeler/`
3. Read the child skill's `SKILL.md` before doing task-specific work.
4. Read `agents/openai.yaml` under the selected child skill when UI metadata is needed.

## Routing Guide

- For full-project initialization, orchestration, progress tracking, resume, or finalization:
  read `scenario_engineering/SKILL.md`
- For pre-sales questionnaires and narrative collection:
  read `scenario_survey/SKILL.md`
- For document extraction from PDFs, text, or narratives:
  read `scenario_parser/SKILL.md`
- For structured requirements analysis from parser outputs:
  read `scenario_analyzer/SKILL.md`
- For cross-case synthesis and model generation:
  read `scenario_modeler/SKILL.md`

## Installation Guidance

If a tool or agent supports direct GitHub skill installation from a repository root, this root entry should be used.

If local installation is needed after cloning:

```bash
python3 scripts/install-skills.py --all
```

To install selected bundled skills instead of the whole pack:

```bash
python3 scripts/install-skills.py --skill scenario_parser --skill scenario_analyzer
```

## Notes

- The repository root is a discovery and routing entry, not a replacement for the child skill definitions.
- Canonical task instructions remain in each child skill directory.
