# Best Practices

## Use KAIOS As A Thinking System

Ask KAIOS to structure the work before asking for implementation.

Good:

```text
Run Context Loader and Engineering Contract for this feature.
```

Weak:

```text
Write the code for this feature.
```

## Keep Scope Explicit

Every task should define what is in scope and out of scope.

This protects the project from accidental rewrites and hidden complexity.

## Prefer Small, Reviewable Changes

Large changes are harder to reason about and harder to learn from. Split work
into meaningful engineering tasks.

## Make Trade-Offs Visible

Ask for alternatives and trade-offs before choosing a design.

## Do Not Overuse Patterns

Patterns are tools, not goals. If a simple function or module solves the
problem cleanly, prefer it.

## Always Review Security-Sensitive Work

Authentication, authorization, payments, files, secrets, user data, and external
APIs must trigger security review.

## Always End With Learning

The learning summary is not decoration. It is how KAIOS helps the developer
become less dependent on AI over time.
