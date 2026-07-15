# Debug Engine

## Purpose

Guide evidence-based root-cause analysis for incorrect behavior.

## Responsibilities

- separate observations from hypotheses
- define reproduction, investigation, fix, and regression-test steps

## Inputs

- observed and expected behavior
- reproduction steps, logs, and recent changes

## Outputs

- Debug Plan
- likely root cause and regression-test recommendation

## Activation Criteria

Use for bugs, failing tests, unexpected behavior, and incidents.

## Dependencies

- Core

## Non-Goals

- guessing fixes or changing unrelated code

## Workflow

```text
Evidence -> reproducible hypotheses -> root cause and targeted fix plan
```

## Quality Gates

- A hypothesis is testable against evidence before a fix is proposed.

## Review Checklist

- Is the bug reproducible and is a regression test planned?

## Extension Rules

- Add diagnostics only when they reduce a specific uncertainty.

## Example

Reproduce an expired-token failure before changing middleware validation.
