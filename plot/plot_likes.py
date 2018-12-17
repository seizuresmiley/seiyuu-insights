import collections
import pygal
from pygal.style import Style
import pandas as pd
import json
import os

#This script intends to graph favourites accumulation through 3200 tweets.
def likes(read_dir,current_file):
    '''returns a list with amount of status likes'''
    #creates an empty list
    result = list()
    time = list()
    #Opens the data file
    with open("%s%s" % (read_dir,current_file),"r",encoding='utf8') as raw:
        data = json.load(raw)
        for tweet in data['tweets']:
            result.append(tweet['favorite_count'])
            time.append(tweet["created_at"])
        time.reverse()
        handle = data['tweets'][0]['user']['screen_name']
        color = "#" + data['tweets'][0]['user']['profile_link_color']
    #Calls a plotting function to plot thee data.
    pygal_line(result,time,handle,color)
    print("Called pygal_line() to plot ",handle)


def pygal_line(lst,time,handle,color):
    '''make a pygal chart'''
    profile_color = Style(colors = [color])
    series = pd.Series(lst,index=time)
    series = series.cumsum()
    chart_title = "Favourites Accumulation for %s" % (handle)
    line_chart = pygal.Line(title=chart_title ,x_title='Time', y_title='Accumulated Favourites', style=profile_color)
    line_chart.x_labels = time
    line_chart.add(handle,series)
    line_chart.render_to_file('analysis_result/favourites_pygal/%s.svg' % (handle))


def files_list(read_dir):
    '''traverses through the working directory and return each file'''
    files = os.listdir(read_dir)
    for file in files:
        likes(read_dir,file)
#We would put the raw data directory as an argument.
files_list("result_raw/")
