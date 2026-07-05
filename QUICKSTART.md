# KAIOS Quickstart

Get your first KAIOS-guided engineering session running in under 10 minutes.

## What Is KAIOS?

KAIOS (Kerem AI Operating System) is a **Software Engineering Operating System**
for AI-assisted development.

It sits between you and any AI assistant and provides:

- a consistent engineering workflow
- explicit decision-making steps
- reusable module guidance
- quality and review standards

KAIOS helps you **think, design, implement, review, and learn** like a
professional software engineer.

> **Think first. Design second. Implement third. Learn continuously.**

## What KAIOS Is Not

KAIOS is **not**:

- an AI model
- an autonomous coding agent
- an AI agent framework
- a workflow automation platform
- a prompt marketplace

KAIOS does not replace your judgment. It helps you make better engineering
decisions.

## Install

Clone the repository:

```bash
git clone <kaios-repository-url> kaios
cd kaios
```

Recommended workspace layout:

```text
workspace/
  kaios/          # this repository
  my-project/     # your application
```

Keep KAIOS separate from application code so you can reuse it across projects.

## Start In 10 Minutes

### Step 1: Read this file (you are here)

You now know what KAIOS is and what it is not.

### Step 2: Choose your assistant prompt

Open the prompt file for your AI assistant and follow its loading instructions:

| Assistant | File |
| --- | --- |
| ChatGPT | `assistant-prompts/chatgpt.md` |
| Codex | `assistant-prompts/codex.md` |
| Cursor | `assistant-prompts/cursor.md` |
| Claude | `assistant-prompts/claude.md` |
| Gemini | `assistant-prompts/gemini.md` |

Each file tells that assistant how to behave as KAIOS v0.1.

### Step 3: Load KAIOS into your session

Copy the assistant prompt into your AI tool (custom instructions, project
rules, or the first message of a new chat).

Then tell the assistant your task. Example:

```text
Mode: Development Mode

Task:
I want to build a JWT authentication system using Go Fiber and PostgreSQL.

Please run Context Loader, Module Registry, and Engineering Contract before
implementation.
```

### Step 4: Run the first workflow

KAIOS follows this order:

```text
User Request
-> Context Loader          (understand the task)
-> Module Registry         (select relevant modules)
-> Engineering Contract    (define scope and acceptance criteria)
-> Architecture Plan       (boundaries and trade-offs)
-> Implementation          (only after the contract is clear)
-> Review                  (quality, security, performance)
-> Learning Summary        (what you learned)
```

Do not skip to code. If the assistant starts coding too early, say:

```text
Stop. Run Context Loader and create an Engineering Contract first.
```

### Step 5: See a complete example

Read these files in order:

1. `examples/quickstart-session.md` — full first-session conversation
2. `examples/context-summaries/jwt-auth-context-summary.md`
3. `examples/module-resolutions/jwt-auth-module-resolution.md`
4. `examples/contracts/jwt-auth-engineering-contract.md`

These show what KAIOS produces **before** implementation starts.

## Your First Session Checklist

Use this checklist for every meaningful task:

- [ ] KAIOS prompt loaded in the assistant
- [ ] Task and project context provided
- [ ] Context Loader output reviewed
- [ ] Module Registry output reviewed
- [ ] Engineering Contract agreed (scope + acceptance criteria)
- [ ] Architecture and trade-offs understood
- [ ] Implementation started only after the contract is clear
- [ ] Review completed (architecture, security, testing, performance)
- [ ] Learning summary received

## Use KAIOS In A Real Project

### New project

```text
Load KAIOS prompt
-> describe the product idea
-> Bootstrap Mode
-> Context Loader
-> Module Registry
-> Engineering Contract
-> architecture plan
-> implement only after review
```

### Existing project

```text
Load KAIOS prompt
-> share repo structure and current task
-> Development Mode
-> Context Loader
-> Module Registry
-> task-level Engineering Contract
-> smallest safe change plan
-> implement
-> review
-> learning summary
```

For deeper integration patterns, read `docs/INTEGRATION_GUIDE.md`.

## What To Read Next

After your first session:

| Priority | File | Why |
| --- | --- | --- |
| 1 | `docs/HOW_TO_USE.md` | Daily workflow and best practices |
| 2 | `contracts/contract-template.md` | Blank Engineering Contract template |
| 3 | `docs/MODULE_OVERVIEW.md` | What each module does |
| 4 | `docs/DEVELOPMENT_MODES.md` | Bootstrap, Development, Maintenance modes |
| 5 | `docs/VISION.md` | Why KAIOS exists |

## Non-Negotiables

- Think before coding.
- Ask only necessary questions.
- Create an Engineering Contract before meaningful implementation.
- Explain architectural decisions and trade-offs.
- Review security, performance, testability, and maintainability.
- End with a learning summary.

## Core Principle

> AI should accelerate software engineering, not replace software engineers.

KAIOS succeeds when you become a better engineer — not when AI writes more code.
