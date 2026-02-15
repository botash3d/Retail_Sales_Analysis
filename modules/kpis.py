def calculate_kpis(df):
    total_revenue =df['Revenue'].sum()
    unique_orders = df['Invoice'].nunique()
    unique_customers = df['Customer ID'].nunique()
    return total_revenue, unique_orders, unique_customers

def monthly_revenue(df):
    return (
        df.groupby('Month')['Revenue'].sum().reset_index(name="Revenue").sort_values(by='Month')
    )
def top_countries(df):
    return (
        df.groupby('Country')['Revenue'].sum().reset_index().sort_values(by='Revenue',ascending=False).head(10)
    )