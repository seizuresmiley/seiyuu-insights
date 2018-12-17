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
            c.update({str(data['tweets'][0]['user']['verified']).replace("True","Verified").replace("False","Not Verified")})
            print(data['tweets'][0]['user']['verified'])
                    
    print(c)
    pygal_bar(c)

def pygal_bar(c):
    '''makes a pygal chart from input'''
    title = "Verification Status"
    lst = c.most_common()
    barchart = pygal.Pie(title=title)
    for items in lst:
        barchart.add(*items)
    print("Plotted")
    barchart.render_to_file('analysis_result/overview/verified.svg')

collect_tags("result_raw/")