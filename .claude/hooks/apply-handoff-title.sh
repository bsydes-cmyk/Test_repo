#!/usr/bin/env bash
# UserPromptSubmit hook.
# On the first prompt after /clear, if a title was staged, apply it via hookSpecificOutput.sessionTitle.
set -euo pipefail

PENDING=".claude/handoff/.pending-title"
[ -f "$PENDING" ] || exit 0

TITLE=$(head -n 1 "$PENDING" | tr -d '\r\n')
[ -z "$TITLE" ] && { rm -f "$PENDING"; exit 0; }

# JSON-escape: backslashes and double quotes
ESC=$(printf '%s' "$TITLE" | sed 's/\\/\\\\/g; s/"/\\"/g')

printf '{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","sessionTitle":"%s"}}\n' "$ESC"

rm -f "$PENDING"
