import json
import collections as col
import os

def rank_users(working_dir):
    print("Ranking users by tags.")
    #we take the input as a search query.
    search_query = input()
    #sets an empty counter object.
    #the counter contains how many times a user
    #tweeted the tag.
    results = col.Counter()
    #traverses through the current working directory.
    for file in os.listdir("result_raw/"):
        #opens the current working file.
        with open("result_raw/%s" % (file),"r",encoding="utf8") as current_file:
            #loads the json file as a variable
            data = json.load(current_file)
            #traverses through the tweets
            for tweet in data['tweets']:
                #pulls out the tags in the tweet.
                tags = tweet['entities']['hashtags']
                #check if the query is inside the variable.
                if any(tag['text'] == search_query for tag in tags):
                    #updates the counter with the screen name.
                    results.update({tweet['user']['screen_name']})
    #dumps the result.
    with open("%s/%s.json" % (working_dir,search_query), 'w+', encoding='utf8') as dump:
        dump.write(json.dumps(results.most_common(), indent=4))
rank_users("analysis_result/tagsearch")
