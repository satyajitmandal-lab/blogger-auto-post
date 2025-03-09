import time
import requests
import json
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load environment variables (GitHub Secrets)
BLOG_ID = "YOUR_BLOGGER_BLOG_ID"
CLIENT_ID = "YOUR_BLOGGER_CLIENT_ID"
CLIENT_SECRET = "YOUR_BLOGGER_CLIENT_SECRET"
REFRESH_TOKEN = "YOUR_BLOGGER_REFRESH_TOKEN"

# Function to get a new access token
def get_access_token():
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token",
    }
    response = requests.post(token_url, data=data)
    return response.json().get("access_token")

# Function to fetch latest deals (Example: Fake API for demonstration)
def fetch_deals():
    deals = [
        {
            "title": "Amazon Deal: iPhone 15 - 30% Off!",
            "link": "https://www.amazon.in/dp/EXAMPLE",
            "price": "₹69,999",
            "image": "https://via.placeholder.com/200"
        },
        {
            "title": "Flipkart Offer: Samsung Galaxy - 40% Off!",
            "link": "https://www.flipkart.com/dp/EXAMPLE",
            "price": "₹55,999",
            "image": "https://via.placeholder.com/200"
        }
    ]
    return deals

# Function to post a deal to Blogger
def post_deals_to_blogger():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    
    deals = fetch_deals()
    for deal in deals:
        post_data = {
            "kind": "blogger#post",
            "title": deal["title"],
            "content": f'<img src="{deal["image"]}"><br><a href="{deal["link"]}">Buy Now - {deal["price"]}</a>',
        }
        post_url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
        response = requests.post(post_url, headers=headers, data=json.dumps(post_data))
        print(f"Posted: {deal['title']} - Status: {response.status_code}")

# Run the script every 10 seconds
if __name__ == "__main__":
    while True:
        try:
            print("Fetching and posting new deals...")
            post_deals_to_blogger()
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(10)  # Wait 10 seconds before fetching again
