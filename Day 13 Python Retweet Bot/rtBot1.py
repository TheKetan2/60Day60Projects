
import tweepy
from time import sleep
#get your respective keys from twitter dev account and put it in below two functions.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='%23100DaysOfCode%20OR%20%23freeCodeCamp%20OR%20%23ReactJS%20OR%20%23Flutter%20OR%20%23io19').items(1000):
    try:
        tweet.retweet()
        sleep(20)
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
    except StopIteration:
        break