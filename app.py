#coding; utf-8

from requests_oauthlib import OAuth1Session
import json
import os
import random
from datetime import datetime, date, timedelta

def puttweet():
    twitter = OAuth1Session(os.environ["TW_CONSUMER_KEY"],
              os.environ["TW_CONSUMER_SECRET"],
              os.environ["TW_ACCESS_TOKEN_KEY"],
              os.environ["TW_ACCESS_TOKEN_SECRET"])

    fitbit = OAuth1Session(os.environ["FB_CLIENT_ID"],
              os.environ["FB_CLIENT_SECRET"],
              os.environ["FB_ACCESS_TOKEN"],
              os.environ["FB_REFRESH_TOKEN"])

    yestaday = datetime.strftime(datetime.today() - timedelta(days=1), '%Y-%m-%d')
    tweets = []
    randomtweet = tweets[random.randrange(len(tweets))]
    params = {"status": randomtweet}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
