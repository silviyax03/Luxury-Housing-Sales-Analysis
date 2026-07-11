import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# ============================
# Read the cleaned CSV
# ============================

file_path = r"C:\Users\Silviya\Downloads\Luxury_Housing_Cleaned.csv"

df = pd.read_csv(file_path)

print("CSV Loaded Successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ============================
# MySQL Connection
# ============================

username = "root"

# Replace with your actual password
password = quote_plus("Alp@Sil@003")

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
