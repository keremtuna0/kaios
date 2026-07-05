# Architecture Overview

KAIOS is a documentation-first Software Engineering Operating System.

It is designed as a set of reusable engineering modules that guide AI-assisted
development without becoming an autonomous coding framework.

## High-Level Flow

```text
User Request
-> Context Loader
-> Module Registry
-> Engineering Contract
-> Planning
-> Implementation
-> Review
-> Learning Summary
```

## Core Architectural Idea

KAIOS modules do not call each other like runtime services. They communicate
through explicit artifacts:

- Context Summary
- Module Resolution
- Engineering Contract
- Architecture Decision
- Implementation Plan
- Review Report
- Learning Summary

This keeps the system portable across ChatGPT, Codex, Cursor, Claude, Gemini,
and future AI assistants.

## Main Subsystems

### Core

Defines the project philosophy, mandatory workflow, and quality expectations.

### Context Loader

Turns raw user intent into structured task context.

### Module Registry

Selects the KAIOS modules that should participate in a task.

### Engineering Contract

Defines scope, acceptance criteria, constraints, quality expectations, and
review requirements before implementation begins.

### Engines

Specialized modules such as Security, Testing, Performance, Pattern, Debug,
Review, and Learning provide focused engineering guidance.

## Boundary

KAIOS owns the engineering process. It does not own application business logic,
autonomous execution, or background automation.
