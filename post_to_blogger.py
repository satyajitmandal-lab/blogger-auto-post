import os
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load credentials from GitHub Secrets
creds = Credentials.from_authorized_user_info({
    "client_id": os.getenv("SECRET_BLOGGER_CLIENT_ID"),
    "client_secret": os.getenv("SECRET_BLOGGER_CLIENT_SECRET"),
    "refresh_token": os.getenv("SECRET_BLOGGER_REFRESH_TOKEN"),
    "token_uri": "https://oauth2.googleapis.com/token"
})

# Initialize Blogger API
service = build("blogger", "v3", credentials=creds)

# Fetch Deals from Amazon/Flipkart (Mock Data Here)
deals = [
    {
        "title": "🔥 iPhone 15 - 20% Off!",
        "content": "<b>Deal Price: ₹60,000</b><br>Check it <a href='https://www.amazon.in'>here</a>",
    },
    {
        "title": "🎧 Boat Headphones - 50% Discount!",
        "content": "<b>Deal Price: ₹999</b><br>Grab it <a href='https://www.flipkart.com'>here</a>",
    }
]

# Post Deals to Blogger
for deal in deals:
    post = {
        "kind": "blogger#post",
        "title": deal["title"],
        "content": deal["content"]
    }
    response = service.posts().insert(blogId=os.getenv("SECRET_BLOGGER_BLOG_ID"), body=post).execute()
    print(f"Posted: {response['title']} - {response['url']}")
