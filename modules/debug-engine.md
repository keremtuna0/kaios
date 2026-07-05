# Debug Engine

## Responsibility

The Debug Engine guides systematic root cause analysis.

## Inputs

- observed behavior
- expected behavior
- reproduction steps
- logs or error messages
- recent changes

## Outputs

- hypotheses
- investigation plan
- likely root cause
- fix strategy
- regression test recommendation

## Activation Criteria

Use when the user reports a bug, failing test, unexpected behavior, or
production incident.

## Non-Goals

- guessing fixes before understanding evidence
- hiding uncertainty
- changing unrelated code

## Review Checklist

- Is the bug reproducible?
- Are facts separated from guesses?
- Is the fix targeted?
- Is a regression test proposed?
