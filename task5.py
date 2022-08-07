import json
from task1 import movie_data
from task4 import movie_details
with open("task1.json","r") as file:
    a=json.load(file)
def get_movie_details_list():
    list=[]
    for i in a:
        k=i["moviceurl"]
        list.append(movie_details(k))
        #print(list)
    with open("task5.json","w") as file5:
        json.dump(list,file5,indent = 4)
    return list
get_movie_details_list()