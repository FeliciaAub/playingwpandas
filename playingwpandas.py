# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:02:40 2019

@author: Felicia
#First Two and a half years had no interesting data (no words commonly used on a given day)
Starts october 2014
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import math
from calendar import monthrange
from heapq import nlargest


def delete_keys(dictionary, words):
    for i in range(len(words)):
        if words[i] in dictionary:
            del dictionary[words[i]]
            
def create_plot(dic, date, enddate):
    mon = date.strftime("%B")
    yr = date.strftime("%Y")
    smon = date.strftime("%m")
    daystart = date.strftime("%d")
    endday = enddate.strftime("%d")
    save = "Graphs/"+ yr +"-" + smon + ".png"
    title = "Frequency of word usage in " + mon + " " + yr
    plt.figure(num=None, figsize=(15, 15), dpi=100, facecolor='w', edgecolor='k')
    index = np.arange(len(dic.keys()))
    plt.xlabel('Count')
    plt.ylabel("Words")
    plt.yticks(index, list(dic.keys()), fontsize=10)
    plt.title(title)
    plt.barh(list(dic.keys()), dic.values(), color='b', edgecolor='k')
    plt.savefig(save, bbox_inches = 'tight')

 
def normalize(d):
    k = nlargest(50, d, key=d.get)
    mlist = get_low(d, k)
    delete_keys(d, mlist)
    return d
     
          
def get_low(d, l):
    alist = []
    for i in d:
         if i not in l:
             alist.append(i)
    return alist
    
def current_dataframe(df, dtobj1, dtobj2):
    adic={}
    datestr = dtobj1.strftime("%Y-%m-%d")
    dateend = dtobj2.strftime("%Y-%m-%d")
    df2 = pd.DataFrame(df[datestr:dateend])
    for index, row in df2.iterrows():
        for i, val in row.items():
            if math.isnan(val) !=True:
                if i in adic:
                    adic[i] += val
                else:
                    adic[i] = val

    if len(adic) > 50:
        adic = normalize(adic)
    if len(adic) > 1:
        create_plot(adic, dtobj1, dtobj2)



df  = pd.read_csv('word_count.csv')
df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)



for i in range(2014, 2019):
    for j in range(1, 13):
        x, y = monthrange(i, j)
        dateobjstart = datetime(i, j, 1)
        dateobjend = datetime(i, j, y)
        current_dataframe(df, dateobjstart, dateobjend)
