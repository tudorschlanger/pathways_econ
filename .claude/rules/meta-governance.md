# Project Governance: Pathways

## Memory Management

### MEMORY.md (root directory, committed)
- Workflow learnings specific to this project
- `[LEARN:category]` entries after corrections
- Keep under 200 lines (stays in Claude's system prompt)

### .claude/state/personal-memory.md (gitignored)
- Machine-specific setup notes
- Local path references
- Personal workflow preferences

## Project Principles

- **Plan-first:** Enter plan mode for non-trivial tasks
- **Quality gates:** Nothing ships below 80/100
- **Verify after:** Compile and confirm output at end of every task
- **Session logging:** Post-plan, incremental, end-of-session
- **Single source of truth:** Beamer `.tex` for slides, Handouts `.tex` for activities

## Context Survival

**Before context compression:**
1. MEMORY.md has all `[LEARN]` entries from this session
2. Session log is current (updated within 10 minutes)
3. Active plan is saved to `quality_reports/plans/`
4. Open questions are documented in session log

**After compression or new session:**
1. Read `CLAUDE.md` + most recent plan in `quality_reports/plans/`
2. Check `git log --oneline -10` and `git diff`
3. State what you understand the current task to be

## Amendment Process

Update this file when:
- The project scope changes significantly
- New tooling is added or removed
- Workflow conventions change based on experience
