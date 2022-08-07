import json
from bs4 import BeautifulSoup
from task5 import get_movie_details_list
director=get_movie_details_list()
def analyse_movie_director(director):
    dict={}
    for i in director:
        director_name=i["director"]
        for j in director_name:
            if j not in dict:
                dir_name=j
                dict[j]=1
            else:
                dict[j]+=1
    print(dict)
    with open("task7.json","w")as file:
        json.dump(dict,file,indent=4)
    return dict
analyse_movie_director(director)

