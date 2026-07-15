# Engineering Contract Module

## Purpose

Turn task context into explicit, testable expectations before implementation.

## Responsibilities

- define scope, acceptance criteria, quality requirements, and learning goals
- connect selected modules to review expectations
- make assumptions and architecture constraints explicit

## Inputs

- Context Summary
- Module Resolution
- user constraints, project constraints, and development mode

## Outputs

- Engineering Contract
- acceptance criteria, architecture constraints, review checklist, and learning goals

## Activation Criteria

Use before meaningful implementation, especially features, fixes, refactors, and security-sensitive work.

## Dependencies

- Core
- Context Loader
- Module Registry

## Non-Goals

- generating code or becoming a runtime configuration format

## Workflow

```text
Context + resolution -> explicit scope and criteria -> Engineering Contract
```

## Quality Gates

- Scope, assumptions, quality requirements, and acceptance criteria are explicit and testable.

## Review Checklist

- Is scope explicit, are assumptions visible, and are acceptance criteria testable?
- Are selected modules connected to review expectations and is learning included?

## Extension Rules

- Extensions may add domain sections such as authentication, payment, deployment,
  or data-privacy requirements, but must retain scope, acceptance criteria,
  quality requirements, review checklist, and learning goals.

## Example

Exclude OAuth from an initial JWT contract while requiring safe credential errors.
