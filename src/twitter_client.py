import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

class TwitterClient:
    def __init__(self):
        consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
        consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
            raise ValueError("Twitter API credentials not found in .env file.")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def get_trending_topics(self, woeid=1):
        """
        Fetches trending topics for a given WOEID (Where On Earth ID).
        Default WOEID is 1 (Worldwide).
        """
        try:
            trends = self.api.get_place_trends(woeid)
            return trends[0]['trends']
        except tweepy.TweepyException as e:
            print(f"Error fetching trends: {e}")
            return []

    def search_tweets(self, query, count=5):
        """
        Searches for tweets based on a query.
        """
        try:
            tweets = self.api.search_tweets(q=query, count=count, lang="en", tweet_mode="extended")
            return [tweet.full_text for tweet in tweets]
        except tweepy.TweepyException as e:
            print(f"Error searching tweets for '{query}': {e}")
            return []

if __name__ == "__main__":
    client = TwitterClient()
    print("Fetching worldwide trends...")
    trends = client.get_trending_topics()
    for i, trend in enumerate(trends[:5]):
        print(f"{i+1}. {trend['name']} (Tweet Volume: {trend['tweet_volume'] if trend['tweet_volume'] else 'N/A'})")
        sample_tweets = client.search_tweets(trend['name'], count=2)
        if sample_tweets:
            print("   Sample Tweets:")
            for tweet in sample_tweets:
                print(f"     - {tweet[:100]}...") # Print first 100 characters
        print("-" * 30)