import json
import os

def seiyuu_info(directory):
    '''traverses the result directory'''
    for file in os.listdir(directory):
        with open("%s%s" % (directory,file), "r",encoding="utf8") as raw:
            #we return the info for the text replacement
            info = json.load(raw)
            handle = info['handle']
            real_name = info['name']
            handle_no_at = info['handle'].replace('@',"")
            print("calling makepage for",handle)
            makepage(handle,handle_no_at,real_name)
            
        
def makepage(handle,handle_no_at,real_name):
    '''replaces text from template.html'''
    #opens the result file
    with open('analysis_result/pages/%s.html' % (handle_no_at), "w+",encoding='utf8') as resultpage:
        #opens the template file
        with open('template.html',"r",encoding="utf8") as template:
            #traverses through each line
            for line in template:
                #replaces the keywords with data from another function.
                newline = line.replace("realname",real_name).replace("ins_handle",handle).replace("no_at",handle_no_at)
                #writes it
                resultpage.write(newline + "\n")
        template.close()
    resultpage.close()
    

seiyuu_info("result_raw_example/")
    



            

    