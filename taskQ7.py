import json
from bs4 import BeautifulSoup
from task5 import get_movies_details_list

language=get_movies_details_list()
def analyse_movies_language(language):
    dict={}
    for i in language:
        if "Language" in i:
            Language=i["Language"]
            if Language not in dict:
                Language=i["Language"]
                dict[Language]=1
            else:
                dict[Language]+=1
        else:
            continue
    # print(dict)
    with open("task6.json","w+")as files:
        json.dump(dict,files,indent=4)
analyse_movies_language(language)