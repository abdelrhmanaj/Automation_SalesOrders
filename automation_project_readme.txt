Python Automation Mini Project
==============================

Files:
- Dataset: python_automation_sales_orders.csv
- Script: automation_sales_report.py

Suggested class flow:
1) Read the dataset with pandas
2) Explore using: head(), info(), isna().sum(), describe()
3) Clean data:
   - parse order_date
   - standardize text columns
   - remove duplicates
   - fill missing values
   - handle invalid quantity and delivery_days
4) Create calculated columns:
   - month
   - gross_revenue
   - net_revenue
5) Create report tables:
   - kpi_summary
   - revenue_by_category
   - revenue_by_city
   - monthly_sales
   - returned_orders
   - top_products
6) Export reports automatically to CSV + Excel

How to run:
python automation_sales_report.py

Output folder:
automation_reports/