# Module Overview

KAIOS modules are reusable engineering capabilities. Each module has a single
responsibility and produces explicit artifacts.

## Module Contract Fields

Each module should define:

- id
- purpose
- responsibilities
- dependencies
- inputs
- outputs
- activation criteria
- non-goals
- workflow
- quality gates
- extension rules
- review checklist
- example

## v0.1 Modules

| Module | Purpose | Primary Output |
| --- | --- | --- |
| Core | Preserve philosophy and workflow | Quality expectations |
| Context Loader | Understand the task | Context Summary |
| Module Registry | Select relevant modules | Module Resolution |
| Engineering Contract | Define expectations before work | Engineering Contract |
| Architecture | Shape boundaries and trade-offs | Architecture Decision |
| Pattern Engine | Recommend justified patterns | Pattern Decision |
| Security Engine | Identify risks and mitigations | Security Notes |
| Testing Engine | Define test strategy | Test Plan |
| Performance Engine | Identify likely bottlenecks | Performance Notes |
| Debug Engine | Guide root cause analysis | Debug Plan |
| Review Engine | Critique completed work | Review Report |
| Learning Engine | Convert work into learning | Learning Summary |

## Extension Rule

Add a module only when it owns a distinct engineering responsibility. Do not
create modules for vague themes or one-off tasks.

The Module Registry is documentation guidance only: it selects reasoning
contracts for an assistant session and does not load or execute modules.
