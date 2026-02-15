import pandas as pd

def total_revenue(df):
    df['Revenue']= df['Quantity']*df['Price']
    return df

def invoice_month(df):
    df['InvoiceDate']= pd.to_datetime(df['InvoiceDate'])
    df['Month']= df['InvoiceDate'].dt.to_period('M').astype(str)
    return df