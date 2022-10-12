import pandas as pd
import numpy as np

product_price_df = pd.read_csv("product_price.csv", sep=",")
customer_product_df = pd.read_csv("customer_product.csv", sep=",")

merged = pd.merge(left=product_price_df, right=customer_product_df, how="left", on="product")
print(merged)

final_df = merged.groupby("name")["price"].sum()
print(final_df)