import pandas as pd
import os
from .preprocesses import total_revenue ,invoice_month


RAW_DATA_DIR = 'data/raw'
PROCESSED_DATA_DIR = 'data/processed'

def load_data():
    df=pd.read_csv(os.path.join(RAW_DATA_DIR, "online_retail_II.csv"))
    df=df[df['Quantity']>0]
    df = df[~df['Invoice'].astype(str).str.startswith('C')]
    return df

def load_processed_data():
    df=load_data()
    total_revenue(df)
    invoice_month(df)
    df.to_csv(os.path.join(PROCESSED_DATA_DIR, "online_retail_II.csv"), index=False)
    return df