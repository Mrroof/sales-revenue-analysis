[![Portfolio validation](https://github.com/Mrroof/sales-revenue-analysis/actions/workflows/portfolio-validation.yml/badge.svg)](https://github.com/Mrroof/sales-revenue-analysis/actions)

# Sales and Revenue Performance Analysis

> **Portfolio case study · Python · pandas · Matplotlib · SQL · Power BI extension**

## Executive summary
This project analyzes synthetic sales transactions to compare revenue and gross profit across products and regions, and to demonstrate how transaction-level data can be transformed into business reporting.

## Business questions
- Which products contribute most to total revenue?
- Which regions generate the most revenue and gross profit?
- How do product mix and transaction trends inform commercial questions?
- What measures would be useful in a Power BI dashboard?

## Demonstration findings
- Total demo revenue: **GHS 8,389,891.74**.
- Laptops generated the largest product revenue: **GHS 3,487,963.36**.
- Kumasi generated the highest regional revenue: **GHS 2,159,211.18**.
- Laptop gross profit in the demo dataset was **GHS 885,400.29**.

![Top product revenue in synthetic sales dataset](docs/sales-product-revenue.svg)

![Revenue by region in synthetic sales dataset](docs/sales-regional-revenue.svg)

## Method
1. Load and validate transaction records.
2. Calculate revenue, cost and gross profit.
3. Aggregate performance by product, region and month.
4. Export summary tables and visualizations.
5. Use the outputs to formulate follow-up commercial questions.

## Run locally
```bash
pip install -r requirements.txt
python src/analyze_sales.py
```

Outputs are written to `outputs/`.

## Power BI dashboard
A reproducible Power BI build kit is available in [`powerbi/`](powerbi/): Power Query import script, DAX measures, report layout/validation blueprint and a report theme. Follow [`powerbi/report-blueprint.md`](powerbi/report-blueprint.md) to build the interactive dashboard in Power BI Desktop. The repository contains the source assets and instructions, not a finished `.pbix` file.

## Limitations
The transactions are synthetic and do not represent actual company sales. Revenue rankings and trends are illustrative only. A business recommendation would require understanding discounts, returns, customer segments, inventory constraints, acquisition costs and data quality.

## Repository structure

```text
data/sales_demo.csv                 # Synthetic transaction records
src/analyze_sales.py                # Data preparation and analysis
sql/analysis_queries.sql            # Example SQL analysis queries
docs/                               # Report-ready charts
requirements.txt                    # Python dependencies
.github/workflows/                  # Automated repository validation
```

## Reproducibility

Run the command above from the repository root. The script regenerates summary outputs locally in `outputs/`; generated outputs are not committed by default. SQL examples are provided separately for readers who want to explore the same business questions in a relational database.

## Business insights

- Total revenue in the synthetic transaction sample is **GHS 8,389,891.74**.
- **Laptops** are the largest product revenue contributor at **GHS 3,487,963.36**.
- **Kumasi** is the leading region by revenue at **GHS 2,159,211.18**.
- Laptop gross profit in the sample is **GHS 885,400.29**. Revenue leadership should therefore be considered alongside gross profit and margin, not in isolation.

## Practical recommendations

1. Review laptop availability, stock-outs and supplier terms, given the product's revenue contribution.
2. Investigate what is driving Kumasi's result: transaction volume, average selling price, product mix or a small number of large orders.
3. Compare gross margin by product and region before shifting sales resources or discount budgets.
4. Track monthly revenue, gross profit, gross margin and units sold together to distinguish growth from discount-led sales.
5. Validate the patterns against actual returns, discounts, inventory costs and customer segments before making commercial decisions.
