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

fig, ax = plt.subplots(2,1)

xdata = []
ydata = []
#ydata1 = []
#ydata2 = []


def animate_1(i):
    df, err = ek.get_data(
        instruments = ['10TBU1'],
        fields = [
            'PRIMACT_1'
        ]
    )

    xdata.append(i)
    ydata.append(df['PRIMACT_1'].iloc[0])
    
    ax[0].cla()
    
    ax[0].plot(xdata, ydata)
    ax[0].set_ylabel('Bitcoin Price 1')
    #ax[0].legend(loc="upper right")
    #ax[0].tight_layout()
    

ani_1 = FuncAnimation(plt.gcf(), animate_1, interval=0.001)

def animate_2(i):
    #df, err = ek.get_data(
    #    instruments = ['BTC='],
    #    fields = ['PRIMACT_1']
    #)

    #xdata.append(i)
    #ydata.append(df['PRIMACT_1'].iloc[0])

    ax[1].cla()

    #ax[1].set_xlim(left=max(0, i-50), right=i+1.4)
    ax[1].set_xlim(left=max(0, i-100), right=i+1.6)
    print("Left: ", max(0, i-10))
    print("Right: ", i+10)

    ax[1].plot(xdata, ydata)
    ax[1].set_ylabel("Bitcoin Price 3")

ani_2 = FuncAnimation(plt.gcf(), animate_2, interval=0.001)


fig.tight_layout()
plt.show()





#import eikon as ek
#ek.set_app_key('0a7c178594324f469445faaea4e3507e4a53d5e1')


#import time
#import datetime
#import numpy as np
#import pandas as pd
#from itertools import count
#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation

##plt.style.use('dark_background')
#plt.style.use('bmh')

#index = count()

#x_vals= []
#y_vals = []

#fig = plt.figure()
#ax = fig.add_subplot(111)

#def animate(i):
#    df, err = ek.get_data(
#        instruments = ['BTC='],
#        fields = ['PRIMACT_1']
#    )

#    x_vals.append(next(index))
#    y_vals.append(df['PRIMACT_1'].iloc[0])
   
#    plt.cla()

#    ax.set_xlim(left=max(0, i-10), right=i+10)
   
#    plt.plot(x_vals, y_vals, label="Bid of Bitcoin")
   
#    plt.tight_layout()
   

#ani = FuncAnimation(plt.gcf(), animate, interval=0.001)

#plt.show()
