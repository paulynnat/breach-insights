import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 📁 Set up paths
DATA_DIR    = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\data"
VISUALS_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\visuals"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

# 📊 Sample hygiene risk records
records = [
    {
        "Entity": "Ascentis Pte Ltd",
        "Sector": "Retail / Loyalty",
        "Hygiene Failures": [
            "No MFA Enforcement",
            "Shared Credentials",
            "Weak Password Policy"
        ]
    },
    {
        "Entity": "Autobahn Rent A Car Pte. Ltd.",
        "Sector": "Transport / Car Rental",
        "Hygiene Failures": [
            "Dormant Admin Account",
            "No MFA Enforcement",
            "Unrevoked Credentials"
        ]
    },
    {
        "Entity": "ABC Insurance Co.",
        "Sector": "Insurance",
        "Hygiene Failures": [
            "No MFA Enforcement",
            "Hardcoded Credentials"
        ]
    }
]

# 🔄 Flatten into tag counts
tag_counts = {}
for record in records:
    for tag in record["Hygiene Failures"]:
        tag_counts[tag] = tag_counts.get(tag, 0) + 1

df_hygiene = pd.DataFrame(list(tag_counts.items()), columns=["Hygiene Failure", "Cases Observed"])

# 💾 Save CSV
csv_path = os.path.join(DATA_DIR, "credential_hygiene.csv")
df_hygiene.to_csv(csv_path, index=False)
print(f"✅ CSV saved to: {csv_path}")

# 📈 Plot hygiene breakdown
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
sns.barplot(
    data=df_hygiene,
    x="Cases Observed",
    y="Hygiene Failure",
    palette="crest"
)
plt.title("Credential Hygiene Breakdown — PDPC Case Analysis", fontsize=14)
plt.xlabel("Cases Observed")
plt.ylabel("Hygiene Failure Type")
plt.tight_layout()

# 💾 Save chart
chart_path = os.path.join(VISUALS_DIR, "credential_hygiene_chart.png")
plt.savefig(chart_path)
print(f"✅ Chart saved to: {chart_path}")
plt.show()