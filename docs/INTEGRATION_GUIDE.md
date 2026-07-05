# Project Integration Guide

KAIOS can be used with new projects, existing projects, and multiple AI
assistants.

## Integration Models

### External Reference Model

Use this when one KAIOS repository serves multiple projects.

```text
workspace/
  kaios/
  project-a/
  project-b/
```

Benefits:

- one KAIOS source of truth
- easy updates
- reusable across projects

Trade-off:

- project-specific KAIOS decisions must be documented inside each project

### Embedded Project Model

Use this when a project needs its own KAIOS copy.

```text
project-a/
  .kaios/
    PROMPT.md
    contract-template.md
    task-template.md
    project-contract.md
```

Benefits:

- project-specific rules stay close to the code
- easier onboarding for contributors

Trade-off:

- updates must be synchronized manually

## New Project Integration

1. Load the KAIOS prompt.
2. Describe the product idea.
3. Run Bootstrap Mode.
4. Create a project-level Engineering Contract.
5. Define architecture before implementation.
6. Create the first task contract.
7. Implement with review and learning summary.

## Existing Project Integration

1. Load the KAIOS prompt.
2. Provide repository structure.
3. Provide current architecture notes if available.
4. Describe the task.
5. Run Context Loader.
6. Resolve modules.
7. Create task-level Engineering Contract.
8. Make the smallest maintainable change.
9. Review and document learning.

## Assistant-Specific Notes

### ChatGPT

Paste the KAIOS prompt at the start of the conversation or store it in custom
instructions if appropriate.

### Codex

Keep KAIOS docs in the workspace and ask Codex to read the relevant files before
changes.

### Cursor

Add KAIOS rules to project instructions and keep templates in `.kaios/`.

### Claude

Provide the KAIOS prompt and attach the relevant docs or templates.

### Gemini

Use the KAIOS prompt as the working instruction and provide repository context
manually when needed.
