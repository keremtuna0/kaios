# 06 — Implementation Plan

This plan describes work order and boundaries; it intentionally contains no production implementation code.

1. Resolve identity field, password policy, token lifetime, claims, and configuration source.
2. Review existing Fiber routes, errors, configuration, migrations, and PostgreSQL conventions.
3. Define create-user and find-by-identity persistence operations backed by a unique indexed identity field.
4. Define small password and JWT signer/verifier collaborators.
5. Implement auth use cases that map expected domain failures to safe outcomes.
6. Add Fiber handlers and middleware that translate HTTP only.
7. Add tests from [the test strategy](07-test-strategy.md).
8. Run [the review template](08-review-template.md) and complete learning before readiness.

## Performance Notes

The initial design needs one indexed user lookup per login. JWT verification remains local and stateless. Measure latency and query behavior before caching, jobs, or distributed coordination.
