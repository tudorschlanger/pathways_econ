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
├── Bibliography_base.bib        # Centralized bibliography
├── Figures/                     # Figures and images
├── Preambles/header.tex         # LaTeX headers
├── Slides/                      # Beamer .tex lecture slides
├── Handouts/                    # Standalone .tex activity/worksheet documents
├── Lectures/                    # Reference materials (PowerPoint, Word, Excel)
├── Pilot/                       # Pilot session materials (reference only)
├── quality_reports/             # Plans, session logs, merge reports
├── explorations/                # Sandbox for experimental work
└── templates/                   # Session log, quality report templates
```

---

## Commands

```bash
# LaTeX (3-pass, XeLaTeX only)
cd Slides && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
BIBINPUTS=..:$BIBINPUTS bibtex file
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex

# Compile handouts (same preamble path)
cd Handouts && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
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
| 1: Thinking Like an Economist | `Lecture01_Opportunity_Cost.tex` | `Handout01_Weekend_Planning.tex` | Opportunity cost, sunk cost fallacy, cost-benefit analysis, smartphone ban debate |
| 2: Causal Claims & Data | `Lecture02_Causal_Claims.tex` | `Handout02_Firefighters.tex` | Causal claims, DAGs, firefighter activity, chart detective |
| 3: Markets & Externalities | `Lecture03_Markets.tex` | `Handout03_Carbon_Tax.tex` | Commons game, tragedy of the commons, carbon tax game |
| 4: Trade Policy | `Lecture04_Trade.tex` | `Handout04_Steel_Tariff.tex` | Steel tariff debate, stakeholder analysis with citations |
| 5: Finance & Behavior | `Lecture05_Finance.tex` | `Handout05_Coin_Flip.tex` | Stock market game, behavioral finance, prospect theory |
