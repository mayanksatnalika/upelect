import time
from dateutil import parser
#import matplotlib.pyplot as plt
import calendar
import pymongo
import datetime
import pytz
import json
import urllib2
import json
import tweepy
from pymongo import MongoClient
import json
import requests
import pymongo
import unicodedata
from sendEmail import msgme
import pandas as pd

now = datetime.datetime.now(pytz.timezone('Asia/Calcutta')) # you could pass `timezone` object here
now = now.date()
now =  now.strftime('%Y-%m-%d')
now = str(now)
print 'today is ',now
uri = 'mongodb://root:root@ds139979.mlab.com:39979/upelect'
consumer_key = "POA1eXAkYisz3kBRdcmjeBcha"
consumer_secret = "Ol97n9dfJcSiHvxUmPfRoR7QcLBMzuM5MdOrG36dBuNyT2EzNw"
access_token = "354671169-ROmqMvVamNyggX9hqNzlpqhTgc6AkCOpT6bsjodA"
access_secret = "RqlakpclhdjQzijYhaSfqqK0Yhzv3AZe6RdQggdms8sYn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

count  = 0
class MyStreamListener(tweepy.StreamListener):
    print('func called')



    def on_data(self, data):
        global count

        # Decode JSON
        datajson = json.loads(data)
        client = pymongo.MongoClient(uri)
        db = client.upelect
        #print datajson
        upnames =  ['up','UP','Uttar','Pradesh','uttar','pradesh','election','uttarpradesh',
                    '@uttarpradesh', '#uttarpradesh','#UttarPradesh','#UttarPradeshelection','uttar pradesh election']
        if 'text'  in datajson:
            if(any(wrd in  datajson['text'] for wrd in upnames) and datajson['lang'] == 'en'):

                dicti = {}
                dicti['tweet_text'] = datajson['text']
                dicti['date'] = now
                #print dicti
                myjson = json.dumps(dicti)
                c = json.loads(myjson)


                db.upradesh_tweets.insert_one(c)
                print("inserted")
                count +=1
                if count%25 == 0:
                    msgstr = 'current count is '+ str(count)
                    msgme(msgstr)



    def on_error(self, status):

        print status


myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#myStream.filter(track =
#                ['#uttarpradesh','#UttarPradesh','#UttarPradeshelection',
#                 'uttar pradesh election','@BJP4UP','@Samajwadi_Party', '@OfficeOfRG', '@AmitShah','@yadavakhilesh','@BSP4India','#bsp']
#               )

myStream.filter(track =
                ['@BJP4UP', '@narendramodi','@BJP4India',
                 '@yadavakhilesh', '@Samajwadi_Party',
                '@OfficeOfRG','@UPCC_Official','@INCIndia',
                 '@BSP4India','#bsp' ]
               )
