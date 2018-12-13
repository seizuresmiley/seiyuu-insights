import json
import os
import collections as col
#sets the working directory.
working_dir = "result_raw/"
result_dir = "analysis_result/rts"

def rt_collector():
    '''collects retweeted tweets' user names'''
    #sets an empty counter object.
    count = col.Counter()
    #traverses through the working directory for files
    for filename in os.listdir(working_dir):
        #outputs the current working file.
        print(filename)
        #opens the file
        with open("%s%s" % (working_dir,filename),"r",encoding="utf8") as file:
            data = json.load(file)
            #traverses through the tweets in the file.
            for tweet in data['tweets']:
                #check if the tweet is a retweet.
                if "retweeted_status" in tweet:
                    #we update the count with screen name.
                    count.update({tweet['retweeted_status']['user']['screen_name']})
            #we make the directory to store the dumped files.
            os.mkdir("%s/%s" % (result_dir,data['handle']))
            #dumps the collection into a json file.
            with open("%s/%s/rts_%s.json" % (result_dir,data['handle'],data['handle']), "w+" ,encoding="utf8") as dump:
                dump.write(json.dumps(count.most_common(),indent=4))
                print("Dumped",data['handle'])
        #resets the count.
        count = col.Counter()
rt_collector()
