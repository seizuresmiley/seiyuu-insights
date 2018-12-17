import collections
import matplotlib.pyplot as plt
import pandas as pd
import pygal
import json
import os
import collections as col

#This script intends to graph favourites accumulation through 3200 tweets.
def collect_tags(read_dir):
    filelist = os.listdir(read_dir)
    count = col.Counter()
    for file in filelist:
        with open('%s%s' % (read_dir,file),"r",encoding='utf8') as raw:
            data = json.load(raw)
            for tweet in data['tweets']:
                if len(tweet["entities"]['user_mentions']) > 0 and "retweeted_status" not in tweet :
                    #then we count the screen names.
                    for mentions in tweet['entities']['user_mentions']:
                        count.update({mentions['screen_name']})
        pygal_bar(count,data['handle'])
        count = col.Counter()


def pygal_bar(count,handle):
    '''makes a pygal chart from input'''
    most_common = count.most_common()
    cutlist = most_common[0:10]
    chart_title = "Top 10 Mentions for %s" % (handle)
    barchart = pygal.Bar(title=chart_title)
    for items in cutlist:
        barchart.add(*items)
    print("Plotted",handle)
    
    barchart.render_to_file('analysis_result/mentions_pygal/%s.svg' % (handle))



collect_tags("result_raw/")