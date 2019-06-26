import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
from urllib.request import urlopen

auth = tweepy.OAuthHandler("YwjEECDNFjGNc44JwGz3d83YM", "rsSUna8KABra0ZeJqnmarMJ4zM5eVNZHt4qQsbAcc2wlckIFe2")
auth.set_access_token("1120468466-I1yMKwzeqtHiGwsxwNSkhL1lM0iA49NwOvArQGc", "R4tNgI2EdOpFH1PT7OpV6cUh9nksKCfnKaDwWao4V1PxB")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
# for tweet in public_tweets:
#   print (tweet.text)
print (public_tweets[0])