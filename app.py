#coding; utf-8

import json
from datetime import datetime, date, timedelta
import fitbit
from key import fitbit_client
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def plotstep():
    #print(fitbit_client.activities(date="2021-05-02"))
    type = int(input("数字を入力\n1:歩数\n2:消費したカロリー\n>>"))
    span = int(input("今日から何日前？\n>>"))
    week = []
    data = []

    for i in range(span):
        week.append(datetime.strftime(datetime.today() - timedelta(days=i), '%Y-%m-%d'))
    week.reverse()

    if type == 1:
        word = "steps"
    elif type == 2:
        word = "activityCalories"

    for j in range(span):
        data.append(fitbit_client.activities(date=week[j])["summary"][word])

    plt.plot(week, data, marker="o")
    plt.savefig('graph/{}{}-{}.png'.format(word, datetime.strftime(datetime.today(), '%Y-%m-%d'),span))

if __name__ == '__main__':
    plotstep()
