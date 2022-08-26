import pymongo as pymongo

import twitter as twitterPremier
import json
import pymongo
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("localhost", 27017)
db = client.local
collection = db.Tweets
requesting = []

scraper = twitterPremier.TwitterHashtagScraper("premierleague")

testTweets = []

for i, tweet in enumerate(scraper.get_items()):
    if i > 10:
        break
    testTweets.append({"id": tweet.id, "content": tweet.content, "likes": tweet.likeCount})

x = collection.insert_many(testTweets)



