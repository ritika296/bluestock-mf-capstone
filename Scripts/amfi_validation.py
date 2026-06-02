import pandas as pd

fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Fund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("\nPASS: All AMFI codes exist in NAV History")
else:
    print("\nMissing Codes:")
    print(missing_codes)