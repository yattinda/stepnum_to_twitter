#coding; utf-8

from requests_oauthlib import OAuth1Session
import json
import os
import random
from datetime import datetime, date, timedelta
import fitbit
import key.py

def puttweet():
    yestaday = datetime.strftime(datetime.today() - timedelta(days=1), '%Y-%m-%d')

    steps = fitbit_client.activities(date=yestaday)["summary"]["steps"]
    # print(steps)
    #
    # tweets = []
    # randomtweet = tweets[random.randrange(len(tweets))]
    # params = {"status": randomtweet}
    # req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)

if __name__ == '__main__':
    puttweet()
