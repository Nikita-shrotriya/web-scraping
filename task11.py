import json
from bs4 import BeautifulSoup
from task4 import movie_details
from task5 import get_movie_details_list
with open("task5.json","r") as file:
    list=json.load(file)
# languege=get_movie_details_list()
print()
def analyse_movies_genre(list):
    list1=[]
    for i in list:
        # print(i)
        a=json.loads(i)
        genre=a["Genre"]
        for j in genre:
            if j not in list1:
                list1.append(j)
    analysis_genre={gener_type:0 for gener_type in list1}
    for gener_type in list1:
        for i in list:
            a=json.load(i)
            if gener_type in a["Genre"]:
                analysis_genre[gener_type]+=1
        with open("task11.json","w+") as file:
            json.dump(analysis_genre,file,indent=4)
    return analysis_genre
gener_analysis=analyse_movies_genre(movie_details)
print(gener_analysis)