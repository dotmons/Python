# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:04:48 2020

@author: Dotmons
"""


from matplotlib import pyplot as plt
from DataSet import get_iris as dfa

df = dfa()


df.plot(kind='hexbin', y='sepal length (cm)', x='sepal width (cm)', alpha=0.8
        )
plt.show()