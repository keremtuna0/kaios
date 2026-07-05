# How To Use KAIOS

**First time here?** Start with [`QUICKSTART.md`](../QUICKSTART.md) for a
10-minute onboarding path, then return here for daily workflow details.

This guide explains how to use KAIOS in a real software project with any AI
assistant.

## Installation

Clone the repository:

```bash
git clone <kaios-repository-url> kaios
```

Recommended folder structure:

```text
workspace/
  kaios/
  my-project/
```

This keeps KAIOS reusable across multiple projects.

To update KAIOS:

```bash
cd kaios
git pull
```

## Project Integration

### Brand New Project

Use KAIOS before choosing architecture or writing code.

```text
Load KAIOS prompt
-> describe the product idea
-> use Bootstrap Mode
-> run Context Loader
-> resolve modules
-> create Engineering Contract
-> plan architecture
-> implement only after review
```

### Existing Project

Use KAIOS to understand the current system before changing it.

```text
Load KAIOS prompt
-> provide repo structure
-> explain current task
-> run Context Loader
-> resolve modules
-> create task-level Engineering Contract
-> plan the smallest safe change
-> implement
-> review
```

## Where KAIOS Should Live

For repeated use across projects:

```text
workspace/
  kaios/
  project-a/
  project-b/
```

For project-specific use:

```text
project-a/
  .kaios/
    PROMPT.md
    contract-template.md
    task-template.md
```

Do not mix KAIOS internals with application business logic. KAIOS should guide
the project, not become part of the product runtime.

## How AI Receives KAIOS Context

At the start of a session, provide:

1. `versions/v0.1/PROMPT.md`
2. the current task
3. relevant project context
4. any constraints
5. the desired development mode

If the assistant supports project rules or custom instructions, place the KAIOS
prompt there.

## Daily Workflow

```text
Start task
-> Load KAIOS
-> Context Loader
-> Module Registry
-> Engineering Contract
-> Planning
-> Implementation
-> Testing
-> Review
-> Learning Summary
```

## AI Interaction

Give the AI:

- what you want to build or fix
- the project goal
- language and framework
- database and external services
- existing architecture
- constraints
- what you already tried
- learning preference

KAIOS should determine:

- missing questions
- task type
- risk level
- relevant modules
- architecture workflow
- review checklist
- learning summary

## Example Prompt

```text
Use KAIOS v0.1.

Mode: Development Mode

Task:
I want to add JWT authentication to a Go Fiber API with PostgreSQL.

Context:
- Existing API project
- Users table exists
- Need production-aware design
- I want to understand the architecture, not just get code

Please run Context Loader, Module Registry, and Engineering Contract before
implementation.
```

## Best Practices

- Start with the problem, not the implementation.
- Ask KAIOS to explain trade-offs.
- Require an Engineering Contract before coding.
- Keep module boundaries explicit.
- Review security and testing for every meaningful feature.
- End with a learning summary.

## Common Mistakes

- Asking for code before requirements are clear.
- Skipping architecture for security-sensitive features.
- Using design patterns because they sound professional.
- Treating KAIOS as an autonomous agent.
- Copying output without understanding the trade-offs.
