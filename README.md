# Sales and Revenue Performance Analysis

## Objective
Evaluate revenue, units, gross profit and performance by product, region and month.

## Data notice
`data/sales_demo.csv` contains **synthetic demonstration transactions**. These are not company sales results.

## Run
```bash
pip install -r requirements.txt
python src/analyze_sales.py
```

## Questions
- Which product and region generate the highest demo revenue?
- How does gross margin vary by product?
- What is the monthly revenue trend?
- Which segments warrant further investigation?

## Power BI extension
Import the CSV into Power BI. Create measures for Total Revenue, Total Cost, Gross Profit, Gross Margin % and Units Sold. Add month, region and product slicers.

## Limitations
Replace synthetic data with legitimate public or authorized data before making real-world claims.
