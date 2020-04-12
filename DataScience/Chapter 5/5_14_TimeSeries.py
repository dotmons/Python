# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:19:34 2020

@author: Dotmons
"""


import statsmodels.api as sm
from matplotlib import pyplot as plt

import urllib.request
import pandas as pd
import numpy as np

dta = sm.datasets.co2.load_pandas().data
'''
#print(dta)
dta.plot()
plt.title("CO2 Levels")
plt.ylabel("Parts per millions")
plt.xlabel("Years of Sales")
plt.close
'''
# Plotting google stock graph on time series

URL = "https://query1.finance.yahoo.com/v8/finance/chart/GOOG?symbol=GOOG"

#with urllib.request.urlopen(URL) as ur:
#    dat = ur.read()
    
#open('foo.csv', 'w').write(str(dat))
#Make DataFrame, w timestamp as the index
df = pd.read_csv('foo.csv')
#df.index = df['Date'].astype('datetime64')
df['LogClose'] = np.log(df['close'])
df['Close'].plot()
plt.title("Normal Axis")
plt.show()