#!/usr/bin/env python3
"""
Generate Bitcoin value graph with polynomial fit
"""
import matplotlib.pyplot as plt
import numpy as np

# Data points
t = np.array([0, 1, 2])
value = np.array([100000, 80000, 20000])

# Fit polynomial (degree 2)
coeffs = np.polyfit(t, value, 2)
p = np.poly1d(coeffs)

# Generate smooth curve for plotting
t_smooth = np.linspace(0, 2, 100)
value_smooth = p(t_smooth)

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))

# Plot data points
ax.scatter(t, value, color='#D55E00', s=150, zorder=3)

# Plot polynomial fit
ax.plot(t_smooth, value_smooth, color='#0072B2', linewidth=2.5)

# Labels and title
ax.set_ylabel('Bitcoin Value ($)', fontsize=18)
ax.set_title("Alex's Bitcoin: Value Over Time", fontsize=20, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.tick_params(axis='both', labelsize=16)

# Format y-axis as currency
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Set x-axis to show years 2024, 2025, 2026
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['2030', '2031', '2032'])

plt.tight_layout()
plt.savefig('fig/bitcoin_value_graph.pdf', dpi=300, bbox_inches='tight')
print("✓ Bitcoin graph saved to fig/bitcoin_value_graph.pdf")
