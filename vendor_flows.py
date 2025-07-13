import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.graph_objects as go

# 📁 Set up paths
DATA_DIR    = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\data"
VISUALS_DIR = r"C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights\visuals"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

# 📊 Sample vendor flow records
records = [
    {
        "Origin": "Starbucks Singapore",
        "Processor": "Ascentis Pte Ltd",
        "Vendor": "Kyanon Digital Co. Ltd"
    },
    {
        "Origin": "Autobahn Rent A Car Pte. Ltd.",
        "Processor": None,
        "Vendor": None
    },
    {
        "Origin": "ABC Insurance Co.",
        "Processor": "SecureData SG",
        "Vendor": "CloudHost Systems"
    }
]

df_flows = pd.DataFrame(records)

# 💾 Save flow data to CSV
csv_path = os.path.join(DATA_DIR, "vendor_flows.csv")
df_flows.to_csv(csv_path, index=False)
print(f"✅ Flow data saved to: {csv_path}")

# 📈 Plot: Sankey-like Entity Flows
# Only include non-null flows
valid_flows = df_flows.dropna()

entities = pd.unique(valid_flows[["Origin", "Processor", "Vendor"]].values.ravel())
entity_dict = {name: i for i, name in enumerate(entities)}

source = []
target = []
value  = []

for _, row in valid_flows.iterrows():
    source.append(entity_dict[row["Origin"]])
    target.append(entity_dict[row["Processor"]])
    value.append(1)

    source.append(entity_dict[row["Processor"]])
    target.append(entity_dict[row["Vendor"]])
    value.append(1)

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=list(entity_dict.keys()),
        color="lightblue"
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    )
)])

fig.update_layout(title_text="Third-Party Vendor Responsibility Flow", font_size=12)

# 💾 Save interactive HTML chart
html_path = os.path.join(VISUALS_DIR, "vendor_flow.html")
fig.write_html(html_path)
print(f"✅ Sankey chart saved to: {html_path}")