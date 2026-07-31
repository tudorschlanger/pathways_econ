#!/usr/bin/env python3
"""
Fetch CPI-U (All Urban Consumers) year-over-year inflation from FRED.
Saves annual average inflation rates to cpi_inflation.csv and a bar chart to cpi_inflation.png.
Series: CPIAUCSL (Consumer Price Index for All Urban Consumers: All Items)
"""
import csv
import urllib.request
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# FRED public CSV download
SERIES = "CPIAUCSL"
URL = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={SERIES}&cosd=2000-01-01&coed=2025-12-31"

def main():
    # Download CSV from FRED
    print(f"Fetching {SERIES} from FRED...")
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        raw = resp.read().decode("utf-8")

    # Parse CSV
    lines = raw.strip().split("\n")
    reader = csv.reader(lines)
    next(reader)  # skip header

    monthly = []
    for row in reader:
        date_str, value_str = row[0], row[1]
        if value_str in (".", ""):
            continue
        year = int(date_str[:4])
        month = int(date_str[5:7])
        value = float(value_str)
        monthly.append((year, month, value))

    # Compute year-over-year inflation for each month, then average by year
    cpi_lookup = {(y, m): v for y, m, v in monthly}

    yoy_by_year = defaultdict(list)
    for y, m, v in monthly:
        prev = cpi_lookup.get((y - 1, m))
        if prev:
            yoy = (v / prev - 1) * 100
            yoy_by_year[y].append(yoy)

    # Annual average inflation
    annual = []
    for year in sorted(yoy_by_year.keys()):
        vals = yoy_by_year[year]
        avg = sum(vals) / len(vals)
        annual.append((year, round(avg, 2)))
        print(f"  {year}: {avg:.2f}%")

    # Save to CSV
    with open("cpi_inflation.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "inflation_pct"])
        w.writerows(annual)
    print("\nSaved to cpi_inflation.csv")

    # Plot
    years = [y for y, _ in annual]
    vals = [v for _, v in annual]

    fig, ax = plt.subplots(figsize=(7, 5.5))
    bars = ax.bar(years, vals, color="#0072B2", edgecolor="#0072B2", width=0.7)

    # Color post-COVID bars differently
    for bar, y in zip(bars, years):
        if y >= 2021:
            bar.set_color("#D55E00")
            bar.set_edgecolor("#D55E00")

    # Fed target line
    ax.axhline(y=2, color="#D55E00", linestyle="--", linewidth=1.5, label="Fed Target: 2%")
    ax.axhline(y=0, color="black", linewidth=0.5)

    ax.set_ylabel("Inflation (%)", fontsize=16)
    ax.set_title("U.S. CPI Inflation (All Urban Consumers)", fontsize=16, fontweight="bold")
    ax.legend(loc="upper left", fontsize=14)
    ax.set_xticks([y for y in years if y % 4 == 1])
    ax.tick_params(labelsize=14)
    ax.set_ylim(-1, 9)
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig("cpi_inflation.png", dpi=200, bbox_inches="tight")
    print("Saved to cpi_inflation.png")

if __name__ == "__main__":
    main()
