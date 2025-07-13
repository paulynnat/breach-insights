# 📁 Set working directory
$repoPath = "C:\Users\User\OneDrive\ドキュメント\GitHub\breach-insights"
Set-Location $repoPath

# 🧠 Define script sequence
$modules = @(
    "taxonomy.py",
    "remediation.py",
    "infrastructure.py",
    "cooccurrence_matrix.py",
    "vendor_flows.py",
    "credential_hygiene.py",
    "retention_lag.py"
)

# 🏃 Run each module
foreach ($script in $modules) {
    Write-Host "🔄 Running $script..."
    python $script
}

Write-Host "`n✅ All dashboard modules executed successfully."