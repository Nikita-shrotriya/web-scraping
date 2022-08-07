import json
import requests
from bs4 import BeautifulSoup
#import pprint

main=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
soup=BeautifulSoup(main.text,"html.parser")

# print(soup)
def scrap_top_list():
    list=[]
    mainDiv=soup.find("div",class_="body_main container")
    # print(mainDiv)
    subDiv=mainDiv.find("table",class_="table")
    # print(subDiv)
    tableall=subDiv.find_all('tr')
    # print(tableall)
    for i in tableall:
        d1={}
        alltds=i.find_all('td')
        # print(alltds)
        for j in alltds:
            rank=i.find('td',class_="bold").get_text()[:-1]
            d1["rank"]=int(rank)
            # print(rank)
            movieName=i.find("a",class_="unstyled articleLink")["href"][3:]
            d1["movieName"]=movieName
            moviceurl=i.find("a",class_="unstyled articleLink")["href"]
            m="https://www.rottentomatoes.com"+moviceurl
            d1["moviceurl"]=m
            # print(movieName)
            Year=i.find('a',class_="unstyled articleLink").text
            year1=Year.strip()
            d1["Year"]=int(Year[-5:-1])
        # print(d1)
        list.append(d1.copy())
        if {} in list:
            list.remove({})
        # print(list)
    with open("task1.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
movie_data=scrap_top_list()
