# Example First Session: JWT Authentication

This example shows a realistic first KAIOS conversation for the task:

```text
I want to build a JWT authentication system using Go Fiber and PostgreSQL.
```

The focus is the **engineering workflow**, not application code.

Related artifact files:

- `examples/context-summaries/jwt-auth-context-summary.md`
- `examples/module-resolutions/jwt-auth-module-resolution.md`
- `examples/contracts/jwt-auth-engineering-contract.md`

For a longer walkthrough, see
`docs/WALKTHROUGHS/jwt-auth-go-fiber-postgres.md`.

---

## 1. Developer Opens The Session

**Developer:**

```text
Use KAIOS v0.1.

Mode: Development Mode

Task:
I want to build a JWT authentication system using Go Fiber and PostgreSQL.

Context:
- New API project
- I want production-aware design
- I want to understand the architecture, not just get code

Run Context Loader, Module Registry, and Engineering Contract before
implementation.
```

**KAIOS:**

Understood. I will follow the KAIOS workflow and will not implement until the
Engineering Contract is clear.

---

## 2. Context Loader

**KAIOS — Context Summary**

**Facts extracted:**

- Domain: authentication
- Language: Go
- Framework: Fiber
- Database: PostgreSQL
- Task type: feature development
- Risk level: **high** (identity, secrets, authorization boundaries)

**Assumptions:**

- HTTP API context
- Password-based auth unless you specify otherwise

**Missing context — please confirm or defer:**

1. Registration required, or login only?
2. Refresh tokens required?
3. Unique identifier: email, username, or both?
4. Roles or permissions needed now?
5. How will secrets be configured?
6. Target deployment environment?

**Recommended mode:** Development Mode (or Bootstrap Mode if this is the first
slice of a greenfield project).

**Developer:**

```text
Use sensible defaults for a learning API:
registration and login, email as unique field, access token only, no roles yet,
secrets from env vars.
```

**KAIOS:**

Recorded as explicit contract assumptions. Proceeding to Module Registry.

Full artifact: `examples/context-summaries/jwt-auth-context-summary.md`

---

## 3. Module Registry

**KAIOS — Module Resolution**

**Selected modules:**

| Module | Why |
| --- | --- |
| Core | Preserve workflow and quality bar |
| Context Loader | Task understood |
| Module Registry | Module selection |
| Engineering Contract | High-risk feature needs explicit scope |
| Architecture | Boundaries and structure |
| Pattern Engine | Repository/service boundaries |
| Security Engine | Auth is security-sensitive |
| Testing Engine | Success and failure paths matter |
| Performance Engine | Login and middleware are hot paths |
| Review Engine | Self-review before done |
| Learning Engine | Teach throughout |

**Skipped:**

| Module | Why |
| --- | --- |
| Debug Engine | No active bug investigation |

Full artifact: `examples/module-resolutions/jwt-auth-module-resolution.md`

---

## 4. Engineering Contract

**KAIOS — Engineering Contract (summary)**

**In scope:**

- registration, login, password hashing, JWT access token, auth middleware,
  PostgreSQL persistence, validation, tests

**Out of scope (v1):**

- OAuth, MFA, roles, email verification, refresh tokens

**Acceptance criteria (sample):**

- passwords never stored in plain text
- valid login returns JWT
- protected routes reject invalid tokens
- secrets from configuration
- tests cover success and key failure paths

**Developer:**

```text
Agreed. Proceed to architecture and trade-offs. Still no code.
```

Full artifact: `examples/contracts/jwt-auth-engineering-contract.md`

---

## 5. Architecture Plan

**KAIOS — Architecture Decision**

Recommended boundaries:

```text
HTTP Handlers
-> Auth Service
-> User Repository
-> PostgreSQL

Auth Service
-> Password Hasher
-> Token Service
-> Config
```

Suggested modules:

- `auth/handler`, `auth/service`, `auth/repository`, `auth/token`,
  `auth/password`, `config`, `middleware`

**Why:**

- handlers stay thin
- business rules stay testable
- persistence can be mocked via repository interface
- security-sensitive operations stay isolated

---

## 6. Trade-Off Analysis

**KAIOS — Trade-off Analysis**

### JWT vs session-based auth

| Option | Benefit | Cost |
| --- | --- | --- |
| JWT access token | Stateless API-friendly | Harder revocation story |
| Server session | Easier revocation | Requires session storage |

**Decision:** JWT access token for v1 API scope. Revisit refresh tokens only if
long-lived sessions become a requirement.

### Direct DB access vs repository

| Option | Benefit | Cost |
| --- | --- | --- |
| Direct SQL in handlers | Less code initially | Hard to test; mixed concerns |
| Repository boundary | Testability; clear persistence edge | Small extra abstraction |

**Decision:** Repository boundary — auth is core domain logic and testability
matters.

### Monolithic auth service vs split services

**Decision:** One auth use-case service with small interfaces for password
hashing and token creation. Avoid premature micro-service split.

---

## 7. Testing Plan

**KAIOS — Test Plan**

**Unit tests:**

- password hash/compare
- token create/validate
- auth service success and failure paths

**Integration tests:**

- repository against PostgreSQL (when available)
- Fiber handler requests for register/login/protected route

**Failure cases:**

- duplicate email, invalid password, missing token, expired token, malformed
  token

---

## 8. Security And Performance Notes

**KAIOS — Security Notes**

- use strong password hashing
- never log passwords or tokens
- validate input; use parameterized SQL
- configure JWT secret externally
- set token expiration
- return safe errors; consider login rate limiting later

**KAIOS — Performance Notes**

- index users by email
- avoid unnecessary DB calls in middleware
- keep token validation stateless for v1
- measure before adding caching

---

## 9. Review (Before Calling The Task Done)

**KAIOS — Review Report (checklist)**

After implementation, verify:

- [ ] Matches Engineering Contract scope
- [ ] Boundaries match architecture decision
- [ ] Security notes addressed
- [ ] Tests cover acceptance criteria
- [ ] No secrets in source code
- [ ] Errors are safe and consistent
- [ ] No unnecessary abstractions added

**Developer:**

```text
Run the review against the contract before we call this done.
```

---

## 10. Learning Summary

**KAIOS — Learning Summary**

What this task teaches:

1. **Authentication is systems design** — endpoints are the last layer, not the
   first decision.
2. **Contracts prevent vague AI output** — scope and acceptance criteria turn
   "build auth" into engineering work.
3. **JWT trades simplicity for revocation** — good for stateless APIs, but know
   the limit.
4. **Repository boundaries earn their place** when persistence and testability
   matter.
5. **Security requirements are part of design** — hashing, secrets, validation,
   and safe errors are non-negotiable.

---

## Session Complete

The developer has:

1. Loaded KAIOS
2. Run Context Loader
3. Resolved modules
4. Agreed an Engineering Contract
5. Reviewed architecture and trade-offs
6. Defined testing, security, and performance expectations
7. Received a review framework and learning summary

**Only now** would KAIOS proceed to implementation — with the contract as the
source of truth.

---

## Try It Yourself

1. Read `QUICKSTART.md`
2. Load `assistant-prompts/cursor.md` (or your assistant)
3. Paste the developer message from Section 1
4. Walk through the workflow before asking for code
