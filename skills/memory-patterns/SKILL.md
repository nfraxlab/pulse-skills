---
name: memory-patterns
description: >-
  Controls when and how the agent uses recall_past_conversations to retrieve
  prior session context. Use when the user references something from a previous
  conversation or when deciding whether information is worth persisting.
metadata:
  author: nfraxlab
  version: "1.0"
---

# Memory Patterns

You have access to `recall_past_conversations`. Use it selectively.

## When to Recall

Recall is worth calling when:
- The user references something from a previous session
  ("last time we discussed", "what did we decide about")
- A question feels familiar and a prior answer would be directly useful
- You need context about a recurring topic or person before responding

Do NOT call recall on every query — only when prior context is needed.
Do NOT surface recalled information unprompted mid-conversation.

## What Is Worth Remembering

The agent cannot directly write to long-term memory storage, but you can
create a skill or suggest a flow to persist important patterns. Prompt
the user to save something when:
- They express a strong preference ("always do X", "never include Y")
- You discover a workflow they use repeatedly
- A naming convention or output format recurs across sessions

## What Is Not Worth Remembering

- Raw meeting content — transcripts are already stored and searchable
- One-time facts tied to a specific date
- Information the user can easily look up themselves

## Anti-Patterns

- Do not call `recall_past_conversations` before every response
- Do not interpret absence of recalled results as a failure — silence is fine
- Do not create duplicate skill entries for the same pattern
