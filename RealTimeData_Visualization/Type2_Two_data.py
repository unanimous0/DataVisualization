# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:58:11 2021

@author: USER
"""


import eikon as ek
ek.set_app_key('0a7c178594324f469445faaea4e3507e4a53d5e1')


import time
import datetime
import numpy as np
import pandas as pd
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#plt.style.use('dark_background')
plt.style.use('bmh')

#fig = plt.figure()
#ax1 = fig.add_subplot(2,1,1)
#ax2 = fig.add_subplot(2,1,2)

fig, ax = plt.subplots(3,1)

index1 = count()
index2 = count()

#xdata = []
#ydata = []
xdata1 = []
xdata2 = []
ydata1 = []
ydata2 = []


def animate_1(i):
    df, err = ek.get_data(
        instruments = ['10TBU1'],
        fields = [
            'IRGFID'
        ]
    )

    xdata1.append(next(index1))
    ydata1.append(df['IRGFID'].iloc[0])
    
    ax[0].cla()
    
    ax[0].plot(xdata1, ydata1)
    ax[0].set_ylabel('매수 호가 잔량')
    #ax[0].legend(loc="upper right")
    #ax[0].tight_layout()
    

ani_1 = FuncAnimation(plt.gcf(), animate_1, interval=0.001)


def animate_2(i):
    df, err = ek.get_data(
        instruments = ['10TBU1'],
        fields = [
            'IRGVAL'
        ]
    )

    xdata2.append(next(index2))
    ydata2.append(df['IRGVAL'].iloc[0])

    #ax[1].set_xlim(left=max(0, j-100), right=j+100)
    #j += 1

    ax[1].cla()

    ax[1].plot(xdata2, ydata2)
    ax[1].set_ylabel("매도 호가 잔량")

ani_2 = FuncAnimation(plt.gcf(), animate_2, interval=0.001)


def animate_3(i):
    
    """
        3번째 순매수잔량은 아래와 같은 에러 뜨면서 중간에 꺼짐 (1, 2번은 정상 작동)
        2021-08-06 10:52:36,936 P[23260] [MainThread 4864] Backend error. 400 Bad Request
        2021-08-06 10:52:36,937 P[23260] [MainThread 4864] HTTP request failed: EikonError-Backend error. 400 Bad Request
    """

    ax[2].cla()

    ax[2].plot(xdata2, [x-y for x,y in zip(ydata1, ydata2)])
    ax[2].set_ylabel("매도 호가 잔량")

ani_3 = FuncAnimation(plt.gcf(), animate_3, interval=0.001)



fig.tight_layout()
plt.show()
