---
name: commit
description: Stage, commit, and push to main. Use for the standard commit cycle.
argument-hint: "[optional: commit message]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Commit and Push

Stage changes, commit with a descriptive message, and push to main.

## Steps

1. **Check current state:**

```bash
git status
git diff --stat
git log --oneline -5
```

2. **Stage files** — add specific files (never use `git add -A`):

```bash
git add <file1> <file2> ...
```

Do NOT stage `.claude/settings.local.json` or any files containing secrets.

3. **Commit** with a descriptive message:

If `$ARGUMENTS` is provided, use it as the commit message. Otherwise, analyze the staged changes and write a message that explains *why*, not just *what*.

```bash
git commit -m "$(cat <<'EOF'
<commit message here>
EOF
)"
```

4. **Push to main:**

```bash
git push origin main
```

5. **Report** what was committed and pushed.

## Important

- Commit directly to `main` — no separate branch needed unless the user asks for one
- Exclude `settings.local.json` and sensitive files from staging
- If the commit message from `$ARGUMENTS` is provided, use it exactly
- If the push is rejected (diverged history), ask the user whether to pull first or force-push
