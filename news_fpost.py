from bs4 import BeautifulSoup
import pandas as pd
import pymongo
import urllib2
import time
from dateutil import parser
import matplotlib.pyplot as plt
import calendar
import pymongo
import datetime
import pytz
import json

url = 'http://www.firstpost.com/tag/uttar-pradesh-assembly-election-2017'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'html.parser')
dates = soup.findAll('p',{'class' : 'text-muted'})
head = soup.findAll('p',{'class' : 'list-title'})
from dateutil import parser

mydate = [(parser.parse(t.text)) for t in dates]
now = datetime.datetime.now(pytz.timezone('Asia/Calcutta')) # you could pass `timezone` object here
yesterday = (now- datetime.timedelta(days=1)).date()
yst =  yesterday.strftime('%Y-%m-%d')

mydic= []
for i in range(0,len(mydate)):
    parser.parse(yst)
    if  (parser.parse( str(mydate[i].date())) == parser.parse(yst)):
        print 'add'

        #row = {'date' : dates_final[i], 'headline': headline[i],'newsroom' : 'Zee news'}
        dicti = {}
        dicti['date'] = str(mydate[i].date())
        dicti['headline'] = head[i].text
        dicti['newsroom'] = 'FirstPost news'
        mydic.append(dicti)


myjson = json.dumps(mydic)
c = json.loads(myjson)
print len(mydic)

uri = 'mongodb://root:root@ds139979.mlab.com:39979/upelect'
client = pymongo.MongoClient(uri)
db = client.upelect
news_raw = db['news_raw']
news_raw.insert_many(c)
print 'firstpost done'
