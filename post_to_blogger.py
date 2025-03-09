import pickle
from googleapiclient.discovery import build

# Load credentials from token.pickle
try:
    with open("token.pickle", "rb") as token_file:
        creds = pickle.load(token_file)
except FileNotFoundError:
    raise FileNotFoundError("Error: token.pickle file not found! Run authentication first.")

# Initialize Blogger API client
service = build("blogger", "v3", credentials=creds)

print("✅ Blogger API is ready to use!")
