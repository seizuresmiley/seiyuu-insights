import json
import urllib.request as req
import os
import tweepy
#We import twitter.py to use it's limit check function.
import csv

working_dir = "analysis_result/user_info"

#Get API keys.
with open('keys.json', "r") as keys:
    api_keys = json.load(keys)
#Sets the values in the dictionary as variables.
key = api_keys['consumer_key']
secret = api_keys['consumer_secret']
access_token = api_keys['access_token']
access_token_secret = api_keys['access_token_secret']
#Authenticates to Twitter.
auth = tweepy.AppAuthHandler(key,secret)
api = tweepy.API(auth)

def get_user_info():
    '''gets profile image and a sample tweet'''
    #opens the list.csv file.
    with open('list.csv' , mode='r') as target_list:
        target_dict = csv.DictReader(target_list)
        #traverses through the list.csv in rows.
        for row in target_dict:
            #checks if the handle exists.
            if row['handle'] == "<none>":
                print("skipped.")
            #if it exists, we do this process.
            else:
                #outputs handle.
                print(row['handle'])
                #calls the API to get a user information.
                result = dict(api.get_user(row['handle'])._json)
                #check if directory exists, if not, makes it.
                if not os.path.isdir("%s/%s" % (working_dir,row['handle'])):
                    os.mkdir("%s/%s" % (working_dir,row['handle']))
                #dumps the user information file.
                with open("%s/%s/%s.json"%(working_dir,row['handle'],row['handle']),"w+",encoding="utf8") as dump:
                    dump.write(json.dumps(result, indent=4))
                    print("dumped.")
                #makes a full-resolution profile picture URL.
                profile_url = result['profile_image_url'].replace("_normal",'')
                #prints the URL out.
                print(profile_url)
                #retrieves the image.
                req.urlretrieve(profile_url,"%s/%s/profile.jpg"%(working_dir,row['handle']))
                #prints success image.
                print("got profile pic.")

def limit_check():
    '''checks the API rate limits'''
    #calls the API to get rate limit information
    rate_limit = api.rate_limit_status()
    remaining_calls = rate_limit["resources"]["statuses"]["/statuses/user_timeline"]["remaining"]
    reset = rate_limit["resources"]["statuses"]["/statuses/user_timeline"]["reset"]
    return {"remaining_calls" : remaining_calls , "reset_time" : reset}

get_user_info()
