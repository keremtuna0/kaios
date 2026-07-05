# Walkthrough: JWT Authentication With Go Fiber And PostgreSQL

This walkthrough shows how KAIOS guides engineering work before code.

## User Request

```text
I want to build a JWT authentication system using Go Fiber and PostgreSQL.
```

## Step 1: Context Loader

KAIOS extracts facts:

- Domain: authentication
- Language: Go
- Framework: Fiber
- Database: PostgreSQL
- Task type: feature development
- Risk level: high
- Reason for risk: authentication affects identity, secrets, user data, and
  authorization boundaries

KAIOS identifies unknowns:

- Is registration required?
- Are refresh tokens required?
- What user fields exist?
- Is email verification required?
- Are roles or permissions required?
- How will secrets be configured?
- What deployment environment is expected?

## Step 2: Module Registry

Selected modules:

| Module | Reason |
| --- | --- |
| Core | Preserve KAIOS workflow and quality rules |
| Context Loader | Extract task context |
| Module Registry | Select relevant modules |
| Engineering Contract | Define scope and acceptance criteria |
| Architecture | Design boundaries |
| Pattern Engine | Decide whether repository/token service abstractions are useful |
| Security Engine | Authentication is security-sensitive |
| Testing Engine | Auth requires success and failure coverage |
| Performance Engine | Login and token validation may affect hot paths |
| Review Engine | Self-review before completion |
| Learning Engine | Convert decisions into learning |

Skipped modules:

| Module | Reason |
| --- | --- |
| Debug Engine | No bug or failure is being investigated yet |

## Step 3: Engineering Contract

### Scope

In scope:

- user registration
- user login
- password hashing
- JWT access token creation
- authenticated route middleware
- PostgreSQL persistence
- validation and error handling
- tests for main success and failure paths

Out of scope until explicitly requested:

- OAuth
- social login
- multi-factor authentication
- admin role system
- email verification
- account recovery

### Acceptance Criteria

- A user can register with valid credentials.
- Passwords are never stored in plain text.
- A user can login with valid credentials.
- Invalid credentials return safe errors.
- A JWT access token is issued after login.
- Protected routes reject missing or invalid tokens.
- Secrets are read from configuration, not hardcoded.
- Tests cover registration, login, token validation, and failure cases.

## Step 4: Architecture

Recommended boundaries:

```text
HTTP Handlers
-> Auth Use Cases / Service
-> User Repository
-> PostgreSQL

Auth Service
-> Password Hasher
-> Token Service
-> Config
```

Suggested modules:

- `auth/handler`
- `auth/service`
- `auth/repository`
- `auth/token`
- `auth/password`
- `config`
- `middleware`

## Step 5: Trade-Offs

### JWT-only vs session-based auth

JWT is a good fit for stateless APIs, but token revocation is harder.

Session-based auth makes revocation easier, but requires server-side session
storage.

Decision: JWT access token is acceptable for a simple API. Add refresh token
strategy only if the product needs long-lived sessions.

### Direct database access vs repository

Direct database access is simpler for tiny applications.

Repository abstraction improves testability and isolates persistence details.

Decision: Use a repository boundary because authentication is core domain logic
and testability matters.

### Single auth service vs smaller services

A single auth service is simpler.

Separate token and password services improve reuse and security review.

Decision: Keep one auth use-case service, but extract password hashing and token
creation behind small interfaces.

## Step 6: Testing Strategy

Unit tests:

- password hashing and comparison
- token creation and validation
- auth service success paths
- auth service failure paths

Integration tests:

- repository with PostgreSQL test database when available
- handler behavior with Fiber test requests

Failure cases:

- duplicate email
- invalid password
- missing token
- expired token
- malformed token

## Step 7: Security Review

Security requirements:

- hash passwords with a strong algorithm
- never log passwords or tokens
- validate input
- use parameterized SQL or safe query builder
- keep JWT secret outside source code
- use token expiration
- return safe error messages
- consider rate limiting for login

## Step 8: Performance Review

Likely concerns:

- index users by email
- avoid unnecessary database calls in middleware
- keep token validation stateless when possible
- measure before adding caching

## Step 9: Learning Summary

This feature teaches:

- authentication is architecture and security work, not just endpoint creation
- repository boundaries improve testability when persistence matters
- JWT simplifies stateless APIs but complicates revocation
- password hashing, secret handling, and safe errors are non-negotiable
- senior engineers define acceptance criteria before implementation
