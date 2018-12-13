import os
import json
import re
import collections as col

#sets the working directory.
working_dir = "result_raw/"

def collect_origin():
    '''collects the origin of the tweets'''
    #sets  an empty counter object.
    count = col.Counter()
    #traverses thtough the files in working directory.
    for filename in os.listdir(working_dir):
        #prints out the current working filename.
        print(filename)
        #opens the current working file.
        with open("%s%s" % (working_dir,filename),"r",encoding="utf8") as file:
            #loads the working file.
            data = json.load(file)
            #traverses through the tweets.
            for tweet in data['tweets']:
                #looks for the platform name using regex.
                match = re.search('\>(.*?)\<',tweet['source']).group(1)
                #if it matches, we update the counter.
                if match:
                    count.update({match})
collect_origin()
