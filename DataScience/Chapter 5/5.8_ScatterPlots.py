# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:55:25 2020

@author: OAdeoye
"""

from matplotlib import pyplot as plt
from DataSet import get_iris as dfa


df = dfa()

'''
df.plot(kind="scatter", x="sepal length (cm)", y="sepal width (cm)")
plt.title("Length vs Width")
plt.show()
'''
colors = ["r", "g", "b"]
markers = [".", "*", "^"]
fig, ax = plt.subplots(1, 1)


for i, spec in enumerate(df['species'].unique()):
    # parsing values matching spec into dff
    dff = df[df['species']==spec]
    #print(dff)
    dff.plot(kind="scatter", x="sepal width (cm)", y="sepal length (cm)",
    alpha=0.5, s=30*(i+1), ax=ax, color=colors[i], marker=markers[i], label=spec)
    #alpha is opaque.. density, s is boldness of the view
plt.legend()
plt.show()
