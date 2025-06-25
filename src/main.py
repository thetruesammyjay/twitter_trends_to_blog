import datetime
from twitter_client import TwitterClient
from blog_poster import BlogPoster

try:
    from config import settings
except ImportError:
    print("Warning: config/settings.py not found or config is not a package. Using default values.")
    class Settings:
        TECH_KEYWORDS = ['tech', 'ai', 'software', 'coding', 'developer',
                         'startup', 'innovation', 'blockchain', 'cybersecurity', 'cloud']
        TREND_LOCATION = 1 # Worldwide
        DEFAULT_TAGS = ["tech", "trends", "twitter"]
        POST_STATUS = "publish"
        SAMPLE_TWEET_COUNT = 3 # Add this default
    settings = Settings()

def format_blog_content(trends_data):
    """
    Formats the trending topics and sample tweets into HTML content for a blog post.
    """
    html_content = "<h1>Today's Top Tech Trends on Twitter</h1>"
    html_content += f"<p>Date: {datetime.date.today().strftime('%B %d, %Y')}</p>"
    html_content += "<p>Here are some of the most discussed technology trends and related tweets on Twitter right now:</p>"

    if not trends_data:
        html_content += "<p>No tech trends found today. Check back later!</p>"
        return html_content

    for i, trend in enumerate(trends_data):
        html_content += f"<h2>{i+1}. {trend['name']}</h2>"
        if trend['tweet_volume']:
            html_content += f"<p><strong>Tweet Volume:</strong> {trend['tweet_volume']:,}</p>"
        else:
            html_content += "<p><strong>Tweet Volume:</strong> N/A</p>"

        if trend['sample_tweets']:
            html_content += "<p><strong>Sample Tweets:</strong></p><ul>"
            for tweet in trend['sample_tweets']:
                # Basic sanitization for HTML display
                clean_tweet = tweet.replace("<", "&lt;").replace(">", "&gt;")
                html_content += f"<li>{clean_tweet}</li>"
            html_content += "</ul>"
        else:
            html_content += "<p>No sample tweets found for this trend.</p>"
        html_content += "<hr>" # Separator for trends

    html_content += "<p>Stay tuned for more updates on the ever-evolving world of technology!</p>"
    return html_content

def run_script():
    try:
        twitter_client = TwitterClient()
        blog_poster = BlogPoster()
    except ValueError as e:
        print(f"Initialization error: {e}")
        return

    print("Fetching trending topics...")
    all_trends = twitter_client.get_trending_topics(woeid=settings.TREND_LOCATION)

    tech_trends = []
    print("Filtering for tech-related trends...")
    for trend in all_trends:
        # Check if any tech keyword is in the trend name (case-insensitive)
        if any(keyword in trend['name'].lower() for keyword in settings.TECH_KEYWORDS):
            print(f"Found tech trend: {trend['name']}")
            tech_trends.append(trend)

    trends_with_tweets = []
    print("Gathering sample tweets for tech trends...")
    for trend in tech_trends:
        # Use SAMPLE_TWEET_COUNT from settings
        sample_tweets = twitter_client.search_tweets(trend['name'], count=settings.SAMPLE_TWEET_COUNT)
        trends_with_tweets.append({
            'name': trend['name'],
            'tweet_volume': trend.get('tweet_volume'),
            'sample_tweets': sample_tweets
        })

    if not trends_with_tweets:
        print("No relevant tech trends found with sample tweets to post.")
        return

    print("Formatting blog content...")
    blog_title = f"Tech Trends on Twitter - {datetime.date.today().strftime('%B %d, %Y')}"
    blog_content = format_blog_content(trends_with_tweets)

    print("Posting to blog...")
    if blog_poster.post_blog_content(blog_title, blog_content, settings.DEFAULT_TAGS, settings.POST_STATUS):
        print("Blog post successfully created!")
    else:
        print("Failed to create blog post.")

if __name__ == "__main__":
    run_script()
