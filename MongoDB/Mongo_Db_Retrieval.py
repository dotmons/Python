# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:02:45 2020

@author: Dotmons
"""


from pymongo import MongoClient

posts = MongoClient().pymongo_test.posts


#Used to find just one object
result = posts.find_one({'author': 'Scott'})
#print(result)

#Used to find multiple objects
results = posts.find({'author': 'Scott'})

for res in results:
    print(res)