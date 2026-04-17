---
name: scenario_survey
description: "Pre-sales survey SKILL for generating industry-specific questionnaires to collect customer expectations and requirements. Outputs structured narratives that feed directly into scenario_analyzer analysis. Uses customer-friendly language without technical jargon, supports multi-language output (default English), with guided techniques for complete stakeholder identification, detailed usage scenarios, and clear success criteria."
tags:
  - pre-sales-survey
  - interview-guide
  - questionnaire-generation
  - stakeholder-elicitation
  - expectation-collection
  - narrative-synthesis
  - scenario-engine-input
  - multi-language
version: "0.3.0"
---

# Scenario Survey SKILL

## Overview

This SKILL designs and executes **pre-sales surveys** to collect customer expectations and requirements BEFORE solution proposal. It generates industry-specific questionnaires using customer-friendly language, avoiding technical jargon like INCOSE terminology. Supports multi-language output (default English). The outputs are structured narratives ready for `scenario_analyzer` analysis.

**Key Positioning**:
- **Timing**: Pre-sales stage (before solution decision)
- **Goal**: Understand customer needs, expectations, and constraints to inform solution proposal
- **Language**: Default English; customize based on customer country

**Core Capabilities**:
1. **Industry-customized questionnaires**: Tailored questions for Hospitality, Healthcare, Education, Logistics, Retail, Manufacturing, Sports/Entertainment, Services industries
2. **Pre-sales framing**: Ask expectations, not outcomes; ask targets, not achieved results
3. **Guided elicitation techniques**: Systematic methods for complete stakeholder identification, detailed usage scenarios, and clear success criteria
4. **Multi-language support**: Default English output; customize language based on customer country
5. **Customer-friendly language**: All questions in everyday business terms, no methodology jargon

**Output Flow**:
```
scenario_survey → Survey Questionnaire → Interview/Survey Execution → Narrative Document → scenario_analyzer
```

## Language Handling

**Default Language**: English (only for minor/unspecified countries)

**Country-Based Language Customization**:

Generate localized questionnaires for customers from major countries. English is the fallback only for minor countries or unspecified regions.

### East Asia
| Customer Country | Output Language | Notes |
|-----------------|-----------------|-------|
| China, Taiwan, Hong Kong | Chinese (Simplified) | 简体中文 |
| Japan | Japanese | 日本語 |
| South Korea | Korean | 한국어 |

### Europe
| Customer Country | Output Language | Notes |
|-----------------|-----------------|-------|
| Germany, Austria, Switzerland (German-speaking) | German | Deutsch |
| France, Belgium (French-speaking), Luxembourg, Monaco | French | Français |
| Italy, Switzerland (Italian-speaking) | Italian | Italiano |
| Spain, Andorra, Latin America | Spanish | Español |
| Russia, Belarus, Kazakhstan, Ukraine | Russian | Русский |
| Netherlands, Belgium (Dutch-speaking) | Dutch | Nederlands |
| Poland | Polish | Polski |
| Portugal | Portuguese | Português |
| Sweden, Norway, Denmark, Finland, Iceland | Nordic languages | Svenska/Norsk/Dansk |

### Southeast Asia
| Customer Country | Output Language | Notes |
|-----------------|-----------------|-------|
| Malaysia | Malay | Bahasa Melayu |
| Thailand | Thai | ภาษาไทย |
| Vietnam | Vietnamese | Tiếng Việt |
| Indonesia | Indonesian | Bahasa Indonesia |
| Philippines | Filipino/English | Filipino |

### South Asia
| Customer Country | Output Language | Notes |
|-----------------|-----------------|-------|
| India | Hindi/English | हिन्दी |
| Pakistan | Urdu | اردو |

### Middle East & North Africa
| Customer Country | Output Language | Notes |
|-----------------|-----------------|-------|
| Saudi Arabia, UAE, Qatar, Kuwait, Bahrain, Oman, Egypt, Jordan, Lebanon, Iraq, Morocco, Algeria, Tunisia | Arabic | العربية |

