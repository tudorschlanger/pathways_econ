---
paths:
  - "Slides/**/*.tex"
  - "Handouts/**/*.tex"
---

# Single Source of Truth: Enforcement Protocol

**Beamer `.tex` is the authoritative source for lecture slides. Handouts `.tex` is the authoritative source for activity sheets.**

## The SSOT Chain

```
Slides/*.tex (SOURCE OF TRUTH for lecture content)
  ├── Bibliography_base.bib (shared references)

Handouts/*.tex (SOURCE OF TRUTH for activities)
  ├── Bibliography_base.bib (shared references)

Figures/ (shared assets for both)
```

## Rules

- NEVER edit derived artifacts independently.
- ALWAYS propagate changes from source.
- If a concept appears in both slides and handouts, update both.
- Figures in `Figures/` are shared; changes affect both slides and handouts.
