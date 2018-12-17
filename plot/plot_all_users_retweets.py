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
               if "retweeted_status" in tweet:
                    #we update the count with screen name.
                    count.update({tweet['retweeted_status']['user']['screen_name']})
        pygal_bar(count,data['handle'])
        count = col.Counter()


def pygal_bar(count,handle):
    '''makes a pygal chart from input'''
    most_common = count.most_common()
    cutlist = most_common[0:10]
    chart_title = "Top 10 Users Retweeted for %s" % (handle)
    barchart = pygal.Bar(title=chart_title)
    for items in cutlist:
        barchart.add(*items)
    print("Plotted",handle)
    
    barchart.render_to_file('analysis_result/rts_pygal/%s.svg' % (handle))



collect_tags("result_raw/")