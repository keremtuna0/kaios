# Engineering Contract: JWT Authentication (Go Fiber + PostgreSQL)

Artifact produced after Context Loader and Module Registry. Implementation
should not begin until this contract is agreed.

## Contract Type

Task Contract

## Mode

Development Mode

## Problem

Build a JWT authentication capability for a Go Fiber API backed by PostgreSQL
so users can register, log in, and access protected routes securely.

## Context Summary

See `examples/context-summaries/jwt-auth-context-summary.md`.

## Selected Modules

See `examples/module-resolutions/jwt-auth-module-resolution.md`.

## Assumptions (If Developer Defers Unknowns)

- Registration and login are both in scope.
- Email is the unique user identifier.
- Access token only for v1; refresh tokens are out of scope.
- No roles beyond authenticated vs unauthenticated for v1.
- Secrets come from environment configuration.
- Local development with Docker-compatible PostgreSQL is acceptable.

## Scope

### In Scope

- user registration
- user login
- password hashing
- JWT access token creation
- authenticated route middleware
- PostgreSQL persistence
- input validation and safe error handling
- tests for main success and failure paths

### Out Of Scope

- OAuth or social login
- multi-factor authentication
- admin or role-based permission system
- email verification
- account recovery
- refresh token rotation (unless explicitly added later)

## Requirements

### Functional Requirements

- A user can register with valid credentials.
- A user can log in with valid credentials.
- Invalid credentials are rejected safely.
- A JWT access token is issued after successful login.
- Protected routes reject missing, invalid, or expired tokens.

### Non-Functional Requirements

| Area | Expectation |
| --- | --- |
| Security | Strong password hashing; no plain-text secrets; safe errors |
| Performance | Identify hot paths; index lookup fields; avoid unnecessary DB work |
| Maintainability | Clear module boundaries; testable services |
| Testability | Unit tests for core logic; integration tests where practical |
| Scalability | Stateless token validation acceptable for v1 API scope |

## Acceptance Criteria

- [ ] Registration succeeds with valid input.
- [ ] Passwords are never stored in plain text.
- [ ] Login succeeds with valid credentials.
- [ ] Invalid credentials return safe, non-enumerating errors where practical.
- [ ] JWT access token is issued after login.
- [ ] Protected routes reject missing or invalid tokens.
- [ ] JWT secret is read from configuration, not hardcoded.
- [ ] Tests cover registration, login, token validation, and key failure cases.

## Architecture Constraints

- Separate HTTP handlers from auth use-case logic.
- Isolate PostgreSQL access behind a repository boundary.
- Extract password hashing and token creation behind small interfaces.
- Keep configuration outside business logic.

Recommended structure:

```text
HTTP Handlers
-> Auth Service / Use Cases
-> User Repository
-> PostgreSQL

Auth Service
-> Password Hasher
-> Token Service
-> Config
```

Suggested packages:

- `auth/handler`
- `auth/service`
- `auth/repository`
- `auth/token`
- `auth/password`
- `config`
- `middleware`

## Implementation Rules

- Code is the last step; planning and trade-offs come first.
- Prefer simple modules over premature abstraction.
- Use parameterized queries or a safe query builder.
- Do not log passwords or tokens.
- Document architectural decisions explicitly.

## Testing Expectations

### Unit

- password hashing and comparison
- token creation and validation
- auth service success paths
- auth service failure paths

### Integration

- repository behavior against PostgreSQL when available
- handler behavior with Fiber test requests

### Failure Cases

- duplicate email
- invalid password
- missing token
- expired token
- malformed token

## Review Checklist

- [ ] Architecture boundaries are clear
- [ ] Naming and module cohesion are sensible
- [ ] SOLID and separation of concerns are respected
- [ ] Security requirements are met
- [ ] Performance risks are identified
- [ ] Tests cover critical paths
- [ ] Reusable pieces are not over-engineered

## Learning Goals

After this task, the developer should understand:

- why authentication is a design problem, not just routing
- JWT vs session trade-offs
- when a repository boundary earns its place
- why acceptance criteria must exist before coding

## Contract Status

**Agreed** — ready for architecture trade-off review, then implementation.

If scope changes (for example, refresh tokens or roles), update this contract
before writing code.
