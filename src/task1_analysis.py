"""
Task 1: Data Aggregation and Analysis
Analyzes supermarket transaction data to extract business insights for InsightSpark.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def load_data(file_path: Path) -> pd.DataFrame:
    """Loads the supermarket transaction data."""
    logging.info(f"Loading data from {file_path}")
    return pd.read_excel(file_path)

def analyze_apples_cash(df: pd.DataFrame) -> tuple:
    """
    Answers: 
    1. Across locations, how many apples were purchased in cash?
    2. How much total cash was spent on these apples?
    """
    # Filter for exact 'apple' matches and 'cash' payment
    mask = (df['product_name'].str.lower() == 'apple') & (df['payment_method'].str.lower() == 'cash')
    apples_cash = df[mask].copy()
    
    # Q1: Group by store and sum quantity
    q1 = apples_cash.groupby('store')['quantity'].sum().reset_index()
    q1.columns = ['Store_Location', 'Total_Apples_Purchased_Cash']
    
    # Q2: Sum total amount
    q2 = apples_cash['total_amount'].sum()
    
    return q1, q2

def analyze_bakershire_non_member(df: pd.DataFrame) -> float:
    """
    Answers: 
    3. Across all payment methods, how much money was spent at the Bakershire 
       store location by non-member customers?
    """
    mask = (df['store'].str.lower() == 'bakershire') & (df['customer_type'].str.lower() == 'non-member')
    return df[mask]['total_amount'].sum()

def main():
    # Define paths
    base_dir = Path(__file__).resolve().parent.parent
    raw_data_path = base_dir / 'data' / 'raw' / 'supermarket_transactions.xlsx'
    deliverables_dir = base_dir / 'deliverables'
    deliverables_dir.mkdir(exist_ok=True)
    
    # Load data
    df = load_data(raw_data_path)
    logging.info(f"Data loaded successfully. Shape: {df.shape}")
    
    # Execute Analysis
    logging.info("Running analysis...")
    q1_result, q2_result = analyze_apples_cash(df)
    q3_result = analyze_bakershire_non_member(df)
    
    # Print Results
    print("\n" + "="*60)
    print("TASK 1: BUSINESS INSIGHTS")
    print("="*60)
    print("Q1: Apples purchased in cash by location:")
    print(q1_result.to_string(index=False))
    print(f"\nQ2: Total cash spent on apples: ${q2_result:,.2f}")
    print(f"Q3: Total spend at Bakershire by non-members: ${q3_result:,.2f}")
    print("="*60 + "\n")
    
    # Export to Excel
    output_path = deliverables_dir / 'task1.xlsx'
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        q1_result.to_excel(writer, sheet_name='Q1_Apples_by_Location', index=False)
        
        summary_df = pd.DataFrame({
            'Metric': ['Total Cash Spent on Apples', 'Bakershire Non-Member Spend'],
            'Value': [f"${q2_result:,.2f}", f"${q3_result:,.2f}"]
        })
        summary_df.to_excel(writer, sheet_name='Financial_Summary', index=False)
        
    logging.info(f"Deliverable successfully exported to {output_path}")

if __name__ == "__main__":
    main()