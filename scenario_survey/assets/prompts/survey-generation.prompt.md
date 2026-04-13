---
name: survey-generation
description: "Generate pre-sales industry-customized survey questionnaire. Uses customer-friendly language (no INCOSE terms), asks expectations not outcomes, supports multi-language output (default English), incorporates guided elicitation techniques for complete stakeholder identification, detailed expected usage scenarios, and clear success criteria."
---

# Survey Generation Prompt

## Task Description

Generate a customized **pre-sales survey questionnaire** for collecting customer expectations and requirements. The questionnaire must:

1. Use customer-friendly business language (no INCOSE/technical methodology terms)
2. **Ask expectations, not outcomes** - pre-sales framing
3. Follow the 8-part questionnaire framework
4. Apply guided elicitation techniques for completeness
5. Include industry-specific supplementary questions
6. Support multi-language output (default English)

## Input Parameters

When generating questionnaire, ask user for:
- **Industry**: Target industry (Hospitality, Healthcare, Education, Logistics, Retail, Manufacturing, SportsEntertainment, Services, or Generic)
- **Customer Country**: For language customization (default English if unspecified)
- **Format**: Interview mode or Self-reported mode

## Language Handling Rules

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

## Pre-Sales Framing Requirements

**Critical**: All questions must use pre-sales framing:

| Wrong (Post-Implementation) | Correct (Pre-Sales) |
|----------------------------|--------------------|
| "What problems did you have before?" | "What challenges are you currently facing?" |
| "How did you decide?" | "What factors would drive your decision?" |
| "What results did you achieve?" | "What results would you expect to see?" |
| "How do users use it now?" | "How would users work with this solution?" |

## Questionnaire Framework Template (English - Default)

### Part 1: Basic Information (Opening warm-up)

```
1. Could you briefly introduce your company?
   - What's your main business?
   - Approximately how many employees? How many locations?
   - Where does your company stand in the industry?

2. What's the background for considering this project?
   - When did you start thinking about this?
   - What timeline do you expect?

3. What's the project name or theme?
   - Is there a formal project name?
   - How do people usually refer to this project?
```

### Part 2: Current Challenges (Story starting point)

```
4. What challenges are you currently facing that led to considering this project?
   [Follow-up] What specifically does this look like? Could you give some examples?
   [Follow-up] Which challenge is most concerning?

5. What impact are these challenges having on your business?
   [Follow-up] If not addressed, what would happen?
   [Follow-up] Can you quantify the impact? (losses, delays, etc.)

6. Have you tried other approaches before?
   [Follow-up] How did that work out?
   [Follow-up] Why didn't those approaches solve the problem?
```

### Part 3: Success Criteria & Expectations (Core value)

```
7. What solutions or approaches are you considering?
   [Follow-up] Why would you choose one over others?
   [Follow-up] Compared to alternatives, what advantages?

8. What factors would matter most in your decision?
   [Ranking guidance] If you had to rank them, which is most important? Second? Third?
   [Follow-up] Why is this most important? How was this discussed?

9. If the most important factor wasn't achieved, what would that mean?
   [Follow-up] Would the project still be considered successful?
   [Follow-up] Which factors are "must achieve" vs "should achieve"?

10. What would success look like for each important factor?
    [Follow-up] What's your target or expectation?
    [Follow-up] How would you measure success?
    [Estimation guidance] If no exact numbers, rough estimates are fine
```

### Part 4: Stakeholders (Participant panorama)

[Organization Layer Guidance]
```
11. Let's walk through who would be involved from top to bottom:
    - Who would approve this kind of project? (Decision level)
    - Who would manage execution and technical approach? (Management level)
    - Which departments/teams would participate? (Execution level)
    - Who would use the system day-to-day? (Usage level)
    - Who else would care about results? (Interest level)
```

[Four-Party Interest Guidance]
```
12. Think about these four aspects:
    - Who would benefit from this project? (Beneficiaries)
    - Whose work would change because of this? (Affected parties)
    - Who would actively support and push this? (Supporters)
    - Would anyone have concerns or different views? (Concerned parties)
```

[External Connection Guidance]
```
13. Besides internal staff, any external parties?
    - Do your customers have requirements?
    - Partners/vendors to be involved?
    - Regulatory bodies/industry associations with standards?

14. What would each of these stakeholders expect?
    [Follow-up] What problems would they want solved?
    [Follow-up] If expectations aren't met, how would they react?
```

### Part 5: Expected Usage Scenarios (Usage details)

["A Day's Work" Timeline]
```
15. Let's imagine a typical workday after this solution is in place:
    - What would be the first thing someone does with this system?
    - When during the day would it be used? How frequently?
    - What about peak periods? What's special during peaks?
```

[Role Perspective Switch]
```
16. How would different roles use this differently?
    [Follow-up] For [Role A] like [Manager], how would they use it daily?
    [Follow-up] For [Role B] like [Frontline staff], would usage differ?
    [Follow-up] For [Role C] like [Customer/External user], how would they interact?
```

