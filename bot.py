import re
import tweepy
import config
from tweepy import OAuthHandler
from textblob import TextBlob
from mock import mockText




class TwitterClient(object):
    def __init__(self):
        # keys and tokens from the Twitter Dev Console
        consumer_key = config.twitConsumerKey
        consumer_secret = config.twitConsumerSecret
        access_token = config.token
        access_token_secret = config.tokenSecret
        handle = "@MockBot1"

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, user, count = 1):
        # empty list to store parsed tweets

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.user_timeline(id=user, count=count, include_rts=True)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                            # return parsed tweets
            return parsed_tweet

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

    def mockReply(self, user, text):
        self.api.update_status(mockText(original = text, handle = user))
        print("Tweet posted.")
