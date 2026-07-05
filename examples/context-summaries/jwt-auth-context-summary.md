# Context Summary: JWT Authentication (Go Fiber + PostgreSQL)

Artifact produced by the **Context Loader** module before planning or
implementation begins.

## Source Request

```text
I want to build a JWT authentication system using Go Fiber and PostgreSQL.
```

## Extracted Facts

| Field | Value |
| --- | --- |
| Domain | Authentication / identity |
| Task type | Feature development |
| Language | Go |
| Framework | Fiber |
| Database | PostgreSQL |
| Project stage | Assumed new feature or greenfield API (confirm with developer) |
| Production expectation | Likely production-aware (auth is rarely throwaway) |

## Assumptions

- REST or HTTP API context.
- Password-based login is acceptable unless stated otherwise.
- Single-service application unless the developer says otherwise.
- Developer wants to understand architecture, not only receive code.

## Unknowns (Clarifying Questions)

Answer these before finalizing the Engineering Contract:

1. Is user registration required, or only login for existing users?
2. Are refresh tokens required, or is a short-lived access token enough?
3. What user fields exist (email, username, roles)?
4. Is email verification required?
5. Are roles or permissions required now?
6. How will secrets and configuration be managed (env vars, secret manager)?
7. What deployment environment is expected (local, Docker, cloud)?

## Task Classification

- **Complexity:** medium to high
- **Risk level:** high
- **Reason for risk:** authentication affects identity, secrets, user data, and
  authorization boundaries. Mistakes create security incidents.

## Recommended Development Mode

**Development Mode** — if adding auth to an existing API.

**Bootstrap Mode** — if this is the first foundational slice of a new project.

## Production Requirements

- Passwords must never be stored in plain text.
- Secrets must not be hardcoded.
- Input validation and safe error responses are required.
- Token expiration should be defined.
- Tests should cover success and failure paths.

## Learning Needs

The developer should understand:

- why auth is architecture and security work, not just endpoints
- JWT vs session trade-offs
- where to place boundaries (handler, service, repository)
- what acceptance criteria matter before coding

## Candidate Modules

Likely modules for Module Registry resolution:

- Core, Context Loader, Module Registry, Engineering Contract (always on)
- Architecture, Pattern Engine, Security Engine, Testing Engine,
  Performance Engine, Review Engine, Learning Engine

Likely skipped:

- Debug Engine (no active bug investigation)

## Context Summary Status

**Ready for Module Registry** after the developer confirms or defers the
unknowns above.

If the developer says "use sensible defaults for a learning API," document those
defaults explicitly in the Engineering Contract assumptions section.
