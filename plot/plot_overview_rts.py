import json
import os
import collections as col
import pygal

#This script intends to graph favourites accumulation through 3200 tweets.
def collect_rts(read_dir):
    filelist = os.listdir(read_dir)
    c = col.Counter()
    for file in filelist:
        with open('%s%s' % (read_dir,file),"r",encoding='utf8') as raw:
            data = json.load(raw)
            for tweet in data['tweets']:
                #check if the tweet is a retweet.
                if "retweeted_status" in tweet:
                    #we update the count with screen name.
                    c.update({tweet['retweeted_status']['user']['screen_name']})
    pygal_bar(c,"overview")
    c = col.Counter()


def pygal_bar(c,handle):
    '''makes a pygal chart from input'''
    most_common = c.most_common()
    cutlist = most_common[0:20]
    chart_title = "Top 20 Retweeted Users for All Users"
    barchart = pygal.Bar(title=chart_title)
    for items in cutlist:
        barchart.add(*items)
    print("Plotted",handle)
    
    barchart.render_to_file('analysis_result/overview/retweets.svg')



collect_rts("result_raw/")