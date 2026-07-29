---
name: format-tables
description: >
  Apply a consistent LaTeX table style for table output. Use this skill whenever
  the user is writing code that produces LaTeX tables — including missing
  values tables, sample means tables, and summary statistics tables — or whenever
  they ask to format, fix, or generate any such table. Do not trigger this when 
  formatting regression tables. When in doubt, load this skill.
---

# Stata LaTeX Table Style Guide

This skill governs all LaTeX tables produced. Apply these rules
to every table you write or modify, without exception.

---

## 1. Universal Formatting Rules

These apply to **all** table types.

### Border lines
| Location | Command |
|---|---|
| Top of table | `\midrule\midrule` (double rule) |
| Bottom of table | `\midrule\midrule` (double rule) |
| Under column headers | `\cmidrule(lr){2-N}` where N = last column index (starts at col 2, not col 1) |
| Under Observations row | `\midrule` (single rule) if Observations is at the top of the table |
| Between panels | A small vertical space: `\addlinespace[4pt]` (no `\midrule`) |
| Under panel name | **Nothing** — no rule under panel headers |

Do **not** use `\toprule` or `\bottomrule`; use `\midrule\midrule` for both top and bottom.

### Panel formatting
- Panel names are **italicized**: `\textit{Panel A: Group Name}`
- Panel names use `\multicolumn{N}{l}{...}` to span all columns         
- Panel names used the pattern: `Panel {A/B/C}:` followed by a short label characterizing that group of variables
- No horizontal rule below the panel name row
- Separate consecutive panels with `\addlinespace[4pt]`

### Variable indentation
- Variables within a panel are indented relative to the panel name
- Use `\hspace{0.5em}` before the variable label in the first column

### Variable label conventions
- Keep the variable names under 20 characters (which includes spaces)

### Column name conventions
- Keep the variable names under 20 characters (which includes spaces)
- In a regression table, put the outcome variable name above the number of the specification using the `prehead/posthead` esttab commands
- In a regression table, if the outcome variable is common to all specifications, combine them into one header (e.g. `\multicolumn{N}{c}{Variable Name}`)
- In a regression table, do NOT add the "b/se" tag on the column headers

### Footnotes
- Every table has a note
- Format: `\textit{Notes:}` followed by the note text
- Describe what the table shows and define each sample/column
- Use `tablenotes` inside a `threeparttable` environment (see skeleton template below)

### Page-width fitting
- Every table must use `tabularx{\linewidth}` inside `threeparttable`. This ensures the table fills the text width and notes match the table width exactly.
- If a table has more than 6 columns, put the table into the `landscape` environment 

**Do not use `\resizebox`** — it causes `tablenotes` to overflow the page.

### Large numbers
- If any figures exceed 10^6, express in thousands (/1,000) or millions (/1,000,000)
- Append the unit to the **variable label**, e.g. `Revenue (USD millions)`

---

## 2. Table Type Specifications

### 2a. Missing Values Table

**Default title:** "Sample Coverage"

**Structure:**
- **Columns:** One column per sample (user-defined)
- **Row 1 — Observations:** Raw observation count for each sample
- **Row 2 - Panel name:** Short label characterizing that group of variables
- **Subsequent rows:** For each variable, the share of non-missing observations within each sample
  - Format shares to **2 significant figures** (e.g. `0.94`, `0.073`, not `0.9372`)


**Footnote must explain:** What the table shows (share non-missing), and how each sample column is defined.

---

### 2b. Sample Means Table

**Default title:** "Sample Means"

**Structure:**
- **Columns:** One column per sample (user-defined)
- **Row 1 — Observations:** Raw observation count for each sample
- **Subsequent rows:** Mean value of each variable within the respective sample

**Footnote must explain:** What the table shows (means), and how each sample column is defined.

---

### 2c. Summary Statistics Table

**Default title:** "Summary Statistics"

