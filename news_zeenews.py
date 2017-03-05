from bs4 import BeautifulSoup
import urllib2
import numpy as np
import pymongo
import pandas as pd
import time
from dateutil import parser
import matplotlib.pyplot as plt
import calendar
import datetime
import pytz

url = 'http://zeenews.india.com/uttar-pradesh'
now = datetime.datetime.now(pytz.timezone('Asia/Calcutta')) # you could pass `timezone` object here
yesterday = (now- datetime.timedelta(days=1)).date()
yst =  yesterday.strftime('%Y-%m-%d')
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),'html.parser')
spans = soup.findAll('span', {'class' : 'lead-health-ab'})
headline = []
urllink = []
for span in spans:
    links =  span.findAll('a')
    for link in links :
        urllink.append(link['href'])
        headline.append(link.text)
len(headline)
finallink  = ['http://zeenews.india.com/' + str(mylink) for mylink in urllink]
cnt = 0
dates = []
for link in finallink:
    #print link
    page = urllib2.urlopen(link)
    soup = BeautifulSoup(page.read(),'html.parser')
    date = soup.find('div',{'class':'writer'})
    dates.append(date.text)
    #time.sleep(3)
    cnt+=1
    if cnt > 16 :
        break
    print cnt

dates_final = []
mydates = [dt.replace('\n','') for dt in dates]
#print mydates
dates_final = [str(parser.parse(dt[-22:-8]).date()) for dt in mydates]


newsroom = ['zeenews']*len(dates_final)
#json_string = json.dumps(row)
import json
mydic= []
for i in range(0,len(dates_final)):
    print i
    print str(dates_final[i])
    if  (parser.parse( dates_final[i]) == parser.parse(yst)):
    #if  ( 'March' in str(dates_final[i]) == True  ):
        print 'add'

        #row = {'date' : dates_final[i], 'headline': headline[i],'newsroom' : 'Zee news'}
        dicti = {}
        dicti['date'] = dates_final[i]
        dicti['headline'] = headline[i]
        dicti['newsroom'] = 'Zee news'
        mydic.append(dicti)

myjson = json.dumps(mydic)
c = json.loads(myjson)
print len(mydic)
uri = 'mongodb://root:root@ds139979.mlab.com:39979/upelect'
client = pymongo.MongoClient(uri)
db = client.upelect
news_raw = db['news_raw']
news_raw.insert_many(c)
print 'zee news done'
