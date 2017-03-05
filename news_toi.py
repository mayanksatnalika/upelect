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
import time
from dateutil import parser
import matplotlib.pyplot as plt
import calendar
import datetime
import pytz
import pytz

url =  'http://timesofindia.indiatimes.com/elections/assembly-elections/uttar-pradesh/news'
now = datetime.datetime.now(pytz.timezone('Asia/Calcutta')) # you could pass `timezone` object here
yesterday = (now- datetime.timedelta(days=1)).date()
yst =  yesterday.strftime('%Y-%m-%d')
print 'yesterday date', yst
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),'html.parser')
headlines = soup.findAll('span',{'class':'w_tle'})
header = []
for head in headlines:
    myhead = head.findAll('a')
    header.append(myhead[0].text)


dates = []
dts = soup.findAll('span',{'class':'w_bylinec'})
for date in dts:
    dates.append(date.text)


for  i in range(0,len(dates)):
    dates[i] = str(parser.parse(dates[i][:-14]).date())
    #print str(dates[i])

print 'yesterday' ,yst
mydic = []
for i in range(0, len(dates)):

   #print header[i]
   #print dates[i]

   #dt = dates[i].split(',')
   #print dt[0]
   #print parser.parse(dates[i].split(,))

   #print '--'

   if  (parser.parse(dates[i]) == parser.parse(yst)):
       print 'add'
       dicti = {}
       dicti['date'] = dates[i]
       #dt[0] = dt[0].strftime('%Y-%m-%d')
       dicti['headline'] = header[i]
       dicti['newsroom'] = 'TimesOfIndia News'
       mydic.append(dicti)



print len(mydic)


myjson = json.dumps(mydic)
c = json.loads(myjson)
uri = 'mongodb://root:root@ds139979.mlab.com:39979/upelect'
client = pymongo.MongoClient(uri)
db = client.upelect
news_raw = db['news_raw']
news_raw.insert_many(c)
print 'toi news done'
