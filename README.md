# Operations & Sales Analytics Dashboard

## Goal
Analyze sales and delivery operations to identify revenue trends, profitability drivers, delivery risk, and return behavior.

## Stack
SQL / SQLite, Python / pandas / matplotlib, and Power BI for the final dashboard.

## Dataset
Synthetic dataset of 15,000 orders across regions, sales channels, product categories, delivery outcomes, and returns.

## Business questions
- How are revenue and profit trending?
- Which regions/categories generate the most value?
- Which products lead within their categories?
- Are late deliveries associated with higher return rates?
- Which KPIs should management monitor?

## Run
```bash
python analysis.py
```

Run `queries.sql` against `data/operations.db` in a SQLite client.

## Resume bullets — use only after you run and understand the project
- Analyzed 15,000 sales and operations records with SQL and Python to evaluate revenue, profitability, delivery performance, and returns.
- Wrote SQL queries using aggregations, CTEs, CASE logic, and window functions to surface product, regional, and operational trends.
- Built a management KPI dashboard design for Power BI covering revenue, margin, late-delivery rate, return rate, and category performance.
