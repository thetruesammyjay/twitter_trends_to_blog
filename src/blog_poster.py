import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class BlogPoster:
    def __init__(self):
        self.webhook_url = os.getenv("BLOG_WEBHOOK_URL")
        if not self.webhook_url:
            raise ValueError("BLOG_WEBHOOK_URL not found in .env file.")

    def post_blog_content(self, title, content, tags=None, status="publish"):
        """
        Posts blog content to the configured webhook URL.
        """
        if tags is None:
            tags = []

        payload = {
            "title": title,
            "content": content,
            "tags": tags,
            "status": status
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)
            response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
            print(f"Successfully posted blog content. Status Code: {response.status_code}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error posting blog content: {e}")
            return False

if __name__ == "__main__":
    poster = BlogPoster()
    test_title = "Test Blog Post from Script"
    test_content = "<p>This is a <strong>test blog post</strong> generated from the <code>blog_poster.py</code> script.</p><p>It demonstrates how to post content via webhook.</p>"
    test_tags = ["test", "script", "webhook"]

    print("Attempting to post a test blog entry...")
    if poster.post_blog_content(test_title, test_content, test_tags, "draft"):
        print("Test blog post sent successfully (check your webhook receiver).")
    else:
        print("Failed to send test blog post.")