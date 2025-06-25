# Trend settings
# Keywords used to filter Twitter trends to identify tech-related topics.
# Trends containing any of these keywords (case-insensitive) will be considered.
TECH_KEYWORDS = [
    'tech', 'ai', 'software', 'coding', 'developer',
    'startup', 'innovation', 'blockchain', 'cybersecurity', 'cloud',
    'programming', 'webdev', 'datascience', 'machinelearning', 'robotics',
    'gadgets', 'fintech', 'biotech', 'spacetech', 'edtech', 'greentech'
]

# Location ID for trends (Where On Earth ID - WOEID).
# WOEID 1 corresponds to Worldwide trends.
# You can find WOEIDs for specific locations online (e.g., searching "WOEID for New York" or "WOEID for Nigeria").
TREND_LOCATION = 1 # Default: Worldwide

# Blog post settings
# Default tags to be applied to the blog post when it's published.
DEFAULT_TAGS = ["tech", "trends", "twitter", "daily-trends"]

# Status of the blog post when it's published via webhook.
# Common options include "publish" (makes the post live) or "draft" (saves it as a draft).
POST_STATUS = "publish"  # Options: "publish", "draft"

# Number of sample tweets to fetch for each trending topic.
# This helps in providing context for each trend in the blog post.
SAMPLE_TWEET_COUNT = 3
