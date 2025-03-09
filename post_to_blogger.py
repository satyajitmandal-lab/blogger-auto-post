import pickle
import requests

# Load authentication token
with open("token.pickle", "rb") as token_file:
    credentials = pickle.load(token_file)

# Get access token from credentials
access_token = credentials.token

# Replace with your Blogger Blog ID
BLOG_ID = "YOUR_BLOGGER_BLOG_ID"

def post_to_blogger(title, content):
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "kind": "blogger#post",
        "title": title,
        "content": content
    }
    
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"✅ Posted: {title}")
    else:
        print(f"❌ Failed to post: {response.text}")

if __name__ == "__main__":
    from fetch_deals import fetch_amazon_deals, fetch_flipkart_deals
    
    amazon_deals = fetch_amazon_deals()
    flipkart_deals = fetch_flipkart_deals()

    for deal in amazon_deals + flipkart_deals:
        post_to_blogger(deal["title"], f'<a href="{deal["link"]}">Check Deal</a>')
