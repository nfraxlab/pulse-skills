---
name: meeting-insights
description: >-
  Defines how the agent extracts and presents insights from live audio
  transcripts, including action items, decisions, and open questions.
  Use when the user asks about the current meeting or requests a summary.
metadata:
  author: nfraxlab
  version: "1.0"
---

# Meeting Insight Patterns

Pulse runs alongside live audio. These patterns maximize value from transcripts.

## Transcript-First Rule

For any question about the current meeting, call `get_current_transcript`
or `get_recent_utterances` before responding. Never answer from assumption
when the ground truth is one tool call away.

## High-Value Signal to Watch For

Monitor the transcript for:
- **Action items**: "I'll send that", "can you look into", "we need to by Friday"
- **Decisions**: "we decided", "let's go with", "agreed — we will"
- **Open questions**: things raised but left unresolved
- **Commitments**: named owners + deliverables + deadlines mentioned together
- **Blockers**: "we're waiting on", "blocked by", "can't proceed until"

## Response Format

When surfacing insights:
- Use concise bullets, not paragraphs
- Attribute to speaker when known: "Per Sam: next steps by EOW"
- Group: Actions / Decisions / Open Questions
- One optional closing line: "Anything else you want to track from this?"

## Passive Insight Cadence

Do not volunteer unsolicited insights more than once per ~5 minutes.
If nothing new or notable has occurred since the last insight, output nothing.

## Summary Requests

When asked for a meeting summary:
1. Read the full transcript
2. Extract: key decisions, action items (owner + deadline when stated),
   open questions, and any notable context
3. Format as a short structured doc the user can copy and share
