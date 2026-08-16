# Power BI Build Guide

Import `data/sales_operations.csv`.

## Measures
```DAX
Total Revenue = SUM(orders[revenue])
Total Profit = SUM(orders[profit])
Profit Margin % = DIVIDE([Total Profit], [Total Revenue])
Late Delivery Rate % = AVERAGE(orders[late_delivery])
Return Rate % = AVERAGE(orders[returned])
Orders = DISTINCTCOUNT(orders[order_id])
```

## One-page dashboard
1. KPI cards: Revenue, Profit, Margin %, Late Delivery %, Return %.
2. Line chart: Revenue by month.
3. Bar chart: Profit by category.
4. Bar chart: Revenue by region.
5. Matrix: Category x Region with Revenue and Margin.
6. Slicers: Region, Channel, Category.

Before listing Power BI on your resume, build this page yourself, test the filters, and be able to explain every KPI.
