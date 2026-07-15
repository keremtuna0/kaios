# 07 — Test Strategy

| Level | Coverage | Evidence |
| --- | --- | --- |
| Unit | Hash/compare, token creation/verification, use-case paths | Deterministic tests with collaborator fakes |
| Handler | Validation, status mapping, safe response shape | Fiber request/response tests |
| Middleware | Missing, malformed, invalid, expired, and valid tokens | Protected-route request tests |
| Integration | PostgreSQL uniqueness and create/find behavior | Isolated project integration harness |

Required cases: valid/invalid/duplicate registration; valid, unknown-user, and wrong-password login; signed, expired, malformed, and wrong-signature tokens; valid identity reaching a protected route; sensitive values absent from errors and logs when test tooling permits.

Every contract criterion needs passing evidence, documented exception, or a blocking issue. Coverage percentage alone is not readiness.
