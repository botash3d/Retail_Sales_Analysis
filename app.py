import streamlit as st
import pandas as pd
import plotly.express as px

from modules.data_loader import load_processed_data
from modules.kpis import calculate_kpis,monthly_revenue,top_countries
st.set_page_config(page_title="Online Retail Dashboard",layout="wide")

st.title("Online Retail II Sales Dashboard")

# LOAD DATA

df=load_processed_data()

# KPIS

total_revenue , unique_orders ,unique_customers = calculate_kpis(df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:.0f}")
col2.metric("Unique Orders", f"{unique_orders}")
col3.metric("Unique Customers", f"{unique_customers}")

st.divider()

st.subheader("Monthly Revenue")
monthly = monthly_revenue(df)
st.line_chart(monthly.set_index("Month")['Revenue'])

st.subheader("Top Countries")
countries = top_countries(df)
fig = px.bar(countries, x="Country", y="Revenue")
st.plotly_chart(fig)