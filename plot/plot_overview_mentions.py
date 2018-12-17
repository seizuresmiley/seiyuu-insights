import collections
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
    pygal_bar(count,"overview")
    count = col.Counter()

def collect_tags_noself(read_dir):
    filelist = os.listdir(read_dir)
    count = col.Counter()
    for file in filelist:
        with open('%s%s' % (read_dir,file),"r",encoding='utf8') as raw:
            data = json.load(raw)
            for tweet in data['tweets']:
                if len(tweet["entities"]['user_mentions']) > 0 and "retweeted_status" not in tweet:
                        #then we count the screen names.
                        for mentions in tweet['entities']['user_mentions']:
                            if data['handle'].replace('@',"") != mentions['screen_name']:
                                count.update({mentions['screen_name']})
    pygal_bar(count,"overview")
    count = col.Counter()

def pygal_bar(c,handle):
    '''makes a pygal chart from input'''
    most_common = c.most_common()
    cutlist = most_common[0:20]
    chart_title = "Top 20 Mentions for All Users"
    barchart = pygal.Bar(title=chart_title)
    for items in cutlist:
        barchart.add(*items)
    print("Plotted",handle)
    
    barchart.render_to_file('analysis_result/overview/mentions_noself.svg')



collect_tags_noself("result_raw/")