# Security Engine

## Purpose

Identify concrete security risks and practical mitigations appropriate to the task.

## Responsibilities

- analyze trust boundaries, data handling, and abuse paths
- define validation, access control, secrets, and dependency expectations

## Inputs

- Engineering Contract
- Architecture Decision
- data flow and external dependency context

## Outputs

- Security Notes or Threat Model

## Activation Criteria

Use for user data, auth, authorization, network boundaries, persistence, files, payments, secrets, or deployment.

## Dependencies

- Engineering Contract
- Architecture Module

## Non-Goals

- fear-driven architecture or replacement of a formal high-risk audit

## Workflow

```text
Trust boundaries -> threats and mitigations -> Security Notes
```

## Quality Gates

- Threats are tied to an asset, path, and mitigation.

## Review Checklist

- Are inputs, access rules, secrets, and sensitive errors handled safely?

## Extension Rules

- Add domain checks only when tied to a concrete threat model.

## Example

Require expiry, configuration-based secrets, safe errors, and login rate-limit consideration for JWT auth.
