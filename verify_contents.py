import os
import tweepy
import json
import csv
# sets the working directory.
working_dir = "result_raw/"


def filelist():
    '''gets all files in the result_raw directory'''
    global working_dir
    files_list = []
    for filename in os.listdir(working_dir):
        files_list.append(filename)
        return files_list


def user_exists():
    '''checks for incomplete data collection'''
    # gets global variable
    global working_dir
    # opens the list.csv file.
    with open('list.csv', mode='r') as target_list:
        target_dict = csv.DictReader(target_list)
        files_list = filelist()
        # collects all the mismatched users.
        mismatches = []
        for row in target_dict:
            seiyuu_name = row['name']
            target_user = row['handle']
            if row['handle'] == "<none>":
                print("%s has no handle." % (row['name']))
            else:
                data = {}
                # Loads the json file.
                with open("%s%s(%s).json" % (working_dir, target_user, seiyuu_name), "r", encoding="utf8") as proc:
                    data = json.load(proc)
                    print("Verifying", data['handle'])
                    # We check if the user has more than 3200 tweets and that we collected 3200
                    # tweets.
                    if data['tweets'][0]['user']['statuses_count'] > 20 and len(data['tweets']) < 20:
                        mismatches.append(data['handle'])
    # Outputs the results
    if len(mismatches) > 0:
        print("Mismatches detected: ")
        for handle in mismatches:
            print(handle)
    else:
        print("No mismatches detected.")


user_exists()
