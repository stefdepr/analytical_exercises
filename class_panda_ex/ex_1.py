import pandas as pd
import numpy as np

data_path = "Boston.csv"

boston_df = pd.read_csv(data_path, sep=",")
print(boston_df.head(3))

bostond_df_sub = boston_df[(boston_df["crim"] < 0.03) & (boston_df["rm"] > 6)]
print(bostond_df_sub)

agg_dict = {"medv": [np.mean, np.std]}
print(boston_df.groupby("rad").agg(agg_dict))

