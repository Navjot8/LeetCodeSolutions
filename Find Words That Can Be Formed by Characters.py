words = ["cat","bt","hat","tree"]
chars = "atach"
dic = {}
for i in "".join(words):
    if i not in dic:
        dic[i] = 0
    dic[i] += 1

dic1 = {}
for i in chars:
    if i not in dic1:
        dic1[i] = 0
    dic1[i] += 1

finalCount = 0
for i in words:
    if i[0] in dic1:
        count = 0
        try:
            for k in i:
                if i.count(k) <= dic1[k]:
                    count += 1
        except:
            p=0
        if count == len(i):
            finalCount += len(i)
print(finalCount)
