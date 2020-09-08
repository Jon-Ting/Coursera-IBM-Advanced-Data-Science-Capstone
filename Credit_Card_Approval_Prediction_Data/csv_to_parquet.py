import pandas as pd

df1 = pd.read_csv("application_record.csv")
df2 = pd.read_csv("credit_record.csv")
df1.to_parquet(path="application_record.parquet")
df2.to_parquet(path="credit_record.parquet")
