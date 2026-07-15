# Learning Engine

## Purpose

Turn completed work into concise, task-specific engineering understanding.

## Responsibilities

- explain what was chosen, why, and what trade-offs were accepted
- identify one useful next learning step

## Inputs

- final implementation summary
- decisions, trade-offs, and review findings

## Outputs

- Learning Summary

## Activation Criteria

Use at the end of every meaningful task.

## Dependencies

- Review Engine

## Non-Goals

- unrelated lessons or replacing practical review

## Workflow

```text
Completed task -> decisions and review findings -> Learning Summary
```

## Quality Gates

- Learning is grounded in the actual decision and does not introduce new scope.

## Review Checklist

- Is the lesson concise and likely to improve future engineering judgment?

## Extension Rules

- Keep extensions task-linked and proportionate to the developer's stated needs.

## Example

Explain why JWT access tokens simplify stateless APIs but make revocation a deliberate product decision.
