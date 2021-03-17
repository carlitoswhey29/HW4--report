# import the module 
import time
import tweepy
import re 

# limit number of friends
MAX_COUNT = 5000
TWITTER_FRIEND_COUNT_FILE = './data/twitter-friends-count.txt'
TWITTER_FRIENDS = './data/friends_list.txt'
# OAuth2 procedure
consumer_key = "" # Removed
consumer_secret = "" # Removed
# authorization of consumer key and consumer secret 
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
# calling the api  
api = tweepy.API(auth)

ids = []
with open(TWITTER_FRIENDS,'r') as rf:
    for person in rf:
        item = person.replace('\n','')
        ids.append(item)

f_ids = []
with open(TWITTER_FRIEND_COUNT_FILE,'a') as f:
  # the screen_name of the targeted user 
  for follower in ids:
    next_friend = tweepy.Cursor(api.followers_ids, id=follower, wait_on_rate_limit=True).items(5000)
    try: 
      for friend in next_friend:
        f_ids.append(friend)
      print(str(follower) + ', Followers:  ' + str(len(f_ids)), file=f)
      print(follower) # to track progress
    except tweepy.TweepError as e:
      print (e)
