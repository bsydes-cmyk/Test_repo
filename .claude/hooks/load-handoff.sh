#!/usr/bin/env bash
# SessionStart hook — matcher: clear
# When /clear fires, if a handoff was staged, inject HANDOFF.md as additional context.
set -euo pipefail

PENDING=".claude/handoff/.pending-context"
HANDOFF=".claude/handoff/HANDOFF.md"

[ -f "$PENDING" ] || exit 0
[ -f "$HANDOFF" ] || exit 0

echo "=== RESUMING FROM HANDOFF (auto-loaded by .claude/hooks/load-handoff.sh) ==="
cat "$HANDOFF"
echo ""
echo "=== END HANDOFF — execute the Next action ==="

rm -f "$PENDING"
