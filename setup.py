from setuptools import setup

setup(
    name='MockBot'
    version=1.0
    description='Twitter bot that mocks negative tweets.'
    packages=['MockBot']
    install_requires=['tweepy','textblob','re',]
)
