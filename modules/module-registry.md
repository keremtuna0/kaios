# Module Registry

## Purpose

Select the KAIOS guidance modules relevant to a task; it does not execute them.

## Responsibilities

- select always-on and risk-based modules
- explain selected and intentionally skipped modules
- state the expected output of each selected module

## Inputs

- Context Summary
- task type, risk, complexity, mode, and constraints

## Outputs

- Module Resolution
- selected modules with reason and expected output; intentionally skipped modules with reason

## Activation Criteria

Use after Context Loader produces a Context Summary.

## Dependencies

- Core
- Context Loader

## Non-Goals

- implementing module behavior
- creating autonomous agents or forcing every module into every task

## Workflow

```text
Context Summary -> select always-on modules -> evaluate task and risk triggers
-> select specialized modules -> document skips -> Module Resolution
```

### Always-On Modules

Core, Context Loader, Module Registry, Engineering Contract, Review Engine, and
Learning Engine are always selected for a meaningful KAIOS task.

### Risk-Based Activation

- **Security:** authentication, authorization, user data, secrets, files,
  external APIs, persistence, payments, or deployment.
- **Testing:** every implementation task.
- **Performance:** data access, external services, large collections,
  concurrency, real-time behavior, or expected scale.
- **Pattern:** extension points, behavior variants, dependency boundaries, or
  repeated construction logic.
- **Debug:** bugs, failing tests, unexpected behavior, or incidents.

### Module Resolution Shape

```text
selected_modules:
  - module:
    reason:
    expected_output:
skipped_modules:
  - module:
    reason:
```

## Quality Gates

- Every selected and skipped module has a task-specific reason and selected modules name their expected output.

## Review Checklist

- Does selection match task risk, avoid unnecessary modules, and explain skips clearly?

## Extension Rules

- New modules must own a distinct responsibility, declare dependencies, inputs,
  outputs, activation criteria, non-goals, extension rules, and review criteria,
  and avoid overlap without explicit justification.

## Example

Select Security and Testing for JWT authentication; skip Debug when no defect is investigated.
