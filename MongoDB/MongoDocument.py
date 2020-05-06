# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:35:04 2020

@author: Dotmons
"""

from mongoengine import Document, StringField, connect, DateTimeField 
connect('mongoengine_test', host='localhost', port=27017)

import datetime

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)
    

post_1 = Post(title='Sample__ post',
              content='Engaging contents',
              author='Adeoye Oludotun')

post_1.save()
print(post_1.title)
post_1.title = "This is a unique documentation"
# To test the validation rule
post_1.author= "willa fjd lfkd afndj elkwnr jaheurh weuirhlekjfa hierheiourhewo"
post_1.save()
print(post_1.title)