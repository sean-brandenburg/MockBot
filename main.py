import re
import config
import tweepy
import bot
from tweepy import OAuthHandler
from textblob import TextBlob
from mock import mockText

def main():

    name = input("Enter the name of the target account: ")
    userIn = "@{}".format(name)
    # creating object of TwitterClient Class
    api = bot.TwitterClient()
    # calling function to get tweets

    api.loop(user=userIn)


if __name__ == "__main__":
    # calling main function
    main()
