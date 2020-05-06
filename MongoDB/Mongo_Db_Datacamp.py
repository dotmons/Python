# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:04:19 2020

@author: Dotmons
"""


from pymongo import MongoClient

record = MongoClient('mongodb://localhost:27017')["datacampdb"].articles

article = {'author': 'Adeoye Oludotun',
           'about': 'Introduction to MongoDB and Python',
           'tags': ['mongodb', 'python', 'nosql']}

#result = record.insert_one(article)
#print("The output value is : {}".format(result.inserted_id))

#
print("Database record: {0}".format(record.list_collection_names))


article_1 = {'author': 'Adeoye Oludotun',
           'about': 'Introduction to MongoDB and Python',
           'tags': ['mongodb', 'python', 'nosql']}

article_2 = {'author': 'Adeoye Oluwabukola',
           'about': 'Introduction to Security',
           'tags': ['A++', 'Security Plus', 'Linux', 'Windows Application']}

result_many = record.insert_many([article_1, article_2])
print("Output id for data entry: {}".format(result_many))