import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# 📁 Set up paths
DATA_DIR    = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\data"
VISUALS_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\visuals"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

# 📊 Sample breach timeline records
records = [
    {
        "Entity": "Ascentis Pte Ltd",
        "Sector": "Retail / Loyalty",
        "Breach Date": "2023-08-30",
        "Discovery Date": "2023-09-10",
        "Remediation Date": "2023-09-15"
    },
    {
        "Entity": "Autobahn Rent A Car Pte. Ltd.",
        "Sector": "Transport / Car Rental",
        "Breach Date": "2022-09-10",
        "Discovery Date": "2022-09-24",
        "Remediation Date": "2022-10-21"
    },
    {
        "Entity": "ABC Insurance Co.",
        "Sector": "Insurance",
        "Breach Date": "2023-03-01",
        "Discovery Date": "2023-03-03",
        "Remediation Date": "2023-03-05"
    }
]

# 🧮 Calculate lag durations
for r in records:
    r["Lag (Discovery)"] = (datetime.strptime(r["Discovery Date"], "%Y-%m-%d") - datetime.strptime(r["Breach Date"], "%Y-%m-%d")).days
    r["Lag (Remediation)"] = (datetime.strptime(r["Remediation Date"], "%Y-%m-%d") - datetime.strptime(r["Discovery Date"], "%Y-%m-%d")).days

df_lag = pd.DataFrame(records)

# 💾 Save CSV
csv_path = os.path.join(DATA_DIR, "retention_lag.csv")
df_lag.to_csv(csv_path, index=False)
print(f"✅ CSV saved to: {csv_path}")

# 📈 Plot lag durations
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
sns.barplot(
    data=df_lag.melt(id_vars=["Entity"], value_vars=["Lag (Discovery)", "Lag (Remediation)"]),
    x="value",
    y="Entity",
    hue="variable",
    palette="flare"
)
plt.title("Breach Response Lag — Discovery vs Remediation", fontsize=14)
plt.xlabel("Days")
plt.ylabel("Entity")
plt.legend(title="Lag Type")
plt.tight_layout()

# 💾 Save chart
chart_path = os.path.join(VISUALS_DIR, "retention_lag_chart.png")
plt.savefig(chart_path)
print(f"✅ Chart saved to: {chart_path}")
plt.show()