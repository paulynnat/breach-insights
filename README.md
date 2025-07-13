# breach-insights
🛡️ Breach Insights Dashboard
A modular analytics dashboard for visualizing breach patterns, remediation actions, and infrastructure exposure based on PDPC case files.

📊 Dashboard Modules
1. Taxonomy Frequency
Visualizes breach tags extracted from case files to highlight recurring technical patterns.
Taxonomy Chart
🔗 taxonomy.csv

2. Remediation Actions
Shows how organizations responded to breaches and the severity of enforcement outcomes.
Remediation Chart
🔗 remediation.csv

3. Infrastructure Risk Map
Analyzes breach surfaces across platform types (CRM, Email, POS, Git repos, etc.).
Infrastructure Chart
🔗 infrastructure.csv

🧠 Methodology
This dashboard synthesizes PDPC case files using a custom breach taxonomy across:
- Exposure vectors (e.g. public indexing, poor encryption)
- Credential hygiene failures
- Vendor oversight
- Retention & access violations
Modules are built in Python (pandas, seaborn, matplotlib) with GitHub integration for versioning and transparency.

🗂️ Repo Structure
| Folder | Contents | 
| /data/ | CSV outputs from each module | 
| /visuals/ | Charts embedded in this README | 
| /scripts/ | Python scripts for modeling breaches | 

📌 Roadmap
- cooccurrence_matrix.py — breach tag interaction mapping
- vendor_flows.py — third-party responsibility flow
- credential_hygiene.py — surface protection modeling
- dashboard_launcher.ps1 — one-click dashboard orchestrator
