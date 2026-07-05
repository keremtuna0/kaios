# Architecture Decisions

## ADR-001: KAIOS starts documentation-first

Decision: v0.1 defines methodology, module contracts, and templates before any
runtime implementation.

Reason: KAIOS is an engineering operating system, not an automation framework.
The thinking model must be stable before any executable layer exists.

Trade-off: There is less immediate automation, but the project avoids becoming
a tool without a philosophy.

## ADR-002: Modules communicate through artifacts

Decision: Modules exchange explicit artifacts such as context summaries,
requirements, architecture decisions, review reports, and learning summaries.

Reason: Artifact-based communication keeps module boundaries clear and makes
the workflow teachable.

Trade-off: The process can feel more formal, but it improves maintainability
and learning.

## ADR-003: Engines begin as contracts

Decision: Security, testing, performance, pattern, debug, review, and learning
engines begin as contracts before implementation.

Reason: Stable responsibilities prevent future engines from overlapping or
becoming god modules.

Trade-off: More upfront documentation is required, but future implementation
will be cleaner.
