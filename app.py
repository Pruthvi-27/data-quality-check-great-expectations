import streamlit as st
import pandas as pd
from cleaning.customer_cleaning import clean_customer_data

st.set_page_config(page_title="Data Quality Dashboard", layout="wide")

st.title("📊 Customer Data Quality Check")
st.write("Upload a CSV file to clean and validate customer data.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df_raw = pd.read_csv(uploaded_file, dtype=str)

    st.subheader("🔍 Raw Data Preview")
    st.dataframe(df_raw.head())

    if st.button("Run Data Quality Check"):
        df_clean = clean_customer_data(df_raw)

        st.success("Data Cleaning Completed!")

        col1, col2 = st.columns(2)
        col1.metric("Rows Before Cleaning", len(df_raw))
        col2.metric("Rows After Cleaning", len(df_clean))

        st.subheader("✅ Cleaned Data Preview")
        st.dataframe(df_clean.head())

        csv = df_clean.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned Data",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )
