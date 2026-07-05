# Context Loader Module

## Purpose

The Context Loader extracts structured task context from an unstructured user
request.

It understands the task. It does not design or implement the solution.

## Responsibilities

- extract facts from the user request
- separate facts from assumptions
- classify the task type
- identify missing context
- estimate risk level
- identify the recommended development mode
- produce a Context Summary artifact

## Inputs

- raw user request
- repository context when available
- existing project constraints
- current architecture notes
- relevant files or folder structure
- user learning preference
- production expectations

## Outputs

- problem domain
- task type
- target language and framework
- data storage requirements
- expected complexity
- production requirements
- learning needs
- assumptions
- missing questions
- risk level
- recommended development mode
- candidate modules

## Workflow

```text
Read request
-> extract facts
-> separate assumptions
-> classify task
-> detect stack and domain
-> identify missing context
-> estimate risk
-> recommend mode
-> produce Context Summary
```

## Task Types

- new project
- feature development
- bug fix
- refactor
- architecture review
- security review
- performance review
- learning request
- documentation task

## Risk Levels

### Low

Documentation, small isolated changes, or learning-only requests.

### Medium

Normal feature work, moderate refactors, integrations, or data model changes.

### High

Authentication, authorization, payments, secrets, user data, infrastructure,
security fixes, production incidents, or broad architecture changes.

## Extension Points

- stack detectors
- project type detectors
- domain classifiers
- risk classifiers
- learning-level adapters
- repository structure analyzers

## Activation Rules

Use when a task starts or when the request is ambiguous.

## Non-Goals

- choosing architecture
- writing code
- reviewing implementation

## Context Summary Shape

```text
problem_domain:
task_type:
mode:
language:
framework:
database:
constraints:
facts:
assumptions:
unknowns:
risk_level:
candidate_modules:
learning_needs:
```

## Review Checklist

- Were assumptions separated from facts?
- Were only necessary questions asked?
- Was the problem domain identified clearly?
- Was the risk level justified?
- Was the recommended mode appropriate?
