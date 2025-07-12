import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 🎯 File paths for data and visuals
DATA_DIR    = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\data"
VISUALS_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\visuals"

# 🛠️ Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

# 📊 Breach taxonomy dataset
taxonomy_data = {
    "Taxonomy Tag": [
        "Protection Obligation Breach",
        "Ransomware Infection",
        "Password Hygiene Failure",
        "Vendor Oversight Failure",
        "Indexed Exposure",
        "No 2FA / MFA Enforcement",
        "Development Environment Exposure",
        "Retention Violation"
    ],
    "Case Count": [22, 7, 6, 6, 5, 4, 4, 5]
}

df_taxonomy = pd.DataFrame(taxonomy_data)

# 💾 Export CSV to /data folder
csv_path = os.path.join(DATA_DIR, "taxonomy.csv")
df_taxonomy.to_csv(csv_path, index=False)
print(f"✅ CSV saved to: {csv_path}")

# 📈 Plot breach tag frequency
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
sns.barplot(
    data=df_taxonomy,
    x="Case Count",
    y="Taxonomy Tag",
    palette="mako"
)
plt.title("Breach Taxonomy Frequency — PDPC Cases", fontsize=14)
plt.xlabel("Case Count")
plt.ylabel("Taxonomy Tag")
plt.tight_layout()

# 💾 Save chart to /visuals folder
chart_path = os.path.join(VISUALS_DIR, "taxonomy_frequency.png")
plt.savefig(chart_path)
print(f"✅ Chart saved to: {chart_path}")

# 👀 Display live chart
plt.show()