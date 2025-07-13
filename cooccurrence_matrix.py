import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from itertools import combinations

# File paths
DATA_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\data"
VISUALS_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\visuals"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

# Simulated breach records with tag lists
records = [
    ["Password Hygiene Failure", "No 2FA / MFA Enforcement", "CRM System Exposure"],
    ["Vendor Oversight Failure", "Protection Obligation Breach", "No MFA"],
    ["Dormant Credential Exposure", "No MFA", "Web Portal Misconfiguration"],
    ["Protection Obligation Breach", "Retention Violation"],
    ["Development Environment Exposure", "No MFA"]
]

# Flatten and count pairwise co-occurrences
pairs = []
for tags in records:
    for combo in combinations(sorted(tags), 2):
        pairs.append(combo)

co_df = pd.DataFrame(pairs, columns=["Tag A", "Tag B"])
matrix = co_df.value_counts().reset_index(name="Count")

# Pivot into co-occurrence matrix
pivot = matrix.pivot(index="Tag A", columns="Tag B", values="Count").fillna(0)

# Save matrix CSV
csv_path = os.path.join(DATA_DIR, "cooccurrence_matrix.csv")
pivot.to_csv(csv_path)
print(f"✅ Matrix saved to: {csv_path}")

# Plot heatmap
plt.figure(figsize=(12,10))
sns.heatmap(pivot, annot=True, cmap="YlGnBu", fmt=".0f", linewidths=0.5)
plt.title("Breach Tag Co-occurrence Matrix", fontsize=16)
plt.tight_layout()

# Save chart
chart_path = os.path.join(VISUALS_DIR, "cooccurrence_matrix.png")
plt.savefig(chart_path)
print(f"✅ Chart saved to: {chart_path}")
plt.show()