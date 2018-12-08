import os
import tweepy
import json
import csv
#sets the working directory.
working_dir = "result_raw_small/"

def filelist():
    '''gets all files in the result_raw directory'''
    global working_dir
    files_list = []
    for filename in os.listdir(working_dir):
        files_list.append(filename)
        return files_list

def user_exists():
    '''checks for incomplete data collection'''
    global working_dir
        files_list = filelist()
        mismatches = []
        for row in target_dict:
            seiyuu_name = row['name']
            target_user = row['handle']
            if row['handle'] == "<none>" :
                print("%s has no handle." % (row['name']))
            else:
                single_result = {}
                data = {}
                with open("%s%s(%s).json" % (working_dir,target_user,seiyuu_name),"r",encoding="utf8") as proc:
                    data = json.load(proc)
                    print("Verifying",data['handle'])
                    if data['tweets'][0]['user']['statuses_count'] > 20 and len(data['tweets']) < 20:
                        mismatches.append(data['handle'])
    if len(mismatches) > 0 :
        print("Mismatches detected: ")
        for handle in mismatches:
            print(handle)
    else:
        print("No mismatches detected.")

def single_user():
    with open("result_raw/@kanako_nomura(Kanako Nomura).json","r+",encoding="utf8") as singleuser:
        data = json.load(singleuser)
        print(data["tweets"][0]["text"])

user_exists()
