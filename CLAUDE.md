# CLAUDE.MD -- Pathways: Economics & Finance Workshop

**Project:** Pathways: Economics & Finance Workshop
**Institution:** Yale University
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile and confirm output at the end of every task
- **Single source of truth** -- Beamer `.tex` is authoritative for slides; Handouts `.tex` for activities
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md

---

## Folder Structure

```
Pathways/
├── CLAUDE.md                    # This file
├── .claude/                     # Rules, skills, agents, hooks
│   ├── agents/                  # Custom agent definitions
│   ├── hooks/                   # Pre/post hooks (e.g., pre-compact)
│   ├── rules/                   # Governance rules (plan-first, orchestrator, etc.)
│   ├── skills/                  # Slash-command skills
│   └── state/                   # Gitignored local state
├── codes/Preambles/             # LaTeX headers (header_slides.tex, header_doc.tex)
├── data/                        # Datasets
├── doc/
│   ├── Lectures/                # Reference materials per lesson (Lesson 1–5)
│   └── Pilot/                   # Pilot session materials (reference only)
├── output/
│   ├── Lecture1/                # Lecture 1: slides + compiled PDF
│   ├── syllabus/                # Course syllabus handout
│   └── figures/                 # Figures and images
├── quality_reports/
│   ├── plans/                   # Implementation plans
│   ├── session_logs/            # Session logs
│   ├── specs/                   # Requirements specifications
│   └── merges/                  # Quality reports at merge time
├── explorations/                # Sandbox for experimental work
└── templates/                   # Session log, quality report, LaTeX templates
```

---

## Commands

```bash
# Compile lecture slides (XeLaTeX, from lecture folder)
cd output/LectureN && TEXINPUTS=../../codes/Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex

# Compile handouts/syllabus (same preamble path)
cd output/syllabus && TEXINPUTS=../../codes/Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Commit | Good enough to save |
| 90 | PR | Ready for deployment |
| 95 | Excellence | Aspirational |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/compile-latex [file]` | 3-pass XeLaTeX + bibtex |
| `/extract-tikz [file]` | Extract TikZ diagrams to PDF/SVG |
| `/proofread [file]` | Grammar/typo/overflow review |
| `/visual-audit [file]` | Slide layout audit |
| `/pedagogy-review [file]` | Narrative, notation, pacing review |
| `/slide-excellence [file]` | Combined multi-agent review |
| `/validate-bib` | Cross-reference citations |
| `/devils-advocate` | Challenge slide design |
| `/create-lecture` | Full lecture creation |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/lit-review [topic]` | Literature search + synthesis |
| `/learn [skill-name]` | Extract discovery into persistent skill |
| `/context-status` | Show session health + context usage |
| `/deep-audit` | Repository-wide consistency audit |
| `/format-tables` | Format tables for LaTeX |

---

## Beamer Custom Environments

| Environment | Effect | Use Case |
|-------------|--------|----------|
| `keybox` | Gold background box | Key points and takeaways |
| `highlightbox` | Gold left-accent box | Important highlights |
| `definitionbox[Title]` | Blue-bordered titled box | Formal definitions |
| `methodbox` | Blue background box | Methods and frameworks |
| `resultbox` | Green-bordered box | Key results and answers |
| `quotebox` | Italic with attribution | Quotes and citations |

---

## Current Project State

| Lecture | Beamer | Handout | Key Content |
|---------|--------|---------|-------------|
| 1: Thinking Like an Economist | `lec1_slides.tex` | -- | Opportunity cost, sunk cost fallacy, cost-benefit analysis, smartphone ban debate |
| Syllabus | -- | `syllabus.tex` | 5-day workshop overview |
| 2: Causal Claims & Data | Planned | Planned | Causal claims, DAGs, firefighter activity, chart detective |
| 3: Markets & Externalities | Planned | Planned | Commons game, tragedy of the commons, carbon tax game |
| 4: Trade Policy | Planned | Planned | Steel tariff debate, stakeholder analysis with citations |
| 5: Finance & Behavior | Planned | Planned | Stock market game, behavioral finance, prospect theory |
