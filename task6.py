import json
from bs4 import BeautifulSoup
from task5 import get_movie_details_list
language=get_movie_details_list()
def analayse_movie_language(language):
    dict={}
    for i in language:
        if "language" in i:
            language=i["Language"]
            if "language" not in dict:
                language=i["Language"]
                dict[language]=1
            else:
                dict[language]+=1 
        else:
            continue
    # print(dict)
    with open("task6.json","w")as file:
        json.dump(dict,file,indent=4)
analayse_movie_language(language)
