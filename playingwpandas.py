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


def delete_low(xdict):
    keys = []
    for i in  xdict:
        if xdict[i] <50:
            keys.append(i)
    return keys

def delete_keys(dictionary, words):
    for i in range(len(words)):
        if words[i] in dictionary:
            del dictionary[words[i]]
            
def create_plot(dic, string):
    save = string+ ".png"
    title = "Number of words repeated in troll tweets in " + string
    plt.figure(num=None, figsize=(10, 10), dpi=100, facecolor='w', edgecolor='k')
    index = np.arange(len((dic.keys())))
    plt.xlabel('Words')
    plt.ylabel("count")
    plt.xticks(index, list(dic.keys()), fontsize=10, rotation=40)
    plt.title(title)
    plt.bar(list(dic.keys()), dic.values(), color='b', edgecolor='k')
   
    plt.savefig(save, bbox_inches = 'tight')
    plt.show()

df  = pd.read_csv('word_count.csv')

df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)

adic={}

df2 = pd.DataFrame(df['2014-10-01':'2014-11-01'])
for index, row in df2.iterrows():
    for i, val in row.items():
        if math.isnan(val) !=True:
            if i in adic:
                adic[i] += val
            else:
                adic[i] = val
wlist = delete_low(adic)
delete_keys(adic, wlist)

oct_2014 = adic     
date = "Oct 2014"
#create_plot(adic, date)

print(oct_2014)

adic={}

df2 = pd.DataFrame(df['2014-11-01':'2014-12-01'])
for index, row in df2.iterrows():
    for i, val in row.items():
        if math.isnan(val) !=True:
            if i in adic:
                adic[i] += val
            else:
                adic[i] = val

wlist = delete_low(adic)
delete_keys(adic, wlist)

oct_2014 = adic     
date = "Nov 2014"
create_plot(adic, date)

