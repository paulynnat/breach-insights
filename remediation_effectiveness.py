import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 🎯 Set up file paths
DATA_DIR    = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\data"
VISUALS_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\visuals"

# 🛠️ Ensure folders exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

# 📊 Remediation actions dataset
remediation_data = {
    "Remediation Action": [
        "Backup Recovery",
        "2FA Rollout",
        "Policy Enforcement",
        "Staff Training",
        "System Migration",
        "No Remediation"
    ],
    "Cases Involving": [4, 3, 5, 6, 3, 4],
    "Penalty Outcome": [
        "Warning / None",
        "Warning",
        "Mixed",
        "Reduced / Warning",
        "Reduced Penalty",
        "Full Penalty"
    ]
}

df_remediation = pd.DataFrame(remediation_data)

# 💾 Save CSV to /data folder
csv_path = os.path.join(DATA_DIR, "remediation.csv")
df_remediation.to_csv(csv_path, index=False)
print(f"✅ CSV saved to: {csv_path}")

# 📈 Plot: Remediation Actions
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
sns.barplot(
    data=df_remediation,
    x="Cases Involving",
    y="Remediation Action",
    palette="crest"
)
plt.title("Remediation Actions — PDPC Case Distribution", fontsize=14)
plt.xlabel("Cases Involving")
plt.ylabel("Remediation Action")
plt.tight_layout()

# 💾 Save chart to /visuals folder
chart_path = os.path.join(VISUALS_DIR, "remediation_actions_chart.png")
plt.savefig(chart_path)
print(f"✅ Chart saved to: {chart_path}")

# 👀 Display chart live
plt.show()