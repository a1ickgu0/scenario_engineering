# SKILLs Repository

A collection of Claude Code SKILL definitions containing specialized prompts/workflows for customer requirements engineering, from pre-sales survey to cross-case modeling.

## 📚 SKILL List

### scenario_survey

**Pre-sales survey SKILL** for generating industry-specific questionnaires to collect customer expectations and requirements. Uses customer-friendly language (no technical jargon), supports multi-language output (default English).

- **Location**: [`scenario_survey/`](./scenario_survey/)
- **Purpose**: Pre-sales requirements gathering, customer expectation collection, stakeholder identification
- **Keywords**: pre-sales survey, interview guide, questionnaire, stakeholder elicitation, expectation collection
- **Version**: 0.2.0
- **Input**: Industry selection + Customer country (for language customization)
- **Output**: Industry-customized survey questionnaires + Customer requirements narrative documents
- **Languages**: English (default), Chinese, Japanese, German, French, Spanish, Arabic

### scenario_analyzer

**INCOSE requirements engineering SKILL** for extracting stakeholder information and operational concepts from customer story narratives. Outputs are structured for OpenSCENARIO DSL preparation.

- **Location**: [`scenario_analyzer/`](./scenario_analyzer/)
- **Purpose**: Single-case structured analysis, requirements extraction, OpenSCENARIO preparation
- **Keywords**: requirements engineering, INCOSE, stakeholder analysis, customer story, scenario analysis
- **Version**: 0.2.0
- **Input**: Customer story narrative documents (from scenario_survey or direct PDF/text)
- **Output**: `-analysis.md` files with customer info, purchase elements, stakeholders, state/environment/entity models, lifecycle phases, and parameterization

### scenario_modeler

**Cross-case modeling SKILL** for synthesizing multiple scenario_analyzer analyses into inductive models. Prepares industry, stakeholder, and purchase factor models for OpenSCENARIO DSL generation.

- **Location**: [`scenario_modeler/`](./scenario_modeler/)
- **Purpose**: Multi-case synthesis, cross-case pattern mining, industry/stakeholder/purchase model generation
- **Keywords**: scenario modeling, synthesis, cross-case analysis, industry model, stakeholder model
- **Version**: 0.1.0
- **Input**: Multiple `-analysis.md` files from scenario_analyzer
- **Output**: Industry Model, Stakeholder Model, Purchase Factor Model with critical analysis and cross-analysis matrices

---

## 🔗 SKILL Chain Workflow

The complete workflow from pre-sales to cross-case modeling:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PRE-SALES STAGE                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Customer Interview/Survey                                               │
│         ↓                                                                │
│  [scenario_survey]                                                       │
│  • Generate industry-specific questionnaire                              │
│  • Multi-language support (English/Chinese/Japanese/etc.)               │
│  • Guided elicitation techniques                                         │
│  • Collect: stakeholders, usage scenarios, success criteria             │
│         ↓                                                                │
│  Customer Requirements Narrative Document                                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                      STRUCTURED ANALYSIS STAGE                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_analyzer]                                                       │
│  • INCOSE requirements engineering                                       │
│  • 12-section structured output                                          │
│  • State/Environment/Entity/Lifecycle models                             │
│  • Parameterization for DSL                                              │
│  • Traceability to original text                                         │
│         ↓                                                                │
│  Single-case Analysis Report (*-analysis.md)                             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                      CROSS-CASE MODELING STAGE                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Multiple Analysis Reports                                               │
│         ↓                                                                │
│  [scenario_modeler]                                                      │
│  • Cross-case synthesis                                                  │
│  • Industry patterns extraction                                          │
│  • Stakeholder abstraction (Category + Role layers)                      │
│  • Purchase factor hierarchy (Driver → Implementation → Metrics)        │
│  • Critical analysis with credibility ratings                            │
│         ↓                                                                │
│  Industry/Stakeholder/Purchase Factor Models                             │
│         ↓                                                                │
│  OpenSCENARIO DSL Preparation                                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Key Workflow Features

