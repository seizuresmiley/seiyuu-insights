import tweepy
import json

#These keys authenticate to Twitter API. Get your own.
with open('keys.json', "r") as keys:
    api_keys = json.load(keys)

print(api_keys)

consumer_key = api_keys['consumer_key']
consumer_secret = api_keys['consumer_secret']
access_token = api_keys['access_token']
access_token_secret = api_keys['access_token_secret']
#Authentication Process.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Request Parameters
print("Target User:")
target_user = input()
print("Target User : " , target_user)
#"response" is legacy code. It only retrieves 200 due to Twitter's API limitations.
response =  api.user_timeline(target_user, count=200)
#"cur_response" would basically go through pages of tweets, until we get to Twitter's
# hard limit of 3200 tweets or so.
cur_response = tweepy.Cursor(api.user_timeline, target_user).items()
# count is our way of counting the tweets this script has gone through
# total_fav counts the amount of likes.
count = 0
total_fav = 0
#user_details is used to get total tweets, followers and verify status.
user_details = api.get_user(target_user)
#This loop will display all tweets it went through.
for tweet in cur_response:
    print(tweet._json['text'])
    print("Favourites : ",tweet._json['favorite_count'])

    count +=1
    total_fav += int(tweet._json['favorite_count'])
    print(">>>>>>>>>>>>>>>>>>>")

#This displays the summary so that we know that the script is targeting the correct account.
print("Scraping Done.")
print("Contender: ",target_user)
print("Verified: ",user_details.verified)
print("Followers: ",user_details.followers_count)
percAnalyzed = 100 * (count / int(user_details.statuses_count))
print("Tweets Analyzed: ", count, "out of ", user_details.statuses_count, "tweets" ,"(%.2f) Percent" % percAnalyzed )
print("Total Faves: ", total_fav)
print("Rating: ", total_fav/count)
