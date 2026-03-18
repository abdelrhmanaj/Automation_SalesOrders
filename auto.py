import pandas as pd
import numpy as np
from pathlib import Path

def sales_orders_automation(file_path):
    file_path = Path("D:\DATA_ANAlSYS\Automation_SalesOrders\python_automation_sales_orders_cleaned.csv")
    df = pd.read_csv(file_path)
    df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d", errors="coerce")
    numeric_cols = ["quantity", "discount_pct", "delivery_days", "customer_rating", "unit_price"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    def clean_text(value):
        if pd.isna(value):
            return value
        return str(value).strip().title()

    text_cols = ["payment_method", "customer_city", "product_category", "customer_segment", "product_name"]

    for col in text_cols:
        df[col] = df[col].apply(clean_text)
    df = df.drop_duplicates()
    df["discount_pct"] = df["discount_pct"].fillna(0)
    df["customer_city"] = df["customer_city"].fillna("Unknown")
    df["customer_rating"] = df["customer_rating"].fillna(df["customer_rating"].median())
    
    df["unit_price"] = df.groupby("product_category")["unit_price"].transform(lambda s: s.fillna(s.median()))
    df.loc[df["quantity"] <= 0, "quantity"] = np.nan
    df.loc[df["delivery_days"] < 0, "delivery_days"] = np.nan
    df.dropna(subset=["quantity", "delivery_days"], inplace=True)
    df["month"] = df["order_date"].dt.month_name()
    df["gross_revenue"] = df["unit_price"] * df["quantity"]
    df["net_revenue"] = df["gross_revenue"] * (1 - df["discount_pct"] / 100)
    df.to_csv("python_automation_sales_orders_cleaned.csv", index=False)
    
    
file_path = Path("D:\DATA_ANAlSYS\Automation_SalesOrders\python_automation_sales_orders_cleaned.csv")
sales_orders_automation(file_path)