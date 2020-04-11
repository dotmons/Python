# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 03:49:08 2020

@author: Dotmons
"""


from DataSet import get_Boston as ds
from matplotlib import pyplot as plt
import pandas as pd


bs = ds()
print('Header content in list: ' + str (list(bs)))
print('Type of Array:: ' + str(type(bs['data'])))
print(bs['feature_names'])
#print(bs['data'])
df = pd.DataFrame(data=bs.data, columns=bs.feature_names)
print('Dataframe list: '+str(list(df)))
df['MEDV'] = bs.target



df.plot(x='CRIM', y='MEDV', kind='scatter')
plt.title('Crime rate on normal axis')
plt.show()
