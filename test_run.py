import pandas as pd
from cleaning.customer_cleaning import clean_customer_data

df_raw = pd.read_csv("data/raw/dirty_dataset.csv", dtype=str)

df_clean = clean_customer_data(df_raw)

df_clean.to_csv("data/clean/cleaned_dataset.csv", index=False)

print("Rows before:", len(df_raw))
print("Rows after :", len(df_clean))
