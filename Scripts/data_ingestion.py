import pandas as pd
import os

# Path to raw data folder
DATA_FOLDER = "Data/raw"

# Get all CSV files
csv_files = [file for file in os.listdir(DATA_FOLDER) if file.endswith(".csv")]

print(f"\nTotal CSV Files Found: {len(csv_files)}")

for file in csv_files:

    print("\n" + "="*60)
    print(f"FILE: {file}")
    print("="*60)

    file_path = os.path.join(DATA_FOLDER, file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())