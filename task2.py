import json
from task1 import movie_data
import json
data1=open("task1.json")
movies=json.load(data1)
def group_by_decade(movies):
    dic1={}
    for index in movies:
        movie_data=[]
        year=index["Year"]
        if year not in dic1:
            for k in movies:
                if year==k["Year"]:
                    movie_data.append(k)
            dic1[year]=movie_data
    with open ("task2.json","w+") as file:
        json.dump(dic1,file,indent=4)
        a=json.dumps(dic1)
year1=group_by_decade(movie_data)