# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a SKILLs repository containing specialized SKILL definitions for Claude Code. SKILLs form a complete workflow chain from pre-sales survey to cross-case modeling for customer requirements engineering.

## SKILL Chain Architecture

```
scenario_survey (售前收集期望) → scenario_analyzer (结构化分析) → scenario_modeler (跨案例建模)
```

| Stage | SKILL | Input | Output |
|-------|-------|-------|--------|
| Pre-Sales | scenario_survey | Industry + Country | Industry questionnaire + Narrative document |
| Analysis | scenario_analyzer | Narrative/PDF | Structured analysis (12 sections) |
| Modeling | scenario_modeler | Multiple analyses | Industry/Stakeholder/Purchase models |

## Current SKILLs

### scenario_survey (v0.2.0)

**Pre-sales survey SKILL** for collecting customer expectations before solution proposal.

**Structure**: [scenario_survey/](scenario_survey/)
- [SKILL.md](scenario_survey/SKILL.md) - SKILL definition (pre-sales + multi-language)
- [README.md](scenario_survey/README.md) - English documentation
- [README_zh.md](scenario_survey/README_zh.md) - Chinese documentation
- [assets/templates/](scenario_survey/assets/templates/) - 9 industry-specific questionnaires

**Key Features**:
- Customer-friendly language (no INCOSE jargon)
- Multi-language support (default English)
- Guided elicitation for stakeholder/scenario/criteria completeness
- Industry-specific templates (Hospitality, Healthcare, Education, Logistics, etc.)

**Invocation**: Keywords like "survey", "questionnaire", "interview guide", "pre-sales", "customer expectations"

### scenario_analyzer (v0.2.0)

**INCOSE requirements engineering SKILL** for structured analysis of customer stories.

**Structure**: [scenario_analyzer/](scenario_analyzer/)
- [SKILL.md](scenario_analyzer/SKILL.md) - SKILL metadata and definition
- [README.md](scenario_analyzer/README.md) - Usage documentation
- [assets/prompts/](scenario_analyzer/assets/prompts/) - Core analysis prompt
- [assets/references/](scenario_analyzer/assets/references/) - Analysis guidelines

**Output Structure** (12 sections):
1. Customer Basic Information
2. Purchase Elements (ranked, quantified)
3. Stakeholder List (roles, expectations, influence, relationships)
4. State Model (stakeholder/system/organization states)
5. Environment Model (industry/regional/organizational/technical)
6. Entity Model (organization/system/external hierarchy)
7. Lifecycle Phases (triggers/actions/completion criteria)
8. Operational Scenarios (trigger/conditions/transitions)
9. Engagement and Commitment
10. Products and Solutions
11. Parameterization Model (metrics/roles/scenarios/constraints)
12. Traceability and Notes

**Invocation**: Keywords like "customer story", "stakeholder analysis", "INCOSE", "requirements extraction"

### scenario_modeler (v0.1.0)

**Cross-case modeling SKILL** for synthesizing multiple analyses into patterns.

**Structure**: [scenario_modeler/](scenario_modeler/)
- [SKILL.md](scenario_modeler/SKILL.md) - SKILL definition
- [README.md](scenario_modeler/README.md) - Documentation
- [assets/prompts/](scenario_modeler/assets/prompts/) - 17 synthesis prompts
- [assets/templates/](scenario_modeler/assets/templates/) - 14 output templates

**Output Models**:
- Industry Model (patterns, challenges, solutions)
- Stakeholder Model (Category + Role layers)
- Purchase Factor Model (Driver → Implementation → Metrics hierarchy)
- Cross-analysis matrices
- Critical analysis with credibility ratings

**Invocation**: Keywords like "model synthesis", "cross-case", "industry model", "pattern extraction"

## Workflow Example

```
# Step 1: Generate survey questionnaire
/scenario_survey
→ Industry: Hospitality, Country: Malaysia
→ Output: hospitality-malaysia-questionnaire-en.md

# Step 2: After interview, synthesize narrative
/scenario_survey --synthesize
→ Output: customer-requirements-narrative.md

# Step 3: Structured analysis
/scenario_analyzer
→ Input: narrative document
→ Output: hotel-analysis.md (12 sections)

# Step 4: Cross-case modeling (multiple cases)
/scenario_modeler
→ Input: multiple -analysis.md files
→ Output: Industry/Stakeholder/Purchase models
```

## PDF Processing Workflow

When processing customer story PDFs for scenario_analyzer:

1. **Extract text**: `pdftotext -layout input.pdf output.txt`
2. **Add references**: Mark page numbers, sections for traceability
3. **Clean content**: Remove headers, footers, formatting noise
4. **Validate**: Ensure extracted text is readable and complete

## Language Handling

Generate localized output for customers from major countries. English is the fallback only for minor countries.

### Major Countries - Local Language Output

**East Asia**:
| Country | Language |
|---------|----------|
| China, Taiwan, Hong Kong | Chinese (Simplified) 简体中文 |
| Japan | Japanese 日本語 |
| South Korea | Korean 한국어 |

**Europe**:
| Country | Language |
|---------|----------|
| Germany, Austria, Switzerland (German) | German Deutsch |
| France, Belgium (French), Luxembourg, Monaco | French Français |
| Italy, Switzerland (Italian) | Italian Italiano |
| Spain, Andorra, Latin America | Spanish Español |
| Russia, Belarus, Kazakhstan, Ukraine | Russian Русский |
| Netherlands, Belgium (Dutch) | Dutch Nederlands |
| Poland | Polish Polski |
| Portugal | Portuguese Português |
| Sweden, Norway, Denmark, Finland, Iceland | Nordic languages |

**Southeast Asia**:
| Country | Language |
|---------|----------|
| Malaysia | Malay Bahasa Melayu |
| Thailand | Thai ภาษาไทย |
| Vietnam | Vietnamese Tiếng Việt |
| Indonesia | Indonesian Bahasa Indonesia |
| Philippines | Filipino |

**South Asia**:
| Country | Language |
|---------|----------|
| India | Hindi हिन्दी |
| Pakistan | Urdu اردو |

**Middle East & North Africa**:
| Country | Language |
|---------|----------|
| Saudi Arabia, UAE, Qatar, Kuwait, Bahrain, Oman, Egypt, Jordan, Lebanon, Iraq, Morocco, Algeria, Tunisia | Arabic العربية |

**South America**:
| Country | Language |
|---------|----------|
| Brazil | Portuguese Português |
| Other Latin America | Spanish Español |

**English-Speaking Countries**:
| Country | Language |
|---------|----------|
| USA, UK, Canada, Australia, New Zealand, Ireland, South Africa, Singapore | English |

### Minor Countries / Unspecified - English Fallback

| Country | Language |
|---------|----------|
| Minor countries, unspecified regions, countries without major language support | English |

## Creating New SKILLs

Follow the standard structure:
```
skill-name/
├── SKILL.md           # Required: YAML frontmatter + definition
├── README.md          # Required: English documentation
├── README_zh.md       # Optional: Chinese documentation
└── assets/
    ├── prompts/       # Prompt templates
    ├── references/    # Reference documents
    ├── templates/     # Output templates
    └── tests/         # Generated examples
```

## Branch Conventions

- `main` - Production stable version
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