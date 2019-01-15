# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 14:05:09 2019

@author: Chaitu Konjeti
"""

import pytumblr
import time
from datetime import datetime
import csv
import re
import sys
import codecs


#reload(sys)
#sys.setdefaultencoding('utf-8')

#opens file and splits every word by the delimiter OR
filename = "C:\Users\Chaitu Konjeti\CDCTweets\Keywords.txt"


#final sorted list
keywords = []

#lists used during sorting
preKeywords = []
andList = []
andListNew = []

#sorts into AND and not AND sections
with open(filename, 'r') as f:
    for line in f:
        for word in re.split('\(\(|\)\)',line):
            if str(word).find('AND') > 0:
                andList.append(str(word))
            elif word != ' OR ':
                preKeywords.append(word)
                
#sorts the non AND section and appends the final product to keywords
for x in preKeywords:
    for x in (x.split(' OR ')):
        if x != '':            
            keywords.append(str(x.replace("\"","")))
            
#sorts the AND section into groups            
for x in andList:
    for y in x.split(' AND '):
        andListNew.append(y.replace("(","").replace(")","").replace("\"","").split(" OR "))
     
#sorts the AND section groups and appends the final product to keywords
x = 0
while x < len(andListNew):
    if x % 2 == 0:
        for z in andListNew[x]:
            for y in range(len(andListNew[x + 1])):
                keywords.append((z + ' ' + andListNew[x + 1][y]))
    x += 1             


#Creates tumblr client
client = pytumblr.TumblrRestClient(
        'l3FxwH8VFOe3hFACwd5bXcM2A69eN40KQGYrK6MNMUjzfu07Ye',
        'q1u63mbjlfpw3KfOvWodNKXH9fS7owjezX0Nm5LgtBr0APTJUk'    
        )
posts = []
max_calls = 5

last_timestamp = int(time.time())
for _ in range(max_calls):
    posts.extend(client.tagged('goals', limit=20, filter='text', before=last_timestamp))
    last_timestamp = posts[-1]['timestamp']


# massage the data into a consistent dictionary
content_key_map = {'text': 'body', 'photo': 'caption', 'quote': 'text', 'link': 'description', 'chat': 'body',
           'audio': 'caption', 'video': 'caption', 'answer': 'answer'}
output_list = []
add_this_item = False
or_tags = ['food', 'fit', 'weight', 'health', 'life']

for p in posts:
    print(p)
    print('--------------------------------------------')
    for t in or_tags:
        
        if t in p['tags']:
            
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



outputFileName = "output_got.csv"
outputFile = codecs.open(outputFileName, "w+", "utf-8")
dataWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


i = 0
for p in output_list:
    row = [repr(s).encode("utf-8") for s in [keywords[i], p['content'],p['date'],p['time'],p['tags'],p['blog_name']]]
    dataWriter.writerow(row)
    i += 0
        
        


    
