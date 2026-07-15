# Performance Engine

## Purpose

Identify likely bottlenecks and define a proportional measurement strategy.

## Responsibilities

- examine data access, external calls, load assumptions, and concurrency risks
- recommend measurable, simple mitigations

## Inputs

- Architecture Decision
- data access patterns, expected load, and external calls

## Outputs

- Performance Notes

## Activation Criteria

Use for data access, external services, large collections, concurrency, real-time work, or stated scale.

## Dependencies

- Architecture Module

## Non-Goals

- premature optimization or speculative micro-optimization

## Workflow

```text
Costly paths -> load assumptions and measures -> Performance Notes
```

## Quality Gates

- Recommendations name a bottleneck hypothesis and measurement.

## Review Checklist

- Are database and network costs visible and is the simplest strategy chosen?

## Extension Rules

- Do not prescribe caching without an observed or credible measured need.

## Example

Index user email and measure login latency before introducing a token cache.
