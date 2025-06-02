
# 📊 Customer & Sales Analysis Dashboard

A comprehensive **Power BI** solution to analyze customer demographics, sales performance, policy distributions, and claims data for an insurance company. This project delivers insights into customer behavior, policy trends, and sales performance across multiple dimensions such as gender, income, coverage, and vehicle class.

## Overview

This project analyzes customer and policy data across **January** and **February**, with interactive dashboards in Power BI. The insights help stakeholders understand customer profiles, optimize product offerings, and track key performance metrics across regions and policy types.

### Key Dashboards:

1. **Customer Analysis Dashboard**  
   ![Customer Analysis](/IBM_Marketing_Customer_Evaluation/Customer%20Analysis.png)

2. **Sales Overview Dashboard**  
   ![Sales Overview](/IBM_Marketing_Customer_Evaluation/Sales%20Overview.png)

## Features

- Customer demographics analysis (gender, marital status, employment)
- Policy distribution by type, state, and vehicle class
- Sales performance tracking by agents, offers, and policy counts
- Claim amount and lifetime value summaries
- Filters for month and policy categories
- Insights into customer behavior patterns and trends

## Tech Stack

- **Data Analysis**: Power BI Desktop
- **Data Modeling**: Power Query, Star Schema
- **Visualization**: Power BI charts, slicers, and interactive elements

## Project Structure

```
customer-sales-analysis/
├── Power BI Report.pbix           # Main Power BI report with dashboards
├── Customer Analysis.png          # Screenshot of the Customer Analysis dashboard
├── Sales Overview.png             # Screenshot of the Sales Overview dashboard
├── README.md                      # Project documentation
```

## Usage

1. Open the **Power BI Report.pbix** file in **Power BI Desktop**.
2. Use slicers (Month, Policy Type, State, etc.) to explore the data.
3. Navigate between:
   - **Customer Analysis**: Demographics, policy distribution, claims, and complaints.
   - **Sales Overview**: Lifetime value, claims, sales by agents and channels, and policy trends.
4. Identify key trends such as:
   - Most opted policy types (e.g., Personal Auto)
   - States with highest policies (e.g., California)
   - Customer profiles by gender, marital status, and employment.

## Key Insights

- **Customer Count**: 9.1K
- **Average Policies per Customer**: 2.97
- **Average Claim Amount**: 434.09
- **Customer Profile**:
  - 51.58% Female, 48.42% Male
  - 58.5% Married, 62% Employed
- **Most Opted Policy Type**: Personal Auto
- **Top State**: California (highest number of policies)
- **Top Vehicle Class**: Four-Door Cars
- **Key Trends**:
  - Sales peak early in the month and decline toward the end.
  - Basic coverage is the most popular across all states.

## Data Processing Steps

- Data loaded and cleaned using **Power Query**:
  - Standardized categories (e.g., Policy Type, Vehicle Class)
  - Filtered and aggregated metrics
- Star schema model built in **Power BI**:
  - Fact table: Policies, Claims, Sales
  - Dimension tables: Customer, Policy Type, State, Vehicle Class

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Credits

- Developed by: **Virinchi Alahari**
- Dataset: **Sample Insurance Data (simulated)**
