# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:14:04 2020

@author: OAdeoye
"""


from matplotlib import pyplot as plt
from DataSet import get_iris as dfa



df = dfa()
from pandas.tool.plotting import scatter_matrix
scatter_matrix(df)
plt.show()