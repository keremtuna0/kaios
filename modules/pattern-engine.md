# Pattern Engine

## Purpose

Recommend a design pattern only when it removes demonstrated complexity.

## Responsibilities

- compare pattern and simpler alternatives
- record accepted and rejected patterns with trade-offs

## Inputs

- Architecture Decision
- change points and dependency boundaries

## Outputs

- Pattern Decision

## Activation Criteria

Use for extension points, behavior variants, repeated construction, or important dependency boundaries.

## Dependencies

- Architecture Module

## Non-Goals

- forcing patterns or hiding business logic behind abstractions

## Workflow

```text
Change point -> compare simple and patterned designs -> Pattern Decision
```

## Quality Gates

- The pattern solves a named problem better than the simpler option.

## Review Checklist

- Will a future maintainer understand why this pattern exists?

## Extension Rules

- Do not add a catalog; record task-specific evidence instead.

## Example

Use small password and token interfaces; do not add factories for one implementation.
