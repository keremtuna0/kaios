# Development Modes

KAIOS uses modes to match the workflow to the situation.

## Bootstrap Mode

Use Bootstrap Mode when starting a new project, major module, or foundational
architecture decision.

Focus:

- problem definition
- users and use cases
- constraints
- high-level architecture
- module boundaries
- project-level Engineering Contract
- initial risks

Avoid:

- writing feature code too early
- choosing patterns before requirements are understood

## Development Mode

Use Development Mode for normal feature work.

Focus:

- task context
- module selection
- task-level Engineering Contract
- implementation plan
- tests
- review
- learning summary

Avoid:

- skipping acceptance criteria
- ignoring failure paths
- hiding assumptions

## Maintenance Mode

Use Maintenance Mode for bugs, refactors, performance issues, security fixes,
legacy code, and production incidents.

Focus:

- observed behavior
- expected behavior
- reproduction steps
- root cause analysis
- minimal safe change
- regression tests
- risk review

Avoid:

- rewriting unrelated code
- guessing fixes without evidence
- optimizing without measurement
