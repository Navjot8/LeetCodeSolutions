s = "is2 sentence4 This1 a3"
num="1234567890"
order=""
l=[""]*len(s.split())
print(l)
sentence=""
for i in s:
    if i in num:
        order+=i
    else:
        sentence+=i
sentence=sentence.split()
print(sentence)
count=0
for i in order:
    l[int(i)-1]=sentence[count]
    count+=1
newSentence=""
for i in l:
    newSentence+=i+" "
print(newSentence[:len(newSentence)-1])