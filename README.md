# KAIOS

KAIOS, Kerem AI Operating System, is a Software Engineering Operating System
for AI-assisted software development.

It is not an AI agent framework, automation platform, or prompt collection.
Its purpose is to help developers think, design, implement, review, and learn
like professional software engineers.

## Start Here

**New to KAIOS? Begin with the Quickstart Pack.**

1. Read [`QUICKSTART.md`](QUICKSTART.md)
2. Choose your assistant prompt in [`assistant-prompts/`](assistant-prompts/)
3. Start your first KAIOS session (see [`examples/quickstart-session.md`](examples/quickstart-session.md))
4. Use the Engineering Contract before coding ([`contracts/contract-template.md`](contracts/contract-template.md))

You should be able to run your first KAIOS-guided workflow in under 10 minutes.

## Core Principle

AI should accelerate software engineering, not replace software engineers.

Every KAIOS interaction should improve both:

- the quality of the software being built
- the engineering judgment of the developer building it

## Current Version

- Active: `versions/v0.1`
- Focus: core methodology, workflow, module contracts, and reusable templates

## Repository Structure

```text
QUICKSTART.md           Start here — 10-minute onboarding
assistant-prompts/      Load KAIOS into ChatGPT, Cursor, Claude, Codex, Gemini
examples/               Example session and pre-implementation artifacts
docs/                   Project-level engineering decisions and operating rules
manifest/               Machine-readable project and module metadata
modules/                Independent KAIOS capability modules
templates/              Reusable task and feature templates
versions/               Versioned KAIOS releases
contracts/              Engineering Contract subsystem and templates
```

## Quickstart Example Artifacts

Before implementation, KAIOS produces explicit artifacts:

- `examples/context-summaries/jwt-auth-context-summary.md`
- `examples/module-resolutions/jwt-auth-module-resolution.md`
- `examples/contracts/jwt-auth-engineering-contract.md`

## Non-Negotiables

- Think before coding.
- Explain architectural decisions.
- Prefer simple, modular, reusable solutions.
- Review security, performance, testability, and maintainability.
- End with a learning summary.

## Essential Documents

- `QUICKSTART.md`: get started in under 10 minutes
- `docs/VISION.md`: why KAIOS exists
- `docs/PHILOSOPHY.md`: how KAIOS thinks
- `docs/GOALS.md`: project goals and non-goals
- `docs/HOW_TO_USE.md`: practical usage guide
- `docs/INTEGRATION_GUIDE.md`: using KAIOS in projects
- `docs/MODULE_OVERVIEW.md`: module responsibilities
- `contracts/engineering-contract.md`: the contract subsystem
