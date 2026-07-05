# Pattern Engine

## Responsibility

The Pattern Engine recommends design patterns only when they solve an actual
engineering problem.

## Inputs

- architecture proposal
- complexity drivers
- change points
- dependency boundaries

## Outputs

- recommended patterns
- rejected patterns
- reasoning and trade-offs

## Activation Criteria

Use when a design decision involves object relationships, module creation,
runtime behavior selection, or extension points.

## Non-Goals

- forcing patterns into simple code
- treating patterns as a checklist
- hiding business logic behind abstractions

## Review Checklist

- Does the pattern remove real complexity?
- Is the pattern understandable to future maintainers?
- Is a simpler structure enough?
