# Testing Engine

## Purpose

Define behavior-focused testing at the appropriate boundaries.

## Responsibilities

- identify unit, integration, edge-case, and failure-path coverage
- record meaningful gaps and readiness evidence

## Inputs

- Engineering Contract
- implementation plan, risk level, and architecture boundaries

## Outputs

- Test Strategy

## Activation Criteria

Use for every implementation task.

## Dependencies

- Engineering Contract
- Architecture Module

## Non-Goals

- vanity coverage targets, brittle implementation-detail tests

## Workflow

```text
Acceptance criteria -> test levels and failures -> Test Strategy
```

## Quality Gates

- Acceptance criteria have observable test evidence or an explicit justification.

## Review Checklist

- Are important behavior and failure paths tested at the right boundary?

## Extension Rules

- Add test categories only when they protect a distinct risk.

## Example

Test valid and invalid login, expiry, missing token, and duplicate registration.
