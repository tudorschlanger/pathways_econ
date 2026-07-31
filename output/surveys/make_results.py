#!/usr/bin/env python3
"""Summarize exit_survey_data.csv into figures + printed stats for the results report.
Charts follow the dataviz light/print palette. No pandas (uses csv + numpy)."""
import csv, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "fig")
os.makedirs(FIG, exist_ok=True)

# ---- palette (dataviz reference, light mode) ----
INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
BLUE, ORANGE, AQUA, RED, GREEN = "#2a78d6", "#eb6834", "#1baf7a", "#e34948", "#008300"
# diverging 5-step (neg dark->light, neutral, pos light->dark)
LIK = ["#c0392b", "#f2b0ae", "#dedcd5", "#a9cbf4", "#2a78d6"]

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "text.color": INK, "axes.labelcolor": INK, "axes.edgecolor": MUTED,
    "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150, "savefig.bbox": "tight",
})

# ---------------- load ----------------
rows = list(csv.DictReader(open(os.path.join(HERE, "exit_survey_data.csv"))))
N = len(rows)
def col(c): return [r[c] for r in rows]
def inums(c): return [int(r[c]) for r in rows if r[c] not in ("", None)]

def dist(c):  # counts of levels 1..5
    v = inums(c); return [v.count(k) for k in range(1, 6)], (np.mean(v) if v else float("nan")), len(v)

# ---------------- print summary ----------------
print(f"N = {N}\n")
from collections import Counter
print("grade:", dict(sorted(Counter(inums('grade')).items())))
print("prior_study:", dict(Counter(col('prior_study'))))
d, m, n = dist('prior_interest'); print(f"prior_interest dist(1-5)={d} mean={m:.2f}\n")

DAYLAB = {1:"Day 1\nDecision-Making", 2:"Day 2\nCorrelation vs\nCausation",
          3:"Day 3\nMarkets &\nExternalities", 4:"Day 4\nTrade &\nTariffs",
          5:"Day 5\nFinancial\nLiteracy"}
interesting = [sum(int(r[f'interesting_day{i}']) for r in rows) for i in range(1,6)]
useful      = [sum(int(r[f'useful_day{i}'])      for r in rows) for i in range(1,6)]
hard        = [sum(int(r[f'hard_day{i}'])        for r in rows) for i in range(1,6)]
print("Q4 interesting by day:", interesting)
print("Q4 useful by day     :", useful)
print("Q4 hard by day       :", hard, "\n")

LEARN = [("learn_board","Instructor at the board"),
         ("learn_discussion","Whole-class discussion / debate"),
         ("learn_smallgroup","Small-group activities"),
         ("learn_games","Games & simulations"),
         ("learn_slides","Slides & handouts"),
         ("learn_news","Real-world news examples"),
         ("learn_other","Other")]
learn_counts = [(lab, sum(int(r[k]) for r in rows)) for k,lab in LEARN]
print("learning methods:", learn_counts, "\n")

dR, mR, nR = dist('recommend')
print(f"recommend dist(1-5)={dR} mean={mR:.2f} pct>=4={100*sum(dR[3:])/nR:.0f}%\n")

TEACH = [("teach_clear","Explained ideas clearly"),
         ("teach_interesting","Made the material interesting"),
         ("teach_encouraged_questions","Encouraged questions & discussion"),
         ("teach_comfortable_confused","I felt comfortable saying I was confused"),
         ("teach_understood_point","I understood the point of each lesson"),
         ("teach_examples_relevant","Examples connected to things I care about")]
P3 = [("p3_relevant_life","Economics is relevant to my daily life"),
      ("p3_gov_policy_interest","Interested in how governments make policy"),
      ("p3_confidence_adults","Confident discussing economics with adults"),
      ("p3_want_hs_class","Want an econ / finance class in high school"),
      ("p3_want_college_econ","Interested in studying economics in college")]
print("== Teaching (mean, %>=4) ==")
for k,lab in TEACH:
    d_,m_,n_ = dist(k); print(f"  {lab:48s} mean={m_:.2f} pos={100*sum(d_[3:])/n_:3.0f}% dist={d_}")
print("== Attitude shift (mean, %>=4) ==")
for k,lab in P3:
    d_,m_,n_ = dist(k); print(f"  {lab:48s} mean={m_:.2f} more={100*sum(d_[3:])/n_:3.0f}% dist={d_}")
print("\n== open feedback ==")
for r in rows:
    if r['feedback_text'].strip():
        print(f"  r{r['respondent_id']} (rec={r['recommend']}): {r['feedback_text']}")

# ---------------- charts ----------------
def bar_labels(ax, bars, vals, color=INK, dx=0, dy=0, fmt="{:.0f}", small=False):
    for b,v in zip(bars, vals):
        if v == 0: continue
        ax.text(b.get_x()+b.get_width()/2+dx, b.get_height()+b.get_y()+dy,
                fmt.format(v), ha="center", va="bottom",
                fontsize=8 if small else 9, color=color)

