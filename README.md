# Operations & Sales Analytics

I built this project to analyze how sales performance and operating outcomes connect across a synthetic dataset of 15,000 transactions. I used SQL for the main business queries and Python/pandas for KPI summaries and visualizations.

## Questions I analyzed

- How do revenue and profit change by month?
- Which regions and product categories contribute the most revenue and profit?
- Which products perform best within each category?
- How often are orders delivered late or returned?
- Are late deliveries associated with a higher return rate?

## Findings

The Southeast produced the highest revenue and profit in the dataset, with about **$2.45 million in revenue** and **$856,000 in profit**.

Delivery performance also showed a useful pattern. On-time orders had a return rate of about **6.25%**, while late orders had a return rate of about **11.64%**. This does not prove that late delivery causes returns, but it suggests delivery performance is worth monitoring alongside return behavior.

## Tools

- SQL / SQLite
- Python
- pandas
- matplotlib

The SQL work includes aggregations, `CASE` statements, common table expressions, and a `DENSE_RANK()` window function for ranking products within categories.

## Project files

- `queries.sql` — business queries for monthly, regional, category, product, and delivery analysis
- `analysis.py` — creates summary outputs and charts from the SQLite data
- `data/operations.db` — SQLite database used by the SQL queries
- `data/sales_operations.csv` — source dataset
- `outputs/` — KPI summaries and charts created by the Python analysis
- `Dashboard/` — dashboard image included with the project

## Run the Python analysis

```bash
pip install pandas matplotlib
python analysis.py
```

The queries in `queries.sql` can be run against `data/operations.db`.

## Sample outputs

![Monthly Revenue](outputs/monthly_revenue.png)

![Profit by Category](outputs/profit_by_category.png)
