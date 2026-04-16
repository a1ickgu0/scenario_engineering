# Scenario Survey SKILL

## Introduction

scenario_survey is a **pre-sales** survey SKILL for generating industry-specific questionnaires to collect customer expectations and requirements. Outputs structured narrative documents ready for scenario_analyzer analysis.

**Key Positioning**:
- **Timing**: Pre-sales stage (before solution decision)
- **Goal**: Understand customer needs, expectations, and constraints to inform solution proposal
- **Language**: Default English; customize based on customer country

**Key Features**:
- Customer-friendly language, avoiding INCOSE and other technical jargon
- **Ask expectations, not outcomes**: Pre-sales framing
- Guided elicitation techniques ensuring complete information collection
- Industry-customized questions tailored to different sector characteristics
- Multi-language support for international customers

## Language Support

Generate localized questionnaires for customers from major countries. English is the fallback only for minor countries.

### East Asia
| Customer Country | Output Language |
|-----------------|-----------------|
| China, Taiwan, Hong Kong | Chinese (Simplified) 简体中文 |
| Japan | Japanese 日本語 |
| South Korea | Korean 한국어 |

### Europe
| Customer Country | Output Language |
|-----------------|-----------------|
| Germany, Austria, Switzerland (German-speaking) | German Deutsch |
| France, Belgium (French-speaking), Luxembourg, Monaco | French Français |
| Italy, Switzerland (Italian-speaking) | Italian Italiano |
| Spain, Andorra, Latin America | Spanish Español |
| Russia, Belarus, Kazakhstan, Ukraine | Russian Русский |
| Netherlands, Belgium (Dutch-speaking) | Dutch Nederlands |
| Poland | Polish Polski |
| Portugal | Portuguese Português |
| Sweden, Norway, Denmark, Finland, Iceland | Nordic languages |

### Southeast Asia
| Customer Country | Output Language |
|-----------------|-----------------|
| Malaysia | Malay Bahasa Melayu |
| Thailand | Thai ภาษาไทย |
| Vietnam | Vietnamese Tiếng Việt |
| Indonesia | Indonesian Bahasa Indonesia |
| Philippines | Filipino |

### South Asia
| Customer Country | Output Language |
|-----------------|-----------------|
| India | Hindi हिन्दी |
| Pakistan | Urdu اردو |

### Middle East & North Africa
| Customer Country | Output Language |
|-----------------|-----------------|
| Saudi Arabia, UAE, Qatar, Kuwait, Bahrain, Oman, Egypt, Jordan, Lebanon, Iraq, Morocco, Algeria, Tunisia | Arabic العربية |

### South America
| Customer Country | Output Language |
|-----------------|-----------------|
| Brazil | Portuguese Português |
| Other Latin America | Spanish Español |

### English-Speaking Countries
| Customer Country | Output Language |
|-----------------|-----------------|
| USA, UK, Canada, Australia, New Zealand, Ireland, South Africa, Singapore | English |

### Minor Countries / Unspecified
| Customer Country | Output Language |
|-----------------|-----------------|
| Minor countries, unspecified regions, countries without major language support | English (fallback) |

## Use Cases

- Collect customer requirements before running scenario_analyzer analysis
- Plan pre-sales customer interviews
- Understand customer solution expectations and success criteria
- Design differentiated questionnaires for different industries
- Systematically identify all potential stakeholders
- Capture detailed expected usage scenarios
- Localized questionnaires for international customers

## Quick Start

### 1. Generate Questionnaire

```
/scenario_survey
```

System will ask for:
- Target industry (Hospitality, Healthcare, Education, etc.)
- Customer country (for language customization, default English)
- Questionnaire mode (Interview or Self-reported)

### 2. Execute Survey

Conduct interview following questionnaire structure, using guided techniques to ensure completeness.

### 3. Synthesize Narrative

After survey completion, synthesize results into structured narrative document.

## Questionnaire Structure

Each questionnaire contains eight parts:

