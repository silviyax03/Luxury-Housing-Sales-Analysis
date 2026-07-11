"""
Load cleaned luxury housing dataset into MySQL.

Steps:
1. Read cleaned CSV.
2. Connect to MySQL using SQLAlchemy.
3. Load data into the luxury_housing_sales table.
"""


import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# ============================
# Read the cleaned CSV
# ============================

file_path = r"data\Luxury_Housing_Cleaned.csv"

df = pd.read_csv(file_path)

print("CSV Loaded Successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ============================
# MySQL Connection
# ============================

username = "root"

# Replace with your actual password
password = quote_plus("YOUR_MYSQL_PASSWORD")

host = "localhost"
port = 3306
database = "luxury_housing"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

print("Connected to MySQL Successfully!")

# ============================
# Import Data
# ============================

df.to_sql(
    name="luxury_housing_sales",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000,
    method="multi"
)

print("===================================")
print("Data Imported Successfully!")
print("===================================")
