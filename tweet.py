import tweepy
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

CONSUMER_KEY=os.getenv("CONSUMER_KEY")
CONSUMER_SECRET=os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET=os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN=os.getenv("BEARER_TOKEN")

# V2 APi Twitter Authentication

client = tweepy.Client(
   BEARER_TOKEN,
   CONSUMER_KEY,
   CONSUMER_SECRET,
   ACCESS_TOKEN,
   ACCESS_TOKEN_SECRET,
   wait_on_rate_limit=True
)

client.create_tweet(text = "Hello, World!")