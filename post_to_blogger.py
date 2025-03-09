import pickle
import os
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load credentials from token.pickle
TOKEN_FILE = "token.pickle"

if not os.path.exists(TOKEN_FILE):
    raise FileNotFoundError("Error: token.pickle file not found! Run authentication first.")

with open(TOKEN_FILE, "rb") as token:
    creds = pickle.load(token)

# Initialize B
