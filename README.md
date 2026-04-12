# SKILLs Repository

A collection of Claude Code SKILL definitions containing specialized prompts/workflows to enhance code analysis, generation, and engineering practices.

## 📚 SKILL List

### scenario_engine

INCOSE requirements engineering SKILL for extracting stakeholder information and operational concepts from customer story PDFs. Outputs are structured for OpenSCENARIO DSL preparation.

- **Location**: [`scenario_engine/`](./scenario_engine/)
- **Purpose**: Single-case customer story analysis, requirements extraction, OpenSCENARIO preparation
- **Keywords**: requirements engineering, INCOSE, stakeholder analysis, customer story, scenario analysis
- **Version**: 0.2.0
- **Output**: Generates `-analysis.md` files with customer info, purchase elements, stakeholders, state/environment/entity models, lifecycle phases, and parameterization

### scenario_modeler

SKILL for synthesizing multiple scenario_engine analyses into inductive models and cross-case patterns. Prepares industry, stakeholder, and purchase factor models for OpenSCENARIO DSL generation.

- **Location**: [`scenario_modeler/`](./scenario_modeler/)
- **Purpose**: Multi-case synthesis, cross-case pattern mining, industry/stakeholder/purchase model generation, OpenSCENARIO DSL preparation
- **Keywords**: scenario modeling, synthesis, cross-case analysis, industry model, stakeholder model, DSL preparation
- **Version**: 0.1.0
- **Input**: Multiple `-analysis.md` files from scenario_engine
- **Output**: Industry Model, Stakeholder Model, Purchase Factor Model, State/Environment/Entity/Lifecycle/Parameterization models with cross-analysis matrices

## 🏗️ Project Structure

```
SKILLs/
├── README.md                    # Repository documentation (English - this file)
├── README_zh.md                 # Chinese documentation
├── CHANGES_ANALYSIS.md          # Detailed analysis of recent changes
├── COMMIT_MESSAGE.md            # Commit message summary
├── .gitignore                   # Git ignore configuration
├── CONTRIBUTING.md              # Contribution guidelines
│
├── scenario_engine/             # Scenario engineering SKILL
│   ├── SKILL.md                 # SKILL definition with metadata
│   ├── README.md                # SKILL documentation (English)
│   ├── README_zh.md             # SKILL documentation (Chinese)
│   ├── CLAUDE.md                # Claude Code guidelines
│   └── assets/
│       ├── prompts/             # Prompt files
│       ├── references/          # Reference documents
│       └── examples/            # Usage examples
│
├── scenario_modeler/            # Scenario modeling synthesis SKILL
│   ├── SKILL.md                 # SKILL definition with metadata
│   ├── README.md                # SKILL documentation (English)
│   ├── README_zh.md             # SKILL documentation (Chinese)
│   └── assets/
│       ├── prompts/             # 17 analysis and synthesis prompt files
│       ├── references/          # 10 reference guides and mappings
│       └── templates/           # 14 output templates
│
└── [other-skill]/               # Other SKILLs (follow same structure)
    └── ...
```

## 🚀 SKILL Usage

Each SKILL can be used in the following ways:

1. **In Copilot**: Enter `/` and search for SKILL name
2. **Via prompts**: Mention SKILL-related keywords, Agent will auto-load

### Workflow: Customer Story → OpenSCENARIO DSL

```
Customer Story PDF/Text
    ↓
[scenario_engine] - Single-case analysis
    ↓
*-analysis.md files (×1 per story)
    ↓
[scenario_modeler] - Multi-case synthesis
    ↓
Industry/Stakeholder/Purchase Models
    ↓
OpenSCENARIO DSL (parameter definitions)
```

## 📊 Recent Changes

- **2026-04-12**: Upgraded `scenario_engine` to v0.2.0 with OpenSCENARIO DSL preparation support
  - Added 5 new analysis dimensions: State Model, Environment Model, Entity Model, Lifecycle Phases, Parameterization
  - Expanded output from 9 items to 14 items with bilingual documentation
  - See [SCENARIO_ENGINE_CHANGES.md](./SCENARIO_ENGINE_CHANGES.md) for detailed analysis
  - See [SCENARIO_ENGINE_COMMIT.md](./SCENARIO_ENGINE_COMMIT.md) for upgrade summary

- **2026-04-12**: Added `scenario_modeler` SKILL (v0.1.0) with 42 new files
  - 17 prompt templates for model synthesis and OpenSCENARIO prep
  - 10 reference guides for taxonomies and mappings
  - 14 output templates for structured results
  - See [CHANGES_ANALYSIS.md](./CHANGES_ANALYSIS.md) for detailed analysis
  - See [COMMIT_MESSAGE.md](./COMMIT_MESSAGE.md) for commit summary

## 📝 Creating New SKILLs

Refer to [CONTRIBUTING.md](./CONTRIBUTING.md) for how to create new SKILLs.

Basic steps:

1. Create `<skill-name>/` directory
2. Add `SKILL.md` file (SKILL definition)
3. Create `assets/` directory to organize resources
4. Write `README.md` documentation (English)
5. Optionally add `README_zh.md` for Chinese version

## 🔄 Branch Management

- `master` - Production stable version
- `dev` - Development branch for new features and improvements

## 📄 License

MIT

---

**[中文版本](README_zh.md)**