### South America
| Customer Country | Output Language | Notes |
|-----------------|-----------------|-------|
| Brazil | Portuguese | Português |
| Other Latin America | Spanish | Español |

### English-Speaking Countries
| Customer Country | Output Language | Notes |
|-----------------|-----------------|-------|
| USA, UK, Canada, Australia, New Zealand, Ireland, South Africa, Singapore | English | English |

### Minor Countries / Unspecified
| Customer Country | Output Language | Notes |
|-----------------|-----------------|-------|
| Minor countries, unspecified regions, or countries without major language support | English | Default fallback |

**Invocation**: User must specify customer country for language customization. The SKILL generates questionnaires in the local language for major countries; only defaults to English for minor/unspecified countries.

## When to Use

- **Pre-sales preparation**: Before proposing solution, need to understand customer expectations
- **Customer interviews**: Planning face-to-face or video interviews in pre-sales stage
- **Requirement gathering**: Need to collect structured customer requirements and success criteria
- **Multiple industry coverage**: Need industry-specific questionnaires for different customer segments
- **Stakeholder identification**: Want systematic approach to identify all relevant stakeholders
- **Usage scenario anticipation**: Need to understand how customer expects to use the solution
- **International customers**: Customers from different countries requiring localized language

## Pre-Sales Question Framing

**Key Principles**:

| Wrong (Post-Implementation) | Correct (Pre-Sales) |
|----------------------------|--------------------|
| "What problems did you have before?" | "What challenges are you currently facing?" |
| "How did you decide?" | "What factors would drive your decision?" |
| "What results did you achieve?" | "What results would you expect to see?" |
| "How do users use it now?" | "How would users work with this solution?" |
| "What compliance issues did you resolve?" | "What compliance requirements must the solution meet?" |

**Framing Guidelines**:
1. **Ask expectations, not outcomes**: "What would you expect?" not "What happened?"
2. **Ask targets, not achieved results**: "What's your target?" not "What did you achieve?"
3. **Ask future scenarios, not past implementations**: "How would you use it?" not "How did you use it?"
4. **Ask constraints, not compliance history**: "What constraints must be considered?" not "What compliance issues did you have?"

## Key Principles

### 1. Customer Language Only
Never use technical methodology terms. Translate all concepts:

| Technical Concept | Customer Language (Pre-Sales) |
|-------------------|------------------------------|
| Stakeholder | "Who would be involved? Who would use it? Who cares about results?" |
| Purchase elements | "What factors would matter most when deciding?" |
| State model | "What stages would the project go through?" |
| Environment model | "What regulations or constraints must be considered?" |
| Entity model | "Which departments would be involved? What system components?" |
| Operational scenario | "How would people use it in daily work?" |
| Parameterized metrics | "What specific targets would indicate success?" |
| Conflicts & priority | "Would there be different opinions? How would you balance them?" |

### 2. Scenario-Based Elicitation
Use concrete scenarios to guide responses, not abstract concepts:
- "Can you describe how a typical workday would look with this solution?"
- "What happens step-by-step when someone starts this task?"

### 3. Target Expectation Collection
Guide natural target sharing:
- "What's your current situation? What improvement would you expect?"
- "Can you estimate the target improvement?"

### 4. Quote-Friendly Collection
Collect natural speech for future reference:
- "What would your leader expect from this project?"
- "Any specific expectations from stakeholders?"

## Guided Elicitation Techniques

### A. Stakeholder Completeness Guidance

**Problem**: Customers often only mention direct participants, missing indirect users, upper management, external parties, and skeptics.

**Method 1: Organization Layer Walkthrough**
```
"Let's walk through who would be involved from top to bottom:
— Who would approve this kind of project? (Decision level)
— Who would manage execution and technical approach? (Management level)
— Which departments/teams would participate? (Execution level)
— Who would use the system day-to-day? (Usage level)
— Who else would care about results? (Interest level)"
```

