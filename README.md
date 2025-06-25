# Twitter Trends to Blog Webhook

A Python script that scrapes trending tech stories from Twitter and posts them to a company blog via webhooks.

## Features

* Fetches trending tech topics from Twitter
* Gathers sample tweets for each trend
* Formats content for blog posts
* Posts to your blog via webhook
* Scheduled to run daily

## Prerequisites

* Python 3.6+
* Twitter Developer Account
* Blog platform with webhook support

## Installation

1. Clone the repository:

```bash
git clone https://github.com/thetruesammyjay/twitter_trends_to_blog.git
cd twitter_trends_to_blog
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your credentials:

```env
TWITTER_CONSUMER_KEY=your_key
TWITTER_CONSUMER_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_TOKEN_SECRET=your_token_secret
BLOG_WEBHOOK_URL=your_webhook_url
```

## Usage

Run the script manually:

```bash
python src/main.py
```

For scheduled execution, set up a cron job or task scheduler to run daily.

## Configuration

Modify the following in `config/settings.py`:
* Tech keywords to search for
* Location for trends (default is worldwide)
* Number of sample tweets to fetch per trend
* Blog post default tags and status (`"publish"` or `"draft"`)

## Webhook Setup

Your blog platform needs to accept POST requests with JSON data in this format:

```json
{
  "title": "Tech Trends on Twitter - [Date]",
  "content": "[HTML formatted content]",
  "tags": ["tech", "trends"],
  "status": "publish"
}
```

## Contributing

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

MIT
