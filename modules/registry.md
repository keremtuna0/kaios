# Scalable Module Registry Design

The Module Registry selects which KAIOS modules should participate in a task.

It recommends modules. It does not execute autonomous agents.

## Registry Entry Shape

Each module should define:

```text
id:
purpose:
responsibilities:
dependencies:
inputs:
outputs:
activation_rules:
non_goals:
extension_rules:
review_checklist:
```

## Resolution Workflow

```text
Context Summary
-> classify task type
-> assess risk level
-> select always-on modules
-> select risk-based modules
-> explain skipped modules
-> produce Module Resolution
```

## Always-On Modules

- Core
- Context Loader
- Module Registry
- Engineering Contract
- Review Engine
- Learning Engine

## Risk-Based Modules

Security Engine activates when work touches:

- authentication
- authorization
- user data
- secrets
- files
- external APIs
- persistence

Testing Engine activates for all implementation work.

Performance Engine activates when work touches:

- data access
- external services
- large collections
- real-time flows
- concurrency

Pattern Engine activates when work includes:

- multiple implementations of behavior
- extension points
- dependency boundaries
- repeated construction logic

Debug Engine activates when work includes:

- failing tests
- bugs
- unexpected behavior
- incidents

## Module Resolution Output

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
- declare outputs
- include activation rules
- avoid overlapping an existing module without justification
