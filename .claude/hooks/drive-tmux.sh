#!/usr/bin/env bash
# Background tmux driver.
# Reads .driver-config for PANE, TMUX_SOCK, COLOR, NEXT.
# Sends /color, /clear, and the resume prompt to the tmux pane.
set -euo pipefail

LOG="/tmp/handoff-driver.log"
exec >> "$LOG" 2>&1
echo "[$(date)] driver starting (pid=$$)"

CONFIG=".claude/handoff/.driver-config"
if [ ! -f "$CONFIG" ]; then
  echo "no config at $CONFIG; exiting"
  exit 0
fi

# shellcheck disable=SC1090
source "$CONFIG"

# Restore tmux server socket if present (nohup should inherit but be safe)
if [ -n "${TMUX_SOCK:-}" ]; then
  export TMUX="$TMUX_SOCK"
fi

if ! command -v tmux >/dev/null 2>&1; then
  echo "ERROR: tmux not found in PATH"
  exit 1
fi

if [ -z "${PANE:-}" ]; then
  echo "ERROR: PANE not set in config"
  exit 1
fi

echo "PANE=$PANE COLOR=${COLOR:-default}"

# Let the skill's text output finish rendering before typing
sleep 1.5

# 1. /color
if [ -n "${COLOR:-}" ] && [ "$COLOR" != "default" ]; then
  echo "sending /color $COLOR"
  tmux send-keys -t "$PANE" "/color $COLOR" Enter
  sleep 0.7
fi

# 2. /clear — fires SessionStart hook which loads HANDOFF.md
echo "sending /clear"
tmux send-keys -t "$PANE" "/clear" Enter
sleep 2.0

# 3. Resume prompt — fires UserPromptSubmit hook which applies title
if [ -n "${NEXT:-}" ]; then
  echo "sending resume prompt"
  tmux send-keys -t "$PANE" -- "$NEXT"
  sleep 0.3
  tmux send-keys -t "$PANE" Enter
fi

rm -f "$CONFIG"
echo "[$(date)] driver done"
