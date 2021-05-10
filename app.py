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
    week = []
    for i in range(6):
        week.append(datetime.strftime(datetime.today() - timedelta(days=i), '%Y-%m-%d'))
    week.reverse()

    if type == 1:
        word = "steps"
    elif type == 2:
        word = "activityCalories"

    data = []

    for j in range(6):
        data.append(fitbit_client.activities(date=week[j])["summary"][word])

    plt.plot(week, data)
    plt.savefig('graph/{}{}.png'.format(word, datetime.strftime(datetime.today(), '%Y-%m-%d')))

if __name__ == '__main__':
    plotstep()
