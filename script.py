import tweepy
from pymongo import MongoClient
import json
import requests
import unicodedata
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

class MyStreamListener(tweepy.StreamListener):

    print('func called')



    def on_data(self, data):
        # Decode JSON
        datajson = json.loads(data)
        client = pymongo.MongoClient(uri)
        db = client.upelect

        #client = MongoClient('localhost', 27017)
        #db = client.newtweetsDB

        #datajson = json.loads(data)
        db.upradesh.insert_one(datajson)

        #print datajson['text']

        print("inserted")

    def on_error(self, status):

        print status




myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track =
                ['#uttarpradesh','#UttarPradesh','#UttarPradeshelection',
                 'uttar pradesh election','@BJP4UP','@Samajwadi_Party',
                    '@OfficeOfRG', '@AmitShah','@yadavakhilesh','@BSP4India','#bsp']
               )
