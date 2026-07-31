"""Plot monthly end-of-period Enron closing prices (1998–2001)."""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("enron_stock_1998_2001.csv", parse_dates=["Date"])
df = df.set_index("Date")

# Resample to monthly, keeping last observation of each month
monthly = df["Close"].resample("ME").last()

fig, ax = plt.subplots(figsize=(4.5, 3.2))
ax.plot(monthly.index, monthly.values, color="#d62728", linewidth=2)
ax.fill_between(monthly.index, monthly.values, alpha=0.15, color="#d62728")

ax.set_xlabel("Year", fontsize=10)
ax.set_ylabel("Closing Price ($)", fontsize=10)
ax.set_title("Enron Stock Price (Monthly)", fontsize=11, fontweight="bold")

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.set_ylim(bottom=0)
ax.grid(True, alpha=0.3)
ax.tick_params(labelsize=9)

fig.tight_layout()
fig.savefig("enron_stock_monthly.pdf", bbox_inches="tight")
print("Saved to enron_stock_monthly.pdf")
