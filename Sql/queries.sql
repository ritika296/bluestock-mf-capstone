-- 1. Top 5 Funds by AUM

SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

--------------------------------------------------

-- 2. Average NAV

SELECT
AVG(nav) AS average_nav
FROM fact_nav;

--------------------------------------------------

-- 3. Funds with Expense Ratio < 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

--------------------------------------------------

-- 4. Count Funds by Risk Grade

SELECT
risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

--------------------------------------------------

-- 5. Top Fund Houses

SELECT
fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house
ORDER BY COUNT(*) DESC;

--------------------------------------------------

-- 6. Average 1 Year Return

SELECT
AVG(return_1yr_pct)
FROM fact_performance;

--------------------------------------------------

-- 7. Highest Sharpe Ratio

SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

--------------------------------------------------

-- 8. Highest Alpha Funds

SELECT
scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;

--------------------------------------------------

-- 9. Average Expense Ratio

SELECT
AVG(expense_ratio_pct)
FROM fact_performance;

--------------------------------------------------

-- 10. Top Performing Funds (5 Year)

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;