import re
import config
import tweepy
import bot
from tweepy import OAuthHandler
from textblob import TextBlob
from mock import mockText

def main():

    name = input("Enter the name of the target account: ")
    # creating object of TwitterClient Class
    api = bot.TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(user = name, count = 1)

    if tweets['sentiment'] == 'negative':
        print(tweets['text'])
        api.mockReply(text = tweets['text'],user = name)

if __name__ == "__main__":
    # calling main function
    main()
