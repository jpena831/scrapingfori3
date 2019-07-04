import tweepy
import csv
import pandas as pd
#Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data with csv writer
# This creates a csv into your local folder with the name below 'hashtags.csv'
csvFile = open('hashtags.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

#please add time from which you wish to collect tweets from hashtag
#in 'q' field or query field, add the hashtag you desire tweets from
for tweet in tweepy.Cursor(api.search,q="#pride",count=100,
                           lang="en",
                           since="2018-05-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
