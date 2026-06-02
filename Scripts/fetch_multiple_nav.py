import requests
import pandas as pd
import os

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        output_file = os.path.join(
            "Data",
            "Raw",
            f"{fund_name}.csv"
        )

        df.to_csv(output_file, index=False)

        print(f"{fund_name} downloaded successfully")

    else:
        print(f"Failed for {fund_name}")