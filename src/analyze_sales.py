from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data/sales_demo.csv", parse_dates=["order_date"])
df["order_month"] = df["order_date"].dt.to_period("M").dt.to_timestamp()
out = ROOT / "outputs"
out.mkdir(exist_ok=True)

monthly = df.groupby("order_month", as_index=False).agg(
    revenue=("revenue_ghs", "sum"),
    gross_profit=("gross_profit_ghs", "sum"),
    units=("units_sold", "sum")
)
product = df.groupby("product", as_index=False).agg(
    revenue=("revenue_ghs", "sum"),
    gross_profit=("gross_profit_ghs", "sum"),
    units=("units_sold", "sum")
)
region = df.groupby("region", as_index=False).agg(
    revenue=("revenue_ghs", "sum"),
    gross_profit=("gross_profit_ghs", "sum")
)

monthly.to_csv(out / "monthly_performance.csv", index=False)
product.to_csv(out / "product_performance.csv", index=False)
region.to_csv(out / "regional_performance.csv", index=False)

ax = monthly.plot(
    x="order_month", y="revenue", figsize=(9, 4), marker="o",
    legend=False, title="Monthly demo revenue"
)
ax.set_ylabel("Revenue (GHS)")
plt.tight_layout()
plt.savefig(out / "monthly_revenue.png", dpi=160)
plt.close()

print("Total demo revenue (GHS):", round(df["revenue_ghs"].sum(), 2))
print("\nProduct performance:\n", product.sort_values("revenue", ascending=False))
print("\nRegional performance:\n", region.sort_values("revenue", ascending=False))