| Stage | SKILL | Core Value |
|-------|-------|------------|
| Pre-Sales | scenario_survey | Customer-friendly language, complete stakeholder elicitation |
| Analysis | scenario_analyzer | INCOSE structure, OpenSCENARIO-ready models |
| Modeling | scenario_modeler | Cross-case patterns, industry insights |

---

## 🏗️ Project Structure

```
SKILLs/
├── README.md                    # Repository documentation (English - this file)
├── README_zh.md                 # Chinese documentation
├── CLAUDE.md                    # Claude Code guidelines
├── CONTRIBUTING.md              # Contribution guidelines
│
├── scenario_survey/             # Pre-sales survey SKILL
│   ├── SKILL.md                 # SKILL definition (pre-sales + multi-language)
│   ├── README.md                # Documentation (English)
│   ├── README_zh.md             # Documentation (Chinese)
│   └── assets/
│       ├── prompts/             # Questionnaire generation + Narrative synthesis
│       ├── references/          # Guidance techniques + Industry patterns
│       ├── templates/           # 9 industry-specific questionnaire templates
│       └── tests/               # Generated questionnaire examples
│
├── scenario_analyzer/             # Requirements engineering SKILL
│   ├── SKILL.md                 # SKILL definition with INCOSE structure
│   ├── README.md                # Documentation (English)
│   ├── README_zh.md             # Documentation (Chinese)
│   ├── CLAUDE.md                # Claude Code guidelines
│   └── assets/
│       ├── prompts/             # Customer story analysis prompt
│       ├── references/          # Analysis guidelines
│       └── examples/            # Usage examples
│
├── scenario_modeler/            # Cross-case modeling SKILL
│   ├── SKILL.md                 # SKILL definition
│   ├── README.md                # Documentation (English)
│   ├── README_zh.md             # Documentation (Chinese)
│   └── assets/
│       ├── prompts/             # 17 analysis and synthesis prompts
│       ├── references/          # 10 reference guides
│       └── templates/           # 14 output templates
│
└── [other-skill]/               # Other SKILLs (follow same structure)
    └── ...
```

---

## 🚀 SKILL Usage

Each SKILL can be used in the following ways:

1. **In Claude Code**: Enter `/` and search for SKILL name
2. **Via prompts**: Mention SKILL-related keywords, Agent will auto-load

### Quick Start Example

```
# Step 1: Pre-sales survey
/scenario_survey
> Industry: Hospitality
> Country: Malaysia
→ Generates English questionnaire for Malaysian hotel chain

# Step 2: After interview, synthesize narrative
/scenario_survey --synthesize --input interview-notes.md
→ Customer requirements narrative document

# Step 3: Structured analysis
/scenario_analyzer
→ -analysis.md with 12-section INCOSE structure

# Step 4: Cross-case modeling (multiple cases)
/scenario_modeler
→ Industry/Stakeholder/Purchase Factor Models
```

---

## 📊 Recent Changes

- **2026-04-12**: Added `scenario_survey` SKILL (v0.2.0)
  - Pre-sales positioning: collect expectations, not outcomes
  - Multi-language support (default English)
  - 9 industry-specific questionnaire templates
  - Guided elicitation techniques for stakeholder/scenario/criteria completeness
  - Country-based language customization

- **2026-04-12**: Upgraded `scenario_analyzer` to v0.2.0
  - Added 5 analysis dimensions: State/Environment/Entity/Lifecycle/Parameterization
  - OpenSCENARIO DSL preparation support
  - Traceability requirements enhanced

- **2026-04-12**: Added `scenario_modeler` SKILL (v0.1.0)
  - 42 files for cross-case synthesis
  - Industry/Stakeholder/Purchase Factor models
  - Critical analysis with credibility ratings

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