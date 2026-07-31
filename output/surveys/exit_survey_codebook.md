# Exit Survey — Codebook

**Source:** `doc/Exit Surveys/Exit survey Pathways 2026.pdf` (24 pages = 12 respondents; each respondent is a consecutive page pair — page 1 = Parts 1–2, page 2 = Parts 3–5).
**Unit of observation:** one individual (row).
**Data file:** `exit_survey_data.csv`.
**Missing / unreadable:** empty cell (`NA`). Ambiguous marks are flagged in `extraction_notes`.

## Identifiers

| Variable | Type | Values / Coding |
|---|---|---|
| `respondent_id` | int | 1–12, in PDF order |
| `scan_pages` | str | source page pair, e.g. `1-2` |

## Part 1 — Quick facts

| Variable | Type | Values / Coding |
|---|---|---|
| `grade` | int | 9, 10, 11, 12; `NA` if only "Other" marked |
| `grade_other` | str | free text written next to "Other" (else empty) |
| `prior_study` | categorical | `class_school` = Yes, a class at school; `self` = Yes, on my own; `informal` = A little, informally; `none_first` = No, first exposure |
| `prior_interest` | ordinal 1–5 | 1 = Not at all, 2 = A little, 3 = Somewhat, 4 = Very, 5 = Already a top interest |

## Part 2 — What you thought about the course

**Q4 grid** — each cell is an independent 0/1 indicator (respondents often marked more than one per column).

| Variable | Type | Values |
|---|---|---|
| `interesting_day1` … `interesting_day5` | 0/1 | 1 = that day marked "Interesting" |
| `useful_day1` … `useful_day5` | 0/1 | 1 = that day marked "Useful outside school" |
| `hard_day1` … `hard_day5` | 0/1 | 1 = that day marked "Hardest to follow" |

Day key: 1 = Economic Decision-Making, 2 = Correlation vs Causation, 3 = Markets & Externalities, 4 = Trade & Tariffs, 5 = Financial Literacy.

**Q5 learning methods** — 0/1 each (respondents often marked more than the "up to two" limit).

| Variable | Meaning |
|---|---|
| `learn_board` | Instructor explaining at the board |
| `learn_discussion` | Whole-class discussion or debate |
| `learn_smallgroup` | Small-group activities |
| `learn_games` | Games and simulations |
| `learn_slides` | Slides and handouts |
| `learn_news` | Real-world news examples |
| `learn_other` | "Other" box marked |
| `learn_other_text` | free text next to "Other" (else empty) |

| Variable | Type | Values |
|---|---|---|
| `recommend` | ordinal 1–5 | 1 = Definitely not, 2 = Probably not, 3 = Not sure, 4 = Probably, 5 = Definitely |

## Part 3 — How the workshop changed how you think

Scale: 1 = Much less than before, 2 = Somewhat less, 3 = About the same, 4 = Somewhat more, 5 = Much more than before.

| Variable | Item |
|---|---|
| `p3_relevant_life` | Q7 — economics is relevant to my daily life |
| `p3_gov_policy_interest` | Q8 — interested in how governments make policy |
| `p3_confidence_adults` | Q9 — confident discussing economic ideas with adults |
| `p3_want_hs_class` | Q10 — want to take an econ/finance class in high school |
| `p3_want_college_econ` | Q11 — interested in studying economics in college |

## Part 4 — Teaching

Scale: 1 = Strongly disagree, 2 = Disagree, 3 = Neutral, 4 = Agree, 5 = Strongly agree.

| Variable | Item |
|---|---|
| `teach_clear` | Q12 — explained ideas clearly |
| `teach_interesting` | Q13 — made the material interesting |
| `teach_encouraged_questions` | Q14 — encouraged questions and discussion |
| `teach_comfortable_confused` | Q15 — I felt comfortable saying when confused |
| `teach_understood_point` | Q16 — I understood the point of each lesson |
| `teach_examples_relevant` | Q17 — examples connected to things I care about |

## Part 5 — Open feedback

| Variable | Type | Values |
|---|---|---|
| `feedback_text` | str | verbatim transcription (empty if blank) |
| `extraction_notes` | str | any ambiguity/flags noted during transcription |
