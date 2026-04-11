# Contributing Guide

Thank you for your interest and contributions to the SKILLs repository!

## 📋 Types of Contributions

We welcome the following types of contributions:

1. **New SKILL Development** - Create new SKILL definitions
2. **SKILL Improvements** - Enhance existing SKILL functionality
3. **Templates and Resources** - Add useful templates, prompts, examples
4. **Documentation** - Improve and refine documentation
5. **Bug Fixes** - Fix issues in existing SKILLs

## 🚀 Workflow

### 1. Fork and Branch

```bash
# Fork repository (via GitHub UI)
# Clone your fork
git clone https://github.com/your-username/SKILLs.git

# Create feature branch (from dev branch)
git checkout -b feature/your-feature-name
```

### 2. Create New SKILL

If adding a new SKILL, follow the standard directory structure:

```
your-skill-name/
├── SKILL.md                 # SKILL definition file (required)
├── README.md               # SKILL documentation (required, English)
├── README_zh.md            # SKILL documentation (optional, Chinese)
└── assets/
    ├── templates/          # Template files
    ├── prompts/            # Prompt files
    ├── examples/           # Usage examples
    └── references/         # Reference documents
```

### 3. SKILL.md File Requirements

New SKILLs must include the following YAML frontmatter:

```yaml
---
name: skill-name
description: "Clear description. Use when: specific use cases"
tags:
  - tag1
  - tag2
version: "0.1.0"
---
```

### 4. Commit Changes

```bash
# Add changes
git add .

# Commit (follow commit message conventions)
git commit -m "feat: add new SKILL"
git commit -m "docs: improve XXX SKILL documentation"
git commit -m "fix: fix issue in XXX SKILL"

# Push to your fork
git push origin feature/your-feature-name
```

### 5. Submit Pull Request

1. Create Pull Request on GitHub
2. Target branch: `dev` (for new features) or `master` (for bug fixes)
3. Describe your changes
4. Wait for review and approval

## 📝 Commit Message Convention

Use the following format for commit messages:

```
feat: add new feature description
fix: fix bug description
docs: documentation update description
refactor: code refactor description
test: test-related description
chore: misc changes description
```

**Examples**:
```bash
git commit -m "feat: Add INCOSE scenario analysis SKILL"
git commit -m "docs: Update scenario-engine README with examples"
git commit -m "fix: Correct typo in use-case template"
```

## 🎨 Code Standards

### Documentation Standards

- Use Markdown format
- Maintain clear and consistent style
- Check spelling and grammar
- Default to English, optionally provide Chinese version

### Naming Conventions

**File names**:
- Use lowercase letters
- Separate words with hyphens: `scenario-template.md`
- Avoid spaces and special characters

**SKILL names**:
- Use lowercase letters
- Separate with hyphens: `skill-name`
- Meaningful and descriptive

### Templates and Examples

- Use existing templates to ensure consistency
- Provide realistic examples
- Include clear instructions and comments

## ✅ Checklist

Before submitting PR, ensure:

- [ ] Code/documentation is clear
- [ ] Spelling and grammar are correct
- [ ] Naming conventions are followed
- [ ] Required YAML frontmatter is attached
- [ ] Relevant README or documentation is included (English by default)
- [ ] If new SKILL, update main README.md
- [ ] Commit message is clear and meaningful
- [ ] Local tests pass (if applicable)

## 🐛 Reporting Bugs

If you find a bug:

1. Check if there's already a related issue
2. Create new issue with detailed description:
   - Bug description
   - Reproduction steps
   - Expected behavior
   - Actual behavior
   - Related SKILL name

## 💡 Suggestions and Discussions

- Propose ideas in Discussions
- Tag related issues
- Provide background and use cases

## 🤝 Community

- Respect all contributors
- Provide constructive feedback
- Help others improve

## 📄 License

By submitting contributions, you agree that your changes are released under the MIT license.

---

Thank you for your contributions! We look forward to working with you! 🎉