# 01 — Context Summary

## What the Developer Provides

- Existing backend API using Go, Fiber, and PostgreSQL.
- Feature: registration, login, JWT access tokens, and a protected route.
- Development Mode; production-conscious but not over-engineered; learning enabled.

## Context Loader Extraction

| Field | Result |
| --- | --- |
| Task type | Feature development in an existing API |
| Risk | High: credentials, tokens, secrets, and user data |
| Facts | Go, Fiber, PostgreSQL, JWT access authentication |
| Assumptions | A users table and configuration convention exist or will be agreed |
| Unknowns | Password policy, token lifetime, refresh tokens, roles, secret source, rate-limit ownership |
| Candidate modules | Core, Context, Registry, Contract, Architecture, Pattern, Security, Testing, Performance, Review, Learning |

Confirm identity field, password policy, token lifetime, protected routes, and secret source before code. Unknowns are never silently implemented.
