# SKILLs Repository

A collection of Claude Code SKILL definitions containing specialized prompts/workflows for customer requirements engineering, from pre-sales survey to cross-case modeling.

## 📚 SKILL List

### scenario_engineering (NEW)

**Top-level orchestration SKILL** for coordinating the complete workflow pipeline. Manages directory structure, progress tracking, and task recovery.

- **Location**: [`scenario_engineering/`](./scenario_engineering/)
- **Purpose**: Pipeline orchestration, directory management, progress tracking, task recovery
- **Keywords**: orchestration, workflow coordination, pipeline management, task recovery
- **Version**: 0.2.0
- **Input**: Project configuration (industry, country, input sources)
- **Output**: Complete project directory with all intermediate and final outputs
- **Phases**: 0 (Init) → 1 (Survey) → 2 (Parser) → 3 (Analyzer) → 4 (Modeler) → 5 (Final)

### scenario_survey

**Pre-sales survey SKILL** for generating industry-specific questionnaires to collect customer expectations and requirements. Uses customer-friendly language (no technical jargon), supports multi-language output (default English).

- **Location**: [`scenario_survey/`](./scenario_survey/)
- **Purpose**: Pre-sales requirements gathering, customer expectation collection, stakeholder identification
- **Keywords**: pre-sales survey, interview guide, questionnaire, stakeholder elicitation, expectation collection
- **Version**: 0.3.1
- **Input**: Industry selection + Customer country (for language customization)
- **Output**: Industry-customized survey questionnaires + Customer requirements narrative documents
- **Languages**: English (default), Chinese, Japanese, German, French, Spanish, Arabic

### scenario_parser (NEW)

**Document extraction SKILL** for parsing customer story PDFs and narratives into structured intermediate data. Outputs dual-format files (MD + JSON) preserving full traceability.

- **Location**: [`scenario_parser/`](./scenario_parser/)
- **Purpose**: Data extraction, PDF parsing, intermediate format generation
- **Keywords**: document extraction, PDF parsing, data extraction, intermediate output
- **Version**: 0.1.1
- **Input**: PDF files, text documents, survey narratives
- **Output**: `*-extracted.md` + `*-extracted.json` (dual-format intermediate files)
- **Output Structure**: customer_info, stakeholder_mentions, pain_points, products, metrics, quotes

### scenario_analyzer

**INCOSE requirements engineering SKILL** for generating structured analysis from scenario_parser outputs. Creates 12-section analysis reports for OpenSCENARIO DSL preparation.

- **Location**: [`scenario_analyzer/`](./scenario_analyzer/)
- **Purpose**: Single-case structured analysis, requirements engineering, OpenSCENARIO preparation
- **Keywords**: requirements engineering, INCOSE, stakeholder analysis, customer story
- **Version**: 0.7.0
- **Input**: Parser outputs (`*-extracted.md` + `*-extracted.json`)
- **Output**: 12-section analysis reports (`*-analysis.md`)
- **Change**: Now requires parser outputs as input (architecture split from v0.6.0)

### scenario_modeler

**Cross-case modeling SKILL** for synthesizing multiple scenario_analyzer analyses into inductive models. Prepares industry, stakeholder, and purchase factor models for OpenSCENARIO DSL generation.

- **Location**: [`scenario_modeler/`](./scenario_modeler/)
- **Purpose**: Multi-case synthesis, cross-case pattern mining, model generation
- **Keywords**: scenario modeling, synthesis, cross-case analysis, industry model
- **Version**: 0.5.0
- **Input**: Multiple `-analysis.md` files from scenario_analyzer
- **Output**: Industry Model, Stakeholder Model, Purchase Factor Model with critical analysis

## Install And Discovery

This repository now includes machine-readable discovery metadata for tool-driven installation:

- `SKILL.md` at repository root: direct repository-entry skill for GitHub URL installs
- `agents/openai.yaml` at repository root: UI metadata for the repository-entry skill
- `skills-index.json`: repository-level skill manifest
- `*/agents/openai.yaml`: UI metadata for each skill
- `scripts/install-skills.py`: local installer for Codex or Claude Code skill directories

Typical usage:

```bash
# List all skills in this repo
python3 scripts/install-skills.py --list

# Install every skill into the default Codex directory
python3 scripts/install-skills.py --all

# Install selected skills into a custom Claude Code skill directory
python3 scripts/install-skills.py --skill scenario_parser --skill scenario_analyzer --dest /path/to/skills
```

Discovery guidance for agents given only a GitHub repo URL:

1. Read root `SKILL.md` first if the tool inspects only the repository root.
2. Read `skills-index.json` to discover bundled child skills.
3. Resolve the requested skill by `name` and `path`.
4. Load `<skill>/SKILL.md` as the canonical child-skill entry file.
5. Optionally read `<skill>/agents/openai.yaml` for UI-facing metadata.

