---
name: create-lecture
description: Create new Beamer lecture from instructor notes and materials. Guided workflow with notation consistency.
argument-hint: "[Topic name]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task"]
context: fork
---

# Lecture Creation Workflow

Create a beautiful, pedagogically excellent Beamer lecture deck.

**This is a collaborative, iterative process. The instructor drives the vision; Claude is a thinking partner.**

---

## CONSTRAINTS (Non-Negotiable)

1. **Read the knowledge base FIRST** -- notation registry, narrative arc, applications database
2. Every new symbol MUST be checked against the notation registry
3. Motivation before formalism -- no exceptions
4. Worked example within 2 slides of every definition
5. Max 2 colored boxes per slide
6. No `\pause` or overlay commands (check project rules)
7. Transition slides at major conceptual pivots
8. Thread at least 1 running classroom activity throughout
9. All citations verified against the bibliography
10. **Work in batches of 5-10 slides** -- share for feedback, don't bulk-dump

---

## WORKFLOW

### Phase 0: Intake & Context
- Read knowledge base (`.claude/rules/knowledge-base-template.md`)
- Inventory provided materials (instructor notes in `notes.md`, existing slides in `Lectures/`, pilot materials in `Pilot/`)
- Read previous lecture's structure and ending
- State pedagogical goal, get user confirmation

### Phase 1: Material Analysis
- Extract key concepts from instructor notes
- Identify slide-worthy content
- Identify interactive activities and group exercises
- Map existing examples to economic concepts
- Present summary for approval

### Phase 2: Structure Proposal
- Propose outline (5-Act or 3-Part template)
- List TikZ diagrams needed
- List new notation to introduce
- Identify which activities need separate handout documents
- **GATE: User approves before Phase 3**

### Phase 3: Draft Slides (Iterative)
- Work in batches of 5-10 slides
- Check notation, apply creation patterns
- Quality checks during drafting

### Phase 4: Figures & Handouts
- TikZ diagrams in Beamer source (single source of truth)
- Create handout `.tex` files for activities that need them
- Ensure slide content and handout content are consistent

### Phase 5: Polish & Compile
- Full 3-pass compilation
- Run Devil's Advocate
- Run Substance Review (domain-reviewer agent)
- Update knowledge base with new notation

---

## Post-Creation Checklist

```
[ ] Lecture compiles without errors
[ ] No overfull hbox > 10pt
[ ] All citations resolve
[ ] Every definition has motivation + worked example
[ ] Max 2 colored boxes per slide
[ ] 2-3 Socratic questions embedded
[ ] Transition slides between sections
[ ] At least 1 running activity threaded throughout
[ ] Handouts created and consistent with slides
[ ] New notation added to knowledge base
[ ] Session log updated
[ ] Devil's Advocate run
```
