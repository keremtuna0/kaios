# Performance Engine

## Responsibility

The Performance Engine identifies likely bottlenecks and scalability risks.

## Inputs

- architecture proposal
- data access patterns
- expected load
- external service calls
- concurrency model

## Outputs

- likely bottlenecks
- measurement strategy
- caching considerations
- database indexing notes
- concurrency risks

## Activation Criteria

Use when the task includes data access, loops over large data, external calls,
real-time behavior, background jobs, or expected scale.

## Non-Goals

- premature optimization
- speculative micro-optimizations
- making code harder to read without evidence

## Review Checklist

- Is the expected load understood?
- Are database and network costs visible?
- Are expensive paths measurable?
- Is the simplest acceptable performance strategy chosen?
