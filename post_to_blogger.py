import os
import pickle
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Blogger API Scope
SCOPES = ["https://www.googleapis.com/auth/blogger"]

# Load credentials from secrets
BLOG_ID = os.getenv("BLOG_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

def get_access_token():
    """Fetches a new access token using the refresh token."""
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token",
    }
    response = requests.post(token_url, data=payload)
    return response.json().get("access_token")

def post_to_blogger(title, content):
    """Posts a new deal to Blogger."""
    access_token = get_access_token()
    if not access_token:
        print("❌ Error: Failed to get access token!")
        return

    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    data = {"kind": "blogger#post", "title": title, "content": content}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("✅ Post successfully published!")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example Deal Post
    title = "🔥 Amazing Deal: 50% OFF on Smartwatch!"
    content = "<p>Get 50% off on the latest Smartwatch. Hurry, limited time offer! <a href='https://www.amazon.in/deal-link'>Buy Now</a></p>"

    post_to_blogger(title, content)
