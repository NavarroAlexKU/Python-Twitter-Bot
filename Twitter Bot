from tweepy import OAuthHandler
from tweepy import API
import tweepy
import time
import numpy as np
import sys
from dateutil import parser
import pandas as pd
from tweepy.streaming import Stream
import json
import os
import logging

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
bear_token = ''

# authentication:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

# create an api instant:
api = tweepy.API(auth)

# create class:
class Listener(tweepy.Stream):
    # create empty list to store tweets:
    tweet = []

    # set limit 100000
    limit = 100000

    # create on_status method:
    def on_status(self, status):
        # append tweets:
        self.tweet.append(status)

        if len(self.tweet) == self.limit:
            # disconnect:
            self.disconnect()
    
    # create on_error method:
    def on_error(self, status):
        print(status)

stream_tweet = Listener(
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET
)

# create key words:
key_words = [
    '#NFL',
    '#Chiefs',
    '#Jets',
    '#Browns',
    '#Cowboys',
    '#Broncos',
    '#Bears',
    '#Patriots',
    '#Dolphins',
    '#Chargers',
    '#Raiders',
    '#Bengals',
    '#Ravens',
    '#Giants',
    '#Jaguars',
    '#Bills',
    '#Cardinals',
    '#Seahawks',
    '#Packers',
    '#Lions',
    '#Colts',
    '#49ers',
    '#Rams',
    '#Texans',
    '#Eagles',
    '#Falcons',
    '#Titans',
    '#Panthers',
    '#Commanders',
    '#Steelers',
    '#Saints',
    '#Buccaneers',
    '#Vikings'


]

# create stream:
stream_tweet.filter(track = key_words)


# create columns:
columns = ['User', 'Tweet']

# create empty list to store data:
data = []

# extract full tweets from tweets in stream_tweet:
for tweet in stream_tweet.tweets:
    # if full tweet:
    if not tweet.truncated:
        # append tweets to data:
        data.append([tweet.user.screen_name, tweet.text])
        # if not full tweet: extract extended tweet instead:
    else:
        data.append([tweet.user.screen_name, tweet.extended_tweet['full_text']])

# create dataframe:
df = pd.DataFrame(data, columns=columns)

# save data to txt file:
df.to_csv('NFL Tweets.txt', sep = '|')