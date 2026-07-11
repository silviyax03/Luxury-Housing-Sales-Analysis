# 🏡 Luxury-Housing-Sales-Analysis
Luxury Housing Sales Analysis – Bengaluru

## 📌 Project Overview

This project analyzes luxury housing sales data in Bengaluru using an end-to-end Data Analytics workflow. The objective is to transform raw housing data into meaningful business insights through Python-based ETL, MySQL database integration, and interactive Power BI dashboards.

The dashboard helps real estate firms understand market trends, builder performance, buyer preferences, pricing patterns, and geographical distribution of luxury housing projects.

---

## 🎯 Project Objectives

- Clean and preprocess raw housing sales data.
- Perform feature engineering for better analysis.
- Load cleaned data into a MySQL database.
- Connect Power BI directly to SQL for live reporting.
- Build an interactive dashboard with KPIs and business insights.
- Analyze market trends, builder performance, buyer preferences, and geographical distribution.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- SQLAlchemy
- MySQL
- Power BI
- DAX
- Google Colab

---

## 📂 Repository Structure

```
Luxury-Housing-Sales-Analysis/
│
├── python/
│   ├── Luxury_Housing_Analysis.ipynb
│   └── load_data.py
│
├── sql/
│   └── SQL Query.sql
│
├── powerbi/
│   ├── Luxury_Housing_Sales.pbix
│   ├── Luxury_Housing_Sales_Dashboard.pdf
│   └── Screenshots
│
├── data/
│   └── Luxury_Housing_Cleaned.csv
│
├── presentation/
│   └── Luxury_Housing_Sales_Analysis.pptx
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains over **100,000 luxury housing sales records** from Bengaluru.

### Important Columns

- Property_ID
- Developer_Name
- Micro_Market
- Ticket_Price_Cr
- Configuration
- Possession_Status
- Amenity_Score
- Sales_Channel
- Buyer_Type
- Buyer_Comments
- Quarter_Label
- Quarter_Number

---

# 🔄 ETL Pipeline

### Step 1 — Data Cleaning (Python)

Performed using Pandas.

Tasks completed:

- Removed duplicate records
- Handled missing values
- Corrected data types
- Standardized categorical values
- Created Quarter Label
- Created Quarter Number
- Exported cleaned dataset

---

### Step 2 — SQL Integration

Loaded the cleaned dataset into MySQL using SQLAlchemy.

Tasks:

- Created database
- Created luxury_housing_sales table
- Imported cleaned dataset
- Validated inserted records
- Executed aggregation queries

---

### Step 3 — Power BI Dashboard

Connected Power BI directly to MySQL for live reporting.

Created:

- KPI Cards
- Interactive Slicers
- Maps
- Scatter Charts
- Matrix
- Pie Charts
- Line Charts
- Tables

---

# 📈 Dashboard Features

## Executive Dashboard

- Total Properties
- Total Revenue
- Average Ticket Price
- Average Amenity Score
- Market Trends by Quarter
- Builder Performance
- Configuration Demand
- Sales Channel Efficiency
- Quarterly Builder Contribution

---

## Detailed Analysis Dashboard

- Possession Status Analysis
- Amenity Impact Analysis
- Top 5 Builders by Revenue
- Buyer Distribution Across Micro Markets
- Geographical Insights
- Buyer Feedback Distribution
- Key Buyer Insights

---

# 📌 DAX Measures

Implemented DAX measures including:

```DAX
Total Properties = DISTINCTCOUNT(luxury_housing_sales[Property_ID])

Total Revenue = SUM(luxury_housing_sales[Ticket_Price_Cr])

Average Ticket Price = AVERAGE(luxury_housing_sales[Ticket_Price_Cr])

Average Amenity Score = AVERAGE(luxury_housing_sales[Amenity_Score])
```

---

# 📊 Business Insights

The analysis revealed several key insights:

- Premium builders generate significantly higher revenue.
- Certain micro-markets dominate luxury housing sales.
- Higher amenity scores are associated with premium pricing.
- Premium housing demand is concentrated in selected Bengaluru locations.
- Buyer feedback highlights amenities, connectivity, and location as major purchase factors.
- Sales are distributed across multiple builders, indicating a competitive luxury housing market.

---

# 📸 Dashboard Screenshots

## Executive Dashboard

*(Insert dashboard_page1.png here)*

---

## Detailed Analysis Dashboard

*(Insert dashboard_page2.png here)*

---

# ▶️ How to Run the Project

## Clone Repository

```bash
git clone https://github.com/<your-username>/Luxury-Housing-Sales-Analysis.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Python Notebook

Open

```
Luxury_Housing_Analysis.ipynb
```

in Google Colab or Jupyter Notebook.

---

## Import Data into MySQL

Run

```
load_data.py
```

after updating your MySQL credentials.

---

## Open Power BI Dashboard

Open

```
Luxury_Housing_Sales.pbix
```

and refresh the MySQL connection.

---

# 📌 Future Improvements

- Predictive housing price forecasting using Machine Learning.
- Sentiment analysis on buyer comments.
- Automated ETL pipeline.
- Real-time dashboard updates.
- Deployment using Streamlit.

---

# 📚 Skills Demonstrated

- Data Cleaning
- Feature Engineering
- ETL Pipeline
- SQL Integration
- Power BI Dashboard Development
- DAX Calculations
- Business Intelligence
- Data Visualization
- Real Estate Analytics

---

# 👩‍💻 Author

**Silviya X**

Data Analytics Project – Luxury Housing Sales Analysis
