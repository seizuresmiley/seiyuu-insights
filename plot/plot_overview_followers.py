import collections
import pygal
import json
import os
import collections as col

#This script intends to graph favourites accumulation through 3200 tweets.
def plot_followers(read_dir):
    filelist = os.listdir(read_dir)
    followers = []
    for file in filelist:
        with open('%s%s' % (read_dir,file),"r",encoding='utf8') as raw:
            data = json.load(raw)
            followers.append((data['handle'],data['tweets'][0]['user']['followers_count']))
            print(file)
    pygal_bar(followers)

def pygal_bar(followers):
    '''makes a pygal chart from input'''
    title = "Followers Count"
    barchart = pygal.Bar(title=title,legend_at_bottom=True,legend_at_bottom_columns = 4)
    for items in followers:
        barchart.add(*items)
    print("Plotted")
    barchart.render_to_file('analysis_result/overview/followers.svg')

plot_followers("result_raw/")