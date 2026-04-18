---
name: handoff
description: Save an exhaustive handoff from the current conversation, stage resume metadata, and hand the user two commands (`/color`, `/clear`) to continue in fresh context with the handoff auto-loaded and the chat auto-renamed. Use when the user says "handoff", "/handoff", wants to preserve progress before clearing, or hits context pressure and needs to continue cleanly in a new session.
---

# handoff

Preserve everything a cold Claude would need to continue this work after `/clear`, and stage the auto-resume.

## Steps — do all, in order

### 1. Compose `.claude/handoff/HANDOFF.md`

Write it with the `Write` tool. Be exhaustive. The reader has zero memory of this session. Structure:

```
# Handoff: <one-line goal>

## Goal
What the user is ultimately trying to accomplish. One line.

## Status
- Done: ...
- In progress: ...
- Blocked / waiting: ...

## Key decisions & rationale
Decisions made and WHY. A cold reader needs reasoning, not just outcomes.

## Files touched
- `path/to/file.ext:42-67` — what changed, why
- ...

## Open threads
Unresolved questions, TODOs, things to verify.

## Next action
The single concrete next step. Name the file, function, or command.

## Context snippets
Errors, command output, API responses — anything cold-Claude would otherwise have to re-derive.

## Resume metadata
- Title: <3-5 word chat title>
- Color: <one of: blue, green, yellow, orange, red, purple, pink>
```

### 2. Stage resume metadata

Write `.claude/handoff/.resume` (plain shell-sourceable key=value, no JSON, no quotes around values):

```
TITLE=<same title as in HANDOFF.md>
COLOR=<same color>
```

The `UserPromptSubmit` hook reads this on the first prompt after `/clear` and auto-applies the title via `hookSpecificOutput.sessionTitle`.

### 3. Tell the user exactly this (no extra commentary before or after)

```
Handoff saved → .claude/handoff/HANDOFF.md

Run these to resume in fresh context:

/color <COLOR>
/clear
```

Substitute the actual color. The title auto-applies on your next prompt; HANDOFF.md auto-loads via SessionStart hook.

## Hard rules

- Do NOT attempt to invoke `/clear`, `/rename`, or `/color` yourself. They are user-only.
- Do NOT skip writing `.resume` — without it, the title won't auto-apply.
- Keep `TITLE` under 50 chars and use only alphanumerics, spaces, and basic punctuation.
- Keep `COLOR` to one of the seven allowed values above.
