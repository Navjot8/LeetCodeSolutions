strs = ["eat","tea","tan","ate","nat","bat"]
dic={}
for i in strs:
    key="".join(sorted(list(i)))
    if key not in dic.keys():
        dic[key]=[i]
    else:
        dic[key].append(i)
print(dic)
# {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}