# import packages:
import pandas as pd
import numpy as np
import re

df = pd.read_csv(r'C:\Users\navarrlx\OneDrive - Danone\Data Science in Python\String Functions in Python\NFL_Tweets4.txt', sep="|")

# create a function to clean tweets:
def clean_tweets(text):
    """
    function to clean tweets.
    1.) remove URL Links:
    2.) remove all non letters and lower case tweets:
    3.) replace retweets with empty string:
    4.) strip characters from left to right
    
    Arguments:
        text(object): tweet as a string data type to clean
    
    Returns:
        clean_tweets with no URL links, only non letters and all lower case text, replaces 'RT' with empty string and strips characters from left to right.
    """
    # remove URL links:
    text = re.sub(r"http\S+", "", text)
    # remove all non-letters and lower case tweets: replace 'rt' with empty string: strip characters from left to right
    text = re.sub('[^a-z\s]', '', text.lower()).replace('rt', '').strip()
    # return clean tweets:
    return text


# create new column called clean tweets: apply clean_tweet function:
df['clean_tweets'] = list(map(lambda x: clean_tweets(x), df['Tweet']))