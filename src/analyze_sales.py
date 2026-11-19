from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data/sales_demo.csv",parse_dates=["order_month"])
out=ROOT/"outputs"; out.mkdir(exist_ok=True)
df["gross_profit"]=df.revenue-df.cost
monthly=df.groupby("order_month",as_index=False).agg(revenue=("revenue","sum"),
 gross_profit=("gross_profit","sum"),units=("units_sold","sum"))
product=df.groupby("product",as_index=False).agg(revenue=("revenue","sum"),
 gross_profit=("gross_profit","sum"),units=("units_sold","sum"))
region=df.groupby("region",as_index=False).agg(revenue=("revenue","sum"),gross_profit=("gross_profit","sum"))
monthly.to_csv(out/"monthly_performance.csv",index=False)
product.to_csv(out/"product_performance.csv",index=False)
region.to_csv(out/"regional_performance.csv",index=False)
ax=monthly.plot(x="order_month",y="revenue",figsize=(9,4),marker="o",legend=False,
 title="Monthly demo revenue")
ax.set_ylabel("Revenue (demo currency units)"); plt.tight_layout()
plt.savefig(out/"monthly_revenue.png",dpi=160); plt.close()
print("Total demo revenue:",round(df.revenue.sum(),2))
print("\nProduct performance:\n",product.sort_values("revenue",ascending=False))
print("\nRegional performance:\n",region.sort_values("revenue",ascending=False))
