# Workflow Quick Reference

**Model:** Contractor (you direct, Claude orchestrates)

---

## The Loop

```
Your instruction
    ↓
[PLAN] (if multi-file or unclear) → Show plan → Your approval
    ↓
[EXECUTE] Implement, verify, done
    ↓
[REPORT] Summary + what's ready
    ↓
Repeat
```

---

## I Ask You When

- **Design forks:** "Option A (fast) vs. Option B (robust). Which?"
- **Content ambiguity:** "Spec unclear on X. Assume Y?"
- **Scope question:** "Also add handout for this activity, or focus on slides?"

---

## I Just Execute When

- Fix is obvious (typo, pattern application)
- Verification (compilation checks)
- Documentation (logs, commits)
- Diagrams (per established TikZ standards)

---

## Quality Gates (No Exceptions)

| Score | Action |
|-------|--------|
| >= 80 | Ready to commit |
| < 80  | Fix blocking issues |

---

## Non-Negotiables (Customize These)

- Path convention: `TEXINPUTS=../Preambles:$TEXINPUTS` for all LaTeX compilation
- Figure standards: white background, 300 DPI minimum, TikZ + pgfplots for diagrams
- Color palette: primary_blue `#012169`, primary_gold `#B9975B`, accent_yellow `#F2A900`

---

## Preferences

**Visual:** Publication-ready TikZ + pgfplots; clean, minimal Beamer theme
**Reporting:** Concise bullet summaries; details on request
**Session logs:** Always (post-plan, incremental, end-of-session)

---

## Exploration Mode

For experimental work, use the **Fast-Track** workflow:
- Work in `explorations/` folder
- 60/100 quality threshold (vs. 80/100 for production)
- No plan needed — just a research value check (2 min)
- See `.claude/rules/exploration-fast-track.md`

---

## Next Step

You provide task → I plan (if needed) → Your approval → Execute → Done.
