import time

import tweepy
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
AT = keys['handle']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("on")
except:
    print("Error during authentication")


def gathering():
    tweetids = []
    for status in api.user_timeline(AT):
        # print(status.created_at)
        tweetids.append(str(status.created_at))  # time is in UTC
    print(tweetids)


if __name__ == "__main__":

    while True:
        gathering()