Direct GitHub URL install target for Codex:

```text
https://github.com/a1ickgu0/scenario_engineering
```

Expected behavior:
- Codex can recognize the repository root as an installable entry skill.
- The root skill then routes work to the correct bundled child skill.

---

## 🔗 SKILL Chain Workflow

The complete workflow from pre-sales to cross-case modeling:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION (scenario_engineering)                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Phase 0: Initialization                                                 │
│  • Determine input source (survey vs independent files)                  │
│  • Create output directory structure                                     │
│  • Initialize state.json for progress tracking                           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                        PRE-SALES STAGE (Phase 1)                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_survey]                                                       │
│  • Generate industry-specific questionnaire                              │
│  • Multi-language support                                                │
│  • Collect: stakeholders, usage scenarios, success criteria             │
│         ↓                                                                │
│  Customer Requirements Narrative Document                                │
│                                                                          │
│  (Optional - Skip if independent files provided)                         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                     EXTRACTION STAGE (Phase 2)                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_parser]                                                       │
│  • PDF/text/narrative → structured data                                  │
│  • Dual-format output (MD + JSON)                                        │
│  • Full traceability preservation                                        │
│         ↓                                                                │
│  Extracted Files (*-extracted.md + *-extracted.json)                     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                      ANALYSIS STAGE (Phase 3)                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_analyzer]                                                     │
│  • Input: Parser outputs (MD + JSON)                                     │
│  • INCOSE requirements engineering                                       │
│  • 12-section structured output                                          │
│  • State/Environment/Entity/Lifecycle models                             │
│         ↓                                                                │
│  Single-case Analysis Report (*-analysis.md)                             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                      MODELING STAGE (Phase 4)                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_modeler]                                                      │
│  • Cross-case synthesis                                                  │
│  • Industry/Stakeholder/Purchase Factor models                           │
│  • Critical analysis with credibility ratings                            │
│         ↓                                                                │
│  OpenSCENARIO DSL Preparation                                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                      FINALIZATION (Phase 5)                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  • Validate completeness                                                 │
│  • Generate execution summary                                            │
│  • Archive state.json                                                    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Architecture Changes (2026-04-21)

| Before | After |
|--------|-------|
| `scenario_analyzer` (PDF → Analysis) | `scenario_parser` + `scenario_analyzer` |
| Direct PDF processing | Parser outputs intermediate MD + JSON |
| Single-phase analysis | Phase 2 (Parser) + Phase 3 (Analyzer) |

**Benefits of Split**:
- Decoupling: Parser can run independently for batch PDF processing
- Flexibility: Analyzer accepts Parser outputs or manually prepared data
- Recovery: Parser outputs are checkpoints, can resume Analyzer separately
- Quality: Intermediate data can be validated before analysis

---

## 🏗️ Project Structure

```
SKILLs/
├── README.md                    # Repository documentation (English - this file)
├── README_zh.md                 # Chinese documentation
├── CLAUDE.md                    # Claude Code guidelines
├── CONTRIBUTING.md              # Contribution guidelines
│
├── scenario_engineering/        # Orchestration SKILL (NEW)
│   ├── SKILL.md                 # SKILL definition
│   ├── README.md                # Documentation
│   ├── README_zh.md             # Documentation (Chinese)
│   └── assets/
│       ├── templates/           # State/Config/Progress templates
│       └── references/          # Phase definitions, Recovery guidelines
│
├── scenario_survey/             # Pre-sales survey SKILL
│   ├── SKILL.md                 # SKILL definition
│   ├── README.md                # Documentation
│   ├── README_zh.md             # Documentation (Chinese)
│   └── assets/
│       ├── templates/           # 9 industry questionnaire templates
│       └── references/          # Industry patterns
│
├── scenario_parser/             # Document extraction SKILL (NEW)
│   ├── SKILL.md                 # SKILL definition
│   ├── README.md                # Documentation
│   ├── README_zh.md             # Documentation (Chinese)
│   └── assets/
│       ├── templates/           # Extracted JSON/MD templates
│       └── references/          # Extraction patterns
│
├── scenario_analyzer/           # Analysis SKILL
│   ├── SKILL.md                 # SKILL definition (v0.7.0)
│   ├── README.md                # Documentation
│   ├── README_zh.md             # Documentation (Chinese)
│   ├── CLAUDE.md                # Claude Code guidelines
│   └── assets/
│       ├── prompts/             # Analysis prompts
│       └── references/          # Analysis guidelines
│
├── scenario_modeler/            # Cross-case modeling SKILL
│   ├── SKILL.md                 # SKILL definition
│   ├── README.md                # Documentation
│   ├── README_zh.md             # Documentation (Chinese)
│   └── assets/
│       ├── prompts/             # 17 synthesis prompts
│       ├── references/          # 10 reference guides
│       └── templates/           # 14 output templates
│
└── [other-skill]/               # Other SKILLs (follow same structure)
```

