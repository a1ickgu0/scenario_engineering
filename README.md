# SKILLs Repository

A collection of Claude Code SKILL definitions containing specialized prompts/workflows to enhance code analysis, generation, and engineering practices.

## 📚 SKILL List

### scenario_engine

INCOSE scenario engineering SKILL providing systems engineering scenario analysis and modeling capabilities.

- **Location**: [`scenario_engine/`](./scenario_engine/)
- **Purpose**: Systems engineering scenario analysis, modeling, requirements decomposition
- **Keywords**: scenario, systems engineering, INCOSE, requirements, use case

## 🏗️ Project Structure

```
SKILLs/
├── README.md                    # Repository documentation (English - this file)
├── README_zh.md                 # Chinese documentation
├── .gitignore                   # Git ignore configuration
├── CONTRIBUTING.md              # Contribution guidelines
│
├── scenario_engine/             # Scenario engineering SKILL
│   ├── SKILL.md                 # SKILL definition file
│   ├── README.md                # SKILL documentation (English)
│   ├── README_zh.md             # SKILL documentation (Chinese)
│   └── assets/
│       ├── templates/           # Scenario template files
│       ├── prompts/             # Prompt files
│       ├── scripts/             # Helper scripts
│       └── examples/            # Usage examples
│
└── [other-skill]/               # Other SKILLs (follow same structure)
    └── ...
```

## 🚀 SKILL Usage

Each SKILL can be used in the following ways:

1. **In Copilot**: Enter `/` and search for SKILL name
2. **Via prompts**: Mention SKILL-related keywords, Agent will auto-load

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