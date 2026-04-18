---
name: handoff
description: One-command session handoff. Writes an exhaustive handoff doc, then drives the tmux pane to set color, clear context, and auto-prompt the fresh session — which auto-loads the handoff and auto-renames the chat. Use when the user types "/handoff", says "handoff", asks to save and continue in fresh context, or hits context pressure.
---

# handoff

Drives a full session reset in one user command. Requires Claude to be running inside tmux.

## Steps — do all, in order. Do not skip or reorder.

### 1. Verify tmux

Run via Bash: `printf '%s' "$TMUX_PANE"` and capture output.

If empty, STOP immediately and reply with EXACTLY:

```
This skill requires Claude Code to be running inside tmux.

Start a tmux session and relaunch Claude:
  tmux new -s claude
  claude

Then re-run /handoff.
```

Do not proceed past this step if `$TMUX_PANE` is empty.

### 2. Also capture `$TMUX` (the tmux server socket path)

Run via Bash: `printf '%s' "$TMUX"` and capture. You'll write both into the driver config in step 6.

### 3. Choose resume metadata

Pick:
- **TITLE**: 3–5 word chat title summarizing the work (alphanumerics, spaces, hyphens only; under 50 chars)
- **COLOR**: one of `blue`, `green`, `yellow`, `orange`, `red`, `purple`, `pink`, `default`
- **NEXT_PROMPT**: a single concrete instruction the fresh Claude should execute first. Examples: `"continue from the Next action section in the loaded handoff"`, `"run the failing test in src/foo_test.py and report the diff"`. Make it self-contained and actionable.

### 4. Write `.claude/handoff/HANDOFF.md`

Use the Write tool. Be exhaustive — the reader has zero memory of this session. Required structure:

```
# Handoff: <one-line goal>

## Goal
What the user is ultimately trying to accomplish. One line.

## Status
- Done: ...
- In progress: ...
- Blocked / waiting: ...

## Key decisions & rationale
Decisions made and WHY. Reasoning, not just outcomes.

## Files touched
- `path/to/file.ext:42-67` — what changed, why
- ...

## Open threads
Unresolved questions, TODOs, things to verify.

## Next action
The single concrete next step. Name the file, function, or command.

## Context snippets
Errors, command output, API responses — anything cold-Claude would otherwise re-derive.

## Resume metadata
- Title: <TITLE>
- Color: <COLOR>
- Next prompt: <NEXT_PROMPT>
```

### 5. Write the SessionStart marker

Write `.claude/handoff/.pending-context` as an empty file. The `load-handoff.sh` hook checks for this on `/clear` and loads HANDOFF.md.

### 6. Write the title marker

Write `.claude/handoff/.pending-title` with exactly the TITLE on a single line, no quotes, no trailing newline tricks. The `apply-handoff-title.sh` hook reads this on the first prompt after `/clear`.

### 7. Write the driver config

Write `.claude/handoff/.driver-config` with exactly this format (substitute real values):

```
PANE=<value of $TMUX_PANE from step 1>
TMUX_SOCK=<value of $TMUX from step 2>
COLOR=<chosen color>
NEXT=<chosen next prompt — single line, no quotes around it>
```

No surrounding quotes on values. No comments. One key=value per line.

### 8. Launch the driver

Run via Bash:

```
nohup .claude/hooks/drive-tmux.sh > /tmp/handoff-driver.log 2>&1 & disown
```

This spawns the tmux driver in the background. It will sleep ~1.5s (to let your output finish), then send `/color`, `/clear`, and the resume prompt to your tmux pane.

### 9. Tell the user EXACTLY this and then stop

```
Handoff staged. The driver will set color, clear context, and resume in ~3s.
Do not type until you see the new context load.

Driver log: /tmp/handoff-driver.log
```

## Hard rules

- Do NOT attempt to invoke `/clear`, `/rename`, or `/color` yourself. The driver does it.
- Do NOT skip the `$TMUX_PANE` check. Without tmux, the driver cannot work.
- Do NOT add commentary after step 9's message — the driver is about to take over the pane.
