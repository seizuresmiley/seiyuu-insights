import collections
import pygal
import json
import os
import collections as col

#This script intends to graph favourites accumulation through 3200 tweets.
def plot(read_dir):
    filelist = os.listdir(read_dir)
    result = col.Counter()
    for file in filelist:
        with open('%s%s' % (read_dir,file),"r",encoding='utf8') as raw:
            data = json.load(raw)
            date_created = data['tweets'][0]['user']['created_at']
            year_created = date_created[-5:]
            print(year_created)
            result.update({year_created})
    pygal_bar(result)

def pygal_bar(result):
    '''makes a pygal chart from input'''
    title = "Account Created Date (By Year)"
    resultlist = sorted(result.items())
    barchart = pygal.Bar(title=title,legend_at_bottom=True,legend_at_bottom_columns = 4)
    for items in resultlist:
        barchart.add(*items)
    print("Plotted")
    barchart.render_to_file('analysis_result/overview/year_created.svg')

plot("result_raw/")