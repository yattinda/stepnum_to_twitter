#coding; utf-8

import json
from datetime import datetime, date, timedelta
import fitbit
from key import fitbit_client
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def plotstep():
    week = []
    step = []
    for i in range(6):
        week.append(datetime.strftime(datetime.today() - timedelta(days=i), '%Y-%m-%d'))

    for j in range(6):
        step.append(fitbit_client.activities(date=week[j])["summary"]["steps"])

    week.reverse()
    step.reverse()

    plt.plot(week, step)
    plt.savefig('graph/{}.png'.format(datetime.strftime(datetime.today(), '%Y-%m-%d')))

if __name__ == '__main__':
    plotstep()
