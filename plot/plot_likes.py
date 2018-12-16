import collections
import matplotlib.pyplot as plt
import pandas as pd
import json
import os

#This script intends to graph favourites accumulation through 3200 tweets.
def likes(read_dir,current_file):
    '''returns a list with amount of status likes'''
    #creates an empty list
    result = list()
    #Opens the data file
    with open("%s%s" % (read_dir,current_file),"r",encoding='utf8') as raw:
        data = json.load(raw)
        for tweet in data['tweets']:
            result.append(tweet['favorite_count'])
        endtime = data['tweets'][0]["created_at"]
        starttime = data['tweets'][-1]["created_at"]
        handle = data['tweets'][0]['user']['screen_name']
    #Calls a plotting function to plot thee data.
    plotter(result,starttime,endtime,handle)
    print("Called plotter() to plot ",handle)

def plotter(lst,start,end,handle):
    '''makes a line chart from the provided args'''
    #Make a Pandas Series.
    series = pd.Series(lst,index=pd.date_range(start=start,end=end,periods=len(lst)))
    #Make a sum of all favourites
    series = series.cumsum()
    #Plots the series into an Axes object
    ax = series.plot(figsize=(20,10),fontsize=30,subplots=False)
    #Sets various visual elements of the chart
    ax.set_title("Like Accumulation for %s" % (handle),fontsize=45)
    ax.set_xlabel("Date",fontsize=30)
    ax.set_ylabel("Like Count",fontsize=30)
    #Make an image object out of the Axes.
    image = ax.get_figure()
    #Saves the image.
    image.savefig('analysis_result/likes/line_plot/%s.png' % (handle))
    print("Plotted" ,handle)
    #Clear out the variables
    ax = None
    series = None
    image = None
    #Specify that we want to make a new plot.
    plt.clf()

def files_list(read_dir):
    '''traverses through the working directory and return each file'''
    files = os.listdir(read_dir)
    for file in files:
        likes(read_dir,file)
#We would put the raw data directory as an argument.
files_list("result_raw/")
