# Versioning Strategy

KAIOS follows semantic versioning for stable releases.

```text
MAJOR.MINOR.PATCH
```

## Version Meaning

### Patch

Use patch versions for corrections that do not change module contracts or
workflow expectations.

Example: `v0.1.1`

### Minor

Use minor versions for new modules, new templates, new playbooks, or expanded
workflow capabilities that remain backward compatible.

Example: `v0.2.0`

### Major

Use major versions for breaking changes to philosophy, module contracts,
artifact flow, or compatibility expectations.

Example: `v1.0.0`

## Repository Layout

Versioned releases live under:

```text
versions/v0.1/
versions/v0.2/
```

Shared current documentation lives under:

```text
docs/
modules/
templates/
contracts/
```

## Compatibility Rule

KAIOS should preserve old workflows whenever practical. If a future version
changes a contract, the migration path must be documented.
