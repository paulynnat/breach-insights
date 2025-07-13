import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 📁 Set up paths
DATA_DIR    = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\data"
VISUALS_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\visuals"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

# 📊 Sample breach records across jurisdictions
records = [
    {
        "Jurisdiction": "Singapore",
        "Entity": "Ascentis Pte Ltd",
        "Tags": ["Protection Breach", "No MFA", "Vendor Oversight"],
        "Penalty": 10000,
        "Remediation": ["MFA rollout", "Firewall block"]
    },
    {
        "Jurisdiction": "Singapore",
        "Entity": "Autobahn Rent A Car",
        "Tags": ["Protection Breach", "Dormant Credentials", "No MFA"],
        "Penalty": 3000,
        "Remediation": ["Credential revocation", "Cyber hygiene training"]
    },
    {
        "Jurisdiction": "France",
        "Entity": "RetailTech SAS",
        "Tags": ["Retention Violation", "Unencrypted Backup"],
        "Penalty": 25000,
        "Remediation": ["Retention policy update", "Encryption enforced"]
    },
    {
        "Jurisdiction": "EU",
        "Entity": "CloudServe GmbH",
        "Tags": ["Protection Breach", "No MFA", "Hardcoded Credentials"],
        "Penalty": 50000,
        "Remediation": ["MFA rollout", "Credential audit"]
    }
]

# 🔄 Flatten tag frequency by jurisdiction
tag_data = []
for r in records:
    for tag in r["Tags"]:
        tag_data.append({"Jurisdiction": r["Jurisdiction"], "Tag": tag})

df_tags = pd.DataFrame(tag_data)
tag_freq = df_tags.groupby(["Jurisdiction", "Tag"]).size().reset_index(name="Count")

# 💾 Save tag frequency CSV
csv_path = os.path.join(DATA_DIR, "jurisdiction_tag_compare.csv")
tag_freq.to_csv(csv_path, index=False)
print(f"✅ Tag frequency saved to: {csv_path}")

# 📈 Plot tag comparison
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
sns.barplot(
    data=tag_freq,
    x="Tag",
    y="Count",
    hue="Jurisdiction",
    palette="Set2"
)
plt.title("Breach Tag Frequency by Jurisdiction", fontsize=14)
plt.xlabel("Tag")
plt.ylabel("Frequency")
plt.xticks(rotation=30)
plt.tight_layout()

# 💾 Save chart
chart_path = os.path.join(VISUALS_DIR, "jurisdiction_tag_compare_chart.png")
plt.savefig(chart_path)
print(f"✅ Chart saved to: {chart_path}")
plt.show()