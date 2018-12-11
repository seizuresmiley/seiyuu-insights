import tweepy
import json
import csv
import time

#These keys authenticate to Twitter API.
with open('keys.json', "r") as keys:
    api_keys = json.load(keys)
#Sets the values in the dictionary as variables.
consumer_key = api_keys['consumer_key']
consumer_secret = api_keys['consumer_secret']
access_token = api_keys['access_token']
access_token_secret = api_keys['access_token_secret']
#Authentication Process.
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
def menu():
    ''' this function makes it so that the collection process requires
    user interaction'''
    print("Type any character to scrape")
    limit_check()
    input()
    scraper()

def scraper():
    '''main collection function'''
    count=0
    with open('list.csv' , mode='r') as target_list:
        target_dict = csv.DictReader(target_list)
        start_time = time.time()
        for row in target_dict:
            seiyuu_name = row['name']
            target_user = row['handle']
            chara_name = row['chara']
            #Check if the targeted person has a twitter account.
            if target_user == '<none>':
                #The resulting json will have the value 'has_twitter' as false.
                print("User has no twitter! skipping.")
            else:
                #This part is the part where we store information that is manually curated.
                result_dict = {"name" : row['name'], "handle" : row['handle'], "chara" : row['chara'],"timestamp" : 0, "tweets" : []}
                #"cur_response" would basically go through pages of tweets, until we get to Twitter's
                #hard limit of 3200 tweets or so.
                #count is also used to make sure we get a consistent amount of tweets.
                #since the API would sometimes return over 3200 tweets.
                cur_response = tweepy.Cursor(api.user_timeline, target_user,count=200).items(3200)

                #Prints out the current user the script is pulling data from.
                print(seiyuu_name,"(%s)" % (target_user)," as %s" % (chara_name))
                #This loop goes through all the tweets.
                for tweet in cur_response:
                    #this stores the responses into a huge dict.
                    result_dict['tweets'].append(tweet._json)
                    count += 1
                    #Prints out the progress of the collection process.
                    print('\r',"Tweets Collected: ", count,"out of 3200 theoretical.",end='')
                    #Breaks the loop when the count hits 3200. However, not all accounts
                    #would hit the 3200 limit.
                print("\n Done:" , count)
                # Dumps the result into a big json file.
                result_dict.update({"timestamp" : time.time()})
                with open("result_raw/%s(%s).json" % (target_user,seiyuu_name),"w+",encoding="utf8") as dump:
                    dump.write(json.dumps(result_dict,indent=4))
                    print(" Dumped to /result_raw/%s(%s).json" % (target_user,seiyuu_name),"\n Starting another user collection")
                    #this part keeps track of the elapsed time.
                    end_time = time.time()
                    print(" Time : ", end_time - start_time, "s")
                    #resets the count.

                count = 0
                api_limits = limit_check()
                print("Limit Status :",api_limits["remaining_calls"],api_limits["reset_time"],sep=' ')
                #this checks if we have enough API calls. It'd wait unitl
                #the reset. It usually takes 161 calls to complete a
                #3200 tweet profile.
                if api_limits["remaining_calls"] < 162:
                    print("Not enough calls left!")
                    print("Waiting until reset at " ,api_limits["reset_time"])
                    time.sleep(api_limits["reset_time"] - time.time())

def limit_check():
    '''checks the API rate limits'''
    #calls the API to get rate limit information
    rate_limit = api.rate_limit_status()
    remaining_calls = rate_limit["resources"]["statuses"]["/statuses/user_timeline"]["remaining"]
    reset = rate_limit["resources"]["statuses"]["/statuses/user_timeline"]["reset"]
    return {"remaining_calls" : remaining_calls , "reset_time" : reset}
menu()
