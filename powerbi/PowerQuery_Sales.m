let
    Source = Csv.Document(
        Web.Contents("https://raw.githubusercontent.com/Mrroof/sales-revenue-analysis/main/data/sales_demo.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(
        PromotedHeaders,
        {
            {"order_id", type text},
            {"order_date", type date},
            {"region", type text},
            {"category", type text},
            {"product", type text},
            {"units_sold", Int64.Type},
            {"unit_price_ghs", Currency.Type},
            {"discount_rate", Percentage.Type},
            {"revenue_ghs", Currency.Type},
            {"cost_ghs", Currency.Type},
            {"gross_profit_ghs", Currency.Type}
        },
        "en-GH"
    ),
    AddedOrderMonth = Table.AddColumn(
        ChangedTypes,
        "order_month",
        each Date.StartOfMonth([order_date]),
        type date
    )
in
    AddedOrderMonth
