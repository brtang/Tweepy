import tweepy
from tweepy.auth import OAuthHandler
import csv

CONSUMER_KEY = 'pC6V4G11qGhIubpNKskUkHe7W'
CONSUMER_SECRET= 'uwM72qcmQDddW63pXYQcFyHabL3LkBqs4hNqdFHYVuBEJ3NEwj'

ACCESS_TOKEN = '744945353477099520-550n6dCi17CULrw6felJEWnaGwRtrOu'
ACCESS_TOKEN_SECRET = 'A5uoGOHGGU9FSvKwnYS7szaNMmPdE8GbZAdxZCshDWmP4'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

for follower in tweepy.Cursor(api.followers, screen_name="uber").items(20):
    print('**********Start follower******')
    print(follower.screen_name)
    print(follower.location)
    print(follower.followers_count)
    print('**********End follower**********')