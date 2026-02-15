# Online Retail II Sales Analysis Dashboard

## Overview

This project presents an interactive sales analytics dashboard built using the Online Retail II transactional dataset. The objective is to analyze historical e-commerce data and extract structured insights related to revenue trends, customer behavior, and product performance.

The system transforms raw transactional records into business-oriented metrics through preprocessing, aggregation, and interactive visualization using Streamlit and Plotly.

---

## Features

### Main Dashboard
- Total Revenue
- Total Orders
- Total Customers
- Monthly Revenue Trend
- Top Countries by Revenue

### Customer Analysis
- Top 10 Customers by Revenue
- Customer Revenue Distribution
- Purchase Frequency Distribution

### Product Analysis
- Top 10 Products by Revenue
- Top 10 Products by Quantity Sold
- Revenue per Unit Analysis

---

## Dataset

**Dataset:** Online Retail II  
**Type:** Transaction-level retail data  

### Preprocessing Steps
- Removed cancelled invoices
- Removed negative quantities (returns)
- Removed missing `CustomerID`
- Created `Revenue` column (`Quantity × UnitPrice`)
- Extracted `InvoiceMonth` for time-based analysis

---

## Tech Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Matplotlib

---

## Installation and Setup

### 1. Clone the Repository

git clone https://github.com/yourusername/online-retail-analysis.git 

cd online-retail-analysis

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Add a processed folder

In the data folder make a new folder named 'processed'

### 4. Run the Application

streamlit run app.py

The dashboard will open in your browser.

------------------------------------------------------------------------

## Key Insights

-   Revenue distribution follows a Pareto-like pattern.
-   A small subset of customers contributes disproportionately to total
    revenue.
-   Product performance is highly concentrated among top-selling SKUs.
-   Customer purchase frequency shows right-skewed behavior.
-   Revenue per unit analysis distinguishes between volume-driven and
    price-driven products.

------------------------------------------------------------------------

## Future Improvements

-   Customer segmentation using clustering techniques
-   Sales forecasting using time-series models
-   Recommendation systems
-   Real-time data integration
-   Cloud deployment

------------------------------------------------------------------------

## Artifacts

-   Video Demonstration: 
-   Term Project Report (PDF): 
-   Source Code: This repository

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.
