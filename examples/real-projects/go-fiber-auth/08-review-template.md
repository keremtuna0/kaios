# 08 — Review Template

## Contract and Scope

- [ ] Every acceptance criterion has evidence.
- [ ] Out-of-scope features were not silently added.
- [ ] Deferrals are documented with owner or follow-up.

## Boundaries and Security

- [ ] Handlers do not own persistence, hashing, or JWT policy.
- [ ] Passwords, tokens, and secrets are not logged or hardcoded.
- [ ] Invalid token behavior, validation, safe errors, and rate-limit ownership are addressed.
- [ ] Email lookup is indexed; caching was not added without measurement.

## Testing and Readiness

- [ ] Unit, handler, middleware, and required integration tests pass.
- [ ] Failure paths receive the same care as success paths.
- [ ] Existing project checks were run and recorded.
- [ ] Learning Summary is complete.

Any unchecked required item means the feature is not ready.
