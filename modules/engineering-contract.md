# Engineering Contract Module

## Purpose

The Engineering Contract module defines expectations before planning and
implementation begin.

## Responsibilities

- convert context into explicit scope
- define acceptance criteria
- define quality requirements
- connect selected modules to review expectations
- prevent hidden assumptions

## Dependencies

- Core
- Context Loader
- Module Registry

## Inputs

- Context Summary
- Module Resolution
- user constraints
- project constraints
- development mode

## Outputs

- Engineering Contract
- acceptance criteria
- architecture constraints
- review checklist
- learning goals

## Activation Rules

Use before implementation for:

- new projects
- new features
- bug fixes
- refactors
- architecture decisions
- security-sensitive work

## Extension Rules

Extensions may add domain-specific contract sections, such as authentication,
payment, deployment, or data privacy requirements.

Extensions must not remove the core contract fields: scope, acceptance criteria,
quality requirements, review checklist, and learning goals.

## Non-Goals

- generating code
- replacing requirements discussion
- becoming a runtime configuration format

## Review Checklist

- Is scope explicit?
- Are assumptions visible?
- Are acceptance criteria testable?
- Are selected modules connected to review expectations?
- Is learning included?
