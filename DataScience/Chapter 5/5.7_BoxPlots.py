# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 07:36:53 2020

@author: OAdeoye
"""

import pandas as pd
from matplotlib import pyplot as plt
import sklearn.datasets

def get_iris():
    ds = sklearn.datasets.load_iris()    
    df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
    code_species_map = dict(zip(range(3), ds['target_names']))
    #print(code_species_map)
    df['species'] = [code_species_map[c] for c in ds['target']]   
    return df

data = get_iris()
print("Header: "+str(list(data)))
print("Species: "+((data['species']).unique()))
col = 'sepal length (cm)'

data['ind'] = pd.Series(data.index).apply(lambda i: i%50)
#print(data['ind'])
data.pivot('ind', 'species')[col].plot(kind='box')
plt.show()
