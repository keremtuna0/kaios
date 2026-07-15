# 05 — Threat Model

| Asset / path | Threat | Required mitigation |
| --- | --- | --- |
| Registration and login | Weak or malformed credentials | Validate input and define password policy. |
| Password storage | Credential disclosure | Use a modern adaptive hash; never log or return hashes. |
| Login endpoint | Credential stuffing | Define rate-limit ownership and use generic invalid-credential errors. |
| JWT signing | Leaked or weak secret | Load strong secret from deployment config; fail safely when absent; never log it. |
| Protected routes | Forged or expired token | Verify signature, allowed algorithm, expiry, and claims before setting identity. |
| PostgreSQL lookup | Injection or duplicate identity | Parameterized queries; unique identity constraint and email index. |
| API errors/logs | Enumeration or token exposure | Use safe stable errors; redact passwords, headers, and tokens. |

Refresh-token rotation, revocation, key rotation, MFA, and recovery are explicit deferrals requiring product and operational decisions. No implementation is ready if secret handling, validation, hashing, or token checks lack testable evidence.