**Method 2: Four-Party Interest Mapping**
```
"Think about these four aspects:
— Who would benefit from this project? (Beneficiaries)
— Whose work would change because of this? (Affected parties)
— Who would actively support and push this? (Supporters)
— Would anyone have concerns or different views? (Concerned parties)"
```

**Method 3: Scenario Reverse Mapping**
```
"In the scenarios you described, besides who you mentioned:
— Who would initiate this operation?
— Who would assist execution?
— Who would review results?
— Who would be affected by the outcome?"
```

**Method 4: External Connection Mapping**
```
"Besides internal staff, any external parties?
— Do your customers have requirements?
— Partners/vendors to be involved?
— Regulatory bodies/industry associations with standards?"
```

### B. Usage Scenario Detail Guidance

**Problem**: Customers give vague descriptions without specifics.

**Method 1: "A Day's Work" Timeline**
```
"Let's imagine a typical workday after this solution is in place:
— What would be the first thing someone does with this system?
— When during the day would it be used? How frequently?
— What about peak periods? What's special during peaks?"
```

**Method 2: Role Perspective Switch**
```
"Let's view from different angles:
— If you're [Role A], like [Manager], how would you use it daily? What steps?
— If you're [Role B], like [Frontline staff], would usage be different?
— If you're [Role C], like [Customer/External user], how would they interact?"
```

**Method 3: Five-Level Detail Drill**
```
Level 1: "What's this scenario roughly?"
Level 2: "Step 1 specifically—what operation? What device?"
Level 3: "What prerequisites needed? Network/permissions/device state?"
Level 4: "After completion, what result? Who sees it? How judged successful?"
Level 5: "If problems occur mid-way? How would you handle?"
```

**Method 4: Boundary Case Exploration**
```
"We've covered normal operation. What about special cases:
— If network fails/system crashes, what's the backup plan?
— If adding new user/device temporarily, how to operate?
— If usage suddenly spikes, can it handle it?"
```

### C. Success Criteria Clarity Guidance

**Problem**: Customers may not articulate clear expectations for success.

**Method 1: Priority Ranking**
```
"Of the factors you mentioned, let's rank them:
— If only one most important, which one?
— Second most important?
— Third most important?

Why is this most important? What would success look like for this?"
```

**Method 2: Success Criteria Definition**
```
"For each important factor, what would success look like?
— What's your target or expectation?
— How would you measure if it's successful?
— What's the minimum acceptable outcome?"
```

**Method 3: Current Pain Point Quantification**
```
"Let's understand current situation to set targets:
— How often does this problem occur now?
— What's the impact when it happens?
— What improvement would you expect? (e.g., 'reduce by half')"
```

**Method 4: Missing Assumption Test**
```
"Let's confirm importance:
— If [Factor A] wasn't achieved, would project be successful?
— If [Factor B] wasn't achieved, what happens?
— Which factors are 'must achieve' vs 'should achieve'?"
```

## Output Requirements

### Survey Questionnaire Structure

Every questionnaire must follow this framework:

**Part 1: Basic Information** (Opening warm-up)
- Company introduction (industry, scale, main business)
- Project context (why considering, timeline expectations)
- Project name/theme

**Part 2: Current Challenges** (Story starting point)
- What challenges currently facing?
- Impact on business? Specific examples?
- Current situation quantification?

**Part 3: Success Criteria & Expectations** (Core value)
- Using Priority Ranking method
- Using Success Criteria Definition method
- Using Current Pain Point Quantification method

**Part 4: Stakeholders** (Participant panorama)
- Using Organization Layer Walkthrough
- Using Four-Party Interest Mapping
- Using External Connection Mapping

**Part 5: Usage Scenarios** (Expected usage)
- Using "A Day's Work" Timeline method
- Using Role Perspective Switch method
- Using Five-Level Detail Drill method

