import pandas as pd

def load_data():
    df = pd.read_csv("data/sales.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

def aggregate_data(df):
    region_sales = df.groupby("region")["sales"].sum()
    product_sales = df.groupby("product")["sales"].sum()
    return region_sales, product_sales