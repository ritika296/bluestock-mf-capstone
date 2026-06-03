# Data Dictionary

## 01_fund_master.csv

| Column            | Type    | Description              |
| ----------------- | ------- | ------------------------ |
| amfi_code         | Integer | Unique AMFI scheme code  |
| fund_house        | Text    | Mutual fund company      |
| scheme_name       | Text    | Scheme name              |
| category          | Text    | Fund category            |
| sub_category      | Text    | Fund sub-category        |
| expense_ratio_pct | Decimal | Expense ratio percentage |
| risk_category     | Text    | Risk classification      |

## 02_nav_history.csv

| Column    | Type    | Description     |
| --------- | ------- | --------------- |
| amfi_code | Integer | Fund identifier |
| date      | Date    | NAV date        |
| nav       | Decimal | Net Asset Value |

## 08_investor_transactions.csv

| Column           | Type    | Description                |
| ---------------- | ------- | -------------------------- |
| investor_id      | Integer | Investor identifier        |
| transaction_date | Date    | Transaction date           |
| transaction_type | Text    | SIP / Lumpsum / Redemption |
| amount_inr       | Decimal | Investment amount          |
| kyc_status       | Text    | KYC verification status    |

## 07_scheme_performance.csv

| Column            | Type    | Description             |
| ----------------- | ------- | ----------------------- |
| return_1yr_pct    | Decimal | 1-year return           |
| return_3yr_pct    | Decimal | 3-year return           |
| return_5yr_pct    | Decimal | 5-year return           |
| alpha             | Decimal | Alpha metric            |
| beta              | Decimal | Beta metric             |
| sharpe_ratio      | Decimal | Sharpe Ratio            |
| expense_ratio_pct | Decimal | Expense ratio           |
| aum_crore         | Decimal | Assets under management |
