# Python Data Analysis Project - Energy Trading Insights
# Author: Data Analytics Portfolio

import pandas as pd
import numpy as np

# -----------------------------
# 1. Create Sample Dataset
# -----------------------------
data = {
    "trade_id": [1, 2, 3, 4, 5, 6],
    "trade_date": pd.to_datetime([
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-04", "2024-01-05", "2024-01-06"
    ]),
    "commodity": ["Gas", "Power", "Gas", "Oil", "Power", "Gas"],
    "volume": [100, 200, 150, 80, 220, 130],
    "price": [3.2, 4.1, 3.5, 70, 4.3, 3.6],
    "pnl": [120, -50, 200, 500, 80, 150]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Basic Data Exploration
# -----------------------------
print("Dataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# 3. Business Analysis
# -----------------------------

# Total PnL by commodity
pnl_by_commodity = df.groupby("commodity")["pnl"].sum()
print("\nTotal PnL by Commodity:")
print(pnl_by_commodity)

# Total volume by commodity
volume_by_commodity = df.groupby("commodity")["volume"].sum()
print("\nTotal Volume by Commodity:")
print(volume_by_commodity)

# Best performing trade
best_trade = df.loc[df["pnl"].idxmax()]
print("\nBest Performing Trade:")
print(best_trade)

# Worst performing trade
worst_trade = df.loc[df["pnl"].idxmin()]
print("\nWorst Performing Trade:")
print(worst_trade)

# -----------------------------
# 4. Simple Insights
# -----------------------------
print("\nInsights:")
print("- Gas shows consistent positive performance")
print("- Oil trade has highest single trade profit")
print("- Power shows mixed performance")

# ------------------------
# 5. Visualization (Matplotlib)
# ------------------------

import matplotlib.pyplot as plt

# Total PnL by Commodity (Bar Chart)
pnl_by_commodity = df.groupby("commodity")["pnl"].sum()

plt.figure()
pnl_by_commodity.plot(kind="bar")
plt.title("Total PnL by Commodity")
plt.xlabel("Commodity")
plt.ylabel("PnL")
plt.xticks(rotation=0)
plt.show()

# Total Volume by Commodity (Bar Chart)
volume_by_commodity = df.groupby("commodity")["volume"].sum()

plt.figure()
volume_by_commodity.plot(kind="bar")
plt.title("Total Volume by Commodity")
plt.xlabel("Commodity")
plt.ylabel("Volume")
plt.xticks(rotation=0)
plt.show()
