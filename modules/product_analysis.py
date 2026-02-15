def top_products_revenue(df):
    return df.groupby('Description')['Revenue'].sum().head(10)

def top_products_by_quantity(df):
    return df.groupby('Description')['Quantity'].sum().head(10)

def revenue_per_quantity(df):
    product_sales = (df.groupby('Description').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
    }).reset_index()
    )
    product_sales['Revenue_per_unit'] = product_sales['Revenue'] / product_sales['Quantity']

    return product_sales.sort_values(by=['Revenue_per_unit'], ascending=False).head(10)