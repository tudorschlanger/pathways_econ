---
paths:
  - "Slides/**/*.tex"
  - "Handouts/**/*.tex"
---

# Task Completion Verification Protocol

**At the end of EVERY task, Claude MUST verify the output works correctly.** This is non-negotiable.

## For LaTeX/Beamer Slides:
1. Compile with xelatex and check for errors
2. Open the PDF to verify figures render (`open` on macOS, `xdg-open` on Linux)
3. Check for overfull hbox warnings

## For LaTeX Handouts:
1. Compile with xelatex and check for errors
2. Open the PDF to verify formatting
3. Check that activity instructions are complete

## For TikZ Diagrams:
1. Verify TikZ code compiles within the Beamer source
2. If extracting to standalone SVG/PDF, verify the output renders correctly

## Common Pitfalls:
- **Assuming success**: Always verify output files exist AND contain correct content
- **Missing preamble references**: Ensure `TEXINPUTS=../Preambles:$TEXINPUTS` is set
- **Broken image paths**: Verify all `\includegraphics` paths resolve

## Verification Checklist:
```
[ ] Output file created successfully
[ ] No compilation errors
[ ] Images/figures display correctly
[ ] Paths resolve correctly
[ ] Opened in viewer to confirm visual appearance
[ ] Reported results to user
```