---

## 🎯 Entry Point Selection

Choose the appropriate SKILL entry point based on your available input materials:

| Entry Point | Starting SKILL | Input Required | Use Case |
|-------------|----------------|----------------|----------|
| **Full Pipeline** | scenario_engineering | None (start fresh) | Complete end-to-end workflow |
| **Survey Only** | scenario_survey | Industry + Country | Generate questionnaires only |
| **Parser Only** | scenario_parser | PDF/Text files | Extract structured data from documents |
| **Analyzer Only** | scenario_analyzer | extracted.md + extracted.json | Generate analysis reports from parsed data |
| **Modeler Only** | scenario_modeler | Multiple *-analysis.md files | Synthesize cross-case models |

### Decision Tree

```
What do you want to do?
    ↓
├── Complete new project → scenario_engineering --new
│
├── Continue existing work → scenario_engineering --resume
│
├── Generate questionnaire only → /scenario_survey
│   (Have: Industry, Country, Language)
│
├── Extract from existing PDFs → /scenario_parser
│   (Have: PDF/Text documents)
│
├── Analyze extracted data → /scenario_analyzer
│   (Have: *-extracted.md + *-extracted.json)
│
└── Model from analyses → /scenario_modeler
    (Have: Multiple *-analysis.md files)
```

---

## 🚀 SKILL Usage

Each SKILL can be used in the following ways:

1. **In Claude Code**: Enter `/` and search for SKILL name
2. **Via prompts**: Mention SKILL-related keywords, Agent will auto-load

### Quick Start Examples

**Full Pipeline (Orchestrated)**:
```
# Start complete workflow
/scenario_engineering --new
→ Industry: Hospitality
→ Country: Malaysia
→ Input: ./customer-stories/*.pdf
→ Outputs complete project directory
```

**Step-by-Step (Manual)**:
```
# Step 1: Pre-sales survey
/scenario_survey
→ Generates questionnaire for Malaysian hotel chain

# Step 2: After interview, synthesize narrative
/scenario_survey --synthesize
→ Customer requirements narrative document

# Step 3: Extract data from documents
/scenario_parser
→ Input: narrative or PDF
→ Output: extracted.md + extracted.json

# Step 4: Structured analysis
/scenario_analyzer
→ Input: extracted.md + extracted.json
→ Output: analysis.md (12 sections)

# Step 5: Cross-case modeling
/scenario_modeler
→ Input: multiple analysis.md files
→ Output: Industry/Stakeholder/Purchase models
```

---

## 📊 Recent Changes

- **2026-05-06**: Entry point selection and LLM capability checks
  - **Updated `scenario_engineering`** (v0.1.0 → v0.2.0)
    - Added Entry Point Selection section with decision tree
    - Added `--from-skill` option for direct SKILL invocation
    - Distinguished entry point vs. phase selection
  - **Updated `scenario_survey`** (v0.3.0 → v0.3.1)
    - Added LLM file capability check for template reading
    - Added fallback to Bash cat command
  - **Updated `scenario_parser`** (v0.1.0 → v0.1.1)
    - Added LLM file capability check for PDF processing
    - Added local Python PDF tools (pdfplumber, pdftotext)
    - Added Python extraction script examples
  - **Updated README.md**
    - Added Entry Point Selection section
    - Updated version numbers for all modified SKILLs

- **2026-04-21**: Architecture refactoring

- **2026-04-21**: Architecture refactoring
  - **Added `scenario_engineering`** (v0.1.0) - Top-level orchestration SKILL
  - **Added `scenario_parser`** (v0.1.0) - Document extraction into MD + JSON
  - **Modified `scenario_analyzer`** (v0.7.0) - Now accepts Parser outputs as input
  - Split Phase 2 into Phase 2 (Parser) + Phase 3 (Analyzer)
  - Independent recovery support for Parser/Analyzer

- **2026-04-16**: Enhanced `scenario_analyzer` (v0.6.0)
  - Added stakeholder pain points extraction
  - Added synthesis sections per table

- **2026-04-12**: Added `scenario_survey` SKILL (v0.2.0)
  - Pre-sales positioning, multi-language support
  - 9 industry-specific questionnaire templates

- **2026-04-12**: Added `scenario_modeler` SKILL (v0.1.0)
  - 42 files for cross-case synthesis

---

## 📝 Creating New SKILLs

Refer to [CONTRIBUTING.md](./CONTRIBUTING.md) for how to create new SKILLs.

Standard SKILL structure:
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

---

## 🔄 Branch Management

- `main` - Production stable version
- `dev` - Development branch for new features

---

## 📄 License

MIT

---

**[中文版本](README_zh.md)**
