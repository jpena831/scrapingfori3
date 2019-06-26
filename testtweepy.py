import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
from urllib.request import urlopen

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
# for tweet in public_tweets:
#   print (tweet.text)
print (public_tweets[0])
