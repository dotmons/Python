# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 08:52:48 2020

@author: Dotmons
"""



from matplotlib import pyplot as plt
from DataSet import get_iris as dfa

df = dfa()

person_corr1 = df["sepal width (cm)"].corr(df["petal length (cm)"])
person_corr2 = df["sepal width (cm)"].corr(df["petal length (cm)"], method="pearson")

spearman_corr1 = df["sepal width (cm)"].corr(df["petal length (cm)"], method="spearman")
spearman_corr2 = df["sepal width (cm)"].corr(df["sepal length (cm)"], method="spearman")

print('person_corr1 : ' + str(person_corr1))
print('person_corr2 : ' + str(person_corr2))
print('spearman_corr1 : ' + str(spearman_corr1))
print('spearman_corr2 : ' + str(spearman_corr2))