| Part | Content | Purpose |
|------|---------|---------|
| 1. Basic Information | Company intro, project context | Opening warm-up, establish dialogue |
| 2. Current Challenges | Difficulties faced, business impact | Establish problem starting point |
| 3. Success Criteria & Expectations | Decision factors, priority, success definition | Clarify core value expectations |
| 4. Stakeholders | Decision makers, participants, users, interested parties | Ensure personnel panorama |
| 5. Expected Usage Scenarios | Typical workday, role usage, exception cases | Collect expected usage details |
| 6. Industry & Environment | Industry regulations, company scale, existing systems | Supplement background constraints |
| 7. Targets & Expectations | Quantified targets, success criteria, key expectations | Define success |
| 8. Review & Supplement | Missing check, additional information | Completeness verification |

## Pre-Sales Question Framing

**Core Principle**: Ask expectations, not outcomes

| Wrong (Post-Implementation) | Correct (Pre-Sales) |
|----------------------------|--------------------|
| "What problems did you have before?" | "What challenges are you currently facing?" |
| "How did you decide?" | "What factors would drive your decision?" |
| "What results did you achieve?" | "What results would you expect to see?" |
| "How do users use it now?" | "How would users work with this solution?" |

## Guided Elicitation Techniques

### Stakeholder Completeness

**Common guidance phrasing**:
```
"Let's walk through who would be involved from top to bottom:
— Who would approve this kind of project? (Decision level)
— Who would manage execution and technical approach? (Management level)
— Which departments/teams would participate? (Execution level)
— Who would use the system day-to-day? (Usage level)
— Who else would care about results? (Interest level)"
```

### Expected Usage Scenarios

**Common guidance phrasing**:
```
"Let's imagine a typical workday after this solution is in place:
— What would be the first thing someone does with this system?
— When during the day would it be used? How frequently?
— What about peak periods? What's special during peaks?"
```

### Success Criteria Clarity

**Common guidance phrasing**:
```
"For each important factor, what would success look like?
— What's your target or expectation?
— How would you measure if it's successful?
— What's the minimum acceptable outcome?"
```

## Industry-Specific Focus

Different industries have specific supplementary questions:

| Industry | Specific Focus |
|----------|---------------|
| Hospitality | Guest feedback, multi-location consistency, rating impact |
| Healthcare | Data security, remote access, industry compliance |
| Education | Student count, 1:1 device policy, campus coverage |
| Logistics | Supply chain continuity, global operations, certification |
| Retail | Customer service, logistics efficiency, rating platforms |
| Manufacturing | Production efficiency, predictive maintenance, certifications |
| Sports & Entertainment | On-site experience, data insights, peak capacity |
| Services | Client collaboration, professional efficiency, compliance |

## Completeness Checklist

After survey completion, verify:

**Stakeholder Completeness**:
- Decision level identified (who would approve)
- Management level identified (who would manage)
- Execution level identified (participating departments)
- Usage level identified (daily users)
- External parties identified (customers/partners/regulators)
- Concerned parties identified

**Expected Usage Completeness**:
- Trigger conditions identified (when would use)
- Operation steps identified (how would operate)
- Prerequisites identified (preparation needed)
- Success criteria identified (how to judge success)
- Exception cases identified (problem handling)

**Success Criteria Completeness**:
- Business value clarified (problem to solve)
- Current pain points quantified (problem size)
- Target expectations set (improvement expected)
- Priority ranked (most important)
- Must-achieve vs should-achieve distinguished

## Relationship with Other SKILLs

```
scenario_survey (pre-sales expectation collection)
    ↓ outputs requirements narrative
scenario_analyzer (structured analysis)
    ↓ outputs analysis report
scenario_modeler (cross-case modeling)
    ↓ outputs industry/stakeholder/purchase factor models
```

## Version History

- **0.2.0** (2026-04-12): Repositioned to pre-sales stage; added multi-language support (default English); updated question framing to expectation-oriented; added country-based language customization
- **0.1.0** (2026-04-12): Initial version