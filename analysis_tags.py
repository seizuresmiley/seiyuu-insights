import json
import os
import collections as coll

working_dir = "result_raw/"
result_dir = "analysis_result/tags/"

def filelist():
    '''gets all files in the working directory'''
    global working_dir
    files_list = []
    for filename in os.listdir(working_dir):
        files_list.append(filename)
    return files_list

def analyze_tags():
    '''ranks tags in tweets'''
    global result_dir
    global working_dir
    files_list = filelist()
    c = coll.Counter()
    for file in files_list:
        with open("%s%s" % (working_dir,file),"r",encoding="utf8") as file:
            data = json.load(file)
            for tweet in data['tweets']:
                if len(tweet['entities']['hashtags']) > 0:
                    for text in tweet['entities']['hashtags']:
                        hastag = text['text']
                        c.update({hastag})
            common_tags = c.most_common()
            with open("%s%s.json" % (result_dir,data['handle']), "w+" ,encoding="utf8") as dump:
                dump.write(json.dumps(common_tags,indent=4))
                print("Dumped",data['handle'])
        c = coll.Counter()


analyze_tags()
