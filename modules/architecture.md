# Architecture Module

## Responsibility

The Architecture module turns requirements into structure: boundaries, data
flow, dependencies, and trade-offs.

## Inputs

- context summary
- requirements
- constraints
- selected modules

## Outputs

- architecture proposal
- alternatives
- trade-off analysis
- selected approach
- implementation boundaries

## Activation Criteria

Use for any feature, system, module, integration, or refactor that affects
structure.

## Non-Goals

- choosing patterns without a problem
- adding abstraction for its own sake
- replacing code review

## Review Checklist

- Are responsibilities separated?
- Are dependencies pointing in the right direction?
- Is the design simpler than the problem allows?
- Can the module be reused later?
