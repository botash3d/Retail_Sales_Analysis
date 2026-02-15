import streamlit as st
import pandas as pd
import plotly.express as px

from app import df
from modules.data_loader import load_processed_data
from modules.product_analysis import top_products_revenue , top_products_by_quantity,revenue_per_quantity

st.set_page_config(page_title="Product Analysis", layout="wide")

st.title("Product Analysis")

st.subheader("Top 10 Products by Revenue")

df = load_processed_data()
top_10_products_revenue = pd.DataFrame(top_products_revenue(df)).reset_index().sort_values('Revenue', ascending=False)
top_10_products_revenue.columns=['Description','Revenue']

fig =px.bar(top_10_products_revenue, x='Revenue', y='Description',orientation="h")

fig.update_layout(
    height=600,
    yaxis=dict(autorange="reversed"),
    xaxis_title="Revenue (£)",
    yaxis_title="Product",
    bargap=0.3,
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 Products by Quantity")

top_products_by_quantity = pd.DataFrame(top_products_by_quantity(df)).reset_index().sort_values('Quantity', ascending=False)
top_products_by_quantity.columns = ['Description','Quantity']
fig = px.bar(top_products_by_quantity, x='Quantity', y='Description',orientation="h")
fig.update_layout(
    height=600,
    yaxis=dict(autorange="reversed"),
    xaxis_title="Quantity",
    yaxis_title="Product",
    bargap=0.3,
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Revenue by Quantity")

revenue_per_unit=revenue_per_quantity(df)

fig=px.bar(revenue_per_unit, x='Revenue_per_unit', y='Description',orientation="h")
fig.update_layout(
    height=600,
    yaxis=dict(autorange="reversed"),
    xaxis_title="Revenue (£)",
    yaxis_title="Product",
    bargap=0.3,
)

st.plotly_chart(fig, use_container_width=True)