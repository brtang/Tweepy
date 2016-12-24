import tweepy
from tweepy.auth import OAuthHandler
import csv
import sys
import time

CONSUMER_KEY = 'pC6V4G11qGhIubpNKskUkHe7W'
CONSUMER_SECRET= 'uwM72qcmQDddW63pXYQcFyHabL3LkBqs4hNqdFHYVuBEJ3NEwj'

ACCESS_TOKEN = '744945353477099520-550n6dCi17CULrw6felJEWnaGwRtrOu'
ACCESS_TOKEN_SECRET = 'A5uoGOHGGU9FSvKwnYS7szaNMmPdE8GbZAdxZCshDWmP4'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

count = 86571
follower_count = 0
loopCount = 180

#Open file to append data

#For writing id's
#file = open('Complete_ids3.txt', 'w', encoding='utf-8')

#For writing follower items into CSV
file = open('complete_followers.csv', 'a', encoding='utf-8')
csvWriter = csv.writer(file)
#csvWriter.writerow(['Count','Follower Name', 'Follower Screen Name','Location', 'Friend Count','Follower Count','Creation Date'])
print('Done writing row')


accepted_states = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'}

#Limit handler function for cursors
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print('Sleeping for 15 minutes...')
            time.sleep(15 * 60)

#Limit handler function for lookup_user items            
def api_limit_handled(chunk):
    while True:
        try:
            return api.lookup_users(user_ids=chunk)
        except tweepy.RateLimitError:
            print('Sleeping for 15 minutes...')
            time.sleep(15 * 60)
            

'''
for follower in limit_handled(tweepy.Cursor(api.followers, screen_name="uber").items()):
    if count < 250:
        for accepted_state in accepted_states:
            if follower.lang == 'en' and accepted_state in follower.location:
                print('**********Start follower******')
                print('Count is: ', count)
                #name = follower.name.decode('iso8859-1')
                print('Name: ', follower.name)
                print('Screen name: ', follower.screen_name)
                print('Location: ', follower.location)
                print('Follower count: ', follower.followers_count)
                print('Friend count: ', follower.friends_count)
                print('Created at: ', follower.created_at)
                print('Language: ', follower.lang)
                print('**********End follower**********')
                count += 1
    else:
        file.close()
        print('Script has reached end. Count is: ', count)
        break
    
ids = []
for page in limit_handled(tweepy.Cursor(api.followers_ids, screen_name="uber").items()):
     ids.append(page)
     file.write(str(page) + '\n')
     print('Length is: ', len(ids))    
     

'''
lines = [line.rstrip('\n') for line in open('C:/Users/Brian/Documents/Scrapy/tweepy/finalUberIds/final_ids_33.txt')] 
lines = [int(i) for i in lines]

chunks = [lines[x:x+100] for x in range(0, len(lines), 100)]
for chunk in chunks:
    followers = api_limit_handled(chunk)
    for follower in followers:
        for accepted_state in accepted_states:
            if follower.lang == 'en' and accepted_state in follower.location:
                print('Count is: ', count)
                print('Name: ', follower.name)
                print('Screen name: ', follower.screen_name)
                print('Location: ', follower.location)
                print('Follower count: ', follower.followers_count)
                print('Friend count: ', follower.friends_count)
                print('Created at: ', follower.created_at)
                print('Language: ', follower.lang)
                csvWriter.writerow([count,follower.name, follower.screen_name,follower.location, follower.friends_count,follower.followers_count,follower.created_at])
                count += 1

    