**Part 6: Industry & Environment** (Background constraints)
- Industry-specific supplementary questions
- Regulatory/compliance requirements
- Scale/geography/existing systems

**Part 7: Targets & Expectations** (Success targets)
- Quantified targets collection
- Quote materials collection

**Part 8: Review & Supplement** (Completeness check)
- "Any people or scenarios missed?"
- "Anything to add that hasn't been mentioned?"

### Narrative Document Output

Survey results synthesized into narrative format matching scenario_analyzer input requirements:

```
## Customer Requirements Narrative

### Basic Information
[Title, Company, Industry, Country, Timeline]

### Current Challenges
[Current situation - problems, context, organizational situation]

### Decision Criteria & Expectations
[What factors would drive decision, who would participate, expected tradeoffs]

### People Involved
[All potential stakeholders with their roles, expectations, influence]

### Expected Usage
[Detailed expected usage scenarios for different roles]

### Success Targets
[Expected outcomes, success criteria, key expectations]

### Key Success Factors
[Ranked success factors with business value explanation]
```

## Completeness Checklist (Pre-Sales Version)

Survey conductor should verify:

**Stakeholder Completeness**
- Decision level identified (who would approve/decide)
- Management level identified (who would manage/coordinate)
- Execution level identified (which departments would participate)
- Usage level identified (who would use day-to-day)
- External parties identified (customers/partners/regulators)
- Concerned parties identified (who might have concerns)

**Usage Scenario Completeness**
- Trigger conditions identified (when would usage start)
- Operation steps identified (how would they operate)
- Prerequisites identified (what preparation needed)
- Success criteria identified (how would success be judged)
- Exception cases identified (what if problems occur)

**Success Factor Completeness**
- Business value clarified (what problem to solve)
- Current pain points quantified (how big is the problem)
- Target expectations set (what improvement expected)
- Priority ranked (which most important)
- Must-achieve vs should-achieve distinguished

**Quote Material Completeness**
- Key expectations recorded (what stakeholders expect)
- Quantified targets collected (specific numbers or ranges)
- Constraints documented (regulatory, budget, technical)

## Workflow

1. **Industry Selection**: User specifies target industry
2. **Template Reference**: **MANDATORY** - Read and follow the corresponding industry template from `assets/templates/` directory
3. **Country Specification**: User specifies customer country for language customization (default English if unspecified)
4. **Questionnaire Generation**: Generate industry-customized questionnaire following template structure and numbering
5. **Survey Execution**: Conduct interview or self-reported survey
6. **Completeness Check**: Verify all required areas covered
7. **Narrative Synthesis**: Convert results into structured narrative document
8. **Output Delivery**: Provide narrative ready for scenario_analyzer input

### Industry Template Reference Rules

**IMPORTANT**: When generating industry-specific questionnaires, you MUST reference the corresponding template file from `assets/templates/` directory.

#### TR-01: Mandatory Template Reference

**Rule**: Before generating any industry questionnaire, you MUST read the corresponding template file. Do not generate questionnaires solely based on SKILL.md generic rules.

| Industry | Template File | Template Path |
|----------|---------------|---------------|
| Education | education-template.md | assets/templates/education-template.md |
| Healthcare | healthcare-template.md | assets/templates/healthcare-template.md |
| Hospitality | hospitality-template.md | assets/templates/hospitality-template.md |
| Logistics | logistics-template.md | assets/templates/logistics-template.md |
| Manufacturing | manufacturing-template.md | assets/templates/manufacturing-template.md |
| Retail | retail-template.md | assets/templates/retail-template.md |
| Services | services-template.md | assets/templates/services-template.md |
| Sports/Entertainment | sports-entertainment-template.md | assets/templates/sports-entertainment-template.md |
| Generic/Other | generic-template.md | assets/templates/generic-template.md |

#### TR-02: Template Structure Compliance