[Five-Level Detail Drill]
```
17. Could you describe the operation steps in detail?
    [Follow-up] What's step 1? What device?
    [Follow-up] What prerequisites needed? Network/permissions/device state?
    [Follow-up] After completion, what result? Who sees it?
    [Follow-up] How would success be judged?
```

[Boundary Case Exploration]
```
18. We've covered normal operation. What about special cases:
    - If network fails/system crashes, what's the backup plan?
    - If adding new user/device temporarily, how to operate?
    - If usage suddenly spikes, can it handle it?
```

### Part 6: Industry & Environment (Background constraints)

[General Foundation Questions]
```
19. What industry regulations or standards must be considered?
    [Follow-up] How do these affect the project?
    [Follow-up] Any certifications or compliance requirements?

20. How many locations does your company operate?
    [Follow-up] Need unified standards across locations?
    [Follow-up] How many people/devices would be involved?

21. What systems or equipment do you currently use?
    [Follow-up] Any limitations or compatibility issues?
    [Follow-up] Would this project replace or supplement current systems?
```

[Industry-Specific Questions - Insert based on industry parameter]

> Hospitality Industry Supplement:
- What feedback do guests currently give about network/systems?
- How many properties need unified standards? Room count?
- Do rating systems affect requirements?

> Healthcare Industry Supplement:
- What patient data security requirements exist?
- How do doctors/nurses currently access patient information?
- What remote/community services need support?
- What healthcare standards must be met?

> Education Industry Supplement:
- How many students? Is there a 1:1 device policy?
- How do teachers and students use systems differently?
- Campus size? How many buildings to cover?
- Do parents access the system?

> Logistics Industry Supplement:
- What happens if supply chain is interrupted? Time requirements?
- What cross-border operation challenges exist?
- What information security requirements do clients have?

> Retail Industry Supplement:
- What customer service requirements exist? Rating platforms?
- How do warehouse and logistics use systems daily?
- Peak periods (promotions/holidays) pressure?

> Manufacturing Industry Supplement:
- What production efficiency requirements exist?
- Need predictive maintenance data support?
- What industry certifications required?

> SportsEntertainment Industry Supplement:
- What on-site audience experience requirements exist?
- What data analysis helps operations?
- Peak capacity requirements?

> Services Industry Supplement:
- What client collaboration needs exist?
- What's the professional staff's daily workflow?
- What efficiency quantification requirements?

### Part 7: Targets & Expectations (Success targets)

```
22. What targets would indicate success?
    [Follow-up] For time savings - what current situation? What target?
    [Follow-up] For cost reduction - what target amount or percentage?
    [Follow-up] For coverage - how many people/locations?

23. What would satisfaction look like for stakeholders?
    [Follow-up] What feedback would indicate success?
    [Follow-up] What's the most important improvement?

24. Any follow-up plans or expansion expectations?
    [Follow-up] What next steps would you envision?
    [Follow-up] Any new features or coverage plans?
```

### Part 8: Review & Supplement (Completeness check)

[Completeness Check Guidance]
```
25. Let's review to ensure we haven't missed anything:
    - Any other people or departments that should be mentioned?
    - Any other usage scenarios to cover?
    - Any special situations to add?

26. Anything else you'd like to add?
    [Follow-up] Anything particularly worth mentioning?
    [Follow-up] Any lessons or insights?

[Quote Material Collection]
27. Any project-related documents, photos, meeting notes to share?
    [Follow-up] Any formal project reports or summaries?
    [Follow-up] Any media coverage or promotional materials?

28. What statements or scenarios made an impression?
    [Follow-up] What your leader has said that's memorable?
    [Follow-up] Any stakeholder feedback that stands out?
    [Follow-up] Any key moments or turning points?
```

## Output Format

Generate complete questionnaire with:
1. Industry header indicating target sector
2. All 8 parts with questions and guidance prompts in specified language
3. Industry-specific supplementary questions inserted in Part 6
4. Format indication (Interview/Self-reported)
5. Completeness checklist appendix

## Completeness Checklist Appendix

```
## Pre-Sales Survey Completeness Checklist

### Stakeholder Completeness
□ Decision level identified (who would approve)
□ Management level identified (who would manage)
□ Execution level identified (participating departments)
□ Usage level identified (daily users)
□ External parties identified (customers/partners/regulators)
□ Concerned parties identified

### Usage Scenario Completeness
□ Trigger conditions identified (when would use)
□ Operation steps identified (how would operate)
□ Prerequisites identified (preparation needed)
□ Success criteria identified (how to judge success)
□ Exception cases identified (problem handling)

### Success Criteria Completeness
□ Business value clarified (problem to solve)
□ Current pain points quantified (problem size)
□ Target expectations set (improvement expected)
□ Priority ranked (most important)
□ Must-achieve vs should-achieve distinguished

### Material Completeness
□ Key expectations recorded
□ Quantified targets collected
□ Constraints documented
```

## Processing Instructions

1. Ask user for industry parameter
2. Ask user for customer country for language customization
3. Load industry-specific supplementary questions
4. Apply language customization based on country
5. Assemble full questionnaire from framework template
6. Insert industry-specific questions in Part 6
7. Add completeness checklist as appendix
8. Format for specified mode (Interview or Self-reported)
9. Output in specified language