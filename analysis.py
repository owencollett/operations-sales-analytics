from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

con = sqlite3.connect(BASE / "data" / "operations.db")
orders = pd.read_sql_query("SELECT * FROM orders", con, parse_dates=["order_date"])
con.close()

monthly = (
    orders.assign(month=orders["order_date"].dt.to_period("M").astype(str))
    .groupby("month", as_index=False)
    .agg(revenue=("revenue","sum"), profit=("profit","sum"))
)
monthly["margin_pct"] = 100*monthly["profit"]/monthly["revenue"]
monthly.to_csv(OUT/"monthly_kpis.csv", index=False)

regional = (
    orders.groupby("region", as_index=False)
    .agg(
        revenue=("revenue","sum"),
        profit=("profit","sum"),
        avg_delivery_days=("delivery_days","mean"),
        late_delivery_rate=("late_delivery","mean"),
        return_rate=("returned","mean")
    )
)
regional.to_csv(OUT/"regional_kpis.csv", index=False)

plt.figure(figsize=(9,5))
plt.plot(monthly["month"], monthly["revenue"], marker="o")
plt.xticks(rotation=45)
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig(OUT/"monthly_revenue.png", dpi=160)
plt.close()

category = orders.groupby("category", as_index=False)["profit"].sum().sort_values("profit", ascending=False)
plt.figure(figsize=(7,5))
plt.bar(category["category"], category["profit"])
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig(OUT/"profit_by_category.png", dpi=160)
plt.close()

print("Revenue:", round(orders["revenue"].sum(),2))
print("Profit:", round(orders["profit"].sum(),2))
print("Margin %:", round(100*orders["profit"].sum()/orders["revenue"].sum(),2))
print("Late delivery rate %:", round(100*orders["late_delivery"].mean(),2))
print("Return rate %:", round(100*orders["returned"].mean(),2))
