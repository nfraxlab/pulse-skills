# pulse-skills

Shared skills repository for [Pulse](https://github.com/nfraxlab/pulse). Skills published from the Pulse macOS app are stored here and indexed by the [skills.sh](https://skills.sh) marketplace.

This repository follows the [Agent Skills](https://agentskills.io/specification) open standard.

## Directory Structure

Each skill lives in its own directory under `skills/`:

```
skills/
  <skill-name>/
    SKILL.md            # Required: YAML frontmatter + markdown instructions
    scripts/            # Optional: executable code the agent can run
      run.py
      run.sh
    references/         # Optional: additional documentation loaded on demand
      REFERENCE.md
    assets/             # Optional: templates, schemas, static resources
```

The directory name must match the `name` field in the SKILL.md frontmatter.

## SKILL.md Format

Every skill requires a `SKILL.md` file with YAML frontmatter followed by markdown instructions.

### Required Fields

| Field | Constraint |
|-------|-----------|
| `name` | 1-64 chars. Lowercase alphanumeric and hyphens only. No leading/trailing or consecutive hyphens. Must match directory name. |
| `description` | 1-1024 chars. Describes what the skill does and when to use it. Include keywords that help agents identify relevant tasks. |

### Optional Fields

| Field | Purpose |
|-------|---------|
| `license` | License name or reference to a bundled LICENSE file. |
| `compatibility` | Max 500 chars. Environment requirements (runtime, system packages, network). |
| `metadata` | Arbitrary key-value pairs (author, version, etc.). |
| `allowed-tools` | Space-delimited list of pre-approved tools. Experimental. |

### Example

```yaml
---
name: code-review
description: Reviews pull requests for style, correctness, and security issues. Use when reviewing code changes or preparing PRs.
license: MIT
compatibility: Requires git and access to the internet
metadata:
  author: nfraxlab
  version: "1.0"
allowed-tools: Bash(git:*) Read
---

Step-by-step instructions for the agent go here in markdown.

See [the reference guide](references/REFERENCE.md) for detailed patterns.

Run the analysis script:
scripts/run.py
```

## Progressive Disclosure

Skills are loaded in stages to minimize context usage:

1. **Metadata** (~100 tokens) -- `name` and `description` are loaded at startup for all skills
2. **Instructions** (recommended < 5000 tokens) -- full SKILL.md body is loaded when the skill is activated
3. **Resources** (on demand) -- files in `scripts/`, `references/`, and `assets/` are loaded only when needed

Keep SKILL.md under 500 lines. Move detailed reference material to separate files.

## Naming Rules

```
code-review          # valid
data-analysis        # valid
pdf-processing       # valid
PDF-Processing       # invalid: uppercase
-pdf                 # invalid: leading hyphen
pdf--processing      # invalid: consecutive hyphens
```

## Publishing

Skills are published from the Pulse macOS app:

1. Open a skill in the detail view
2. Open the context menu and select **Publish to Marketplace**
3. The app generates a spec-compliant slug from the skill name
4. `SKILL.md` is created with full YAML frontmatter
5. Scripts are published as `scripts/run.<ext>` (py, sh, js)
6. Documents are published as `references/<name>`
7. Files are pushed to this repo via the GitHub Contents API

## Validation

Use the [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) library to validate skills locally:

```
skills-ref validate ./skills/my-skill
```
