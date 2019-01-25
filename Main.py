# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 14:05:09 2019

@author: Chaitu Konjeti
"""

import pytumblr
import time
from datetime import datetime
import csv
import codecs
import functions as f
import re


#opens file and splits every word by the delimiter OR
filename = "C:\Users\Chaitu Konjeti\CDCTumblr\Keywords.txt"

keywords = f.sortKeyword(filename)
#keywords = [s.replace('"', '') for s in keywords]
#keywords = [repr(s).encode('utf-8').replace('\\x92',"'") for s in keywords]
#keywords = [s.replace('"', '') for s in keywords]
#keywords = [s.encode('utf-8').replace('\\x92',"'") for s in keywords]
#print(keywords)
#keywords = [repr(s) for s in keywords]

#Creates tumblr client
client = pytumblr.TumblrRestClient(
        'l3FxwH8VFOe3hFACwd5bXcM2A69eN40KQGYrK6MNMUjzfu07Ye', 
        'q1u63mbjlfpw3KfOvWodNKXH9fS7owjezX0Nm5LgtBr0APTJUk'    
        )
posts = []
max_calls = 1
i = 0
last_timestamp = int(time.time())
for i in range(5):
    for _ in range(max_calls):
        #print((keywords[i]).encode('utf-8').replace('\\x92',"'"))
        posts.extend(client.tagged(keywords[i], limit=20, filter='text', before=last_timestamp))
        #posts = [repr(s).encode('utf-8').replace('\\x92',"'") for s in posts]
        last_timestamp = posts[-1]['timestamp']

#print(posts)

# massage the data into a consistent dictionary
content_key_map = {'text': 'body', 'photo': 'caption', 'quote': 'text', 'link': 'description', 'chat': 'body',
           'audio': 'caption', 'video': 'caption', 'answer': 'answer'}
output_list = []
add_this_item = False
#print(keywords)


for p in posts:
#    print(p)
    #print('--------------------------------------------')
#    print(repr(p[content_key_map[p['type']]])).encode('utf-8')
#    print(p['tags'])
#    print('--------------------------------------------')
    for t in keywords:
        #print(t)
        
        #("--------------------------------------")
        if t in (repr(p[content_key_map[p['type']]])):
            output_list.append(
                {
                    'content': p[content_key_map[p['type']]],
                    'date': datetime.utcfromtimestamp(int(p['timestamp'])).strftime('%Y-%m-%d'),
                    'time': datetime.utcfromtimestamp(int(p['timestamp'])).strftime('%H:%M:%S'),
                    'tags': p['tags'],
                    'id': p['id'],
                    'blog_name': p['blog_name'],
                    'post_url': p['post_url'],
                    'type': p['type']
                }
                
            )
            break
#print('-------------------------------------------------------')
#print(output_list)

outputFileName = "Tumblr_BlogPosts.csv"
outputFile = codecs.open(outputFileName, "w+", "utf-8")
dataWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


i = 0
for p in output_list:
    row = [repr(s).encode("utf-8") for s in [p['content'],p['date'],p['time'],p['tags'],p['blog_name']]]
    dataWriter.writerow(row)
    i += 0
        
        


    
