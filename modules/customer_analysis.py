def top_customers(df):
    return (df.groupby('Customer ID')['Revenue'].sum().sort_values(ascending=False).head(10))

