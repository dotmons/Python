# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:40:20 2020

@author: Dotmons
"""

import pandas as pd

from matplotlib import pyplot as plt
import sklearn.datasets

def get_iris_data():
    ds = sklearn.datasets.load_iris()
    df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
    code_species_map = dict(zip(range(3), ds['target_names']))
    df['species'] = [code_species_map[c] for c in ds['target']]
    return df

col ='sepal length (cm)'
df = get_iris_data()['sepal length (cm)']
df['ind'] = pd.Series(df.index).apply(lambda i: i% 50)
df.pivot('ind', 'species')[col].plot(kind='box')
plt.show()  