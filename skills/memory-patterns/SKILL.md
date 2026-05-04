---
name: memory-patterns
description: >-
  Guides Pulse on retrieving, saving, and updating durable workspace memory
  and behavioral instructions. Use when the user references prior context,
  states a stable preference, or when deciding whether something should be
  saved for future conversations.
metadata:
  author: nfraxlab
  version: "1.1"
tags:
  - memory
  - retrieval
  - persistence
  - preferences
trigger_phrases:
  - do you remember
  - remember this
  - keep this in mind
  - last time we decided
  - always do this
---

# Memory Patterns

Pulse has two durable stores for future behavior:

- Workspace Memory: stable facts, decisions, recurring context, and other
  non-behavioral carry-forward information.
- Behavioral instructions: compact workspace-level rules for how Pulse should
  behave.

Use the right store. Do not treat all persistence as the same thing.

## Retrieval Policy

Before answering with uncertainty, missing recall, or "I don't remember,"
search first.

Use `retrieve_context` when the answer may depend on prior transcript,
workspace Memory, notes, or older conversations and the correct source is not
obvious.

Good retrieval triggers:
- The user references a previous session, decision, preference, or recurring topic
- The current question likely depends on earlier context not visible in the turn
- The same project, customer, convention, or workflow keeps coming up

Treat `recall_past_conversations` as a fallback for older Pulse session recall
when workspace Memory does not contain the needed context.

## What Belongs In Workspace Memory

Use `remember_context` for stable non-behavioral information likely to help in
future conversations, even if the user did not explicitly say "remember this."

Good memory candidates:
- Durable project decisions
- Recurring names, conventions, and product facts
- Stable user or workspace preferences that are not about Pulse's own behavior
- Reusable context that future tasks will likely need

Be conservative. Save only information with clear future value.

## What Belongs In Behavioral Instructions

Use `update_behavioral_instructions` when the user states an enduring
preference about how Pulse should behave, write, format, collaborate, or use
tools.

Examples:
- Response style and tone preferences
- Formatting defaults
- How direct or skeptical Pulse should be
- Stable tool-use or coding-agent preferences

Keep this section compact and workspace-level. Do not save one-off phrasing
requests as behavioral instructions.

## What Not To Save

- Raw meeting transcripts or long notes
- Large project specs or research write-ups
- Temporary task state or one-off details
- Speculative claims not yet established as true
- Sensitive secrets or credentials
- Behavioral preferences stored as generic Memory

## Anti-Patterns

- Do not save everything just because it might be useful someday
- Do not store user-facing documents in Memory instead of notes
- Do not put Pulse behavior rules into generic Memory
- Do not answer from vague recollection when retrieval is cheap
- Do not interpret missing results as proof that something never happened
