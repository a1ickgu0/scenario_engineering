# Purchase Factor Synthesis Prompt

## Purpose

Synthesize and abstract purchase factors from multiple scenario_engine analysis outputs into a hierarchical model: Business Driver Layer → Technical Implementation Layer → Quantified Metrics Layer.

---

## Input Requirements

Provide multiple `-analysis.md` documents with purchase elements sections containing:
- Ranking
- Purchase factor
- Business value
- Quantified metrics
- Traceability reference

---

## Hierarchical Model Definition

### Level 1: Business Driver Layer

**Why buy - Strategic motivations**

| Driver | Definition | Example Factors |
|--------|------------|-----------------|
| Cost Optimization | Reduce operational or capital expenditure | NaaS subscription, energy efficiency, OpEx model |
| Efficiency Improvement | Improve operational speed or throughput | AI-native operations, automation, faster deployment |
| Security/Compliance | Meet security standards or regulatory requirements | Zero-trust, HIPAA compliance, GDPR |
| User Experience | Improve end-user satisfaction or capability | Reliable Wi-Fi, seamless connectivity, mobile-first |
| Innovation Transformation | Enable new capabilities or business models | Cloud transition, digital transformation, AI integration |
| Sustainability | Support environmental or long-term goals | Energy reduction, carbon footprint, green operations |

### Level 2: Technical Implementation Layer

**What to buy - Capability enablers**

| Implementation | Definition | Business Drivers Supported |
|----------------|------------|---------------------------|
| AI-native Operations | AI-driven network management and troubleshooting | Efficiency, User Experience, Cost |
| Zero-trust Security | Fine-grained access control and policy enforcement | Security/Compliance |
| Wi-Fi Coverage/Capacity | High-density wireless connectivity | User Experience, Efficiency |
| Cloud Management | Centralized cloud-based monitoring and control | Efficiency, Innovation, Cost |
| SD-WAN | Software-defined wide area networking | Efficiency, Innovation, Cost |
| NaaS Subscription | Network-as-a-Service subscription model | Cost, Innovation |
| Automation | Automated deployment, configuration, updates | Efficiency, Cost |
| Energy Efficiency | Power-saving network infrastructure | Sustainability, Cost |

### Level 3: Quantified Metrics Layer

**How to measure - Success indicators**

| Metric Type | Pattern | Examples |
|-------------|---------|----------|
| Reduction Rate | X% reduction in Y | 100% reduction in fault tickets, 50% reduction in downtime |
| Increase Rate | Xx increase in Y | 2x Wi-Fi coverage, 3x capacity increase |
| Time Savings | X minutes/hours | 30 minutes deployment, hours to minutes |
| Coverage Scale | X users/devices/sites | 26,500 students, 67 schools, 31,000 users |
| Availability | X% uptime/first-connect | 100% first-connect success, 24x7x365 monitoring |
| Cost Metric | OpEx vs CapEx | Monthly subscription, no capital expenditure |

---

## Analysis Instructions

### Step 1: Factor Extraction

1. Extract all purchase factors from the purchase elements table in each document
2. Preserve original factor names and descriptions
3. Note ranking position for each factor
4. Extract quantified metrics and business value

### Step 2: Business Driver Mapping

1. Map each extracted factor to one of the 6 Business Drivers
2. Use semantic similarity and business value description
3. Document reasoning for ambiguous mappings
4. Count frequency per Business Driver

### Step 3: Technical Implementation Mapping

1. Identify technical capability behind each factor
2. Map to one of the Technical Implementations
3. Build Business Driver → Technical Implementation relationships
4. Count frequency per Technical Implementation

### Step 4: Metric Pattern Extraction

1. Extract all quantified metrics from source documents
2. Classify metrics by Metric Type pattern
3. Normalize metric expressions:
   - "100% Reduction" → Reduction Rate: 100%
   - "2x Wi-Fi coverage" → Increase Rate: 2x
   - "30 Minutes" → Time Savings: 30 minutes
4. Count frequency per Metric Type

### Step 5: Industry × Driver Analysis

1. Build Industry × Business Driver matrix
2. Calculate priority ranking per industry:
   - Sum rankings for factors in same Driver category
   - Lower sum = higher priority
3. Identify industry-specific driver priorities

### Step 6: Factor → Solution Mapping

1. Extract products/solutions from each document
2. Map solutions to Technical Implementations they enable
3. Build Technical Implementation → Solution relationships

---

## Output Format

Follow the template: `purchase-factor-template.md`

**Required Sections**:

### 1. Business Driver Frequency Table

| Business Driver | Frequency | Typical Factors | Industries |

### 2. Technical Implementation Frequency Table

| Technical Implementation | Frequency | Business Drivers | Solutions |

### 3. Metric Type Catalog

| Metric Type | Frequency | Typical Expressions | Source Cases |

### 4. Industry × Business Driver Priority Matrix

| Industry | Cost Optimization | Efficiency | Security | User Experience | Innovation | Sustainability |

### 5. Business Driver → Technical Implementation → Solution Chain

```
Cost Optimization
├── NaaS Subscription
│   └── HPE GreenLake for Networking
├── Energy Efficiency
│   └── Low-power APs, Energy-efficient switches
└── Automation
    └── Mist Cloud, Marvis AI

Efficiency Improvement
├── AI-native Operations
│   └── Marvis AI, Juniper Mist
├── Automation
    └── Mist Cloud, ServiceNow integration
└── Cloud Management
    └── Aruba Central, Mist Cloud
```

### 6. Factor Detailed Analysis

| Original Factor | Business Driver | Technical Implementation | Quantified Metric | Source Cases |

---

## Traceability Requirements

For each factor entry, include:
- Original Factor Name: Exact wording from source
- Source Cases: Case IDs where this factor appears
- Ranking: Position in original ranking
- Typical Quote: Original quantified metric expression

---

## Quality Checklist

- [ ] All purchase factors are extracted from source documents
- [ ] Each factor is mapped to a Business Driver
- [ ] Technical Implementation mapping is consistent
- [ ] Metrics are normalized by type pattern
- [ ] Industry × Driver matrix reflects priority rankings
- [ ] Factor → Solution chain is traceable

---

## Example Usage

```
Factor analysis example:
Original: "AI-native network operations" + "100% reduction in fault tickets"
→ Business Driver: Efficiency Improvement
→ Technical Implementation: AI-native Operations
→ Quantified Metric: Reduction Rate: 100%
→ Solutions: Marvis AI, Juniper Mist
→ Source: Education-UK-06-Aberdeen, Manufacturing-Portugal-12-Colep

Industry priority:
Education: User Experience (rank avg: 2) > Efficiency (rank avg: 2.5) > Security
Healthcare: Security (rank avg: 1.5) > Efficiency > Cost
Manufacturing: Efficiency (rank avg: 1) > Cost > Security
```