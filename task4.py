from bs4 import BeautifulSoup
import requests
import json
url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"

def movie_details(movie_url):
    res=requests.get(movie_url)
    soup = BeautifulSoup(res.text,"html.parser") 
    h1=soup.find("h1", class_="scoreboard__title").get_text()
    li=soup.find_all("li",class_="meta-row clearfix")
    dic={}
    dic["Name"]=h1
    for k in li:
        f=k.text
        b=f.split()
        if "Rating:" in b:
            dic["Rating"]=b[1]
        
        elif "Genre:" in b:
            k=b[1:]
            g=" "
            for i in k:
                g+=i
            g=g.strip()
            g=g.split(",")
            
            dic["Genre"]=g
        elif "Language:" in b:
            dic['Language']=b[2]
            # print(dic)     
        elif "Director:" in b:
            w=b[1:]
            h=" "
            i=0
            while i<len(w):
                h=h+w[i]
                i+=1
            l=h.split(",")
            k=" "
            r={}
            l1=[]
            for i in l:
                str1=""
                for j in i:
                    if j!=k:
                        str1+=j
                l1.append(str1)
            dic["Director"]=l1
        elif "Producer:" in b:
            dic["Producer"]=b[1:]
        elif "Runtime:" in b:
            s=b[1:]
            for i in s:
                if "h" in i:
                    first=int(i[0:-1])*60
                elif "m" in i:
                    sec=int(i[:-1])
            dic["Runtime"]=first+sec
    with open("Task4.json","w+") as file:
        json.dump(dic,file,indent = 4)
    return dic
movie_details(url)