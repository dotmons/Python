# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pymongo import MongoClient

posts = MongoClient().pymongo_test.posts

post_data_1 = {'title': 'Python and MongoDB',
             'content': 'PyMongo is fun, you guys',
             'author': 'Scott'
             }

post_data_2 = {'title': 'Virtual Environments',
             'content': 'Use virtual environments, you guys',
             'author': 'Scott'
             }

post_data_3 = {'title': 'Learning Python',
             'content': 'Learn Python, it is easy',
             'author': 'Bill'
             }


new_result = posts.insert_many([post_data_1, post_data_2, post_data_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))

#result = posts.insert_one(post_data)
#print('One post: {0}'.format(result.inserted_id))

bills_post = posts.find_one({'author': 'Scott'})
print(bills_post)