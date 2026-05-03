---
name: creating-skills
description: >-
  Guides the agent through creating, naming, and structuring workspace skills
  following the Agent Skills open standard. Covers SKILL.md format, YAML
  frontmatter, scripts, reference documents, assets, naming rules, and
  publishing. Use when the user asks to save a reusable pattern, workflow,
  or procedure as a skill.
metadata:
  author: nfraxlab
  version: "1.0"
---

# Creating Skills

Skills are the primary way to persist reusable knowledge in Pulse. Each
skill follows the Agent Skills open standard so it can be shared,
published, and loaded by any compatible agent.

## Available Tools

| Tool | Purpose |
|------|---------|
| `create_skill` | Install a new workspace skill bundle (name, description, optional script) |
| `add_skill_document` | Reinstall an existing skill bundle with an additional document |
| `read_skill` | Read a skill and its attached documents |
| `list_skills` | List all skills in the workspace |
| `run_skill` | Execute a skill's script |

## When to Create a Skill

Create a skill when ALL of the following are true:
- The pattern will come up again in this workspace
- It took more than one step or required non-obvious reasoning
- The user explicitly asked you to remember it, OR you solved something
  that a future session would need to approach the same way

Do NOT create a skill for:
- One-off answers or single-session content
- Simple factual questions
- Patterns already covered by an existing skill

Always call `list_skills` first to avoid duplicates.

## Skill Structure

A complete skill maps to this directory layout when published:

```
<skill-name>/
  SKILL.md            # Required: YAML frontmatter + markdown instructions
  scripts/            # Optional: executable code the agent can run
    run.py
    run.sh
  references/         # Optional: additional documentation loaded on demand
    REFERENCE.md
  assets/             # Optional: templates, schemas, static resources
```

When creating through Pulse tools:
- `create_skill` installs a complete skill bundle and generates `SKILL.md`
- `add_skill_document` rewrites that installed bundle to include new reference material
- The published directory structure is derived from the installed bundle, not assembled from separate sources of truth

## Installation Model

Treat workspace skills as installed bundles, not ad hoc records plus extra files.

- `create_skill` installs the initial bundle with a generated `SKILL.md`
- `add_skill_document` should be used only when you genuinely need another bundled file
- `read_skill` should always be your check that the installed bundle reads correctly before relying on it

This matters because Pulse now uses the same bundle-first model across:
- system skills loaded from `pulse-skills`
- marketplace skills imported into a workspace
- workspace skills created directly by the agent

## Naming Rules

Names must be **1-64 characters**, lowercase alphanumeric and hyphens only.

```
weekly-report-format     # valid
standup-template         # valid
code-review              # valid
Code-Review              # invalid: uppercase
-code-review             # invalid: leading hyphen
code--review             # invalid: consecutive hyphens
code-review-             # invalid: trailing hyphen
```

## SKILL.md Format

Every skill requires YAML frontmatter followed by markdown instructions.

### Required Frontmatter Fields

| Field | Constraint |
|-------|-----------|
| `name` | 1-64 chars, kebab-case. Must match the directory name. |
| `description` | 1-1024 chars. What the skill does and when to use it. Include keywords that help agents match tasks to this skill. |

### Optional Frontmatter Fields

| Field | Purpose |
|-------|---------|
| `license` | License name (e.g. MIT) or reference to a bundled LICENSE file. |
| `compatibility` | Max 500 chars. Runtime, system packages, or network requirements. |
| `metadata` | Arbitrary key-value pairs: author, version, tags, etc. |
| `allowed-tools` | Space-delimited list of pre-approved tools (experimental). |

### Example SKILL.md

```yaml
---
name: standup-template
description: >-
  Generates a daily standup summary from the most recent meeting transcript.
  Use after a standup or daily sync meeting.
metadata:
  author: nfraxlab
  version: "1.0"
---
```

## Writing Instructions (Markdown Body)

The markdown body after the frontmatter contains the step-by-step
instructions the agent follows when using the skill.

Write instructions the agent can apply in under 30 seconds from reading:

```markdown
# Standup Template

## When to Apply
After a daily standup or sync meeting ends.

## Steps
1. Read the full transcript
2. Extract: what each person did yesterday, plans for today, blockers
3. Format as a table with columns: Person | Yesterday | Today | Blockers

## Example Output
| Person | Yesterday | Today | Blockers |
|--------|-----------|-------|----------|
| Sam | Finished auth PR | Start billing API | Waiting on design review |
```

Keep the SKILL.md body under 500 lines (recommended under 5000 tokens).
Move detailed reference material to separate documents.

## Scripts

Scripts are executable code the agent can run via `run_skill`. When
installing a skill with a script, provide:

- `script_content`: The full script body
- `script_type`: One of `python`, `shell`, or `none`

Scripts are useful for:
- Data extraction or transformation pipelines
- Automated report generation
- File processing workflows
- API calls or integrations

Example: installing a skill with a Python script:

```
create_skill(
  name="export-action-items",
  description="Extracts action items from a meeting transcript and writes them to a markdown file.",
  script_content="import json\n...",
  script_type="python"
)
```

When published, scripts appear as `scripts/run.py` or `scripts/run.sh`.

## Reference Documents

Attach additional documentation to a skill using `add_skill_document` when
the installed bundle genuinely needs another file. Documents are loaded on
demand (not at startup) to save context tokens.

Good uses for reference documents:
- Detailed formatting guides or style references
- Template files the skill should follow
- API documentation or schema definitions
- Examples too long to fit in the main SKILL.md

```
add_skill_document(
  skill_name="standup-template",
  document_name="formatting-guide",
  content="## Formatting Rules\n..."
)
```

When published, documents appear under `references/<name>`.

Prefer a small number of clear bundled documents over many incremental adds.

## Progressive Disclosure

Skills are loaded in three stages to minimize context usage:

1. **Metadata** (~100 tokens) -- `name` and `description` loaded at startup
2. **Instructions** (< 5000 tokens) -- full SKILL.md body loaded on activation
3. **Resources** (on demand) -- scripts, references, assets loaded when needed

This means the description must be good enough for the agent to decide
whether to activate the skill without reading the full body.

## Before Every New Task

For recurring tasks, call `list_skills` to check for an existing skill
to follow rather than re-solving from scratch.

## Publishing

Skills can be published to the marketplace from the Pulse macOS app.
On publish, Pulse assembles the full directory structure:
- SKILL.md with YAML frontmatter
- Scripts as `scripts/run.<ext>`
- Documents as `references/<name>`
- Files are pushed to the shared skills repository
