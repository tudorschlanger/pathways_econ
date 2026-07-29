---
name: format-tables-reg
description: >
  Apply a consistent LaTeX regression table style for Stata output. Use this skill whenever
  the user is writing Stata code that produces regression LaTeX tables — including OLS, IV,
  probit, logit, or any coefficient table. Also trigger when the user references esttab,
  outreg2, estadd, eststo, or any regression table-building workflow, or asks about
  column headers, specification rows, fixed effects indicators, significance stars, or
  standard errors in the context of Stata or LaTeX. When in doubt, load this skill.
---

# Stata LaTeX Regression Table Style Guide

This skill governs all LaTeX regression tables produced in Stata projects. Apply these
rules to every table you write or modify, without exception.

---

## 1. Universal Formatting Rules

### Border lines
| Location | Command |
|---|---|
| Top of table | `\midrule\midrule` (double rule) |
| Bottom of table | `\midrule\midrule` (double rule) |
| Under column headers | `\cmidrule(lr){2-N}` where N = last column index (starts at col 2) |
| Between panels | `\addlinespace[4pt]` — no `\midrule` |
| Under panel name | **Nothing** — no rule under panel headers |

Do **not** use `\toprule` or `\bottomrule`. Use `\midrule\midrule` at top and bottom only.

**Header row order** (top to bottom):
1. `\midrule\midrule`
2. Outcome variable header row (using `\multicolumn`)
3. Specification number row (`(1)`, `(2)`, ...)
4. `\cmidrule(lr){2-N}`
5. Data rows begin

Never place `\cmidrule` directly after `\midrule\midrule` — column headers must appear between them.

### Panel formatting
- Panel names are **italicized**: `\textit{Panel A: Group Name}`
- Panel names span all columns: `\multicolumn{N}{l}{\textit{Panel A: ...}}`
- Pattern: `Panel {A/B/C}:` followed by a short label characterizing that group
- No horizontal rule below the panel name row
- Separate consecutive panels with `\addlinespace[4pt]`

### Variable label conventions
- Keep labels under 20 characters (including spaces)
- Use human-friendly labels: `Democrat $\times$ Post` not `dem_post`
- No underscores in labels

### Page-width fitting
- Always use `\begin{tabularx}{\linewidth}{X *{N}{c}}`
- **Do not use `\resizebox`** — it causes `tablenotes` to overflow the page
- For tables with more than 6 columns, wrap the entire `table` environment in `\begin{landscape}...\end{landscape}` (requires `\usepackage{pdflscape}` in preamble)

### Standard errors
- Standard errors are always reported in parentheses directly below the coefficient
- This is handled automatically by esttab with option `se` (see §3)

### Significance stars
- Use three levels: `*` p<0.10, `**` p<0.05, `***` p<0.01
- Always include a note in the footnote: *Standard errors in parentheses. \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.*
- In esttab use: `star(* 0.10 ** 0.05 *** 0.01)`

### Formatting values
- Regression coefficients: 2 significant digits by default
- **Check:** if 2 digits causes any coefficient to display as `0.00`, switch to 3 significant digits for the whole table and flag this to the user
- Specification detail values (mean of dep. var., Adjusted R²): 2 significant digits
- Specification detail labels should be indented by 0.5em
- Observation counts: integers only, no decimal places

### Fixed effects and Controls
- If you have multiple fixed effects, add them on separate lines and indicate where they are used using `\checkmark`
- If you have multiple controls, ask the user which ones should be in the regression and which ones should not be shown


### Footnotes
- Every table has a note
- Format: `\textit{Notes:}` followed by the note text
- The text should be written in natural language and not mathematical notation (e.g. This table presents regression coefficients of expectations on news.)
- Next, include how the outcome and treatment variables were calculated. 
- Next include the controls that are included in each specification (whether shown in the table or not)
- Next include the fixed effects 
- Next describe the samples used. 
- Always end with the stars legend: *{Robust|clustered|two-way clustered} standard errors are in parentheses. \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.*
- Use `\small` inside `tablenotes`

