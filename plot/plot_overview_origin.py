import collections
import pygal
import json
import os
import collections as col
import re

#This script intends to graph favourites accumulation through 3200 tweets.
def plot(read_dir):
    filelist = os.listdir(read_dir)
    result = col.Counter()
    for file in filelist:
        with open('%s%s' % (read_dir,file),"r",encoding='utf8') as raw:
            data = json.load(raw)
            for tweet in data['tweets']:
                #looks for the platform name using regex.
                match = re.search('\>(.*?)\<',tweet['source']).group(1)
                #if it matches, we update the counter.
                if match:
                    result.update({match})
    pygal_bar(result)

def pygal_bar(result):
    '''makes a pygal chart from input'''
    title = "Top 10 Tweet Origins"
    result_short = result.most_common()
    barchart = pygal.Pie(title=title,legend_at_bottom=True,legend_at_bottom_columns = 4,print_values=True)
    for items in result_short[0:10]:
        barchart.add(*items)
    print("Plotted")
    barchart.render_to_file('analysis_result/overview/origin.svg')

plot("result_raw/")