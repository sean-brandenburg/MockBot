import re
import config
import tweepy
import bot
from tweepy import OAuthHandler
from textblob import TextBlob
from mock import mockText

def main():
    # creating object of TwitterClient Class
    api = bot.TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(user = '@MockBot1', count = 1)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    print(tweets[0])

if __name__ == "__main__":
    # calling main function
    main()
