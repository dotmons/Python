# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:18:02 2020

@author: Dotmons
"""


from pymongo import MongoClient

#Initiating connection
#MongoClient('localhost', 27017)
startup_log = MongoClient('mongodb://localhost:27017')["local"].startup_log

#Getting output
output = startup_log.find({"hostname": "Dotmons-PC"})


for outs in output:
    print(outs, "\n\n\n\n\n")