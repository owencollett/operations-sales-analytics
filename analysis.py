from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

BASE=Path(__file__).resolve().parent
OUT=BASE/'outputs'; OUT.mkdir(exist_ok=True)
con=sqlite3.connect(BASE/'data'/'operations.db')
orders=pd.read_sql_query('SELECT * FROM orders',con,parse_dates=['order_date']); con.close()
monthly=(orders.assign(month=orders.order_date.dt.to_period('M').astype(str)).groupby('month',as_index=False).agg(revenue=('revenue','sum'),profit=('profit','sum')))
monthly['profit_margin_pct']=100*monthly.profit/monthly.revenue; monthly.to_csv(OUT/'monthly_kpis.csv',index=False)
regional=orders.groupby('region',as_index=False).agg(revenue=('revenue','sum'),profit=('profit','sum'),avg_delivery_days=('delivery_days','mean'),late_delivery_rate=('late_delivery','mean'),return_rate=('returned','mean')); regional.to_csv(OUT/'regional_kpis.csv',index=False)
delivery=orders.groupby('late_delivery',as_index=False).agg(orders=('order_id','count'),return_rate=('returned','mean')); delivery['delivery_status']=delivery.late_delivery.map({0:'On Time',1:'Late'}); delivery.to_csv(OUT/'delivery_return_analysis.csv',index=False)
plt.figure(figsize=(9,5)); plt.plot(monthly.month,monthly.revenue,marker='o'); plt.title('Monthly Revenue'); plt.xlabel('Month'); plt.ylabel('Revenue ($)'); plt.xticks(rotation=45); plt.tight_layout(); plt.savefig(OUT/'monthly_revenue.png',dpi=160); plt.close()
cat=orders.groupby('category',as_index=False).profit.sum().sort_values('profit',ascending=False); plt.figure(figsize=(7,5)); plt.bar(cat.category,cat.profit); plt.title('Profit by Product Category'); plt.xlabel('Category'); plt.ylabel('Profit ($)'); plt.tight_layout(); plt.savefig(OUT/'profit_by_category.png',dpi=160); plt.close()
print(f'Orders: {len(orders):,}'); print(f'Revenue: ${orders.revenue.sum():,.2f}'); print(f'Profit: ${orders.profit.sum():,.2f}'); print(f'Profit Margin: {100*orders.profit.sum()/orders.revenue.sum():.2f}%'); print(f'Late Delivery Rate: {100*orders.late_delivery.mean():.2f}%'); print(f'Return Rate: {100*orders.returned.mean():.2f}%')
