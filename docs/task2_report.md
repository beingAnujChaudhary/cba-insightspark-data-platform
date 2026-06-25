# 🔒 Task 2: Data Anonymization & Privacy Report

**Prepared for:** InsightSpark Data Science Team  
**Author:** Anuj Chaudhary, Data Engineering  
**Date:** 2026-06-25

## 1. Executive Summary
This report details the data anonymization pipeline applied to the `mobile_customers` dataset. The objective was to strip Personally Identifiable Information (PII) to comply with data privacy regulations (e.g., Australian Privacy Principles) while preserving the statistical utility required for InsightSpark's downstream machine learning and analytical models.

## 2. Anonymization Techniques Applied

To ensure a defense-in-depth approach to privacy, we utilized a combination of the following techniques:

### A. Data Suppression (Redaction)
Columns that offered no analytical value but posed high privacy risks were completely removed.
*   **Removed:** `customer_id`, `current_location`.

### B. Cryptographic Hashing (Pseudonymization)
While not explicitly requested for all IDs, hashing ensures that if a unique identifier is needed for record linking, it cannot be reverse-engineered.
*   *Note: In this specific pipeline, direct identifiers were dropped to minimize risk.*

### C. Data Masking
Partial information is hidden to allow for visual verification by support staff without exposing full PII.
*   **Username:** Masked to show only the first 2 and last 2 characters (e.g., `us****me`).
*   **Email:** Domain preserved, local part masked (e.g., `***@gmail.com`).
*   **Credit Card Number:** Masked to show only the last 4 digits (e.g., `****1234`).
*   **CVV:** Completely masked (`***`).

### D. Synthetic Data Replacement
Real values were replaced with statistically similar, entirely fake data generated via the `Faker` library.
*   **Replaced:** `name`, `address`, `residence`.

### E. Noise Addition
Random variance was added to temporal data to prevent exact matching attacks.
*   **Applied:** `date_registered`, `birthdate` (±30 days random noise).

### F. Data Generalization (Binning)
Continuous variables were converted into categorical brackets to prevent inference attacks (where a bad actor combines rare job titles with exact ages to identify a person).
*   **Binned:** `age` $\rightarrow$ `age_group` (e.g., 25-34), `salary` $\rightarrow$ `salary_bracket` (e.g., 50k-100k).

### G. Tokenization
Categorical variables were mapped to random tokens to preserve the underlying distribution of the data without exposing the actual labels.
*   **Tokenized:** `credit_card_provider`, `credit_card_expire`, `employer`, `job`.

## 3. Data Utility Assessment
Despite the heavy anonymization, the resulting dataset retains high utility for InsightSpark:
*   **Demographic Analysis:** Age groups and salary brackets allow for customer segmentation.
*   **Behavioral Tracking:** Tokenized employers and job titles allow for occupational trend analysis.
*   **Temporal Analysis:** Noised dates still allow for cohort analysis and registration trend tracking.

## 4. Conclusion
The anonymized dataset (`deliverables/task2.csv`) is now safe for sharing with InsightSpark. It successfully mitigates linkage and inference attacks while maintaining the structural integrity required for robust data science modeling.
