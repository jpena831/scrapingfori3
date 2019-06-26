import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
from urllib.request import urlopen


#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def redirect(url):
    page = urlopen(url)
    return page.geturl()


def get_all_tweets(screen_name):
        #Twitter only allows access to a users most recent 3240 tweets with this method

        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        #initialize a list to hold all the tweepy Tweets
        alltweets = []

        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = screen_name,count=1, tweet_mode='extended')

        #save most recent tweets
        alltweets.extend(new_tweets)

        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
                print ("getting tweets before %s" % (oldest))

                #all subsequent requests use the max_id param to prevent duplicates
                new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest, tweet_mode='extended')

                #save most recent tweets
                alltweets.extend(new_tweets)

                #update the id of the oldest tweet less one
                oldest = alltweets[-1].id - 1

                print ("...%s tweets downloaded so far" % (len(alltweets)))

        
        outtweets = [] #initialize master list to hold our ready tweets
        for tweet in alltweets:
                #not all tweets will have media url, so lets skip them
                try:
                        print (tweet.entities['hashtags'], tweet.entities['media'][0]['media_url'] )
                        
                except (NameError, KeyError):
                        #we dont want to have any entries without the media_url so lets do nothing
                        pass
                else:
                        #got media_url - means add it to the output
                        outtweets.append([tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8"), tweet.entities['hashtags'], tweet.entities['media'][0]['media_url']])

        #write the csv  
        with open('%s_tweets.csv' % screen_name, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(["id","created_at","text","hashtags","media_url","follower_count","likes"])
                writer.writerows(outtweets)

        pass


if __name__ == '__main__':
        #pass in the username of the account you want to download
        usernames = ["taylorswift13"]
        for x in usernames:
                  get_all_tweets("taylorswift13")

            #    get_all_tweets("JLo")
