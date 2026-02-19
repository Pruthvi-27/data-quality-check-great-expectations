# Data-quality-check-great-expectations
Interactive Streamlit dashboard for automated customer data cleaning and validation using Great Expectations. Detects and resolves all data quality issues, providing a fully cleaned dataset ready for analysis.

## 🚀 Features

- Upload CSV files containing customer data
- Clean and standardize data:
  - Customer ID validation
  - Name normalization
  - Age checks
  - Email & phone formatting
  - Country and status cleaning
  - Duplicate detection
- Automated **data validation** using **Great Expectations**
- Interactive **Streamlit dashboard**:
  - Preview raw and cleaned data
  - View row counts before and after cleaning
  - Download cleaned datasets
- Generates **data quality reports** with validation results
- User-friendly, no coding required for end-users

---

## 💻 Tech Stack

- **Python 3.x**  
- **Pandas** – data manipulation  
- **Great Expectations** – data quality validation  
- **Streamlit** – interactive frontend dashboard  

---

## 📂 Project Structure
```
GX/
├── data/
│   ├── raw/
│   │   └── dirty_dataset.csv
│   └── clean/
│       └── cleaned_dataset.csv
├── cleaning/
│   ├── __init__.py
│   └── customer_cleaning.py
├── test_run.py
├── app.py
└── README.md
```


## ⚡ How to Run Locally

1. Clone the repository:
git clone https://github.com/yourusername/data-quality-check-great-expectations.git
cd data-quality-check-great-expectations

2. Install dependencies:
   pip install great-expectations pandas streamlit

3. Run the Streamlit app:
   streamlit run app.py

4. Open the local URL (e.g., http://localhost:8501) in your browser.

📊 Demo
Upload your CSV file → Click Run Data Quality Check → View cleaned dataset → Download CSV.

