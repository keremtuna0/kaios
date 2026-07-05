# KAIOS Modules

Modules are independent KAIOS capabilities. Each module must have a single
responsibility and communicate through explicit artifacts.

## v0.1 Modules

- `core`: project philosophy and mandatory workflow
- `context-loader`: task understanding
- `module-registry`: module selection
- `engineering-contract`: task expectations and acceptance criteria
- `architecture`: architecture reasoning
- `pattern-engine`: design pattern decisions
- `security-engine`: security risk analysis
- `testing-engine`: test strategy and coverage reasoning
- `performance-engine`: performance risk analysis
- `debug-engine`: debugging workflow and root cause analysis
- `review-engine`: self-review
- `learning-engine`: learning summary

## Module Contract

Each module should define:

- responsibility
- inputs
- outputs
- activation criteria
- non-goals
- review checklist
- extension rules
