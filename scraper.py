import tweepy
import csv
import sys

CONSUMER_KEY = '' #Your key here
CONSUMER_SECRET = '' #Your key here
ACCESS_TOKEN = '' #Your key here
ACCESS_TOKEN_SECRET = '' #Your key here

authentication = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
authentication.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(authentication,wait_on_rate_limit=True)

#replace filename with the filename you want
csvFile = open('filename.csv', 'a')
csvWriter = csv.writer(csvFile)
#replace #hashtag with hashtag of your choice
for tweet in tweepy.Cursor(api.search, q="#hashtag").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()