**Rule**: Generated questionnaires must follow the template's structure:
- Use numbered questions (Q1, Q2, Q3...)
- Include [Follow-up] prompts for deeper responses
- Include industry-specific guidance boxes (e.g., [Retail Industry Common Factors])
- Include perspective switch guidance (e.g., ["A Day's Work" - Store Perspective])
- Include completeness checklist matching template appendix

| Template Element | Required in Output | Example |
|------------------|--------------------|---------|
| Numbered questions | Required | "1. Could you briefly introduce your company?" |
| Follow-up prompts | Required | "[Follow-up] What specifically does this look like?" |
| Industry guidance boxes | Required | "[Retail Industry Common Factors]" |
| Perspective guidance | Required | "["A Day's Work" - Store Perspective]" |
| Completeness checklist | Required | "Appendix: Pre-Sales Survey Completeness Checklist" |

#### TR-03: Local Language Adaptation

**Rule**: Translate template content to customer's local language while preserving template structure and numbering. Add local-specific compliance/regulatory questions where applicable.

| Adaptation Type | Requirement | Example |
|-----------------|-------------|---------|
| Language translation | Translate all questions to local language | English → Chinese for Hong Kong customers |
| Structure preservation | Keep numbering, follow-ups, guidance boxes | Q1-Q36 numbering preserved |
| Local additions | Add local compliance/regulatory questions | Hong Kong: PDPO, payment compliance, food safety |

#### TR-04: Template Selection Priority

**Rule**: When customer industry is specified, use industry-specific template first. Only use generic-template.md when industry is unspecified or not covered by existing templates.

| Scenario | Template Selection |
|----------|-------------------|
| Specified industry with template | Use industry-specific template (e.g., retail-template.md for Retail) |
| Specified industry without template | Use generic-template.md with industry customization |
| Unspecified industry | Use generic-template.md |

### Template Reference Workflow

```
Step 1: Identify Industry
├── User specifies industry (e.g., "Retail")
├── Check assets/templates/ for corresponding template
└── If found → retail-template.md
└── If not found → generic-template.md

Step 2: Read Template
├── Read full template file content
├── Extract structure (numbering, sections, follow-ups)
├── Identify industry-specific guidance boxes
└── Identify completeness checklist items

Step 3: Adapt to Local Language
├── Translate questions to customer's local language
├── Preserve numbering and structure
├── Add local-specific compliance questions
└── Maintain follow-up prompts and guidance boxes

Step 4: Generate Questionnaire
├── Follow template question numbering
├── Include all template sections
├── Add local additions in appropriate sections
└── Include completeness checklist from template

Step 5: Output Validation
├── Verify numbering matches template
├── Verify follow-ups included
├── Verify guidance boxes preserved
├── Verify completeness checklist included
```

### Template Reference Completeness Check

**Pre-Generation Check**:
```
- [ ] Template file identified for specified industry
- [ ] Template file content read
- [ ] Template structure extracted
- [ ] Template numbering noted
```

**Post-Generation Check**:
```
- [ ] Questionnaire numbering matches template
- [ ] Follow-up prompts included
- [ ] Industry guidance boxes included
- [ ] Completeness checklist included
- [ ] Local language adaptation complete
- [ ] Local additions added where applicable
```

---

## Version History

- **0.3.0** (2026-04-16):
  - **Added Industry Template Reference Rules**: TR-01 Mandatory Template Reference, TR-02 Template Structure Compliance, TR-03 Local Language Adaptation, TR-04 Template Selection Priority
  - **Updated Workflow**: Added mandatory Step 2 "Template Reference" before questionnaire generation
  - **Added Template Reference Workflow**: Detailed process for reading and adapting templates
  - **Added Template Reference Completeness Check**: Pre-generation and post-generation verification checklist
  - **Added Template Mapping Table**: Industry-to-template-file mapping for all 9 templates
- **0.2.0** (2026-04-12): Repositioned to pre-sales stage; added multi-language support (default English); updated all question framing from post-implementation to pre-sales expectations; added country-based language customization
- **0.1.0** (2026-04-12): Initial scenario_survey SKILL draft