# 🗄️ Task 4: Relational Database Design Proposal

**To:** InsightSpark Data Engineering Team & CBA Stakeholders  
**From:** Anuj Chaudhary, Data Engineering Team  
**Subject:** Normalized Database Schema for @CommBank Twitter Data  

## 1. Design Principles
This database design adheres to **Microsoft’s Database Design Basics** and the principles of **Third Normal Form (3NF)** to ensure:
*   **Reduced Redundancy:** Tweet text and user metadata are stored only once.
*   **Data Integrity:** Primary Keys (PK) and Foreign Keys (FK) enforce referential integrity.
*   **Subject-Based Tables:** Information is divided logically into Users, Core Tweets, and Interaction Types.

## 2. List of Tables & Fields

### Table 1: `Users`
Stores the metadata of the Twitter accounts interacting with or authoring tweets.
*   `user_id` **(Primary Key)**: Unique alphanumeric identifier for the Twitter user.
*   `username`: The user's @ handle (e.g., @CommBank).
*   `display_name`: The public display name of the user.
*   `account_created_at`: Timestamp of when the user created their account.

### Table 2: `Tweets`
Stores the core content and metrics of the tweets.
*   `tweet_id` **(Primary Key)**: Unique alphanumeric identifier for the tweet.
*   `author_id` **(Foreign Key)**: Links to `Users.user_id`.
*   `created_at`: Timestamp of when the tweet was posted.
*   `tweet_text`: The full text content of the tweet.
*   `like_count`: Integer representing the number of likes.
*   `retweet_count`: Integer representing the number of standard retweets.

### Table 3: `Replies`
Maps the relationship between a parent tweet and the tweet replying to it.
*   `reply_id` **(Primary Key)**: Unique identifier for the reply relationship.
*   `parent_tweet_id` **(Foreign Key)**: Links to `Tweets.tweet_id` (the original tweet).
*   `reply_tweet_id` **(Foreign Key)**: Links to `Tweets.tweet_id` (the actual reply tweet).

### Table 4: `Quote_Retweets`
Maps the relationship between an original tweet and a new tweet that quotes it.
*   `quote_id` **(Primary Key)**: Unique identifier for the quote relationship.
*   `original_tweet_id` **(Foreign Key)**: Links to `Tweets.tweet_id`.
*   `quoting_tweet_id` **(Foreign Key)**: Links to `Tweets.tweet_id`.

### Table 5: `Mentions`
Tracks when a specific user (like @CommBank) is tagged in a tweet.
*   `mention_id` **(Primary Key)**: Unique identifier for the mention record.
*   `tweet_id` **(Foreign Key)**: Links to `Tweets.tweet_id`.
*   `mentioned_user_id` **(Foreign Key)**: Links to `Users.user_id`.

## 3. Table Relationships
*   **Users ➔ Tweets (One-to-Many):** One user can author many tweets, but a tweet has only one author.
*   **Tweets ➔ Replies (One-to-Many):** One parent tweet can receive many replies.
*   **Tweets ➔ Quote_Retweets (One-to-Many):** One original tweet can be quoted multiple times.
*   **Tweets ➔ Mentions (One-to-Many):** One tweet can contain multiple user mentions.
*   **Users ➔ Mentions (One-to-Many):** One user (e.g., @CommBank) can be mentioned across many different tweets.

## 4. Conclusion
This normalized structure eliminates data redundancy, ensures high data integrity through strict foreign key constraints, and provides InsightSpark's data scientists with a highly queryable schema for extracting complex social media insights.