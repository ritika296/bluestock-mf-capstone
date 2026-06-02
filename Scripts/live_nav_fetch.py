import requests
import pandas as pd
import os

# HDFC Top 100 Direct Fund
scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:

    data = response.json()

    df = pd.DataFrame(data["data"])

    # Check current folder
    print("Current Working Directory:")
    print(os.getcwd())

    # Save file
    output_file = "HDFC_Top100_Live.csv"

    df.to_csv(output_file, index=False)

    print(f"\nFile saved successfully: {output_file}")

    print("\nFirst 5 Records:")
    print(df.head())

else:
    print("Failed to fetch data")
    