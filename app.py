#coding; utf-8

from requests_oauthlib import OAuth1Session
import json
import os
import random
from datetime import datetime, date, timedelta
import fitbit
from key import fitbit_client

def puttweet():
    yestaday = datetime.strftime(datetime.today() - timedelta(days=1), '%Y-%m-%d')

    steps = fitbit_client.activities(date=yestaday)["summary"]["steps"]
    # print(steps)
if __name__ == '__main__':
    puttweet()
