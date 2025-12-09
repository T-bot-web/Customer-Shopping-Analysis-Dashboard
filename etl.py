import pandas as pd
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]   
DATA_DIR = BASE / 'data'
RAW_CSV = DATA_DIR / 'customer_shopping_analysis.csv'
CLEAN_CSV = DATA_DIR / 'customer_shopping_cleaned.csv'
DB_PATH = DATA_DIR / 'customer_dashboard.db'

def load_csv(path):
    return pd.read_csv(path)

def clean_df(df):
    
    df.columns = [c.strip().lower().replace(' ', '_').replace('(', '').replace(')', '') for c in df.columns]

    
    if 'purchase_amount_usd' in df.columns:
        df['purchase_amount_usd'] = pd.to_numeric(df['purchase_amount_usd'], errors='coerce')

    if 'review_rating' in df.columns:
        df['review_rating'] = pd.to_numeric(df['review_rating'], errors='coerce')

    
    if 'category' in df.columns:
        df['category'] = df['category'].fillna('Unknown')

  
    text_cols = df.select_dtypes(include=['object']).columns
    for c in text_cols:
        df[c] = df[c].astype(str).str.strip()

    return df

def save_clean_csv(df):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_CSV, index=False)
    print('Clean CSV saved to', CLEAN_CSV)

def load_to_sqlite(df):
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('customers', conn, if_exists='replace', index=False)
    conn.close()
    print('Loaded into SQLite DB at', DB_PATH)

def main():
    print('Running ETL...')
    df = load_csv(RAW_CSV)
    df = clean_df(df)
    save_clean_csv(df)
    load_to_sqlite(df)
    print('ETL finished.')

if __name__ == '__main__':
    main()
