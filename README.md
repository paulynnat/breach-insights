# breach-insights
🛡️ Breach Insights Dashboard
A modular analytics dashboard for visualizing breach patterns, remediation actions, infrastructure exposure, tag interactions, credential hygiene, response timelines, vendor accountability, and jurisdictional contrasts based on PDPC and international case files.

📊 Dashboard Modules
1. Taxonomy Frequency
Visualizes breach tags to highlight recurring technical failures and enforcement patterns.
Taxonomy Chart
🔗 taxonomy.csv

2. Remediation Actions
Summarizes how organizations responded to breaches and enforcement severity.
Remediation Chart
🔗 remediation.csv

3. Infrastructure Risk Map
Analyzes breach surfaces across platform types (CRM, Email, POS, Git, custom portals).
Infrastructure Chart
🔗 infrastructure.csv

4. Credential Hygiene Modeling
Breaks down authentication risk types including MFA failure, shared credentials, and dormant accounts.
Credential Hygiene Chart
🔗 credential_hygiene.csv

5. Response Lag Analysis
Calculates breach-to-discovery and discovery-to-remediation delays to measure organizational responsiveness.
Lag Chart
🔗 retention_lag.csv

6. Co-occurrence Matrix
Maps how breach tags interact to reveal compound vulnerabilities.
Co-occurrence Heatmap
🔗 cooccurrence_matrix.csv

7. Vendor Responsibility Flow
Visualizes third-party accountability chains across breach events.
🌐 Interactive Sankey Chart
🔗 vendor_flows.csv

8. Jurisdiction Comparison
Compares breach taxonomies, penalties, and remediation patterns across countries.
Jurisdiction Chart
🔗 jurisdiction_tag_compare.csv

⚙️ One-Click Dashboard Launcher
Run all modeling scripts with a single command using the orchestration shell:
.\dashboard_launcher.ps1
This updates all CSV datasets and visual charts in /data/ and /visuals/.

📂 Repo Structure
| Folder | Contents | 
| /data/ | Structured CSV outputs | 
| /visuals/ | Charts and interactive dashboards | 
| /scripts/ | Python modules for breach modeling | 
| Root | PowerShell launcher, README, config files | 

🌍 Expansion Roadmap
- Ingest CNIL (France), GDPR (EU), and OAIC (Australia) cases
- Enhance jurisdiction_compare.py with penalty scales and taxonomy divergence
- Add modules for enforcement severity modeling and breach archetype clustering
- Embed dashboard into Streamlit or Observable for public intelligence observatory

📊 Background to dashboard creation:
An initial exploratory analysis of six distinct breach-related use cases, using an event study methodology was conducted to assess whether market reactions around breach disclosures indicate statistical significance and whether insights could be drawn.

🧠 Key Insight:
Despite applying conventional event study models, the results do not show statistically significant reactions across the sample. This absence of significance highlights potential limitations in traditional modeling frameworks—and suggests:
- Either market efficiency (events were priced in or not considered material),
- Or model limitations (event windows, benchmarks, or estimation methods may dilute observable impact),
- Or a more complex, delayed response that the event study framework doesn't capture well.

🔍 Research Directions:
The results shows why there's still room for research and opens new pathways for exploration >>> Breach Insights 
