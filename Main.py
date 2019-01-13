# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 14:05:09 2019

@author: Chaitu Konjeti
"""

import pytumblr
import os
import time
from datetime import datetime
import csv
import re


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
        
        
        
        )