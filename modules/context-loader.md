# Context Loader Module

## Purpose

Extract structured task context from an unstructured developer request.

## Responsibilities

- separate facts, assumptions, and unknowns
- classify task type, risk, mode, and candidate modules
- identify missing project context and the developer's learning needs

## Inputs

- raw request
- repository context, architecture notes, and relevant files when available
- project constraints, production expectations, and learning preference

## Outputs

- Context Summary
- problem domain, target stack, storage needs, and expected complexity
- facts, assumptions, unknowns, risk level, recommended mode, and candidate modules

## Activation Criteria

Use at the start of every meaningful task or when a request becomes ambiguous.

## Dependencies

- Core

## Non-Goals

- choosing architecture
- writing code or reviewing implementation

## Workflow

```text
Request -> extract facts -> separate assumptions -> classify task and stack
-> identify missing context -> assess risk and mode -> Context Summary
```

### Task Classification

Classify the request as a new project, feature development, bug fix, refactor,
architecture/security/performance review, learning request, or documentation
task. A task may have more than one relevant label.

### Risk Levels

- **Low:** documentation, small isolated changes, or learning-only work.
- **Medium:** normal feature work, moderate refactors, integrations, or data-model changes.
- **High:** authentication, authorization, payments, secrets, user data,
  infrastructure, security fixes, incidents, or broad architecture changes.

### Context Summary Shape

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

## Quality Gates

- Facts, assumptions, and unknowns are visibly separate.
- The summary identifies stack, constraints, risk, mode, and candidate modules.

## Review Checklist

- Is the domain clear, risk justified, mode appropriate, and are only necessary questions identified?

## Extension Rules

- Add stack, project-type, domain, risk, learning-level, or repository
  classifiers only when they preserve the fact-versus-assumption boundary.

## Example

JWT authentication is high risk because it handles identity, secrets, and user data.
