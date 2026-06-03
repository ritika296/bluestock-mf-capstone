import pandas as pd

# =========================
# NAV HISTORY CLEANING
# =========================

nav = pd.read_csv("Data/Raw/02_nav_history.csv")

# Convert date column
nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

# Sort by fund and date
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Fill missing NAV values
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

# Keep only positive NAV
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(
    "Data/processed/nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned")
print(nav.shape)


# =========================
# INVESTOR TRANSACTIONS CLEANING
# =========================

txn = pd.read_csv(
    "Data/Raw/08_investor_transactions.csv"
)

# Convert date
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

# Amount should be numeric
txn["amount_inr"] = pd.to_numeric(
    txn["amount_inr"],
    errors="coerce"
)

# Keep only positive amounts
txn = txn[txn["amount_inr"] > 0]

# Standardize transaction type
txn["transaction_type"] = (
    txn["transaction_type"]
    .str.upper()
    .str.strip()
)

# Check KYC values
print("\nKYC Status Values:")
print(txn["kyc_status"].unique())

# Save cleaned file
txn.to_csv(
    "Data/processed/investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions Cleaned")
print(txn.shape)

# =========================
# SCHEME PERFORMANCE CLEANING
# =========================

perf = pd.read_csv(
    "Data/Raw/07_scheme_performance.csv"
)

# Convert return columns to numeric

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio numeric
perf["expense_ratio_pct"] = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

# Find anomalies
anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(anomalies.shape)

# Save cleaned file
perf.to_csv(
    "Data/processed/scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance Cleaned")
print(perf.shape)

