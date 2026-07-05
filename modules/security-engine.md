# Security Engine

## Responsibility

The Security Engine identifies security risks and recommends practical
mitigations appropriate to the task.

## Inputs

- requirements
- architecture proposal
- data flow
- authentication and authorization context
- external dependencies

## Outputs

- threat notes
- validation requirements
- access control concerns
- secrets handling guidance
- dependency and configuration risks

## Activation Criteria

Use when a task touches user data, authentication, authorization, network
boundaries, persistence, file handling, payments, secrets, or deployment.

## Non-Goals

- creating fear-driven architecture
- adding security tooling without a concrete risk
- replacing a formal security audit for high-risk systems

## Review Checklist

- Are inputs validated?
- Are access rules explicit?
- Are secrets kept out of source and logs?
- Are sensitive errors handled safely?
- Are dependency risks considered?
