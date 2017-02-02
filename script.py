import tweepy
from pymongo import MongoClient
import json
import requests
import pymongo
import unicodedata
from sendEmail import msgme
import pandas as pd

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


        db.upradesh.insert_one(datajson)

        #print datajson['text']

        print("inserted")
        count +=1
        if count%5 == 0:
            msgstr = 'current count is '+ str(count)
            msgme(msgstr)

    def on_error(self, status):

        print status


myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track =
                ['#uttarpradesh','#UttarPradesh','#UttarPradeshelection',
                 'uttar pradesh election','@BJP4UP','@Samajwadi_Party',
                    '@OfficeOfRG', '@AmitShah','@yadavakhilesh','@BSP4India','#bsp']
               )