def diverging_likert(items, scale_labels, fname, title, xlabel="Number of respondents"):
    """items: list of (label, key). Sorted by % positive (levels 4-5) desc -> best on top."""
    data = []
    for key,lab in items:
        d_,_,n_ = dist(key); data.append((lab, d_, n_))
    data.sort(key=lambda t: (t[1][3]+t[1][4])/t[2])  # ascending; barh puts first at bottom
    fig, ax = plt.subplots(figsize=(7.4, 0.62*len(items)+1.15))
    for y,(lab,c,n_) in enumerate(data):
        neu = c[2]
        x = -(c[0]+c[1]+neu/2)
        for idx in range(5):
            w = c[idx]
            if w:
                ax.barh(y, w, left=x, color=LIK[idx], edgecolor="white", linewidth=1.2, height=0.62)
                tc = "white" if idx in (0,4) else INK
                ax.text(x+w/2, y, str(w), ha="center", va="center", fontsize=8, color=tc)
            x += w
    ax.axvline(0, color=INK2, lw=1)
    ax.set_yticks(range(len(data)), [t[0] for t in data], fontsize=9)
    ax.set_xlabel(xlabel, fontsize=9, color=INK2)
    left  = max(c[0]+c[1]+c[2]/2 for _,c,_ in data)
    right = max(c[3]+c[4]+c[2]/2 for _,c,_ in data)
    ax.set_xlim(-left-1.5, right+1.5)
    ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
    ax.set_title(title, fontsize=11, fontweight="bold", loc="left", pad=20, color=INK)
    handles = [Patch(facecolor=LIK[i], edgecolor="white", label=scale_labels[i]) for i in range(5)]
    ax.legend(handles=handles, ncol=5, fontsize=7.3, loc="lower left",
              bbox_to_anchor=(0,1.0), frameon=False, handlelength=1.1, columnspacing=1.0)
    fig.savefig(os.path.join(FIG, fname)); plt.close(fig)
    print("wrote", fname)

diverging_likert(TEACH, ["Strongly disagree","Disagree","Neutral","Agree","Strongly agree"],
                 "fig_teaching.pdf", "Teaching: student agreement with each statement")
diverging_likert(P3, ["Much less","Somewhat less","About the same","Somewhat more","Much more"],
                 "fig_attitude.pdf", "Shift in attitudes after the workshop")

# recommend single diverging bar
fig, ax = plt.subplots(figsize=(7.4, 1.5))
c = dR; neu=c[2]; x=-(c[0]+c[1]+neu/2)
for idx in range(5):
    w=c[idx]
    if w:
        ax.barh(0, w, left=x, color=LIK[idx], edgecolor="white", linewidth=1.2, height=0.5)
        ax.text(x+w/2,0,str(w),ha="center",va="center",fontsize=8,color=("white" if idx in (0,4) else INK))
    x+=w
ax.axvline(0,color=INK2,lw=1)
ax.set_yticks([0],["Would recommend\nto a friend"],fontsize=9)
ax.set_xlim(-(c[0]+c[1]+c[2]/2)-1.5, (c[3]+c[4]+c[2]/2)+1.5); ax.set_xticks([])
ax.spines["bottom"].set_visible(False)
h=[Patch(facecolor=LIK[i],edgecolor="white",label=l) for i,l in
   enumerate(["Definitely not","Probably not","Not sure","Probably","Definitely"])]
ax.legend(handles=h,ncol=5,fontsize=7.3,loc="lower left",bbox_to_anchor=(0,1.0),
          frameon=False,handlelength=1.1,columnspacing=1.0)
ax.set_title("Would you recommend this workshop to a friend?",fontsize=11,fontweight="bold",loc="left",pad=20)
fig.savefig(os.path.join(FIG,"fig_recommend.pdf")); plt.close(fig); print("wrote fig_recommend.pdf")

# days grouped bar
fig, ax = plt.subplots(figsize=(7.4, 3.4))
x = np.arange(5); w = 0.26
b1=ax.bar(x-w, interesting, w, color=BLUE,  label="Interesting")
b2=ax.bar(x,   useful,      w, color=AQUA,  label="Useful outside school")
b3=ax.bar(x+w, hard,        w, color=RED,   label="Hardest to follow")
for bars,vals in [(b1,interesting),(b2,useful),(b3,hard)]:
    for b,v in zip(bars,vals):
        if v: ax.text(b.get_x()+b.get_width()/2, v+0.12, str(v), ha="center", va="bottom", fontsize=8, color=INK2)
ax.set_xticks(x, [DAYLAB[i] for i in range(1,6)], fontsize=8.3)
ax.set_ylabel("Number of respondents", fontsize=9, color=INK2)
ax.set_ylim(0, max(interesting+useful+hard)+1.2)
ax.yaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
ax.legend(fontsize=8.3, frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5,1.12))
ax.set_title("Which days landed best — and which were hardest", fontsize=11, fontweight="bold", loc="left", pad=24)
fig.savefig(os.path.join(FIG,"fig_days.pdf")); plt.close(fig); print("wrote fig_days.pdf")

# learning methods horizontal bar (single hue)
lc = sorted(learn_counts, key=lambda t: t[1])
fig, ax = plt.subplots(figsize=(7.4, 3.0))
yy = np.arange(len(lc))
bars = ax.barh(yy, [v for _,v in lc], color=BLUE, height=0.62)
for b,(_,v) in zip(bars, lc):
    if v: ax.text(v+0.1, b.get_y()+b.get_height()/2, str(v), va="center", fontsize=8.5, color=INK2)
ax.set_yticks(yy, [l for l,_ in lc], fontsize=9)
ax.set_xlabel("Number of respondents who found it most helpful", fontsize=9, color=INK2)
ax.set_xlim(0, max(v for _,v in lc)+1)
ax.xaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
ax.set_title("Which ways of learning helped most", fontsize=11, fontweight="bold", loc="left", pad=10)
fig.savefig(os.path.join(FIG,"fig_learning.pdf")); plt.close(fig); print("wrote fig_learning.pdf")

print("\nDONE")
