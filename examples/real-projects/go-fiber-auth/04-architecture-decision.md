# 04 — Architecture Decision

## Decision

Use a thin Fiber handler calling an auth use-case service. Keep PostgreSQL access behind a small user repository; use narrow password and token collaborators; read token settings from configuration.

```text
Fiber handler -> Auth service -> User repository -> PostgreSQL
                    |-> Password hasher
                    |-> Token signer/verifier
Middleware -> Token verifier -> request identity
```

## Alternatives and Trade-offs

| Alternative | Decision |
| --- | --- |
| Handler directly queries SQL and signs tokens | Rejected: mixes HTTP, persistence, and security policy; difficult to test. |
| Full clean-architecture framework, factories, and event bus | Rejected: adds ceremony without a current extension need. |
| Small service and narrow collaborators | Chosen: clear, testable boundaries proportional to risk. |
| Session authentication | Rejected for scope: easier revocation but requires session storage; JWT is the stated API goal. |

Small repository, password, and token interfaces are justified by testing and security boundaries. Generic repositories, factories, and service locators are not: they solve no present problem. Auth owns use cases; persistence owns user storage; middleware owns HTTP enforcement; config owns environment mapping.
