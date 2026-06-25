"""
Task 3: Social Media Intelligence Pipeline
Simulates Twitter API ingestion and applies NLP for sentiment and topic analysis.
"""

import pandas as pd
import numpy as np
import re
from textblob import TextBlob
from pathlib import Path
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_mock_tweets(n=100):
    """Generates mock Twitter data simulating the API v2 response structure."""
    np.random.seed(42)
    texts = [
        "The new @CommBank app update is amazing, so much faster! 🚀 #Banking",
        "I've been on hold with @CommBank support for 2 hours. Terrible service.",
        "Did anyone else get a weird SMS from CommBank? Looks like a scam/phishing attempt.",
        "Just got my new credit card delivered. Thanks @CommBank! ",
        "Why is the NetBank portal down again? I need to pay my bills! 😡",
        "CommBank home loan rates are super competitive right now. Highly recommend.",
        "Fraud alert: someone tried to use my card. @CommBank blocked it instantly, great security.",
        "The CommBank Yello rewards program is a joke, no good perks anymore.",
        "Love the Bill Sense feature in the app, helps me track my spending.",
        "Branches closing down everywhere, what is happening to customer service?"
    ]
    return pd.DataFrame({
        'tweet_id': [f"tw_{i}" for i in range(n)],
        'created_at': [datetime.now() - timedelta(hours=np.random.randint(1, 100)) for _ in range(n)],
        'text': np.random.choice(texts, n),
        'like_count': np.random.randint(0, 50, n),
        'reply_count': np.random.randint(0, 20, n)
    })

def analyze_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """Applies NLP sentiment analysis to tweet text."""
    df['clean_text'] = df['text'].apply(lambda x: re.sub(r'@\w+|http\S+|[^A-Za-z0-9\s!?]', '', x))
    df['sentiment_score'] = df['clean_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['sentiment_category'] = df['sentiment_score'].apply(lambda x: 'Positive' if x > 0.1 else ('Negative' if x < -0.1 else 'Neutral'))
    return df

def extract_topics(df: pd.DataFrame) -> pd.DataFrame:
    """Extracts business-relevant topics from the dataset."""
    keywords = ['app', 'credit card', 'home loan', 'scam', 'fraud', 'support', 'branch', 'rewards']
    topic_counts = {kw: df['text'].str.contains(kw, case=False).sum() for kw in keywords}
    return pd.DataFrame(list(topic_counts.items()), columns=['Topic', 'Mentions']).sort_values('Mentions', ascending=False)

def main():
    base_dir = Path(__file__).resolve().parent.parent
    deliverables_dir = base_dir / 'deliverables'
    deliverables_dir.mkdir(exist_ok=True)
    
    logging.info("Simulating Twitter API v2 ingestion...")
    df = generate_mock_tweets()
    
    logging.info("Running NLP Sentiment Analysis...")
    df = analyze_sentiment(df)
    
    logging.info("Extracting trending topics...")
    topics = extract_topics(df)
    
    # Generate Executive Summary
    sentiment_dist = df['sentiment_category'].value_counts(normalize=True) * 100
    summary = f"""
# @CommBank Twitter Intelligence Report
**Date:** {datetime.now().strftime('%Y-%m-%d')}
**Total Tweets Analyzed:** {len(df)}

## Key Findings:
1. **Brand Sentiment:** {sentiment_dist.get('Positive', 0):.1f}% Positive, {sentiment_dist.get('Neutral', 0):.1f}% Neutral, {sentiment_dist.get('Negative', 0):.1f}% Negative.
2. **Top Discussed Product:** {topics.iloc[0]['Topic']} ({topics.iloc[0]['Mentions']} mentions).
3. **Risk Alert:** Detected mentions of 'scam' and 'fraud'. Requires immediate cybersecurity review.
"""
    with open(deliverables_dir / 'task3_executive_summary.txt', 'w') as f:
        f.write(summary)
        
    df.to_csv(deliverables_dir / 'task3_processed_data.csv', index=False)
    logging.info("Task 3 pipeline complete. Deliverables exported.")

if __name__ == "__main__":
    main()