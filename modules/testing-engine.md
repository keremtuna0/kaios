# Testing Engine

## Responsibility

The Testing Engine defines what should be tested and at which level.

## Inputs

- requirements
- implementation plan
- risk level
- architecture boundaries

## Outputs

- unit test scope
- integration test scope
- edge cases
- failure scenarios
- test gaps

## Activation Criteria

Use for every implementation task.

## Non-Goals

- chasing 100 percent coverage as a vanity metric
- testing implementation details instead of behavior
- adding brittle tests that block refactoring

## Review Checklist

- Do tests cover the important behavior?
- Are failure paths represented?
- Are boundaries tested at the right level?
- Can implementation change without breaking unrelated tests?
