from sqlalchemy import create_engine
import pandas as pd
import os

# Create db folder if missing
os.makedirs("Data/db", exist_ok=True)

engine = create_engine(
    "sqlite:///Data/db/bluestock_mf.db"
)

fund_master = pd.read_csv(
    "Data/Raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "Data/processed/nav_history_clean.csv"
)

transactions = pd.read_csv(
    "Data/processed/investor_transactions_clean.csv"
)

performance = pd.read_csv(
    "Data/processed/scheme_performance_clean.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Loaded Successfully")