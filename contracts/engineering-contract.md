# Engineering Contract

The Engineering Contract is the agreement that defines what good means before
implementation begins.

It connects user intent, project constraints, selected KAIOS modules, acceptance
criteria, and review expectations.

## Purpose

The Engineering Contract prevents vague AI-assisted development.

It ensures the developer and AI agree on:

- scope
- requirements
- constraints
- architecture expectations
- testing expectations
- security expectations
- performance expectations
- learning goals

## Position In The Workflow

```text
User Request
-> Context Loader
-> Module Registry
-> Engineering Contract
-> Planning
-> Implementation
-> Review
-> Learning Summary
```

## Inputs

- Context Summary
- Module Resolution
- project constraints
- user requirements
- known risks
- development mode
- learning preference

## Outputs

- task scope
- out-of-scope items
- acceptance criteria
- selected modules
- architecture constraints
- implementation rules
- test expectations
- review checklist
- learning goals

## Contract Types

### Project Contract

Used in Bootstrap Mode. Defines project-wide rules, architecture direction, and
quality expectations.

### Task Contract

Used in Development Mode. Defines requirements and acceptance criteria for one
feature or change.

### Maintenance Contract

Used in Maintenance Mode. Defines reproduction evidence, root cause goals,
change boundaries, and regression expectations.

## Integration With Modules

The Engineering Contract consumes Context Loader and Module Registry outputs.

It informs:

- Architecture Module
- Pattern Engine
- Security Engine
- Testing Engine
- Performance Engine
- Review Engine
- Learning Engine

## Non-Goals

The Engineering Contract is not:

- a legal contract
- a runtime configuration file
- an automation script
- a replacement for developer judgment

It is an engineering alignment artifact.
