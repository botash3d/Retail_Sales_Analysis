import pandas as pd
import streamlit as st
import plotly.express as px

from modules.data_loader import load_processed_data
from modules.customer_analysis import top_customers

df =load_processed_data()

st.set_page_config(page_title="Customer Analysis", layout="wide")

st.title('Customer Analysis')

st.subheader('Top Customers')

top_10_customers = top_customers(df)

top_10_df = pd.DataFrame(top_10_customers).reset_index()
top_10_df.columns = ['Customer ID','Revenue']

fig=px.bar(
    top_10_df.sort_values('Revenue'),
    x='Revenue',
    y='Customer ID',
    title='Top 10 Customers by revenue',
    orientation="h"
)
fig.update_layout(
    yaxis_title="Revenue (£)",
    xaxis_title="Customer ID",
)

fig.update_traces(texttemplate="£%{x:,.0f}", textposition="outside")
st.plotly_chart(fig,use_container_width=True)


purchase_freq = (
    df.groupby("Customer ID")["Invoice"]
    .nunique()
    .reset_index()
)

purchase_freq.columns = ["Customer ID", "Purchase Frequency"]

purchase_freq_filtered = purchase_freq[
    purchase_freq["Purchase Frequency"] <
    purchase_freq["Purchase Frequency"].quantile(0.99)
]


fig = px.histogram(
    purchase_freq_filtered,
    x="Purchase Frequency",
    nbins=30,
    title="Customer Purchase Frequency Distribution"
)

st.plotly_chart(fig, use_container_width=True)


customer_revenue = (
    df.groupby("Customer ID")["Revenue"]
    .sum()
    .reset_index()
)


customer_revenue_filtered = customer_revenue[
    customer_revenue["Revenue"] < customer_revenue["Revenue"].quantile(0.99)
]


fig = px.histogram(
    customer_revenue_filtered,
    x="Revenue",
    nbins=50,
    title="Customer Revenue Distribution (99% trimmed)"
)

st.plotly_chart(fig, use_container_width=True)
