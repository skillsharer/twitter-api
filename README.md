# Python Tweeting Script using Tweepy

This script allows you to send a tweet using the new X API (formerly known as Twitter) with Python and Tweepy. Detailed description can be found [here](https://skillsharer.medium.com/your-quickstart-guide-to-tweeting-with-python-be3586bda32e).

## Prerequisites

1. Python 3.x installed.
2. A .env file containing your X API keys.

## Setup & Installation

1. Clone this repository:
 ```bash
 git clone git@github.com:skillsharer/twitter-api.git
 ```
2. Navigate to the directory:
 ```bash
 cd twitter-api
 ```

3. Install the required packages:
  ```bash
  pip install tweepy python-dotenv
  ```

4. Set up your .env file in the root of the directory with the following format:
  ```bash
  CONSUMER_KEY=YOUR_CONSUMER_KEY
  CONSUMER_SECRET=YOUR_CONSUMER_SECRET
  ACCESS_TOKEN=YOUR_ACCESS_TOKEN
  ACCESS_TOKEN_SECRET=YOUR_ACCESS_TOKEN_SECRET
  BEARER_TOKEN=YOUR_BEARER_TOKEN
  ```

## Usage:

Run the script using:
```bash
python tweet.py
```

The script will then send a "Hello, World!" tweet using the provided API keys.



