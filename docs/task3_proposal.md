# 📱 Task 3: Social Media Intelligence Proposal

**To:** InsightSpark Data Science Team & CBA Stakeholders  
**From:** Anuj Chaudhary, Data Engineering Team  
**Subject:** Unlocking Business Intelligence from @CommBank Unstructured Social Media Data  

## 1. Executive Summary
While structured data (transactions) tells us *what* our customers are doing, unstructured data (social media) tells us *why* they are doing it. This proposal outlines a framework for InsightSpark to ingest, process, and analyze unstructured data from the **@CommBank** Twitter/X account to drive actionable business intelligence.

## 2. The Value of Unstructured Data
By leveraging the **Twitter API v2**, we can extract a rich matrix of data points:
*   **Tweet Objects:** Text content, timestamps, language, and conversation IDs.
*   **Engagement Metrics:** Reply counts, retweet counts, like counts.
*   **Entities:** Hashtags, mentioned users, and annotated topics.

## 3. Proposed Business Insights & Use Cases

### A. Real-Time Brand Sentiment & Crisis Management
*   **Insight:** Track daily sentiment (Positive, Neutral, Negative) of mentions directed at @CommBank.
*   **Business Value:** If the CBA mobile app experiences an outage, Twitter will immediately spike with negative sentiment. This allows CBA PR and IT teams to respond in real-time before the issue escalates.

### B. Customer Support Bottleneck Identification
*   **Insight:** Analyze reply threads to measure average response times and customer frustration levels.
*   **Business Value:** By categorizing complaints (e.g., #CreditCard, #HomeLoan, #Scam), CBA can identify which product lines are generating the most friction and allocate customer support resources accordingly.

### C. Fraud & Scam Alert Monitoring
*   **Insight:** Track spikes in keywords related to "scam", "phishing", or "unauthorized transaction".
*   **Business Value:** Proactively identify new fraud vectors targeting CBA customers in the wild, allowing the cybersecurity team to issue warnings or block malicious domains before they scale.

## 4. Technical Implementation Strategy
1.  **Ingestion:** Use the Twitter API v2 `/2/tweets/search/recent` endpoint to query `from:CommBank` and `@CommBank` mentions.
2.  **Transformation (NLP):** Apply Python libraries (like `TextBlob` or `HuggingFace Transformers`) to clean text and assign sentiment polarity scores (-1 to 1).
3.  **Storage:** Load the structured insights into our normalized relational database (as designed in Task 4).
4.  **Visualization:** Feed the aggregated data into a BI dashboard for CBA executives to monitor daily brand health.

## 5. Conclusion
Integrating @CommBank Twitter data into InsightSpark’s data lake will bridge the gap between quantitative transaction metrics and qualitative customer emotions, empowering CBA to make proactive, customer-centric decisions.