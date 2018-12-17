import collections
import pygal
import json
import os
import collections as col

#This script intends to graph favourites accumulation through 3200 tweets.
def plot(read_dir):
    filelist = os.listdir(read_dir)
    result = []
    for file in filelist:
        with open('%s%s' % (read_dir,file),"r",encoding='utf8') as raw:
            data = json.load(raw)
            result.append((data['handle'],data['tweets'][0]['user']['friends_count']))
            print(file)
    pygal_bar(result)

def pygal_bar(result):
    '''makes a pygal chart from input'''
    title = "Favourites Count (User Favourited Tweets)"
    barchart = pygal.Bar(title=title,legend_at_bottom=True,legend_at_bottom_columns = 4)
    for items in result:
        barchart.add(*items)
    print("Plotted")
    barchart.render_to_file('analysis_result/overview/faves.svg')

plot("result_raw/")