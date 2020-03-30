import tweepy
import time
from random import seed
from random import randint
from keys import *
seed(1)
value = randint(1,99)
print('Portfolio Twitter Bot | Version 1.0.0', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    value = randint(1,99)
    print('[Searching for Tweets]', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    search = api.search(q='#developer #coding #programming',count=10,since_id=last_seen_id,tweet_mode='extended')
    for result in reversed(search):
        value = randint(1,99)
        last_seen_id = result.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        #if not 'RT' in result.full_text:
        if '#developer' in result.full_text.lower():
            print('[Retrieved Tweet] ID: ' + str(result.id) + ' | ' + result.full_text, flush=True)            
            print('[Tweet] Tweeting Portfolio to ID: ' + str(result.id) , flush=True)
            api.update_status('@' + result.user.screen_name + " I'm a developer looking for a job since the coronavirus took my job, if you could give my portfolio a look, and maybe even retweet this that would be greatly appreciated! <3 noobular.github.io ["+str(value)+"]", result.id)

while True:
    reply_to_tweets()
    time.sleep(15)