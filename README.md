# ml-seiyuu-analysis
Million Live! Seiyuu Twitter Analysis

Analysing trends among seiyuus through Tweets.

## Scope

We intend to analyse various metrics retrieved through Twitter. We are targeting various Voice Actors who had a part in voicing the characters in the series of video games named *"THE IDOLM@STER Million Live!"*. We got a result of over 72,000 tweets across 32 users.


## Information:
Site : on [seirent.info](http://projects.seirent.info/MLAnalysis/main.html)

Language: Python

Third Party libraries used: [tweepy](http://www.tweepy.org), [pandas](https://pandas.pydata.org/), [pygal](http://pygal.org)



## Methodology
We retrieved user handles from this unofficial list of handles compiled by fans.

We can not thank them hard enough for their efforts.

https://docs.google.com/spreadsheets/d/1C-DamOHRSZQvhhAow458luQ43ohnHs6kETyP7dMTBbA/edit#gid=0

Using the [tweepy](http://www.tweepy.org/) library, we can pull tweets through the official Twitter API. We can then dump the request into a JSON file to be analysed later on.
This process is done using [twitter.py](https://github.com/seizuresmiley/ml-seiyuu-analysis/blob/master/twitter.py).


## Using twitter.py
"twitter.py" is the script that we used to dump raw data for analysis. It is advised that the data is verified afterwards using "verify_contents.py" to make sure the resulting dump is complete.

The script requires valid keys from Twitter to be able to do API calls. You can get the keys from [Twitter Developer Platform](https://developer.twitter.com/content/developer-twitter/en.html).

`result_raw_example` is example data retrieved using the tool.

It contains 20 tweets. You can use the analysis tools on these if you want.


## Verification Script
The verification script makes sure we get the maximum amount of tweets from a user. The max is 3200 tweets from a single user due to Twitter's API limits. [Learn More](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html).

## Analysis Scripts
Scripts in `analysis_tools` are tools for rudimentary data analysis.

However, most visualization tools are in `plot` folder.
