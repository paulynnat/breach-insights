import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 🎯 File paths
DATA_DIR    = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\data"
VISUALS_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\visuals"

# 🛠️ Ensure folders exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

# 📊 Sample breach surface data
risk_data = {
    "Platform Type": [
        "CRM System",
        "Email Server",
        "Cloud Drive",
        "Point-of-Sale (POS)",
        "Web Database",
        "Internal Git Repo",
        "Shared Drive",
        "Unsecured Webform"
    ],
    "Cases Observed": [6, 9, 4, 3, 5, 2, 3, 4],
    "Example Breach": [
        "Unencrypted client records",
        "Phished credentials",
        "Misconfigured access rights",
        "Payment data exposed",
        "SQL injection exposure",
        "Token leak in repo",
        "Overshared folders",
        "Webform without HTTPS"
    ]
}

df_risks = pd.DataFrame(risk_data)

# 💾 Save CSV
csv_path = os.path.join(DATA_DIR, "infrastructure.csv")
df_risks.to_csv(csv_path, index=False)
print(f"✅ CSV saved to: {csv_path}")

# 📈 Plot breach surface chart
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
sns.barplot(
    data=df_risks,
    x="Cases Observed",
    y="Platform Type",
    palette="flare"
)
plt.title("Infrastructure Risk Map — Breach Surface by Platform", fontsize=14)
plt.xlabel("Cases Observed")
plt.ylabel("Platform Type")
plt.tight_layout()

# 💾 Save chart
chart_path = os.path.join(VISUALS_DIR, "infrastructure_risks_chart.png")
plt.savefig(chart_path)
print(f"✅ Chart saved to: {chart_path}")

# 👀 Display chart
plt.show()