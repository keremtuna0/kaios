# 03 — Engineering Contract

## Goal

Add maintainable JWT access-token authentication to the existing API.

## Scope

In scope: registration, login, password hashing, user persistence, short-lived JWTs, middleware, protected-route proof, validation, safe errors, and tests.

Out of scope: OAuth, MFA, verification, recovery, sessions, refresh tokens, role administration, and deployment.

## Acceptance Criteria

- Valid registration creates a user without a plaintext password.
- Duplicate registration and invalid credentials return safe stable errors.
- Valid login returns a signed, expiring access token.
- Missing, malformed, expired, and invalid tokens are rejected.
- Secrets are configured outside source control and never logged.
- Email lookup is parameterized and indexed.
- Tests demonstrate listed behavior and failures.

## Ready-to-Implement Gate

Resolve or explicitly defer Context Summary unknowns, then review architecture, threat model, implementation plan, and test strategy.
