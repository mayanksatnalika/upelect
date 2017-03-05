from bs4 import BeautifulSoup
import urllib2
import numpy as np
import pandas as pd
import time
from dateutil import parser
import matplotlib.pyplot as plt
import calendar
import datetime
import json
import pymongo
import pytz
url = 'http://www.ndtv.com/topic/elections-2017/'
now = datetime.datetime.now(pytz.timezone('Asia/Calcutta')) # you could pass `timezone` object here
yesterday = (now- datetime.timedelta(days=1)).date()
yst =  yesterday.strftime('%Y-%m-%d')
print 'yesterday date', yst
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),'html.parser')
print 'read ndtv news'
headline  = soup.findAll('p',{'class'  : 'header fbld'})
dates = soup.findAll('p',{'class':'list_dateline'})
header = zip(headline,dates)
headline_text = []
date_text = []
datestr = ''
for myitem in header:
    #if 'UP' not in myitem:
        #continue
    datestr = ''

    arr =  myitem[1].text.split('|', 2 )
    if len(arr) < 3 :
        continue
    for link in myitem[0].findAll('a'):
        #print link.text
        headline_text.append(link.text)

    #print arr[2]
    arr2 =  arr[2].split(' ', 4 )
    for term in arr2[2:]:
        datestr  = datestr +  ' ' +  str(term)
    #print datestr
    #print parser.parse(datestr).date()
    date_text.append( str( parser.parse(datestr).date() ))






print 'yesterday' ,yst
mydic = []
for i in range(0, len(date_text)):
   ch1 = 1
   ch2 = 1
   if 'UP' not in headline_text[i]:
       ch1 = 0
   if 'Uttar Pradesh' not in headline_text[i]:
       ch1 = 0
   if ch1 == 0 and ch2 == 0 :
       continue
   #print headline_text[i]
   #print date_text[i]
   #print '--'

   if  (parser.parse(date_text[i]) == parser.parse(yst)):
       print 'add'
       dicti = {}
       dicti['date'] = date_text[i]
       dicti['headline'] = headline_text[i]
       dicti['newsroom'] = 'NDTV News'
       mydic.append(dicti)

myjson = json.dumps(mydic)
c = json.loads(myjson)
print len(mydic)
uri = 'mongodb://root:root@ds139979.mlab.com:39979/upelect'
client = pymongo.MongoClient(uri)
db = client.upelect
news_raw = db['news_raw']
news_raw.insert_many(c)
print 'ndtv news done'
