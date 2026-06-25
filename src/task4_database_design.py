# ==========================================
# 🗄️ TASK 4: DATABASE DESIGN VIA SQLALCHEMY ORM
# ==========================================
from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# Initialize the Base class and a local SQLite engine for testing
Base = declarative_base()
engine = create_engine('sqlite:///data/processed/comm_bank_twitter.db', echo=False)

# ==========================================
# 📊 DEFINE TABLES (ORM CLASSES)
# ==========================================

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(String(50), primary_key=True)
    username = Column(String(50), nullable=False)
    display_name = Column(String(100))
    account_created_at = Column(DateTime)
    
    # Relationships
    tweets = relationship("Tweet", back_populates="author")
    mentions = relationship("Mention", back_populates="mentioned_user")

class Tweet(Base):
    __tablename__ = 'tweets'
    
    tweet_id = Column(String(50), primary_key=True)
    author_id = Column(String(50), ForeignKey('users.user_id'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    tweet_text = Column(Text, nullable=False)
    like_count = Column(Integer, default=0)
    retweet_count = Column(Integer, default=0)
    
    # Relationships
    author = relationship("User", back_populates="tweets")
    replies = relationship("Reply", foreign_keys="Reply.parent_tweet_id", back_populates="parent_tweet")
    quotes = relationship("QuoteRetweet", foreign_keys="QuoteRetweet.original_tweet_id", back_populates="original_tweet")
    mentions = relationship("Mention", back_populates="tweet")

class Reply(Base):
    __tablename__ = 'replies'
    
    reply_id = Column(Integer, primary_key=True, autoincrement=True)
    parent_tweet_id = Column(String(50), ForeignKey('tweets.tweet_id'), nullable=False)
    reply_tweet_id = Column(String(50), ForeignKey('tweets.tweet_id'), nullable=False)
    
    # Relationships
    parent_tweet = relationship("Tweet", foreign_keys=[parent_tweet_id], back_populates="replies")
    reply_tweet = relationship("Tweet", foreign_keys=[reply_tweet_id])

class QuoteRetweet(Base):
    __tablename__ = 'quote_retweets'
    
    quote_id = Column(Integer, primary_key=True, autoincrement=True)
    original_tweet_id = Column(String(50), ForeignKey('tweets.tweet_id'), nullable=False)
    quoting_tweet_id = Column(String(50), ForeignKey('tweets.tweet_id'), nullable=False)
    
    # Relationships
    original_tweet = relationship("Tweet", foreign_keys=[original_tweet_id], back_populates="quotes")
    quoting_tweet = relationship("Tweet", foreign_keys=[quoting_tweet_id])

class Mention(Base):
    __tablename__ = 'mentions'
    
    mention_id = Column(Integer, primary_key=True, autoincrement=True)
    tweet_id = Column(String(50), ForeignKey('tweets.tweet_id'), nullable=False)
    mentioned_user_id = Column(String(50), ForeignKey('users.user_id'), nullable=False)
    
    # Relationships
    tweet = relationship("Tweet", back_populates="mentions")
    mentioned_user = relationship("User", back_populates="mentions")

# ==========================================
# 🚀 EXECUTE SCHEMA CREATION
# ==========================================
def generate_database():
    """Creates the database and tables based on the ORM definitions."""
    print("🔄 Generating CommBank Twitter Database Schema...")
    Base.metadata.create_all(engine)
    print("✅ Database and tables created successfully at: data/processed/comm_bank_twitter.db")

if __name__ == "__main__":
    import os
    os.makedirs('data/processed', exist_ok=True)
    generate_database()