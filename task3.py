import json
with open("task2.json","r+") as file:
    a=json.load(file)
def decade(movies):
    dict={}
    list=[]
    for i in movies:
        b=int(i)
        mod=b%10
        dec=b-mod
        if dec not in list:
            list.append(dec)
    list.sort()
    for j in list:
        dict[j]=[]
    for j in dict:
        c=j+9
        for k in movies:
            if int(k)<=c and int(k)>=j:
                for l in movies[k]:
                    dict[j].append(l)
                with open("task3.json","w+") as file:
                    json.dump(dict,file,indent=4)
                    a=json.dumps(dict)
    return dict
print(decade(a))   