**Structure:**
- **Columns (fixed order):** Observations | Mean | Std. Dev. | Min | P10 | Median | P90 | Max
- **Rows:** One per variable

**Footnote must explain:** What the table shows and how the sample is defined.

### 2d. Regression Table

**Default title:** "Regression table"

**Structure:**
- **Columns (fixed order):** Specification (1) | Specification (2)  
- **Rows:** One per regressor, or specification information (e.g. Fixed effects, Observations)

**Footnote must explain:** What the table shows and how the sample is defined.

---

## 3. Skeleton Template

Use this as the base for all three table types (adapt column count and content):

```latex
\begin{table}[!htp]
\centering
\begin{threeparttable}
\caption{TABLE TITLE}
\label{tab:label}
\begin{tabularx}{\linewidth}{X *{N}{c}}
\midrule\midrule
...
\midrule\midrule
\end{tabularx}
\begin{tablenotes}
\small
\item \textit{Notes:} NOTES HERE.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

**Key structure:** `threeparttable` wraps both `tabularx` and `tablenotes`. The `tabularx{\linewidth}` fills exactly the text column, so `tablenotes` inherits the correct width and will not overflow.

---

## 4. LaTeX Validity Checks

Before returning any table code, **mentally compile** the LaTeX by running through each of these checks. Flag any failure explicitly to the user.

### 4a. Brace balance
Every `{` must have a matching `}`. Count them:
- `\begin{tabularx}{\linewidth}{...}` — three `{` groups that must each close
- `\begin{threeparttable}` is closed by `\end{threeparttable}`
- `\textit{...}`, `\multicolumn{...}{...}{...}`, `\cmidrule(lr){...}` — each pair must close

### 4b. Dollar-sign balance (`$`)
- Math mode delimiters must come in pairs: every opening `$` needs a closing `$`
- Numbers in table cells should **not** be wrapped in `$...$` unless math formatting is genuinely needed
- Stray `$` (e.g. from a copy-paste of a variable label like `$wage`) will break compilation

### 4c. Ampersand count (`&`)
- Every data row must have exactly **(number of columns - 1)** ampersands
- Panel name rows span the full width and typically have **0** ampersands (or use `\multicolumn`)
- `\cmidrule` and `\addlinespace` lines have no `&` — that is correct
- A row with too few or too many `&` produces an "Extra alignment tab" or "Missing \cr" error

### 4d. Environment nesting
Correct nesting order (outer -> inner):
`table` -> `threeparttable` -> `tabularx` / `tablenotes`
Environments must close in reverse order — no crossing.

### Reporting failures
If any check fails, report it like this before showing corrected code:
> **LaTeX issue found:** [describe the problem and line/context] — corrected below.

---

## 5. Quick Checklist

Before finalising any table, verify:

- [ ] Top border: `\midrule\midrule`
- [ ] Bottom border: `\midrule\midrule`
- [ ] Column header underline: `\cmidrule(lr){2-N}` (not starting at col 1)
- [ ] Check that `\midrule\midrule` is never followed by `\cmidrule(lr){2-N}`
- [ ] Panel names: italicised, `Panel X: Label` format, no rule below
- [ ] Panel separator: `\addlinespace[4pt]`, no `\midrule`
- [ ] Variables indented with `\hspace{1em}`
- [ ] Large numbers converted; unit noted in label
- [ ] Footnote starts with `\textit{Notes:}`
- [ ] Title matches default (or user has specified otherwise)
- [ ] Shares (missing values table) formatted to 2 significant figures
- [ ] `tabularx{\linewidth}` used (not `\resizebox`)
- [ ] `threeparttable` wraps both `tabularx` and `tablenotes`
- [ ] `tablenotes` placed after `\end{tabularx}`, inside `threeparttable`
- [ ] All `{` have matching `}` (brace count balanced)
- [ ] No stray or unpaired `$` signs
- [ ] Every data row has exactly (columns - 1) `&` separators
