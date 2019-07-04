import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
from urllib.request import urlopen

#please add your Twitter API credentials below
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

#this will simply print tweets in your terminal or prompt window based on your account profile timeline
public_tweets = api.home_timeline()
# for tweet in public_tweets:
#   print (tweet.text)
print (public_tweets[0])
