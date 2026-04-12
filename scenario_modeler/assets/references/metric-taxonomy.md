# Metric Taxonomy Reference

## Purpose

This document provides standardized metric terminology and classification for normalizing quantified metrics from scenario_engine analysis outputs.

---

## Metric Type Classification

### Reduction Metrics

| Metric Type | Pattern | Normalized Format | Examples |
|-------------|---------|-------------------|----------|
| Fault Ticket Reduction | X% reduction in tickets | `fault_ticket_reduction: X%` | 100%, 80%, 50% |
| Downtime Reduction | X% reduction in downtime | `downtime_reduction: X%` | 90%, 50% |
| Cost Reduction | X% reduction in cost | `cost_reduction: X%` | 30%, 20% |
| Manual Work Reduction | X hours reduced to Y minutes | `manual_work_reduction: hours_to_minutes` | hours → minutes |
| Incident Reduction | X% reduction in incidents | `incident_reduction: X%` | 70%, 50% |
| Error Rate Reduction | X% reduction in errors | `error_rate_reduction: X%` | 95%, 60% |

### Increase Metrics

| Metric Type | Pattern | Normalized Format | Examples |
|-------------|---------|-------------------|----------|
| Coverage Increase | Xx coverage increase | `coverage_increase: Xx` | 2x, 3x |
| Capacity Increase | Xx capacity increase | `capacity_increase: Xx` | 2x, 1.5x |
| Efficiency Increase | X% efficiency improvement | `efficiency_increase: X%` | 50%, 30% |
| Speed Increase | Xx faster | `speed_increase: Xx` | 2x, 3x |
| User Count Increase | From X to Y users | `user_count_increase: X→Y` | 26500 → 31000 |

### Time Metrics

| Metric Type | Pattern | Normalized Format | Examples |
|-------------|---------|-------------------|----------|
| Deployment Time | X minutes/hours | `deploy_time: Xmin/Xhr` | 30min, 2hr |
| Resolution Time | X hours → minutes | `resolution_time: hours_to_minutes` | hours → minutes |
| Setup Time | X minutes | `setup_time: Xmin` | 5min, 10min |
| Migration Time | X minutes downtime | `migration_time: Xmin` | 30min |
| Response Time | X seconds/minutes | `response_time: Xs/Xmin` | 30s, 5min |

### Coverage Scale Metrics

| Metric Type | Pattern | Normalized Format | Examples |
|-------------|---------|-------------------|----------|
| User Count | X users/learners | `user_count: X` | 26500, 31000 |
| Site Count | X schools/sites | `site_count: X` | 67, 100 |
| Device Count | X devices | `device_count: X` | 31000 |
| Coverage Area | X locations | `coverage_area: X` | 67 schools, 100 sites |

### Availability Metrics

| Metric Type | Pattern | Normalized Format | Examples |
|-------------|---------|-------------------|----------|
| Uptime | X% uptime | `uptime: X%` | 99.9%, 99.99% |
| First Connect Success | X% first-connect success | `first_connect_success: X%` | 100% |
| Availability Rate | X% availability | `availability_rate: X%` | 99.9% |
| Service Level | 24x7x365 monitoring | `service_level: 24x7x365` | 24x7x365 |

### Cost Metrics

| Metric Type | Pattern | Normalized Format | Examples |
|-------------|---------|-------------------|----------|
| Subscription Model | Monthly subscription | `cost_model: subscription_monthly` | Monthly NaaS |
| OpEx vs CapEx | CapEx → OpEx | `cost_model: opex` | CapEx eliminated |
| Energy Cost | Less power with more devices | `energy_efficiency: true` | Less power, double APs |

---

## Metric Normalization Rules

### Rule 1: Percentage Normalization

**Input patterns**:
- "100% reduction"
- "completely eliminated"
- "all tickets gone"

**Normalized output**: `metric_name: 100%`

### Rule 2: Factor Normalization

**Input patterns**:
- "2x increase"
- "two times"
- "doubled"
- "twice as much"

**Normalized output**: `metric_name: 2x`

### Rule 3: Duration Normalization

**Input patterns**:
- "30 minutes"
- "30 min"
- "half an hour"

**Normalized output**: `metric_name: 30min`

### Rule 4: Count Normalization

**Input patterns**:
- "26,500 students"
- "26500 users"

**Normalized output**: `metric_name: 26500`

### Rule 5: Boolean Normalization

**Input patterns**:
- "all learners connected"
- "100% success"
- "completely"
- "fully"

**Normalized output**: `metric_name: 100%` or `metric_name: true`

---

## Metric × Industry Typical Values

| Industry | Typical Reduction Metrics | Typical Increase Metrics | Typical Time Metrics | Typical Coverage Metrics |
|----------|--------------------------|-------------------------|--------------------|-------------------------|
| Education | fault_ticket: 100% | coverage: 2x | deploy: 30min | users: 26000+, sites: 60+ |
| Healthcare | incident: 50% | efficiency: 30% | response: faster | sites: regional network |
| Hospitality | manual_work: hours→min | speed: 2x | resolution: faster | sites: national offices |
| Manufacturing | fault: 80%, downtime: 50% | efficiency: 50% | deploy: fast | sites: production facilities |
| IT Services | ticket: 70% | speed: 3x | resolution: minutes | clients: multiple |

---

## Metric Validation Checklist

- [ ] All quantified metrics are extracted
- [ ] Metrics are normalized to standard format
- [ ] Percentage values are in 0-100% range
- [ ] Factor values are reasonable (1x-10x typical)
- [ ] Duration values are reasonable (minutes to hours)
- [ ] Count values are extracted from scale descriptions
- [ ] Original expressions are preserved for traceability

---

## Metric Value Ranges Reference

| Metric Type | Typical Range | Typical Values | Notes |
|-------------|----------------|----------------|-------|
| fault_ticket_reduction | 50% - 100% | 100%, 80%, 70% | Education often 100% |
| coverage_increase | 1.5x - 3x | 2x, 1.5x | Wi-Fi capacity |
| deploy_time | 10min - 2hr | 30min, 1hr | Network deployment |
| user_count | 1000 - 50000 | 26500, 31000 | Education large scale |
| site_count | 1 - 100+ | 67, 10 | Distributed sites |
| uptime | 99% - 99.99% | 99.9%, 99.99% | Service availability |

---

## Metric-to-Business Driver Mapping

| Metric Type | Primary Business Driver | Secondary Driver |
|-------------|------------------------|------------------|
| fault_ticket_reduction | Efficiency Improvement | Cost Optimization |
| coverage_increase | User Experience | Efficiency Improvement |
| deploy_time | Efficiency Improvement | Cost Optimization |
| user_count | User Experience | Scale Capability |
| uptime | User Experience | Security/Compliance |
| cost_model: subscription | Cost Optimization | Innovation Transformation |
| energy_efficiency | Sustainability | Cost Optimization |