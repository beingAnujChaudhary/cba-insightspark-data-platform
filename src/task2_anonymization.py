"""
Task 2: Data Anonymization
Implements a data privacy pipeline to anonymize customer PII while preserving analytical utility.
"""

import pandas as pd
import numpy as np
import hashlib
from faker import Faker
from pathlib import Path
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
fake = Faker()

def hash_identifier(value: str, salt: str = 'cba_insightspark') -> str:
    """Applies SHA-256 hashing to an identifier."""
    if pd.isna(value): return np.nan
    return hashlib.sha256(f"{salt}_{value}".encode('utf-8')).hexdigest()[:16]

def add_date_noise(date_val, max_days=30):
    """Adds random noise to a date to prevent exact identification."""
    if pd.isna(date_val): return date_val
    try:
        date_obj = pd.to_datetime(date_val)
        noise = timedelta(days=np.random.randint(-max_days, max_days))
        return (date_obj + noise).strftime('%Y-%m-%d')
    except:
        return date_val

def main():
    base_dir = Path(__file__).resolve().parent.parent
    raw_data_path = base_dir / 'data' / 'raw' / 'mobile_customers.xlsx'
    deliverables_dir = base_dir / 'deliverables'
    deliverables_dir.mkdir(exist_ok=True)
    
    logging.info("Loading mobile customer data...")
    df = pd.read_excel(raw_data_path)
    df_anon = df.copy()
    
    # 1. Removal (Redaction)
    logging.info("Removing direct identifiers...")
    df_anon = df_anon.drop(columns=['customer_id', 'current_location'], errors='ignore')
    
    # 2. Masking
    logging.info("Masking sensitive fields...")
    df_anon['username'] = df_anon['username'].apply(lambda x: str(x)[:2] + '*' * (len(str(x))-4) + str(x)[-2:] if len(str(x)) > 4 else '****')
    df_anon['email'] = df_anon['email'].apply(lambda x: f"***@{str(x).split('@')[1]}" if '@' in str(x) else '***@unknown.com')
    df_anon['credit_card_number'] = df_anon['credit_card_number'].apply(lambda x: '****' + str(x)[-4:] if len(str(x)) >= 4 else '****')
    df_anon['credit_card_security_code'] = '***'
    
    # 3. Synthetic Replacement
    logging.info("Generating synthetic replacements...")
    df_anon['name'] = [fake.name() for _ in range(len(df_anon))]
    df_anon['address'] = [fake.address().replace('\n', ', ') for _ in range(len(df_anon))]
    df_anon['residence'] = [fake.city() for _ in range(len(df_anon))]
    
    # 4. Noise Addition
    logging.info("Adding noise to temporal data...")
    df_anon['date_registered'] = df_anon['date_registered'].apply(add_date_noise)
    df_anon['birthdate'] = df_anon['birthdate'].apply(add_date_noise)
    
    # 5. Binning (Generalization)
    logging.info("Binning continuous variables...")
    df_anon['age_group'] = pd.cut(df_anon['age'], bins=[0, 18, 25, 35, 45, 55, 65, 100], labels=['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'], right=False)
    df_anon['salary_bracket'] = pd.cut(df_anon['salary'], bins=[0, 50000, 100000, 150000, 200000, float('inf')], labels=['<50k', '50k-100k', '100k-150k', '150k-200k', '200k+'], right=False)
    df_anon = df_anon.drop(columns=['age', 'salary'])
    
    # 6. Tokenization (Preserving Distribution)
    logging.info("Tokenizing categorical variables...")
    for col in ['credit_card_provider', 'credit_card_expire', 'employer', 'job']:
        unique_vals = df_anon[col].unique()
        token_map = {val: f"TOKEN_{i}" for i, val in enumerate(unique_vals)}
        df_anon[col] = df_anon[col].map(token_map)
        
    # Export
    output_path = deliverables_dir / 'task2.csv'
    df_anon.to_csv(output_path, index=False)
    logging.info(f"Anonymized dataset exported to {output_path}")

if __name__ == "__main__":
    main()