import pandas as pd

# Read the file
df = pd.read_csv("Data/Raw/01_fund_master.csv")

# Show first 5 rows
print(df.head())

# Show column names
print("\nColumns:")
print(df.columns.tolist())