import json
import os
import collections as col

#defines some working directories.
working_dir = "result_raw/"
result_dir = "analysis_result/mentions"

def mention_collector():
    '''collects the mentioned user in a json file'''
    # sets a counter variable.
    count = col.Counter()
    #traverses through the working directory for files.
    for filename in os.listdir(working_dir):
        #prints out the current working filename.
        print(filename)
        #opens the current working file.
        with open("%s%s" % (working_dir,filename),"r",encoding="utf8") as file:
            #loads the working file as a dictionary.
            data = json.load(file)
            #traverses through the tweets.
            for tweet in data['tweets']:
                #we check if there's a mention in the tweet.
                if len(tweet["entities"]['user_mentions']) > 0:
                    #then we count the screen names.
                    for mentions in tweet['entities']['user_mentions']:
                        count.update({mentions['screen_name']})
            #makes a directory to put the result file in.
            os.mkdir("%s/%s" % (result_dir,data['handle']))
            #We dump it into a file.
            with open("%s/%s/mentions_%s.json" % (result_dir,data['handle'],data['handle']), "w+" ,encoding="utf8") as dump:
                dump.write(json.dumps(count.most_common(),indent=4))
                print("Dumped",data['handle'])
        #resets the counter.
        count = col.Counter()
mention_collector()
