from src.analysis import load_data, aggregate_data
from src.plots import *

df = load_data()

region_sales, product_sales = aggregate_data(df)

line_plot(df)
bar_plot(region_sales)
histogram(df)
scatter_plot(df)
subplots(df)
heatmap(df)
annotated_plot(df)