import pandas as pd
import re

def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # CUSTOMER ID
    df['customer_id'] = df['customer_id'].astype(str).str.strip()
    df = df[df['customer_id'].str.match(r'^\d+$', na=False)]

    # NAME
    df['name'] = df['name'].fillna('Unknown').str.strip().str.title()

    # AGE
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df = df[(df['age'] >= 18) & (df['age'] <= 100)]

    # EMAIL
    df['email'] = df['email'].fillna('Unknown')

    # PHONE
    def standardize_phone(phone):
        if pd.isna(phone) or str(phone).strip() == '':
            return None
        digits = re.sub(r'\D', '', phone)
        if len(digits) >= 10:
            return digits[-10:]
        return None

    df['phone'] = df['phone'].apply(standardize_phone)

    # COUNTRY
    df['country'] = df['country'].fillna('Unknown').str.title()

    # AMOUNT
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['amount'] = df['amount'].where(df['amount'] >= 0)

    # ORDER DATE
    df['order_date'] = pd.to_datetime(
        df['order_date'], errors='coerce'
    ).dt.strftime('%Y-%m-%d')

    # STATUS
    df['status'] = df['status'].fillna('Unknown').str.title()

    # DUPLICATE FLAG
    df['duplicate_flag'] = df.duplicated(
        subset=['customer_id', 'order_date'],
        keep='first'
    ).astype(int)

    return df.reset_index(drop=True)
