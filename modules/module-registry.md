# Module Registry

## Purpose

The Module Registry determines which KAIOS modules should participate in a
task.

It recommends modules. It does not execute autonomous agents.

## Responsibilities

- read the Context Summary
- select always-on modules
- select risk-based modules
- explain why modules were selected
- explain why modules were skipped
- produce a Module Resolution artifact

## Dependencies

- Core
- Context Loader

## Inputs

- context summary
- task type
- risk level
- complexity level
- development mode
- known constraints

## Outputs

- selected modules
- reason each module is selected
- modules intentionally skipped
- expected output from each selected module

## Workflow

```text
Context Summary
-> select always-on modules
-> evaluate task type
-> evaluate risk triggers
-> select specialized modules
-> document skipped modules
-> produce Module Resolution
```

## Always-On Modules

- Core
- Context Loader
- Module Registry
- Engineering Contract
- Review Engine
- Learning Engine

## Risk-Based Activation

Security Engine activates for authentication, authorization, user data, secrets,
files, external APIs, persistence, payments, or deployment.

Testing Engine activates for every implementation task.

Performance Engine activates for data access, external services, large
collections, concurrency, real-time behavior, or expected scale.

Pattern Engine activates for extension points, multiple behavior variants,
dependency boundaries, or repeated construction logic.

Debug Engine activates for bugs, failing tests, unexpected behavior, and
incidents.

## Activation Rules

Use after the Context Loader produces a context summary.

## Non-Goals

- implementing module behavior
- forcing every module into every task
- creating autonomous sub-agents

## Module Resolution Shape

```text
selected_modules:
  - module:
    reason:
    expected_output:
skipped_modules:
  - module:
    reason:
```

## Extension Rules

New modules must:

- own a distinct responsibility
- declare dependencies
- declare inputs and outputs
- define activation rules
- define non-goals
- include review criteria
- avoid overlapping existing modules without explicit justification

## Review Checklist

- Were selected modules justified?
- Were unnecessary modules avoided?
- Does selection match task risk?
- Are skipped modules explained?
- Are module outputs clear?
