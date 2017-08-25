#!/usr/bin/env python
import plugins.twitter as twitter

def setupTwitter(consumer_key):
    t = twitter.Twitter()
    t.consumer_key = consumer_key
    t.consumer_secret = "test"
    t.access_token = "test"
    t.access_token_secret = "test"
    t.check_config()

setupTwitter('test')