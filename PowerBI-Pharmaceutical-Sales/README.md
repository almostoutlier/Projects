
# 📊 Pharmaceutical Sales Analysis

This **Data Analytics Project** provides an in-depth sales performance analysis for a global pharmaceutical company using **Power BI** dashboards. The project focuses on the **Germany** and **Poland** markets, offering actionable insights to drive data-backed business decisions.

---

## 🔍 Project Overview

**Datamatrix-ml Pharmaceuticals** operates via distributors and does not sell directly to customers. This project analyzes their wholesale-retail sales data to uncover trends, patterns, and opportunities for optimization. The analysis spans **2017–2020** and covers:

✅ Sales by Year, Month, City, Channel, and Sub-channel  
✅ Product Class and Top Product Analysis  
✅ Distributor and Customer Insights  
✅ Sales Team Performance Breakdown

---

## 🏗️ Features

- High-level and detailed sales analysis dashboards
- Year, Month, City, Country, Channel, and Sub-channel filters
- Product class and top product insights
- Sales team and sales rep performance tracking
- Star schema data modeling in Power BI
- Data cleaning and validation using **Power Query** and **pandas**

## Tech Stack

- **Data Analysis & Cleaning**: pandas, Power Query Editor  
- **Dashboarding**: Power BI Desktop, Power BI Service  
- **Data Modeling**: Star Schema Design  
- **Visualization**: Interactive charts, KPIs, filters, and slicers

## Project Structure

```
pharmaceutical-sales-analysis/
├── data-exploration.ipynb       # EDA with pandas
├── pharma-data.csv              # Raw sales dataset
├── pharma-analysis.pbix         # Power BI report file
├── README.md                    # Project documentation
```

---

## 📂 Table of Contents

- [Objectives](#objectives)
- [Dataset](#dataset)
- [Solution Approach](#solution-approach)
- [Key Insights](#key-insights)
- [Business Recommendations](#business-recommendations)
- [How To Use](#how-to-use)
- [Screenshots](#screenshots)
- [License](#license)
- [Credits](#credits)

---

## 🎯 Objectives

| For Whom               | Requirement Description                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| Executive Committee    | High-level overview of sales by year, month, customer city, channel, and sub-channel. Top product & city insights. |
| Sales Manager/Rep      | Detailed view of sales by distributor, product, customer, city, channel, and sub-channel breakdowns.          |

---

## 📊 Dataset

Sourced from distributor-provided CSV files, the dataset includes:

| Field          | Description                                  |
|----------------|----------------------------------------------|
| Distributor    | Name of wholesaler                           |
| Customer Name  | Customer's name                              |
| City           | Customer's city                              |
| Country        | Customer's country                           |
| Channel        | Buyer class (Hospital, Pharmacy)             |
| Sub-channel    | Sector (Government, Private, etc.)           |
| Product Name   | Name of drug                                 |
| Product Class  | Drug classification (Antibiotics, etc.)      |
| Quantity       | Units sold                                   |
| Price          | Price per unit                               |
| Sales          | Total sales amount                           |
| Month/Year     | Date of sale                                 |
| Sales Rep/Team | Sales representative & their team             |
| Manager        | Sales manager overseeing the sale             |

🔗 [Download Dataset](https://drive.google.com/file/d/1npKF_C2tG5psY-at4wvpEgh6T-7KHxEZ/view?usp=share_link)

---

## Model View
![Model View](/PowerBI-Pharmaceutical-Sales/Model%20View.png)

## 🛠️ Solution Approach

| Requirement ID | Solution ID      | Solution Description                                                                          |
|----------------|------------------|-----------------------------------------------------------------------------------------------|
| DM-DA01-REQ-1  | DM-DA01-SOL-1    | Executive Summary dashboard with high-level overview, top products, and city sales analysis.   |
| DM-DA01-REQ-2  | DM-DA01-SOL-2    | Distributor & Customer Analysis dashboard detailing sales by product, distributor, and city.   |

### Tools & Techniques

- **Exploratory Data Analysis (EDA)**: Conducted in **pandas** to check missing values, outliers, and data types.
- **Data Cleaning (Power Query Editor)**:
  - Converted sales figures, price, and quantity into numeric types.
  - Removed duplicate records.
  - Standardized distributor and product names.
  - Validated customer segmentation.
- **Data Model (Power BI)**: Star schema design with separate **dimension** and **fact** tables.
- **Interactive Dashboards**: Filters by year, month, city, country, channel, and sub-channel.

---

## 🔑 Key Insights

- **Top Product Class**: Analgesics - $9.04 Billion  
- **Top Product**: Ionclotide - $51.9 Million  
- **Top City**: Butzbach - $93.5 Million  
- **Price Range Analysis**: Sales peak in the $400-600 range; high-value products drive revenue but have fewer transactions.  
- **Sales Decline (2017-2020)**: Consistent year-over-year decrease, suggesting market contraction or competition pressures.  
- **Seasonality Patterns**:
  - Peaks in **Q2 (April–June)** and **Q4 (Oct–Dec)**.
  - Troughs in **January** and **August**.
- **Sub-channel Performance**:
  - Retail: $3.34 Billion
  - Government: $3.09 Billion
  - Private: $2.52 Billion
  - Institution: $2.88 Billion
- **Sales Team Performance**:
  - **Top Rep**: Jimmy Grey (Charlie Team) - $985M
  - **Top Team**: Charlie Team (Consistent leader)

---

## 💡 Business Recommendations

- Focus on **Analgesics** and **Mood Stabilizers** for sustained growth.
- Optimize pricing in the $400–800 range where revenue is maximized.
- Enhance marketing for **Ionclotide** and create bundle offers based on **Market Basket Analysis**.
- Use **ARIMA/Prophet** models for sales forecasting and inventory planning.
- Prioritize geographic expansion in Poland and under-served German cities.
- Diversify distributor base to mitigate risk.

---

## 🚀 How To Use

1. Open the `.pbix` file in **Power BI Desktop**.  
2. Use filters to slice the data by time period, geography, channel, or product.  
3. Explore the **Executive Summary** and **Sales Team Performance** dashboards for insights.

---

## 📸 Screenshots

### Executive Summary  
![Executive Summary](/PowerBI-Pharmaceutical-Sales/Executive%20Summary.jpeg)

---

### Sales Team Performance  
![Sales Team Performance](/PowerBI-Pharmaceutical-Sales/Sales%20Team%20Performance.jpeg)

---

## Data Processing Pipeline

1. Data cleaning in **Power Query**:
   - Remove duplicates
   - Standardize names
   - Convert data types
2. Data modeling in **Power BI**:
   - Star schema design
   - Dimension & fact tables
3. Visualize insights in **Power BI Dashboards**.

---

## 📄 License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

---

## 🙌 Credits

- Dataset Source: [Foresight BI](https://foresightbi.com.ng/practice-data/3-datasets-for-your-portfolio/)  