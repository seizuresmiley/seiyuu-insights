import collections
import pandas as pd
import pygal
import json
import os
import collections as col

#This script intends to graph favourites accumulation through 3200 tweets.
def collect_tags(read_dir):
    filelist = os.listdir(read_dir)
    c = col.Counter()
    for file in filelist:
        with open('%s%s' % (read_dir,file),"r",encoding='utf8') as raw:
            data = json.load(raw)
            for tweet in data['tweets']:
                if len(tweet['entities']['hashtags']) > 0:
                    for text in tweet['entities']['hashtags']:
                        hashtag = text['text']
                        c.update({hashtag})
    pygal_bar(c,"overview")
    c = col.Counter()


def pygal_bar(c,handle):
    '''makes a pygal chart from input'''
    most_common = c.most_common()
    cutlist = most_common[0:20]
    chart_title = "Top 20 Hashtags for All Users"
    barchart = pygal.Bar(title=chart_title)
    for items in cutlist:
        barchart.add(*items)
    print("Plotted",handle)
    
    barchart.render_to_file('analysis_result/overview/hashtags.svg')



collect_tags("result_raw/")