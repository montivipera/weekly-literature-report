#!/usr/bin/env bash
# guard.sh - PreToolUse hook for Edit|Write; see CLAUDE.md "Enforcement reference". Acts only on
# papers/<slug>/ paths. Allow = exit 0, no output (permission rules still apply). Deny = JSON, exit 0.

deny() {
  jq -n --arg r "$1" '{hookSpecificOutput: {hookEventName: "PreToolUse",
    permissionDecision: "deny", permissionDecisionReason: $r}}'
  exit 0
}

if ! command -v jq >/dev/null 2>&1; then
  echo "guard.sh: jq is not installed; Edit/Write blocked until it is (see CLAUDE.md setup)." >&2
  exit 2
fi
f=$(jq -r '.tool_input.file_path // empty' 2>/dev/null)
[ -z "$f" ] && exit 0

proj=${CLAUDE_PROJECT_DIR:-$PWD}
case "$f" in
  /*) ;;
  *) f="$proj/$f" ;;
esac

# Locate the papers/ root: the project's own first, else the first "/papers/" in the path.
case "$f" in
  "$proj"/papers/*) root="$proj/papers" ;;
  */papers/*) root="${f%%/papers/*}/papers" ;;
  *) exit 0 ;;
esac

rest=${f#"$root"/}
slug=${rest%%/*}
[ -z "$slug" ] || [ "$slug" = "$rest" ] && exit 0   # not inside papers/<slug>/
pdir="$root/$slug"
rel=${rest#*/}
case "/$rel/" in
  */../*|*/./*) deny "guard.sh: use a normalised path inside papers/$slug/ (no '.' or '..' segments)." ;;
esac
# STATE.md and inbox.md are always writable.
case "$rel" in
  STATE.md|inbox.md) exit 0 ;;
esac

# Frozen plan: deny once any tag plan-<slug>-* exists, in every mode.
if [ "$rel" = "analysis-plan.md" ]; then
  tag=$(git -C "${root%/papers}" tag -l "plan-$slug-*" 2>/dev/null | head -n 1)
  if [ -n "$tag" ]; then
    deny "analysis-plan.md for '$slug' is frozen by git tag $tag. Never edit it: record any change as a row in deviations.md, or append the idea to inbox.md instead."
  fi
fi

state="$pdir/STATE.md"
if [ ! -f "$state" ]; then
  echo "guard.sh: warning: papers/$slug/STATE.md not found; edit allowed without live-file check. Copy the STATE.md template first." >&2
  exit 0
fi

getkey() {
  sed -n "s/^[[:space:]]*$1:[[:space:]]*//p" "$state" | head -n 1 |
    sed 's/[[:space:]]*#.*$//; s/[[:space:]]*$//' | tr -d "\"'"
}
mode=$(getkey mode)
live=$(getkey live_file)

[ "$mode" = "propagate" ] && exit 0
[ "$mode" = "work" ] || echo "guard.sh: warning: mode '$mode' in papers/$slug/STATE.md is not work|propagate; treating as work." >&2

# Work mode: allow only the live file(s); a value ending in "/" is a directory prefix.
set -f
for lf in $(printf '%s' "$live" | tr ',' ' '); do
  lf=${lf#./}
  case "$lf" in
    */) case "$rel" in "$lf"*) exit 0 ;; esac ;;
    *) [ "$rel" = "$lf" ] && exit 0 ;;
  esac
done
set +f

deny "Blocked by guard.sh: papers/$slug/$rel is not the live file (live_file: ${live:-unset}; mode: ${mode:-unset}). Edit only the live file; append the idea to inbox.md instead, or ask the user to type 'propagate inbox'."
