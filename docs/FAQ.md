# FAQ

## Is KAIOS an AI agent framework?

No. KAIOS is an engineering methodology and operating system for AI-assisted
software development.

## Does KAIOS generate code?

KAIOS can guide implementation, but code generation is not the main goal. The
main goal is better engineering thinking and better software quality.

## Can I use KAIOS with ChatGPT, Codex, Cursor, Claude, or Gemini?

Yes. KAIOS is assistant-agnostic. Load the KAIOS prompt and provide project
context to the AI assistant you use.

## Should KAIOS live inside my project?

Either approach works.

For multiple projects, keep KAIOS beside your projects:

```text
workspace/
  kaios/
  my-project/
```

For one project, copy the relevant KAIOS files into:

```text
my-project/.kaios/
```

## Does KAIOS replace senior engineers?

No. KAIOS is designed to strengthen engineering judgment, not replace it.

## When should I use the Engineering Contract?

Use it before implementation for any meaningful feature, refactor, bug fix, or
architecture decision.

## Is KAIOS production-ready?

KAIOS v0.1 is methodology-ready. It is not a runtime product. Milestone 1 makes
it usable in real projects as an engineering workflow.