---

## 2. Skeleton LaTeX Template

```latex
\begin{table}[!htp]
\centering
\begin{threeparttable}
\caption{TABLE TITLE}
\label{tab:label}
\begin{tabularx}{\linewidth}{X *{N}{c}}
\midrule\midrule
 & \multicolumn{N-1}{c}{Outcome Variable Name} \\        % omit if columns have the same outcome variable
 & \multicolumn{1}{c}{(1)} & \multicolumn{1}{c}{(2)} \\
\cmidrule(lr){2-3}
Regressor 1    & 0.12** & 0.08*  \\
               & (0.04) & (0.04) \\
Regressor 2    & -0.30* &        \\
               & (0.17) &        \\
\addlinespace[4pt]
\multicolumn{N}{l}{\textit{Specification details}}  \\
\hspace{0.5em} Sample                        & All    & Urban  \\
\hspace{0.5em} Fixed Effects                 & \multicolumn{1}{c}{\(\checkmark\)} & \multicolumn{1}{c}{\(\checkmark\)} \\
\hspace{0.5em} Mean dep. var.                & 0.45   & 0.48   \\
\hspace{0.5em} Adjusted R\textsuperscript{2} & 0.24   & 0.31   \\
\hspace{0.5em} Observations                  & 12{,}000 & 5{,}400 \\
\midrule\midrule
\end{tabularx}
\begin{tablenotes}
\small
\item \textit{Notes:} DESCRIBE TABLE AND SAMPLE DEFINITIONS HERE.
Standard errors in parentheses. * p<0.10, ** p<0.05, *** p<0.01.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

For landscape (> 6 columns):
```latex
\begin{landscape}
\begin{table}[!htp]
  ... (same structure)
\end{table}
\end{landscape}
```

---

## 3. esttab Skeleton

This is the canonical esttab call structure. Adapt options as needed.

```stata
* Step 1 — store estimates
eststo clear
eststo m1: reg y x1, robust
estadd local fe  "\multicolumn{1}{c}{ }", replace
qui sum y if e(sample), meanonly
estadd scalar ymean = r(mean), replace

eststo m2: reghdfe y x1 x2, absorb(fe)
estadd local fe  "\multicolumn{1}{c}{\(\checkmark\)}", replace
qui sum y if e(sample), meanonly
estadd scalar ymean = r(mean), replace

* Step 2 — add specification detail scalars

* Step 3 — export table
esttab m1 m2 using "table.tex", replace ///
    booktabs                          /// use booktabs rules
    se                                /// SEs in parentheses below coef
    star(* 0.10 ** 0.05 *** 0.01)    ///
    label                             /// use variable labels not names
    sfmt(%9.2f %9.2f %9.0f)          /// format: ymean, r2_a, N
    stats(controls fe ymean r2_a N, ///
        labels("Fixed Effects" "Mean dep. var." ///
                "Adjusted R\textsuperscript{2}" "Observations")) ///
    mgroups("Outcome Variable", ///
        pattern(1 0)            ///
        prefix(\multicolumn{@span}{c}{) suffix(}) ///
        span erepeat(\cmidrule(lr){@span})) ///
    mtitles("(1)" "(2)")              /// 
    mlabels(none)                     /// Prevents duplicate model number rows in esttab LaTeX output       
    nodepvars collabels(none)         /// Suppress "b/se" sub-headers
    varlabels(x1 "Variable name")     /// when label is active, use varlabels() to override coefficient display names     
    prehead(                          ///
        "\begin{table}[!htp]"         ///
        "\centering"                  ///
        "\begin{threeparttable}"      ///
        "\caption{TABLE TITLE}"       ///
        "\label{tab:label}"           ///
        "\begin{tabularx}{\linewidth}{>{\raggedright\arraybackslash}X *{@M}{c}}") ///
    posthead("\cmidrule(lr){2-@span}") ///
    prefoot("\addlinespace[4pt]")     ///
    postfoot(                         ///
        "\end{tabularx}"              ///
        "\begin{tablenotes}"          ///
        "\small"                      ///
        "\item \textit{Notes:} NOTES. Standard errors in parentheses. * p<0.10, ** p<0.05, *** p<0.01." ///
        "\end{tablenotes}"            ///
        "\end{threeparttable}"        ///
        "\end{table}")
