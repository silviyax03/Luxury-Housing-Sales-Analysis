CREATE DATABASE luxury_housing;

USE luxury_housing;

CREATE TABLE luxury_housing_sales (
    Property_ID VARCHAR(20) PRIMARY KEY,
    Micro_Market VARCHAR(100),
    Project_Name VARCHAR(100),
    Developer_Name VARCHAR(100),
    Unit_Size_Sqft FLOAT,
    Configuration VARCHAR(20),
    Ticket_Price_Cr FLOAT,
    Transaction_Type VARCHAR(50),
    Buyer_Type VARCHAR(50),
    Purchase_Quarter DATE,
    Connectivity_Score FLOAT,
    Amenity_Score FLOAT,
    Possession_Status VARCHAR(50),
    Sales_Channel VARCHAR(50),
    NRI_Buyer VARCHAR(10),
    Locality_Infra_Score FLOAT,
    Avg_Traffic_Time_Min INT,
    Buyer_Comments TEXT,
    Price_per_Sqft FLOAT,
    Quarter_Number INT,
    Purchase_Year INT,
    Quarter_Label VARCHAR(5)
);

-----------analysis_queries-----------
USE luxury_housing;

SELECT COUNT(*) AS Total_Records
FROM luxury_housing_sales;

SELECT Transaction_Type,
COUNT(*) AS Total
FROM luxury_housing_sales
GROUP BY Transaction_Type;

SELECT
Developer_Name,
ROUND(AVG(Ticket_Price_Cr),2) AS Avg_Ticket_Price
FROM luxury_housing_sales
GROUP BY Developer_Name
ORDER BY Avg_Ticket_Price DESC;

SELECT
Buyer_Type,
COUNT(*) AS Buyers
FROM luxury_housing_sales
GROUP BY Buyer_Type;

SELECT
Configuration,
COUNT(*) AS Total
FROM luxury_housing_sales
GROUP BY Configuration
ORDER BY Total DESC;

SELECT
Quarter_Label,
COUNT(*) AS Bookings
FROM luxury_housing_sales
GROUP BY Quarter_Label
ORDER BY Quarter_Label;
