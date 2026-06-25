# 🏦 CBA InsightSpark Data Platform

**End-to-End Data Engineering, Analytics, Data Privacy, and Database Design**

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/Managed%20with-uv-black?logo=apache&logoColor=white)](https://github.com/astral-sh/uv)
[![Pandas](https://img.shields.io/badge/Pandas-2.2+-150458?logo=pandas)](https://pandas.pydata.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red?logo=sqlite)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> *"Transforming raw transactional and social data into secure, actionable business intelligence for Australia's leading financial institutions."*

---

## 📌 Project Overview

This repository contains my comprehensive solution for the **Commonwealth Bank (CBA) Data Science Virtual Experience Program** on Forage. 

The project simulates the work of an enterprise Data Engineering team supporting **InsightSpark**, a data science specialist partnering with CBA. The objective is to build a robust data platform capable of ingesting, processing, anonymizing, and modeling data from diverse sources to generate insights for businesses, governments, and investors.

### 🎯 Business Problem
CBA and InsightSpark aim to leverage large-scale transactional and open-source data to provide valuable insights. The Data Engineering team is responsible for:
1. Building reliable, scalable data pipelines.
2. Aggregating and processing complex transactional datasets.
3. Enforcing strict data privacy and anonymization protocols.
4. Designing normalized relational databases for unstructured social media data.

---

## 🏗️ System Architecture & Pipeline Flow

```text
┌─────────────┐      ┌──────────────────┐      ┌─────────────────┐      ┌──────────────┐
│  RAW DATA   │ ───▶ │ DATA AGGREGATION │ ───▶ │ PII ANONYMIZATION│ ───▶ │ INSIGHTS &   │
│  (CSV/API)  │      │ & CLEANING       │      │ & GOVERNANCE     │      │ DB DESIGN    │
└─────────────┘      └──────────────────┘      └─────────────────┘      └──────────────┘
       │                      │                         │                        │
       ▼                      ▼                         ▼                        ▼
 [Supermarket]          [Pandas/NumPy]            [Hashlib/Faker]         [SQLAlchemy/ERD]
 [Twitter API]          [KPI Extraction]          [Data Binning]          [3NF Normalization]
```

---

## 📂 Repository Structure

```text
cba-insightspark-data-platform/
│   README.md                 # Project documentation
│   pyproject.toml            # Project metadata & dependencies (uv)
│   uv.lock                   # Lockfile for reproducible environments
│   .gitignore                # Git ignore rules
│
├── data/
│   ├── raw/                  # Original datasets (Not committed)
│   ├── processed/            # Cleaned & aggregated data
│   └── anonymized/           # Privacy-preserved datasets
│
├── notebooks/                # Exploratory Data Analysis (EDA)
│   ├── 01_task1_analysis.ipynb
│   ├── 02_task2_anonymization.ipynb
│   └── 03_task3_twitter_analysis.ipynb
│
├── src/                      # Production-ready Python scripts
│   ├── task1_analysis.py     # Transaction aggregation pipeline
│   ├── task2_anonymization.py# PII masking & hashing pipeline
│   ├── task3_twitter_proposal.py # Social media API strategy
│   └── task4_database_design.py  # SQLAlchemy ORM schema generation
│
├── docs/                     # Business & Technical Documentation
│   ├── task1_report.md       # Analysis methodology & formulas
│   ├── task2_report.md       # Anonymization strategy & risk assessment
│   ├── task3_proposal.md     # Business proposal for Twitter insights
│   └── task4_database_design.md # ERD documentation & normalization logic
│
├── sql/
│   └── schema.sql            # Raw DDL statements for database creation
│
└── deliverables/             # 📤 Final stakeholder submissions
    ├── task1.xlsx            # Analyzed spreadsheet with pivot tables
    ├── task2.csv             # Fully anonymized dataset
    ├── task3.pdf             # Executive proposal for social media analytics
    └── task4.pdf             # Comprehensive database design document
```

---

## ⚙️ Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Core Language** | Python 3.12+ |
| **Package Management** | `uv` (Astral) - *Ultra-fast Python package installer* |
| **Data Manipulation** | Pandas, NumPy, Openpyxl |
| **Data Privacy** | Hashlib (SHA-256), Faker (Synthetic Data) |
| **Database & ORM** | SQLAlchemy, SQLite |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook, Git, GitHub |

---

## 🚀 Environment Setup

This project uses **`uv`**, an extremely fast Python package manager, to handle dependencies and virtual environments.

### 1. Clone the Repository
```bash
git clone https://github.com/beingAnujChaudhary/cba-insightspark-data-platform.git
cd cba-insightspark-data-platform
```

### 2. Initialize & Activate Virtual Environment
```bash
# Create the virtual environment
uv venv

# Activate it
# Windows PowerShell:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
# Sync dependencies from pyproject.toml
uv sync

# OR manually add core packages
uv add pandas numpy matplotlib seaborn openpyxl faker sqlalchemy jupyter
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook
```

---

## 📊 Task 1 — Data Aggregation and Analysis

**Objective:** Analyze supermarket transaction data to extract actionable business insights and identify revenue drivers.

### 🛠️ Technical Implementation
*   **Data Wrangling:** Handled missing values, removed duplicates, and corrected invalid records using `pandas`.
*   **Aggregation:** Utilized `groupby()`, `pivot_table()`, and window functions to calculate KPIs.
*   **Export:** Generated formatted Excel reports using `openpyxl` for non-technical stakeholders.

### 💡 Business Questions Answered
*   Which store generated the highest revenue?
*   Which products contribute the most to overall sales volume?
*   What are the peak transaction periods (time-of-day/day-of-week)?
*   What are the customer spending trends and average basket sizes?

**📁 Deliverables:** `notebooks/01_task1_analysis.ipynb` | `deliverables/task1.xlsx`

---

## 🔒 Task 2 — Data Anonymization & Privacy

**Objective:** Protect customer Personally Identifiable Information (PII) to prevent linkage attacks while preserving the analytical utility of the dataset.

### 🛠️ Technical Implementation
*   **Data Removal:** Dropped high-risk, unnecessary PII columns (Names, direct Phone Numbers).
*   **Cryptographic Hashing:** Applied **SHA-256** via `hashlib` to Customer IDs to allow relational joins without exposing raw IDs.
*   **Data Masking:** Partially masked sensitive fields (e.g., `XXXXXX1234`).
*   **Binning/Generalization:** Used `pd.cut()` to bucket continuous variables (e.g., Age 34 → Age Group 30-40) to prevent identity inference.
*   **Synthetic Data:** Utilized `Faker` to replace specific identifiers with realistic dummy data where structural integrity was required.

**📁 Deliverables:** `notebooks/02_task2_anonymization.ipynb` | `deliverables/task2.csv`

---

## 📱 Task 3 — Social Media Intelligence Proposal

**Objective:** Formulate a strategic proposal on how unstructured data from the `@CommBank` Twitter/X account can be leveraged for business intelligence.

### 🛠️ Technical Implementation & Strategy
*   **API Integration Strategy:** Mapped out data extraction pipelines using the **Twitter API v2** (Tweets, Replies, Retweets, User Metadata).
*   **NLP & Sentiment Analysis:** Proposed utilizing Natural Language Processing (NLP) to classify customer sentiment (Positive/Neutral/Negative).
*   **Topic Modeling:** Identified methods to extract recurring themes (e.g., Credit Cards, Home Loans, Mobile App UX).

### 💡 Potential Business Insights
*   **Brand Monitoring:** Real-time tracking of public perception and crisis management.
*   **Product Feedback:** Identifying friction points in digital banking apps based on user complaints.
*   **Emerging Trends:** Detecting shifts in customer financial needs based on hashtag velocity.

**📁 Deliverables:** `docs/task3_proposal.md` | `deliverables/task3.pdf`

---

## 🗄️ Task 4 — Relational Database Design

**Objective:** Design a highly normalized, scalable relational database schema to store complex, hierarchical Twitter data.

### 🛠️ Technical Implementation
*   **Normalization:** Applied **Third Normal Form (3NF)** principles to eliminate data redundancy and update anomalies.
*   **ORM Generation:** Used **SQLAlchemy** to define Python classes that map to database tables, generating executable DDL (`schema.sql`).
*   **Entity Relationship Design:** 
    *   **Users** (1) ➔ (N) **Tweets**
    *   **Tweets** (1) ➔ (N) **Replies**
    *   **Tweets** (N) ➔ (N) **Mentions** (Resolved via associative entity)
    *   **Quote Retweets** mapped with self-referential foreign keys.

**📁 Deliverables:** `sql/schema.sql` | `docs/task4_database_design.md`

---

## 🗺️ Product Roadmap (Future Enhancements)

To transition this project from a simulated environment to a production-grade enterprise system, the following enhancements are planned:

- [ ] **Automated ETL Orchestration:** Implement **Apache Airflow** or **Prefect** to schedule and monitor data pipelines.
- [ ] **Data Transformations:** Integrate **dbt (data build tool)** for modular SQL transformations and data modeling.
- [ ] **Cloud Data Warehouse:** Migrate the SQLite database to **PostgreSQL** or **Snowflake** for cloud-native scalability.
- [ ] **Interactive Dashboard:** Build a **Streamlit** or **Dash** application to visualize the aggregated insights and sentiment analysis.
- [ ] **Data Quality Framework:** Implement **Great Expectations** to automatically validate data quality at ingestion.

---

## 📈 Key Skills Demonstrated

*   **Data Engineering:** Pipeline design, ETL processes, Data Wrangling.
*   **Data Analysis:** Exploratory Data Analysis (EDA), KPI extraction, Statistical Aggregation.
*   **Data Governance:** PII Anonymization, Cryptographic Hashing, Data Privacy Compliance.
*   **Database Architecture:** Relational Modeling, 3NF Normalization, SQL, SQLAlchemy ORM.
*   **Business Communication:** Translating technical data processes into executive-level business proposals.

---

## 👨‍💻 Author

**Anuj Chaudhary**  
*Aspiring Data Scientist | Machine Learning Engineer | AI Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-@beingAnujChaudhary-black?logo=github)](https://github.com/beingAnujChaudhary)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-@beinganujchaudhary-blue?logo=linkedin)](https://www.linkedin.com/in/beinganujchaudhary/)

---

## 🙏 Acknowledgements

This project was completed as part of the **Commonwealth Bank Data Science Virtual Experience Program** hosted on [Forage](https://www.theforage.com/). 

*Disclaimer: This repository contains my own work and opinions, which do not reflect the official views of Commonwealth Bank or InsightSpark. The datasets and business requirements were provided for educational and portfolio-building purposes.*
