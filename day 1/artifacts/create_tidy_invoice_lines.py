from pathlib import Path
import pandas as pd

base = Path(".")

# Read source files
invoices = pd.read_csv(
    base / "invoices.csv",
    parse_dates=["InvoiceDate"],
)

invoice_lines = pd.read_csv(
    base / "invoice_lines.csv",
    dtype={"StockCode": "string"},
)

# Join invoice-level fields onto each line item
tidy = (
    invoice_lines
    .merge(
        invoices,
        on="InvoiceNo",
        how="left",
        validate="many_to_one",
    )
    .assign(line_total=lambda df: df["Quantity"] * df["LineUnitPrice"])
    .rename(
        columns={
            "InvoiceLineID": "invoice_line_id",
            "InvoiceNo": "invoice_no",
            "InvoiceDate": "invoice_date",
            "CustomerID": "customer_id",
            "IsCancelled": "is_cancelled",
            "InvoiceTotal": "invoice_total",
            "StockCode": "stock_code",
            "Quantity": "quantity",
            "LineUnitPrice": "line_unit_price",
        }
    )
    [
        [
            "invoice_line_id",
            "invoice_no",
            "invoice_date",
            "customer_id",
            "is_cancelled",
            "invoice_total",
            "stock_code",
            "quantity",
            "line_unit_price",
            "line_total",
        ]
    ]
)

# Export tidy single-table CSV
tidy.to_csv(base / "tidy_invoice_lines.csv", index=False)
print("Wrote tidy_invoice_lines.csv")
