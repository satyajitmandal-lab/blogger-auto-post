import os
import requests

# Blogger API Scope
SCOPES = ["https://www.googleapis.com/auth/blogger"]

# Load credentials from GitHub Secrets
BLOG_ID = os.getenv("BLOG_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

# Set the minimum discount percentage required to post
MIN_DISCOUNT_PERCENT = 5  # Change this value as needed

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

def fetch_deals():
    """Simulated function to fetch product deals (replace this with real data)."""
    deals = [
        {"title": "🔥 Smartwatch", "old_price": 5000, "new_price": 3000, "link": "https://www.amazon.in/deal1"},
        {"title": "🎧 Wireless Earbuds", "old_price": 2000, "new_price": 1800, "link": "https://www.amazon.in/deal2"},
        {"title": "💻 Laptop", "old_price": 60000, "new_price": 42000, "link": "https://www.amazon.in/deal3"},
    ]
    return deals

def calculate_discount(old_price, new_price):
    """Calculates discount percentage."""
    discount = ((old_price - new_price) / old_price) * 100
    return round(discount, 2)

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
        print(f"✅ Post '{title}' successfully published!")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    deals = fetch_deals()
    for deal in deals:
        discount = calculate_discount(deal["old_price"], deal["new_price"])
        if discount >= MIN_DISCOUNT_PERCENT:
            title = f"🔥 {deal['title']} - {discount}% OFF!"
            content = f"<p>Original Price: <s>₹{deal['old_price']}</s><br>Discounted Price: ₹{deal['new_price']}<br><a href='{deal['link']}'>Buy Now</a></p>"
            post_to_blogger(title, content)
        else:
            print(f"❌ Skipping {deal['title']} - Only {discount}% OFF (Less than {MIN_DISCOUNT_PERCENT}%)")
