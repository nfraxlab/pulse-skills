---
name: knowledge-management
description: >-
  Guides Pulse on choosing between transcripts, workspace memory, behavioral
  instructions, notes, and skills. Use when the user asks what was decided,
  wants something saved, needs durable documentation, or asks Pulse to find
  prior context.
metadata:
  author: nfraxlab
  version: "1.1"
tags:
  - notes
  - memory
  - transcripts
  - retrieval
  - instructions
trigger_phrases:
  - remember this
  - write this down
  - take notes
  - what did we decide
  - find my notes
  - save this for later
---

# Knowledge Management

Pulse keeps different kinds of knowledge in different stores. Choose the store
by the user's intent, not by whichever tool is easiest to call.

## Store Boundaries

- Working context: current chat, active task state, scratchpad, and todos.
- Transcript context: live or recent audio from the current session.
- Workspace Memory: compact facts, preferences, decisions, and recurring
  context from prior sessions.
- Behavioral instructions: compact rules for how Pulse should behave in this
  workspace.
- Notes: user-facing documents, plans, meeting notes, references, and
  knowledge the user may want to read or edit later.
- Skills: reusable procedures and operating instructions.

## Retrieval Policy

Use `retrieve_context` when the answer could live in more than one store. It
searches transcript, notes, workspace Memory, and older recall fallback, and
returns source-labelled
evidence.

Prefer source-specific tools when the user names the source clearly:

- Current meeting, audio, or what was just said: transcript tools first.
- A note, document, plan, or saved write-up: note tools first.
- Previous conversation, recurring preference, or prior decision: workspace
  Memory first.
- Ambiguous "do you remember" or "what did we decide": use `retrieve_context`
  and synthesize from the strongest sources.

If the answer likely depends on prior context and that context is not visible
in the current turn, retrieve first instead of answering from weak recall.

Do not claim something is from memory when it came from a note. Keep source
labels straight in your own reasoning and be clear with the user when it
matters.

## Writing Notes

Create or update notes when the user asks to:

- take notes
- write something down
- preserve a decision or plan
- create reference material
- summarize a meeting for later use
- organize project knowledge

Use `create_subpage` when the new document belongs under an existing parent
note. Use `get_note_tree` or `list_note_children` first if the parent is
unclear.

Do not repeat the note title as the first heading. Pulse Notes stores the title
separately.

## Memory Discipline

Workspace Memory should stay compact. It is for stable future-use facts, not
full documents.

Good memory candidates:

- durable user preferences
- recurring project names and goals
- decisions likely to affect future work
- stable conventions the user expects Pulse to remember

Behavioral preferences do not belong here. Save them through behavioral
instructions instead.

Use notes instead of memory for:

- full meeting transcripts
- long project specs
- research summaries
- drafts, plans, and reference docs
- temporary task details

## Synthesis

When multiple stores return relevant context:

1. Prefer the most explicit user-authored source.
2. Prefer newer notes or transcripts over older memory when they conflict.
3. Treat long-term memory as a recall hint unless corroborated by notes,
   transcript, or the current user message.
4. Say when context is missing instead of inventing a confident answer.
