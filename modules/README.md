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

Each registered module follows
[`templates/module-template.md`](../templates/module-template.md) and defines:

- purpose
- responsibilities
- inputs
- outputs
- activation criteria
- dependencies
- non-goals
- workflow
- quality gates
- review checklist
- extension rules
- example

`module-registry.md` is the authoritative Module Registry contract;
`registry.md` is a compatibility pointer for older references.
