# Architecture Module

## Purpose

Turn requirements into boundaries, data flow, alternatives, and trade-offs.

## Responsibilities

- propose structure and dependency direction
- choose and explain an approach

## Inputs

- Engineering Contract
- requirements, constraints, and selected modules

## Outputs

- Architecture Decision
- implementation boundaries

## Activation Criteria

Use when work affects feature, system, integration, module, or refactor structure.

## Dependencies

- Engineering Contract

## Non-Goals

- adding abstractions without a problem or replacing code review

## Workflow

```text
Contract -> alternatives and trade-offs -> Architecture Decision
```

## Quality Gates

- Responsibilities and dependency direction are clear.

## Review Checklist

- Is the selected structure simpler than the problem allows?

## Extension Rules

- Add a pattern only when a demonstrated change point needs it.

## Example

Keep HTTP handlers, auth use cases, persistence, token creation, and hashing at separate boundaries.
