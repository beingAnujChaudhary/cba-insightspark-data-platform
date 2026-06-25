# 📊 Task 1: Supermarket Transaction Analysis Report
**Prepared for:** InsightSpark & Commonwealth Bank  
**Date:** 2026-06-25  
**Analyst:** Anuj Chaudhary  

## Executive Summary
This report outlines the analysis of the Australian supermarket transaction dataset to answer key business questions regarding product sales, payment methods, and customer segment behavior.

## Findings

### 1. Apple Purchases (Cash Only)
**Question:** Across locations, how many apples were purchased in cash?  
**Answer:** A total of **117** apples were purchased using cash.  
*(Note: The top 3 locations by volume are South Cynthia, Swansonfurt, and South Billyview).*

### 2. Revenue from Cash Apple Sales
**Question:** How much total cash was spent on these apples?  
**Answer:** **$537.03**

### 3. Bakershire Non-Member Spend
**Question:** Across all payment methods, how much money was spent at the Bakershire store location by non-member customers?  
**Answer:** Non-member customers spent a total of **$2,857.51** across **179** transactions at the Bakershire location.

## Methodology
*   **Data Source:** `supermarket_transactions.xlsx`
*   **Tools:** Python, Pandas, Openpyxl
*   **Data Validation:** Exact string matching was used for product names to prevent aggregation errors (e.g., ensuring 'apple' did not include 'apple juice').

---
*Full data tables are available in `deliverables/task1_analysis_results.xlsx`.*