```

### `estadd local` vs `estadd scalar`
| Use | When |
|---|---|
| `estadd local` | The value is a **string** or uses LaTeX (e.g. `\checkmark`, sample name like "Urban") |
| `estadd scalar` | The value is **numeric** and you want esttab to apply `sfmt` formatting (e.g. mean of dep. var., R²) |

---

## 4. LaTeX Validity Checks

Before returning any table code, mentally compile it through these checks. Flag any failure explicitly.

### 4a. Brace balance
- Every `{` must have a matching `}`
- `\begin{tabularx}{\linewidth}{...}` has three `{` groups — all must close
- `\multicolumn{N}{l}{...}`, `\textit{...}`, `\cmidrule(lr){...}` — each must close

### 4b. Dollar-sign balance
- Every `$` must be paired; unpaired `$` breaks math mode for the rest of the document
- Numbers in cells should not be wrapped in `$...$` unless math is genuinely needed

### 4c. Ampersand count
- Every data row must have exactly **(columns − 1)** `&` separators
- `\cmidrule`, `\addlinespace`, and panel name rows (using `\multicolumn`) have 0 `&` — correct
- Spec detail rows (Sample, Controls, etc.) also need **(columns − 1)** `&`

### 4d. Environment nesting
Correct order: `table` → `threeparttable` → `tabularx` + `tablenotes`
Environments must close in reverse order — no crossing.

### 4e. Checkmark format
Every `\checkmark` indicator must be wrapped: `\multicolumn{1}{c}{\(\checkmark\)}`
A bare `\checkmark` will misalign the column.

### 4f. Escaped paranthesis format
Check that every `\(` is balanced by `\)' 

### Reporting failures
> ⚠️ **LaTeX issue found:** [describe problem and location] — corrected below.

---

## 5. Quick Checklist

- [ ] Top border: `\midrule\midrule`
- [ ] Bottom border: `\midrule\midrule`
- [ ] Column headers appear between `\midrule\midrule` and `\cmidrule` — never skip straight from `\midrule\midrule` to `\cmidrule`
- [ ] Column header underline: `\cmidrule(lr){2-N}` (starts at col 2, not col 1)
- [ ] No `b/se` tags on column headers (`collabels(none)` in esttab)
- [ ] Panel names: italicised, `Panel X: Label` format, `\multicolumn{N}{l}{...}`, no rule below
- [ ] Panel separator: `\addlinespace[4pt]`, no `\midrule`
- [ ] Coefficients formatted to 2 significant digits; none display as `0.00`
- [ ] Spec detail values formatted to 2 significant digits; observations as integers
- [ ] Specification rows separated from regressors by `\addlinespace[4pt]` (via `prefoot`)
- [ ] Spec order: Sample → Controls → Fixed Effects → Mean dep. var. → Adj. R² → Observations
- [ ] All `\checkmark` indicators use `\multicolumn{1}{c}{\(\checkmark\)}`
- [ ] `tabularx{\linewidth}` with `>{\raggedright\arraybackslash}X` first column
- [ ] No `\resizebox`
- [ ] Landscape environment used if > 6 columns
- [ ] `threeparttable` wraps both `tabularx` and `tablenotes`
- [ ] `tablenotes` uses `\small`, placed after `\end{tabularx}`, inside `\end{threeparttable}`
- [ ] Footnote starts with `\textit{Notes:}` and ends with stars legend
- [ ] All `{` have matching `}` (brace count balanced)
- [ ] No stray or unpaired `$` signs
- [ ] Ensure all the single dollar signs `$` are escaped 
- [ ] Ensure the label `_` are not escaped
- [ ] Every data row has exactly (columns − 1) `&` separators
