import pandas as pd

performance = pd.read_csv(
r"C:\Users\ritik\OneDrive\Pictures\Desktop\Bluestock_mf_capstone\Data\processed\scheme_performance_clean.csv"
)

risk = input("Enter Risk Appetite (Low/Moderate/High): ")

recommend = (
    performance[
        performance["risk_grade"] == risk
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nRecommended Funds:\n")

print(
    recommend[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)