import requests
import os
from datetime import datetime

BLOG_ID = os.getenv("BLOG_ID")  # Replace with actual blog ID
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

def get_access_token():
    """Fetches access token using the refresh token."""
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token",
    }
    response = requests.post(token_url, data=payload)
    return response.json().get("access_token")

def post_to_blogger():
    """Creates a test post to Blogger and publishes it immediately."""
    access_token = get_access_token()
    if not access_token:
        print("❌ Error: Failed to get access token!")
        return

    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"

    # Get current timestamp in RFC3339 format (Blogger API format)
    now = datetime.utcnow().isoformat() + "Z"

    data = {
        "kind": "blogger#post",
        "title": "Test Post",
        "content": "<p>This is a test post!</p>",
        "status": "LIVE",  # Force publish immediately
        "published": now   # Set current time for immediate publishing
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("✅ Successfully posted to Blogger!")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

# Run the test
post_to_blogger()
