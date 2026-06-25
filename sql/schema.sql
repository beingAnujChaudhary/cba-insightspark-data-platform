-- ==========================================
-- 🗄️ TASK 4: DATABASE SCHEMA FOR TWITTER DATA
-- ==========================================
-- Designed following 3rd Normal Form (3NF) principles
-- to reduce redundancy and ensure data integrity.

-- 1. USERS TABLE
CREATE TABLE Users (
    user_id VARCHAR(50) PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    display_name VARCHAR(100),
    account_created_at TIMESTAMP
);

-- 2. TWEETS TABLE
CREATE TABLE Tweets (
    tweet_id VARCHAR(50) PRIMARY KEY,
    author_id VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    tweet_text TEXT NOT NULL,
    like_count INT DEFAULT 0,
    retweet_count INT DEFAULT 0,
    FOREIGN KEY (author_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- 3. REPLIES TABLE
CREATE TABLE Replies (
    reply_id SERIAL PRIMARY KEY,
    parent_tweet_id VARCHAR(50) NOT NULL,
    reply_tweet_id VARCHAR(50) NOT NULL,
    FOREIGN KEY (parent_tweet_id) REFERENCES Tweets(tweet_id) ON DELETE CASCADE,
    FOREIGN KEY (reply_tweet_id) REFERENCES Tweets(tweet_id) ON DELETE CASCADE
);

-- 4. QUOTE_RETWEETS TABLE
CREATE TABLE Quote_Retweets (
    quote_id SERIAL PRIMARY KEY,
    original_tweet_id VARCHAR(50) NOT NULL,
    quoting_tweet_id VARCHAR(50) NOT NULL,
    FOREIGN KEY (original_tweet_id) REFERENCES Tweets(tweet_id) ON DELETE CASCADE,
    FOREIGN KEY (quoting_tweet_id) REFERENCES Tweets(tweet_id) ON DELETE CASCADE
);

-- 5. MENTIONS TABLE
CREATE TABLE Mentions (
    mention_id SERIAL PRIMARY KEY,
    tweet_id VARCHAR(50) NOT NULL,
    mentioned_user_id VARCHAR(50) NOT NULL,
    FOREIGN KEY (tweet_id) REFERENCES Tweets(tweet_id) ON DELETE CASCADE,
    FOREIGN KEY (mentioned_user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);