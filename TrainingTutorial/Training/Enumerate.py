# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:15:14 2020

@author: OAdeoye
"""

data = ('Apple', 'Corn', 'Banana')
dico = {'Tunde': '1', 'Dotun': '2', 'Bode': '3', 'Ade': '4' }

print(type(data))
enum = enumerate(data, 1)
print(type(enum))

for i, e in enum:
    print(i, e)

for i, e in dico.items():
    print(i, e)