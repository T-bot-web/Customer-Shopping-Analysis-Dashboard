Option A: CSV
- Open Power BI Desktop -> Home -> Get data -> Text/CSV -> select data/customer_shopping_cleaned.csv
- Transform in Power Query if needed -> Load

Option B: SQLite
- Install a Power BI SQLite connector from Marketplace or use ODBC driver for SQLite.
- Connect -> Browse to data/customer_dashboard.db -> import 'customers' table.

Create visuals:
- Cards: Total Sales = SUM(customers[purchase_amount_usd])
- Total Customers = DISTINCTCOUNT(customers[customer_id])
- Avg Rating = AVERAGE(customers[review_rating])
- Charts: Category on X, SUM(purchase_amount_usd) on Y (clustered column)
- Slicers: Season, Category, Payment Method, Location
