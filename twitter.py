import tweepy
import json
import csv
import sys
import os.path

#These keys authenticate to Twitter API.
with open('keys.json', "r") as keys:
    api_keys = json.load(keys)

consumer_key = api_keys['consumer_key']
consumer_secret = api_keys['consumer_secret']
access_token = api_keys['access_token']
access_token_secret = api_keys['access_token_secret']
#Authentication Process.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
def menu():
    print("Type any character to scrape")
    input()
    scraper()

def scraper():
    count=0
    with open('list.csv' , mode='r') as target_list:
        target_dict = csv.DictReader(target_list)
        for row in target_dict:
            seiyuu_name = row['name']
            target_user = row['handle']
            chara_name = row['chara']

            if target_user == '<none>':
                result_dict = {"name" : row['name'], "handle" : row['handle'], "chara" : row['chara'],"has_twitter" : False, "tweets" : []}
                print("User has no twitter! skipping.")
            else:
                result_dict = {"name" : row['name'], "handle" : row['handle'], "chara" : row['chara'],"has_twitter" : True, "tweets" : []}

                #"cur_response" would basically go through pages of tweets, until we get to Twitter's
                #hard limit of 3200 tweets or so.
                #count is also used to make sure we get a consistent amount of tweets.
                #since the API would sometimes return over 3200 tweets.
                cur_response = tweepy.Cursor(api.user_timeline, target_user).items()
                #This loop will display all tweets it went through, unitl it hits 3200.
                print(seiyuu_name,"(%s)" % (target_user)," as %s" % (chara_name))
                for tweet in cur_response:
                    result_dict['tweets'].append(tweet._json)
                    count += 1

                    print('\r',"Tweets Collected: ", count,"out of 3200 theoretical.",end='')
                    if count == 3:
                        print("\n Done:" , count)
                        break

                    # Dumps the result into a big json file.
                with open("result_raw/%s(%s).json" % (target_user,seiyuu_name),"a",encoding="utf8") as dump:
                    dump.write(json.dumps(result_dict,indent=4))
                    print("Dumped to /result_raw/%s(%s).json" % (target_user,seiyuu_name)," Starting another user collection")
                    #resets the count.
                    count = 0
menu()
