# Review Engine

## Purpose

Critique completed work against its contract before it is considered ready.

## Responsibilities

- review architecture, quality, security, performance, and testability
- distinguish required fixes from follow-up improvements

## Inputs

- Engineering Contract
- implementation summary, tests, and architecture decision

## Outputs

- Review Report

## Activation Criteria

Use before every meaningful task is completed.

## Dependencies

- Engineering Contract

## Non-Goals

- rewriting everything automatically or demanding theoretical perfection

## Workflow

```text
Contract + evidence -> readiness checks -> Review Report
```

## Quality Gates

- Every acceptance criterion is satisfied, deferred, or explicitly blocked.

## Review Checklist

- Are boundaries, failures, tests, and security/performance risks addressed?

## Extension Rules

- Add review lenses only when they have a named owner and decision outcome.

## Example

Reject readiness if protected-route failures are untested or JWT secrets can be logged.
