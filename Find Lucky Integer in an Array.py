arr = [1,2,2,3,3,3,4]
dic = {i: arr.count(i) for i in arr}
print(dic)
for key,val in dict(sorted(dic.items(),key=lambda a:(a[1],a[0]),reverse=True)).items():
    if key==val:
        print(key)
