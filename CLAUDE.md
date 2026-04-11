# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a SKILLs repository containing specialized SKILL definitions for Claude Code. Each SKILL is a reusable prompt/workflow definition that can be invoked to perform specific analysis tasks.

## Current SKILLs

### scenario_engine

An INCOSE requirements engineering SKILL for extracting stakeholder information, operational concepts, and product/solution details from vendor customer story PDFs.

**Structure**: [scenario_engine/](scenario_engine/)
- [SKILL.md](scenario_engine/SKILL.md) - SKILL metadata and definition (YAML frontmatter + markdown)
- [README.md](scenario_engine/README.md) - Usage documentation
- [assets/prompts/](scenario_engine/assets/prompts/) - Core prompt templates
- [assets/references/](scenario_engine/assets/references/) - Analysis guidelines

**Invocation**: Reference keywords like "customer story", "stakeholder analysis", "INCOSE", or mention extracting requirements from PDF narratives.

## PDF Processing Workflow

When analyzing customer story PDFs:

1. **Extract text**: Use `pdftotext -layout input.pdf output.txt` or `pdf2txt.py -o output.txt input.pdf`
2. **Add references**: Mark page numbers, sections, or paragraph locations for traceability
3. **Clean content**: Remove headers, footers, and formatting noise
4. **Validate**: Ensure extracted text is readable and complete

## SKILL Output Requirements

The scenario_engine SKILL produces structured output with:
- Customer basic information (title, country, industry, company, year)
- Purchase elements (3-5 business-level factors, ranked by importance, with quantified metrics)
- Stakeholder listing with roles, expectations, influence, value/risk
- Conflict and priority analysis
- Engagement and commitment recommendations
- Operational scenarios
- Product/solution identification
- **Traceability**: Every analysis item must reference original text (page/section/quote)

**Output language**: Use the local language of the source document. Default to Chinese if undetermined.

## Creating New SKILLs

Follow the standard structure:
```
skill-name/
├── SKILL.md           # Required: YAML frontmatter (name, description, tags, version) + definition
├── README.md          # Required: Documentation
└── assets/
    ├── prompts/       # Prompt templates
    ├── references/    # Reference documents
    ├── templates/     # Optional: Templates
    └── examples/      # Optional: Usage examples
```

## Branch Conventions

- `master` - Production stable version
- `dev` - Development branch for new features

## Commit Message Format

```
feat: Add feature description
fix: Fix bug description
docs: Documentation update
refactor: Code refactor description
test: Test-related description
chore: Misc changes description
```